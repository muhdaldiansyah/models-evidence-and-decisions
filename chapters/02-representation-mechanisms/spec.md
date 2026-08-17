---
chapter: 2
part: 1
title: "Representation, Mechanisms, and Scale"
status: specified
pages_target: 29
hours_target: 6
---

# Chapter 2: Representation, Mechanisms, and Scale

> **Provisional.** This specification is built on `../../decisions/0009-chapter2-representation-terminology-and-boundary.md`, which is **PROPOSED and not author-adjudicated**. The nine Chapter 2 entries in `../../canon/terminology.md` are provisional for the same reason. Rejecting a clause of Decision 0009 invalidates the corresponding sections here. Title, central question, core competence, and the page and hour targets are **not** provisional — they are governed by `README.md` and `../../decisions/0001-book-architecture-freeze.md`.

## Central question

What is inside the model, at what grain, and how do parts produce behavior?

## Core competence

Construct purpose-relative representations using boundaries, entities, variables, states, mechanisms, abstraction, aggregation, scale, and alternative representations.

## Role in the book

Chapter 1 taught the reader to ask what is being asked, for what use, and what would count as an adequate answer. It ended with a first complete pass in which a representation was used but never examined.

Chapter 2's unique job is to make that representation an object of deliberate construction and comparison:

> Teach readers how to build and compare purpose-relative representations of a target system before asking whether the resulting quantities are well measured, whether the resulting records are representative, or whether the representation survives systematic criticism.

The chapter must accomplish five things.

1. Establish that a representation is selective by definition, that the selection is governed by a stated purpose, and that this is established practice across engineering, the sciences, and agency standards rather than a stance this book invented.
2. Give the reader a repeatable way to decide what goes inside a boundary, what counts as a part, what must be carried forward, and at what grain — and to say why, in terms of the question being answered.
3. Let the reader draw a mechanism while knowing exactly what drawing it has and has not established.
4. Make the difference between leaving something out and putting something false in a distinction the reader can apply, and make the different burdens of defence that follow from it explicit.
5. Show, on one system, that a representation can be adequate for one purpose and inadequate for another — so that "which representation is correct?" is replaced by "correct for which question?"

The chapter is not a survey of modelling formalisms. It teaches no notation. It should leave the reader able to build two defensible representations of an unfamiliar system and to say what each can and cannot answer.

The generalization from **phenomenon-relativity** (established: a mechanism is always a mechanism *of* some phenomenon) to **purpose-relativity of representation generally** is this book's pedagogical synthesis and must be labelled as such, per `../../canon/pedagogy.md`.

## Hard prerequisites

- Chapter 1, specifically: intended use, target, decision situation, and the claim-type screen.
- Ordinary arithmetic, ratios, percentages, and the ability to read a small table.
- Ability to sketch a labelled box-and-arrow diagram. No drawing skill and no software are required.
- No calculus, no differential equations, no probability, no programming.
- No domain expertise. All case facts needed for every task must be supplied in the chapter.

## Soft dependencies / spiral links

| Spiral element | Treatment in Chapter 2 | Later development |
|---|---|---|
| Purpose governs content | Extended from Chapter 1's intended use to what is inside the representation | Chapters 5, 12, 16–17 |
| Boundary | Analytical cut governed by purpose and provisional; taught by example and warning | Chapters 4, 9, 13 |
| State | What must be carried forward to answer what comes next; no evolution law | Chapters 13, 14 |
| Mechanism | Parts, activities, organization — proposed, never established | Chapters 5, 7 |
| Aggregation | Representational aggregation only, before any data exist | Chapters 4, 8, 9 |
| Alternative representations | Different representations for different purposes; robustness across them | Chapters 5, 12 |
| Grain and scale | Resolution as a decision with consequences for the answerable question set | Chapters 3, 4, 9, 13 |

## Established concepts to cover

### Representation and its target

- A representation stands for a **selected** part or aspect of a target system; selection is definitional, not a concession (`frigg2025models` §1).
- The target system is not the model; the model is not its description (`frigg2025models` §2.4).
- Chapter 2's `target system` is not a renaming of Chapter 1's `target`.
- Which model is right depends on the question: "The model we choose depends on the questions we wish to answer, and so there may be multiple models for a single dynamical system, with different levels of fidelity depending on the phenomena of interest" (`astrom2008feedback` p. 27).
- A faithful one-to-one representation would fail even if achievable — unmeasurable, unsolvable, and above all uninterpretable (`levins1966strategy` p. 421).

### Boundary

