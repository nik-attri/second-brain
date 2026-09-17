---
author: Jemiseye Vincent Vincent
fetched_at: '2026-09-17T08:09:59.046850Z'
id: d38eb524dc05
lane: lead
published: ''
source: linkedin
title: 'Day 5: Learning AI Automation 

  Project Title: AI-Powered Contact Form Intake & Dynamic Routing System

  Five days ago, I d'
url: https://www.linkedin.com/posts/jemiseye-vincent-vincent-235b30401_aiautomation-n8n-openai-activity-7506226133265317889-FTwq
---

Day 5: Learning AI Automation 
Project Title: AI-Powered Contact Form Intake & Dynamic Routing System
Five days ago, I decided to stop just reading about AI and start building practical automations. Today, I tackled a real-world problem that almost every business faces: drowning in contact form inbox chaos.
The Goal
When a user submits a contact form, someone usually has to read it, figure out if it's junk, and manually send it to the right department. That takes time, and high-value leads often sit waiting in an inbox for hours.
My goal for Day 5 was to build an intelligent, end-to-end system using n8n and OpenAI that automatically reads incoming messages, categorizes them in real time, logs the data, and notifies the right team instantly on Discord.
How I Built It & Got the Result
Capturing the Lead: Built a custom form trigger in n8n that listens for new submissions in real time.
Context Checking: Connected a Google Sheets node to cross-reference our internal database and pull historical records before taking action.
AI Classification: Used OpenAI's GPT models to analyze raw message text and automatically classify every submission into one of three buckets: Spam, Technical, or Lead while also generating an AI-suggested next step for our team.
Smart Logic Routing: Built conditional Switch rules combined with a custom JavaScript node to parse the JSON output into clean text properties.
Instant Alerts via Discord:
Spam: Passed to a No-Operation node to drop junk submissions without disturbing the team.
Technical Queries: Routed directly to the support channel on Discord with full context for quick troubleshooting.
 New Leads: Recorded directly in our Google Sheet database and instantly flagged on Discord alongside the AI’s recommended next action.
The Result
After testing all three branches and resolving edge cases (like JSON string parsing and node data mapping), the workflow was officially published and set to live mode!
What used to take hours of manual triaging now takes under 3 seconds on complete autopilot.
Building in public has been a game-changer. Onto Day 6! 
#AIAutomation #n8n #OpenAI #BuildInPublic #NoCode #WorkflowAutomation #AutomationEngineer #ArtificialIntelligence #ChatGPT #LLMs #TechCommunity #FutureOfWork #DigitalTransformation #SoftwareEngineering #BusinessAutomation #ProductivityHacks #TechStartup #WorkSmart #DeveloperLife #Innovation #TechCareers #SelfTaughtDeveloper #CodingLife #MachineLearning #AITools@Adebayo
