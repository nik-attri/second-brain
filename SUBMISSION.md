# Assignment 2 — Submission

**Sahil Khirsaria · 22 August 2026 · [nik-attri/second-brain](https://github.com/nik-attri/second-brain)**

> **North Star** — Currently a full-time AI engineer at Attri with zero independent
> consulting clients, by **November 2026** I am running an AI automation consulting
> practice with **3 paying SMB clients on $5,000/month retainers** — verifiable by
> **three signed contracts and three months of invoices** — because I want $15,000/month
> of income that is not tied to one job.

**154 ingested → 154 scored → 2 kept → 2 verified.**

---

## 1. North Star statement ✅

| Part | Value |
|---|---|
| Current state | Full-time AI engineer at Attri, zero independent clients, no signed contracts |
| Time-bound goal | 3 clients at $5,000/month, by **30 November 2026** |
| Provable activity | 3 signed contracts + 3 months of invoices, each ≥ $5,000/mo |
| Reason | $15,000/month of income not tied to one job |

**Verifier's test.** A stranger on 1 Dec 2026 asks for three contracts dated on or before
30 Nov 2026, invoices ≥ $5,000/mo each, and payment confirmation for one cycle each.
Three exist → success. Two → failure. No interpretation required.

Full statement and the qualified-client definition: [`00-north-star.md`](00-north-star.md)

## 2. Source list ✅

| Source | Lane | In | Kept | Verdict |
|---|---|---|---|---|
| **LinkedIn post search** (Apify) | lead | 100 | **2** | ⭐⭐ Only source producing leads |
| YouTube (RSS + transcripts) | capability | 54 | 0 | Descriptions are bio boilerplate |
| LinkedIn profile posts | capability | 0 | 0 | Wrong profile slug — known defect |
| Instagram | — | — | — | Actor needs paid Apify plan (402) |

**Three conscious cuts** — arXiv (no contacts, no budgets); the frontier-lab accounts
(Sundar Pichai, Nvidia, Google, DeepMind, ChatGPT, Claude, Dario Amodei, Sam Altman —
they change nothing about whether an SMB signs); Instagram (weak for B2B retainers, and
paid). Reasons in [`01-sources.md`](01-sources.md).

## 3. Second brain folder ✅

154 real markdown items against a bar of 10. `brain/raw/` → `brain/scored/` → `brain/synth/`.
Retrieval is YAML frontmatter plus a score-prefixed filename — no vector store, no chunking,
no RAG, because neither context window nor token budget is close to breaking.

## 4. Personalization engine ✅

- **The filter:** [`engine/prompts/scoring.md`](engine/prompts/scoring.md)
- **The LLM's unedited draft, kept for the diff:** [`engine/prompts/scoring.v0-llm-draft.md`](engine/prompts/scoring.v0-llm-draft.md)
- **Before:** `brain/raw/2026-08-22/` — 113 items
- **After:** `brain/synth/2026-08-22-digest.md` — 2 leads

Score distribution: 86 items at 0 · 22 at 1–3 · 3 at 4–5 · **2 at 6–7**.

Deterministic work (fetch, dedupe, date-filter, store, schedule) is plain Python.
The LLM only scores. Every outbound hook is a draft prefixed *"Draft only — rewrite"*.

## 5. Ingestion mechanism ✅

GitHub Actions, daily 03:00 UTC. Run
[32571015682](https://github.com/nik-attri/second-brain/actions/runs/32571015682)
green in 3m53s, committed its own output. Dedupe state committed back so each run only
ingests what it hasn't seen. Manual fallback: `python engine/run.py`, logged in `logs/`.

---

## Known limitations

- **YouTube transcripts are IP-blocked.** YouTube blocks cloud IPs, so transcripts never
  fetch from Actions. Mitigated with a permanent cache, per-run fetch cap, inter-call
  delay, and abort-on-first-block; backfills over days from a residential IP.
- **Capability lane is empty.** Profile-posts returns nothing; Instagram needs a paid plan.
- **Two leads is a small sample**, and both are recruiter/HR posts needing one
  identification step before outreach. The engine says so in each `reason`.

## What running it taught me

The engine kept Ashwani Kawdiya at **6** while its own reason said *"he's a competitor more
than a client."* I added rule 6 by hand — *anyone already automating the process themselves
is a peer, not a prospect* — and on the next run he scored **0**. The gap between what a
model notices and what it acts on is the whole argument for the hand-edit step.
