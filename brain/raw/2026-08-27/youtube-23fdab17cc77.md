---
author: '@campusx-official'
fetched_at: '2026-08-27T13:20:19.169798Z'
id: 23fdab17cc77
lane: capability
published: '2026-08-24T13:33:10+00:00'
source: youtube
title: 'Securing Your RAG Application: Testing for Toxicity, Leakage & Scope Drift
  | CampusX'
url: https://www.youtube.com/watch?v=uHulfbxXnSU
---

This session covers the essential safety and security layer of production RAG systems, guiding you through identifying core LLM failure modes—such as prompt injections, data poisoning, and unauthorized tool usage—and establishing a strict Application Safety Policy. You will learn how to build and execute automated evaluation pipelines using DeepEval and G-Eval across three critical safety pillars: auditing for domain-specific toxicity, stopping sensitive system prompt and PII data leaks, and preventing off-topic scope drift, all backed by practical guardrail strategies and red-teaming principles.

This lecture was taken live for insiders, join here: https://youtu.be/j_G30FLmCcw

📱 Grow with us:
CampusX' LinkedIn: https://www.linkedin.com/company/campusx-official
CampusX on Instagram for daily tips: https://www.instagram.com/campusx.official
My LinkedIn: https://www.linkedin.com/in/nitish-singh-03412789
Discord: https://discord.gg/PsWu8R87Z8
E-mail us at support@campusx.in

Chapters:

00:00 - Introduction & The RAG Eval Suite Architecture
01:40 - Why AI Safety & Security Matter for LLM Applications
05:10 - The 6 Core Safety Failure Modes in Production LLMs
10:10 - Non-Adversarial vs. Adversarial Failures
12:30 - Common Attack Vectors: Direct Injections, Jailbreaking & Obfuscation
16:55 - Data Poisoning & Knowledge Base Attacks
20:30 - Privacy, Model Inversion & Resource Exhaustion Attacks
23:30 - The 2-Step Defense: Rigorous Evaluation & Multi-Layered Guardrails
28:30 - What is Red Teaming? Continuous Vulnerability Discovery
30:55 - Defining the Attack Surface for the CampusX Doubt Solver
37:25 - Drafting a Concrete Application Safety Policy
40:15 - Metric 1: Toxicity Evaluation & Why Provider Filters Aren't Enough
44:50 - Building Balanced Toxicity Test Datasets (Adversarial, Benign & Mixed)
52:40 - Implementing & Running Toxicity Evals in DeepEval
01:01:25 - Metric 2: Sensitive Information & PII Leakage Audits
01:04:05 - Live Vulnerability Demo: Leaking Private Data via RAG Chunks
01:07:20 - Structuring Multi-Evaluator Pipelines for Prompt, Content & PII Leakage
01:15:10 - Fixing Data Leaks via System Prompt Hardening & XML Tagging
01:22:30 - Metric 3: Scope Adherence (Preventing Domain Drift & Feature Hijacking)
01:27:35 - Implementing Custom G-Eval Metrics for Scope Verification
01:31:00 - Handling Mixed Queries: Solving Edge-Case Failures
01:34:00 - Summary & Next Steps: Operations Evals and CI/CD Regression Testing