- The cut is analytical, not physical; governed by purpose; provisional.
- Narrow boundaries can hide delayed and distal consequences (`sterman2006evidence`).
- Widening enables new questions rather than merely adding work (`astrom2008feedback` p. 29).
- Where the cut falls can change the internal description, not only its size (`astrom2008feedback` p. 33).
- Agency practice requires the documented intended use to state what is represented (`nasa2024models` §4.1.1.1).

### Parts, roles, and state

- Entities are the things that engage in activities (`machamer2000mechanisms` p. 3).
- Roles — carried forward, acted on from outside, observed — are assigned within a representation; the same quantity can take different roles in different representations of one system.
- The state is what summarizes the past well enough to answer what comes next; the canonical definition is itself purpose-qualified (`astrom2008feedback` pp. 28, 34).
- Grain is a decision: "A key issue in modeling is to decide how accurately this storage has to be represented" (`astrom2008feedback` p. 34).

### Mechanism

- Minimal formulation: a mechanism *for a phenomenon* is a set of parts whose activities and interactions are organized so as to be responsible for that phenomenon (`craver2026mechanisms` §2).
- Phenomenon-relativity: "All mechanisms are mechanisms *of* some phenomenon" (`craver2026mechanisms` §2.1.1); boundaries are fixed by relevance to the phenomenon (§5.1).
- A drawn mechanism is a hypothesis. Four signs it remains one: an arrow with no nameable activity; a black box; a could-produce rather than does-produce claim; no intervention having tested it (`machamer2000mechanisms` pp. 3, 17, 18; `craver2026mechanisms` §3.3).
- Intervention supplies the evidence, not the diagram (`machamer2000mechanisms` p. 17).
- Association alone is insufficient for an intervention conclusion (`pearl2009causal`).

### Abstraction, idealization, generality

- Abstraction is omission; it is silent, and silence asserts nothing false (`weisberg2007idealization` fn. 14; `frigg2025models` §1).
- Idealization is the assertion of something known to be false.
- The asymmetry of defence: an omission is defended by irrelevance to the question; a distortion must be defended by tolerability of the induced error.
- Abstraction is not generality: "Abstraction is an issue of the amount of detail … The generality of a schema is the scope (small or large) of the domain in which it can be instantiated" (`machamer2000mechanisms` p. 16).
- Legitimacy of a simplification "depends not only on the reality to be described but also on the state of the science" (`levins1966strategy` pp. 421–422), demonstrated by the constant-environment case (p. 422).

### Aggregation, grain, and scale

- Representational aggregation is treating distinguishable things as one for the purpose at hand — a choice made before any data exist.
- It is distinct from aggregation introduced by observation, recording, or reporting, which is Chapter 4.
- Some features of a representation carry meaning and others are artifacts; on a map you know which, in a model often not (`levins1966strategy` p. 423).

### Alternative representations

- Multiple models of one system at different fidelities are normal engineering practice (`astrom2008feedback` pp. 27, 32).
- Building several deliberately different representations is a **method**: conclusions surviving across them are more trustworthy — robust theorems, "our truth is the intersection of independent lies" (`levins1966strategy` p. 423).

## Terminology to introduce or stabilize

Nine terms are registered provisionally in `../../canon/terminology.md` under the Chapter 2 block. The terminology burden must stay low; everything not listed as controlled is ordinary careful language.

| Term | Treatment in Chapter 2 | Distinction or caution |
|---|---|---|
| representation | Required; default word for the constructed object | Interchangeable with `model`; no distinction manufactured; selection is definitional |
| target system | Required | Not a renaming of Chapter 1's `target`; `focal system` rejected as an unnecessary coinage |
| boundary | Required | Analytical, not physical; purpose-governed; provisional; taught by example and warning, **not** by criterion |
| mechanism | Required, always phenomenon-indexed and hedged | *Proposed*, *represented*, *could produce* — never *established*, never *causes*; regularity **not** required of the reader |
| abstraction | Required | Omission, hence silent; keep apart from generality |
| idealization | Named contrast only | Assertion of falsehood; no Galilean/minimalist/MMI taxonomy |
| generality (scope) | Required | Size of the domain of instantiation; a different dial from detail |
| aggregation | Required, always qualified as representational | Chapter 4 owns observation/reporting aggregation; **no source defines the Chapter 2 sense** — demonstrate, do not cite |
| state | Required at representation depth | What must be carried forward; not "a variable that changes"; a property of the representation, not the system |

