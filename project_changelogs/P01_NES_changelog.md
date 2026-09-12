# NES (P01) Canonical Version Determination and Changelog

**Project:** P01-NES — North East Scotland Creative Industries Mapping
**Date:** 2026-09-08
**Status:** R1.5 pilot — awaiting Iain's confirmation of canonical versions
**Method:** File system inventory + document internal metadata + version-chain analysis. No archive files modified.

## 1. Deliverable streams

The NES project has three distinct deliverable streams, each with its own version chain:

| Stream | Description | Canonical version (proposed) |
|---|---|---|
| A. Main report | Creative industries mapping report | `260605 Mapping_Creative_Industries_report_v3.12.docx` + `.pdf` (Jun 5) |
| B. Policy playbook | Policy recommendations companion | `NES_Policy_Playbook_v3.docx` + `.pdf` (Jun 5) |
| C. Presentation | Client presentation deck | `NorthEastScotland_CreativeIndustries_2026_FINAL.pptx` (Jun 5) |

## 2. Version chain — A. Main report

| Version ID | Date | Document | Label | Internal rev | Paras | Tables | Authority | Superseded by |
|---|---|---|---|---|---|---|---|---|
| NES-R-v01 | 2025-08-10 | `250810 NE Scotland initial CI Mapping.docx` | — | 9 | 462 | 16 | SUPERSEDED | NES-R-v06 |
| NES-R-v02 | 2026-02-03 | `260203 North East Scotland Creative Economy.docx` | — | 7 | 648 | 27 | SUPERSEDED | NES-R-v06 |
| NES-R-v03 | 2026-02-05 | `260204 North East Scotland Creative Economy v2.docx` | v2 | 112 | 209 | 18 | SUPERSEDED | NES-R-v06 |
| NES-R-v04 | 2026-02-05 | `260205North East Scotland Creative Economy v3.docx` | v3 | 81 | 46 | 2 | SUPERSEDED | NES-R-v06 |
| NES-R-v05a | 2026-04-16 | `260416 From_pinning_stones_to_convergence_economy.docx` | — | — | — | — | SUPERSEDED | NES-R-v05c |
| NES-R-v05b | 2026-04-18 | `260418 Pinning_stones_convergence_economy.docx` | — | — | — | — | SUPERSEDED | NES-R-v05c |
| NES-R-v05c | 2026-04-20 | `260420_Pinning_stones_convergence_economy_FINAL.docx` | FINAL | 376 | 679 | 24 | SUPERSEDED (filename "FINAL" does not establish finality) | NES-R-v08 |
| NES-R-v06 | 2026-05-08 | `260508 NES_Creative_Industries_Report.docx` | — | 2 | 524 | 18 | SUPERSEDED | NES-R-v08 |
| NES-R-v06b | 2026-05-09 | `260508 NES_Creative_Industries_Report_IB.docx` | — | 117 | 539 | 20 | SUPERSEDED (IB = Iain Bennett revision) | NES-R-v08 |
| NES-R-v07a | 2026-05-12 | `main_report_reconciled_v1.docx` | v1 | 22 | 828 | 16 | SUPERSEDED | NES-R-v08 |
| NES-R-v07b | 2026-05-12 | `main_report_reconciled_v1.2.docx` | v1.2 | 58 | 728 | 24 | SUPERSEDED | NES-R-v08 |
| NES-R-v07c | 2026-05-30 | `main_report_v2.docx` | v2 | — | 1528 | 0 | SUPERSEDED | NES-R-v08 |
| NES-R-v07d | 2026-06-02 | `260601 main_report_v2_31May2026_0911.docx` | v2 | 32 | 1571 | 12 | SUPERSEDED | NES-R-v08 |
| NES-R-v08a | 2026-06-04 | `260602 Mapping_Cretive_Industries_report_v3.10.docx` | v3.10 | 21 | 735 | 24 | SUPERSEDED | NES-R-v08c |
| NES-R-v08b | 2026-06-05 | `main_report_v3.11.docx` | v3.11 | 116 | 667 | 24 | SUPERSEDED | NES-R-v08c |
| **NES-R-FINAL** | 2026-06-05 | `260605 Mapping_Creative_Industries_report_v3.12.docx` + `.pdf` | v3.12 | 3 | 709 | 28 | **CANONICAL (proposed)** | — |

