"""The personalization engine. ONE LLM call per batch, and nothing else.

The model's only job is judgment. Fetching, deduping, date-filtering and storing
already happened deterministically in ingest.py.
"""
import glob
import json
import os
import sys
from datetime import datetime

import anthropic
import requests
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = "claude-opus-5"
GEMINI_URL = ("https://generativelanguage.googleapis.com/v1beta/models/"
              "{model}:generateContent")

# Flipped to True the first time Anthropic reports no credit / bad key / rate cap.
# Once we switch, we stay switched for the rest of the run.
_FELL_BACK = [False]

FIELDS = ["id", "lane", "score", "reason", "company", "contact_name",
          "pain_signal", "automation_hypothesis", "hook", "budget_signal", "unlocks"]

SCHEMA = {
    "type": "object",
    "properties": {
        "results": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "lane": {"type": "string", "enum": ["lead", "capability", "cut"]},
                    "score": {"type": "integer"},  # 0-10; bounds enforced by the prompt, not the schema
                    "reason": {"type": "string"},
                    "company": {"type": "string"},
                    "contact_name": {"type": "string"},
                    "pain_signal": {"type": "string"},
                    "automation_hypothesis": {"type": "string"},
                    "hook": {"type": "string"},
                    "budget_signal": {"type": "string"},
                    "unlocks": {"type": "string"},
                },
                "required": FIELDS,
                "additionalProperties": False,
            },
        }
    },
    "required": ["results"],
    "additionalProperties": False,
}


def load_config():
    with open(os.path.join(ROOT, "engine", "config.yaml")) as fh:
        return yaml.safe_load(fh)


def read_item(path):
    with open(path) as fh:
        text = fh.read()
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    meta = yaml.safe_load(parts[1]) or {}
    meta["text"] = parts[2].strip()
    return meta


def load_raw(day):
    paths = sorted(glob.glob(os.path.join(ROOT, "brain", "raw", day, "*.md")))
    return [i for i in (read_item(p) for p in paths) if i]


def chunk(seq, size):
    for start in range(0, len(seq), size):
        yield seq[start:start + size]


INSTRUCTION = ("Score every item below. Return one result per item, using the "
               "exact `id` given. Use empty strings for fields that do not apply.\n\n")


def gemini_schema(node):
    """Gemini takes an OpenAPI subset: uppercase types, no additionalProperties."""
    if not isinstance(node, dict):
        return node
    out = {}
    for key, val in node.items():
        if key == "additionalProperties":
            continue
        if key == "type" and isinstance(val, str):
            out[key] = val.upper()
        elif key == "properties":
            out[key] = dict((k, gemini_schema(v)) for k, v in val.items())
        elif key == "items":
            out[key] = gemini_schema(val)
        else:
            out[key] = val
    return out


def _is_exhausted(err):
    """True only for 'this key can no longer serve requests' conditions."""
    if isinstance(err, (anthropic.AuthenticationError, anthropic.PermissionDeniedError,
                        anthropic.RateLimitError)):
        return True
    if isinstance(err, anthropic.BadRequestError):
        return "credit balance" in str(err).lower()
    return False


def call_anthropic(client, criteria, payload, effort):
    response = client.messages.create(
        model=MODEL,
        max_tokens=16000,
        system=criteria,
        thinking={"type": "adaptive"},
        output_config={"effort": effort, "format": {"type": "json_schema",
                                                    "schema": SCHEMA}},
        messages=[{"role": "user",
                   "content": INSTRUCTION + json.dumps(payload, indent=1)}],
    )
    if response.stop_reason == "refusal":
        print("  ! model declined this batch, skipping")
        return []
    text = next(b.text for b in response.content if b.type == "text")
    return json.loads(text)["results"]


