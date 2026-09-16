---
author: Даниил Гандапас
fetched_at: '2026-09-16T08:03:43.660155Z'
id: 2b174ecd6337
lane: lead
published: ''
source: linkedin
title: 'I work as a course instructor at an educational center with 150+ students.


  Teaching is great, but watching our administ'
url: https://www.linkedin.com/posts/daniilgandapas_googleappsscript-automation-productengineering-activity-7505890954952724480-tBMa
---

I work as a course instructor at an educational center with 150+ students.

Teaching is great, but watching our administration battle routine spreadsheets every evening was painful.

Every single day, administrators spent 1.5 to 2 hours on repetitive manual work:
– Cross-checking attendance sheets across multiple study groups;
– Figuring out whose monthly subscription had expired;
– Tracking who missed class and needed a makeup session;
– Manually copying individual payments into a central accounting sheet.

Human errors were inevitable: an unrecorded payment, an accidentally overwritten formula, or a forgotten reminder.

Seeing this friction from the inside every day, I decided to automate the entire flow.

Instead of pitching an expensive SaaS CRM or setting up cloud servers, I built a lightweight automation engine directly inside Google Workspace using Google Apps Script, Google Sheets, and the Telegram Bot API.

How it works:

1. Dynamic Course Sheets: Each group has its own schedule matrix and a built-in payment action panel. The administrator selects a student, picks a plan (monthly, single session, or custom discount), and clicks one button.
2. Centralized Ledger: The script locates the student in the master database, updates their balance, and logs the transaction in the accounting registry.
3. Undo Protection: If someone clicks the wrong row, an Undo function safely reverts the transaction and restores previous cell states without corrupting other records.
4. Automated Telegram Recon: Every evening, a scheduled trigger compares today's attendance against paid credits. The Telegram bot sends administrators an instant digest: who has an outstanding balance and who needs a makeup lesson scheduled.

The outcome:
– $0 spent on infrastructure or SaaS licenses;
– Daily administrative routine dropped from 2 hours to 5 minutes;
– Zero lost payments or untracked debts since deployment.

You don't always need a complex cloud architecture to deliver value. Sometimes the best engineering is simply observing the manual friction around you and writing the code to remove it.

Have you ever automated workflows using Google Sheets and Telegram, or did you go straight for an off-the-shelf CRM?

#googleappsscript #automation #productengineering #buildinpublic #javascript #backend #MoldovaIT #ChisinauTech