**Notes:**
- The "Pinning Stones" naming (v05a–v05c, Apr 16–20) was the first titled report frame. The "FINAL" label on v05c was premature — at least 8 later versions exist.
- The "Mapping Creative Industries" naming (v08a–v08c, Jun 4–5) replaced "Pinning Stones" as the report title.
- v3.12 has both DOCX and PDF, suggesting a rendered final. Internal metadata shows `author=python-docx`, `rev=3`, indicating script-generated rendering.
- No files later than Jun 5 exist in any NES subfolder that are versions of the main report.

## 3. Version chain — B. Policy playbook

| Version ID | Date | Document | Label | Authority | Superseded by |
|---|---|---|---|---|---|
| NES-P-v01 | ~Apr 17 | `NES_Creative_Industries_Policy_Playbook.docx` | — | SUPERSEDED | NES-P-v03 |
| NES-P-v02a | 2026-04-17 | `260417 NES_Creative_Industries_Policy_Playbook_v2.docx` | v2 | SUPERSEDED | NES-P-v03 |
| NES-P-v02b | 2026-04-17 | `260417 NES_Creative_Industries_Policy_Playbook_v2.1.docx` | v2.1 | SUPERSEDED | NES-P-v03 |
| NES-P-v02c | 2026-04-17 | `260417 NEScotland Creative Industries Playbook and RES recommendationsv2.docx` | v2 | SUPERSEDED | NES-P-v03 |
| NES-P-v02d | 2026-04-20 | `260420_NES_Policy_Playbook_tracked_changes.docx` | tracked | SUPERSEDED | NES-P-v03 |
| NES-P-v02e | ~May 12 | `NES_Policy_Playbook_v2.docx` (in Reports/) | v2 | SUPERSEDED | NES-P-v03 |
| **NES-P-FINAL** | 2026-06-05 | `NES_Policy_Playbook_v3.docx` + `.pdf` | v3 | **CANONICAL (proposed)** | — |

## 4. Version chain — C. Presentation

| Version ID | Date | Document | Label | Authority | Superseded by |
|---|---|---|---|---|---|
| NES-PR-v01 | 2025-08-12 | `250812 NE Scotland initial mapping v2.pptx` | v2 | SUPERSEDED (initial mapping presentation) | NES-PR-v03 |
| NES-PR-v02a | 2026-06-05 | `NES_Creative_Economy_2026.pptx` | — | SUPERSEDED | NES-PR-v03 |
| NES-PR-v02b | 2026-06-05 | `NES_Creative_Economy_2026_granite-flame.pptx` | granite-flame | SUPERSEDED (template variant) | NES-PR-v03 |
| **NES-PR-FINAL** | 2026-06-05 | `NorthEastScotland_CreativeIndustries_2026_FINAL.pptx` | FINAL | **CANONICAL (proposed)** | — |

## 5. Changelog — method and content evolution

This is a hypothesis-generating analysis based on file dates, titles, and metadata. Confidence is MEDIUM unless noted. Full content comparison has not been performed.

### Phase 1: Initial mapping (Aug 2025)
- **Method:** Data-driven CI mapping using SIC codes, company data, and sector composition analysis.
- **Spillover framing:** Not evident in the initial mapping title or structure.
- **Option framing:** Not evident.
- **Confidence:** LOW (title and metadata only; content not compared).

### Phase 2: Creative Economy drafting (Feb 2026)
- **Method:** Shift from "CI Mapping" to "Creative Economy" framing. Multiple rapid versions (v1, v2, v3 in 2 days). High revision counts (v2: rev=112) suggest intensive iterative drafting.
- **Spillover framing:** "Reconciling the Digital Creative overlap" (Feb 5) suggests cross-sector overlap analysis was introduced — a potential spillover identification point.
- **Option framing:** "Options assessment" document appears Mar 9 (`260309 North East Scotland Options assessment.docx`), suggesting strategic option analysis was introduced in this phase.
- **Breakthrough flag:** Cross-sector overlap reconciliation (Feb 5) may mark the point where digital-creative crossover was first recognised as a spillover mechanism.
- **Confidence:** MEDIUM (file titles are indicative; content not compared).

