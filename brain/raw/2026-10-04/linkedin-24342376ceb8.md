---
author: Will Pham
fetched_at: '2026-10-04T08:58:41.103108Z'
id: 24342376ceb8
lane: lead
published: ''
source: linkedin
title: 'A reminder isn''t a system.


  Your gas, EICR and EPC certificates need one that acts.


  Here''s how I''d build it.


  A while b'
url: https://www.linkedin.com/posts/will-pham_a-reminder-isnt-a-system-your-gas-eicr-activity-7512108402752376832-k9tJ
---

A reminder isn't a system.

Your gas, EICR and EPC certificates need one that acts.

Here's how I'd build it.

A while back I was on a call with a board member at a big real estate franchise, and he said something that kind of stuck with me.

"If you can identify a problem that people hate dealing with, bores the hell out of them... you solve that problem, you're on a winner."

Compliance is pretty much that problem.

Goodlord surveyed 2,650 agents and 63% said compliance limits their business.

Only 14% plan to invest in fixing it.

From what I've seen, most setups are a spreadsheet or a calendar reminder.

Which works, as long as someone actually acts on it in a busy week.

A reminder tells someone.

A system does the next step.

Here’s how I would design a system for this:

𝗦𝘁𝗲𝗽 𝟬: Get every expiry date into one table, one row per certificate per property.
An AI step reads the date straight out of the certificate PDF, and a human checks it once.
Honestly this is the step most people skip, and it's the one everything else depends on.

𝟲𝟬 𝗱𝗮𝘆𝘀 𝗼𝘂𝘁: The system emails your contractors asking for quotes and availability.
Nobody has to remember to do it.

𝟯𝟬 𝗱𝗮𝘆𝘀 𝗼𝘂𝘁: It messages the tenant for access dates, books the visit with whichever contractor came back, and lets the landlord know it's booked.

𝟭𝟰 𝗱𝗮𝘆𝘀 𝗼𝘂𝘁, 𝗻𝗼𝘁𝗵𝗶𝗻𝗴 𝗯𝗼𝗼𝗸𝗲𝗱: It escalates to a named person on your team.
Not "the team." One person.

𝗗𝗼𝗻𝗲: The new certificate gets filed against the property and the next expiry date is set automatically.
Gas resets to 12 months, EICR to 5 years, EPC to 10.

Same engine for all three.

It's simpler than it sounds.

I'd run it in n8n on top of an Airtable base, with one scheduled check every morning that looks at days-to-expiry and fires whichever stage applies.

𝗪𝗵𝗲𝗿𝗲 𝗶𝘁 𝗯𝗿𝗲𝗮𝗸𝘀 (𝗯𝗲𝗰𝗮𝘂𝘀𝗲 𝗶𝘁 𝘄𝗶𝗹𝗹)

→ 𝗗𝗮𝘁𝗲𝘀 𝗯𝘂𝗿𝗶𝗲𝗱 𝗶𝗻 𝗣𝗗𝗙𝘀: They're sitting in someone's inbox. That's why step 0 matters more than the rest.

→ 𝗧𝗲𝗻𝗮𝗻𝘁𝘀 𝘄𝗵𝗼 𝗱𝗼𝗻'𝘁 𝗿𝗲𝗽𝗹𝘆: Re-ask after a couple of days, then flag it to a human.

→ 𝗖𝗼𝗻𝘁𝗿𝗮𝗰𝘁𝗼𝗿𝘀 𝘄𝗵𝗼 𝗴𝗼 𝗾𝘂𝗶𝗲𝘁: After 48 hours, it falls back to a second contractor automatically.

None of this is complicated on its own.

It's just that a person doing it manually forgets, gets busy, or is off sick.

The system doesn't.

If your certificates still live in inboxes and spreadsheets, message me and I'll show you what this would look like on your portfolio.
