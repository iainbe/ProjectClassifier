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
| Total claims requiring fix | 14 | |