Used as **ordinary careful language**, not registry-controlled: entity, part, variable, grain, resolution, fidelity, scale, role, interface.

**Avoided entirely:** `level` (overloaded past repair at this depth); `coarse-graining` (physics-specific, unsourced); `parameter` as controlled vocabulary; `state space`; `how-possibly`/`how-actually` and `schema`/`sketch` as required reader terms.

**No symbolic notation.** No `x`, `u`, `y`; no state-space form; no order, linearity, reachability, or observability.

## Interfaces with other chapters

| Chapter | Interface established here | Boundary Chapter 2 must respect |
|---|---|---|
| Ch. 1 | Purpose and intended use now govern the *content* of the representation, not only the adequacy of the answer | Do not reteach decision framing as main content |
| Ch. 3: Measurement | A represented quantity is distinguished from its observation | Do not teach validity, reliability, operationalization, or measurement error |
| Ch. 4: Observation and provenance | Representational aggregation is explicitly separated from aggregation in records | Do not inventory sampling, selection, missingness, censoring, or reporting mechanisms |
| Ch. 5: Assumptions and rival models | Alternative representations exist and can be compared | Do not teach assumption records, dimensional or limiting checks, Fermi bounds, verification, validation, or rival-model falsification |
| Ch. 6: Probability | Uncertainty about what to represent is acknowledged | No probability, distributions, or simulation |
| Ch. 7: Identification | Mechanisms are drawable and hypothetical; intervention is what would test them | Do not define estimands, identifiability, causal graphs, or identification strategies |
| Ch. 8: Estimation | Representations have quantities that would have to be estimated | No estimators, likelihood, regression, or model checking |
| Ch. 9: Transport | Scale and population grain are representational choices | Do not teach external validity, generalizability, target populations, or transportability |
| Ch. 10–12: Choice | Representations serve decisions and may be built for optimization | No objectives, utility, trade-offs, constraints, or solvers |
| Ch. 13: Dynamics | `state` is introduced as what must be carried forward | Do not teach evolution laws, stock-flow, delay, feedback loops, equilibrium, stability, oscillation, or policy resistance |
| Ch. 14: Sequential and control | Roles include what is acted on and what is observed | Do not teach policies, observability, structural identifiability, filtering, or control |
| Ch. 15: Strategic | Representations may contain agents who respond | Do not teach equilibrium, games, incentives, or endogenous response |
| Ch. 16–17: Integration and deployment | Representation choice is one stage the reader can now perform deliberately | Chapter 2 is heavily scaffolded; independent triage is Chapter 16 |

## Scope boundary

### Core

The chapter must teach the reader to do the following at an introductory but productive level.

- State a purpose precisely enough that it constrains what must be represented.
- Draw an explicit boundary, and defend at least one inclusion and one exclusion by reference to the purpose.
- Recognize that a boundary is analytical rather than physical, and that it is provisional.
- List the parts of a representation and assign each a role: carried forward, acted on from outside, or observed.
- Identify what must be carried forward — the state — using the test that a quantity recomputable from others, or irrelevant to what comes next, is not state.
- Choose a grain and say what the choice makes answerable and unanswerable.
- Draw a mechanism for a **specified phenomenon**, and state its epistemic status in words the reader can defend.
- Apply the four-sign check that distinguishes a hypothesized mechanism from an established one.
- Distinguish leaving something out from putting something false in, and state the different defence each requires.
- Distinguish reducing detail from widening scope.
- Identify an aggregation and demonstrate, arithmetically, one decision under which it hides something material.
- Separate representational aggregation from aggregation produced by observation or reporting.
- Build two representations of one target system for two different purposes, and state what each can and cannot answer.
- Identify one simplification whose verdict **flips** between two stated purposes.
- Recognize that a conclusion surviving across differently simplified representations is more trustworthy than one that does not.
- Revise a representation when the purpose changes, without treating the revision as an admission of prior error.

### Deferred to later chapters

