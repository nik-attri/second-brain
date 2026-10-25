---
author: Vanita S
fetched_at: '2026-10-25T07:55:38.724753Z'
id: ee37e2d2b949
lane: lead
published: ''
source: linkedin
title: 'Meta found that making an AI agent smarter wasn''t the answer. Giving it less
  to do was.


  The original approach was famil'
url: https://www.linkedin.com/posts/vanita-s-703598438_the-thin-orchestrator-how-we-made-our-ai-activity-7520024483311620099-g7WU
---

Meta found that making an AI agent smarter wasn't the answer. Giving it less to do was.

The original approach was familiar: build one powerful agent, give it all the context, and let it figure everything out.
It worked in demos. In production, it hallucinated.

The problem was architectural. The agent had to navigate multiple repositories, programming languages, data sources and pipeline stages. Too much context led it to mix up rules between systems.

Meta's solution was surprisingly simple:
→ A thin orchestrator handles routing, sequencing and reliability checks.
→ 14 specialised agents handle domain-specific reasoning.
→ Deterministic workflow templates define the order of operations.
→ Each agent loads only the knowledge it needs for its task.

The results were striking: preparing a new data column, which previously took 3–4 days manually, could be completed in under an hour with the new system.

And when Meta needed to support another workflow, it could reuse existing agents with a different workflow template rather than build everything from scratch.

The bigger engineering lesson:
A production agent isn't just a model with tools. It's a system with clear boundaries, isolated context, predictable workflows and controlled failure modes.

We spend a lot of time discussing which model is smarter. Perhaps we should spend more time asking whether we're giving the model the right problem to solve.

Source: https://lnkd.in/ddKGm3fy

#AIEngineering #AgenticAI #SoftwareArchitecture
