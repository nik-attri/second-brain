---
author: Kelvin Asonta
fetched_at: '2026-11-12T10:28:04.999743Z'
id: afbef4658283
lane: lead
published: ''
source: linkedin
title: 'Enforcing Clean Boundaries: How 10 Modules Communicate Without Spaghetti Code


  The biggest risk of any monolith is that,'
url: https://www.linkedin.com/posts/kelvin-asonta_cleanarchitecture-ddd-php-activity-7526590341588766720-9C0C
---

Enforcing Clean Boundaries: How 10 Modules Communicate Without Spaghetti Code

The biggest risk of any monolith is that, over time, every feature starts querying every table until you have an untestable ball of mud. When building StraytTix from scratch, I set a strict rule across all 10 backend modules: No module reaches directly into another module's internal state without a defined contract or domain event.

How we enforce this in practice: 

1. 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 𝗖𝗼𝗻𝘁𝗿𝗮𝗰𝘁𝘀 & 𝗗𝗧𝗢𝘀: Shared configurations (like global platform fee rules) are exposed via AppSettingsServiceInterface returning immutable readonly DTOs (AppSettingsDTO). 

2. 𝗘𝘃𝗲𝗻𝘁-𝗗𝗿𝗶𝘃𝗲𝗻 𝗦𝗶𝗱𝗲 𝗘𝗳𝗳𝗲𝗰𝘁𝘀: When an order is paid in Modules/Payments, it doesn't manually build PDFs or send emails. It dispatches domain events that Modules/Tickets and Modules/Notification handle asynchronously. 

3. 𝗦𝗰𝗼𝗽𝗲𝗱 𝗥𝗼𝘂𝘁𝗲 𝗣𝗿𝗼𝘃𝗶𝗱𝗲𝗿𝘀: Each module registers its own versioned API routes (/api/v1/...) and middleware pipelines independently. The result? I can refactor the entire payment gateway logic without touching a single line of ticket scanning code. 

How do you prevent domain leakage in large codebases? 

#cleanarchitecture #ddd #php #laravel #backenddevelopment #softwareengineering