### Phase 3: Pinning Stones (Apr 2026)
- **Method:** Major reframing — "From Pinning Stones to Convergence Economy" as the report title. This appears to be a significant narrative and structural shift, not just a version increment.
- **Spillover framing:** "Convergence economy" framing implies cross-sector spillovers are central to the argument.
- **Option framing:** Policy Playbook v2 (Apr 17) accompanies this version, suggesting policy recommendations (potentially including options) were formalised.
- **Breakthrough flag:** The "convergence economy" concept (Apr 16) may mark a breakthrough in framing spillovers as an economic narrative rather than just a mapping observation.
- **Confidence:** MEDIUM (title change is clear; content evolution not yet compared).

### Phase 4: Reconciliation and revision (May 2026)
- **Method:** "Reconciled" versions (May 12) suggest integration of feedback or data sources. The v1→v1.1→v1.2 progression (same day) indicates rapid iteration. Paragraph count dropped from 828 (v1) to 728 (v1.2) — possible tightening/trimming.
- **Spillover framing:** "Comment concordance" files (May 8–10) suggest client/stakeholder feedback was being addressed, potentially affecting spillover claims.
- **Option framing:** "Options assessment tables" (May 12) suggests option analysis was being formalised in table format.
- **Breakthrough flag:** "David Officer comments addressed" (May 7) and "DO_Comment_Response_Concordance" (May 10) suggest a specific reviewer's feedback drove changes. The nature of those changes is a key analytical question.
- **Confidence:** MEDIUM (file titles indicate feedback integration; content not compared).

### Phase 5: v3 sequence and final (Jun 2026)
- **Method:** Complete rebuild as "Mapping Creative Industries" (dropping "Pinning Stones" title). v3.0→v3.3→v3.6→v3.9→v3.10→v3.11→v3.12 in 3 days, with both Markdown drafting and DOCX rendering. Tables increased from 24 (v3.10) to 28 (v3.12), suggesting data/analysis was added.
- **Spillover framing:** "Convergence" concept retained but title simplified. The "granite-flame" template suggests a branded final presentation.
- **Option framing:** Policy Playbook v3 (Jun 5) accompanies the final report, suggesting options were finalised alongside.
- **Breakthrough flag:** The v3 rebuild (Jun 3–5) may represent a structural breakthrough — a complete reorganisation of the report. The change from 1528 paragraphs (v2, no tables) to 735 paragraphs with 24 tables (v3.10) suggests a shift from narrative to structured/data-driven reporting.
- **Confidence:** MEDIUM (structure change is clear from metadata; content not compared).

## 6. Analytical observations

1. **Title evolution as a signal:** "CI Mapping" → "Creative Economy" → "Pinning Stones / Convergence Economy" → "Mapping Creative Industries". Each title change may signal a methodological or framing shift. The dropping of "Pinning Stones" in the final version is notable — the narrative frame was abandoned in favour of a more conventional mapping title.

2. **Spillover identification timeline (hypothesised):**
   - Feb 5: Digital-creative crossover recognised (potential first spillover identification)
   - Apr 16: "Convergence economy" framing (spillovers elevated to central narrative)
   - Jun 3–5: v3 rebuild (spillover analysis may have been restructured)

3. **Strategic option timeline (hypothesised):**
   - Mar 9: First "Options assessment" document
   - Apr 17: Policy Playbook v2 (options formalised in policy recommendations)
   - May 12: Options assessment tables
   - Jun 5: Policy Playbook v3 (final options)

4. **Version stability:** The "FINAL" label on Pinning Stones (Apr 20) was followed by 8+ versions over 6 weeks. This is a clear case study in why filename labels do not establish authority.

5. **Key analytical questions for R3:**
   - What did the "convergence economy" framing add that the original mapping lacked?
   - What feedback drove the v3 rebuild?
   - Which spillover claims survived from early drafts to v3.12, and which were added late?
   - Did the option analysis change between the Mar 9 assessment and the final Policy Playbook v3?

## 7. Confirmation requested

1. Confirm v3.12 (Jun 5) as canonical for the main report, Policy Playbook v3 for the playbook, and `NorthEastScotland_CreativeIndustries_2026_FINAL.pptx` for the presentation.
2. Confirm there are no later versions outside the checked folders.
3. Confirm the three-stream deliverable structure is correct, or identify additional deliverables.
4. After confirmation, I will create the `canonical/` subfolder with copies and proceed to the other 9 projects.
