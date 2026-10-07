---
name: sark
description: Decide which Foresight team lanes should handle the current turn; use at the start of every substantive Foresight request involving analysis, data, code, product, planning, delivery or review, and use explicitly as $sark when a team decision must be guaranteed.
---

# SARK — Foresight team orchestrator

## Jonbot alignment

When `$jonbot` is active, read Jonbot's current behavioural sources before dispatching. Jonbot supplies the collaboration and quality contract, not a reviewer lane; preserve every selected specialist's independent remit and receipt.

Sark decides who needs to be active for this turn. It is the orchestration
layer, not another reviewer: it does not replace THAD, SHELDON, PIGPEN,
WISHFUL, GREY, SKiN, FoK or MrU, and it does not borrow their conclusions.

Run Sark at the start of every substantive Foresight turn. For a quick factual
answer, a simple rewrite or a self-contained small task, Sark still makes an
explicit decision: **direct handling; no specialist lane warranted**. Do not
create ceremonial reviews or agent noise for work that cannot benefit from it.

## Freeze the turn contract

Before choosing lanes, state internally or in a compact commentary update:

- the requested outcome and user/job;
- the thing being changed, investigated, explained or decided;
- authority and boundary: read-only, local implementation, preflight, Product,
  publish, deploy or client release;
- meaningful uncertainty, risk, dependencies and non-goals.

Treat a fresh user message as a fresh routing decision. Continue already-active
lanes only when their unfinished work still serves the revised request.

## Select the smallest useful team

Sark must make a positive selection or an explicit no-lane decision. Select
lanes by the work, not by names mentioned in the chat.

- **THAD** — substantial plans, implementations, Product changes, reports,
  claims of completion or release: purpose, user/job, usefulness, fitness and
  proof boundary. It is the final constructive PASS/BLOCK authority.
- **SHELDON** — code, data paths, database/artifact lineage, runtime behaviour,
  performance, tests, or claims that something works.
- **PIGPEN** — substantial implementation, refactor, cleanup, new script,
  artifact ownership or structural-risk work. Run before adding product logic
  or one-off machinery.
- **WISHFUL** — feasibility, access, cost, licensing, dependencies, missing
  inputs or future capability are material. It is advisory and never blocks.
- **GREY** — a decision or analysis depends on partial, noisy, indirect,
  conflicting or thin evidence. It actively investigates weak signals and
  returns a best current reading, alternatives and next discriminating evidence;
  it is advisory and never blocks.
- **FoK** — Places evidence discovery, compatible source combination, governed
  analysis, source recovery or evidence-gap routing.
- **SKiN** — a rendered interface or interaction journey is changed or needs
  critique. It reviews experienced signal and utility, not implementation.
- **MrU** — a Places universe, Admin definition, source binding, lifecycle or
  rebuild currentness may be affected.

Add a domain specialist only when its distinct evidence or perspective changes
the result. For distinct independent work packages, use parallel agents when
available; otherwise run the highest-risk dependency first. Do not use agents
merely to restate one another's view.

## Dispatch and receipt

For substantive work, announce the selected lanes and why in one compact Sark
dispatch. Give each lane a bounded question, frozen scope, permitted actions
and expected receipt. Never claim a lane ran because its skill exists or because
it was named in a plan.

Collect the necessary receipts before describing substantive work as complete:
question, evidence inspected, finding/verdict, resulting action, proof boundary
and residual uncertainty. Route each finding to its owner instead of merging
all perspectives into a generic review.

The end-of-turn response should say which lanes actually ran, what they found,
which lanes Sark deliberately did not activate, and the local/preflight/Product/
release boundary where relevant.

## Avoid orchestration theatre

- Never use one reviewer as a substitute for another.
- Never let tests, a clean folder, a polished screen or a caveat replace the
  purpose, runtime, inference or UX question owned by its lane.
- Never turn GREY or WISHFUL into vetoes; they improve the reading and route.
- Never expand authority, publish, deploy, delete or contact anyone merely
  because Sark selected a lane.
- Never hold a simple answer hostage to a full team ceremony.
