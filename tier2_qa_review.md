# Tier 2 QA Review — Five-Lens Spot-Check

**Date:** 2026-09-11
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

## Pass 2: Systematic spot-check (2026-09-11)

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

## Residual uncertainty

1. **R3 pilot claims**: 11 R3 claims have the same baseline-as-METHOD_OUTPUT pattern. Not corrected in this pass.
2. **C-G2-002**: 22% London employment growth figure unverified. Needs source clarification.
3. **C-G2-056**: CoSTAR attribution is testimony-based. University of York co-partner missing from claim.
4. **C-G2-041**: Development Fund pipeline forecasts from 2021 unconfirmed as realised.
5. **C-G2-070**: LCR Music Base Case (£324.7m) vs Integrated Case (£405.9m) gap not noted in claim.
6. **C-G2-043**: SYMCA £2bn GVA is an upper bound with generic ONS productivity index.
7. **Project-level roles**: P22-LCRFILM and P27-WAKECDF have DESIGNER;DELIVERER at project level, which could misread as programme delivery rather than evaluation delivery.
