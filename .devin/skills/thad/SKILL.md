---
name: thad
description: THAD, the Half-Ass Detector, is an adversarial purpose, product, and proof gate for plans, implementations, and deliverables. Use when the user invokes THAD, Half-Ass Detector, proper critique, or asks whether something is safe, complete, or release-ready. Use proactively before substantial plans, implementations, product behaviour, data-ownership decisions, releases, client setup, or user-facing work is treated as finished.
---

# THAD, the Half-Ass Detector

THAD is an adversarial review gate. It tests whether the stated purpose, promised product, and claimed proof align with the evidence actually available.

## Required review

1. State the purpose and the decision it is meant to support.
2. Identify the promised product, scope, dependencies, exclusions, and acceptance conditions.
3. Trace each material claim to evidence that is available, reproducible, lawful to use, and appropriate to the claim.
4. Test delivery readiness, ownership, data rights, operational fit, quality assurance, and failure recovery.
5. Run both lenses:
   - `/blindspot`: identify what a sceptical client, evaluator, rival, user, or maintainer would notice first and what the deliverable hides.
   - `/deepthink`: examine the underlying incentive, failure mode, second-order consequence, and whether the work solves the actual problem rather than a proxy.
6. Check wording for unsupported confidence, scope creep, invented precision, unpriced work, and contradictions with source documents.

## Verdicts

Never return a bare thumbs-up or thumbs-down. Return one explicit classified verdict:

- `PASS`: the work is ready for the stated purpose, with residual risks recorded.
- `BLOCK — PURPOSE FAILURE`: it solves the wrong problem or does not support the required decision.
- `BLOCK — PRODUCT FAILURE`: the promised product is incomplete, unusable, or outside the agreed scope.
- `BLOCK — PROOF FAILURE`: material claims are unsupported, irreproducible, or overstated.
- `BLOCK — DATA/RIGHTS FAILURE`: data is missing, unlawfully used, undisclosable, or inadequately governed.
- `BLOCK — DELIVERY FAILURE`: ownership, time, cost, dependencies, QA, or recovery arrangements cannot support delivery.
- `BLOCK — SAFETY/COMPLIANCE FAILURE`: material legal, accessibility, privacy, security, or policy requirements are unmet.

For every BLOCK include:

- diagnosis and the exact evidence behind it;
- salvageable work;
- alternatives and trade-offs;
- a recommendation;
- a concrete recovery path;
- a re-review gate with pass criteria; and
- residual risk if the recommendation is adopted.

For a PASS, still include evidence, assumptions, residual risk, and the re-review trigger. Do not claim a test, source check, or completed action unless it was actually performed.

## House-style compatibility

When reviewing bid, proposal, report, or partner-facing prose, also apply `/style`: UK English, no em dashes, no contrastive negation, sentence case headings, no jargon or Americanisms, evidence-backed claims, and no hyperbole. Flag claims needing a second independent source. Do not edit the deliverable unless the user explicitly approves edits.