- Constructs, operationalization, proxies, validity, reliability, measurement error: Chapter 3.
- Sampling, selection, missingness, censoring, reporting, institutional production of records, aggregation in data: Chapter 4.
- Assumption records, dimensional and extreme-condition checks, Fermi bounds, verification, validation, structural uncertainty, rival-model criticism: Chapter 5.
- Probability, conditioning, expectation, simulation, calibration: Chapter 6.
- Estimands, statistical identifiability, causal identification, causal graphs, do-calculus, identification strategies: Chapter 7.
- Estimators, likelihood, regression, uncertainty quantification, model checking: Chapter 8.
- Evidence synthesis, external validity, generalizability, target populations, transportability: Chapter 9.
- Values, objectives, metrics, utility, alternatives generation: Chapter 10.
- Decision trees, expected utility, sensitivity, value of information: Chapter 11.
- Optimization, constraints, robustness formalism, regret, adaptive plans: Chapter 12.
- Stock-flow representation, accumulation analysis, delay models, feedback-loop analysis, equilibrium, stability, oscillation, policy resistance: Chapter 13.
- Policies, sequential information, observability, structural identifiability, control: Chapter 14.
- Strategic dependence, incentives, equilibrium, principal-agent reasoning, endogenous response: Chapter 15.
- Independent triage and post-deployment monitoring: Chapters 16 and 17.

### Deferred to depth curriculum

- Formal theories of scientific representation: similarity, isomorphism, inferential, and fictional accounts.
- The idealization taxonomy: Galilean, minimalist, and multiple-models idealization and their justifications.
- Model theory, the semantic view of theories, and the models-as-mediators programme.
- Formal aggregation theory, perfect aggregation conditions, and near-decomposability.
- Multiscale modelling, renormalization, homogenization, and coarse-graining formalism.
- Zeigler-style system specification hierarchies and experimental frames.
- Compositional and object-oriented modelling languages, differential-algebraic formulations, and model libraries.
- The mechanistic-explanation literature's debates on constitution, levels, and mechanistic causation.

## Section architecture

The chapter uses one recurring anchor — the Chapter 1 water utility, extended to its distribution network — developed incrementally through the concept sections and consolidated in a worked three-way comparison. Three short contrasts each isolate exactly one representation choice.

| Section | Working title | Pages | Learning hours | Primary output |
|---|---|---:|---:|---|
| 1 | The Same System, Two Questions | 2 | 0.30 | An unscaffolded representation, produced before any Chapter 2 vocabulary |
| 2 | Boundary: What the Question Puts Inside | 5 | 1.00 | An explicit boundary with one defended inclusion and one defended exclusion |
| 3 | Parts, Roles, and What Must Be Carried Forward | 5 | 1.00 | A role table for the anchor, with the state identified and justified |
| 4 | Mechanism: What Would Have to Be True | 4 | 0.80 | A drawn mechanism for a specified phenomenon, with its epistemic status stated |
| 5 | Leaving Out, Making Up, and Lumping Together | 6 | 1.15 | A defended simplification set, and one aggregation shown arithmetically to hide a decision-relevant difference |
| 6 | Three Representations of One Utility | 4 | 0.85 | A worked comparison of storage-only, treatment-and-demand, and network representations against three purposes |
| 7 | Cold-Start Practice and Retrieval | 3 | 0.90 | An independently constructed representation pair on an unfamiliar system |
| **Total** |  | **29** | **6.00** |  |

### Drafting constraints

- The anchor is developed incrementally in sections 2–5 so that section 6 is consolidation and comparison, not first exposure.
- At least half of active learning time must be prediction, production, explanation, diagnosis, or retrieval, per `../../decisions/0008`.
- Three self-explanation pauses, placed at boundary choice (§2), at the aggregation failure (§5), and at the mechanism's epistemic status (§4).
- Support fades between §6 and §7. Reasoning prompts fade; case facts never do.
- No section may introduce notation.
- Every diagram must be reproducible by hand in under two minutes.

## Examples / recurring cases

### Primary anchor: the Chapter 1 water utility, extended to its distribution network

Recurrence is permitted by `readiness-audit.md` §7 only if a genuinely new operation is added. The new operation is the three-way representation comparison.

The pedagogical core: Chapter 1's single-tank representation was **adequate** for its question — will usable storage breach the operating reserve within seven days? — and is **inadequate** for a different one: if we must restrict supply, who loses service first? Same system, same representation, verdict flips with the purpose.

This mirrors the verified `levins1966strategy` p. 422 case in which a constant-environment assumption was legitimate for one question and is not for another.

**New synthetic facts required.** Pressure zones, elevations, per-zone demand, and pump capacity are not in Chapter 1's frozen `case-data.md`. Chapter 2 requires its own governed case-data file. Those facts inherit Chapter 1's **open SME gate**; Chapter 2's extension cannot be more validated than the case it extends.

### Short contrast 1 — pendulum, two purposes

Deliberate recurrence performing a new operation. For "how long is one swing": length and gravity, air resistance omitted. For "why does it eventually stop": air resistance and pivot friction become the whole point. Same object, two entity sets, both correct. Two sentences.

