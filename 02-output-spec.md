# Output Spec

Derived from the North Star the way the lecture derived `name, contact, description` for the consultant.

**If this output would help everyone, it helps no one.** This one is useless to anyone who isn't selling AI automation to 10–200-person companies.

## The output

Every item the engine keeps becomes one record with a `lane`:

### Lane 1 — `lead` (primary)

| Field | Meaning |
|---|---|
| `company` | Company name |
| `size_estimate` | Employee count, or best inference |
| `contact_name` | Named decision-maker (founder / COO / Head of Ops) |
| `contact_path` | Where I can reach them (profile URL, email if public) |
| `pain_signal` | **Verbatim quote** of the thing they said that indicates automation need |
| `automation_hypothesis` | The specific automation I'd propose — one sentence |
| `hook` | Opening line for outreach, referencing their words not mine |
| `budget_signal` | Evidence they can pay $5K/mo (SaaS stack, hiring, funding, revenue) |
| `verified` | Tavily check: is this a real company with a real person? |
| `score` | 0–10 against the North Star |

### Lane 2 — `capability` (secondary)

| Field | Meaning |
|---|---|
| `what` | The technique, tool, or positioning insight |
| `unlocks` | Which automation this lets me sell that I couldn't before |
| `score` | 0–10 |

Anything that is neither a lead nor a capability is **cut**. News, opinion, model releases I can't sell, and general AI discourse all score 0.

## Why two lanes and not one

A consulting practice needs pipeline *and* the ability to deliver. LinkedIn and Instagram feed lane 1. YouTube and X feed lane 2. Lane 1 is primary — if the engine returns zero leads in a week, that week failed regardless of how many capabilities it found.

## Human review gate

Per the brief: **no AI slop goes out.** The engine produces `hook` as a *draft*. Nothing is sent without me rewriting it. The engine buys clarity and speed, not permission to spam.
