# P10-KIRK — Kirklees Creative Economy: Canonical Version Determination and Changelog

**Project:** P10-KIRK — Kirklees Creative Industries Mapping (three reports: 2022, 2024, 2026)
**Date:** 2026-09-09
**Status:** R1.5 special batch — three reports identified by Iain as a method evolution case study. Removed from batch 3 and treated separately.
**Method:** File system inventory + document internal metadata + version-chain analysis across three reporting cycles.

## 1. Deliverable structure

Kirklees has THREE separate reports across three years, each with its own version chain. This makes P10-KIRK uniquely valuable as a method evolution case study within the pilot.

| Report cycle | Date range | Canonical version | Paras | Tables | Pages |
|---|---|---|---|---|---|
| 2022 report | Jun 2022 | `2206 Kirklees Creative Economy final report.docx` + `.pdf` | 430 | 8 | 44 |
| 2024 update | Jul–Sep 2024 | `240718 Kirklees Creative Economy 2024 final.docx` + `.pdf` | 544 | 19 | 48 |
| 2026 report | May 2026 | `260528 Kirklees-creative-industries-economic-impact-report-2026-FINAL.docx` + `.pdf` | 608 | 21 | 73 |

**Method evolution signal:** Each report is larger and more data-rich than the previous one. Paragraph count grew 430→544→608 (+41%). Table count grew 8→19→21 (+163%). Page count grew 44→48→73 (+66%).

## 2. Version chain — 2022 report

| Version ID | Date | Document | Label | Paras | Tables | Authority |
|---|---|---|---|---|---|---|
| KIRK-2022-v01 | 2022-03-22 | `150622 Kirklees 2015 Creative Economy Report BOP Consulting_corrected.docx` | — | 687 | 15 | SUPERSEDED (2015 BOP report, corrected) |
| KIRK-2022-v02 | 2022-06-22 | `2206 Kirklees Creative Economy final report_HB[40].docx` | FINAL | 386 | 8 | SUPERSEDED (HB version) |
| KIRK-2022-v03 | 2022-06-28 | `2204 Kirklees Creative Economy Baseline .docx` | — | 403 | 8 | SUPERSEDED (baseline, rev=158) |
| KIRK-2022-v04 | 2022-06-28 | `Kirklees Creative Industries draft report.docx` | DRAFT | 615 | 3 | SUPERSEDED (draft, rev=8) |
| KIRK-2022-v05 | 2022-06-28 | `2206 Kirklees Creative Economy final 1.1.docx` | FINAL 1.1 | 386 | 8 | SUPERSEDED (v1.1) |
| **KIRK-2022-FINAL** | 2022-06-28 | `2206 Kirklees Creative Economy final report.docx` + `.pdf` | FINAL | 430 | 8 | **CANONICAL** (rev=286, 44-page PDF) |
| KIRK-2022-v07 | 2022-07-15 | `2207 Kirklees Creative Economy revised.docx` | — | 401 | 9 | LATER MODIFICATION (rev=125) — status unclear |

**Note:** The Jul 2022 "revised" version (rev=125, 401 paras, 9 tables) is later than the Jun 28 "final" (rev=286, 430 paras, 8 tables). It has fewer paragraphs but more tables. This may be a post-publication correction or a different version. Flagged as UNRESOLVED.

**Note:** The 2015 BOP Consulting report (`150622 Kirklees 2015 Creative Economy Report BOP Consulting_corrected.docx`, 687 paras, 15 tables) is a predecessor report from a different contractor, included for reference. It is NOT a Fifth Sector deliverable.

## 3. Version chain — 2024 update

| Version ID | Date | Document | Label | Paras | Tables | Authority |
|---|---|---|---|---|---|---|
| KIRK-2024-v01 | 2024-07-18 | `240627 Kirklees Creative Economy 2024.docx` | — | 528 | 18 | SUPERSEDED (rev=318) — R2 manifest source |
| **KIRK-2024-FINAL** | 2024-09-23 | `240718 Kirklees Creative Economy 2024 final.docx` | FINAL | 544 | 19 | **CANONICAL** (rev=26, 48-page PDF) |
| KIRK-2024-v03 | 2024-09-02 | `Kirklees key numbers shared within their impact report.docx` | — | 15 | 0 | COMPANION (key numbers summary) |

**Note:** The R2 manifest source (SRC-R2-11) is `240627 Kirklees Creative Economy 2024.docx` (Jul 18, rev=318, 528 paras, 18 tables), which is NOT the latest version. The canonical is `240718 Kirklees Creative Economy 2024 final.docx` (Sep 23, rev=26, 544 paras, 19 tables) — later, with more content. The R2 source should be updated or supplemented.

## 4. Version chain — 2026 report

