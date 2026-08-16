# Chapter 1 Freeze Gates

Status: live validation tracker. This file records what evidence is still required before Chapter 1 can move from authored draft toward verified/frozen status. It does not create new substantive requirements beyond existing Chapter 1 governance.

## Current authored state

- Six-section manuscript complete: **yes**
- Integrated manuscript revision after first complete-draft audit: **yes**
- Parallel cold-transfer forms separated: **yes**
- Post-production rubric separated: **yes**
- Diagnosis feedback separated: **yes**
- Source/citation audit completed: **yes**
- Water-domain authoritative precheck completed: **yes**
- Pre-SME realism wording controls applied to `anchor.md` and `case-data.md`: **yes**
- Human SME review packet prepared: **yes**
- Timed-reader/cold-transfer protocol prepared: **yes**
- Pilot data-capture template prepared: **yes**
- Operational validation handoff prepared: **yes**

The chapter is therefore **authored and validation-ready**, not yet publication-frozen.

## Gate 1 — Human water-domain SME

**Status: OPEN**

Required evidence:

- a human drinking-water utility / engineering reviewer has examined the anchor operating story;
- reviewer disposition is recorded as `PASS`, `PASS WITH WORDING CHANGES`, or `REVISE MECHANISM`;
- the five focused questions in `sme-review-water-anchor.md` are answered or explicitly marked outside reviewer expertise;
- any accidental unsafe/universal implications are identified.

Gate closes when:

- author adjudication of reviewer comments is complete;
- accepted changes are synchronized through governed case artifacts and reader-facing prose;
- unresolved mechanism concerns are either repaired or explicitly block freeze.

## Gate 2 — Session 1 timed reader + cold transfer

**Status: OPEN**

Required evidence:

- participant-level timing recorded against an exact manuscript commit;
- opening attempt preserved;
- three self-explanation pauses captured;
- planted-failure diagnosis captured before feedback;
- first cold-transfer form completed without visible rubric/checklist/worked solution;
- eight rubric dimensions recorded after production;
- retrieval-from-memory task completed;
- reader debrief captured;
- contamination/version issues recorded.

Gate does **not** require a validated total score.

## Gate 3 — Delayed parallel-form retest

**Status: OPEN**

Required evidence:

- second form remains unseen until retest;
- actual delay falls within or is interpretable against the current 7–14 day pilot window;
- reader does not reread Chapter 1 immediately before the task;
- original delayed response preserved;
- eight rubric dimensions recorded after production;
- major category errors and domain-familiarity effects recorded.

Gate closes when delayed evidence is available for author adjudication; it does not imply proven durable far transfer.

## Gate 4 — Pilot adjudication

**Status: BLOCKED BY GATES 2–3**

Required output:

For each material finding separate:

1. observed evidence;
2. interpretation;
3. author decision;
4. scope of change;
5. follow-up evidence needed.

Inspect at minimum:

- 4-hour feasibility;
- usefulness of the 5-minute opening;
- distinct value of all three self-explanation pauses;
- approximate active-production/retrieval share relative to the 50% guardrail;
- cold-transfer 30–40 minute feasibility;
- hidden-domain-knowledge problems;
- form/order effects;
- repeated weak rubric dimensions;
- major category errors;
- delayed-retention/transfer weaknesses;
- premature feedback or answer-reveal problems.

## Gate 5 — Final manuscript synchronization

**Status: BLOCKED BY GATES 1 AND 4**

Required work:

- synchronize accepted SME wording into `chapter.md`;
- apply pilot-based manuscript/exercise changes;
- keep governed case facts and reader-facing prose consistent;
- verify transfer links, rubric reveal, and delayed-form concealment;
- remove any temporary pilot-facing wording that should not remain in publication text;
- preserve source/citation discipline.

## Gate 6 — Final chapter audit

**Status: BLOCKED BY GATE 5**

Audit:

- architecture remains 24 pages / 4 hours unless pilot evidence justifies reopening a parameter;
- all six sections still serve their governed jobs;
- central question and core competence remain intact;
- reveal order is coherent;
- exactly two worked backward revisions remain conceptually distinct;
- analysis, recommendation, and decision remain distinct;
- evidence does not silently determine values;
- prediction/association is not used as intervention evidence;
- dynamics/feedback remain introductory rather than formal Chapter 13–15 material;
- synthetic water values are not presented as standards or norms;
- all citation keys resolve and source-note cautions are respected;
- no exercise exposes answer/rubric/parallel form before production;
- timed/pilot parameters are described as pilot-derived design choices rather than universal optima;
- no unsupported durable-far-transfer claim appears.

## Gate 7 — Freeze decision

**Status: BLOCKED BY GATE 6**

Possible dispositions:

- `FREEZE` — no material unresolved Chapter 1 defect remains;
- `FREEZE WITH DEFERRED NON-BLOCKING ITEMS` — only explicitly documented editorial/housekeeping work remains;
- `REVISE AND RE-PILOT` — a material instructional or domain defect requires another evidence cycle;
- `REOPEN GOVERNED DECISION` — only if evidence contradicts a frozen Chapter 1 design choice strongly enough to justify reopening it.

Do not use lack of a CI status response as evidence that the chapter failed validation. CI/build verification is a separate repository/tooling matter.

## Non-blocking housekeeping

The following may remain open without blocking the validation sequence unless they create a concrete conflict:

- consolidation of stale `notes.md`;
- later book-wide recurrence decisions;
- cosmetic layout refinement not affecting task concealment or comprehension;
- optional figure polishing;
- repository CI visibility if the GitHub integration cannot access combined status.

## Next evidence needed

At present, meaningful progress requires at least one external observation:

1. returned human SME review; or
2. actual Session 1 participant data.

Without one of those, additional manuscript tuning would be speculative rather than evidence-driven.