---
author: Hardik Shah
fetched_at: '2026-10-31T09:04:14.179149Z'
id: fca619a11f9d
lane: lead
published: ''
source: linkedin
title: 'Many teams struggle to answer this question.


  Traditional software can be unit tested, integration tested and regression'
url: https://www.linkedin.com/posts/hardikshah97_aiengineering-llmops-generativeai-activity-7522207176569069568-hSPd
---

Many teams struggle to answer this question.

Traditional software can be unit tested, integration tested and regression tested.

However, with AI functionality there is a challenge of stochastic outputs, meaning that sometimes you can get better sounding responses which may not be as accurate.

𝗟𝗟𝗠 𝗘𝘃𝗮𝗹𝘂𝗮𝘁𝗶𝗼𝗻𝘀 (𝗘𝘃𝗮𝗹𝘀) 𝗵𝗲𝗹𝗽 𝗵𝗲𝗿𝗲.

I would recommend at least having the following in place before sending prompt/model changes to production.

✔ 𝗚𝗼𝗹𝗱𝗲𝗻 𝗱𝗮𝘁𝗮𝘀𝗲𝘁

Start with a small set of real-world examples with expected behaviour/reference answers.

✔ 𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗲𝗱 𝘃𝗮𝗹𝗶𝗱𝗮𝘁𝗶𝗼𝗻

Validate that the output has the right structure, citations, conforms to a schema and doesn’t contain any banned content.

✔ 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝘀𝗰𝗼𝗿𝗶𝗻𝗴

Add an LLM judge to score your outputs on how relevant, accurate and complete they are. This should be calibrated with human reviews.

✔ 𝗥𝗲𝗴𝗿𝗲𝘀𝘀𝗶𝗼𝗻 𝗴𝗮𝘁𝗲

Set up evaluations to run in CI. Whenever prompts, models or retrieval logic change run evaluations. If quality falls below an acceptable level then we should flag/block releases.

✔ 𝗣𝗿𝗼𝗱𝘂𝗰𝘁𝗶𝗼𝗻 𝗾𝘂𝗮𝗹𝗶𝘁𝘆 𝗺𝗼𝗻𝗶𝘁𝗼𝗿𝗶𝗻𝗴

Every week sample some real examples and review failures. This will show us any new edge cases and improve our evaluation dataset. Never evaluate quality alone.

We should always be tracking the following metrics:

𝗤𝘂𝗮𝗹𝗶𝘁𝘆 – Does it provide useful and correct answers?

𝗟𝗮𝘁𝗲𝗻𝗰𝘆 – How long does it take to respond?

𝗖𝗼𝘀𝘁 – How expensive is each successful request?

It may not be worth it if your outputs are marginally better but 4x more expensive. This will be down to product and business decisions.

Remember that LLM judges can also be biased so human reviews are still vital.

The aim is to understand whether your AI system is improving.

How do you currently evaluate your prompt changes? Manually or through automated evaluations? Or have you got it integrated into your CI?

#AIEngineering #LLMOps #GenerativeAI #SoftwareArchitecture #AI
