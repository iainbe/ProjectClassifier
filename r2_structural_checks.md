# R2 Structural and Rule Checks

**Date:** 2026-09-09
**Codebook version:** v1.1 (candidate)

## 1. CSV structure checks

- [x] `02_sources.csv` parses with 16 source rows + header
- [x] `10_review_history.csv` parses with 62 entries (1 lock + 25 Iain INITIAL_CODE + 25 Devin INITIAL_CODE + 11 ADJUDICATION)
- [x] All source IDs unique (SRC-R2-01 through SRC-R2-15, plus SRC-R2-09B)
- [x] All review IDs unique (REV-R2-001 through REV-R2-062)
- [x] All project IDs in sources match pilot project IDs (P01-P10)
- [x] All review_batch values = R2

## 2. Source fidelity checks

- [x] SRC-R2-06 corrected from client quotation (190730 final.docx) to Jan 9 2020 final report PDF — confirmed by Iain
- [x] SRC-R2-09B added (LIVDCI final report) — accepted by client, confirmed by Iain
- [x] SRC-R2-11 corrected from Jul 18 version to Sep 23 "final" — confirmed by Iain
- [x] Old extractions renamed as SUPERSEDED (SRC-R2-06_v1_full_OLD_docx_SUPERSEDED.txt, SRC-R2-11_v1_full_OLD_jul18_SUPERSEDED.txt)
- [x] All 16 sources have extraction warnings recorded
- [x] All 16 sources have authority_status and authority_rationale recorded

## 3. Rule consistency checks

- [x] No context mislabelled as created impact: D01 GVA figures coded as METHOD_APPLICATION (not intervention effect); D04 network ties coded as PRE_EXISTING; T04 GVA coded as VISIBILITY_OPTION_VALUE (not intervention effect)
- [x] No proposals mislabelled as delivered programmes: D02 workshop coded PROPOSED; D07 programme coded as NOT_SUCCESSFUL (bid-support delivered separately); T01 inception coded PROPOSED with APPLICATION_NOT_SUCCESSFUL
- [x] No costs labelled as benefits: No monetary costs in the R2 units
- [x] No monetary values labelled non-monetary: T04 £250.9M coded as VISIBILITY_OPTION_VALUE (monetary); D01 GVA figures coded as METHOD_APPLICATION (monetary)
- [x] No missing evidence labelled NULL: D08 coded as OUTSIDE_PACKET (not NULL); all NOT_ESTABLISHED fields explicitly marked
- [x] No unverified rights: No permission/rights claims in R2 units
- [x] No outcomes dated before exposure: D02 workshop PROPOSED (no outcome date before exposure); D07 programme NOT_SUCCESSFUL (no outcome claimed)
- [x] No unsupported causal escalation: D04 tie_change = PRE_EXISTING (not causal); D05 attribution = CO_AUTHORED_ANALYSIS (not causal); T04 = VISIBILITY_OPTION_VALUE (not causal estimate)
- [x] No unknown procurement gates yielding BID: O01 missing brief = PASS (Iain adjudicated sufficient); O02 contract = PASS (Iain adjudicated standard)
- [x] No incorrect precedent links: No precedent links asserted in R2 units

## 4. Coverage checks

- [x] 12 atomic claim units coded (D01-D08, T01-T04)
- [x] 2 opportunity packets coded (O01, O02)
- [x] Both coders (Iain and Devin) recorded INITIAL_CODE entries for all 14 units
- [x] All 11 disagreements adjudicated with rationale
- [x] All adjudications recorded in 10_review_history.csv

## 5. Agreement analysis

| Metric | Count | Rate |
|---|---|---|
| Total fields compared | 21 | — |
| Initial agreements | 10 | 47.6% |
| Disagreements | 11 | 52.4% |
| Adjudicated to Iain's label | 11 | 100% of disagreements |
| Post-adjudication agreement | 21 | 100% (all fields resolved) |

**Threshold:** 80% initial per-field agreement.
**Result:** 47.6% initial agreement — BELOW THRESHOLD.

**However:** All 11 disagreements were adjudicated by Iain with rationale. No unresolved critical classification, source, attribution, rights or procurement-rule defect remains.

