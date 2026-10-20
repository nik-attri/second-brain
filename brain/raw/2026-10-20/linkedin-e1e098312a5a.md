---
author: Sergej Koščejev
fetched_at: '2026-10-20T08:01:46.116884Z'
id: e1e098312a5a
lane: lead
published: ''
source: linkedin
title: 'Automating PR reviews


  I’m back from LangDev 2026 where I presented mops. Other tools to make MPS accessible
  to agents g'
url: https://www.linkedin.com/posts/sergejkoscejev_automating-pr-reviews-im-back-from-langdev-activity-7518211536226562048-oqrl
---

Automating PR reviews

I’m back from LangDev 2026 where I presented mops. Other tools to make MPS accessible to agents generally take the form of MCP plugins and are designed for pair-programming with an agent. mops, on the other hand, makes it possible to give agents autonomous tasks and fire off several agents running on separate worktrees or separate repositories using various MPS versions. To make use of this new capability, I have long wanted to build some sort of automation to review pull requests on MPS-extensions. I am pleased to report that it is taking shape, though not exactly in the form that I envisioned.

I was originally thinking that I would build some kind of autonomous workflow using codex exec or claude -p – these ways of invoking Codex or Claude let you give the agent a single prompt, have it work on something, and exit once done. The obstacle to setting this up turned out to be technical as well as financial: the automation setups I looked at would have required API billing and looked too complicated.

Around the same time, I noticed that Matt Pocock had published a new skill, chief-of-staff, that also reminded me of the efforts I reported previously where I started using long-running agent sessions for managing long-term efforts. This is probably not as efficient as starting a new session for each new task (because coming back after a long break means the cache has expired and the LLM has to reprocess the complete input from the beginning) but so far my subscription limits were enough for this, and being able to come back and pick up where I left off without having to reexplain everything to the agent has been very valuable. Thus, I decided to take a similar approach and started a new session with the chief-of-staff skill:

/chief-of-staff In this long-running conversation I want to continuously monitor MPS-extensions for new pull requests and review them on this computer in a worktree, using mops. Exclude cascading merge PRs from reviews. At first, we should automate the initial repo/worktree and mops wrapper setup (including full build), these automations should not be part of MPS-extensions but a separate repo. Suggest improvements to mops and skills. Reviewers shouldn’t need to run tests because the CI already does it.
Do not comment on PRs, present review findings to me for approval first.
Flag any issues.
Make sure to use appropriate agent/effort levels so that we don’t burn our usage limits unnecessarily.
Restate what I want you to do in your own words before continuing.

This has worked out quite well: the agent starts reviews automatically, and presents me with the findings that I can look at and either approve for posting or ask the agent to dig deeper into something. You can see a few instances of “my lawyeragent talking to your lawyeragent” in PR #1910 where Sascha Lißon has been working on adding view models

(truncated by LinkedIn, for the full version with links and formatting see Email archive on my website)
