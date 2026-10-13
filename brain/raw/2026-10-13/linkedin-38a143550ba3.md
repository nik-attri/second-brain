---
author: Nick Kavunenko
fetched_at: '2026-10-13T09:52:45.453689Z'
id: 38a143550ba3
lane: lead
published: ''
source: linkedin
title: 'There’s not a single new idea in my AI-development pipeline and that’s exactly
  why it works so well!

  By default, every t'
url: https://www.linkedin.com/posts/nikolay-kavunenko_theres-not-a-single-new-idea-in-my-ai-development-activity-7515701683453227008-gUYN
---

There’s not a single new idea in my AI-development pipeline and that’s exactly why it works so well!
By default, every task in my pipeline goes through seven steps. You’re probably already doing all of them - there’s nothing new here at all. But skipping just one of them cost me the $500 I mentioned in my previous post, when I was testing how autonomous Kiro could build something. 
So, classic steps:
1. Task analysis. Do we even need this? Has it already been done? Does it align with the project goals?
2. Design. What’s the right approach? What are the alternatives? What existing code can we reuse?
3. Design review. A separate agent reviews the design without having participated in creating it or seeing its context. For more complex tasks, I also review it myself.
4. Implementation + tests.
5. Code review. Again, a separate agent with a clean context.
6. Deployment to a test environment.
7. Verification in the test environment that the feature actually works.

The only thing that’s different here is that AI does all seven steps. I use Claude Code or OpenCode with some trick.
Here’s an example of how strict one of these steps can be: design is reviewed by a separate Claude Code instance, following instructions from the architect, plus all the necessary context: project goals and rules, the task itself, and other relevant instructions. It evaluates the design across ten dimensions. The passing score is 90/100. If it doesn’t pass, the plan goes back for revision. There can be multiple rounds and if the AI can’t resolve the issues on its own, only then it asks me for help.

Now, back to the $500 step. That was step 7. It didn’t exist in my previous experiment (in fact Kiro doesn’t really have a pipeline like this at all). So for two weeks, it never actually checked whether the service worked in a real environment.

Today in my process a task isn’t considered done until it has been deployed and verified. Green tests alone are not enough. 

But doing all these steps manually is exhausting. For maximum quality, each step needs a separate session. Builds can take 10–15 minutes or more. A single task can take hours. Running parallel sessions in the same project can interfere with each other, and context gets lost between sessions. Also when you’re doing all of this manually, you naturally start wanting to skip steps. In my next post, I’ll talk about what changes when no single step is allowed to be skipped. 

But for now here’s a question people rarely answer honestly: Which of these seven steps do you skip most often? Just reply with the number.
For me, it was 2 and 3 - I often did them too superficially and rushed straight into implementation.
