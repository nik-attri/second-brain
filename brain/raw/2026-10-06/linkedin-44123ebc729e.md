---
author: Nada Mostafa
fetched_at: '2026-10-06T09:36:31.340105Z'
id: 44123ebc729e
lane: lead
published: ''
source: linkedin
title: 'What if the roof could calculate its own snow-load distribution?

  That question became one of the computational studies b'
url: https://www.linkedin.com/posts/nada-mostafa-hussien_aecsoftware-aecdevelopment-designautomation-activity-7513164569993781248-AGzp
---

What if the roof could calculate its own snow-load distribution?
That question became one of the computational studies behind our ن 𝗡𝗼𝗼𝗻 𝗦𝘁𝘂𝗱𝗶𝗼 submissions to the Abdullatif Al Fozan Award for Mosque Architecture.

With the project located in Turku, Finland, snow was an important environmental and structural condition to account for particularly with a roof composed of hundreds of panels across changing levels and slopes.
Manually defining snow-load zones would mean repeatedly interpreting the geometry, identifying level changes and drift conditions, calculating the corresponding loads, and mapping them back onto the model.

𝗧𝗵𝗶𝘀 𝗼𝗽𝗲𝗻𝗲𝗱 𝗮𝗻 𝗼𝗽𝗽𝗼𝗿𝘁𝘂𝗻𝗶𝘁𝘆 𝗳𝗼𝗿 𝘁𝗵𝗲 𝗽𝗿𝗼𝗰𝗲𝘀𝘀 𝘁𝗼 𝗯𝗲 𝗮𝘂𝘁𝗼𝗺𝗮𝘁𝗲𝗱.
A custom GH-Python script was built in Grasshopper to automate the snow-load analysis, translating EN 1991-1-3 and the Finnish National Annex into a geometry-driven workflow.
the script translates relationships such as:
s = μ · Ce · Ct · sk
and, for snow drift at changes in roof height:
μ₂ = min(2Δh / sk, 8)
into a workflow that responds directly to the roof geometry.
The script reads the 𝗿𝗼𝗼𝗳 𝘀𝘂𝗿𝗳𝗮𝗰𝗲𝘀 𝗱𝗶𝗿𝗲𝗰𝘁𝗹𝘆 𝗳𝗿𝗼𝗺 𝗥𝗵𝗶𝗻𝗼 and analyzes them panel by panel extracting centroids, elevations, and surface slopes, while using the specified wind direction to evaluate spatial relationships between panels.

It then searches for neighboring higher roof levels, evaluates potential drift zones and their distance from the level change, applies the corresponding load profile and slope correction, and calculates a 𝗹𝗼𝗮𝗱 𝗳𝗼𝗿 𝗲𝗮𝗰𝗵 𝗶𝗻𝗱𝗶𝘃𝗶𝗱𝘂𝗮𝗹 𝗽𝗮𝗻𝗲𝗹.

The results are mapped directly back onto the model as numerical values and a 𝗰𝗼𝗹𝗼𝗿-𝗰𝗼𝗱𝗲𝗱 𝟯𝗗 𝗹𝗼𝗮𝗱 𝗺𝗮𝗽, making the analysis immediately readable within the design environment.

We also 𝘁𝗲𝘀𝘁𝗲𝗱 𝘁𝗵𝗲 𝘁𝗼𝗼𝗹 𝗮𝗰𝗿𝗼𝘀𝘀 𝗯𝗼𝘁𝗵 𝗰𝗼𝗺𝗽𝗲𝘁𝗶𝘁𝗶𝗼𝗻 𝗽𝗿𝗼𝗽𝗼𝘀𝗮𝗹𝘀, using different roof geometries to see how the same automated logic responded beyond the model it was initially developed for.

Grateful to Dr. Mohamed Noeman and Toka Hassan Taman for always encouraging us to explore, test, and take these studies further.
Credit to the entire Noon Studio team behind both proposals.
#AECSoftware #AECDevelopment #DesignAutomation #GHPython #Grasshopper #Python #Rhino3D #ComputationalDesign
