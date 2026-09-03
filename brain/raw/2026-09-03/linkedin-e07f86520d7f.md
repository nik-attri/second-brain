---
author: Davy Gérald O.
fetched_at: '2026-09-03T07:29:37.396483Z'
id: e07f86520d7f
lane: lead
published: ''
source: linkedin
title: 'After 5+ years deploying enterprise ERPs such as Microsoft Dynamics and ERPNext,
  I came to a simple conclusion:


  The cap'
url: https://www.linkedin.com/posts/davy-g%C3%A9rald-o-2b03033b7_after-5-years-deploying-enterprise-erps-activity-7501172287199621122-hHsd
---

After 5+ years deploying enterprise ERPs such as Microsoft Dynamics and ERPNext, I came to a simple conclusion:

The capabilities of high-performance ERP systems should also be accessible to SMEs without multinational budgets.

That’s how Nexidior was born: a management SaaS designed to evolve into a complete ERP.

But Nexidior is more than a product.

It’s my technical laboratory.

My goals:

1• Combine my two areas of expertise: ERP Consulting + Full-Stack Engineering.

2• Challenge my engineering skills in a real-world environment, outside the structure of a large company.

3• Push myself toward Solution Architect level.

To build this as a solo engineer without drowning in technical debt, I chose pragmatism.

••••• Architecture •••••

• TypeScript Full-Stack — one language across the stack, maximizing productivity while going deep into the ecosystem.

• Modular Monolith — no premature microservices. Simpler deployment, lower costs, and the possibility to distribute later when the system requires it.

• Headless — backend and frontend are decoupled, keeping the core ready for mobile apps and third-party integrations.

••••• Stack •••••

NestJS for structure, modularity and dependency injection.

PostgreSQL + Prisma for a strong relational foundation and complex transactional business logic.

Nuxt 4 for productivity, file-based routing and application structure.

••••• Infrastructure •••••

Linux + Docker + Contabo + Coolify + GitHub

A simple git push triggers the deployment pipeline.

The objective is simple:

Focus on engineering and product development, not manual Ops.

💡 One of the architectural decisions I’m most proud of is the strict separation between data and presentation.

In Nexidior, a backend entity dictionary dynamically drives parts of the frontend interface and routing.

That’s where Backend-Driven UI comes in.

I’ll break down this architecture with actual code in my next post:

Dashboard — Axis 2.

💬 For an MVP, would you choose a well-structured monolith or start with microservices from day one?
