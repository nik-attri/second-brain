---
author: Prathamesh Patil
fetched_at: '2026-10-20T08:01:46.114161Z'
id: 49dcaf280214
lane: lead
published: ''
source: linkedin
title: '𝗚𝗶𝘁𝗛𝘂𝗯 𝗔𝗰𝘁𝗶𝗼𝗻𝘀 𝘁𝗼 𝘀𝗲𝗰𝘂𝗿𝗲𝗹𝘆 𝗽𝘂𝗯𝗹𝗶𝘀𝗵 𝗻𝗽𝗺 𝗽𝗮𝗰𝗸𝗮𝗴𝗲𝘀


  GitHub Actions to securely publish npm packages Written by Liran Tal No'
url: https://www.linkedin.com/posts/prathameshpatil5090_codingtips-100daysofcode-learntocode-activity-7518212871630188544-dhNq
---

𝗚𝗶𝘁𝗛𝘂𝗯 𝗔𝗰𝘁𝗶𝗼𝗻𝘀 𝘁𝗼 𝘀𝗲𝗰𝘂𝗿𝗲𝗹𝘆 𝗽𝘂𝗯𝗹𝗶𝘀𝗵 𝗻𝗽𝗺 𝗽𝗮𝗰𝗸𝗮𝗴𝗲𝘀

GitHub Actions to securely publish npm packages Written by Liran Tal November 10, 2020 0 mins read GitHub Actions are growing in popularity ever since GitHub announced general availability for all developers and repositories on the GitHub platform. Fueled with some rate limits we’re seeing in the ecosystem, such as new billing and rate limits for open source from Travis CI, will further drive developers to migrate their software automations to GitHub Actions. In this article, I’d like to show you how I’m using GitHub Actions to publish npm packages that I maintain in my open source projects. If you’re following the GitHub flow which consists of GitHub pull requests workflows, then this will further unify your experience around GitHub workflows for your teams and community contributors in your project. What is GitHub Actions? GitHub Actions is a technology developed by GitHub to provide developers with a way to automate their workflows around continuous integration, helping them build, deploy, schedule recurring tasks, and more. GitHub Actions is natively available and integrated into GitHub repositories and features many reusable workflows from community contributors, such as publishing npm packages, publishing docker images, running security tests , and more. How do actions work in GitHub? GitHub’s cloud infrastructure is running GitHub Actions for users by creating a workflow file in a GitHub repository directory named .github/workflows , describing the trigger, schedule for the job, and the actions the job should take using YAML. What is a GitHub workflow? A GitHub workflow is a set of jobs that would run based on a trigger or a cron-based schedule. A job consists of one or more steps that make up an automated workflow. Setting up a Node.js project for GitHub Actions Let’s add an initial GitHub Actions automation to a Node.js project. The GitHub Actions job will install all required npm packages, run tests, and eventually publish our project as an npm package that users can consume. Our npm package is going to be a Command Line Interface (CLI) for you to browse the amazing list of talks from SnykCon 2020, Snyk’s first-ever global security event that took place in 2020. The complete project is hosted on GitHub . Here&#x27;s a sneak peek at how the npm package looks: A complete GitHub CI workflow starts off with creating the following GitHub Action file at the root of the repository path: .github/workflows/main.yml name: main on: [ push ] jobs: build: runs, on: ubuntu, latest strategy: matrix: node, version: [ 12. x , 14. x ] steps:, uses: actions / checkout @ v2, name: Build on Node . js $ {{ matrix . node, version }} uses: actions / setup, node @ v1 with : node, version: $ {{

#CodingTips #100DaysOfCode #LearnToCode #Tip #BuildInPublic #LearnInPublic
