# Corpus Gate Review — 26/09/12

**Frozen object under review:** the full spillover-toolkit corpus at commit `58ebd18` — 68 projects (all carded), 568 claims, 124 sources, 587 evidence links, 14 tenders, 35 permission requests. Decision supported: whether the corpus is ready to drive (a) tender citation, (b) website positioning, (c) individual card sign-off.

**Corpus state at review:**
- Cards: 10 REVIEWED / 12 DRAFT (walked) / 46 PROVISIONAL
- Projects: 41 REVIEWED / 27 PENDING
- Claims: 566/568 evidence-linked (2 linked during this review); 0 OPTION claims missing option_state
- `permission_status`: 303 empty + 243 UNKNOWN + 17 NOT_REQUESTED + 5 NOT_ESTABLISHED — i.e. **~96% of claims have no resolved permission state**
- `contracting_role`: blank on 26/68 projects
- Sources: 86 COMPLETE / 25 SUPPORTING / 15 blank extraction_quality

---

## 1. THAD — purpose, product, proof

**Purpose:** evidence-governed capability to cite prior work, decide bids, and position the business.

**Verdict: PASS WITH CONDITIONS** — the corpus is fit to *enter* case-level review at scale; it is not yet fit for citation at scale.

- **Product exists:** the architecture does what it claims — claim→evidence→source traceability works (99.6% of claims linked), option states are enforced, CONTEXT/METHOD_OUTPUT/EFFECT separation holds, unsuccessful bids and pending outcomes are correctly marked.
- **The gate that matters is concentrated:** the card lifecycle correctly forbids tender use of non-REVIEWED cards — but that means **only 10 of 68 cards are citable today**, and `reference_permission` is unresolved on effectively everything. The corpus is a well-built library whose lending desk is closed.
- **Salvageable / not a defect:** this is a queue position, not a product failure. The pass condition is the R3 walkthrough, not rework.
- **Residual risk:** PROVISIONAL card headlines are derived from reviewed claims with spot-verification (P15/P19/P21/P32/P34/P46/P52 verified verbatim this session), not full re-reads. One mis-trace at card level propagates to a tender document. Re-review trigger: any card moving PROVISIONAL→REVIEWED without a full-read check of its headline claim.

## 2. SKiN — the journey to a citable claim

**Audience:** Iain writing a tender, needing a defensible cited precedent. **Verdict: FRICTION.**

- **Most valuable capability discovered:** the cross-project arcs (Liverpool ×5, Wakefield ×5, Kirklees ×2, Lancaster ×3, compact line ×3, CGP bids ×2) — relationship depth no competitor can fake. But discovering an arc requires reading multiple cards; nothing surfaces "the Wakefield arc" as an object.
- **Worst interaction failure:** answering "what can I cite *right now*?" requires intersecting three fields (card_status=REVIEWED, citation_status, reference_status) across two files, and the answer is ~10 cards. The corpus doesn't yet offer a `cleared_for_use` view.
- **Hidden opportunity:** `project_index.csv` precedent_strength is polluted by verbose values ("STRONG for i…") — my batch cards wrote sentences into a coded field. A clean controlled vocabulary would make filtering instant.
- **Corrections:** (1) add a derived `CLEARED` flag/view to project_index.csv combining card+citation+reference status; (2) tighten precedent_strength to controlled values (STRONG/MODERATE/WEAK/NOT_ESTABLISHED + qualifier column); (3) add arc/family tags so multi-project geographies surface as one object.

## 3. WISHFUL — feasible routes to the goal

**Ambition preserved:** citable, permission-secured evidence base feeding tenders and website.

**Magical-thinking findings:** none structural — the toolkit correctly refuses to treat pending outcomes as delivered, contribution work as ownership, or forecasts as results. The discipline is real. The residual optimism is *permission-by-implication*: ~96% of claims carry no resolved permission state, and several cards lean on "implied" consent (P33 IPM, published-report attribution).

**Current reality:** the bottleneck is not evidence, it's sign-off and permission. Both are human-gated — correctly.

**Feasibility: FEASIBLE WITH CONDITIONS**, via ranked routes:

1. **R3 walkthrough of the ~15 highest-precedent cards first** (P08, P22, P27, P33, P46, P57, P34, P32, P24, P64/69, P85 pending outcome, P86 pending signature, P51, P52) — converts the corpus's centre of gravity to REVIEWED without walking all 68 serially. *FEASIBLE NOW — needs Iain time.*
2. **Send the drafted permission asks** (35 seeded, DRAFTED) in parallel — consent latency runs while review proceeds. *FEASIBLE WITH HUMAN-IN-THE-LOOP — Iain sends; wording is drafted.*
3. **Batch-fill the 26 blank contracting_role fields** from Iain's one-line answers — closes the largest single integrity gap in one conversation. *FEASIBLE NOW.*
4. **Website positioning** only after routes 1-2 produce a cleared set — *FEASIBLE IN STAGES*, gated on real permissions, not assumed ones.

