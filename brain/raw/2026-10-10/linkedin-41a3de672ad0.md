---
author: TRAIL Labs
fetched_at: '2026-10-10T09:12:54.637568Z'
id: 41a3de672ad0
lane: lead
published: ''
source: linkedin
title: '[About 16% of the sources four AI answer engines cited were classified as
  AI-generated]


  Google''s September spam update'
url: https://www.linkedin.com/posts/trail-labs_aisearch-geo-aeo-activity-7514602572465377280-PHJk
---

[About 16% of the sources four AI answer engines cited were classified as AI-generated]

Google's September spam update finished rolling out around October 8. Since then we have read several posts claiming that AI-written content is being dropped from the index at scale. A new AIES 2026 paper measures the other side: do AI answer engines filter AI-written sources out?

Researchers at Northwestern sent 712 real user queries on politics, health and the environment to ChatGPT (with web search), Copilot, Gemini and Perplexity through each product's interface, then ran the text of 19,154 cited pages through an AI-text detector.

About 16% (3,056) were classified as AI-generated. In the authors' test on 105 articles from sites reported as AI content farms, all assumed AI-written, the detector labeled 31.4% human, so they read 16% as a lower bound.

Engines differ by nearly 4x. Copilot 27.8%, Gemini 14.7%, Perplexity 9.4%, ChatGPT 7.3%. ChatGPT cites the most sources per answer and has the lowest share, so volume alone does not explain it.

The AI-generated sources sit in the long tail. 97.1% came from outside the 25 most-cited domains. Of 1,180 Wikipedia pages cited, 15 were AI-generated. Several niche domains had every cited page classified as AI-generated, and of 200 AI-classified pages the authors checked by hand, none disclosed AI use.

Google's own documents point the same direction. The scaled content abuse policy lists "using generative AI tools or other similar tools to generate many pages without adding value for users" and targets low-value content "no matter how it's created." The AI content guidance, updated October 1, says "it is critical to manually factcheck and review all AI-generated content for accuracy and trustworthiness before publishing."

Our reading: the useful question is whether a page can be verified, more than whether AI wrote it. When TRAIL Search drafts an article, it checks that every paragraph with numbers carries a source link and rewrites the ones that do not. We do not detect AI authorship.

Limits: there is no web-wide baseline, so the paper cannot say whether 16% is high or low. The authors also note one detector, English and US-related queries only, three topics, and "AI-generated" is not a quality judgment. The study does not test what makes a page get cited. Korean-language answers are not in the sample.

Cards are drawn from the paper's results section and Table 6, and from Google Search Central and the Search Status Dashboard. M. Allaham, N. Diakopoulos, "Synthetic Sources?: Auditing Generative Search Engine Citations for Evidence of AI-Generated Sources," AIES 2026 (arXiv 2605.23684). We have not reproduced this work.

#AISearch #GEO #AEO #LLMcitations #AIGeneratedContent #GoogleSpamUpdate #InformationRetrieval #TRAILLabs #TRAILSearch
