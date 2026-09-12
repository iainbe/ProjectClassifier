# Tier 2 QA Review — Five-Lens Spot-Check

**Date:** 26/09/11
**Reviewer:** Devin (first coder)
**Lenses applied:** /wishful, /skin, /thad, /deepthink, /blindspot
**Scope:** All 54 G2 post-2020 claims, with source spot-checks

## QA process critique

The previous Tier 2 pass applied Lens A and Lens B as **batch labels**, not as per-claim scrutiny. Rule checks verified that claim_type was assigned and FKs resolved, but did not check whether claim_type was **correct**. /wishful was not applied at all. This review corrects that gap.

## Findings by lens

### /wishful — Overstatement, correlation-as-causation, assumed outcomes

**CRITICAL: 4 claims mislabel sector characteristics as EFFECT**

| Claim | Current | Issue | Source evidence | Fix |
|---|---|---|---|---|
| C-G2-029 | EFFECT/PRODUCT | ImmerseUK sector list presented as product spillover effect | Lines 461-475: List of ImmerseUK member sectors, not evidence of spillover from mapping | → CONTEXT |
| C-G2-050 | EFFECT/PRODUCT | Createch adoption across sub-sectors presented as product spillover effect | Sector observation, not an effect of the mapping project | → CONTEXT |
| C-G2-068 | EFFECT/PRODUCT | Farnborough hangars-to-sound-stages presented as product spillover effect | Lines 44-47: Existing conversion, not caused by Surrey+ mapping | → CONTEXT |
| C-G2-071 | EFFECT/PRODUCT | Adlib Audio cross-sector services presented as product spillover effect | Line 88: Adlib founded 1984, pre-exists mapping; sector characteristic | → CONTEXT |

**CRITICAL: 1 claim mislabels context as METHOD_OUTPUT**

| Claim | Current | Issue | Source evidence | Fix |
|---|---|---|---|---|
| C-G2-053 | METHOD_OUTPUT/DIRECT | Wakefield CCI growth presented as method output | Line 96: "correlates with" — context, not method output or Fifth Sector effect | → CONTEXT |

**CRITICAL: 5 claims misattribute programme effects to Fifth Sector**

Fifth Sector was the **evaluator** of these programmes, not the deliverer. The programme effects are real but Fifth Sector's contribution was the evaluation, not the programme delivery.

| Claim | Current | Programme | Fifth Sector role | Fix |
|---|---|---|---|---|
| C-G2-040 | EFFECT/KNOWLEDGE | LCR Film Fund | Evaluator | Retain EFFECT; set fifth_sector_role=EVALUATOR, fifth_sector_contribution=EVALUATION |
| C-G2-054 | EFFECT/NETWORK | CDF / Creative Wakefield | Evaluator | Retain EFFECT; set fifth_sector_role=EVALUATOR, fifth_sector_contribution=EVALUATION |
| C-G2-055 | EFFECT/PRODUCT | CDF / XPLOR | Evaluator | Retain EFFECT; set fifth_sector_role=EVALUATOR, fifth_sector_contribution=EVALUATION |
| C-G2-056 | EFFECT/NETWORK | CDF / CoSTAR | Evaluator | Retain EFFECT; set fifth_sector_role=EVALUATOR, fifth_sector_contribution=EVALUATION |
| C-G2-057 | EFFECT/KNOWLEDGE | CDF / Creative Leadership | Evaluator | Retain EFFECT; set fifth_sector_role=EVALUATOR, fifth_sector_contribution=EVALUATION |

**1 claim mislabels programme effect as METHOD_OUTPUT**

| Claim | Current | Issue | Fix |
|---|---|---|---|
| C-G2-012 | METHOD_OUTPUT/KNOWLEDGE | Absorptive capacity increase is a CWL programme effect, not Fifth Sector's method output | → EFFECT; set fifth_sector_role=EVALUATOR |

### /skin — Claim specificity, testability, named actors

**Issues found:**

