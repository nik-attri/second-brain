---
author: Max Vlasov
fetched_at: '2026-09-10T07:37:49.461181Z'
id: 115dbd1036de
lane: lead
published: ''
source: linkedin
title: 'I’d like to share a case of how we used AI to evaluate ticket quality and
  identify weak points in software projects.


  Th'
url: https://www.linkedin.com/posts/max-vlasov-129666a8_ai-artificialintelligence-projectmanagement-activity-7503713227315429378-NYwk
---

I’d like to share a case of how we used AI to evaluate ticket quality and identify weak points in software projects.

The goal was to detect potential project problems early — before they turned into budget overruns and scope creep.

We wanted to understand whether there was a relationship between:
- the quality of project management;
- the project domain;
- the team involved;
- the quality of ticket and story descriptions;
- the problems that appeared later in the project.

Our first decision was not to build an AI agent or a multi-agent system.
We decided that a simple script would be enough.

The script had a connector to Jira and read access to tickets and project documentation across multiple projects. It collected the relevant data, sent it to an LLM through an API, and received the analysis back.

Before running it, we created an evaluation framework for the stories.

A good story should clearly answer:
- What business problem are we solving?
- Who is affected by this change?
- What exactly should happen?
- How will we know that it works?
- What is included in the scope?
- What is explicitly out of scope?
- What dependencies or assumptions should we consider?
- What happens in edge cases or error scenarios?
- Is the story small enough to estimate and deliver?
- Does it support the overall project goal?

The script was scheduled to run once a week and generated visual reports showing trends and correlations across projects.

We went through five rounds of tuning and calibration. It definitely did not work perfectly from the first attempt.

But eventually, the tool started showing a clear relationship between problematic projects, ticket quality, and the people involved in creating and managing the work.

The most valuable part was not simply that AI reviewed tickets faster.

It helped us compare ticket quality across projects and identify patterns before those patterns became serious delivery or budget problems.

The time saving was significant.

Previously, reviewing the tickets in one project and understanding the main problem areas took at least one full working day.

With the automated report, the team could review the results and understand the key risk areas in around 30 minutes.

That became one of our main KPIs:
- Manual analysis: at least 1 full working day per project
- Automated report review: around 30 minutes
- Time saved: more than 90% of the review effort

The tool does not replace human judgment. It gives the team a faster way to see where attention is needed.

One lesson I took from this project is simple:
Before building an AI solution, define what “good” looks like. If the evaluation criteria are unclear, AI will only automate the ambiguity.

We are still using the tool.

How do you currently check the quality of tickets in your projects — manually, with a checklist, or not at all?

#AI #ArtificialIntelligence #ProjectManagement #BusinessAnalysis #SoftwareDevelopment #Agile #ProductManagement
