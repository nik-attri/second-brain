---
author: Andrei Zaikin
fetched_at: '2026-10-16T07:40:28.966128Z'
id: bc5e5fa1ed3c
lane: lead
published: ''
source: linkedin
title: There is a growing consensus in AI-First engineering circles that humans no
  longer need to read code (or even documentat
url: https://www.linkedin.com/posts/zaikin_there-is-a-growing-consensus-in-ai-first-activity-7516759699980050432-gs1E
---

There is a growing consensus in AI-First engineering circles that humans no longer need to read code (or even documentation). The logic goes: if you don’t understand how something works, just ask your coding agent and it will explain it to you.

I think this is wishful thinking.

To ask an agent the right question, you first need a rough mental model of the territory. You can’t interrogate a system you don’t know exists. Humans still need to read text. The real shift isn't that documentation is dead; it’s that its purpose has fundamentally changed.

When we let coding agents generate documentation unchecked, we get a specific kind of AI slop: jagged documentation.

Because an agent operates within the recency bias of its current task, it tends to obsessively document ephemeral implementation details that were top-of-mind during the session, while glossing over the broader system design. You end up with a 500-word breakdown of a retry helper next to a two-sentence hand-wave about the core data pipeline.

Our organic readers have finite cognitive bandwidth. Every token of low-value implementation detail we force a human to read is a tax on their attention. If we want to protect their cognitive load, our documentation only needs to do two things:
1. Provide a high-level map just clear enough for a human to orient themselves and know what questions to ask the agent next.
2. Capture the "Why"—the business constraints, architectural trade-offs, and rejected alternatives that no agent can ever reverse-engineer from the source code alone.

Everything else (the "what" and the "how") is already in the code. If an agent can read it in two seconds, a human shouldn't have to read it in the docs.

So how do we strip the slop without spending hours manually rewriting markdown files? We can use clean-context sub-agents as documentation auditors:
• The Blind Test: Spin up a sub-agent with a fresh context window and zero access to the documentation. Ask it to explain the module or perform a task using only the source code. Whatever it figures out effortlessly doesn't belong in the docs. Where it stumbles or guesses wrong reveals the exact hidden context you actually need to document.
• The "Right Questions" Check: Feed the draft documentation to another clean sub-agent and ask: "Based only on this text, what architectural questions would a senior engineer ask before modifying this system?" If the doc doesn't spark the right questions, it’s failing as a mental map.

Sub-agents are brilliant at pruning redundancy and stress-testing context. But the final pass still belongs to us. Only human taste can turn a pruned set of facts into a coherent narrative—one that respects the cognitive limits of the person reading it.
