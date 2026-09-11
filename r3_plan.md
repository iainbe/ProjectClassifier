# R3 Plan — Full Pilot Reassessment with Codebook v1.3

**Date:** 2026-09-09
**Codebook:** v1.3-candidate (approved)
**Entry gate:** M2 passed (v1.2/v1.3 approved, R2 re-coding 100% agreement)
**Exit gate:** M3 — Iain decides whether to accept the corrected pilot as G2-ready

## 1. What R3 is

R3 is the substantive pilot reassessment. It populates the nine linked CSVs with real claim records for all ten projects and five opportunities, using codebook v1.3. This is the first time the CSVs move from header-only to populated records.

R3 is NOT:
- Full portfolio screening (that's G2)
- New interviews, outreach or permission requests (that's G3+)
- Website publication (that's G5a/G5b)
- Software build (that's G6)
- A re-read of every archive file — record read extent and stopping rules

## 2. Scope

### Ten projects

| ID | Project | Canonical sources available | Extracted text available |
|---|---|---|---|
| P01-NES | NE Scotland | v3.12 + Apr 20 + May 8 reports | Yes (R2 + earlier) |
| P02-FGTG | ManMet From Good to Great | Nov 6 transcript + final report (outside R2 packet) | R2 transcript only |
| P03-MITIH | MITIH Createch | Oct 25 report + policy playbook | Yes (R2 + earlier) |
| P04-GBSLEP | GBSLEP mapping | Dec 2017 report + draft | Yes (R2 + earlier) |
| P05-WMCA | WMCA Creative Scaleup | Jan 9 2020 final report PDF | Yes (R2 corrected) |
| P06-COSTAR | CoSTAR | Case for support + immersive analysis | Yes (R2 + earlier) |
| P07-CC | Creative City | Inception note | Yes (R2) |
| P08-LIVDCI | Liverpool DCI | Proposal + Jul 2024 final report | Yes (R2 + earlier) |
| P09-CDEC | CDEC | Challenges paper + demonstrators | Yes (R2 + earlier) |
| P10-KIRK | Kirklees | 2022 + 2024 + 2026 reports | Yes (R2 + earlier) |

### Five opportunities

| ID | Opportunity | Sources |
|---|---|---|
| T01 | British Council Art and Tech | RFP + clarifications + draft agreement (R2) |
| T02 | The Queen's Hall | To locate |
| T03 | Blackburn with Darwen | To locate |
| T04 | LCR Film/Screen Impact | ITQ (R2) |
| T05 | Derby Cultural Data Strategy | To locate |

### Known gaps to resolve before coding

1. **P02-FGTG:** The final report with workshop outcomes is outside the R2 packet. Need to locate and extract it for R3.
2. **T02, T03, T05:** Sources not yet located. Need to find in `Active proposals` or `Archive proposals/2026 Proposals lost`.
3. **P10-KIRK 2026:** The 2026 report is in progress. R3 codes what exists; the 2026 methodology evaluation question is addressed separately.

## 3. Work sequence

### Step 1: Source preparation (1-2 hours)

- Locate and extract P02-FGTG final report
- Locate T02, T03, T05 opportunity sources
- Register all new sources in `02_sources.csv`
- Update the R3 source manifest
- Verify extraction quality and record warnings

### Step 2: Project reassessment — Batch A (P01, P02, P03) (3-4 hours)

Start with the three projects that have the richest source material and the most complex version/option/network issues.

For each project:
1. Complete provenance/coverage review of canonical sources
2. Resolve known high-risk checks (NES versions; FGTG workshop/report; MITIH investment sequence)
3. Populate `01_projects.csv` with project record (lifecycle, role, contracting, phase)
4. Populate `03_methods.csv` with method records (status, application evidence)
5. Populate `04_claims.csv` with atomic claim records (claim_type, effect_family, evidence_status, timing, attribution, value_basis, etc.)
6. Populate `05_evidence_links.csv` linking claims to sources
7. Populate `06_measurements.csv` for numeric claims
8. Populate `07_validation_actions.csv` for material gaps
9. Update changelog and index card with R3 findings

### Step 3: Project reassessment — Batch B (P04, P05, P06) (3-4 hours)

GBSLEP, WMCA, CoSTAR. These test the subcontractor/associate role, document-type correction, and bid-support classification.

Same per-project work as Step 2.

### Step 4: Project reassessment — Batch C (P07, P08, P09) (2-3 hours)

Creative City, LIVDCI, CDEC. These test inception notes, proposal-vs-delivery, and legacy advisory work.

Same per-project work as Step 2.

### Step 5: Project reassessment — Batch D (P10) (2-3 hours)

Kirklees 2022, 2024, 2026. This is the methodological-evolution batch with the 2026 workflow evaluation.

Same per-project work as Step 2, plus:
- Evaluate the Kirklees 2026 workflow (Markdown drafts, changelog, deepthink/blindspot reviews, consistency audits)
- Assess whether the 2026 process produced better methodology/outcomes
- Record findings separately from the substantive claims

### Step 6: Opportunity reassessment (2-3 hours)

All five opportunities (T01-T05). For each:
1. Verify buyer materials, submitted version and outcome
2. Rebuild buyer requirement maps and scored criteria
3. Check conflicting deadlines, fees, capacity, legal/IP conditions
4. Assess using information available at the decision date
5. Record `actual_outcome` and `feedback_status`
6. Populate `08_tenders.csv`
7. Iain's commercial review of all five decisions

### Step 7: Double-coding and adjudication (2-3 hours)

- Iain independently codes high-risk numerical/causal/rights claims
- Iain independently codes each project's key category/status/contribution claims
- Devin codes the same set
- Compare, adjudicate, record in `10_review_history.csv`
- Pre-register a stratified sample of remaining claims covering every used category and evidence state
- Record agreement by field and project
- Expand sample where systematic errors appear

### Step 8: Inventory and G2 package preparation (2-3 hours)

- Reconcile pilot identities with the wider register
- Prepare proposed canonical full-screening scope
- Identify phases, duplicates, borderline adjacent work, missing roots, coverage risk
- Prepare corrected `G2_report.md` with:
  - Honest completion matrix
  - Coding/adjudication results
  - Repaired codebook/template versions
  - Methods, decision use, effects and options as separate findings
  - Unanswered research questions
  - Permitted commercial wording
  - Workload estimate
  - Separate decisions for full screening, deeper research, rights outreach, website work

### Step 9: M3 presentation

Present the M3 package and stop for Iain's decision.

## 4. Effort estimate

| Step | Estimated effort | Running total |
|---|---|---|
| 1. Source preparation | 1-2 hours | 1-2 |
| 2. Batch A (P01-P03) | 3-4 hours | 4-6 |
| 3. Batch B (P04-P06) | 3-4 hours | 7-10 |
| 4. Batch C (P07-P09) | 2-3 hours | 9-13 |
| 5. Batch D (P10) | 2-3 hours | 11-16 |
| 6. Opportunities | 2-3 hours | 13-19 |
| 7. Double-coding | 2-3 hours | 15-22 |
| 8. G2 package | 2-3 hours | 17-25 |
| 9. M3 presentation | 0.5 hours | 17.5-25.5 |

**Total: approximately 17-25 hours of work.** This is a substantial phase. I will do my best to complete it as soon as possible.

## 5. Rules and constraints

- Record read extent and stopping rules, not an implication that every archive file was read
- Do not fabricate measurements for qualitative claims
- Do not fabricate publication approvals to fill tables
- Recode every affected prior assertion using explicit old-to-new dispositions
- Keep traceable pre-correction records in review history
- Summaries must be derived from reviewed records, not independent sources of truth
- No new interviews, outreach or permission requests
- No website publication
- No software build
- No full portfolio screening
- No spending
- All five opportunity decisions receive Iain's commercial review
- Test usability from bid/HOLD through response design and measurement planning
- Do not penalise a commercially sound conventional commission for not needing spillover analysis

## 6. M3 acceptance criteria

- Pilot records and narratives agree
- All material claims have traceable dispositions
- Required independent coding and commercial review are complete
- No unresolved critical defect
- Schemas/templates/history are aligned
- Export/re-import preserves IDs and long text
- Remaining uncertainty is visible and blocks affected reuse rather than the entire knowledge base
- v1.3 promoted from candidate to accepted pilot release only when Iain approves

**M3 approval makes the pilot G2-ready, not rollout-authorised. Stop and seek G2 approval for the specifically proposed full scope.**

## 7. Decision requested

Do you approve this R3 plan? If so, I'll start with Step 1 (source preparation). If you want to adjust the scope, sequencing or priorities, let me know.
