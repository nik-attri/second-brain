---
author: Andrej Kaurin
fetched_at: '2026-09-21T08:21:43.786347Z'
id: c9e030bee5ab
lane: lead
published: ''
source: linkedin
title: 'OpenAI didn''t just automate coding. It automated the entire dev pipeline.


  Gergely Orosz''s report on OpenAI''s Codex-driv'
url: https://www.linkedin.com/posts/andrejkaurin_softwareengineering-ai-codex-activity-7507708971412078592-GRdo
---

OpenAI didn't just automate coding. It automated the entire dev pipeline.

Gergely Orosz's report on OpenAI's Codex-driven workflow makes one thing clear: the bottleneck was never writing code. It was everything around it.

→ The loop
↳ A human sets a goal, Codex pulls context from Git, GitHub, Slack, Notion, Databricks, Datadog
↳ Codex implements the change and pushes the PR toward green
↳ Domain-specialist agents review through different lenses
↳ A risk classifier decides who needs to approve, and how strictly

→ The other end of the loop
↳ Perf Factory de-duplicates alerts and root-causes latency regressions
↳ It dispatches agents to propose fixes before humans notice
↳ Sevbot assists incidents but still can't mitigate on its own

→ Why this matters
✅ Non-engineering Codex adoption hit ~90% in four months
✅ PR volume drove a ~10x rise in CI load in six months
🚫 Most teams still measure AI success by lines of code generated

My take: the real constraint has shifted from "can AI write this?" to "can our review, CI, and risk systems absorb the output?" OpenAI didn't win by giving everyone a smarter autocomplete. It won by rebuilding governance, routing, and infrastructure around the agent.

If you're rolling out AI coding tools without rethinking your CI/CD and review process, you're building a faster car with the same tiny bridge.

What's the actual bottleneck in your engineering org right now: code generation, or everything downstream of it?

#SoftwareEngineering #AI #Codex #DevOps #EngineeringLeadership
