---
author: Kresimir Furkovic
fetched_at: '2026-09-20T08:03:48.402875Z'
id: c528d76a366d
lane: lead
published: ''
source: linkedin
title: Last week we got ourselves a new kid on the block. His name is Jev, and he
  does not want to have a conversation with you
url: https://www.linkedin.com/posts/kresimirf_last-week-we-got-ourselves-a-new-kid-on-the-activity-7507338579564601344-oATL
---

Last week we got ourselves a new kid on the block. His name is Jev, and he does not want to have a conversation with you. Which, frankly, is a relief.
Jev is a new model architecture, and not a classical LLM. It does not generate tokens, spin up paragraphs, or apologize before giving you an answer. It gives you decisions. Think of Jev as an LLM that can only speak in multiple choice. You hand it context and questions. It hands back choices, scores, yes/no probabilities. 
So what is this good for? Anything where the real work is judgment, not prose. Tagging. MLR review. Quality control. The unglamorous middle layer of pharma content operations where humans currently sit in a room clicking checkboxes until their eyes glaze over.

Your team is tagging content manually? Fine. Take your tag taxonomy and ask Jev which ones apply to a CLM slide. Or go simpler: ask a yes/no question per tag, calibrate a threshold against content you’ve already tagged, and there it is — your auto-tagging engine. No fine-tune, no vector-store séance, no six-month vendor engagement. Questions in, decisions out.

Turn your MLR framework into a series of yes/no questions:
•	Does the document carry the privacy disclaimer?
•	Does an image marked in the Component DAM Library as AI-generated actually carry the AI flag?
•	Is the referenced claim correctly derived from the reference article?
You get the idea. It might take 100 questions. Every “no” gets flagged. And the best part — once Jev tells you where the wheels came off, you point your LLM of choice at those specific failures and ask it to draft the fix. Jev does the judging. The generator does the writing. Nobody pretends to do both badly.

You already built one of these? Maybe you already have a tagging system. An MLR agent. Some clever LangChain thing your team is quietly proud of. You may think you don’t need Jev.
Look at the receipts.
•	Jev: $0.042 per million input tokens. Output is free.
•	Claude Opus 5: $5 per million input, $25 per million output. Cache reads $0.50/M. Batch shaves 50%. And Opus will happily charge you for its own reasoning while it thinks about your slide.
Roughly 390x cheaper. That’s not a discount, but a different pricing category.
Did I mention the speed? Over 100x faster. Jev can review your document in the time Vault takes to render the PDF preview in the reviewer’s browser. Opus performs in seconds, sometimes minutes. Jev performs faster than reviewers inhale when starting a review.

This is not the death of the LLM. A big portion of what we’ve been asking language models to do was never generation at all — it was classification. And now there is a model built for the actual job.

Video source: https://lnkd.in/dH64qHzU
