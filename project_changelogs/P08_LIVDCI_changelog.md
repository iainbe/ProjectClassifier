# Liverpool DCI (P08) Canonical Version Determination and Changelog

**Project:** P08-LIVDCI — Liverpool City Region Digital & Creative Industries Cluster Mapping
**Date:** 26/09/08
**Status:** R1.5 batch 3 — use both (proposal + final report), confirmed by Iain
**Method:** File system inventory + document internal metadata + version-chain analysis. No archive files modified.

## 1. Deliverable streams

The LIVDCI project has three distinct deliverable streams, each with its own version chain:

| Stream | Description | Canonical version (proposed) |
|---|---|---|
| A. Final report | Digital and creative cluster mapping report | `LiverpoolCityRegion_DigitalCreative_final.docx` + `.pdf` (24/07/08, rev=104, 844 paras, 27 tables, 85 pages) |
| B. Proposal | Fifth Sector's proposal | `240105 LCR DCI Cluster mapping_TheFifthSector.docx` (24/01/05, rev=307, 274 paras, 1 table) — R2 source |
| C. Changes document | Final report changes | `240708 LCR Digital final report changes.docx` (24/07/08, rev=30, 3 paras, 1 table) |

## 2. Version chain — A. Final report

| Version ID | Date | Document | Paras | Tables | Authority | Superseded by |
|---|---|---|---|---|---|---|
| LIVDCI-A-v01 | 24/06/04 | `LCR DCI final report outline.docx` | 597 | 5 | SUPERSEDED (outline, rev=723) | LIVDCI-A-FINAL |
| LIVDCI-A-v02 | 24/06/05 | `240604 LCR digital and creative cluster mapping.docx` | 617 | 5 | SUPERSEDED (rev=77) | LIVDCI-A-FINAL |
| LIVDCI-A-v03 | 24/06/06 | `240606 LCR_digitalcreativecluster-mapping.docx` | 588 | 5 | SUPERSEDED (rev=2) | LIVDCI-A-FINAL |
| LIVDCI-A-v04 | 24/06/06 | `Liverpool City Region DigitalCreative draft.docx` | 705 | 6 | SUPERSEDED (draft, rev=290) | LIVDCI-A-FINAL |
| **LIVDCI-A-FINAL** | 24/07/08 | `LiverpoolCityRegion_DigitalCreative_final.docx` + `.pdf` | 844 | 27 | **CANONICAL** (85-page PDF) | — |

**Notes:**
- The final report went through outline → draft → final in about a month (Jun 4–Jul 8).
- Paragraph count grew significantly: 597 (outline) → 617–705 (drafts) → 844 (final).
- Table count grew dramatically: 5 (outline/drafts) → 27 (final), indicating substantial data content was added in the final phase.
- 27 tables in the final report indicates substantial data content.
- Both DOCX and PDF exist for the final, suggesting a rendered final.

## 3. Version chain — B. Proposal

| Version ID | Date | Document | Paras | Tables | Authority | Superseded by |
|---|---|---|---|---|---|---|
| **LIVDCI-B-FINAL** | 24/01/05 | `240105 LCR DCI Cluster mapping_TheFifthSector.docx` | 274 | 1 | **CANONICAL (proposed)** (R2 source, rev=307) | — |

**Notes:**
- The proposal has rev=307 — extremely high revision count for a proposal. This suggests extensive iterative drafting before submission.
- The R2 source (proposal, 274 paras, 1 table) is much smaller than the final report (844 paras, 27 tables, 85 pages).

## 4. Version chain — C. Changes document

| Version ID | Date | Document | Paras | Tables | Authority | Superseded by |
|---|---|---|---|---|---|---|
| **LIVDCI-C-FINAL** | 24/07/08 | `240708 LCR Digital final report changes.docx` | 3 | 1 | **CANONICAL (proposed)** (rev=30) | — |

**Notes:**
- A very short document (3 paras, 1 table) — likely a summary of changes made to the final report.

## 5. R2 manifest impact

SRC-R2-09 covers both the proposal (B) and the final report (A). Iain confirmed "use both" — the R2 test uses the proposal as the R2 test source (testing proposal vs delivery) and the final report as the canonical deliverable.