1. **C-G2-029**: "25+ non-creative sectors" — the source lists ImmerseUK member sectors, not 25+ sectors where immersive tech was applied through this project. The claim overstates the evidence.
2. **C-G2-050**: "Createch strengths being adopted" — vague. Which createch? Adopted by whom? Source doesn't specify.
3. **C-G2-068**: "translating aerospace technology into screen production innovation" — wishful framing. Source says hangars "have been turned to" sound stages. No evidence of technology translation.
4. **C-G2-071**: "music-sector technical services sold into non-music sectors" — Adlib serves music and corporate events. "Corporate events" is not the same as cross-sector spillover.
5. **C-G2-053**: "employment grew 32% and GVA grew 79%" — source says "correlates with" not "caused by". Claim should preserve this distinction.

### /thad — Decision, output, proof

**EFFECT claims require: what decision does this inform, what output was produced, what proof exists?**

1. **C-G2-056** (CoSTAR attribution): Decision = CoSTAR award. Output = testimony. Proof = interview quote (lines 220-228). But attribution chain is: CDF → Production Park relationship → CoSTAR bid. This is contribution analysis, not causal proof. The claim should note this is testimony-based, not counterfactual.
2. **C-G2-040** (LFO partnership): Decision = LFO governance change. Output = LFO report observation. Proof = LFO report. But this is the LFO's own programme effect, not Fifth Sector's effect.
3. **C-G2-054** (network growth): Decision = network development. Output = membership data. Proof = Creative Wakefield records. But this is CDF's effect, not Fifth Sector's.

### /deepthink — Cross-document consistency, causal reconstruction

1. **C-G2-053 vs C-G2-058**: Wakefield jobs inconsistency (120 vs 160 FTE) is correctly flagged, but C-G2-053 presents employment growth without noting the inconsistency in the underlying jobs data.
2. **C-G2-070 vs C-G2-072**: LCR Music GVA claim uses "Integrated Case" (£405.9m) but doesn't note that Base Case is £324.7m — a £81.2m gap. The claim should preserve both scenarios.
3. **C-G2-075**: Solent GVA reconciliation (£5.25bn vs £6.9bn) is correctly noted, but the claim doesn't note that the £5.25bn itself relies on ONS regional output scaling which has its own assumptions.
4. **C-G2-043**: SYMCA £2bn GVA claim uses "up to" language but the measurement record (MEAS-G2-021) doesn't flag that this is an upper bound with a generic ONS productivity index.

### /blindspot — Missing actors, unintended recipients, expired options

1. **Expired options**: C-G2-048 (Pennine Originals) and C-G2-063 (Solent Createch) are DESIGN claims for unsuccessful bids. Their option_state should be EXPIRED or LAPSED, not empty.
2. **Missing actors**: C-G2-056 (CoSTAR) doesn't mention the University of York as co-partner in the CoSTAR bid. Source line 240 mentions "Production Park's successful partnership with the Council and the University of York."
3. **Unintended recipients**: C-G2-053 (Wakefield growth) doesn't consider whether growth displaced activity from neighbouring areas (leakage/displacement).
4. **Non-adopters**: No claims record non-adopters or negative cases. The LCR Music SNA (C-G2-072) found only 0.6% of possible connections exist — this is a null finding that should be preserved as evidence of network weakness, not just a method output.
5. **C-G2-041** (LCR Film Fund option): Development Fund pipeline forecasts (7.8:1 leverage) are forecasts from 2021. Have any been realised? If unknown, option_state should be UNKNOWN not empty.

## Summary of fixes required

| Category | Count | Action |
|---|---|---|
| Sector characteristic mislabelled as EFFECT | 4 | Reclassify to CONTEXT |
| Context mislabelled as METHOD_OUTPUT | 1 | Reclassify to CONTEXT |
| Programme effect mislabelled as METHOD_OUTPUT | 1 | Reclassify to EFFECT + EVALUATOR |
| Programme effect with missing evaluator role | 5 | Add fifth_sector_role=EVALUATOR |
| Expired options for unsuccessful bids | 2 | Set option_state=EXPIRED |
| Missing actors / unintended recipients | 3 | Add notes |
| Pass 1 total | 14 | |

## Pass 2: Systematic spot-check (26/09/11)

After pass 1, a systematic spot-check of all G2 claims against source documents found a **systematic misclassification pattern**: 26 baseline measurement claims mislabelled as METHOD_OUTPUT.

### Systematic issue: sector baselines mislabelled as METHOD_OUTPUT