| Version ID | Date | Document | Label | Paras | Tables | Authority |
|---|---|---|---|---|---|---|
| KIRK-2026-v01 | 2025-10-17 | `kirklees-creative-economic-impact-report.pdf` | — | — | — | SUPERSEDED (early PDF, 49 pages) |
| KIRK-2026-v02 | 2026-05-25 | `kirklees-creative-economic-impact-report-2026-publication-draft.md` | DRAFT | — | — | SUPERSEDED (publication draft) |
| KIRK-2026-v03 | 2026-05-27 | `260527 kirklees-creative-economic-impact-report-2026.docx` | — | 605 | 21 | SUPERSEDED (rev=2) |
| KIRK-2026-v04 | 2026-05-27 | `260527 kirklees-creative-economy-impact-report-2026.docx` | — | 603 | 14 | SUPERSEDED (different title spelling, fewer tables) |
| **KIRK-2026-FINAL** | 2026-05-28 | `260528 Kirklees-creative-industries-economic-impact-report-2026-FINAL.docx` | FINAL | 608 | 21 | **CANONICAL** (rev=2, 73-page PDF) |
| KIRK-2026-v06 | 2026-05-30 | `kirklees-creative-economic-impact-report-2026.docx` | — | 586 | 0 | LATER but 0 tables — different format? |

**Note:** The May 30 version (rev=1, 586 paras, 0 tables) is later than the FINAL but has 0 tables. This may be a text-only export or a different format. Flagged as UNRESOLVED.

**Note:** The 2026 report was produced using a different workflow — Markdown drafts, audit files, changelogs, consistency audits, deepthink/blindspot reviews. This is a significant methodological shift from the 2022 and 2024 reports.

## 5. Changelog — method evolution across three reports

### 2022 report: Baseline mapping
- **Method:** Creative economy mapping using SIC codes, Companies House data, BRES data, Beauhurst data, music business data, voluntary arts data. Dashboard created (v2, v3). Interim findings presented. Baseline document produced (rev=158). Final report (rev=286, 430 paras, 8 tables, 44 pages).
- **Spillover framing:** Not evident from metadata. The 2015 BOP report (predecessor) is included for reference.
- **Option framing:** Not evident from metadata.
- **Confidence:** LOW (metadata only; content not compared).

### 2024 update: Expanded data and analysis
- **Method:** Updated mapping with additional data sources. Table count more than doubled (8→19). Paragraph count increased (430→544). New data: Beauhurst export (Jul 2024), workforce dashboard, Holmfirth art week venues. High revision count (rev=318) on the Jul 18 version suggests intensive iteration.
- **Spillover framing:** Not evident from metadata.
- **Option framing:** Not evident from metadata.
- **Breakthrough flag:** The doubling of tables (8→19) suggests significant analytical expansion. What new data/analysis was added?
- **Confidence:** LOW (metadata only; content not compared).

### 2026 report: New workflow and deeper analysis
- **Method:** Major shift in production workflow — Markdown drafts, audit files, changelogs, consistency audits, deepthink/blindspot reviews, GVA method prompts, SIC/IT/RTIC crosswalk analysis, FTE intensity analysis, freelance GVA recommendations. Report produced through a structured review process (report_audit_deepthink_blindspot, report_errors_reconciliation, report_update_consistency_audit). Final report (rev=2, 608 paras, 21 tables, 73 pages).
- **Spillover framing:** The 2026 report title includes "economic-impact" — suggesting a shift from mapping to impact assessment. The freelance GVA recommendations and FTE intensity analysis suggest workforce spillover analysis.
- **Option framing:** The "report_remaining_decisions.md" and "report_update_freelance_gva_recommendations.md" suggest option/policy analysis was performed.
- **Breakthrough flag:** The 2026 workflow shift is a major methodological evolution. The introduction of structured audits (deepthink, blindspot, consistency) and the Markdown-first approach represent a different production method.
- **Breakthrough flag:** The freelance GVA recommendations suggest workforce spillover analysis was introduced or deepened.
- **Breakthrough flag:** The SIC/IT/RTIC crosswalk analysis suggests new sectoral classification work.
- **Confidence:** MEDIUM (workflow files and titles indicate significant methodological change; content not compared).

## 6. Method evolution timeline