### Short contrast 2 — an average that is fine, then isn't

An aggregate adequate for one decision that hides the deciding fact for another. The arithmetic must be checkable without a calculator. **Design constraint:** the aggregate must be genuinely fine for the first purpose, or the contrast teaches "averages are bad" instead of "adequacy is purpose-relative."

### Short contrast 3 — a mechanism that establishes nothing

Non-numeric. Two mechanisms are drawable for the same association, running in opposite directions. Both drawable, neither established. Hands off to Chapter 7 without teaching any of it.

### Deliberately not used

Predator–prey, traffic flow, and epidemic models — all pull toward dynamics, feedback, or causal identification. The Chapter 1 student-assessment contrast — its interest is measurement validity, which is Chapter 3.

## Exercise architecture

Following the book-wide scaffold governed by `../../decisions/0008`.

### 1. Opening attempt (§1)

Represent the utility for a stated purpose, unscaffolded, before any Chapter 2 vocabulary. Preserved unscored as a baseline for later comparison.

### 2. Boundary defence (§2)

Given a purpose, state one inclusion and one exclusion and defend each. Then given a second purpose, state which of the two decisions changes.

### 3. Role table and state test (§3)

Complete a role table for the anchor. Apply the state test to two candidate quantities, one of which is recomputable from others and therefore fails.

### 4. Mechanism with epistemic status (§4)

Draw a mechanism for a specified phenomenon. Then apply the four-sign check and write one sentence stating what the drawing has and has not established.

### 5. Aggregation demonstration (§5)

Compute an aggregate, then compute the disaggregated quantities, then state the decision under which the difference matters. The reader must produce the arithmetic, not read it.

### 6. Planted-defect diagnosis (§6)

Five defects, each mapping to one high-risk collapse from `readiness-audit.md` §5:

| Planted defect | Collapse targeted |
|---|---|
| A representation defended as "more realistic" with no purpose stated | detail = realism = adequacy |
| A drawn mechanism captioned as an established effect | mechanism = causal effect |
| An aggregate hiding a decision-relevant difference | aggregation harmless |
| A boundary drawn at a physical edge rather than an analytical one | boundary = physical edge |
| A quantity called `state` that is recomputable from others | state = any variable |

Diagnosis must include the defect, its consequence for what the representation can answer, and a repair.

### 7. Cold-transfer production task (§7)

One parallel form, produced without the chapter's checklist, worked comparison, or rubric visible.

### 8. Retrieval and delayed retest (§7)

Reconstruct the representation checklist from memory before checking it. Delayed retest on the other parallel form, per the pilot window in `../../decisions/0008`.

### Rubric dimensions

Diagnostic, dimension-level, no validated aggregate cut score — consistent with `../../decisions/0008`.

1. Purpose stated precisely enough to constrain content.
2. Boundary explicit, with defended inclusion and exclusion.
3. Parts identified and roles assigned.
4. State correctly identified and justified.
5. Mechanism drawn for a specified phenomenon, with epistemic status stated correctly.
6. Simplifications distinguished as omission or distortion, with the appropriate defence.
7. Aggregation identified and its failure demonstrated, not asserted.
8. Two representations compared, with one simplification whose verdict flips between purposes.

## Transfer target

> Given an unfamiliar system and **two different stated purposes**, construct two defensible representations, state what each includes and excludes and why, and identify one simplification that is acceptable under the first purpose and unacceptable under the second.

The final clause is discriminating. A reader who produces two representations but cannot name a simplification whose verdict flips has produced two drawings, not demonstrated the competence.

### Parallel forms

- **Form A — regional blood supply** (physical/logistical). Shelf life gives natural accumulation; blood types give heterogeneity so total units can be adequate while one type is short; donors, laboratory, transport, and hospitals give real boundary questions.
- **Form B — city rental-assistance programme** (institutional). Application backlog gives the state; concentrated district need gives the same aggregation structure in institutional clothing.

Both demand identical structural outputs; only the surface domain differs. Every Chapter 1 transfer domain is excluded, so a reader completing both chapters meets no repeated domain.

Chapter 2 must not claim durable far transfer. It aims to establish an initial independent representation-construction capability and to generate diagnostic evidence about remaining failure.

## Evidence / source plan

### Source discipline

Per `../../decisions/0003`. Every citation key must exist in `../../references.bib` with a matching note in `../../sources/`.

### Load-bearing sources

