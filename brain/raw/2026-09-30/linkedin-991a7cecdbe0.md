---
author: TechHive
fetched_at: '2026-09-30T09:08:45.788335Z'
id: 991a7cecdbe0
lane: lead
published: ''
source: linkedin
title: 'Nobody was waiting on the model.

   

  The build took nine weeks anyway, and eight of them had nothing to do with AI.

   

  A ma'
url: https://www.linkedin.com/posts/techhiveteam_nobody-was-waiting-on-the-model-activity-7510981315379458049-oSCe
---

Nobody was waiting on the model.
 
The build took nine weeks anyway, and eight of them had nothing to do with AI.
 
A manufacturing company had a document extraction prototype. It pulled line items, quantities and delivery dates off supplier purchase orders — PDFs, scans, occasionally a photo someone had taken on a phone. An operations analyst had built it herself over a few weekends. It worked, and it was better than the three people doing it manually.
 
It had been stuck for four months.
 
The reason wasn't accuracy. It was that nobody could answer what happens when it's wrong.
 
A wrong quantity on a purchase order becomes a wrong delivery, and a wrong delivery becomes a phone call from a customer. That risk sat with the operations director, and she had no way to see or control it. So she said no, correctly.
 
What we built was mostly the answer to her question.
 
A confidence score per extracted field, not per document — because one bad date in an otherwise clean order is the failure mode that matters. Anything below threshold holds in a review queue. A screen where her team sees the original document beside the extracted values and corrects in place. A weekly report showing what was auto-approved, what was corrected, and where the errors clustered.
 
Roughly three weeks on the review interface, two on integration with their ERP, two on the reporting and controls, two on rollout and training.
 
It's been running eight months. She approved it because she could finally see it, not because the model got better.
 
If your pilot works and won't ship, the blocker is usually a person who can't yet see what they're being asked to sign off.

#AI #AIAgents #CaseStudy #EnterpriseAI #Automation #ProductEngineering
