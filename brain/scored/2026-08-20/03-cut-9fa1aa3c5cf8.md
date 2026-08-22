---
author: '@campusx-official'
automation_hypothesis: ''
budget_signal: ''
company: ''
contact_name: ''
hook: ''
id: 9fa1aa3c5cf8
lane: cut
pain_signal: ''
reason: A text-to-SQL model selection walkthrough with code is mildly useful, but
  you can already run this and it doesn't create a new offer.
score: 3
scored_at: '2026-08-22T11:12:21.784961Z'
source: youtube
unlocks: ''
url: https://www.youtube.com/watch?v=RG5A-W3eMHI
verdict: cut
---

Public leaderboards help narrow down candidates, but they won't tell you how a model performs on your unique database, business logic, or prompt constraints. In this hands-on session of our LLM Evaluation Masterclass, we step into the shoes of AI Engineers at ESPN Cricinfo to build a production-ready Text-to-SQL engine.  We walk through the entire model selection lifecycle—from establishing budget and latency ceilings to crafting a golden dataset, setting up custom execution evaluation pipelines, and running live benchmark tests across 5 top candidate LLMs.

Code - https://github.com/campusx-official/llm-sql-eval

This lecture was taken live for insiders, join here: https://youtu.be/j_G30FLmCcw

📱 Grow with us:
CampusX' LinkedIn: https://www.linkedin.com/company/campusx-official
CampusX on Instagram for daily tips: https://www.instagram.com/campusx.official
My LinkedIn: https://www.linkedin.com/in/nitish-singh-03412789
Discord: https://discord.gg/PsWu8R87Z8
E-mail us at support@campusx.in

Chapters:

00:00 - Course Recap & Hands-On Transition
02:24 - Session Agenda: How to Run Custom Model Evals
03:30 - Case Study Introduction: Text-to-SQL for ESPN Cricinfo
08:24 - The 3-Step Selection Framework: Requirements, Filtering, & Custom Evals
13:14 - Step 1: Gathering Requirements & Defining the Task
14:00 - Calculating Operational Costs: Token Math & Budget Ceilings
31:48 - Deep Dive: Prompt Cashing & KV Cache Optimization
39:37 - Latency, Context, and Correctness Constraints
45:48 - Step 2: Leaderboard Shortlisting & OpenRouter Setup
52:43 - Normalizing Leaderboard Scores: Weighting Accuracy vs. Speed
01:04:40 - Selecting the 5 Finalist Candidate Models
01:08:40 - Step 3: Custom Eval Workflow Architecture
01:11:05 - Creating & Validating the Golden Dataset (golden_hard.csv)
01:27:48 - Testing OpenRouter Connection with a Single Prompt (first_test.py)
01:32:32 - Writing the Evaluator: Why String Comparison Fails for SQL
01:34:00 - Table Comparison Logic: Row Checks, Value
