---
author: Mojolaoluwa Ajayi
fetched_at: '2026-08-31T09:04:05.509645Z'
id: 464583b95d6a
lane: lead
published: ''
source: linkedin
title: Mojola, what did you do at work today? Well, we built two AI agents at work,
  and then we made them talk to each other.
url: https://www.linkedin.com/posts/mojolaoluwa-ajayi-b14937270_mojola-what-did-you-do-at-work-today-well-activity-7500108640520011776-b2bj
---

Mojola, what did you do at work today? Well, we built two AI agents at work, and then we made them talk to each other.

As you may know, I work in the product operations team at Lendsqr.
Customer support at a fintech isn't simple. When something goes wrong, resolving an issue involves many moving parts: receiving the complaint, reassuring the customer, digging into data, diagnosing root causes, and routing fixes, all while new tickets pile up.

That was the reality before we started building.

Phase 1: Dara 
We first built Dara, our level-one support agent. Her job is to handle the initial tier of customer issues.

When an issue comes in, Dara runs preliminary checks, fetches customer data, and summarizes her findings into a clean handoff. What used to take a human agent multiple tools, manual data pulls, and time-consuming drafting, Dara does instantly.

Phase 2: AMAH 
Once Dara handled the surface layer, we tackled the deeper investigations: reading logs, checking codebase behavior, and finding actual root causes.
Enter AMAH, "Ask Me Anything Honestly" (Adedeji Olowe still thinks we need a better name, suggestions welcome 😂).

AMAH performs the log- and code-level technical analysis that used to force engineers to context-switch and dig in manually. Escalations transformed from "here's the complaint" to "here’s the complaint, the customer data, and the exact system-level cause."

Phase 3: The Conversation 
With both agents active, the next question was obvious: Why aren't they talking to each other?

So we connected them.

Now, when Dara encounters a ticket requiring technical analysis, she hands it straight to AMAH. AMAH queries the database, inspects the logs, and diagnoses the root cause.

If it’s a bug: AMAH provides the resolution steps for engineering.

If it’s user error: AMAH explains the situation and drafts the exact response for Dara to send back to the customer.

Seeing this live workflow run end-to-end was incredible.

Is it perfect? No. We’re still calibrating edge cases and refining outputs. But the direction is clear: multi-touch, manual back-and-forth has been replaced by a two-agent conversation that resolves tickets in a fraction of the time.

Big shoutouts to my colleagues who spearheaded their creation: Feranmi Orekoya and Timilehin Adejoro.

We’re nowhere near done, but the future is already running in production.

Drop your name ideas for AMAH in the comments! 🙃
