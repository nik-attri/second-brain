---
author: Amarnath Rao Sulake
fetched_at: '2026-08-26T03:44:58.789701Z'
id: 413e536a2a6e
lane: lead
published: ''
source: linkedin
title: '🚀 Your AI Agent Has Hundreds of Tools. How Does It Know Which One to Use?


  We''ve spent a lot of time solving one problem'
url: https://www.linkedin.com/posts/amarnath-rao-sulake-06994592_ai-aiengineering-agenticai-activity-7498210346105712640-awiK
---

🚀 Your AI Agent Has Hundreds of Tools. How Does It Know Which One to Use?

We've spent a lot of time solving one problem:

How can AI agents use tools?

MCP helps with that.

APIs help with that.

Agent-to-agent protocols help with that.

But there's a new problem emerging:

How does an agent discover the right tool in the first place?

Imagine an enterprise with:
 🔹 500+ internal APIs
 🔹 200 MCP servers
 🔹 100+ specialized agents
 🔹 Hundreds of workflows and skills

You can't realistically hard-code every capability into every AI agent.

And dumping every tool description into the model's context isn't scalable either.

This is where Agentic Resource Discovery (ARD) becomes interesting.
Instead of:
"Here are all the tools you can use."

The model can ask:
"I need a capability that can investigate a production database issue."

A discovery layer can then find relevant capabilities, provide information about who operates them, how they can be accessed, and—critically—whether they can be trusted.

Conceptually:
Agent → Discover → Verify → Select → Invoke
This creates a new layer in the agent architecture:
Discovery.
And that's an interesting shift.
The agent ecosystem may evolve from:
Static tools → Dynamic capabilities
Manually configured agents → Discoverable agents
Tool lists → Capability discovery

But discovery introduces its own engineering problems:
🔐 How do we verify a capability?
🛡️ How do we enforce enterprise policies?
🎯 How do we rank competing tools?
🔄 How do we handle deprecated capabilities?
🧩 How do private and public resources coexist?
📊 How do we observe what an agent discovered and why?

We're not just building AI agents anymore.

We're starting to build an ecosystem in which agents can discover other capabilities.

And that could become one of the foundational layers of the agentic web.

Question:
 Would you allow an enterprise AI agent to dynamically discover and use a new tool, or should every capability always be explicitly approved and configured first?

#AI #AIEngineering #AgenticAI #SoftwareArchitecture #SystemDesign #MCP #CloudNative #Engineering #TechLeadership #SoftwareEngineering
