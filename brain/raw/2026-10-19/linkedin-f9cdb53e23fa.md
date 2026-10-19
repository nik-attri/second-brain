---
author: Kaung Nay Lin Khant
fetched_at: '2026-10-19T08:16:32.007084Z'
id: f9cdb53e23fa
lane: lead
published: ''
source: linkedin
title: 'For my NLP research, every experiment started with hours of pipeline setup.

  I had to clean the data. Convert to JSONL. S'
url: https://www.linkedin.com/posts/kaung-nay-lin-khant_for-my-nlp-research-every-experiment-started-activity-7517640661966266368-uDOY
---

For my NLP research, every experiment started with hours of pipeline setup.
I had to clean the data. Convert to JSONL. Set up API keys. Write the script. Hit rate limits. Fix them. Compute metrics. Format the LaTeX table. Change one design, start over.  😞 

So I started building tools to handle the repetitive stuff, and figured other researchers might need them too. The first one is live on PaperLab.space: https://paperlab.space
It’s for evaluation. Upload a spreadsheet, pick models, get an Excel file, a LaTeX table, and a config to rerun it. Free, and it works for languages like Burmese and Thai too.

Prefer code? The engine is open source:
💻 pip install paperlab-space

More tools are coming: more metrics, LLM-as-judge, fine-tuning dataset prep, and local models. The goal is to cover all the repetitive parts of NLP research.

If you know someone stuck in setup hell, feel free to pass it on.
And what’s the most annoying part of your research workflow? That might be the next tool. 🙌
