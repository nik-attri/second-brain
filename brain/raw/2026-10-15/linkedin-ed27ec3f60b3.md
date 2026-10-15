---
author: Dhrubo ..
fetched_at: '2026-10-15T07:50:40.332262Z'
id: ed27ec3f60b3
lane: lead
published: ''
source: linkedin
title: 'Day 7 of building one AI agent a day, in public.

  Today: SENTRA AI -- Alert Triage Copilot for high-volume enterprise tel'
url: https://www.linkedin.com/posts/dhrubojyoti-gangopadhyay_buildinpublic-aiagents-cybersecurity-activity-7516395073627136004-PNnM
---

Day 7 of building one AI agent a day, in public.
Today: SENTRA AI -- Alert Triage Copilot for high-volume enterprise telemetry.
Most security and operations teams aren't drowning in incidents. They are drowning in uncoordinated alerts.
When an anomaly hits an enterprise stack, alerts fire simultaneously across disconnected systems--Splunk, Microsoft Sentinel, CrowdStrike. The problem isn't detecting the signal; it's the 40 minutes an on-call engineer spends manually cross-referencing scattered runbooks, checking historical incident tickets, and writing the initial remediation brief.
Instead of building another chat interface, we built a 4-agent autonomous pipeline that explains the incident before asking an engineer to act:
1. Unified Telemetry Normalization:
Vendor alerts (Splunk, CrowdStrike, Sentinel) enter a hardened FastAPI gateway. Raw JSON payloads are normalized into a unified schema with strict Pydantic validation. No unstructured guessing.
2. pgvector Retrieval Over Historical Runbooks:
The alert context is matched against our private pgvector database containing validated SOPs, past post-mortems, and runbooks. It retrieves the exact 3 most relevant prior resolutions within 120ms.
3. LangGraph Multi-Agent Triage Loop:
Four isolated specialists coordinate under a deterministic supervisor:
- Signal Analyst: Extracts telemetry indicators and establishes timeline chronology.
- RAG Retriever: Pulls grounded context from internal documentation.
- Evidence Verifier: Runs deterministic sanity checks against historical false-positive patterns.
- Remediation Writer: Drafts plain-English root cause hypotheses and step-by-step containment instructions.
4. Human-in-the-Loop Degradation:
The system never auto-executes high-impact remediation on live infrastructure. If sentiment is ambiguous or confidence dips below 90%, it instantly routes a structured summary to Slack and Jira for human review.
The result: Alert triage time dropped from 42 minutes to under 90 seconds, with a complete audit trail for every recommendation.
Building reliable AI agents isn't about replacing engineers. It's about eliminating the manual 40-minute context chase so engineers can make decisions faster.
How does your team handle alert fatigue across fragmented monitoring tools?
#BuildInPublic #AIAgents #CyberSecurity #DevSecOps #SoftwareEngineering #Automation #SystemDesign #FastAPI #LangGraph
