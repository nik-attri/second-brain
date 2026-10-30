---
author: Viikas Gaurav
fetched_at: '2026-10-30T09:17:14.640397Z'
id: da7be6a62dd6
lane: lead
published: ''
source: linkedin
title: 'IFC Geometry: Mesh vs. Solid — Is One Always Better for Railway BIM?

  In railway BIM, the choice between mesh-based geome'
url: https://www.linkedin.com/posts/vikas-sinha-cartotech_railwaybim-openraildesigner-infrastructurebim-activity-7521861634525687808-fx29
---

IFC Geometry: Mesh vs. Solid — Is One Always Better for Railway BIM?
In railway BIM, the choice between mesh-based geometry and solid modelling is not simply a question of software capability; it is a question of modelling methodology, design intent and downstream requirements.

While developing railway infrastructure models using Bentley OpenRail Designer, we leverage advanced corridor modelling driven by horizontal and vertical alignments, templates and parametric design rules. This approach generates track components such as rails, sleepers, ballast and sub-ballast as tessellated mesh geometry during IFC export.

The real engineering advantage lies in its dynamic design behaviour. When an alignment, cross-section or track template changes, the corridor can be regenerated efficiently, updating the associated components without manually rebuilding individual elements. This is particularly valuable in complex railway projects where design iterations are inevitable.

Does this mean solids are unnecessary? 
Absolutely not. If the project requires solid-based IFC geometry for specific downstream applications, solids can be extracted from the existing corridor and assigned the required IFC classifications and Property Sets (PSets). Alternatively, components can be developed through dedicated 3D solid modelling.

Our position is simple: BIM geometry should serve the engineering workflow, not just satisfy a visual representation requirement. The right approach must balance parametric design flexibility, IFC interoperability, information richness and downstream usability.

We welcome other technical perspectives, experiences and arguments from railway designers, BIM specialists and IFC professionals. 

Do you prefer mesh-based or solid-based geometry for railway infrastructure, and why? Let's exchange views and learn from different project requirements.
Visit us: www.carto-tech.com
For technical discussions and collaboration: vikas@carto-tech.com
#RailwayBIM #OpenRailDesigner #InfrastructureBIM #BIMInteroperability #DigitalEngineering
