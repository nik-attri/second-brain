---
author: MIDAS IT EUROPE
fetched_at: '2026-09-10T07:37:49.463680Z'
id: 5df63a6a4417
lane: lead
published: ''
source: linkedin
title: '📐 MIDAS CIVIL NX Feature Focus: Part 3


  "Which load case is actually driving this moment?"


  It is one of the most common'
url: https://www.linkedin.com/posts/midas-it-europe_midascivilnx-bridgeengineering-structuralengineering-activity-7503710421632151553-B9Mv
---

📐 MIDAS CIVIL NX Feature Focus: Part 3

"Which load case is actually driving this moment?"

It is one of the most common questions in a design review, and one of the most tedious to answer by hand.

When a girder moment is governed by multiple load cases, what matters for the calculation package is not only the total. It is which case produced which part of it: the traffic envelope, the temperature term, or something else, and by how much.

Answering that manually means re-running every constituent load case, putting the results in a table, applying the factors, and hoping your totals agree with the solver.

MIDAS CIVIL NX now answers it directly.

The Load Combination Contribution Analyzer, developed for MIDAS CIVIL NX 2026:
▸ reads the combination from the model
▸ resolves any nested sub-combinations
▸ reports the signed contribution of every constituent load case, at every output location

Then it checks its own work. It rebuilds the combination from those contributions and compares it with what CIVIL NX itself reports, before showing any result. That check always runs and cannot be disabled.

𝗪𝗵𝗮𝘁 𝗺𝗮𝗸𝗲𝘀 𝘁𝗵𝗲 𝗼𝘂𝘁𝗽𝘂𝘁 𝘂𝘀𝗮𝗯𝗹𝗲
✅ Complete coverage, not a spot check — each element, part and component
✅ Sub-combinations handled correctly — load cases appearing through multiple branches are accumulated correctly
✅ Beyond screen precision — results requested at nine significant figures, so rounding never explains the gap
✅ CSV export — units, precision and the combination tree included, so the table can be read independently

Want to see the decomposition run on a real bridge model? Get in touch for a walkthrough.

So - when a combination result surprises you, do you accept the envelope value, or stop to find out which case is actually driving it? 
We would like to hear how you check governing cases in your own models. 👇

💻 Try MIDAS CIVIL NX: https://lnkd.in/eq7Vrr48

#MIDASCivilNX #BridgeEngineering #StructuralEngineering #LoadCombinations #FEM #Eurocode
