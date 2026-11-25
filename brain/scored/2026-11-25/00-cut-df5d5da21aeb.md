---
author: Milind Patel
automation_hypothesis: ''
budget_signal: ''
company: ''
contact_name: Milind Patel
hook: ''
id: df5d5da21aeb
lane: cut
pain_signal: ''
reason: Author describes an LLM spending gateway that his engineering team has already
  built internally.
score: 0
scored_at: '2026-11-25T11:54:57.687088Z'
source: linkedin
unlocks: ''
url: https://www.linkedin.com/posts/patelmilind_we-keep-asking-our-engineering-teams-to-activity-7531319638194937856-n-75
verdict: cut
---

We keep asking our 
engineering teams to innovate.
But how much of their time are we 
actually giving them to do it?

I've been looking at this 
from another angle.

How much engineering effort 
goes into keeping the systems 
we've already built under control?

Our work on LLM spending 
is a good example.

When one team runs 
a proof of concept, 
keeping track of usage 
seems straightforward.

Then another team starts one.

And another.

Now you've got different models, different token usage, and a monthly bill that doesn't clearly tell you which project drove the cost.

So I started breaking down 
what needed to change.

Why were we relying 
on someone checking 
an invoice after the money 
had already been spent?

Could we make this 
part of the platform instead?

We started by putting LLM calls 
through a common gateway.

Every request could now 
be tagged with the team, 
project and model.

At least we could see 
where the spending 
was coming from.

But seeing the problem 
wasn't enough.

So we added token budgets 
at organisation, project 
and model level.

Then we looked at what 
should happen when a project 
approached its limit.

Stopping it immediately 
would only create another 
problem for the team.

So we added alerts first.

If usage kept rising, 
requests could be queued 
or moved to a cheaper model.

Only at the hard limit 
would they be blocked.

There was another thing 
I didn't want us to miss.

What happens when someone 
forgets to configure a budget 
for a new service?

We'd be back where we started.

So we kept the budget policies 
in code and made them part 
of the deployment checks.

No budget policy, 
no deployment.

Once these guardrails were in place, 
I saw an incremental 10% saving 
in AI spend month on month.

But the part I found more interesting 
was the change in how we operated.

Instead of discovering the problem 
at the end of the month, 
the platform had controls 
built into it.

And it made me question 
how much other recurring w
