# R2 Coding Comparison — Iain vs Devin

**Date:** 2026-09-09
**Lock confirmed:** Iain 2026-09-09T08:15:00Z
**Devin coded:** 2026-09-09T08:30:00Z (without seeing Iain's labels)

## Summary

| Metric | Count |
|---|---|
| Total fields compared | 21 |
| Agreements | 10 |
| Disagreements | 11 |
| Agreement rate | 47.6% |
| Threshold | 80% |
| Result | BELOW THRESHOLD — material disagreements require adjudication |

## Field-by-field comparison

### Agreements (10/21)

| Unit | Field | Iain | Devin | Status |
|---|---|---|---|---|
| D02 | method_status | PROPOSED | PROPOSED | AGREE |
| D02 | evidence_status | HYPOTHESIS | HYPOTHESIS | AGREE |
| D03 | option_holder | COMMISSIONER | COMMISSIONER | AGREE |
| D03 | option_state | PROPOSED | PROPOSED | AGREE |
| D04 | tie_change | PRE_EXISTING | PRE_EXISTING | AGREE |
| D04 | attribution_strength | DISTINCTIVENESS_ONLY | DISTINCTIVENESS_ONLY | AGREE |
| D05 | contracting_role | SUBCONTRACTOR | SUBCONTRACTOR | AGREE |
| D06 | method_status | APPLIED | APPLIED | AGREE |
| D06 | evidence_status | REPORTED | REPORTED | AGREE |
| D06 | contracting_role | SUBCONTRACTOR | SUBCONTRACTOR | AGREE |
| T01 | method_status | PROPOSED | PROPOSED | AGREE |
| T01 | lifecycle_status | APPLICATION_NOT_SUCCESSFUL | APPLICATION_NOT_SUCCESSFUL | AGREE |
| T02 | method_status | APPLIED | APPLIED | AGREE |
| D07 | lifecycle_status | NOT_SUCCESSFUL | NOT_SUCCESSFUL | AGREE |

### Disagreements (11/21)

| Unit | Field | Iain | Devin | Issue |
|---|---|---|---|---|
| D01 | claim_type | METHOD_APPLICATION | CONTEXTUAL_BASELINE | Is a GVA figure a method application or a contextual baseline? |
| D01 | canonical_version | May 8 (SRC-R2-02) | UNRESOLVED | Which report's numbers are canonical between the two extracts? |
| D05 | attribution_strength | CO_AUTHORED_ANALYSIS | DISTINCTIVENESS_ONLY | Did Fifth Sector co-author the analysis (Iain) or merely identify patterns (Devin)? |
| D07 | claim_type | BID_SUPPORT_DELIVERED | RECOMMENDATION_DESIGN | Is the case-for-support a delivered bid-support commission (Iain) or a recommendation/design (Devin)? |
| D07 | method_status | APPLIED | PROPOSED | Was the bid-support work APPLIED (delivered) or PROPOSED (the programme it supported)? |
| D08 | evidence_status | OUTSIDE_PACKET | NOT_DETECTED | Is the workshop evidence outside the packet (Iain) or not detected in this document (Devin)? |
| T03 | evidence_status | REPORTED_CONTEXT | HYPOTHESIS | Is the convergence description a contextual finding (Iain) or a proposed mechanism/hypothesis (Devin)? |
| T04 | value_basis | VISIBILITY_OPTION_VALUE | MODELLED_ESTIMATE | Does measurement create option value through visibility (Iain) or is it a modelled estimate of baseline (Devin)? |
| O01 | missing_brief_gate | PASS | HOLD | Is the ITQ sufficient without the technical brief (Iain) or does the missing brief produce HOLD (Devin)? |
| O01 | budget_interpretation | ALL_PHASES | AMBIGUOUS | Is £38K clearly for all phases (Iain) or ambiguous between Phase 1 and all phases (Devin)? |
| O02 | contract_gate | PASS | HOLD | Are the contract terms standard/acceptable (Iain) or do unknowns produce HOLD (Devin)? |

## Disagreement analysis

### 1. D01 claim_type: METHOD_APPLICATION vs CONTEXTUAL_BASELINE

**Iain's position:** The GVA figures are a method application — the mapping methodology was applied to produce them.
**Devin's position:** The GVA figures are a contextual baseline — they measure existing sector scale, not effects created by an intervention.

**Analysis:** Both are partially right. The mapping methodology was APPLIED (method_status), and the output is a contextual baseline finding (claim_type). The codebook distinguishes claim_type from method_status — a contextual baseline can be produced by an applied method. This may be a coding frame issue rather than a substantive disagreement.

### 2. D01 canonical_version: May 8 vs UNRESOLVED

**Iain's position:** May 8 (SRC-R2-02) is canonical — later version with more cautious figures.
**Devin's position:** UNRESOLVED — both predate the v3.12 canonical, so version authority between these two is unresolved.

**Analysis:** The v3.12 is the confirmed canonical version (in canonical/P01-NES/). The R2 test uses both extracts to test version/baseline distinction. Iain's knowledge of the project context informs his selection of May 8; Devin codes conservatively as UNRESOLVED because neither extract is the confirmed canonical.

### 3. D05 attribution_strength: CO_AUTHORED_ANALYSIS vs DISTINCTIVENESS_ONLY

**Iain's position:** Fifth Sector co-authored the analysis with BOP — the findings are co-created in the analytical sense.
**Devin's position:** Fifth Sector identified patterns through analysis; attribution is distinctiveness only (analytical contribution, not pattern creation).

**Analysis:** These are closer than they appear. Both agree Fifth Sector didn't create the knowledge transfer patterns. Iain's "co-authored analysis" is about the analytical work; Devin's "distinctiveness only" is about the attribution to the patterns. The codebook may need a clearer distinction between analytical contribution and effect attribution.

### 4. D07 claim_type: BID_SUPPORT_DELIVERED vs RECOMMENDATION_DESIGN

**Iain's position:** The bid-support work was delivered (Fifth Sector wrote the case for support). The commission (bid-support) is distinct from the programme (which was not funded).
**Devin's position:** The case-for-support is a recommendation/design document — it proposes a programme.

**Analysis:** This is a commission/programme distinction issue. The bid-support commission was delivered (APPLIED); the programme it supported was proposed (PROPOSED) and not funded. The codebook may need to handle two-level classification: the commission status and the programme status separately.

### 5. D07 method_status: APPLIED vs PROPOSED

**Iain's position:** APPLIED — the bid-support work was delivered.
**Devin's position:** PROPOSED — the programme proposed in the case-for-support was not delivered.

**Analysis:** Same issue as #4. Iain codes the commission (bid-support = delivered); Devin codes the programme (not delivered). Both are correct at their respective levels.

### 6. D08 evidence_status: OUTSIDE_PACKET vs NOT_DETECTED

**Iain's position:** The workshop DID happen and outcomes ARE recorded in a final report, but that final report is outside the R2 packet.
**Devin's position:** No post-workshop effects test exists in this document. NOT_DETECTED with scope.

**Analysis:** Iain has project knowledge beyond the packet. Devin codes only what the packet establishes. The codebook needs to handle prior knowledge disclosure: Iain's knowledge that the workshop happened is valid but outside the R2 packet scope. The correct R2 classification from the packet alone is NOT_DETECTED; Iain's knowledge is recorded as a disclosed limitation.

### 7. T03 evidence_status: REPORTED_CONTEXT vs HYPOTHESIS

**Iain's position:** The challenges paper documents existing convergence trends as a contextual finding about the state of the digital economy.
**Devin's position:** The paper proposes a cross-sector convergence mechanism; no occurrence evidence supplied; mechanism is hypothetical.

**Analysis:** The paper does both: it describes existing convergence trends (contextual) AND proposes that the CDEC should foster collaboration (hypothesis). The R2 question asks for "one atomic proposed cross-sector mechanism" — which points to the proposed mechanism, not the contextual description. But Iain's reading that the convergence description is contextual is also valid.

### 8. T04 value_basis: VISIBILITY_OPTION_VALUE vs MODELLED_ESTIMATE

**Iain's position:** Making the sector's GVA visible to policy creates strategic option value — the measurement enables decisions that weren't possible before.
**Devin's position:** The GVA figure is a modelled estimate of existing baseline scale, not an intervention effect.

**Analysis:** This is a fundamental disagreement about whether measurement itself creates value. Iain sees the act of measuring as creating option value (visibility enables policy decisions). Devin sees the GVA figure as a modelled estimate of what already exists. The codebook needs to clarify whether "value created by measurement" is a valid value_basis or whether it conflates measurement with value creation.

### 9. O01 missing_brief_gate: PASS vs HOLD

**Iain's position:** The ITQ contains sufficient information to proceed without the technical brief.
**Devin's position:** The ITQ references an "attached technical brief" that is not in the packet; essential buyer document missing produces HOLD.

**Analysis:** The codebook says "an inaccessible mandatory section blocks the gate decision rather than being assumed compliant." Iain's project experience may inform his judgement that the ITQ's 4 pages are sufficient; Devin codes conservatively that a referenced but missing document produces HOLD.

### 10. O01 budget_interpretation: ALL_PHASES vs AMBIGUOUS

**Iain's position:** £38K is clearly for all phases; Phase 1 is a portion.
**Devin's position:** The ITQ says "across all phases" but also "relates only to Phase 1" — ambiguous.

**Analysis:** The ITQ text is genuinely ambiguous. "Up to £38,000 may be available to support this work across all phases" could mean the total budget envelope is £38K, or that Phase 1 has up to £38K. Iain's reading is reasonable; Devin flags the ambiguity.

### 11. O02 contract_gate: PASS vs HOLD

**Iain's position:** Contract terms are standard and acceptable.
**Devin's position:** No changes allowed to contract; Annex 1 is draft; IP/data-sharing terms need review; HOLD pending.

**Analysis:** Iain's commercial experience informs his judgement that the terms are standard. Devin codes conservatively that a draft agreement with no-negotiation terms produces HOLD pending review. The codebook says "an inaccessible mandatory section blocks the gate decision" — but the contract is accessible (it's in the packet as SRC-R2-15), just draft.