The codebook states: "A mapping report estimating regional GVA is CONTEXT with a descriptive estimate, not value created by the consultant."

The following claims describe sector characteristics (GVA, employment, company counts, turnover, LQs) that were measured by the mapping/strategy work but are not themselves method outputs. They are contextual baselines against which spillover effects might later be assessed.

| Claim | Project | Proposition (short) | Source evidence |
|---|---|---|---|
| C-G2-001 | P11-ELFC | £1.4bn GVA, 36200 jobs | Line 54, 409: sector baseline |
| C-G2-002 | P11-ELFC | 57% GVA growth, 43% employment growth | Line 55, 426-429: sector baseline; 22% London employment unverified |
| C-G2-007 | P11-ELFC | Hackney LQ 9.46 | Line 449: sector characteristic |
| C-G2-009 | P12-KIRK15 | CI employment 3360, CE 5020 | Sheet 1: sector baseline |
| C-G2-010 | P12-KIRK15 | GVA £100.979m | Sheet 6: sector baseline |
| C-G2-015 | P14-DCAT | 500 immersive companies | Sector baseline |
| C-G2-018 | P14-DCAT | HVMC cluster access | Sector characteristic |
| C-G2-019 | P15-LIVMUS | £100.5m turnover, 2360 jobs | Line 46, 155: sector baseline |
| C-G2-020 | P15-LIVMUS | £98m Beatles heritage | Line 49, 151: sector baseline |
| C-G2-021 | P15-LIVMUS | Adlib sector strength | Line 47, 224: sector characteristic |
| C-G2-025 | P17-LCRCSU | 32% employment growth | Sector baseline |
| C-G2-028 | P19-LCRIMM | 169 organisations | Sector baseline |
| C-G2-030 | P19-LCRIMM | Meetup ecosystem | Sector characteristic |
| C-G2-032 | P20-SYMCA21 | 4000+ companies | Sector baseline |
| C-G2-043 | P24-SYMCACGP | £2bn GVA (upper bound) | Sector baseline |
| C-G2-044 | P24-SYMCACGP | 2.46 multiplier | Contextual finding |
| C-G2-045 | P24-SYMCACGP | 1013 courses | Sector baseline |
| C-G2-047 | P25-LANCGP | 4500 businesses | Sector baseline |
| C-G2-049 | P26-WSBH | 10225 companies | Sector baseline |
| C-G2-059 | P28-CALDER | 655 ONS firms | Sector baseline |
| C-G2-062 | P29-SOLENTCGP | 4510 businesses | Sector baseline |
| C-G2-064 | P30-HEREFORD | 590 businesses | Sector baseline |
| C-G2-066 | P31-PRODPARK | Data fragment | Sector baseline |
| C-G2-067 | P32-SURREY | £7.2bn GVA | Sector baseline |
| C-G2-070 | P33-LCRMUS | £405.9m GVA | Line 790-810: modelled baseline |
| C-G2-075 | P34-SOLENTHANTS | £5.25bn GVA | Sector baseline |

All 26 reclassified METHOD_OUTPUT → CONTEXT.

### Additional spot-check findings

1. **C-G2-002**: 22% London employment growth figure NOT FOUND in source. Only 29% London GVA growth confirmed (line 427). Flagged as unverified.
2. **P13-CWL correction**: Iain led evaluation as BOP Associate Director, not merely advisor/interpreter. Project and all 4 claims updated: fifth_sector_role=EVALUATOR, contracting_role=ASSOCIATE.
3. **7 empty option_state fields**: All OPTION claims with empty option_state set to PROPOSED.

### Remaining genuine METHOD_OUTPUT claims (6)

These are genuinely method outputs — programme delivery data or analytical method application:
- C-G2-024: CICP evaluation approach design
- C-G2-037: LCR Film Fund £6.76 leverage (programme output data)
- C-G2-038: LCR Film Fund 455 FTE (programme output data)
- C-G2-039: Development Fund deployment (programme output data)
- C-G2-052: CDF programme £22.03m total value (programme output data)
- C-G2-072: SNA of 272 businesses (analytical method application)

### R3 pilot claims — same pattern flagged