| Claim | Source |
|---|---|
| Representation is selective; model ≠ target ≠ description | `frigg2025models` §1, §2.4 |
| Model choice depends on the question; multiple models at different fidelity | `astrom2008feedback` pp. 27, 32 |
| A faithful one-to-one model fails, including by being uninterpretable | `levins1966strategy` p. 421 |
| Legitimacy of simplification depends on the question | `levins1966strategy` pp. 421–422 |
| Intended use must state what is represented | `nasa2024models` §4.1.1.1 |
| Narrow boundaries hide distal consequences | `sterman2006evidence` |
| Widening enables new questions; the cut changes the internal description | `astrom2008feedback` pp. 29, 33 |
| Entities engage in activities | `machamer2000mechanisms` p. 3 |
| State is purpose-qualified; grain is a decision | `astrom2008feedback` pp. 28, 34 |
| Minimal mechanism; phenomenon-relativity | `craver2026mechanisms` §2, §2.1.1, §5.1 |
| A drawn mechanism is a hypothesis; intervention is the evidence | `machamer2000mechanisms` pp. 3, 17, 18 |
| Association alone is insufficient for intervention conclusions | `pearl2009causal` |
| Abstraction is omission; idealization asserts falsehood | `weisberg2007idealization` fn. 14; `frigg2025models` §1 |
| Abstraction is not generality | `machamer2000mechanisms` p. 16 |
| Map analogy; robust theorems across representations | `levins1966strategy` p. 423 |

### Known source gaps constraining the manuscript

1. **No sourced boundary-selection procedure.** §2 teaches by example and warning. The manuscript may not present a general procedure as sourced.
2. **No sourced definition of representational aggregation.** §5 demonstrates arithmetically. The manuscript may not cite a source for the Chapter 2 sense.
3. **`weisberg2007idealization` read in preprint.** Locators are section headings. Before freeze, the published *Journal of Philosophy* 104(12):639–659 text must be checked and locators converted to printed pages.
4. **Jones (2005) not read directly.** The omission/distortion distinction rests on two secondary reports and must be attributed as such.

### Evidence needed before prose is considered stable

- Water-domain SME review of the network extension, coupled to Chapter 1's open Gate 1.
- Timed reader pilot against the 6-hour target.
- Cold-transfer pilot on both parallel forms with counterbalanced order.

## Failure modes this chapter should prevent

Drawn from `readiness-audit.md` §5. Each must be actively defeated in the manuscript, not merely avoided.

1. **Representation = reality.** A representation selects and organizes for a purpose; it is not the system.
2. **Detail = realism = adequacy.** More detail can be irrelevant, unmeasurable, or uninterpretable.
3. **Boundary = physical edge.** Analytical boundaries include or exclude processes, actors, horizons, and scales where no wall exists.
4. **Mechanism = established causal effect.** A drawn mechanism is a hypothesis.
5. **State = any variable.** A quantity recomputable from others, or irrelevant to what comes next, is not state.
6. **Aggregation = data summarization only.** Representation aggregates before any data exist.
7. **Scale = just units.** Spatial, temporal, organizational, and population grain can differ with units unchanged.
8. **One true model.** Different representations of one system serve different purposes without one being globally correct.
9. **Alternative representation = rival-model criticism.** Chapter 2 compares for construction and perspective; Chapter 5 owns falsification.
10. **Mechanism = dynamics.** A representation can contain mechanisms without feedback, stability, or control machinery.
11. **Simpler = more general.** Reducing detail and widening scope are different moves (`machamer2000mechanisms` p. 16).
12. **Revision = prior error.** Changing a representation when the purpose changes is correct practice, not a confession.

## Open questions

### Before drafting

1. Does the author accept Decision 0009 as proposed, and if not, which clauses change?
2. Does the author accept the water-network recurrence, given that it couples Chapter 2 to Chapter 1's open SME gate?
3. Is `state` reader-facing Chapter 2 vocabulary, or is the idea taught without the word until Chapter 13?
4. Are three self-explanation pauses right for a 6-hour chapter when Chapter 1 uses three for 4 hours?
5. Should the loyalty-app contrast be replaced by a case with no commercial framing?

### Before declaring Chapter 2 verified or frozen

6. Has the published Weisberg text been checked and its locators converted?
7. Has Jones (2005) been read, or is the attribution left explicitly second-hand?
8. Has the network extension passed water-domain SME review?
9. Do the transfer forms need their own SME check?
10. Does the 29-page / 6-hour budget survive a timed reader pilot?
11. Is R01 reopened for a boundary-selection source, or does the chapter stand on example and warning?
