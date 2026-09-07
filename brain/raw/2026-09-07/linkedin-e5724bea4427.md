---
author: Arghya Ranjan Roy
fetched_at: '2026-09-07T07:41:00.236148Z'
id: e5724bea4427
lane: lead
published: ''
source: linkedin
title: "I stopped writing posts manually 1 weeks ago.\n \nInstead I built a system\
  \ that watches other creators in my niche, extrac"
url: https://www.linkedin.com/posts/arghya-ranjan-roy-309bb5266_aiautomation-n8n-workflowengineering-activity-7502606784348495872-CNRh
---

I stopped writing posts manually 1 weeks ago.
 
Instead I built a system that watches other creators in my niche, extracts the ideas worth stealing, and queues them as ready-to-publish drafts  scored, categorized, and sourced.
 
Here's the actual architecture, because "AI automation" means nothing without the engineering behind it.
 
THE PIPELINE (n8n, 29 nodes )
1. Ingestion Form trigger accepts any number of YouTube URLs, batch-pasted.
2. A code node parses and extracts video IDs from arbitrary URL formats - no manual              cleanup.
3. Deduplication layer: Before anything touches an LLM, the system checks Airtable ("Check       If Already In Sources") to see if a video's already been processed.
    (This isn't optional polish , it's what keeps token spend from scaling linearly with re-runs.
    Most people skip this and burn API budget re-processing the same sources.)
4. Metadata + transcript acquisition: oEmbed pulls the title.
5. Supadata pulls the transcript.
6. Both routes branch on failure - a video with no captions gets flagged and skipped                ("Mark Source Skipped"), not silently dropped or, worse, crashed on.
7. Insight extraction (Gemini API): Raw transcript + timestamps get joined and sent to                Gemini for structured insight extraction ..not summarization.
8. Each insight comes back scored (1-10 priority), tagged to a content pillar, and mapped to      a suggested format (Carousel, StoryTelling, Text Only, Photo+Caption).
9. Resilience layer the part most builds skip: "gemini Responded OK?" and "Parsed OK?"             are explicit guard nodes.
10. If the LLM call fails or returns malformed JSON, the source gets reset to a retry state              instead of failing the whole run.
11. A batch of 20 videos surviving one bad response is the difference between a toy and             something you'd trust in production.
12. Fan-out + write: Insights are split into individual rows, flagged for last-item detection (so     the loop knows when a source is fully drained), then written to the Vault as structured            airtable records - Insight, Source, Content Pillar, Suggested Format, Priority Score.
13. Rate-limit safety + loop control: A deliberate wait node throttles calls before the batch           loop advances to the next video.

Result: I paste 20 competitor video links, walk away, come back to 100+ scored, categorized, publish-ready insights sitting in a database - not a wall of raw transcript I still have to think about.
 
If you're a founder drowning in content ops, lead ops, or repetitive research work , this same architecture pattern (ingest → dedupe → extract → validate → structure → store) applies far beyond content. I've used it for lead capture and I'm building it for tender monitoring next.
 
Open to conversations either way building this kind of infrastructure for your team, or discussing where the pattern breaks.
 
#AIAutomation #n8n #WorkflowEngineering #AIAgents #Automation