| Dimension | 2022 | 2024 | 2026 | Trend |
|---|---|---|---|---|
| Paragraphs | 430 | 544 | 608 | +41% growth |
| Tables | 8 | 19 | 21 | +163% growth |
| Pages | 44 | 48 | 73 | +66% growth |
| Production workflow | DOCX-only | DOCX-only | Markdown + audit + DOCX | Shift to structured review |
| Title framing | "Creative Economy" | "Creative Economy" | "creative-industries-economic-impact" | Shift to impact framing |
| Data sources | SIC, Companies House, BRES, Beauhurst, music, voluntary arts | + workforce dashboard, Holmfirth | + SIC/IT/RTIC crosswalk, FTE intensity, freelance GVA | Expanding |
| Audit/review process | Not evident | Not evident | deepthink, blindspot, consistency audit | New structured review |
| Spillover framing | Not evident | Not evident | Freelance GVA, workforce | Emerging in 2026 |
| Option framing | Not evident | Not evident | Remaining decisions, recommendations | Emerging in 2026 |

## 7. Key observations

1. **Three-report evolution is unique in the pilot.** No other project has three separate reporting cycles. This makes P10-KIRK the richest case for method evolution analysis.
2. **The 2026 workflow shift is significant.** The introduction of Markdown drafts, structured audits (deepthink, blindspot, consistency), and a changelog represents a different production method. This may reflect learning from the spillover toolkit process itself.
3. **The title change in 2026** from "Creative Economy" to "creative-industries-economic-impact" suggests a shift from mapping to impact assessment — potentially the point where spillover analysis became explicit.
4. **The R2 manifest source is the wrong version.** SRC-R2-11 is the Jul 18, 2024 version (528 paras, 18 tables), not the Sep 23 "final" (544 paras, 19 tables). The R2 source should be updated.
5. **The 2022 "revised" version (Jul 2022)** is UNRESOLVED — is it a correction or a different version?
6. **The 2026 May 30 version** (586 paras, 0 tables) is UNRESOLVED — is it a text-only export or a different format?
7. **The 2015 BOP Consulting report** is a predecessor from a different contractor, included for reference. It is NOT a Fifth Sector deliverable.

## 8. UNRESOLVED items for Iain

1. Is the Jul 2022 "revised" version a correction to the 2022 final, or a different version?
2. Is the May 30, 2026 version (0 tables) a text-only export or a different format?
3. ~~Were the 2022 and 2024 reports accepted by the client?~~ RESOLVED: Both accepted (confirmed by Iain, 2026-09-09).
4. ~~Was the 2026 report accepted by the client?~~ RESOLVED: 2026 report is still in progress / not yet accepted (confirmed by Iain, 2026-09-09).
5. What drove the workflow shift in 2026 (Markdown, audits, changelog)?
6. Did the spillover toolkit process influence the 2026 workflow?

## 9. Methodology evaluation questions (Iain, 2026-09-09)

The 2026 workflow shift is itself an analytical subject. Two evaluation questions:

### 9.1 Did the changed methodology produce better process or outcomes?

Compare the 2026 report production process against the 2022 and 2024 cycles:
- **Process quality:** Did the Markdown-first drafting, structured audits (deepthink, blindspot, consistency), changelog and error reconciliation produce a cleaner methodology, fewer errors, or better-documented decisions than the DOCX-only workflows of 2022/2024?
- **Outcome quality:** Is the 2026 report more analytically rigorous, better evidenced, or more transparent about its methods and limitations than the 2022/2024 reports? Does it contain spillover/option analysis that the earlier reports lacked?
- **Evidence:** The 2026 archive contains audit files (report_audit_deepthink_blindspot, report_errors_reconciliation, report_update_consistency_audit, report_version_control_reconciliation) that do not exist for 2022/2024. These files are themselves evidence of process change. Content comparison of the three reports is needed to assess outcome quality.
- **Confidence:** MEDIUM that the process changed (evidenced by audit files). NOT_ESTABLISHED that outcomes improved (requires content comparison).

### 9.2 Were the coding support tools used effectively?

- **Tools observed:** The 2026 archive contains evidence of: SIC/IT/RTIC crosswalk analysis, FTE intensity analysis, freelance GVA recommendations, a shadow classifier (shadow_classifier_kirklees.xlsx), a master audit (kirklees_master_audit.xlsx), and a current-vs-fresh classifier comparison (kirklees_current_vs_fresh_classifier_comparison_20260623.xlsx).
- **Effectiveness question:** Were these tools used effectively to produce defensible classifications and measurements? Or did they introduce new error modes (e.g., classifier drift, crosswalk mismatches, FTE estimation assumptions)?
- **Streamlining question:** Could a standardised process be written to streamline and ruggedise the move from initial draft to final report — incorporating the audit steps, changelog, consistency checks and error reconciliation as a repeatable workflow rather than an ad-hoc 2026 experiment?
- **Toolkit relevance:** If the 2026 workflow is judged better, it could inform the spillover toolkit's own report production methodology. The audit files (deepthink, blindspot, consistency) map directly to the toolkit's lens protocols. This is a potential feedback loop from project practice to toolkit design.
- **Confidence:** LOW. Requires content review of the audit files and the three reports to assess.