The same baseline-as-METHOD_OUTPUT pattern was found in 11 R3 pilot claims. These are flagged for correction in the next pass but not changed in this pass to maintain scope discipline.

## Updated total

| Pass | Category | Count |
|---|---|---|
| 1 | Sector characteristic as EFFECT | 4 |
| 1 | Context as METHOD_OUTPUT | 1 |
| 1 | Programme effect as METHOD_OUTPUT | 1 |
| 1 | Missing evaluator role | 5 |
| 1 | Expired options | 2 |
| 1 | Unknown option state | 1 |
| 1 | Empty option_state | 7 |
| 2 | Sector baseline as METHOD_OUTPUT | 26 |
| 2 | Unverified figure flagged | 1 |
| 2 | P13-CWL role correction | 4 claims + 1 project |
| **Total** | | **52 claim fixes + 1 project fix** |

## Residual uncertainty — ALL RESOLVED

All residual uncertainties have been resolved through user decisions (26/09/11):

1. **R3 pilot claims**: 11 R3 claims corrected (8 in pass 2, 3 in final pass). COMPLETE.
2. **C-G2-002**: 22% London employment VERIFIED in SRC-G2-003 Table 2 (131,300 to 159,700 = 21.6% rounds to 22%). No change needed.
3. **C-G2-056**: rival_explanations added (University of York, Wakefield Council, Production Park, national CoSTAR programme). Retained as EFFECT/DESCRIPTIVE per user decision C.
4. **C-G2-041**: option_state set to EXPIRED. Final evaluation (SRC-G2-030, 25/06) does NOT confirm 7.8:1 leverage forecast. Development Fund treated as COVID emergency support. 7.8:1 in final eval is a hypothetical scenario ratio, not a realised outcome.
5. **C-G2-070**: No change. "Integrated Case" label already signals scenario. Per user decision B.
6. **C-G2-043**: Methodological caveat added to MEAS-G2-021 (ONS productivity index, LinkedIn workforce, BRES pre-pandemic). Per user decision A.
7. **Project-level roles**: No change. Claim-level EVALUATOR provides distinction. Per user decision C.
8. **value_basis**: Filled for 14 claims with £ figures (CONTEXT→DESCRIPTIVE_ESTIMATE, METHOD_OUTPUT→OBSERVED_AMOUNT, DESIGN→SCENARIO_ESTIMATE). Per user decision A.
9. **Tender sources**: No project records needed. LCR Screen Sector Research is unsuccessful bid; BC Art and Tech is pending tender. Per user confirmation.
10. **Derby conflation**: Three distinct Derby projects identified and separated (P35-DERBYMAP, P23-DERBY, P36-DERBYCSR). C-R3-038 corrected. AGENTS.md updated with conflation rules.
11. **C-R3-022**: option_state corrected from PROPOSED to EXPIRED (P07-CC is NOT_AWARDED). Caught in final QA verification.

## Final QA verification — ALL CHECKS PASS

| # | Check | Result |
|---|-------|--------|
| 1 | Unique IDs (all registers) | PASS |
| 2 | Foreign keys (claims→projects, sources→projects, evidence→claims/sources, measurements→claims) | PASS |
| 3 | Empty project_id on claims | PASS |
| 4 | OPTION claims without option_state | PASS |
| 5 | Empty effect_family | PASS |
| 6 | Empty fifth_sector_role | PASS |
| 7 | DESIGN claims for unsuccessful bids without EXPIRED | PASS |
| 8 | EFFECT claims without attribution_strength | PASS |
| 9 | Claims with £ figures but empty value_basis | PASS |
| 10 | Sector baselines mislabelled as METHOD_OUTPUT | PASS |
| 11 | Conflation check (claim geography vs project geography) | PASS |
| 12 | Strong causal verbs in non-EFFECT claims | PASS (2 false positives confirmed correct) |
| 13 | Sources with empty project_id | PASS (4 tender pipeline items, confirmed correct) |

## Final register counts

| Register | Rows |
|----------|------|
| 01_projects.csv | 36 |
| 02_sources.csv | 53 |
| 03_methods.csv | 48 |
| 04_claims.csv | 115 |
| 05_evidence_links.csv | 126 |
| 06_measurements.csv | 78 |
| 07_validation_actions.csv | 48 |
| 08_tenders.csv | 5 |
| 09_publication_assets.csv | — |
| 10_review_history.csv | 232 |

