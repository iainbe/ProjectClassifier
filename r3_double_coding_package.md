# R3 Double-Coding Package — High-Risk Claims for Iain's Independent Coding

**Date:** 2026-09-09
**Codebook:** v1.3-candidate
**Protocol:** Iain codes first and locks labels; Devin compares against his initial coding; adjudicate disagreements

## High-risk claims requiring double-coding

These are the claims that are numerical, causal, rights-related, or each project's key category/status/contribution claims.

### Numerical/causal claims (7)

| Claim ID | Project | Proposition | Key fields to code |
|---|---|---|---|
| C-R3-001 | P01-NES | £453M direct GVA / £675M total impact | claim_type, attribution_strength, value_basis |
| C-R3-003 | P01-NES | Convergence could raise impact to £1.1B | claim_type, attribution_strength, value_basis, option_state, option_holder |
| C-R3-011 | P03-MITIH | SNA identifies microbusinesses as bridging organisations | claim_type, attribution_strength, tie_change |
| C-R3-013 | P03-MITIH | Gated investment sequence proposed | claim_type, attribution_strength, option_state, option_holder |
| C-R3-017 | P04-GBSLEP | Intermediaries and knowledge transfer mapped | claim_type, attribution_strength, tie_change |
| C-R3-032 | P10-KIRK | £250.9m GVA | claim_type, attribution_strength, value_basis |
| C-R3-033 | P10-KIRK | Measurement creates visibility and option value | claim_type, attribution_strength, value_basis, option_state, option_holder |

### Key category/status/contribution claims per project (10)

| Claim ID | Project | Proposition | Key fields to code |
|---|---|---|---|
| C-R3-001 | P01-NES | £453M direct GVA (also numerical) | claim_type, method_status |
| C-R3-006 | P02-FGTG | Workshop delivered with outcomes recorded | claim_type, method_status, evidence_status |
| C-R3-009 | P03-MITIH | 3847 job postings 46% increase | claim_type, method_status |
| C-R3-014 | P04-GBSLEP | GBSLEP creative economy mapped | claim_type, attribution_strength |
| C-R3-018 | P05-WMCA | WMCA creative businesses mapped | claim_type, attribution_strength |
| C-R3-020 | P06-COSTAR | Case for Support delivered | claim_type, method_status |
| C-R3-022 | P07-CC | SIPF application proposed | claim_type, method_status, programme_status |
| C-R3-023 | P08-LIVDCI | LCR cluster mapped | claim_type, method_status |
| C-R3-027 | P09-CDEC | ICT-creative convergence documented | claim_type, evidence_status |
| C-R3-029 | P10-KIRK | Three-cycle mapping with expanding scope | claim_type, method_status |

### Tender gate decisions (3)

| Opportunity | Gate field | Devin's code |
|---|---|---|
| T01-BCAT | bid_recommendation | BID |
| T04-LCRFILM | bid_recommendation | PASS |
| T05-DERBY | bid_recommendation | HOLD |

## Instructions for Iain

For each claim above, please code the key fields listed using codebook v1.3. Record your codes in a simple format:

```
C-R3-001: claim_type=METHOD_OUTPUT, attribution_strength=DESCRIPTIVE, value_basis=DESCRIPTIVE_ESTIMATE
C-R3-003: claim_type=DESIGN, attribution_strength=NOT_ASSESSED, value_basis=SCENARIO_ESTIMATE, option_state=PROPOSED, option_holder=COMMISSIONER
...
```

Once you've coded all 20 claims and 3 tender gates, I'll compare against my coding, identify disagreements, and we'll adjudicate.

## Devin's coding summary

For reference, here are the key codes I assigned:

- **claim_type:** METHOD_OUTPUT (mapping/analysis outputs), DESIGN (proposals/recommendations), BID_SUPPORT_DELIVERED (CoSTAR), EFFECT (workshop networking)
- **attribution_strength:** DESCRIPTIVE (most mapping claims), CO_AUTHORED_ANALYSIS (GBSLEP), NOT_ASSESSED (proposals/hypotheses)
- **value_basis:** DESCRIPTIVE_ESTIMATE (GVA/workforce figures), SCENARIO_ESTIMATE (£1.1B convergence), VISIBILITY_OPTION_VALUE (Kirklees measurement-as-value), NONE (qualitative claims)
- **option_state:** PROPOSED (all option claims), PRE_EXISTING (network ties)
- **option_holder:** COMMISSIONER (all proposed options)
- **tie_change:** PRE_EXISTING (SNA/intermediary mapping), NEW (workshop networking)
- **method_status:** APPLIED (delivered work), PROPOSED (inception/SIPF)
- **evidence_status:** REPORTED (documented findings), OUTSIDE_PACKET (not used in R3 since all sources are now in packet)
- **programme_status:** NOT_AWARDED (CoSTAR bid, Creative City SIPF)
