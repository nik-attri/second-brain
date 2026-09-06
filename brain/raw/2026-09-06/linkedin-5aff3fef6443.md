---
author: Aditya Shah
fetched_at: '2026-09-06T07:25:15.513181Z'
id: 5aff3fef6443
lane: lead
published: ''
source: linkedin
title: 'I recently watched an AI coding agent make changes across a codebase and realized
  something uncomfortable:


  AI is gettin'
url: https://www.linkedin.com/posts/adityarshah91_opensource-ai-softwareengineering-activity-7502254593049944065-vRX_
---

I recently watched an AI coding agent make changes across a codebase and realized something uncomfortable:

AI is getting very good at changing code. I'm not sure we're getting equally good at understanding the consequences.

A few files change, the diff looks reasonable, and we review it like any other PR.

But what about the code three or four layers away that depends on what just changed?

That question led me down a rabbit hole  tracing callers, following imports, and trying to reconstruct the blast radius manually.

So I built Semantic Vision.

It turns Python, JavaScript, and TypeScript codebases into an interactive map. You can explore call graphs, run impact analysis to see direct and transitive callers, trace execution flows, inspect complexity, and generate context-aware documentation.

The idea is simple:

Don't just review what changed. Understand what the change affects.

It's open source, runs locally, and there's a live demo you can explore without installing anything: Link in the comments


Curious - how do you currently check the blast radius of an AI-generated change?

#opensource #AI #softwareengineering #developertools
