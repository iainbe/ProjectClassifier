---
name: load-the-team
description: Coordinate the Foresight team for substantial work. Use when the user says "load the team" or needs THAD, SHELDON, PIGPEN and relevant specialist lanes to produce one evidenced outcome.
---

# Load the Foresight team

## Jonbot alignment

When `$jonbot` is active, read Jonbot's current behavioural sources before coordinating. Jonbot is the shared collaboration contract, not a reviewer lane; preserve every specialist's independent remit, evidence and receipt.

If `$sark` is available, begin with its turn-level lane selection. `load-the-team`
then performs the selected substantial-work coordination and receipt collection;
it does not replace Sark's decision about which lanes are warranted.

## Purpose

Turn a substantial Foresight request into a coordinated, evidenced piece of work. This is an operating gate, not a roster announcement: name the necessary lanes, give each a bounded job, and collect their receipts before claiming completion.

Use it when the user says `load the team`, asks for a team assessment, or starts significant implementation, cleanup, Places data work, a universe rebuild, or a user-facing product change. Do not use it for a small self-contained question or a trivial one-file edit.

## Start with the work contract

State the requested outcome, user/job, scope, non-goals, real authority, and the local/preflight/live/release boundary. Then select only the lanes warranted by the work:

- **THAD** is required for substantial work: purpose, usefulness, product fitness, proof boundary, and an explicit constructive PASS/BLOCK.
- **SHELDON** is required where code, data paths, runtime behaviour, performance, tests, or maintainability are in scope.
- **PIGPEN** is required before substantial implementation, refactoring, cleanup, new scripts, or generated artifacts. It sets the ownership/location plan and records hygiene risks; it must not use cleanup as a pretext for broad unverified rewrites.
- **WISHFUL** is required when feasibility, missing data, cost, access, assumptions, or a proposed future capability is material. It advises routes; it never vetoes work.
- **GREY** is required when an analysis or decision depends on partial, noisy, indirect, conflicting or incomplete evidence. It produces the best current reading and next discriminating evidence; it never vetoes work.
- **SKiN** is required for a changed user-facing interface or interaction journey.
- **FoK** is required for Places questions involving evidence discovery, source combination, derived insight, or data gaps.
- **MrU** is required when a Places universe, source binding, Admin definition, lifecycle script, or rebuild currentness may be affected.

Do not claim a lane ran merely because its skill exists. Record the question, evidence inspected, verdict or finding, and the resulting action for every selected lane.

## Coordination rules

1. Run PIGPEN's ownership and placement pass before adding product logic, one-off scripts, or partial output. Place reusable behaviour with its owner; isolate genuinely temporary output outside tracked product paths and remove it when its purpose ends.
2. Preserve distinct responsibilities: THAD keeps the **why**, SHELDON the **what is true**, WISHFUL the **how forward**, and PIGPEN the **structural hygiene**. Do not let a passing test substitute for THAD, or a clean folder substitute for runtime proof.
3. For cross-lane findings, route the finding to the owning lane: structural disorder to PIGPEN, runtime/proof concerns to SHELDON, missing/uncertain data to FoK and WISHFUL, universe staleness to MrU, and product-fit concerns to THAD.
4. A rejection alone is not an outcome. Convert a justified concern into a smallest safe correction, owner, proof gate, and residual risk. Do not silently expand external authority, publish, deploy, or delete material data.

## Completion receipt

Return one concise team receipt containing:

- the work contract and selected lanes;
- each lane's evidence and verdict;
- changes made, tests/visual/runtime checks actually run, and what each proves;
- unresolved risks, source/access limits, and explicit local/preflight/live/release status;
- THAD's final constructive verdict.

For substantial implementation, do not call the work complete without THAD, SHELDON, and PIGPEN receipts. A missing receipt is a **BLOCK - DELIVERY/PROOF FAILURE**, unless the user explicitly narrowed or waived that lane.