def call_gemini(criteria, payload, model):
    key = os.environ.get("GEMINI_API_KEY", "")
    if not key:
        raise RuntimeError("GEMINI_API_KEY unset — no fallback available")
    resp = requests.post(
        GEMINI_URL.format(model=model),
        headers={"x-goog-api-key": key, "Content-Type": "application/json"},
        json={
            "systemInstruction": {"parts": [{"text": criteria}]},
            "contents": [{"role": "user",
                          "parts": [{"text": INSTRUCTION + json.dumps(payload, indent=1)}]}],
            "generationConfig": {"responseMimeType": "application/json",
                                 "responseSchema": gemini_schema(SCHEMA)},
        },
        timeout=300,
    )
    resp.raise_for_status()
    data = resp.json()
    parts = data["candidates"][0]["content"]["parts"]
    return json.loads("".join(p.get("text", "") for p in parts))["results"]


def score_batch(client, criteria, batch, cfg):
    payload = [{
        "id": i["id"],
        "source": i.get("source", ""),
        "lane_hint": i.get("lane", ""),
        "author": i.get("author", ""),
        "url": i.get("url", ""),
        "text": i.get("text", "")[:4000],
    } for i in batch]

    provider = cfg.get("provider", "auto")
    gem_model = cfg.get("gemini_model", "gemini-2.5-flash")

    if provider == "gemini" or _FELL_BACK[0]:
        return call_gemini(criteria, payload, gem_model)

    try:
        return call_anthropic(client, criteria, payload, cfg["effort"])
    except Exception as err:
        if provider == "auto" and _is_exhausted(err):
            print("  ! Anthropic unavailable (%s) — switching to Gemini %s "
                  "for the rest of this run" % (type(err).__name__, gem_model))
            _FELL_BACK[0] = True
            return call_gemini(criteria, payload, gem_model)
        raise


def write_scored(day, items, results, threshold):
    by_id = dict((i["id"], i) for i in items)
    outdir = os.path.join(ROOT, "brain", "scored", day)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    # Filenames carry the score, so a re-scored item would land in a NEW file and
    # leave its old verdict behind. Clear the day before rewriting it.
    for stale in glob.glob(os.path.join(outdir, "*.md")):
        os.remove(stale)
    kept = []
    for res in results:
        item = by_id.get(res["id"])
        if not item:
            continue
        verdict = "keep" if res["score"] >= threshold else "cut"
        front = {k: res.get(k, "") for k in FIELDS}
        front.update({
            "verdict": verdict,
            "source": item.get("source", ""),
            "url": item.get("url", ""),
            "author": item.get("author", ""),
            "scored_at": datetime.utcnow().isoformat() + "Z",
        })
        name = "%02d-%s-%s.md" % (res["score"], verdict, res["id"])
        with open(os.path.join(outdir, name), "w") as fh:
            fh.write("---\n")
            fh.write(yaml.safe_dump(front, default_flow_style=False,
                                    allow_unicode=True, sort_keys=True))
            fh.write("---\n\n")
            fh.write(item.get("text", "")[:2000] + "\n")
        if verdict == "keep":
            kept.append(front)
    return outdir, kept


def main():
    day = sys.argv[1] if len(sys.argv) > 1 else datetime.utcnow().strftime("%Y-%m-%d")
    cfg = load_config()["settings"]
    items = load_raw(day)
    if not items:
        print("no raw items for %s — run ingest.py first" % day)
        return 1

    with open(os.path.join(ROOT, "engine", "prompts", "scoring.md")) as fh:
        criteria = fh.read()

    client = anthropic.Anthropic()
    results = []
    batches = list(chunk(items, cfg["batch_size"]))
    for num, batch in enumerate(batches, 1):
        print("scoring batch %d/%d (%d items)" % (num, len(batches), len(batch)))
        results += score_batch(client, criteria, batch, cfg)

    outdir, kept = write_scored(day, items, results, cfg["keep_threshold"])
    print("\nBEFORE: %d raw items" % len(items))
    print("AFTER:  %d kept (score >= %d)" % (len(kept), cfg["keep_threshold"]))
    print("-> %s" % outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
