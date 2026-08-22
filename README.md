# Second Brain

A folder that filters the internet against one goal.

**North Star:** 3 paying SMB clients on $5,000/month retainers by November 2026.
Full statement and verification test in [`00-north-star.md`](00-north-star.md).

## How it works

```
sources ──> ingest.py ──> brain/raw/ ──> score.py ──> brain/scored/ ──> synthesize.py ──> brain/synth/
            deterministic              ONE llm call              deterministic
            (no LLM)                   (judgment only)           (+ verify.py / Tavily)
```

Everything an API answers reliably — fetching, deduping, date-filtering, storing,
scheduling — is plain Python. The model's only job is scoring each item against the
North Star. Nothing is loaded into a context window that a `grep` could have answered.

**Retrieval strategy:** markdown files, YAML frontmatter as the index, filename prefixed
with the score. No vector store, no chunking, no RAG — the corpus fits in a context
window and the token budget is nowhere near breaking. Escalate only when one of those
two things stops being true.

## Layout

| Path | What |
|---|---|
| `00-north-star.md` | The goal, its four parts, and the verifier's test |
| `01-sources.md` | Every source, signal marks, and what was cut |
| `02-output-spec.md` | The two output lanes |
| `engine/config.yaml` | **Edit this** — which accounts and searches to watch |
| `engine/prompts/scoring.md` | **Edit this** — the filter itself |
| `engine/prompts/scoring.v0-llm-draft.md` | The LLM's unedited first draft, kept for the diff |
| `brain/raw/<date>/` | Everything ingested — the "before" |
| `brain/scored/<date>/` | Every item with a score and a reason |
| `brain/synth/<date>-digest.md` | The digest — the "after" |
| `logs/` | Dated proof each run happened |

## Running it

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then fill in your keys
set -a && source .env && set +a
python engine/run.py
```

Individual stages take an optional date: `python engine/score.py 2026-08-21`.

Automated daily via `.github/workflows/ingest.yml`. If the cron dies, the same command
run by hand once a week is a valid fallback — the logs record either way.

## Cost

| Service | What for | Cost |
|---|---|---|
| Anthropic (`claude-opus-5`) | Scoring — primary | ~$0.20/day at ~60 items |
| Google (`gemini-3.6-flash`) | Scoring — fallback | free tier |
| Apify | LinkedIn / Instagram | ~$1.50 per 1,000 results |
| Tavily | Lead verification | Free tier: 1,000 credits/month |

## Provider fallback

`settings.provider` in `config.yaml`:

- `auto` (default) — score on Claude; switch to Gemini **only** on credit-exhausted,
  bad-key, or rate-limit errors, then stay switched for the rest of the run.
- `anthropic` / `gemini` — force one.

A schema or parameter error still raises loudly. The fallback covers "this key can no
longer serve requests", not "this request was wrong" — otherwise a real bug would hide
behind a silent provider switch. Both paths are tested against the same JSON schema, so
output is identical in shape regardless of who scored it.

`gemini-3.7-flash` is listed by the API but returns 503; `3.6-flash` is the pinned choice.

## The rule this whole thing exists to protect

The engine drafts. It never sends. Every `hook` is a starting point for a human rewrite.
No AI slop leaves this folder.
