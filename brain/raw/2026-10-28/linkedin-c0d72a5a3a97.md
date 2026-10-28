---
author: Daniel Fuster
fetched_at: '2026-10-28T09:07:49.054382Z'
id: c0d72a5a3a97
lane: lead
published: ''
source: linkedin
title: 'I built an automation that watches the USD/NGN rate so I don’t have to. 💱

  If you earn in dollars, import goods, or pay f'
url: https://www.linkedin.com/posts/daniel-fuster-75aa44343_n8n-automation-nocode-activity-7521121153357336576-dn24
---

I built an automation that watches the USD/NGN rate so I don’t have to. 💱
If you earn in dollars, import goods, or pay for foreign tools, you know the habit: opening a rate site five times a day and hoping you catch a good moment to convert.
So I replaced the habit with a rule. I built it in n8n:
1️⃣ Every morning at 9:00, n8n pulls the latest USD/NGN rate from a free exchange-rate API.
2️⃣ It cleans the data and compares it to my target rate.
3️⃣ If the rate hits my target, a Slack alert goes out right away, and 
4️⃣ Every day, alert or not, the rate is logged to Google Sheets, so I’m building a rate history. I can chart and review
What I practiced building this:
→ HTTP Request with retry-on-fail, so a brief API outage doesn’t break the run
→ Cleaning API data with the Edit Fields node
→ Conditional logic with the If node
→ Parallel branches, so logging and alerting run independently
Lesson from the build: I first set the if condition to “is equal to.” A rate will almost never exactly equal a target, so it never fired. Switching to “less than or equal to” fixed it. Small operator, big difference. Testing with real data catches things like this.
The same pattern works for any pair, any threshold, any channel: importers timing payments, freelancers timing wthreshold, andithdrawals, finance teams tracking exposure.
I’m sharing each build as I go. If you’re drowning in manual checking or reporting, I’d love to hear what you’d automate first.
#n8n #automation #nocode #workflowautomation #freelance
