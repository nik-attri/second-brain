---
author: Ongkarak Kanchanakamol
fetched_at: '2026-09-25T08:20:01.809435Z'
id: ab98c5ed1e07
lane: lead
published: ''
source: linkedin
title: 'We removed an automation feature. The OT process got better.

  For the past few months I''ve been building a Time Attendanc'
url: https://www.linkedin.com/posts/ongkarak-kanchanakamol_how-we-redesigned-ot-approval-activity-7509159233922445312-d61r
---

We removed an automation feature. The OT process got better.
For the past few months I've been building a Time Attendance & Workforce Management system for our agro-industrial plants. One of the most sensitive pieces is overtime. Every OT hour is real money, and every mistake shows up on someone's payslip.
This week we sat down with the HR teams from two factories and redesigned the whole OT claim flow in 70 minutes. Here's what we landed on.
1️⃣ One document, two moments of truth
An OT request is a single document that gets checked twice:
Before the work: the employee requests OT, then their supervisor (Tier 1) and manager (Tier 2) approve the plan. Once approved, the OT appears on the weekly work plan automatically.
After the work: the same document comes back for payment confirmation. Nobody has to fill in a second form.
2️⃣ The system routes by time, not by people remembering
One hour after the planned OT ends, the document moves to the manager on its own. Nobody needs to "send it for claim" at month-end anymore.
3️⃣ Evidence, not guesswork
The manager sees three things side by side: the approved OT window, the actual fingerprint scans, and the hours the system calculated. Anything unusual gets a flag: missed scans, in-only or out-only scans, working more or less than requested, and requests filed after the fact.
The manager then picks one of three actions: confirm, approve with corrected hours (never above the approved plan, with a mandatory reason), or reject.
4️⃣ The payroll gate belongs to each plant's HR
Confirmed claims land in each factory's HR inbox. HR can tick individual claims or approve everything in one click, then print the signed documents and export to Excel for Accounting. The head of HR can act across all plants.
The part I found most interesting:
Our previous version auto-approved any claim where the scans matched the plan. It was efficient, but HR asked us to remove it. Their reasoning was simple: someone accountable should look at every payment, even the normal ones.
So the system no longer decides. It prepares the evidence and highlights what looks off, and a person makes the call. Approving a normal claim takes about three seconds, and the accountability stays with a human.
Lessons I'm taking forward
Automate the routing and the evidence gathering, not the judgment.
A 70-minute meeting with the people who actually close payroll beat weeks of guessing.
Every document should read the same on paper, on screen, and in the Excel export.
Still iterating. Next up is cleaning scanner-ID mappings so every flag reflects reality rather than data gaps.
How do you balance automation and accountability in approval workflows? I'd love to hear what's worked for you.
#WorkforceManagement #HRTech #ProcessDesign #DataEngineering #DigitalTransformation #Manufacturing
