---
author: Yaochen Rao
fetched_at: '2026-11-06T10:07:26.142726Z'
id: 70d9b02bf30c
lane: lead
published: ''
source: linkedin
title: 'Happy to share our recent work on using LLMs to automate scientific literature
  curation! 🧬


  A lot of valuable assay data'
url: https://www.linkedin.com/posts/yaochen-rao-9342a6237_drugdiscovery-llm-targetedproteindegradation-activity-7524404206213103618-RAWl
---

Happy to share our recent work on using LLMs to automate scientific literature curation! 🧬

A lot of valuable assay data is buried in scientific papers and supplementary materials. Collecting these data manually takes a lot of time, and keeping databases up to date as new papers come out is even more challenging.

In this work, we wanted to see how much of this process could be automated with LLMs.

We developed an agentic workflow that extracts and verifies experimental data from the literature, using only a small number of expert-annotated papers to optimize the extraction process. With just 7 annotated molecular glue papers, we achieved an F1 score of 0.98, and the same approach also worked well for PROTACs without additional prompt optimization.

Interestingly, we found that existing manually curated databases often missed data that was already reported in the original papers. We were able to recover additional assay records from the same publications and fill in missing experimental details, such as cell lines and assay types, for records already in the databases.

We then applied the workflow to a much larger collection of papers and built AutoTPD+, a living database containing over 7,600 degradation assay records from more than 1,000 publications, designed to be updated monthly as new literature becomes available.

We also explored whether the expanded dataset could help downstream machine learning models. In our experiments, surrogate models trained on AutoTPD+ showed 8.9–18.2% lower prediction error estimates in a controlled comparison, suggesting potential benefits for downstream predictive modeling.

I'm excited about the possibility of moving away from static, manually curated datasets towards scientific databases that can continuously grow with the literature, while also making more experimental data available for machine learning.

Many thanks to my co-authors Farzaneh Jalalypour, N M Anoop Krishnan, and Rocío Mercado Oropeza for all the support and great discussions along the way!

📄 Paper: https://lnkd.in/eVKuiPwW
🌐 Code & data: https://lnkd.in/e6q3a2g2

#DrugDiscovery #LLM #TargetedProteinDegradation #MolecularGlues #PROTACs
