---
author: '@campusx-official'
fetched_at: '2026-08-20T20:09:09.731560Z'
id: 06dee25228ea
lane: capability
published: '2026-08-15T16:05:26+00:00'
source: youtube
title: 'Evaluating RAG: Testing the Generator & Full Pipeline with the RAG Triad |
  CampusX'
url: https://www.youtube.com/watch?v=PATGn2XhmCY
---

In this hands-on session of our LLM Evaluation Masterclass, we move beyond isolated retriever testing to build and evaluate our Generator component, and then connect both into an end-to-end RAG Pipeline evaluated against the industry-standard RAG Triad.  We demonstrate how to diagnose critical generator failure modes—like ungrounded hallucinations and off-topic outputs—and how to iteratively refine your system prompt using DeepEval and LLM-as-a-Judge.

This lecture was taken live for insiders, join here: https://youtu.be/j_G30FLmCcw

Code: https://github.com/campusx-official/rag-eval-deepeval

📱 Grow with us:
CampusX' LinkedIn: https://www.linkedin.com/company/campusx-official
CampusX on Instagram for daily tips: https://www.instagram.com/campusx.official
My LinkedIn: https://www.linkedin.com/in/nitish-singh-03412789
Discord: https://discord.gg/PsWu8R87Z8
E-mail us at support@campusx.in

Chapters:

00:00 - Introduction & Plan of Action: Building the RAG Eval Suite
01:44 - Building Component 2: The Generator (generator.py)
04:09 - Generator System Prompt Design & Zero-Temperature Constraints
07:31 - Deep Dive: The 2 Core Generator Failure Modes
08:07 - Failure Mode 1: Unfaithfulness & Hallucinations (The Air Canada Trap)
12:07 - Failure Mode 2: Answer Irrelevance (Faithful but Off-Topic)
15:33 - How LLM-as-a-Judge Measures Faithfulness (Atomic Claims Extraction)
23:55 - How LLM-as-a-Judge Measures Answer Relevancy (Reference-Free Eval)
32:45 - Creating the Faithfulness Golden Dataset from ChromaDB Chunks
35:50 - Writing the Generator Evaluation Script (eval_generator.py)
38:40 - Running Generator Baseline Trial (91% Faithfulness / 73% Relevancy)
42:13 - Prompt Engineering: Refining Rules Over Failed Test Cases
45:40 - Optimized Trial Results: Reaching 96% Faithfulness & 92% Relevancy
49:20 - Managing Rate Limits & Open-Source LLM-as-a-Judge Options
52:13 - Experiment Tracking Demo: Visualizing Test Runs on Confident AI
54:40 - Assembling the Full Pipeline (rag_pipeline.py)
59:00 - Pipeline-Level Evaluation: Introducing the RAG Triad
01:03:30 - Defining Contextual Relevancy (Claim-to-Query Alignment)
01:07:30 - Implementing RAG Triad Testing (eval_rag_pipeline.py)
01:10:05 - Analyzing Triad Results: The Curious Case of the Low Contextual Relevancy
01:13:00 - Resolving the Duality: Why Recall & Precision Differ from Chunk Relevancy
01:19:30 - Wrap-Up & Looking Ahead to Application-Level Evals (GEval & Safety)
