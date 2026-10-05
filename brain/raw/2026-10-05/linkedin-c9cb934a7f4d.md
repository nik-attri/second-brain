---
author: Evgheni Voitovetchi
fetched_at: '2026-10-05T09:48:27.491250Z'
id: c9cb934a7f4d
lane: lead
published: ''
source: linkedin
title: 'AI testing AI is no longer just an idea.

  It is already becoming part of real AI products.

  And this creates an interestin'
url: https://www.linkedin.com/posts/evgheni-voitovetchi_ai-aiagents-langchain-activity-7512800925267300353-9Non
---

AI testing AI is no longer just an idea.
It is already becoming part of real AI products.
And this creates an interesting question:
Who tests the AI agent?
If a product has thousands of agent sessions every day, a team cannot check all of them manually.
The answer can be: another AI.
LangChain recently added Jev to LangSmith Evals.
Jev is a decision model made for evaluation tasks.
It does not need to generate long text. It can make simple structured decisions:
Did the agent complete the task?
Did it use the right tool?
Did it follow the rules?
Was the execution path good enough?
And this is already practical.
In one early LangChain test, Jev evaluated one case in about 0.44 seconds and cost around $0.00035 per evaluation.
LangChain says this is only an early test, not a general benchmark.
But the main point is more interesting:
AI checking another AI is already becoming a real development tool.
We now have different levels of agent testing:
Code checks
→ simple and deterministic rules
LLM-as-a-Judge
→ quality and semantic checks
Jev / decision models
→ fast structured evaluation
Agent-as-a-Judge
→ complex cases where the evaluator needs to inspect the full trace
For a product, the QA loop can look like this:
Production Agent → Traces → Automatic Evaluation → Suspicious Sessions → Human Review → Fix → Regression Test
The main value here is scale.
A team cannot manually review 10,000 agent sessions.
But automated evaluators can check production sessions and send only risky or unusual cases to people.
They can also find silent failures.
For example, an agent can tell the user:
“Your refund has been processed.”
The answer looks correct.
But the refund tool may actually fail.
So a good evaluation system should check not only what the agent said, but also what really happened.
This changes AI product QA.
As agents become more autonomous, testing also needs to become more automatic.
Not to replace people.
But to use human review only where it is really needed.
AI agents do the work.
AI evaluators check how well they do it.
#AI #AIAgents #LangChain #LangSmith #AIEngineering #AgenticAI #ProductDevelopment
