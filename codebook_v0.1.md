# Spillover & Strategic Option Value Classification Codebook v0.1

**Version:** 0.1 (pilot draft)
**Created:** 2026-09-08
**Status:** For pilot calibration

---

## 1. Purpose

This codebook defines how to classify evidence from Fifth Sector's Creative Economy projects for spillovers and strategic option value. It is used with the linked record templates (project, source, method, claim, evidence, measurement, validation, tender, publication).

Every classification decision must be traceable to a source document with a precise locator. "No evidence found" is never a synonym for "no effect" — it means the evidence trail does not address the question.

---

## 2. Effect Family

The primary classification of what type of value was created beyond immediate project outputs.

| Code | Label | Definition | Example | Counterexample |
|---|---|---|---|---|
| DIRECT | Direct outcome | Benefit to an intended recipient that was contracted or explicitly planned as a project output | A mapping report delivered to the commissioning LEP | A neighbouring firm adopting the mapping method without being a client |
| PRODUCT | Product/process/tool spillover | A tool, technique, analytical framework, or process developed for one application diffuses to firms or organisations that were not the intended beneficiary | Social network analysis method developed for MITIH adopted by a separate creative cluster evaluation | A firm buying the same method from a competitor |
| KNOWLEDGE | Knowledge/capability spillover | Learning or capability transfers to participants or organisations beyond the contracted scope through deliberate or emergent diffusion mechanisms | Peer-to-peer learning in a cohort programme changes practice at non-participating partner organisations | A participant applying what they learned to their own work (that's a direct outcome if the programme aimed to teach them) |
| NETWORK | Network/relationship spillover | New, durable connections form between organisations or individuals not previously connected, persisting beyond the funded intervention | Two firms from different sectors that met through a Fifth Sector-facilitated workshop later co-bid for a contract | Two firms that already had a working relationship being introduced again |
| OPTION | Strategic option | The intervention preserved or created a capability, relationship, or infrastructure that a decision-maker could exercise later under conditions not yet visible at investment time | A three-phase programme structure where Phase 1 creates capability that makes Phase 2 cheaper conditional on Phase 1 completion | A one-off report with no follow-on decision point |
| OTHER | Other/unclassified | Effect observed that does not fit the above categories | A policy change influenced by evidence from the project | — |
| NULL | Null/no effect detected | A specified test was applied and no effect was found | A network analysis shows no new bridging ties formed | Evidence was simply not available (use NOT_ASSESSED instead) |

### Decision rule: Direct outcome vs spillover
1. Was the recipient an intended beneficiary of the project? → If yes, likely DIRECT.
2. Was the benefit contracted or compensated? → If yes, likely DIRECT.
3. Did the benefit travel beyond the contracted scope to an unintended recipient? → If yes, classify as PRODUCT, KNOWLEDGE, or NETWORK.
4. Is the benefit a preserved future choice rather than a realised effect? → If yes, classify as OPTION.
5. Record uncertain boundary cases with a note; do not force a label.

---

## 3. Mechanism

The pathway through which the spillover or option value travelled or could travel.

| Code | Label | Definition |
|---|---|---|
| ADOPTION | Adoption | A firm or organisation takes up a tool, method, or process developed in the project |
| ADAPTATION | Adaptation | A firm or organisation modifies a tool, method, or process from the project for their own use |
| DEMONSTRATION | Demonstration | The project's work shows what is possible, influencing others to try similar approaches |
| PEER_LEARNING | Peer learning | Structured or informal knowledge transfer between participants or organisations |
| WORKFORCE_MOBILITY | Workforce mobility | Individuals who participated in or learned from the project move to new organisations, carrying capabilities |
| BROKERAGE | Brokerage | The project introduced parties who then collaborate independently |
| COLLABORATION | Collaboration | Parties who met through the project form a durable working relationship |
| SHARED_INFRA | Shared infrastructure | Physical, digital, or organisational infrastructure created by the project is used by others |
| REUSABLE_EVIDENCE | Reusable evidence | Data, analysis, or findings from the project are reused by others for different purposes |
| LEARNING_UNCERTAINTY | Learning under uncertainty | The project reduced uncertainty about a future decision, creating option value |
| OTHER_MECH | Other mechanism | Specify in notes |

Multiple mechanisms may apply to one claim. Record all that are relevant.

---

## 4. Option Subtype

For claims classified as OPTION, record the type of strategic flexibility.

| Code | Label | Definition |
|---|---|---|
| DEFER | Defer | The investment preserves the right to wait for more information before committing |
| STAGE_LEARN | Stage/learn | The investment is sequenced so each phase generates information for the next decision gate |
| EXPAND | Expand | The investment creates a base from which to scale up if conditions are favourable |
| SWITCH_REPURPOSE | Switch/repurpose | The investment creates capability that can be redirected to a different use |
| CONTRACT_ABANDON | Contract/abandon | The investment preserves the right to reduce or exit if conditions are unfavourable |
| MAINTAIN_ACCESS | Maintain access | The investment preserves access to a network, capability, or resource for future use |

Also record:
- **Option holder:** Who has the decision right (funder, client, Fifth Sector, participants, other)
- **Exercise access:** Can the holder actually exercise the option? Are there barriers?

---

## 5. Method Status

| Code | Label | Definition |
|---|---|---|
| NOT_IDENTIFIED | Not identified | No spillover/option method is evident in the project documentation |
| PROPOSED | Proposed | A spillover/option method appears in the proposal or plan but no evidence of application |
| APPLIED | Applied | Evidence shows the method was used in delivery |
| CORROBORATED | Application corroborated | Independent evidence (not just the deliverer's own report) confirms the method was applied |
| UNKNOWN | Unknown | Method records are missing or inaccessible |

---

## 6. Outcome Status

| Code | Label | Definition |
|---|---|---|
| NOT_ASSESSED | Not assessed | No evidence was found that addresses whether the outcome occurred |
| HYPOTHESIS | Plausible hypothesis | The outcome is predicted by theory or mechanism but no direct evidence confirms it |
| REPORTED | Reported | The outcome is reported by the deliverer or a participant but not independently corroborated |
| CORROBORATED | Independently corroborated | The outcome is confirmed by an independent source or method |
| CONTRADICTED | Contradicted | Evidence contradicts the claimed outcome |
| NOT_DETECTED | Not detected | A specified test was applied and no effect was found |

---

## 7. Attribution Strength

| Code | Label | Definition |
|---|---|---|
| NOT_ASSESSED | Not assessed | Attribution has not been examined |
| DESCRIPTIVE | Descriptive association | The outcome co-occurs with the intervention but causality is not examined |
| CONTRIBUTION | Contribution supported | The claim examines alternative explanations and finds the intervention contributed to the outcome |
| CAUSAL_ESTIMATE | Causal estimate | The claim uses a credible identification strategy (comparison group, natural experiment, or similar) to estimate the causal effect |

---

## 8. Value Status

| Code | Label | Definition |
|---|---|---|
| UNQUANTIFIED | Unquantified | No quantitative measure of value is attempted |
| NON_MONETARY | Non-monetary quantified | A quantitative measure exists (e.g., number of adopters, network density) but not in monetary terms |
| SCENARIO_MONETARY | Scenario-based monetary estimate | A monetary estimate exists based on stated scenarios and assumptions, not independently reviewed |
| REVIEWED_MONETARY | Reviewed monetary estimate | A monetary estimate has been reviewed for methodology, sensitivity, and double counting |

Never infer value status from causal status or vice versa. A claim can have strong attribution but no monetary valuation, or a monetary estimate with weak attribution.

---

## 9. Boundary

| Axis | Codes |
|---|---|
| Recipient status | INTENDED / UNINTENDED / UNCLEAR |
| Organisational scope | WITHIN_ORG / ACROSS_ORG / UNCLEAR |
| Sectoral scope | WITHIN_SECTOR / ACROSS_SECTOR / UNCLEAR |
| Geographic scope | WITHIN_AREA / ACROSS_AREA / UNCLEAR |
| Supply chain scope | WITHIN_CHAIN / ACROSS_CHAIN / UNCLEAR |
| Compensation | COMPENSATED / UNCOMPENSATED / UNCLEAR |

---

## 10. Intent and Timing

| Axis | Codes |
|---|---|
| Intent | DESIGNED_IN / EMERGENT / RETROSPECTIVE |
| Timing | REALISED / IN_PROGRESS / FORECAST / EXPIRED |

- **DESIGNED_IN:** The spillover or option was an explicit objective of the project design.
- **EMERGENT:** The spillover occurred without being planned but was observed during or after delivery.
- **RETROSPECTIVE:** The spillover or option is hypothesised after the fact from the evidence trail.
- **EXPIRED:** An option existed but was not exercised before it lapsed or became irrelevant.

---

## 11. Direction and Distribution

| Axis | Codes |
|---|---|
| Direction | BENEFICIAL / ADVERSE / MIXED / UNCLEAR |
| Beneficiaries | Record who benefits |
| Cost bearers | Record who bears costs |
| Access barriers | Record any barriers to access (confidentiality, IP, cost, geography, eligibility) |

---

## 12. Evidence Sufficiency

Record:
- **Source quality:** PRIMARY (original document from the project) / SECONDARY (derived from project material) / TERTIARY (third-party reference)
- **Independence:** INDEPENDENT (separate source from the claimant) / SAME_SOURCE (same author/organisation) / UNKNOWN
- **Coverage:** COMPLETE (all expected evidence available) / PARTIAL / MINIMAL / MISSING
- **Time lag:** CONTEMPORARY (from the project period) / SHORT_LAG (within 1 year) / LONG_LAG (1+ years) / UNKNOWN
- **Contrary evidence:** NONE / PRESENT (describe)
- **Reviewer confidence:** HIGH / MEDIUM / LOW — with reasons

---

## 13. Commercial Reuse

| Code | Label | Definition |
|---|---|---|
| INTERNAL_ONLY | Internal only | Evidence may be used internally but not shared externally |
| ANONYMISED_DRAFT | Anonymised draft | May be shared in draft with client names and identifying details removed |
| PERMISSION_PENDING | Permission pending | Client or rights holder has been approached but clearance not yet received |
| APPROVED_NAMED | Approved named use | Client has approved use of their name and specific evidence |
| PROHIBITED | Prohibited | Use is explicitly prohibited by contract, confidentiality, or rights |

---

## 14. Fifth Sector Role

| Code | Label | Definition |
|---|---|---|
| DESIGNER | Designer | Fifth Sector designed the intervention or method |
| DELIVERER | Deliverer | Fifth Sector delivered the intervention |
| EVALUATOR | Evaluator | Fifth Sector evaluated the intervention (designed/delivered by others) |
| ADVISOR | Advisor | Fifth Sector provided advisory input but did not design or deliver |
| INTERPRETER | Interpreter | Fifth Sector retrospectively interpreted evidence from a project delivered by others |
| PARTNER | Partner | Fifth Sector was one of several delivery partners |

Record this separately from attribution. Fifth Sector's role does not determine the strength of attribution to the intervention itself.

---

## 15. Four Analytical Lenses

These are analytical approaches applied during assessment, not classification codes. Record which lenses were applied and what they found.

| Lens | Function | Application |
|---|---|---|
| /skin | Practitioner validation | Examines practitioner testimony, participant accounts, workshop notes for evidence of spillover presence |
| /thad | Theory-anchored analysis | Applies established theory to predict what patterns spillovers would create, then checks whether those patterns hold |
| /deepthink | Counterfactual analysis | Reconstructs what would have happened without the intervention; tests alternative explanations |
| /blindspot | Invisible outcomes | Searches for outcomes beyond the original project objectives and measurement frame |

Record: lens applied → question asked → finding → limitation.

---

## 16. Decision Trees

### 16.1 Is this a spillover or a direct outcome?

```
Was the recipient an intended beneficiary?
├── YES → Was the benefit beyond the contracted scope?
│   ├── YES → Classify as spillover (PRODUCT/KNOWLEDGE/NETWORK)
│   └── NO → Classify as DIRECT
└── NO → Did the benefit travel from the project to this recipient?
    ├── YES → Classify as spillover (PRODUCT/KNOWLEDGE/NETWORK)
    └── NO → Not a project effect; record as context only
```

### 16.2 Is this strategic option value?

```
Does the intervention preserve or create a capability, relationship, or infrastructure?
├── NO → Not an option; classify as DIRECT or spillover
└── YES → Is there a decision-maker who could exercise a future choice based on this?
    ├── NO → Not an option; record as a capability without a decision right
    └── YES → Is there a credible scenario where exercising the option would be valuable?
        ├── NO → The option has negligible value; record as OPTION with low value
        └── YES → Classify as OPTION with subtype and record the decision structure
```

### 16.3 Can we attribute this to Fifth Sector?

```
What was Fifth Sector's role?
├── DESIGNER or DELIVERER → Did Fifth Sector's specific contribution differ from what another firm would have done?
│   ├── Evidence supports distinctive contribution → Record CONTRIBUTION or CAUSAL_ESTIMATE
│   └── No evidence of distinctive contribution → Record DESCRIPTIVE
├── EVALUATOR or INTERPRETER → Fifth Sector measured or interpreted, not caused
│   └── Record Fifth Sector role as evaluator/interpreter; do not claim delivery attribution
└── ADVISOR or PARTNER → Record specific contribution; do not claim full attribution
```

---

## 17. Ambiguous Cases and Counterexamples

### Case 1: Participant applies learning to their own work
A workshop participant changes their practice based on what they learned. If the workshop's objective was to teach participants, this is a DIRECT outcome. If the participant was not the target audience but learned incidentally, this is a KNOWLEDGE spillover.

### Case 2: Firm adopts a method after seeing it in a report
A firm reads a published report and adopts the analytical method. If the report was published as a public good, this is a PRODUCT spillover via DEMONSTRATION. If the firm paid for access, this is a compensated direct transaction.

### Case 3: Two organisations that knew each other collaborate after a project
If the project created the collaboration, this is a NETWORK spillover. If they were already collaborating, this is not a spillover — record as context. Check for pre-existing ties.

### Case 4: Phase 2 is cheaper because Phase 1 assembled a team
Lower Phase 2 costs could reflect: (a) option value (preserved capability), (b) ordinary learning economies, (c) reusable assets, or (d) relationship pricing. Only classify as OPTION if there is an actual decision right and a credible alternative of not proceeding.

### Case 5: A mapping project enables future policy decisions
The mapping creates an evidence base that could inform future decisions. This is OPTION (MAINTAIN_ACCESS or STAGE_LEARN) if there is a decision-maker with a future choice. If no decision point is identifiable, it is a DIRECT outcome (the report itself).

---

## 18. Versioning

This codebook is versioned. Changes require:
1. Recording the change in the change log
2. Recoding affected records
3. Not changing the meaning of existing codes without explicit version increment

Change log:
| Version | Date | Change | Reason |
|---|---|---|---|
| 0.1 | 2026-09-08 | Initial pilot draft | Created for Stage 1 pilot calibration |