## 6. Changelog — method and content evolution

This is a hypothesis-generating analysis based on file dates, titles, and metadata. Confidence is MEDIUM unless noted. Full content comparison has not been performed.

### Phase 1: Proposal (24/01)
- **Method:** Fifth Sector submitted a proposal (24/01/05, 274 paras, 1 table, rev=307). The extremely high revision count suggests intensive iterative drafting.
- **Spillover framing:** Not evident from title. Requires content review.
- **Option framing:** Not evident from title.
- **Confidence:** LOW (title and metadata only; content not compared).

### Phase 2: Outline and drafting (24/06)
- **Method:** Rapid progression from outline (Jun 4, 597 paras, 5 tables) through multiple drafts (Jun 5–6) to a more developed draft (Jun 6, 705 paras, 6 tables). The outline → draft sequence happened in 2–3 days.
- **Spillover framing:** Not evident from titles. Requires content review.
- **Option framing:** Not evident from titles.
- **Breakthrough flag:** The rapid outline-to-draft progression (Jun 4–6) suggests a well-defined method was applied quickly.
- **Confidence:** MEDIUM (file dates and paragraph/table counts are indicative; content not compared).

### Phase 3: Final report (24/07)
- **Method:** Final report produced 24/07/08 (844 paras, 27 tables, 85 pages). The jump from 6 tables (draft) to 27 tables (final) indicates substantial data/analysis was added in the final phase (~4 weeks after the last draft). A changes document was also produced (3 paras, 1 table).
- **Spillover framing:** Not evident from title. Requires content review.
- **Option framing:** Not evident from title.
- **Breakthrough flag:** The table count jump (6 → 27) in the final phase suggests significant data analysis was added, potentially including cluster mapping data, economic metrics, or comparative tables.
- **Confidence:** MEDIUM (structure change is clear from metadata; content not compared).

## 7. Analytical observations

1. **Proposal vs delivery gap:** The R2 source (proposal, 274 paras, 1 table) is much smaller than the final report (844 paras, 27 tables, 85 pages). The R2 diagnostic (R2-T02) tests "identify one atomic proposition about method reuse/role, and separate what the supplier proposal reports from independently verified delivery."

2. **High proposal revision count:** The proposal has rev=307 — extremely high revision count for a proposal. This suggests the proposal went through extensive iteration before submission.

3. **Rapid final report development:** The final report went through outline → draft → final in about a month (Jun 4–Jul 8). The table count jump (5 → 27) in the final phase is notable.

4. **Substantial data content:** 27 tables in the final report indicates substantial data content — likely cluster mapping data, economic metrics, or comparative analysis.

5. **Key analytical questions for R3:**
   - Was the final report accepted by the client?
   - What is the current status of the LCR DCI commission?
   - What did the 22 additional tables (draft → final) contain?

## 8. UNRESOLVED items

1. ~~Was the final report accepted by the client?~~ RESOLVED: Report accepted by client (confirmed by Iain, 26/09/09).
2. What is the current status of the LCR DCI commission?

## R3 card walkthrough (26/09/12)

- **Resolved:** Rating split approved by Iain — precedent_strength STRONG (PRIME + accepted + innovative method), evidence_strength MEDIUM (headline GVA is modelled estimate).
- **Register repair:** contracting_role=PRIME, prime_contractor=The Fifth Sector (VAL-R3-015 now correctly landed).
- **Card corrections:** 77,252 corrected to GVA per capita (was misread as workforce total); circular reuse claim fixed (method originated P04-GBSLEP 2017); £77,252 GVA/capita added to quantified_results.
- **Status:** Index card REVIEWED.

## citation_status recorded (26/09/16)

- `citation_status` added to the index card: DELIVERED_WORK — completed as PRIME, no publication evidence.
- Evidence: `01_projects.csv` lifecycle_status + `09_publication_assets.csv` (TENDER_ONLY_NOT_WEBSITE). Derived by Devin, pending Iain confirmation.
- `reference_permission` unchanged — citation status is not permission to name the client.
