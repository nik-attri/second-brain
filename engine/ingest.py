"""Deterministic ingestion. No LLM anywhere in this file.

Fetch -> normalize -> dedupe -> write markdown. That's it.
Anything an API answers reliably lives here, never in the model's context.
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timedelta

import feedparser
import requests
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(ROOT, "engine", "state", "seen.json")
APIFY = "https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items"


def load_config():
    with open(os.path.join(ROOT, "engine", "config.yaml")) as fh:
        return yaml.safe_load(fh)


def load_seen():
    try:
        with open(STATE) as fh:
            return json.load(fh)
    except (IOError, ValueError):
        return {}


def save_seen(seen):
    with open(STATE, "w") as fh:
        json.dump(seen, fh, indent=2)


def item_id(url, title):
    return hashlib.sha1((url or title).encode("utf-8")).hexdigest()[:12]


def make_item(source, lane, url, title, author, published, text):
    return {
        "id": item_id(url, title),
        "source": source,
        "lane": lane,
        "url": url or "",
        "title": (title or "").strip()[:200],
        "author": (author or "").strip(),
        "published": published or "",
        "text": (text or "").strip(),
    }


# ── YouTube ──────────────────────────────────────────────────────────────
def resolve_channel_id(handle):
    """@handle -> UC... channel id, by reading the channel page."""
    try:
        resp = requests.get(
            "https://www.youtube.com/" + handle,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=20,
        )
        # Page markup varies by channel; try both shapes.
        for pattern in (r'"channelId":"(UC[\w-]{22})"', r'channel/(UC[\w-]{22})'):
            match = re.search(pattern, resp.text)
            if match:
                return match.group(1)
        return None
    except requests.RequestException:
        return None


def fetch_youtube(cfg):
    items = []
    for handle in cfg.get("handles", []):
        chan = resolve_channel_id(handle)
        if not chan:
            print("  ! could not resolve %s" % handle)
            continue
        feed = feedparser.parse(
            "https://www.youtube.com/feeds/videos.xml?channel_id=" + chan
        )
        for entry in feed.entries:
            summary = ""
            if hasattr(entry, "summary"):
                summary = entry.summary
            items.append(make_item(
                "youtube", "capability", entry.get("link"), entry.get("title"),
                handle, entry.get("published", ""), summary,
            ))
        print("  youtube %s -> %d" % (handle, len(feed.entries)))
    return items


# ── Apify (LinkedIn / Instagram / X) ─────────────────────────────────────
def run_actor(actor, payload, token):
    """Generic Apify actor call. Returns the dataset items as a list."""
    if not actor:
        print("  ! no actor id configured, skipping")
        return []
    try:
        resp = requests.post(
            APIFY.format(actor=actor.replace("/", "~")),
            params={"token": token},
            json=payload,
            timeout=300,
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as err:
        print("  ! apify %s failed: %s" % (actor, err))
        return []


def _first(record, keys, default=""):
    """Pull the first present key. Flattens the {name: ...} objects Apify nests."""
    for key in keys:
        val = record.get(key)
        if isinstance(val, dict):
            val = val.get("name") or val.get("username") or val.get("url")
        if val:
            return val if isinstance(val, str) else str(val)
    return default


TEXT_KEYS = ["content", "text", "postContent", "caption", "description"]
URL_KEYS = ["linkedinUrl", "url", "postUrl", "link", "postLink"]
AUTHOR_KEYS = ["author", "authorName", "profileName", "ownerUsername", "username"]
DATE_KEYS = ["postedAt", "publishedAt", "postedDate", "date", "timestamp"]


def _normalize(rows, source, lane):
    items = []
    for row in rows:
        text = _first(row, TEXT_KEYS)
        posted = _first(row, DATE_KEYS)
        if isinstance(posted, str) and "T" not in posted and len(posted) > 10:
            posted = posted[:10]
        items.append(make_item(
            source, lane, _first(row, URL_KEYS), text[:120],
            _first(row, AUTHOR_KEYS), posted, text,
        ))
    return items


def fetch_linkedin_leads(cfg, token):
    """One run for every query — the actor takes them as an array, so this is
    a single billable run instead of one per keyword."""
    queries = cfg.get("queries", [])
    if not queries:
        return []
    rows = run_actor(cfg.get("actor"), {
        "searchQueries": queries,
        "maxPosts": cfg.get("max_results_per_query", 15),
        "postedLimit": cfg.get("posted_limit", "month"),
        "sortBy": "date",
        "profileScraperMode": "short",
    }, token)
    print("  linkedin leads (%d queries) -> %d posts" % (len(queries), len(rows)))
    return _normalize(rows, "linkedin", "lead")


def fetch_linkedin_authors(cfg, token):
    profiles = cfg.get("profiles", [])
    if not profiles:
        return []
    rows = run_actor(cfg.get("actor"), {
        "authorUrls": ["https://www.linkedin.com/in/" + p for p in profiles],
        "maxPosts": cfg.get("max_results", 20),
        "postedLimit": "month",
        "sortBy": "date",
        "profileScraperMode": "short",
    }, token)
    print("  linkedin capability (%d authors) -> %d posts" % (len(profiles), len(rows)))
    return _normalize(rows, "linkedin", "capability")


def fetch_apify_simple(cfg, token, source, lane, payload):
    items = _normalize(run_actor(cfg.get("actor"), payload, token), source, lane)
    print("  %s/%s -> %d" % (source, lane, len(items)))
    return items


# ── Write ────────────────────────────────────────────────────────────────
def write_raw(items, day):
    outdir = os.path.join(ROOT, "brain", "raw", day)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    for item in items:
        front = dict(item)
        body = front.pop("text")
        front["fetched_at"] = datetime.utcnow().isoformat() + "Z"
        path = os.path.join(outdir, "%s-%s.md" % (item["source"], item["id"]))
        with open(path, "w") as fh:
            fh.write("---\n")
            fh.write(yaml.safe_dump(front, default_flow_style=False,
                                    allow_unicode=True, sort_keys=True))
            fh.write("---\n\n")
            fh.write(body + "\n")
    return outdir


def prefilter(items, cfg):
    """Deterministic gate. Cheap rules run BEFORE any token is spent."""
    settings = cfg["settings"]
    # First run needs history; steady state does not. LOOKBACK_DAYS=90 to backfill.
    lookback = int(os.environ.get("LOOKBACK_DAYS", settings["lookback_days"]))
    cutoff = datetime.utcnow() - timedelta(days=lookback)
    seen = load_seen()
    kept, dropped = [], 0
    for item in items:
        if item["id"] in seen:
            dropped += 1
            continue
        if len(item["text"]) < settings["min_chars"]:
            dropped += 1
            continue
        published = item.get("published", "")[:10]
        if re.match(r"^\d{4}-\d{2}-\d{2}$", published):
            if datetime.strptime(published, "%Y-%m-%d") < cutoff:
                dropped += 1
                continue
        kept.append(item)
        seen[item["id"]] = published or "?"
    save_seen(seen)
    print("prefilter: %d kept, %d dropped (dupe/short/older than %dd)"
          % (len(kept), dropped, lookback))
    return kept


def main():
    cfg = load_config()
    apify_token = os.environ.get("APIFY_TOKEN", "")
    day = datetime.utcnow().strftime("%Y-%m-%d")
    items = []

    print("ingesting %s" % day)
    if cfg["youtube"]["enabled"]:
        items += fetch_youtube(cfg["youtube"])
    if cfg["linkedin_lead_search"]["enabled"]:
        items += fetch_linkedin_leads(cfg["linkedin_lead_search"], apify_token)
    if cfg["linkedin_capability"]["enabled"]:
        items += fetch_linkedin_authors(cfg["linkedin_capability"], apify_token)
    if cfg["instagram_capability"]["enabled"]:
        sub = cfg["instagram_capability"]
        items += fetch_apify_simple(sub, apify_token, "instagram", "capability",
                                    {"directUrls": ["https://instagram.com/" + u
                                                    for u in sub.get("usernames", [])],
                                     "resultsLimit": sub.get("max_results", 20)})
    if cfg["instagram_lead"]["enabled"]:
        sub = cfg["instagram_lead"]
        items += fetch_apify_simple(sub, apify_token, "instagram", "lead",
                                    {"hashtags": sub.get("hashtags", []),
                                     "resultsLimit": sub.get("max_results", 30)})

    print("fetched %d raw items" % len(items))
    items = prefilter(items, cfg)
    outdir = write_raw(items, day)
    print("wrote %d -> %s" % (len(items), outdir))
    return 0 if items else 1


if __name__ == "__main__":
    sys.exit(main())