## Final claim type distribution

| Claim type | Count |
|------------|-------|
| CONTEXT | 56 |
| DESIGN | 29 |
| METHOD_OUTPUT | 20 |
| EFFECT | 8 |
| BID_SUPPORT_DELIVERED | 2 |
| **Total** | **115** |

## QA status: COMPLETE (Pass 1-2)

All Tier 2 QA checks pass. All residual uncertainties resolved through user decisions. AGENTS.md updated with rules to prevent recurrence in future batches.

---

## Pass 3: Full-Read Consistency Audit (26/09/12)

**Scope:** Complete source corpus — all G2, R2, R3, LPF, and project-specific sources read in full. Register reconciliation, evidence link gaps, source metadata, and QA re-verification.

### Inventory verification

All source files in `extracted_text/` verified against `02_sources.csv` register. 111 source records in register; 107 extracted text files on disk. Mapping confirmed for all canonical sources.

**Problematic sources flagged:**

| Source | Issue | Action |
|--------|-------|--------|
| SRC-G2-056 (Plymouth NMP Digital Strategy) | BINARY PDF stream; 22MB; no human-readable text | extraction_quality=BINARY; cannot be analysed |
| SRC-G2-065 (WYCA proposal) | EMPTY file; 0 bytes | extraction_quality=EMPTY; no claims possible |
| SRC-G2-074 (Lancaster AHRC CIC) | FILENAME/CONTENT MISMATCH; extracted text is Liverpool MusicFutures email | extraction_quality=MISMATCH; do not code under P75; validation action raised |

**Supporting sources not separately extracted (25):** These are supporting documents (drafts, presentations, procurement specs, web versions, workshop notes) whose content is covered by their canonical source. Marked extraction_quality=SUPPORTING, source_review_state=NOT_ASSESSED.

### Evidence link gap closure

109 evidence links added (E-G2-430 to E-G2-538) connecting claims to sources that were missing from `05_evidence_links.csv`:

| Project | Source | Claims linked |
|---------|--------|---------------|
| P46 (TVCA) | SRC-G2-036 | 23 |
| P69 (Wakefield OY) | SRC-G2-067 | 30 |
| P83 (BC Western Balkans) | SRC-G2-085 | 19 |
| P57 (Rushmoor) | SRC-G2-051 | 9 |
| P52 (Somerset) | SRC-G2-046 | 12 |
| P62 (TRP) | SRC-G2-059 | 11 |
| P22 (LCR Film Fund) | SRC-G2-030 (LPF-FINAL) | 5 (additional links) |

All 65 projects now have at least one evidence link from claims to their canonical source.

### Source register metadata update

59 G2-BATCH-C source records (SRC-G2-030 through SRC-G2-088) updated with:
- `derived_location` populated for all sources with extracted text files
- `extraction_quality` set to COMPLETE/SUPPORTING/BINARY/EMPTY/MISMATCH as appropriate
- `source_review_state` set to REVIEWED for complete reads; NOT_ASSESSED for supporting/problematic
- `reviewer` = Devin; `review_date` = 26/09/12
- `extraction_scope` = full for complete reads
- `extraction_warnings` populated for substantial reports and problematic sources

### Validation actions added

16 new validation actions (VAL-G2-025 through VAL-G2-040) covering:
- SRC-R2-09B internal GVA inconsistency (£4.0bn vs £4.5bn)
- SRC-G2-074 filename/content mismatch
- SRC-G2-056 binary extraction failure
- SRC-G2-065 empty file
- SRC-G2-075 Lancaster Horizon bid status unknown
- SRC-G2-077/079/080/081 work-in-progress status verification
- SRC-G2-085 BC WB phase status confirmation
- Numeric verification for Wakefield OY visitor spend and engagement counts
- Somerset Cebr multiplier verification
- Rushmoor games sector undercount verification
- TRP interview methodology check

### QA fixes applied

