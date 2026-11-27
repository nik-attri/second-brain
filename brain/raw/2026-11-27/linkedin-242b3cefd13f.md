---
author: Vijay k ( AI Native Engineer )
fetched_at: '2026-11-27T11:35:29.172257Z'
id: 242b3cefd13f
lane: lead
published: ''
source: linkedin
title: 'Recently, my friend Bhavik and I started exploring an interesting use case:
  Can AI make Snowflake-to-Databricks migratio'
url: https://www.linkedin.com/posts/vijay-ai-native-engineer_recently-my-friend-bhavik-and-i-started-activity-7532036584062431232-CWmx
---

Recently, my friend Bhavik and I started exploring an interesting use case: Can AI make Snowflake-to-Databricks migration easier and more efficient?

A database migration involves much more than moving tables. It requires understanding existing schemas, converting SQL queries, rebuilding pipelines, validating data and optimizing performance.

We're exploring how Generative AI and AI agents can help across this process.

Some areas we're focusing on:

- Metadata Analysis: Understand Snowflake schemas, tables and dependencies.
- SQL Conversion:Convert Snowflake SQL into Databricks SQL / PySpark.
- Pipeline Generation: Assist in building ingestion and transformation workflows.
- Data Validation: Compare source and target data and identify mismatches.
- Optimization:** Suggest improvements for performance and cost.

Our idea is to build an AI-powered Migration Assistant, starting with a small proof of concept and gradually expanding its capabilities.

We're particularly interested in exploring how far AI can automate migration tasks while keeping human review and data validation at the centre.

Excited to explore and build this together with Bhavik! Bhavik Nagre

High-level migration approach
I suggest dividing the migration into eight phases.
Phase 1 – Discovery and Assessment
Understand the existing Snowflake environment.
Identify databases, schemas, tables, views, and stored procedures.
Analyze dependencies between objects.
Identify frequently used queries and workloads.
Assess data volumes and complexity.
Identify Snowflake-specific SQL features.
AI contribution: Use an LLM to analyze SQL scripts, classify objects, identify dependencies, and generate migration assessment reports.
Phase 2 – Migration Strategy and Prioritization
Divide workloads into migration waves.

Phase 3 – Data Migration
Move data from Snowflake to Databricks.
Establish secure connectivity.
Extract historical data.

Phase 4 – SQL and Code Conversion
Convert Snowflake SQL to Databricks SQL / PySpark.
Convert views and SQL queries.

Phase 5 – Pipeline Modernization
Rebuild the data processing architecture.
Implement Bronze, Silver, and Gold layers.

Phase 6 – Automated Testing and Validation
Ensure the migrated platform produces the same business results.
Compare source and target record counts.

Phase 7 – Performance and Cost Optimization
Optimize the Databricks environment.
Optimize Delta tables.

Phase 8 – Deployment and Cutover
Prepare for production migration.
Deploy development, UAT, and production workloads.
Run parallel validation.
Establish monitoring and alerting.


For those who have worked on data migrations, what has been the most challenging part of moving from Snowflake to Databricks?

 #DataEngineering #Snowflake #Databricks #GenerativeAI
