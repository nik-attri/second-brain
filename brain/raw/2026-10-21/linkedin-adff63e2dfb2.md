---
author: Zain Aldeen Fayod
fetched_at: '2026-10-21T08:06:52.695933Z'
id: adff63e2dfb2
lane: lead
published: ''
source: linkedin
title: '#Zain_lesson_14

  Post 15/17: Resilience Engineering, Surviving Downstream Disastera.


  In #Zain_lesson_13 we used CQRS to'
url: https://www.linkedin.com/posts/zainaldeenfayod_zainabrlessonabr14-zainabrlessonabr13-activity-7518566508709707777-plzs
---

#Zain_lesson_14
Post 15/17: Resilience Engineering, Surviving Downstream Disastera.

In #Zain_lesson_13 we used CQRS to break the query bottleneck, and our system now runs background workers, read projections, and async workflows.

Then reality hits:
A payment gateway times out or inventory DB spikes in connections
What does standard code do? 
It retries IMMEDIATELY! 
And that turns a normal behavior into a disaster
**Self-inflicted kind of DDoS**

Welcome to the thundering herd problem!
The Anti-Pattern: Blind Retries

So imagine 509 checkout calls hit your API while the payment provider struggles:
1- All 500 fail
2- All 500 retry immediately!
3- The provider gets slammed with 1000 requests, then 1500 requests and so on!

Here the retries didn't help you to recover, it DDoS into total collapse!

The production Toolkit
1- Exponential Backoff with Jitter:
Never retry on fixed intervals, exponential Backoff doubles delays: 100ms -> 200ms -> 400ms
Crucially add random Jitter:
backoff time = (2^ attempt * base) + random(0, 200ms)

Jitter decorrelates calls, so instead of 500 pods hitting downstream in sync, the traffic spreads smoothly across time.

2- Circuit Breaker
If a dependency is down for any reason, Stop calling it!
Wrap outbound network calls in a Circuit Breaker as following:
. CLOSED: it means the dependency is healthy and the traffic flows normally.

. OPEN: it means the error rate reaches threshold (like 50% over 10 seconds. So the breaker trips, calls fail FAST without hitting the network, protecting threads.

. HALF-OPEN: it means after a cooldown time allow small probe through, if it succeeds close the circuit if not trip open again.


3- Dead Letter Queues (DLQs)
Never retry indefinitely, set a hard limit (3-5 attempts) and if an event still fails route it to a DLQ:
. Preserve payload for auditing.
. Unblock main consumer queues
. Alerts on-call for manual review or replying once the outage clears
That solved the issues of cascading outages under network strain.
The new problem:
With 10+ services, outbox relays and DLQs..
When a user says: “My card was charged but the order is still pending “
How do you trace that request across 6 databases and brokers without drowning in the logs?

This is what we will know in the next lesson.
Next up:
In Post 16, we will cover Distributed Observability:
OpenTelemetry, Tracing and Correlation IDs.