| Fix | Count | Details |
|-----|-------|---------|
| DESIGN claims for NOT_AWARDED without EXPIRED | 3 | C-G2-449, C-G2-450, C-G2-451 (P07-CC): option_state PROPOSED → EXPIRED |
| Sector baseline mislabelled as METHOD_OUTPUT | 2 | C-G2-465 (Birmingham LQ), C-G2-480 (Beauhurst company count): METHOD_OUTPUT → CONTEXT, value_basis=DESCRIPTIVE_ESTIMATE |

### Updated register counts

| Register | Rows (previous) | Rows (current) |
|----------|----------------|----------------|
| 01_projects.csv | 36 | 65 |
| 02_sources.csv | 53 | 111 |
| 03_methods.csv | 48 | 52 |
| 04_claims.csv | 115 | 561 |
| 05_evidence_links.csv | 126 | 578 |
| 06_measurements.csv | 78 | 78 |
| 07_validation_actions.csv | 48 | 63 |
| 08_tenders.csv | 5 | 5 |
| 10_review_history.csv | 232 | 256 |

### Updated claim type distribution

| Claim type | Count (previous) | Count (current) |
|------------|-------------------|------------------|
| CONTEXT | 56 | 213 |
| DESIGN | 29 | 150 |
| METHOD_OUTPUT | 20 | 102 |
| EFFECT | 8 | 82 |
| BID_SUPPORT_DELIVERED | 2 | 14 |
| **Total** | **115** | **561** |

### Updated effect family distribution

| Effect family | Count |
|---------------|-------|
| CONTEXTUAL | 205 |
| DIRECT | 98 |
| OPTION | 86 |
| KNOWLEDGE | 83 |
| NETWORK | 43 |
| PRODUCT | 30 |
| NOT_APPLICABLE | 16 |

### QA verification — ALL CHECKS PASS

| # | Check | Result |
|---|-------|--------|
| 1 | Unique IDs (all registers) | PASS |
| 2 | Foreign keys (claims→projects, sources→projects, evidence→claims/sources, measurements→claims) | PASS |
| 3 | Empty project_id on claims | PASS |
| 4 | OPTION claims without option_state | PASS |
| 5 | Empty effect_family | PASS |
| 6 | Empty fifth_sector_role | PASS |
| 7 | DESIGN claims for unsuccessful bids without EXPIRED | PASS (fixed 3 claims) |
| 8 | EFFECT claims without attribution_strength | PASS |
| 9 | Claims with £ figures but empty value_basis | PASS |
| 10 | Sector baselines mislabelled as METHOD_OUTPUT | PASS (fixed 2 claims; 1 false positive confirmed) |
| 11 | Claims without evidence links | PASS (109 links added) |
| 12 | Evidence→Sources FK | PASS |
| 13 | Measurements→Claims FK | PASS |
| 14 | Sources with empty project_id | PASS (4 tender pipeline items confirmed correct) |

### Remaining open validation actions

| Status | Count |
|--------|-------|
| RESOLVED | 15 |
| OPEN | 48 |
| **Total** | **63** |

48 validation actions remain OPEN, requiring:
- Iain confirmation on bid/commission statuses (Lancaster Horizon, Beatles, CELL, Southampton, WB6, BC WB phase)
- Numeric spot-checks (Wakefield OY visitor spend, Somerset Cebr multiplier, Rushmoor games undercount)
- Source file location (Lancaster AHRC CIC correct source, WYCA proposal original)
- Methodology checks (TRP interview sample, Wakefield OY engagement counting)

## QA status: COMPLETE (Pass 3)

All Tier 2 QA checks pass after full-read reconciliation. 109 evidence links added. 59 source records updated. 16 validation actions added. 5 claim fixes applied. 3 problematic sources flagged. AGENTS.md rules remain authoritative.

---

# Pass 4: Index card QA + register schema repair (26/09/12)

## Five-agent review of index cards P04-P09

Applied SHELDON / THAD / DEEPTHINK / BLINDSPOT / SKiN / WISHFUL to the six populated index cards.

### Errors found and fixed

