---
author: '@campusx-official'
fetched_at: '2026-11-19T10:56:09.397511Z'
id: 9144c0f3be3f
lane: capability
published: '2026-11-18T15:16:19+00:00'
source: youtube
title: Structured Output in Google ADK (with Pydantic & Mini Project) | CampusX
url: https://www.youtube.com/watch?v=YbVAjwAMHfI
---

In this session of our Google Agent Development Kit (ADK) series, we explore how to enforce strict, deterministic JSON outputs so your AI agents can reliably communicate with frontend UIs, backend APIs, databases, and downstream agents. You will learn why regex parsing and prompt-level JSON requests fail in production, and how ADK solves this by pairing Pydantic schemas (output_schema) with Gemini's native structured generation mode. We walk through designing production-grade schemas—handling optional null values, lists, standardized Literal enums, and numeric constraints—and demonstrate how to persist parsed dictionaries directly into session state using output_key. Finally, we build a Support Ticket Classifier agent that routes incoming student queries by category, urgency, and human-escalation requirements.

Pydantic Crash Course: https://youtu.be/lRArylZCeOs

Code - https://github.com/campusx-official/google-adk-course

This lecture was taken live for insiders, join here: https://youtu.be/j_G30FLmCcw
AI Engineering Roadmap: https://youtu.be/dQgsHROf8Cw

📱 Grow with us:
CampusX' LinkedIn: https://www.linkedin.com/company/campusx-official
CampusX on Instagram for daily tips: https://www.instagram.com/campusx.official
My LinkedIn: https://www.linkedin.com/in/nitish-singh-03412789
Discord: https://discord.gg/PsWu8R87Z8
E-mail us at support@campusx.in

Chapters:

00:00 - Introduction & Recap of Google ADK Progress
01:26 - Why Structured Output Matters: When Code Reads Agent Outputs
03:45 - 4 Key Use Cases: Frontend UIs, Backend APIs, Multi-Agent Handoffs & Databases
06:35 - Why Regex Pattern Matching Breaks on LLM Text
09:42 - Why Prompting for JSON Still Fails in Production
12:48 - How Structured Output Works in Google ADK (Pydantic + output_schema)
15:58 - Under the Hood: Native Schema Enforcement & Validation
16:45 - Hands-On Demo: Building a Student Inquiry Extractor Agent
20:14 - Production Schema Design: Handling Nulls, Lists, Enums & Constraints
26:30 - Persisting Structured Output in Session State via output_key
29:55 - Mini Project: Building a Multi-Agent Ticket Classifier & Router
33:48 - Live Demo: Routing Support Tickets by Category, Urgency & Escalation
35:20 - Summary & Upcoming ADK Topics
