---
author: saroosh mehboob
fetched_at: '2026-09-21T08:21:43.783387Z'
id: 7f0e75bed157
lane: lead
published: ''
source: linkedin
title: '🚀 **What if your tests could run automatically every time you pushed code?**


   That was the problem we wanted to solve.'
url: https://www.linkedin.com/posts/saroosh-mehboob-601317211_what-if-your-tests-could-run-automatically-activity-7507708959613423617-CF-v
---

🚀 **What if your tests could run automatically every time you pushed code?**

 That was the problem we wanted to solve.

 Manual testing was taking time, creating bottlenecks, and making it harder to catch issues early.

 So we automated the testing process using **AWS CodeBuild**.

 Here’s how the case study looked 👇

 🔴 **BEFORE: The Problem**

 Our development workflow involved:

 • Manual test execution\
 • Delayed feedback for developers\
 • Higher chances of missing issues\
 • Extra effort before every deployment

 The biggest challenge?

 **Testing was becoming a bottleneck in the development pipeline.**

 🟢 **THE SOLUTION: AWS CodeBuild**

 We integrated automated testing into the CI/CD pipeline using **AWS CodeBuild**.

 The workflow became:

 **Code Push → Build → Automated Tests → Test Results → Deployment**

 Now, whenever developers pushed changes, the testing process could run automatically.

 ⚙️ **HOW IT WORKED**

 1️⃣ Developer pushes code to the repository.

 2️⃣ The CI/CD pipeline triggers CodeBuild.

 3️⃣ CodeBuild prepares the required environment.

 4️⃣ Automated test cases execute.

 5️⃣ Test results determine whether the pipeline should continue.

 6️⃣ Only code that passes the required checks moves forward.

 📈 **THE IMPACT**

 This simple change helped us move from:

 ❌ Manual testing\
 to\
 ✅ Automated testing

 From:

 ❌ Delayed feedback\
 to\
 ✅ Faster feedback

 From:

 ❌ Testing as a separate activity\
 to\
 ✅ Testing as part of the delivery pipeline

 💡 **THE BIGGEST LESSON**

 Automation isn't just about reducing manual work.

 It's about **moving quality checks closer to the moment code is written.**

 The earlier we detect a problem, the easier it is to fix.

 ☁️ **AWS CodeBuild + CI/CD = Faster Feedback + Consistent Testing + Better Developer Experience**

 If you're still running important tests manually before deployment, it may be worth asking:

 **“What part of our testing process can we automate next?”**

 💬 Have you implemented automated testing with AWS CodeBuild?

 What challenges did you face?
