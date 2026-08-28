---
author: Milad Eidi
fetched_at: '2026-08-28T14:42:55.599506Z'
id: ecca9f8c03cc
lane: lead
published: ''
source: linkedin
title: Sometimes the difference between finding the right candidate gene and missing
  it starts before the VCF is even analyzed.
url: https://www.linkedin.com/posts/milad-eidi-27a14a135_varsage-hpo-raredisease-activity-7499107615881338880-ygfc
---

Sometimes the difference between finding the right candidate gene and missing it starts before the VCF is even analyzed.
It starts with how we describe the patient!

A clinical note might say:
“The child started walking late, has poor balance and recurrent seizures.”
For computational analysis, that description becomes much more useful when translated into standardized Human Phenotype Ontology (HPO) terms.

Why does this matter?
Because phenotype-driven prioritization asks a very practical question:
Do the known effects of this gene actually resemble what we see in this patient?
HPO has become a core framework for representing clinical phenotypes in rare-disease genomics [1], and recent studies continue to show the value of phenotype information for prioritizing candidate genes and identifying causal disease genes [2,3].

But manually converting every clinical description into HPO terms is not always easy.
Symptoms may be written informally, described with synonyms, buried in long notes, or expressed in ways that do not exactly match an HPO label.

That is why I added clinical-description-to-HPO extraction by AI in VarSage.
The user can simply describe the case in whatever words they want.
VarSage first looks for HPO terms and synonyms directly. AI will interpret complex natural-language descriptions and suggest additional HPO terms.
The extracted terms are then shown to the analyst for review before they are used in the analysis.

Those phenotype terms contribute to gene-phenotype matching and help prioritize variants whose genes better fit the patient's clinical presentation.
The idea is simple:
Clinical description -> HPO profile -> phenotype-gene matching -> better candidate prioritization

AI is useful here not because it should decide which variant is causal, but because it can help transform messy clinical language into structured information that genomic analysis can actually use.
And importantly, the analyst remains in control of the HPO profile.

reach out this functionality here:
🔗 www.varsage.app

[1] Gargano MA, et al. The Human Phenotype Ontology in 2024: phenotypes around the world. Nucleic Acids Research. 2024.
[2] Kim J, et al. Assessing the utility of large language models for phenotype-driven gene prioritization in the diagnosis of rare genetic disease. AJHG. 2024.
[3] Alsentzer E, et al. Few shot learning for phenotype-driven diagnosis of patients with rare genetic diseases. npj Digital Medicine. 2025.
[4] Yang J, et al. Enhancing phenotype recognition in clinical notes using large language models: PhenoBCBERT and PhenoGPT. Patterns. 2024.
#VarSage #HPO #RareDisease #Bioinformatics #Genomics #VariantPrioritization #ClinicalGenomics #HumanGenetics #AIinHealthcare
