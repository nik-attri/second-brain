---
author: Rahoul Baruah
fetched_at: '2026-10-13T09:52:45.456081Z'
id: 06527ebe77fe
lane: lead
published: ''
source: linkedin
title: It was February 2026 when I realised that software development had completely
  changed and I essentially stopped writing
url: https://www.linkedin.com/posts/rahoulb_it-was-february-2026-when-i-realised-that-activity-7515704014773207040-TGBC
---

It was February 2026 when I realised that software development had completely changed and I essentially stopped writing code by hand.
Over the next couple of months I changed our Linear statuses and set up a couple of claude code instances, running in tmux, with cron jobs set to deal with various scenarios. The basic idea was “these are the parts of my job that I don’t enjoy, let’s automate them away”.

In particular, I don’t like estimating work and I find code review deathly boring.

So, all through this year, I've been building processes to automate this stuff.  

The previous process was:
- Requests are given by a human but recorded by a clanker
- Estimation and technical design is done by clankers
- Picking what to work on next is manual
- Coding is automated but with me baby-sitting
- Code review is by a clankenmaschine
- Deployment to staging is triggered manually
- Review on staging is human and manual
- Deployment to production is triggered manually

But, as of a couple of weeks ago, I've got the clankers working 24 hours a day: 
- Requests are given by a human but recorded by a clanker
- Estimation and technical is done by a human
- Picking what to work on next is automatic
- Coding is automatic (asking for human advice if needed) and runs in parallel
- Code review is automatic (asking for human advice if needed) and runs in parallel
- Deployment to staging is automatic
- Review on staging is human and manual
- Deployment to production is automatic

In other words, we now put humans at the start and end of the process.

Everything in-between is automated.

Which means that, as long as I keep the schedule filled with tickets, the clankers can work 24 hours a day.
(And yes I do often wake up to 20 notifications asking for decisions on various PRs)

I’m now a sweatshop owner forcing maximum efficiency out of my developers. 24 hour party clankers.
