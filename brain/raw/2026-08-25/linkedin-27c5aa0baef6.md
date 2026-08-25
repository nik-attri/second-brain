---
author: Ashrith Balaji Gudla
fetched_at: '2026-08-25T03:40:11.536598Z'
id: 27c5aa0baef6
lane: lead
published: ''
source: linkedin
title: 'A few months ago, I was doing what every job seeker dreads: finding an HR''s
  email, writing "Hi, I hope you''re doing well'
url: https://www.linkedin.com/posts/ashrith-balaji-gudla-5768302a8_work-flow-demo-activity-7497854022243037184-XIYs
---

A few months ago, I was doing what every job seeker dreads: finding an HR's email, writing "Hi, I hope you're doing well...", attaching my resume, hitting send — and repeating that 30-40 times a day.

It was slow, repetitive, and draining energy I needed for interview prep.

So I did what any backend developer would do — I built a system to fix my own problem.

Introducing Referral Hub — a full-stack outreach automation platform I built (and I'm actively using right now) to manage job referral emails at scale, without losing the personal touch.

It started as a learning project around Spring Scheduler and Spring Mail, and grew into a complete campaign-management system.

What it does:

📇 Recruiter CRM — 2000+ contacts with bulk import/export, search, and grouping, plus duplicate-email prevention
✉️ Reusable Templates — Multiple templates with placeholders like {{recruiterName}}, {{roleName}}, {{companyName}} for auto-personalized emails
📎 Resume Attachment — PDFs are validated, stored, and auto-attached via MIME
🚀 Campaigns — Map a template + resume + contact group and launch in one click
⏰ Scheduled Automation — Spring Scheduler runs weekly campaigns on a configurable cron expression
🛡️ Safety Controls — Cooldown periods, eligibility checks, batch limits, and do-not-contact handling
📊 History & Auditing — Every send is logged with status and error details

🧰 Stack: Java 17, Spring Boot, Spring Data JPA/Hibernate, PostgreSQL, Spring Mail (SMTP/MIME), Spring Scheduler | React, Vite, Tailwind | Render + Vercel

The most interesting problem wasn't sending an email — it was keeping the scheduler thin and pushing eligibility, personalization, and delivery tracking into dedicated services, plus learning that a successful SMTP submission doesn't guarantee inbox delivery.

Still in a controlled testing phase (~300 emails/day, batch-limited) while I refine deliverability. Since it's a shared demo, my account has a 300-email/day cap — so if your dispatch doesn't go through right away, it's likely just the daily limit being used up by other testers, not a bug. Try again the next day.

Want to try it? The profile section is fully editable — swap in your own details before running a campaign.

🔗 Live app: https://lnkd.in/dBgK2a66
💻 Frontend: https://lnkd.in/drzzctcm
💻 Backend: https://lnkd.in/dgn3jVh9

If you're a job seeker drowning in manual outreach, or a dev curious about the Spring Boot design — I'd love your thoughts in the comments. Stars appreciated too ⭐

#buildinpublic #springboot #java #backenddevelopment #jobsearch #softwareengineering #reactjs #postgresql #opensource
