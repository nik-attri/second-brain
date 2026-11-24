---
author: '@campusx-official'
fetched_at: '2026-11-24T13:04:10.741501Z'
id: cc0c9c7fc567
lane: capability
published: '2026-11-23T14:00:12+00:00'
source: youtube
title: 'Google ADK Internals: Sessions, Runners & Event-Driven Architecture | CampusX'
url: https://www.youtube.com/watch?v=Z1F5pw2GwLA
---

In this deep-dive session of our Google Agent Development Kit (ADK) series, we look behind the scenes of high-level commands like adk web to explore the core internal architecture that powers stateful, production-grade agent applications.

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

00:00 - Introduction & Recap: Tools and Structured Output in ADK
01:00 - Why Learn ADK Internals? Moving Beyond adk web
02:55 - The Core Problem: Why LLMs are Stateless
07:05 - Creating the Illusion of Memory via Conversation History
09:20 - Defining Sessions: Multi-Day Retention, Session IDs & User IDs
14:25 - The ADK Hierarchy: App, User, Session, and Event Layers
17:18 - What is an Event? Tracking User Messages, Tool Calls & Agent Handoffs
19:55 - Event Metadata: Authors, Timestamps & Invocation IDs Explained
24:32 - Live Inspection of Event Traces in ADK Web
26:48 - What is a Session Service? Creation, Retrieval & State Persistence
28:45 - Session Service Types: In-Memory, Database & Vertex AI
31:12 - The Missing Link: Introducing the Runner Orchestrator
33:38 - Anatomy of a Conversational Turn: What the Runner Executes
36:35 - Step-by-Step Execution Lifecycle of runner.run
42:05 - Project Setup: Structuring Standalone Agent Scripts (run_agent.py)
45:30 - Code Deep Dive: Instantiating the Runner and In-Memory Session Service
48:20 - Building the Custom Execution Function (ask)
50:35 - Live Execution: Testing Multi-Session State Retention in Pure Python
53:15 - Summary & Next Steps: Building Custom Web Chat UIs
