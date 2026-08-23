---
author: Giang Truong
fetched_at: '2026-08-23T03:41:53.678102Z'
id: 371f950f0b9e
lane: lead
published: ''
source: linkedin
title: 'Changelog: Migrating Sora MCP to xmcp — Dual HTTP/STDIO, Prompts, and Resources


  The Model Context Protocol (MCP) has be'
url: https://www.linkedin.com/posts/axyl1410_changelog-migrating-sora-mcp-to-xmcp-dual-activity-7497124802915119104-uXK5
---

Changelog: Migrating Sora MCP to xmcp — Dual HTTP/STDIO, Prompts, and Resources

The Model Context Protocol (MCP) has become central to how AI assistants (Cursor, Claude Code, Windsurf, Claude Desktop, and Zed) discover, inspect, and install Sora UI components.

To eliminate legacy serverless glue code and deliver a more robust developer experience, we completely rebuilt our MCP infrastructure using the xmcp framework (apps/xmcp).

Key architecture highlights from the migration:

1. Native Dual Bundling (HTTP + STDIO)
Running `bun run build` now generates two standalone distributions:
- `dist/http.js`: Streamable HTTP server over SSE for remote team setups.
- `dist/stdio.js`: Zero-dependency STDIO bridge for local desktop agents without network overhead.

2. Full MCP Specification Support 
Beyond tools, we now support core MCP primitives:
- Prompts (`install-component`): Automates safe, non-interactive installation workflows with workspace resolution.
- Resources (`registry-catalog`): Injects an up-to-date snapshot of all UI components directly into the AI's context window.     

3. Standardized `/mcp` Streaming Endpoint
We decoupled our human-readable discovery dashboard on the root domain from the live MCP streaming endpoint at `/mcp`.

4. Hardened Tool Schemas & Token Budgets
Upgraded `search_docs`, `get_page`, `list_sections`, and `get_component_info` with strict token budgeting (e.g., strict 8,000-token caps and automatic truncation notices).

All documentation and setup instructions for Cursor, Claude Desktop, and Claude Code have been updated.

Read the full deep dive here: https://lnkd.in/ghUR3ugQ
