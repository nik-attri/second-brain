---
author: Dilen C.
fetched_at: '2026-09-05T07:12:59.562697Z'
id: 8f18e843c9cb
lane: lead
published: ''
source: linkedin
title: 'Have we been misusing the term “reduced FEM”? 🤨


  For the first few years of my career in the space industry, I certainly'
url: https://www.linkedin.com/posts/activity-7501889366651449345-KiUj
---

Have we been misusing the term “reduced FEM”? 🤨

For the first few years of my career in the space industry, I certainly was.

When I started working in #space, engineers around me referred to a coarser and simplified version of a detailed finite element model as the “reduced FEM.”

So naturally, I followed suit.

Take a detailed model with 500,000 elements.

Remove geometric detail.
Coarsen the mesh.
Replace some solids with shells or beams.
Simplify fasteners and interfaces.
Replace detailed equipment with concentrated masses.

You might end up with 20,000 elements.

We called that the reduced FEM.

And intuitively, it makes sense:

500,000 elements → 20,000 elements = reduced FEM. Right? 💩

It was only when I later worked on a project with Airbus that I realised there was an important distinction I had been overlooking.🤔

Making a #FEM smaller is not necessarily the same thing as performing model reduction.

A manually simplified or coarsened model is still fundamentally a physical FEM. It just contains fewer physical elements and DOFs.

I would now be more inclined to call that a:

simplified FEM
or
coarse/system-level FEM

A mathematically reduced-order model is something different. Take Craig–Bampton Component Mode Synthesis.

Instead of manually rebuilding the structure with fewer elements, we start from the detailed system and transform its behaviour into a much smaller set of retained interface DOFs and generalised modal coordinates.

Conceptually:

Detailed FEM

500,000 physical DOFs

↓

#Craig–Bampton reduction

Interface DOFs + retained modes

↓

A few hundred retained/generalised DOFs

with:

Mᵣ = TᵀMT

Kᵣ = TᵀKT

So both models may be dramatically smaller than the original, but they got there through very different routes:

Simplification:
Reduce the physical representation.

Model reduction:
Reduce the mathematical order of the system.

That Airbus project changed the terminology I use today.

It also reminded me of something that happens surprisingly often in engineering: we can use a term for years, everyone around us understands what we mean, and then one project exposes a completely different interpretation of the same term.

So I’m curious how other #FEA and #structural #dynamics #engineers use it:

If you manually simplify a 500,000-element FEM into a 20,000-element physical model, do you call it a “reduced FEM”?

Or should reduced FEM be reserved for a model produced through mathematical reduction/condensation?

#FEA #FiniteElementAnalysis #StructuralDynamics #ModelReduction #CraigBampton #ComponentModeSynthesis #Nastran #SpaceEngineering #SpacecraftStructures
