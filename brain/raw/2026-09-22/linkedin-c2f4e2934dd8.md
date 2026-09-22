---
author: Shubham D.
fetched_at: '2026-09-22T08:04:05.562784Z'
id: c2f4e2934dd8
lane: lead
published: ''
source: linkedin
title: 'You created 10 million files. Now your queries take 10 minutes instead of
  10 seconds.


  I looked at 12 companies. All 12'
url: https://www.linkedin.com/posts/shubhamdangii_you-created-10-million-files-now-your-queries-activity-7508022605241552896-aZkz
---

You created 10 million files. Now your queries take 10 minutes instead of 10 seconds.

I looked at 12 companies. All 12 had the small files problem.

None of them knew it until production slowed down.

When you finally checked, 15GB of data was stored as 10 million files.

Each file was 1.5KB.

That is the problem.

→ What is the Small Files Problem?
Storing lots of tiny files instead of few large files.
Creates overhead. Metadata explosion. Performance degrades.
Delta Lake was designed to solve exactly this.

→ Why Does It Happen?
Streaming writes small batches
Real-time ingestion creates many partitions
Incremental processing writes small increments
No optimization after writes
Too many shuffle operations

→ The Impact
Query planning takes forever (10M files to scan)
HDFS metadata bloats (memory issues)
Listing files becomes bottleneck
Compaction fails
Query latency increases 10-100x

→ Delta Lake Solution
OPTIMIZE command compacts small files.

OPTIMIZE table_name

Combines many small files into larger ones.
Reduces file count by 10-100x.
Dramatically improves query performance.

→ Auto Compaction
Enable autom atic compaction on writes.
Databricks handles it automatically.
No manual OPTIMIZE needed.

→ Z-ORDER Clustering
Sort data by column while optimizing.

OPTIMIZE table_name ZORDER BY customer_id

Collocates related data.
Improves query performance on filter columns.
Perfect for dimension tables.

→ Vacuum Command
VACUUM table_name RETAIN 7 DAYS

Removes old file versions.
Frees up storage.
Reduces metadata bloat.

→ Monitoring for Small Files
Check partition sizes in UI
Monitor file counts via system tables
Alert if average file size < 100MB
Track OPTIMIZE frequency

→ Best Practices
Run OPTIMIZE regularly
Enable auto-compaction
Use Z-ORDER on filter columns
VACUUM old versions
Monitor file metrics
Tune batch sizes for streaming
Design partitioning carefully
Right-size your writes

→ Interview Question
"Your table has 50 million small files. Queries are 50x slower. How do you fix it?"

Answer: Run OPTIMIZE to compact files. Enable Z-ORDER on hot filter columns. Check partition strategy (too many partitions). Configure batch write size (increase). Monitor file metrics. Set up alerts for small files.

→ Performance Impact
Before OPTIMIZE: 50 million files, 10 minute query
After OPTIMIZE: 500 files, 6 second query

That is 100x faster.

Junior engineers ignore this.
Senior engineers build it from day 1.

Small files compound.
By year 2, your lakehouse is unusable.

Optimize early. Optimize often.

Get my DE Guide here: https://lnkd.in/ghCp94Z2

Tag someone whose data lake is drowning in small files.