**Recommended HOW:** routes 1+2+3 in parallel this week; website work stays downstream. **Proof point:** a `CLEARED` subset exists and every tender citation traces to it.

## 4. Deepthink — the corpus's load-bearing claim

**Claim under review (the signature):** "Official statistics undercount the creative workforce — our LinkedIn/alternative-data method reveals the true scale" (appears as ~2-7x gaps across P08, P20, P24, P26, P28, P30, P34, P46, P48, P57, P84 — the corpus's most repeated finding).

**Strongest fair form:** conventional business registers (IDBR/BRES/ONS) miss freelancers, micro-businesses below VAT threshold, and SIC-misclassified firms; platform data captures people official sources structurally exclude.

**Cross-examination findings:**
- **Category-boundary risk (material):** LinkedIn's 80,511 (P34) and BRES's 39,980 do not measure the same population. LinkedIn counts self-described creative professionals; BRES counts employees of CI-classified businesses. The "hidden workforce" framing risks presenting a *definitional difference* as a *measurement correction*. A hostile methodologist would say you measured two different things and called the gap "hidden".
- **Survivable because:** the corpus's own documents frame it as "freelance and micro-business community uncounted" (SRC-G2-029 line 15 verified verbatim) — which is the defensible version. The claims sit correctly as CONTEXT/DESCRIPTIVE_ESTIMATE. The risk is *simplification at card/citation level* — "officials miss 2x" is quotable but less defensible than "a different, larger population is visible in platform data".
- **Second load-bearing claim — multipliers:** the 2.46 FTE / £0.50-per-£1 figures (C-G2-044, C-G2-096/097, C-G2-168) are literature multipliers (Cebr/Oxford Economics) applied to local data. Registered as EFFECT/CONTEXT claims — for citation they must carry "per Cebr/Oxford Economics, applied to…" provenance, never as observed local effects. Currently correctly typed but the caveat must survive into tender prose.
- **Confidence:** the pattern is `SUPPORTED` as "official data undercounts the informal workforce"; `PLAUSIBLE` as a precise multiplier claim. **Recommended wording:** always "alternative-data estimate" + named source + the official figure alongside — never a bare corrected number.

## 5. Blindspot — hostile reads

**Frozen argument:** "Fifth Sector's evidence base demonstrates delivered capability to identify, measure and evaluate spillovers and option value."

**Expert perspectives applied:** sceptical procurement evaluator; rival consultancy; client whose programme outcomes we cite; methodologist.

**What a hostile reader notices first:**
- **FATAL-if-mishandled:** citing client-owned programme outcomes (LFO filming data, SYMCA ARG effects, Wakefield CDF results) in a way that reads as Fifth Sector's achievement. The EVALUATOR-role separation exists in registers but must survive into prose every time. One careless bid sentence = misrepresentation.
- **MATERIAL:** every referee permission is unresolved. A procurement evaluator who phones a named client and gets "who?" destroys the bid. Permission must precede naming, not follow.
- **MATERIAL:** BOP-era work (P11–P19, P13, P14) — if a bid implies Fifth Sector authored deliverables that are BOP's, a rival who knows the sector will spot it. The register already caps these at contribution; the risk is prose drift.
- **MATERIAL:** self-reported corpus — an evaluator can't verify our internal claim register; they verify via the client and the published artefact. So the *citation* must always point at something external (report, published version, PO) not at our register.
- **COMPETITIVE:** age profile — a large fraction of the deepest evidence is pre-2022. The live/active set (P68, P79, P80, P81-83, P85-87) is thin on completed outcomes. Positioning should lead with recent (P33, P34, P22 final, P79) and use older work for method lineage.
- **PRESENTATIONAL:** unsuccessful bids (P36, P76, P25/P29) are internally honest but externally useless — never let them leak into client-facing material.

**Recovery:** the register discipline already anticipates most of this — the failure mode is translation into prose. Recommend a standing rule: **every external citation sentence must name (a) client, (b) our role, (c) the artefact** — "evaluated the LCR Production Fund for LCR CA" not "generated £24.5m spend".

**Ranked findings:** (1) client-outcome-vs-our-role conflation [fatal if it ships]; (2) unresolved permissions [material]; (3) BOP attribution drift [material]; (4) recency gap [competitive]; (5) prose-simplification of the undercount claim [presentational→material].

## Overall gate result

**PASS TO PROCEED to case-level review** — corpus architecture sound, no proof failures found in spot verification. Three standing conditions before external use: (1) only REVIEWED+CLEARED cards cited; (2) permission resolves before naming; (3) role-attribution sentence rule enforced. Full-resolution bottleneck is human: your confirmations and the permission sends.
