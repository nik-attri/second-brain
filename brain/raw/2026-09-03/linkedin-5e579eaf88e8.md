---
author: Pranav Kakde
fetched_at: '2026-09-03T07:29:37.397664Z'
id: 5e579eaf88e8
lane: lead
published: ''
source: linkedin
title: 'Ever handed GitHub Copilot a 400-page requirements doc and asked it to generate
  test cases?

  It either times out, gives y'
url: https://www.linkedin.com/feed/update/urn:li:activity:7501166936785948672
---

Ever handed GitHub Copilot a 400-page requirements doc and asked it to generate test cases?
It either times out, gives you generic garbage, or takes forever because it's re-reading the whole doc every single time.

Turns out this is a solved problem — search engines figured it out years ago. The fix: stop feeding your AI agent the whole haystack. Search for the relevant chunk first, then generate.

I wrote up 4 real ways to do this, from fancy to dead simple:
🔹 Classic RAG with a vector database — best when your questions don't use the same words as the doc
 🔹 Vector-less RAG using BM25 — keyword search, zero infra, surprisingly effective for most QA docs
 🔹 Manual chunking + an index file — even better, automate it with a simple bag-of-words script
 🔹 Ditch binary Excel/Word entirely — split into CSVs and Markdown files, index them, skip the formatting bloat
Less tokens. Faster responses. Better test cases, because the AI isn't drowning in noise it never needed.

Full writeup with code examples here 👇
https://lnkd.in/dpg6_KNe

#SoftwareTesting #QualityEngineering #AI #GitHubCopilot #RAG