| # | Finding | Lens | Status |
|---|---------|------|--------|
| 1 | P08 "77,252 total" misread — it is £77,252 GVA per capita, not workforce | DEEPTHINK | FIXED |
| 2 | P08 circular reuse claim (listed itself as reuse example; method originated P04-GBSLEP 2017) | DEEPTHINK | FIXED |
| 3 | P07 "five case model reused in CELL (P79)" — absent from P79 text | DEEPTHINK | FIXED (set NOT_ESTABLISHED) |
| 4 | P06 £75.6m presented without scope qualifier — national programme total, not bid share | DEEPTHINK | FIXED |
| 5 | P04 "50,000 workers" glossed three source figures (49,600 / 49,900 / "nearly 50,000") | DEEPTHINK | FIXED (approximately) |
| 6 | P04 "significant innovation" presented as fact — it is BOP's self-description | DEEPTHINK | FIXED (attributed) |
| 7 | P04 Crafts "11x" needed measure+geography clarification (Birmingham centre; LQ 6.2 GBSLEP area) | DEEPTHINK | FIXED |
| 8 | REVIEWED status claimed without Iain consistency confirmation | THAD | RESOLVED via walkthrough |

### Register schema-drift corruption found and repaired

15 pilot rows (P01-P15) in 01_projects.csv had role/evidence values written under wrong columns — a legacy schema migration left [contracting_role, prime_contractor, relationship_evidence, review_status] values shifted into [relationship_evidence, review_status, codebook_version, review_batch]. Confirmed values (e.g., P08 PRIME/The Fifth Sector from VAL-R3-015) were invisible under the current header. Repaired: all 15 rows realigned; stray notes text in parent_project_id moved to notes; review_batch set R3-PILOT. Backup: 01_projects.csv.bak.

74 claim fields realigned in 04_claims.csv to match confirmed contracting roles (incl. P05 SUBCONTRACTOR→BOP_ASSOCIATE, P06/P07→ADVISORY, P08→PRIME). Backup: 04_claims.csv.bak.

### Walkthrough resolutions (Iain confirmations 26/09/12)

| Project | Resolution |
|---------|-----------|
| P04-GBSLEP | Fifth Sector co-lead with Jonathan Todd (then BOP) — "contribution unclear" resolved |
| P05-WMCA | BOP associate arrangement — fees paid to Fifth Sector; register semantics confirmed: ALL work paid to Fifth Sector; contracting_role distinguishes lead/subcontractor/associate arrangement |
| P06-COSTAR | Framework design (LEAD/DRIVE/ACCELERATE) confirmed as Fifth Sector contribution — innovation claim verified |
| P07-CC | Framework design (five work packages + five-case model) confirmed |
| P08-LIVDCI | precedent_strength STRONG / evidence_strength MEDIUM split approved |
| P09-CDEC | Paid commission confirmed; challenges paper never finalised — deliverables were demonstrators + TDC12 presentation |

### Card status

P04-P09 all REVIEWED with Iain consistency confirmation recorded. P01-P03, P10 remain PROVISIONAL pending same walkthrough.

### Remaining known limitations (not defects)

- All A4 permission fields remain INTERNAL_ONLY/NOT_ESTABLISHED — no card may be cited in tenders until reference_status cleared (template §C.5 gate)
- project_index.csv browse layer still not created (template §D promised)
- source_claims cite generic C-G2-* ranges, not specific claim IDs
- P06 Create Growth date discrepancy in source (2023-26 vs 2022-2025) preserved
- P09 Nov 29 proposal remains unextractable (scanned PDF)
- P36-DERBYCSR contracting_role=BIDDER is a legitimate value (not corruption)
- contracting_role EMPTY on P37+ is honest — Phase 2 projects not yet confirmed

### Method lesson added

Schema-drift check is now a required QA step: before any CSV field update, verify row structure against header (field count AND positional semantics). The earlier "check headers" rule was insufficient — rows can have the right count with values in wrong columns.

---

# Pass 5: Index layer + permissions (26/09/12)

## project_index.csv created
65 rows — one per register project. Card-bearing projects (P01-P10) carry REVIEWED status, precedent/evidence ratings, spillover types, contract values, headline findings. Non-card projects show NO_CARD with register identity. Closes the SKiN browse-layer gap.

## Permission gate: TENDER_CITATION cleared for all 10 pilot projects
All pilot projects approved APPROVED_NAMED for tender submissions (TENDER_ONLY — website gate remains separate). 09_publication_assets.csv populated with 10 rows including per-project permitted wording and caveats.