## 6. Critical error check

- [x] No context-to-impact escalation: All baseline figures coded as method application or visibility option value, not intervention effects
- [x] No proposal-to-outcome conflation: D02, D07, T01 all correctly distinguish proposed from delivered
- [x] No missingness-to-null: D08 coded as OUTSIDE_PACKET, not null
- [x] No distinctiveness-to-causality: D04, D05 attribution coded as distinctiveness or co-authored analysis, not causal
- [x] No unverified-rights escalation: No rights claims in R2

## 7. R2 coverage limitations (disclosed)

- R2 exercises claim classification and tender gates more thoroughly than measurement/option design, publication rights, and phase splitting
- No claim unit tests a full measurement-design exercise with real option-valuation fields
- No claim unit tests a real permission-pending case on actual source material
- No claim unit tests the publication template
- No claim unit tests a multi-phase split
- These receive their first real test in R3

## 8. Codebook issues identified by R2

1. **claim_type vs method_status:** D01 disagreement reveals these axes need clearer separation. A contextual baseline can be produced by an applied method. Iain adjudicated as METHOD_APPLICATION; Devin coded CONTEXTUAL_BASELINE. The codebook should clarify that claim_type captures the nature of the claim (what kind of finding), while method_status captures whether the method was applied. These are orthogonal.

2. **Two-level commission/programme classification:** D07 disagreement reveals that bid-support work has two levels: the commission (delivered) and the programme (not funded). Iain adjudicated as BID_SUPPORT_DELIVERED. The codebook should add BID_SUPPORT_DELIVERED as a claim_type and clarify that method_status can be APPLIED for the commission even when the programme is NOT_SUCCESSFUL.

3. **Measurement-as-value:** T04 disagreement reveals a fundamental question about whether measurement creates value. Iain adjudicated as VISIBILITY_OPTION_VALUE. The codebook should add VISIBILITY_OPTION_VALUE as a value_basis and clarify that the act of measuring can create option value by enabling policy decisions, separate from the GVA figure itself.

4. **Outside-packet evidence:** D08 disagreement reveals that prior project knowledge (workshop happened, outcomes in final report) needs a codebook status. Iain adjudicated as OUTSIDE_PACKET. The codebook should add OUTSIDE_PACKET as an evidence_status with disclosure requirements.

5. **Contextual finding vs hypothesis:** T03 disagreement reveals that papers can both describe existing trends (contextual) and propose mechanisms (hypothesis). Iain adjudicated as REPORTED_CONTEXT. The codebook should clarify that when a paper primarily documents existing conditions, the primary classification is contextual even if it also proposes actions.

6. **Conservative vs commercial coding:** Devin coded conservatively (HOLD for missing brief, AMBIGUOUS for budget, HOLD for contract); Iain coded with commercial experience (PASS, ALL_PHASES, PASS). The 100% adjudication-to-Iain pattern suggests Devin's coding was too conservative for tender gate decisions. The codebook should clarify that commercial experience is a valid input for gate decisions, with disclosure.

## 9. M2 acceptance matrix

| Check | Result | Status |
|---|---|---|
| Source fidelity | All 16 sources extracted; 3 corrections applied; originals untouched | PASS |
| Unit coverage | 12 units + 2 opportunities; both coders; all adjudicated | PASS |
| Rule consistency | No critical rule violations detected | PASS |
| Agreement | 47.6% initial (below 80% threshold); 100% post-adjudication | BELOW THRESHOLD but RESOLVED |
| Critical errors | None unresolved | PASS |
| IDs/links/codes | All unique and valid | PASS |
| Codebook issues | 6 issues identified for v1.1 revision | FLAGGED for R1 rework if needed |

**M2 decision required:** The 47.6% initial agreement rate is below the 80% threshold. However, all disagreements were adjudicated with rationale, no critical errors remain, and the disagreements reveal codebook clarity issues rather than fundamental method defects. Iain decides whether to:
- (a) Approve safe restart of the full pilot (R3), with codebook v1.1 revisions to address the 6 identified issues
- (b) Request R1 rework to fix the codebook issues before R3
- (c) Defer the decision
