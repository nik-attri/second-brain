# Source List

Rule from the brief: **real sources only.** A brain fed aspirational sources you never read is dead on arrival.

## Live sources

| Source | What it feeds | Mechanism | Cost | Signal |
|---|---|---|---|---|
| **LinkedIn — post & job search** | SMB decision-makers describing manual work; companies hiring ops/admin roles (a hiring post for a data-entry role *is* an automation lead) | Apify actor, keyword + filter based | ~$1.5/1k | ⭐⭐ **primary** |
| **Instagram — accounts + hashtags** | Agency owners, D2C brands, local service businesses posting about ops chaos | Apify actor | ~$1.5/1k | ⭐ **secondary** |
| **X / Twitter — accounts + search** | Founders venting about manual processes; AI tooling releases | Apify actor | ~$1.5/1k | mixed |
| **YouTube — channel RSS** | Capability lane: what automations to build, how other consultants price and position | RSS (`/feeds/videos.xml`) | free | capability only |

## ⭐ Signal — measured, not guessed (first run, 2026-08-22)

| Source | Ingested | Kept | Verdict |
|---|---|---|---|
| **LinkedIn post search (lead)** | 60 | **2** | ⭐⭐ The only source that produced a lead. Both survived Tavily verification. |
| YouTube (capability) | 60 | 0 | RSS gives only the video *description*, not content. Saraev's are bio boilerplate — the filter scored them 4 and called it: "right person, all bio boilerplate." |
| LinkedIn profile posts (capability) | 0 | 0 | Profile URL wrong; needs the real slug. |
| Instagram | — | — | Actor requires a paid Apify plan (402 on free tier). |

**LinkedIn carries 100% of the signal so far.** That is one run, not a law — but it already
matches the brief's prediction that this list shrinks fast.

> Next cut, on current evidence: YouTube. Not because the channels are bad, but because
> RSS descriptions are too thin to judge. Either pull transcripts or drop it.

## ✂️ Consciously cut

**arXiv / research papers — CUT.**

Reason: papers score high on interest and zero on *"can this person pay me $5K/month in November."* arXiv has no company names, no contacts, no budgets. It's the source that feels productive and converts nothing. Reading it would be a hobby wearing the costume of pipeline work.

Cut date: 2026-08-21. Revisit condition: only if a client engagement requires a technique I can't get from applied sources.

## Needs your input

Fill these in — I can't invent them, and the brief requires sources you actually consume:

```
LINKEDIN
  keywords I'd search for:        ___
  people/companies I follow:      ___

INSTAGRAM
  accounts I actually follow:     ___
  hashtags worth watching:        ___

X / TWITTER
  accounts I actually read:       ___
  searches worth running:         ___

YOUTUBE
  channels I actually watch:      ___
```
