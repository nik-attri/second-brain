---
author: Dmytro Yeremenko
fetched_at: '2026-10-09T09:48:29.164826Z'
id: 058c1929fad3
lane: lead
published: ''
source: linkedin
title: Splitting the creation of a 3D asset into stages turned out not to be the hardest
  part. The more interesting challenge w
url: https://www.linkedin.com/posts/dmytro-yeremenko_splitting-the-creation-of-a-3d-asset-into-activity-7514252917747568640-bAYa
---

Splitting the creation of a 3D asset into stages turned out not to be the hardest part. The more interesting challenge was figuring out how to properly hand work over between people.
Imagine a common situation. One artist takes the Retopology stage. They finish half the work, but cant continue today. Meanwhile, another team member is available and could finish that stage.
What happens next?
In a typical workflow, the messages start: Where is the file? Which version is the latest? Whats already done? Whats left to do? Can someone else even touch this model?
Now imagine there are ten assets instead of one. And people are working on them from different countries, at different times, with different schedules.
This is where I started separating two very different actions.

Save Progress — the artist saves their current work. Its not finished yet, but its state is recorded. They can return to it later, or someone else can pick up where they left off.

Submit — the artist considers their stage complete and sends the result for review. This distinction matters.
Saving progress doesnt automatically mean the work is ready for the next production stage.
For example, another artist can continue unfinished Retopology. But the UV stage shouldnt become available just because someone saved a file. First, Retopology needs to be completed and reviewed.
So were not just passing a file between people.
Were passing the file along with its state, version, and a clear understanding of what can happen with it next.
For me, this is gradually becoming one of the core principles behind the Production Room in SEN.

An artist shouldnt have to figure out the entire history of a model. They should be able to open an available task, know which version to continue from, and understand whats expected of them.
Now imagine this process happening directly inside DCC(Blender). Get the latest version, do your part, save your progress, or submit the stage for review — without constantly switching between applications or manually searching for files.
Thats the kind of workflow Im currently working toward. But another interesting thought came out of this.If we preserve not only the versions of the work, but also the history of reviews, feedback, and corrections, then this process becomes useful for more than just production. 
It becomes something people can learn from. And not necessarily only from their own mistakes.
I'll come back to that part separately.
