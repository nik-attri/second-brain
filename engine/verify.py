"""Verification layer. Fake accounts are the norm, not the exception.

No scraped lead reaches the digest until Tavily can corroborate that the company
and the person actually exist.
"""
import glob
import os
import sys
from datetime import datetime

import requests
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAVILY = "https://api.tavily.com/search"


def tavily(query, key):
    try:
        resp = requests.post(
            TAVILY,
            headers={"Authorization": "Bearer " + key},
            json={"api_key": key, "query": query, "max_results": 3,
                  "search_depth": "basic"},
            timeout=45,
        )
        resp.raise_for_status()
        return resp.json().get("results", [])
    except requests.RequestException as err:
        print("  ! tavily failed for %r: %s" % (query, err))
        return []


def split(path):
    with open(path) as fh:
        parts = fh.read().split("---", 2)
    return (yaml.safe_load(parts[1]) or {}), parts[2] if len(parts) > 2 else ""


def main():
    day = sys.argv[1] if len(sys.argv) > 1 else datetime.utcnow().strftime("%Y-%m-%d")
    key = os.environ.get("TAVILY_API_KEY", "")
    if not key:
        print("TAVILY_API_KEY unset — skipping verification (leads stay unverified)")
        return 0

    checked = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "brain", "scored", day, "*.md"))):
        front, body = split(path)
        if front.get("verdict") != "keep" or front.get("lane") != "lead":
            continue
        company = (front.get("company") or "").strip()
        person = (front.get("contact_name") or "").strip()
        if not company:
            front["verified"] = False
            front["verify_note"] = "no company name to check"
        else:
            hits = tavily((company + " " + person).strip(), key)
            front["verified"] = len(hits) > 0
            front["verify_note"] = hits[0]["url"] if hits else "no corroborating result"
        front["verified_at"] = datetime.utcnow().isoformat() + "Z"
        with open(path, "w") as fh:
            fh.write("---\n")
            fh.write(yaml.safe_dump(front, default_flow_style=False,
                                    allow_unicode=True, sort_keys=True))
            fh.write("---" + body)
        checked += 1
        print("  %s %s -> %s" % (
            "OK " if front["verified"] else "?? ", company or "(unnamed)",
            front["verify_note"]))
    print("verified %d leads" % checked)
    return 0


if __name__ == "__main__":
    sys.exit(main())
