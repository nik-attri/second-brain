---
author: Srinivasulu G
fetched_at: '2026-09-27T08:42:51.923122Z'
id: 295e41cbdbc1
lane: lead
published: ''
source: linkedin
title: 'Why does parsing a PDF for RAG still require 2GB of Docker bloatware and 15
  broken C++ dependencies?

  I got tired of wait'
url: https://www.linkedin.com/posts/srinivasulu-g-71673b358_ai-machinelearning-rag-activity-7509845352523476994-Rvut
---

Why does parsing a PDF for RAG still require 2GB of Docker bloatware and 15 broken C++ dependencies?
I got tired of waiting 10 minutes just to pip install heavy document extraction libraries.
So I built DocuMorph Studio — a full-stack, glassmorphic Document ETL & RAG engine packaged into just 59 Kilobytes.
Zero mandatory dependencies. Zero external API keys. Zero telemetry. Just pure Python and a 1-click launch.
Here is what happens under the hood in 59 KB:
🔹 Zero-Bloat Format Ingestion: Parses PDFs, Word (.docx), Excel spreadsheets (.xlsx/.csv), and HTML into clean, hierarchical Markdown using Python’s native stdlib (zlib, zipfile, ElementTree).
🔹 Multi-File Batch Queue: Drag and drop 20 documents at once. It ingests them in parallel, displays real-time progress cards, and lets you download everything as a structured ZIP in 1 click.
🔹 Smart Entity & Key-Value Extraction: Contracts, invoices, and spec sheets automatically get parsed into key-value pairs (Revenue, Dates, Monetary Amounts, SLA tiers) with instant CSV export.
🔹 Interactive RAG Chunking Deck: Live sliders to test chunk size and overlap across 4 strategies (Heading-based, Sliding Window, Sentence Boundary, Table-Preserving).
🔹 1-Click Vector DB Export: Directly copy formatted payloads for LangChain (Document), LlamaIndex (TextNode), Chroma / Pinecone, and prompt-ready XML.
🔹 Cyber-Glass UI: Dark mode glassmorphism with ambient glowing orbs, live token analytics, and instant typography previews.
Future Enhancements Fixing the Multi batch file Processing
Want to test it locally in 10 seconds?
1️⃣ Clone the repo: git clone https://lnkd.in/d2aRdJ73
2️⃣ Double-click run.bat (or run python server.py).
That’s it. It auto-detects Python and opens localhost:8000 immediately.
⭐ GitHub Repo (100% Free & Open-Source): 👉 https://lnkd.in/dJ-TrtiJ
What is the biggest bottleneck in your current document ingestion pipeline: table parsing, chunking strategy, or dependency hell? Drop your thoughts below! 👇
#AI #MachineLearning #RAG #Python #GenerativeAI #OpenSource #LangChain #LlamaIndex #VectorDatabase #SoftwareEngineering #DataEngineering
