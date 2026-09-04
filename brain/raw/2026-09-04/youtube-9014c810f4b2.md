---
author: '@campusx-official'
fetched_at: '2026-09-04T07:31:58.593902Z'
id: 9014c810f4b2
lane: capability
published: '2026-09-03T10:00:22+00:00'
source: youtube
title: 'RAG Regression Testing Explained: How to Prevent Silent AI Failures'
url: https://www.youtube.com/watch?v=Aov5QczE3Vo
---

This session covers how to build an end-to-end regression testing framework for RAG systems to ensure that performance tweaks—such as changing chunk sizes, updating system prompts, or adding re-rankers—do not silently degrade safety, quality, or operational metrics in other parts of the pipeline. You will learn how to unify component, pipeline, safety, and operational evaluations into a single automated execution script (run_suite.py), establish a statistical baseline.json, account for probabilistic LLM noise using standard deviation thresholds in a Metric Registry, and execute an automated delta comparison (compare.py) and promotion logic (promote.py) before shipping to production.

This lecture was taken live for insiders, join here: https://youtu.be/j_G30FLmCcw

📱 Grow with us:
CampusX' LinkedIn: https://www.linkedin.com/company/campusx-official
CampusX on Instagram for daily tips: https://www.instagram.com/campusx.official
My LinkedIn: https://www.linkedin.com/in/nitish-singh-03412789
Discord: https://discord.gg/PsWu8R87Z8
E-mail us at support@campusx.in

Chapters:

00:00 - Introduction & Recap: Completing the 3-Tier RAG Eval Suite
02:10 - What is Regression in RAG? The Danger of Single-Metric Tuning
06:00 - Regression Testing in Traditional Software vs. LLM Applications
08:00 - Architecture of the RAG Regression Testing Pipeline
10:15 - The Workflow: Baseline, Candidate & Delta Comparisons
14:30 - Complexity 1: Handling Directional Metrics (Higher vs. Lower is Better)
16:20 - Complexity 2: Mitigating Probabilistic LLM Judge Noise
18:45 - Calculating Noise Thresholds Using Standard Deviations
22:15 - Building the Metric Registry Configuration (metric_registry.py)
24:35 - Limitations of Small Golden Datasets & Disclaimers
25:10 - Refactoring the Codebase: Consolidating Ops & Safety Scripts
30:30 - Standardizing Quality Evals with the Test Harness (harness.py)
31:15 - Automating the Suite Execution (run_suite.py)
34:50 - Live Experiment: Tuning Retriever Chunk Sizes (1500 to 500)
38:05 - Running the Automated Regression Suite (Live Execution)
44:10 - Analyzing the Candidate Run Output Across 14 Metrics
45:05 - Comparing Baseline vs. Candidate (compare.py)
47:50 - Automated Deployment Decision Framework (promote.py)
50:50 - CI/CD Integration & Tooling Landscape (MLflow, Confident AI)
52:35 - Summary & What’s Next: Taking Evals Online Post-Deployment
