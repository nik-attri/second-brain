"""Turn the kept items into the one note actually worth reading."""
import glob
import os
import sys
from datetime import datetime

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_front(path):
    with open(path) as fh:
        parts = fh.read().split("---", 2)
    return yaml.safe_load(parts[1]) or {}


def main():
    day = sys.argv[1] if len(sys.argv) > 1 else datetime.utcnow().strftime("%Y-%m-%d")
    scored = sorted(glob.glob(os.path.join(ROOT, "brain", "scored", day, "*.md")))
    raw = glob.glob(os.path.join(ROOT, "brain", "raw", day, "*.md"))
    fronts = [read_front(p) for p in scored]
    kept = [f for f in fronts if f.get("verdict") == "keep"]
    kept.sort(key=lambda f: -f.get("score", 0))

    outdir = os.path.join(ROOT, "brain", "synth")
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    path = os.path.join(outdir, "%s-digest.md" % day)

    lines = ["# Digest — %s" % day, ""]
    lines.append("**%d in -> %d scored -> %d kept.** Everything below is a draft; "
                 "nothing goes out without a rewrite." % (len(raw), len(fronts), len(kept)))
    lines.append("")

    for lane, heading in (("lead", "## Leads"), ("capability", "## Capability")):
        rows = [f for f in kept if f.get("lane") == lane]
        lines.append(heading + " (%d)" % len(rows))
        lines.append("")
        if not rows:
            lines.append("_Nothing cleared the bar today._")
            lines.append("")
            continue
        for f in rows:
            flag = "" if f.get("verified", True) else "  ⚠️ UNVERIFIED"
            lines.append("### [%d] %s%s" % (
                f.get("score", 0),
                f.get("company") or f.get("author") or "(untitled)", flag))
            lines.append("")
            lines.append("- **Why:** %s" % f.get("reason", ""))
            if lane == "lead":
                lines.append("- **Contact:** %s" % (f.get("contact_name") or "?"))
                lines.append("- **They said:** \"%s\"" % f.get("pain_signal", ""))
                lines.append("- **Build:** %s" % f.get("automation_hypothesis", ""))
                lines.append("- **Budget signal:** %s" % f.get("budget_signal", ""))
                lines.append("- **Hook (DRAFT — rewrite):** %s" % f.get("hook", ""))
            else:
                lines.append("- **Unlocks:** %s" % f.get("unlocks", ""))
            lines.append("- **Source:** %s" % f.get("url", ""))
            lines.append("")

    with open(path, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print("digest -> %s (%d kept)" % (path, len(kept)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
