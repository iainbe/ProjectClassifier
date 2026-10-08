# Consistency audit — 2026-07-31

## Content checks

| Check | Status | Evidence |
|---|---|---|
| Plain-English proposition | PASS | Slide 2 |
| Intended users identified | PASS | Slide 3 |
| Places explained as location/place intelligence | PASS | Slides 4, 7–9; Slide 7 includes source Slide 05 map |
| Circuits explained as connections/network intelligence | PASS | Slides 4, 11–14; Slide 14 includes source Slide 28 map |
| How the platform is used | PASS | Slide 5 |
| Policy-maker benefits | PASS | Slides 15, 17 |
| Direct-beneficiary benefits | PASS | Slide 15 |
| Social-benefits statement in Circuits section | PASS | Slide 13 |
| Evidence limitations retained | PASS | Slides 12, 14, 16 and Appendix slides 20–21 |
| Current-state maturity explained | PASS | Slide 18 and Appendix |
| Technical readiness appendix labelled | PASS | Slides 19–22 |

## Language checks

- PASS — Main narrative avoids internal terms such as “renderer”, “product instance”, “claim ceiling”, “fail closed” and “sealed activation”.
- PASS — “Observed” is used for programme/listing patterns.
- PASS — Social benefits are framed as potential benefits of better evidence and decisions, not automatic platform outcomes.
- PASS — Places and Circuits are used consistently as the two complementary views.
- PASS — Client Slide 08 explicitly names Graphs and pairs the concept with the source Slide 09 Graph image.
- PASS — Client Slides 07, 08 and 14 each contain one embedded source-deck image, with captions explaining the client relevance.
- PASS — Slide 07 uses the source Slide 05 Places map; Slide 08 uses the source Slide 09 Graph view; Slide 14 uses the source Slide 28 Circuits map.

## Visual checks

- PASS — Structural PPTX check: 22 slides reopened successfully; no shapes extend outside slide bounds; no text box exceeded the review threshold.
- PASS — Quick Look thumbnail generated successfully and the first slide was visually inspected for hierarchy, contrast and legibility.
- PASS — Social-benefits card was inspected at rendered scale and remains prominent on slide 13.
- NEEDS REVIEW — PowerPoint PDF export was attempted but the active PowerPoint session returned the source deck rather than the client deck. Open the client deck directly in PowerPoint/Keynote and review all 22 slides before external delivery.

## Open issues

- The deck was generated with python-pptx; a final render in PowerPoint/Keynote or another office renderer is required before delivery.
- Speaker notes have not been added; detailed caveats are visible in the appendix and on relevant slides.