## Material corrections from permission walkthrough
- P06-COSTAR: bid was SHORTLISTED on submission strength; consortium lost at interview (Fifth Sector not involved). lifecycle→SHORTLISTED_NOT_AWARDED; precedent WEAK→MODERATE; card reframed as submission-stage success.
- P07-CC: same — SIPF application shortlisted. Same corrections applied.
- P03-MITIH: register revealed 25/06 report rejection for recommendations + Oct 24 reconciliation acceptance — now recorded in card lifecycle, decision-use, and caveats.
- Distinction codified: failed-bid (no delivered work) vs rejected-recommendation (completed work, rejected element). P06/P07/P03 all delivered work with documented outcomes.

## Contract values recorded
P02 £25k; P03 £25k; P10 £10k×3 cycles (£30k total); P01+P04 NOT_DISCLOSED; others NOT_ESTABLISHED.

---

# Pass 6: Live-work templates review (26/09/12)

## SHELDON verdict: PARTIALLY PROVEN
- EXISTS+proven: bid_submission_record_template.md, project_management_record_template.md, register_update_workflow.md, bid_records/, project_records/, AGENTS.md live-work rules, tools/regenerate_index.py (executed+verified), repo sync (commit e56660d)
- CONFIGURED: trigger rules are convention (fire when agent reads AGENTS.md); Drive-canonical rule unenforceable
- PARTIALLY EXISTS: record directories empty awaiting first live event
- UNKNOWN: trigger firing at real events — untestable until first use

## SKiN verdict: FRICTION → cleared after fixes
- Worst failure (fixed): bid template invented TND-YYYY-NNN ID scheme contradicting 08_tenders.csv T-NN convention; register-row rule undefined (P06/P07 precedent now codified: commissioned bid work → project row, speculative → tenders only)
- Hidden opportunity: precedent_cards_cited field will record which track-record items appear in winning bids — conversion analytics for the toolkit itself
- Residual friction: PM checklist requires opening the file — mitigated by standing monthly prompts, not eliminated

## Fixes applied during review
- tools/regenerate_index.py persisted (was session-only logic); includes schema-drift check
- Bid ID scheme aligned to T-NN convention
- Register-row rule defined in template, workflow, AGENTS.md
- PM milestone section converted to self-contained checklist (event-triggered + standing monthly prompts)

---

# Pass 7: Date normalisation + tenders schema repair (26/09/12)

## Date format: all registers/cards/docs normalised to YY/MM/DD
- ~2,300 cell/value conversions across 10 CSVs + all markdown
- Rules: YYYY-MM-DD→YY/MM/DD everywhere; YYYY-MM→YY/MM in date-typed fields; bare YYYY→YY in date fields only (folder paths like "2017 Projects" preserved); ISO timestamps→YY/MM/DDT; unambiguous English dates converted ("Dec 2017"→17/12); year-ranges ("2017-18") and prose preserved
- EXCEPTION: extracted_text/ source files untouched — verbatim evidence
- Convention codified in AGENTS.md; tools/normalise_dates.py persisted

## Schema drift found #3: 08_tenders.csv
T02/T03/T04 had an extra empty field at position 34 (positioning_rationale) shifting last 4 values +1 → review_batch values landed in overflow. Repaired: realigned all 3 rows. Pre-existing quirk noted: T04 as_at_date=AS_AT (literal value, outside repair scope).

---

# Pass 8: Drive sweep agent (26/09/12)

- tools/drive_sweep.py scans watch roots (Active projects/proposals, Archive, toolkit) vs registers; classifies gaps; collapses to folder-level; notifies via macOS + SWEEP_LATEST.md
- Tuning fixes during build: ';'-split multi-path folders; non-project folder list (Foresight, ONS data, PM, Templates); tender-check-before-project-check ordering; folder-level dedup
- Register data fix: 7 Active-projects folder paths filled (P75, P78, P79, P80, P81, P82, P83)
- Baseline: 24,511 files tracked. Real findings: Creative Scotland Salaries unregistered (needs Iain decision: project row vs bid record); ~10 unregistered Active proposals folders
- launchd: weekday 09:00 sweeps; logs to sweep_reports/sweep.log
