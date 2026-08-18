# Terminology Registry

This file is an authoring control artifact, not necessarily the reader-facing glossary.
It records the book's preferred terms and the distinctions that must never be collapsed (see `README.md`, Intellectual Principle).
The manuscript must conform to this registry; introducing or varying a term requires an entry here.
Definitions marked `TODO` are placeholders pending verification against canonical sources; they are not verified definitions.

Entry format:

```md
## term

- Preferred term:
- Field/origin:
- Introduced in:
- Distinct from:
- Aliases/cautions:
- Definition status: TODO / verified
```

## Index

65 entries, in registry order. Navigation only — the entries below are the record.

**Adjudicated (29).** Note that `construct`, `measure`, and `proxy` appear in this sequence but were filled in from proposed Decision 0010 and are provisional; see the Chapter 3 block. [intended use](#intended-use) · [context of use](#context-of-use) · [adequacy](#adequacy) · [positive](#positive) · [normative](#normative) · [decision](#decision) · [decision-maker](#decision-maker) · [alternative](#alternative) · [consequence](#consequence) · [statistical identifiability](#statistical-identifiability) · [causal identification](#causal-identification) · [structural identifiability](#structural-identifiability) · [construct](#construct) · [measure](#measure) · [proxy](#proxy) · [target](#target) · [target population](#target-population) · [estimand](#estimand) · [estimator](#estimator) · [estimate](#estimate) · [association](#association) · [prediction](#prediction) · [intervention](#intervention) · [counterfactual](#counterfactual) · [utility](#utility) · [objective](#objective) · [metric](#metric) · [robustness](#robustness) · [feedback](#feedback) · [stability](#stability) · [equilibrium](#equilibrium) · [observability](#observability)

**Provisional — Chapter 2 block (9), pending adjudication of [Decision 0009](../decisions/0009-chapter2-representation-terminology-and-boundary.md).** [representation](#representation) · [target system](#target-system) · [boundary](#boundary) · [mechanism](#mechanism) · [abstraction](#abstraction) · [idealization](#idealization) · [generality](#generality) · [aggregation](#aggregation) · [state](#state)

**Provisional — Chapter 3 block (12), pending adjudication of [Decision 0010](../decisions/0010-chapter3-measurement-terminology-and-boundary.md).** [working definition](#working-definition) · [operationalization](#operationalization) · [score](#score) · [validity](#validity) · [validation](#validation) · [reliability](#reliability) · [measurement error](#measurement-error) · [precision](#precision) · [trueness](#trueness) · [accuracy](#accuracy) · [measurand](#measurand) · [calibration](#calibration) — plus [construct](#construct), [measure](#measure), and [proxy](#proxy), filled in from the same decision in their existing positions above.

**Provisional — Chapter 4 block (7), pending adjudication of [Decision 0011](../decisions/0011-chapter4-observation-process-terminology-and-boundary.md).** [observation process](#observation-process) · [record](#record) · [selection](#selection) · [coverage](#coverage) · [nonresponse](#nonresponse) · [missingness](#missingness) · [censoring](#censoring)

**Provisional — Chapter 5 block (5), pending adjudication of [Decision 0012](../decisions/0012-chapter5-criticism-terminology-and-boundary.md).** [verification](#verification) · [assumption record](#assumption-record) · [rival model](#rival-model) · [structural uncertainty](#structural-uncertainty) · [failure mode](#failure-mode) — plus [adequacy](#adequacy) and [validation](#validation), updated from the same decision in their existing positions above.

## intended use

- Preferred term: intended use
- Field/origin: modeling and simulation / engineering M&S
- Introduced in: Chapter 1
- Distinct from: purpose; relevant application context; formal context of use; adequacy
- Aliases/cautions: established terminology in modeling and simulation for the expected purpose or application of an M&S; this book cautiously extends the expression to analyses, estimates, forecasts, and recommendations as a pedagogical synthesis meaning what the analytical result will be used to judge, decide, or do; do not present that extension as one universal formal disciplinary definition
- Definition status: verified for M&S usage; book extension adjudicated as pedagogical synthesis

## context of use

- Preferred term: context of use
- Field/origin: computational modeling and simulation VVUQ / model credibility
- Introduced in: Chapter 1 as an optional field-specific preview; formal home Chapter 5
- Distinct from: intended use; ordinary relevant application context; validation domain; target context
- Aliases/cautions: often abbreviated `COU` in ASME/FDA computational-model credibility practice; established but field-specific; do not present it as a universal synonym for intended use; Chapter 1 readers are not required to memorize the term or acronym
- Definition status: verified at introductory depth; formal Chapter 5 terminology review still required

## adequacy

- Preferred term: adequacy
- Field/origin: modeling and simulation / VVUQ / engineering evaluation; usage varies
- Introduced in: Chapter 1 in disciplined ordinary language; developed in Chapter 5
- Distinct from: accuracy; validity; validation; applicability; credibility; numerical correctness; fitness for purpose
- Aliases/cautions: Chapter 1 should normally say `adequate for the stated use` or `adequate for the stated intended use`; the book does not claim that this phrase denotes one universal standardized adequacy framework; individual traditions operationalize adequacy differently; **developed in Chapter 5**, where the full form is that a model is adequate *for a stated use, at a stated accuracy, for a stated quantity* — and **adequacy is not accuracy** (`fda2023credibility` §VI.D p. 33 separates quantifiable model accuracy from the judgment that total credibility evidence is sufficient for the context of use given model risk; `nrc2012reliability` Summary p. 3 treats validation as meaningful for specified quantities of interest and in relation to the accuracy required for an intended use); how much evidence is enough is governed by what happens if the model is wrong
- Definition status: verified for the Chapter 1 use-dependent principle; **Chapter 5 development provisional** under proposed `decisions/0012` §1, source-verified against `fda2023credibility` and `nrc2012reliability`

## positive

- Preferred term: positive
- Field/origin: economics for the paired positive/normative distinction; Chapter 1 applies it cautiously across analytical domains
- Introduced in: Chapter 1
- Distinct from: descriptive; empirical; objective; certain; normative
- Aliases/cautions: normally use `positive question` or `positive component`; at Chapter 1 depth it concerns what is, was, or would happen under specified conditions; a positive question may be descriptive, predictive, interventional, or counterfactual; `positive` does not mean favorable or beneficial and should not be presented as synonymous with objective, certain, or universally value-free
- Definition status: established economics usage verified; broader Chapter 1 transfer author-approved as a cautious pedagogical extension

## normative

- Preferred term: normative
- Field/origin: economics for the paired positive/normative distinction; broader disciplinary senses vary
- Introduced in: Chapter 1
- Distinct from: positive; descriptive; prescriptive; objective; utility; preference
- Aliases/cautions: at Chapter 1 depth concerns what should count as better, acceptable, important, or preferable, or what should be done; do not reduce normative reasoning to mere opinion; do not use `prescriptive` as a universal synonym because later decision-theory usage may distinguish it
- Definition status: paired economics usage verified; Chapter 1 introductory use author-approved; later decision-theory specialization remains deferred

## decision

- Preferred term: decision
- Field/origin: ordinary language / decision analysis / decision theory
- Introduced in: Chapter 1 at practical depth; formal home Chapter 11
- Distinct from: analytical question; target; analysis; recommendation; consequence
- Aliases/cautions: Chapter 1 uses `decision` for the selection, authorization, or commitment concerning an action or course of action by the relevant actor or institution; an analysis can inform a decision and a recommendation can advise a decision, but neither is the decision itself; not every analytical question immediately implies a decision
- Definition status: established usage verified at introductory depth; formal decision-under-uncertainty treatment remains Chapter 11

## decision-maker

- Preferred term: decision-maker
- Field/origin: decision analysis / decision theory / organizational decision practice
- Introduced in: Chapter 1
- Distinct from: analyst; recommender; stakeholder; implementer
- Aliases/cautions: the person, group, or institution with the relevant authority or responsibility for the immediate decision; authority may be distributed, and an attractive action outside that authority should be reframed as a request, escalation, negotiation, or another actor's decision rather than silently treated as feasible
- Definition status: verified at introductory practical depth; formal governance and decision-theory distinctions remain later work

## alternative

- Preferred term: alternative
- Field/origin: decision analysis / ordinary decision practice
- Introduced in: Chapter 1 at intuitive depth; formal value-focused development Chapter 10
- Distinct from: consequence; scenario; target; recommendation
- Aliases/cautions: a candidate course of action that can be chosen, authorized, requested, negotiated, or otherwise pursued through the relevant decision process; do not assume the initially supplied alternatives are complete; when the option set is materially narrow, consider at least one plausible missing, combined, contingent, information-gathering, or escalation alternative; `option` may appear in ordinary prose but `alternative` is preferred controlled vocabulary
- Definition status: introductory use verified; systematic alternative generation remains Chapter 10

## consequence

- Preferred term: consequence
- Field/origin: decision analysis / ordinary decision practice
- Introduced in: Chapter 1 at practical depth
- Distinct from: alternative; target; value; utility; recommendation
- Aliases/cautions: an outcome, effect, burden, benefit, cost, risk, or other material result that may occur under an alternative for a relevant stakeholder or system; evidence may inform beliefs about consequences, but the evaluation of those consequences requires values, requirements, or other decision premises; one analytical target rarely exhausts all decision-relevant consequences
- Definition status: verified at introductory practical depth; formal value and utility treatment remains Chapters 10–11

## statistical identifiability

- Preferred term: statistical identifiability
- Field/origin: statistics
- Introduced in: Chapter 7
- Distinct from: causal identification; structural identifiability
- Aliases/cautions: often just "identifiability" in statistics texts; always qualify in this book
- Definition status: TODO — verify against canonical sources

## causal identification

- Preferred term: causal identification
- Field/origin: causal inference / econometrics
- Introduced in: Chapter 7
- Distinct from: statistical identifiability; structural identifiability
- Aliases/cautions: unqualified "identification" in econometrics usually means this; always qualify
- Definition status: TODO — verify against canonical sources

## structural identifiability

- Preferred term: structural identifiability
- Field/origin: systems and control theory
- Introduced in: Chapter 14 (deferred from Chapter 7 per README)
- Distinct from: statistical identifiability; causal identification; observability
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

## construct

- Preferred term: construct
- Field/origin: measurement science / psychometrics; the concept-to-indicator framing follows social-science methodology
- Introduced in: Chapter 3
- Distinct from: measure; proxy; score; target; measurand; metric
- Aliases/cautions: the thing you are trying to measure, as opposed to any procedure for measuring it; rung 1 of the Chapter 3 ladder `construct → working definition → measure → score`; a construct is not fixed by choosing a measure for it (see `operationalization`); `adcock2001validity` §p. 530 separates the loose idea (their *background concept*) from the specific formulation adopted (their *systematized concept*), and this book calls the second a **working definition**; do not treat `construct` as implying a psychological or latent variable — it covers stored volume and service adequacy alike
- Definition status: **provisional** — introduced by proposed `decisions/0010`; source-verified against `adcock2001validity` p. 530

## measure

- Preferred term: measure
- Field/origin: measurement science; social-science methodology uses `indicator` for the same thing
- Introduced in: Chapter 3
- Distinct from: construct; working definition; score; proxy; metric; measurand
- Aliases/cautions: the **procedure** that produces numbers or classifications, not the numbers themselves and not the thing measured; rung 3 of the Chapter 3 ladder; `indicator` is the equivalent term in the literature and is named once, attributed (`adcock2001validity` p. 530: indicators are "also routinely called measures"); the procedure includes classification, not only quantification; distinct from the measure-theoretic sense, which this book does not use
- Definition status: **provisional** — introduced by proposed `decisions/0010`; source-verified against `adcock2001validity` p. 530

## proxy

- Preferred term: proxy
- Field/origin: measurement / econometrics
- Introduced in: Chapter 3
- Distinct from: construct; measure; score; target
- Aliases/cautions: a measure of something **else**, accepted because the construct cannot be measured directly or affordably; using a proxy is a substitution whose cost must be stated, not a free convenience; **a proxy's failure mode is structured, not random** — it fails in the specific circumstances where the substitution breaks, which is why more data does not repair it; do not write as though the proxy and the construct were the same quantity
- Definition status: **provisional** — introduced by proposed `decisions/0010`; the structured-failure point is the book's own formulation, not a cited claim

## target

- Preferred term: target
- Field/origin: ordinary and interdisciplinary analytic usage with multiple discipline-specific technical senses; the book-wide Chapter 1 use is pedagogical synthesis
- Introduced in: Chapter 1 (informal); Chapter 7 (formal specialization)
- Distinct from: construct; measure; operationalization; proxy; target quantity; estimand; estimator; estimate; response variable; label; decision; objective; metric
- Aliases/cautions: qualify whenever possible; the noun following `target` carries the substantive meaning; do not claim one universal technical definition; Chapter 1 uses `target` as the informal organizing word for what an inquiry is trying to determine about a focal entity, unit, population, or system
- Definition status: source-verified that disciplinary uses differ; book-wide Chapter 1 synthesis author-approved

## target population

- Preferred term: target population
- Field/origin: survey statistics / statistics / clinical research
- Introduced in: Chapter 1 (intuitive); formal development in Chapters 7 and 9
- Distinct from: observed sample; study sample; data-collection setting; target system
- Aliases/cautions: established qualified term for population-based questions; use only when inference or generalization concerns a population; do not force onto one-off physical-system problems
- Definition status: established at introductory depth; later source/study-population, transport, and generalization distinctions remain pending

## estimand

- Preferred term: estimand
- Field/origin: statistics / causal inference / clinical-trial methodology
- Introduced in: Chapter 1 as a concept preview only; formal home Chapter 7
- Distinct from: target; endpoint; estimator; estimate
- Aliases/cautions: Chapter 1 does not require the term; ICH E9(R1) provides an authoritative treatment-effect definition for its clinical-trial context, but that definition must not be presented as the book's universal cross-disciplinary definition; broader formal adjudication remains Chapter 7 work
- Definition status: clinical-trial usage verified; broader book-wide formal definition provisional pending Chapter 7 research

## estimator

- Preferred term: estimator
- Field/origin: statistics
- Introduced in: Chapter 8
- Distinct from: estimand; estimate
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

## estimate

- Preferred term: estimate
- Field/origin: statistics
- Introduced in: Chapter 8
- Distinct from: estimand; estimator
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

## association

- Preferred term: association
- Field/origin: statistics / epidemiology / causal inference
- Introduced in: Chapter 1 at intuitive depth
- Distinct from: correlation; prediction; causal effect; intervention
- Aliases/cautions: Chapter 1 uses `association` broadly for a relationship among variables, events, quantities, or states under observed or otherwise specified conditions; correlation is one narrower associational concept; association alone does not establish what would happen under intervention; do not infer that observational data can never support causal inference, because causal conclusions may use observational evidence together with additional causal assumptions or design information
- Definition status: technical associational-versus-causal distinction verified at introductory depth; broad reader-facing wording adjudicated for Chapter 1

## prediction

- Preferred term: prediction
- Field/origin: statistics / machine learning / forecasting
- Introduced in: Chapter 1 at intuitive depth; formal home Chapter 6
- Distinct from: description; causal explanation; intervention effect; counterfactual attribution
- Aliases/cautions: Chapter 1 uses prediction for an unknown, new, or future observable outcome given information available for making the prediction; prediction may exploit associations without causal interpretation; a useful predictor is not automatically a causal lever; `forecast` is a more specific future-directed term
- Definition status: verified at introductory depth; formal probabilistic prediction, uncertainty, scoring, and calibration remain Chapter 6

## intervention

- Preferred term: intervention
- Field/origin: causal inference / experimental science / policy evaluation
- Introduced in: Chapter 1 as an intuitive preview; formal home Chapter 7
- Distinct from: observed exposure; association; prediction; decision or recommendation
- Aliases/cautions: at Chapter 1 depth asks what would happen under an action or externally changed condition; state the action and comparison condition when material; association alone is insufficient for an intervention-effect claim, although observational evidence may contribute under additional causal assumptions and identification conditions
- Definition status: verified at introductory depth; formal causal targets, notation, identification, and design remain Chapter 7

## counterfactual

- Preferred term: counterfactual
- Field/origin: causal inference / philosophy / economics
- Introduced in: Chapter 1 as an intuitive preview; formal home Chapter 7
- Distinct from: generic hypothetical scenario; ordinary association; forecast
- Aliases/cautions: at Chapter 1 depth asks about an alternative outcome under a different action or condition while retaining relevant factual or background information about the case; do not use `counterfactual` as a loose synonym for any hypothetical scenario; do not present intervention and counterfactual as mutually exclusive formal categories because causal frameworks relate them closely
- Definition status: verified at introductory depth; framework-specific formal semantics, potential outcomes, and counterfactual notation remain Chapter 7

## utility

- Preferred term: utility
- Field/origin: decision theory
- Introduced in: Chapter 11
- Distinct from: objective; metric
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

## objective

- Preferred term: objective
- Field/origin: decision analysis / optimization
- Introduced in: Chapter 10
- Distinct from: utility; metric
- Aliases/cautions: values are structured before objectives are defined (Ch. 10)
- Definition status: TODO — verify against canonical sources

## metric

- Preferred term: metric
- Field/origin: TODO
- Introduced in: Chapter 10
- Distinct from: objective; measure; utility
- Aliases/cautions: metric gaming and Goodhart-type failures treated in Chapter 15
- Definition status: TODO — verify against canonical sources

## robustness

- Preferred term: robustness
- Field/origin: decision analysis / optimization
- Introduced in: Chapter 12
- Distinct from: stability
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

## feedback

- Preferred term: feedback
- Field/origin: dynamical systems / control / system dynamics
- Introduced in: Chapter 1 as an intuitive environment screen; formal home Chapter 13 with engineered-control specialization in Chapter 14
- Distinct from: ordinary evaluative or reviewer feedback; delay; accumulation; adaptive response; strategic response; stability
- Aliases/cautions: at Chapter 1 depth, use `feedback` when consequences of a process or action return through the system and influence later behavior, outcomes, information, or actions; do not teach `positive feedback` or `negative feedback`, loop polarity, controller design, or stability analysis here; feedback does not by itself imply adaptation or strategic behavior
- Definition status: verified at introductory systems depth; formal dynamical and control treatment remains Chapters 13–14

## stability

- Preferred term: stability
- Field/origin: dynamical systems
- Introduced in: Chapter 13
- Distinct from: equilibrium; robustness
- Aliases/cautions: README requires equilibrium-versus-stability to remain distinct
- Definition status: TODO — verify against canonical sources

## equilibrium

- Preferred term: equilibrium
- Field/origin: dynamical systems; game theory
- Introduced in: Chapter 13 (dynamic sense); Chapter 15 (strategic sense, "equilibrium as consistency")
- Distinct from: stability
- Aliases/cautions: the dynamic and strategic senses must not be conflated
- Definition status: TODO — verify against canonical sources

## observability

- Preferred term: observability
- Field/origin: control theory
- Introduced in: Chapter 14
- Distinct from: structural identifiability; the observation process (Chapter 4)
- Aliases/cautions: never use as a loose synonym for "measurable"
- Definition status: TODO — verify against canonical sources

---

## Chapter 2 block — PROVISIONAL

The nine entries below were introduced by **proposed** `decisions/0009-chapter2-representation-terminology-and-boundary.md`, which has **not** been author-adjudicated. They are recorded here so that Chapter 2's drafting is inspectable against a single vocabulary. Treat them as provisional: rejecting a clause of Decision 0009 invalidates the corresponding entry.

## representation

- Preferred term: representation
- Field/origin: philosophy of science; modeling and simulation; engineering
- Introduced in: Chapter 2
- Distinct from: the target system it represents; a description of the model (`frigg2025models` §2.4); reality
- Aliases/cautions: used interchangeably with `model` at Chapter 2 depth, preferring `representation` because it foregrounds selection and purpose; **no distinction between the two is manufactured**; a representation stands for a *selected* part or aspect of a target system, and selection is part of the definition rather than a later concession
- Definition status: verified — `frigg2025models` §1; `astrom2008feedback` p. 27

## target system

- Preferred term: target system
- Field/origin: philosophy of science (established)
- Introduced in: Chapter 2; reserved by Chapter 1's spec at orientation depth
- Distinct from: the model or representation of it; Chapter 1's `target`; target population; target quantity
- Aliases/cautions: **not a renaming of Chapter 1's `target`** — Chapter 1's `target` is what the answer is about, while the target system is the part of the world under representation; they frequently coincide and are not the same concept; `focal system` was considered and rejected as an unnecessary coinage
- Definition status: verified — `frigg2025models` §1

## boundary

- Preferred term: boundary (model boundary; system boundary)
- Field/origin: system dynamics; modeling and simulation; systems engineering
- Introduced in: Chapter 2
- Distinct from: a physical edge; the scope of a decision; the target population; the observation window
- Aliases/cautions: an analytical cut, not a wall; governed by purpose and provisional; narrowing can hide delayed and distal consequences (`sterman2006evidence`); widening enables new questions rather than merely adding work (`astrom2008feedback` p. 29); where the cut falls can change the internal description, not only its size (`astrom2008feedback` p. 33); **Chapter 2 teaches boundary choice by worked example and warning, not by criterion — no general selection procedure is sourced**
- Definition status: partially verified — component claims are sourced; no general boundary-selection theory was obtained (see `research-01-models-representations-boundaries.md` §3)

## mechanism

- Preferred term: mechanism
- Field/origin: philosophy of science (mechanistic explanation); life sciences
- Introduced in: Chapter 2, phenomenon-indexed and epistemically hedged; causal identification remains Chapter 7
- Distinct from: an identified causal effect; a correlation; structure or dependency without production; dynamics (Chapter 13); explanation
- Aliases/cautions: reader-facing definition is the **minimal** formulation — a mechanism *for a phenomenon* is a set of parts whose activities and interactions are organized so as to be responsible for that phenomenon (`craver2026mechanisms` §2); **always a mechanism *of* a specified phenomenon**, never of a system as such; the regularity-bearing `machamer2000mechanisms` p. 3 formulation is **not** the reader-facing one, since most of this book's cases are not regular; Chapter 2 may say a mechanism is *proposed*, *represented*, or *could produce* the phenomenon, and may **not** say it is *established* or that X *causes* Y; drawing a mechanism is a hypothesis — intervention is what supplies evidence (`machamer2000mechanisms` p. 17); how mechanisms relate to causation is itself contested (`craver2026mechanisms` §2.1.3) and Chapter 2 does not adjudicate it
- Definition status: verified — `craver2026mechanisms` §2, §2.1.1, §5.1; `machamer2000mechanisms` pp. 2–3, 17–18

## abstraction

- Preferred term: abstraction
- Field/origin: philosophy of science; mechanistic explanation
- Introduced in: Chapter 2
- Distinct from: idealization; generality or scope; aggregation; approximation; simplification as a loose synonym
- Aliases/cautions: abstraction is **leaving a feature out** — it is silent about what it omits, and silence asserts nothing false; must be kept apart from generality: "Abstraction is an issue of the amount of detail … The generality of a schema is the scope (small or large) of the domain in which it can be instantiated" (`machamer2000mechanisms` p. 16); the omission-versus-distortion cut is Jones's (2005) and is **one defensible position rather than consensus** — Weisberg reports it and declines to adopt it, and Aristotelian idealization is omission filed under idealization
- Definition status: verified as a reported position — `weisberg2007idealization` fn. 14; `frigg2025models` §1; `machamer2000mechanisms` p. 16

## idealization

- Preferred term: idealization
- Field/origin: philosophy of science
- Introduced in: Chapter 2 as a **named contrast only**; taxonomy deferred to the depth curriculum
- Distinct from: abstraction; error; approximation; falsification
- Aliases/cautions: idealization is **putting in something known to be false**; the asymmetry is what the reader needs — an omission is defended by showing the feature does not bear on the question, while a distortion must be defended by showing the error it introduces is tolerable for the use, which is a harder argument; do not teach Galilean, minimalist, or multiple-models idealization as reader vocabulary; the abstraction/idealization boundary is contested in the literature
- Definition status: verified as a reported position — `weisberg2007idealization` fn. 14; `frigg2025models` §1

## generality

- Preferred term: generality (scope)
- Field/origin: mechanistic explanation; model-building methodology
- Introduced in: Chapter 2
- Distinct from: abstraction; precision; realism; robustness; external validity and transportability (Chapter 9)
- Aliases/cautions: generality is the **size of the domain over which a representation can be instantiated**, which is a different dial from how much detail it contains; simpler and more general are different moves; the generality/realism/precision trade-off (`levins1966strategy` p. 422) is Levins's influential **strategy argument**, not a proven constraint, and is disputed in later literature that has not been inspected
- Definition status: verified — `machamer2000mechanisms` p. 16; `levins1966strategy` p. 422

## aggregation

- Preferred term: aggregation (representational aggregation, in Chapter 2)
- Field/origin: modeling practice; the term is also heavily used in data and reporting contexts
- Introduced in: Chapter 2 for representational aggregation; Chapter 4 for aggregation introduced by the observation, recording, or reporting process
- Distinct from: abstraction; aggregation in records and reporting (Chapter 4); the ecological fallacy and aggregate-to-individual inference (Chapters 4 and 9); averaging as a computation
- Aliases/cautions: in Chapter 2, aggregation means **treating distinguishable things as one for the purpose at hand**, a choice made before any data exist; the Chapter 2 / Chapter 4 split must be stated explicitly wherever the word appears; **no inspected source defines representational aggregation or supplies criteria for it**, so Chapter 2 demonstrates aggregation failure arithmetically in its own anchor case rather than citing one; do not import the ecological-fallacy literature
- Definition status: **unsourced at representation level** — taught by self-evidencing demonstration per Decision 0009 clause 6.3

## state

- Preferred term: state
- Field/origin: dynamical systems; control theory
- Introduced in: Chapter 2 at representation depth; formal home Chapter 13, with observability and control in Chapter 14
- Distinct from: any variable; a parameter; an observed or recorded value; the state space; equilibrium; stability
- Aliases/cautions: the state is **the collection of things that must be carried forward — what summarizes the past well enough to answer what comes next**; the canonical control-theory definition is itself purpose-qualified: "a collection of variables that summarize the past of a system for the purpose of predicting the future" (`astrom2008feedback` p. 34); a quantity recomputable from others, or irrelevant to what comes next, is **not** state; do not define state as "a variable that changes over time"; state is a property of the representation relative to what is to be predicted, not a property of the system; **no symbolic notation, no state-space form, no order, linearity, reachability, or observability in Chapter 2**; `state space` is not named until Chapter 13
- Definition status: verified — `astrom2008feedback` pp. 28, 34

---

## Chapter 3 block — PROVISIONAL

The twelve entries below were introduced by **proposed** `decisions/0010-chapter3-measurement-terminology-and-boundary.md`, which has **not** been author-adjudicated. The existing `construct`, `measure`, and `proxy` entries above were filled in from the same decision and carry the same provisional status.

## working definition

- Preferred term: working definition
- Field/origin: plain English for what `adcock2001validity` p. 530 calls a *systematized concept*
- Introduced in: Chapter 3
- Distinct from: construct; measure; score; a dictionary definition; a stipulation
- Aliases/cautions: the **specific formulation of a construct adopted for this analysis**, usually an explicit definition; rung 2 of the Chapter 3 ladder, and the rung most often skipped; skipping it means operationalizing a loose idea directly, so the procedure carries an unexamined choice about what the construct means; it is called a *working* definition because it is revisable — `adcock2001validity` p. 530 shows three upward revision tasks and p. 532 quotes Kaplan's paradox, resolved "by a process of approximation"; the source's own term is named once, attributed, and not used as working vocabulary because it is a field-specific coinage
- Definition status: **provisional** — proposed `decisions/0010` clause 1.3; content source-verified against `adcock2001validity` p. 530

## operationalization

- Preferred term: operationalization
- Field/origin: social-science methodology
- Introduced in: Chapter 3; the term appears in the chapter's governed title
- Distinct from: conceptualization; scoring; definition; calibration
- Aliases/cautions: the move from a **working definition to a measure** — not "turning a vague idea into a number", which conflates two rungs; **choosing a measure does not define the construct**, because interpretations of scores are falsifiable claims requiring evidence (`adcock2001validity` p. 532) and a stipulation cannot be falsified; the historical position that the procedure *is* the definition (operationism) may be mentioned as having existed but must not be characterized, since it was not researched
- Definition status: **provisional** — proposed `decisions/0010` clauses 1.4, 1.6; source-verified against `adcock2001validity` pp. 530, 532

## score

- Preferred term: score
- Field/origin: social-science methodology / measurement
- Introduced in: Chapter 3
- Distinct from: construct; working definition; measure; estimate; metric
- Aliases/cautions: what a measure produces for a case, including "both numerical scores and the results of qualitative classification" (`adcock2001validity` p. 530); rung 4 of the ladder; **a score is uninterpretable without its working definition** — "Scores are never examined in isolation; rather, they are interpreted and given meaning in relation to the systematized concept" (p. 531); two organizations reporting the same-looking score under different working definitions are not reporting comparable things
- Definition status: **provisional** — proposed `decisions/0010` clause 6.3; source-verified against `adcock2001validity` pp. 530–531

## validity

- Preferred term: validity
- Field/origin: measurement science / social-science methodology / psychometrics
- Introduced in: Chapter 3
- Distinct from: reliability; accuracy; trueness; precision; model validation (Chapter 5); internal and external validity of causal inference (Chapters 7 and 9); credibility
- Aliases/cautions: **a property of the interpretation of scores in relation to a construct, for a use — never a property of an instrument**; `adcock2001validity` p. 531 locates validation on "the conjunction of these components"; "is this measure valid?" is a **malformed question**, and the answerable form is "are these scores interpretable as this construct, for this use?"; teach **one validity with several kinds of evidence for it**, never a taxonomy of validities — the source reports 37 adjectives attached to the word and resolves them as "types of evidence for validity", not separate validities; **contextual specificity** holds: a measure valid in one context may be invalid in another (p. 530), which is Chapter 3's own point and must not be extended into Chapter 9's transportability; `adcock2001validity` p. 529 separates measurement validity from the validity of causal inference
- Definition status: **provisional** — proposed `decisions/0010` §2; source-verified against `adcock2001validity` pp. 529–531

## validation

- Preferred term: *avoided in Chapter 3*; **used in Chapter 5** in the computational-model sense
- Field/origin: two distinct traditions share the word
- Introduced in: named once in Chapter 3 as a collision to be avoided; **taken up in Chapter 5**, where the computational-model sense properly belongs
- Distinct from: validity; verification; calibration
- Aliases/cautions: **do not use as reader-facing Chapter 3 vocabulary**; in measurement it names the procedures for assessing evidence that scores support an interpretation (`adcock2001validity` p. 530 separates *validity* from *validation*), while in computational modelling it names assessment of whether a model is adequate for a context of use (`asme2025credibility`, `fda2023credibility`); Chapter 3 says *assessing the evidence for an interpretation* and names the collision explicitly once, so that readers arriving at Chapter 5 do not merge the two; **Chapter 5 uses the computational-model sense and must reopen the collision explicitly** rather than adopting the word silently — a reader who took Chapter 3's instruction seriously is owed an explanation of why the rule changed; the Chapter 5 pair is *verification asks whether you did the thing right; validation asks whether you did the right thing*
- Definition status: **provisional** — proposed `decisions/0010` clause 2.5 and `decisions/0012` clause 2.2; Chapter 5 sense source-verified against `asme2025credibility` slides 5–7

## reliability

- Preferred term: reliability
- Field/origin: social-science methodology / psychometrics; the metrology counterpart is precision
- Introduced in: Chapter 3
- Distinct from: validity; trueness; accuracy; robustness (Chapter 12); dependability in ordinary speech
- Aliases/cautions: concerns whether **repeated applications of a procedure yield consistent results** — "Random error, which occurs when repeated applications of a given measurement procedure yield inconsistent results, is conventionally labeled a problem of reliability" (`adcock2001validity` p. 531); **reliable does not mean valid** — an instrument can be highly repeatable and consistently wrong; how reliability relates to validity is **contested** and Chapter 3 shows the disagreement rather than resolving it (p. 532: on one account unreliable scores may still be correct "on average" and so valid; on another, reliability is "a necessary but not sufficient condition of measurement validity")
- Definition status: **provisional** — proposed `decisions/0010` clauses 3.1, 3.7; source-verified against `adcock2001validity` pp. 531–532

## measurement error

- Preferred term: measurement error
- Field/origin: metrology; social-science methodology uses `bias` for the systematic component
- Introduced in: Chapter 3; measurement-error models and correction are Chapter 8
- Distinct from: mistake; production error; uncertainty; residual; noise alone
- Aliases/cautions: VIM §2.16 defines it as "measured quantity value minus a reference quantity value", and Note 2 warns it "should not be confused with production error or mistake" — a general reader will otherwise hear *error* as *someone blundered*; **knowability is conditional**: §2.16 Note 1 makes the error known only where a reference value exists through calibration or convention; splits into **systematic** error (called **bias** in the social-science tradition, `adcock2001validity` p. 531) and **random** error; **where the construct is chosen rather than standardized there is no reference value to subtract from**, and error language must be used with visible care
- Definition status: **provisional** — proposed `decisions/0010` clauses 3.1, 3.6, 4.2; source-verified against `jcgm2012vim` §2.16 and `adcock2001validity` p. 531

## precision

- Preferred term: precision
- Field/origin: metrology (VIM §2.15)
- Introduced in: Chapter 3
- Distinct from: accuracy; trueness; resolution; certainty; significant figures
- Aliases/cautions: "closeness of agreement between indications or measured quantity values obtained by replicate measurements on the same or similar objects under specified conditions"; **precision is the one that is a number** — expressed by standard deviation, variance, or coefficient of variation; VIM §2.15 Note 4 records that "measurement precision" is sometimes **erroneously** used to mean measurement accuracy; **more measurements improve precision**; do not teach repeatability, intermediate precision, or reproducibility conditions (ISO 5725), which are specialist
- Definition status: **provisional** — proposed `decisions/0010` clause 3.1; source-verified against `jcgm2012vim` §2.15

## trueness

- Preferred term: trueness
- Field/origin: metrology (VIM §2.14)
- Introduced in: Chapter 3
- Distinct from: accuracy; precision; validity
- Aliases/cautions: "closeness of agreement between the average of an infinite number of replicate measured quantity values and a reference quantity value"; **not a quantity and not expressed numerically**; **inversely related to systematic measurement error and unrelated to random measurement error** — from which the chapter's central practical result follows: **more measurements do nothing for trueness**; VIM §2.14 states that "measurement accuracy" should not be used for trueness
- Definition status: **provisional** — proposed `decisions/0010` clauses 3.1, 3.4; source-verified against `jcgm2012vim` §2.14

## accuracy

- Preferred term: accuracy
- Field/origin: metrology (VIM §2.13)
- Introduced in: Chapter 3, taught as the **combination** of trueness and precision
- Distinct from: trueness alone; precision alone; validity; resolution
- Aliases/cautions: "closeness of agreement between a measured quantity value and a true quantity value of a measurand"; **accuracy is not a quantity and is not given a numerical quantity value** (§2.13 Note 1) — a measurement is said to be more accurate when it offers a smaller measurement error; §2.13 Note 2 forbids using the term for trueness or for precision "although it does relate to both these concepts"; therefore **a quoted "accuracy" figure on a specification sheet is not what the standard means by accuracy**, and the reportable quantity is not the one that matters
- Definition status: **provisional** — proposed `decisions/0010` clauses 3.2, 3.3; source-verified against `jcgm2012vim` §2.13

## measurand

- Preferred term: measurand
- Field/origin: metrology (VIM §2.3)
- Introduced in: Chapter 3, **signposted only** — not reader-facing working vocabulary
- Distinct from: construct; working definition; target; target quantity
- Aliases/cautions: the quantity **intended** to be measured, with the VIM warning that the quantity actually measured can differ from it — structurally the same gap as working definition versus measure, arrived at independently; **the vocabularies do not translate cleanly**: a measurand is a *quantity*, whereas a working definition need not be quantitative at all; Chapter 1's note already forbids using `measurand` as a general synonym for the book's `target`
- Definition status: **provisional** — proposed `decisions/0010` clause 6.2; source-verified against `jcgm2012vim` §2.3

## calibration

- Preferred term: calibration
- Field/origin: metrology
- Introduced in: Chapter 3 at recognition depth only
- Distinct from: validation; validity; verification; probability calibration (Chapter 6)
- Aliases/cautions: taught only far enough to explain how a systematic offset is found, and to establish that **calibrating an instrument against a standard does not establish that the quantity it measures is the quantity you want**; traceability chains and calibration hierarchies are depth-curriculum material; **not** to be confused with the Chapter 6 sense of calibration for probabilistic forecasts, which is a different concept sharing the word
- Definition status: **provisional** — proposed `decisions/0010` clause 3.9

---

## Chapter 4 block — PROVISIONAL

The seven entries below were introduced by **proposed** `decisions/0011-chapter4-observation-process-terminology-and-boundary.md`, which has **not** been author-adjudicated. The existing `aggregation` entry already carries the Chapter 2 / Chapter 4 split and is not re-registered.

## observation process

- Preferred term: observation process
- Field/origin: statistics and survey methodology; the term is fixed by this chapter's governed title
- Introduced in: Chapter 4
- Distinct from: the process being modelled; measurement (Chapter 3); the representation (Chapter 2); monitoring (Chapter 17)
- Aliases/cautions: **the process that decides which things get written down**, which is a different system from the one being studied and has its own actors, purposes, and failure modes; the key idea is that **being recorded is something that happens to a unit and can depend on the unit's value** — `meng2018paradox` p. 685 formalizes exactly this, decomposing error using "the correlation between X_j and the response/recording indicator R_j"; five stages are taught — eligibility, coverage, capture, retention, reporting — of which only eligibility and capture are sourced, so **the five-stage enumeration is the book's own pedagogical device**; do not describe the recording indicator itself as the observation process, since the indicator is per unit and the process is what generates it
- Definition status: **provisional** — proposed `decisions/0011` §1–2; core claim source-verified against `meng2018paradox` p. 685

## record

- Preferred term: record
- Field/origin: ordinary and administrative usage; no inspected source defines it as a term of art
- Introduced in: Chapter 4
- Distinct from: the thing recorded; the score (Chapter 3); the measure; data as an undifferentiated mass
- Aliases/cautions: a record exists because something caused it to exist, and that cause is **not** the phenomenon it describes; `provenance` — the history of how a record came to exist, who produced it, for what purpose, under what requirement — is used as ordinary careful language and is **not** registered, because no inspected source defines it; provenance is not a metadata field
- Definition status: **provisional** — proposed `decisions/0011` clauses 2.1–2.2; **unsourced**, taught by demonstration

## selection

- Preferred term: selection
- Field/origin: statistics; survey methodology; econometrics
- Introduced in: Chapter 4; identification consequences are Chapter 7; correction methods are Chapter 8
- Distinct from: sampling; random error; measurement error (Chapter 3); the selection of alternatives (Chapter 10)
- Aliases/cautions: selection is **not one event at a sampling stage** — it operates at every stage of the observation process, so a dataset with no sampling design still has selection; what matters is not how many units were selected but **whether being selected is related to the value**; a designed random sample is valuable precisely because it *arranges* for that relation to be absent (`meng2018paradox` p. 685, insight I); **more records do not fix a selection problem** — without that arrangement, error grows with the population size rather than shrinking with the number collected (insight II; p. 687)
- Definition status: **provisional** — proposed `decisions/0011` §3; source-verified against `meng2018paradox` pp. 685, 687

## coverage

- Preferred term: coverage
- Field/origin: survey methodology and official statistics
- Introduced in: Chapter 4
- Distinct from: response rate; sample size; representativeness; completeness
- Aliases/cautions: **complete is not representative** — covering most or all of a population does not control whether being recorded is related to the value; `meng2018paradox` p. 685 insight (III) holds that the "bigness" of a dataset for population inferences "should be measured by the *relative size* f = n/N, not the *absolute size* n"; a dataset with no gaps can still be badly wrong for a given quantity; do not treat a coverage figure as evidence of trustworthiness
- Definition status: **provisional** — proposed `decisions/0011` clauses 3.1, 3.5; source-verified against `meng2018paradox` p. 685

## nonresponse

- Preferred term: nonresponse
- Field/origin: survey methodology
- Introduced in: Chapter 4
- Distinct from: missingness generally; coverage; refusal as a motive; attrition
- Aliases/cautions: **the response rate is a poor indicator of bias** — "Response rates lack validity in that there is not even a moderate correlation with nonresponse bias" (`davern2013nonresponse`); this does **not** mean nonresponse is harmless, only that the rate does not measure the damage; bias attaches to a **quantity being estimated, not to a dataset** — it "is an estimate level measure and it cannot be easily summarized by a survey level proxy measure" (same source), which is the same move Chapter 1 made about adequacy and Chapter 3 about validity; the survey-methodology framing does not automatically cover administrative or operational records
- Definition status: **provisional** — proposed `decisions/0011` clauses 3.5–3.6; source-verified against `davern2013nonresponse`

## missingness

- Preferred term: missingness
- Field/origin: statistics
- Introduced in: Chapter 4 as a question to ask; methods are Chapter 8
- Distinct from: censoring; absence of a unit from the dataset entirely; zero; not applicable
- Aliases/cautions: the reader is taught **the question, not the taxonomy** — *is whatever caused this to be absent related to what it would have been?*; three plain-language cases are given (unrelated to the value; related to something else recorded; **related to the value itself**, which is the dangerous one because nothing in the data reveals it); whether the missingness process may be ignored **depends on why the data are missing**, and the conditions are restrictive (`rubin1976missing`, published summary); **MCAR / MAR / MNAR must not be attributed to `rubin1976missing`** — its verified summary uses *missing at random* and *observed at random* and does not contain the three-way scheme, which was consolidated later; a pattern of missingness is visible in the data but its cause is not; deleting rows with gaps is an assumption about the observation process, not a tidying step
- Definition status: **provisional** — proposed `decisions/0011` §4; `rubin1976missing` is **abstract-verified only**, no internal locator citable

## censoring

- Preferred term: censoring
- Field/origin: statistics; survival analysis owns the formal treatment
- Introduced in: Chapter 4 at recognition depth; formal treatment is depth curriculum
- Distinct from: missingness; truncation; rounding; saturation treated as a valid reading
- Aliases/cautions: a **censored** observation carries partial information — you know the value lies beyond a bound, because the recording process stopped there — whereas a **missing** one carries none; a logger that saturates at its maximum has not lost the reading, it has told you the value was at least the maximum; treating a censored value as missing discards real information and treating it as the bound understates the value, and **both errors run in known directions**; censoring is often disguised as an ordinary value and is detectable only if the bound is documented or a pile-up at a limit is noticed; **no inspected source defines this distinction**, so Chapter 4 teaches it by worked arithmetic demonstration and cites nothing for it
- Definition status: **provisional and unsourced** — proposed `decisions/0011` clause 4.4; taught by demonstration

---

## Chapter 5 block — PROVISIONAL

The five entries below were introduced by **proposed** `decisions/0012-chapter5-criticism-terminology-and-boundary.md`, which has **not** been author-adjudicated. The existing `adequacy` and `validation` entries were also updated from the same decision and carry the same provisional status.

## verification

- Preferred term: verification
- Field/origin: computational modelling and simulation VVUQ
- Introduced in: Chapter 5
- Distinct from: validation; validity (Chapter 3); calibration; credibility; adequacy
- Aliases/cautions: the reader-facing pair is **verification asks whether you did the thing right; validation asks whether you did the right thing**; `asme2025credibility` slides 5–7 distinguishes numerical verification, model validation, uncertainty quantification, and broader credibility assessment, and the four must not be merged; a perfectly verified computation of the wrong model is wrong, which is why the pair is taught together; Chapter 1 was permitted to refer only to `aspects of numerical verification` and deferred the rest here
- Definition status: **provisional** — proposed `decisions/0012` clause 2.1; source-verified against `asme2025credibility` slides 5–7

## assumption record

- Preferred term: assumption record
- Field/origin: modelling practice; named in this chapter's governed core competence
- Introduced in: Chapter 5
- Distinct from: a list of caveats; a limitations section; sensitivity analysis
- Aliases/cautions: **naming an assumption does not handle it** — an assumption record is a starting point, not a discharge; the useful form pairs each assumption with what would show it false, following the template recorded at `platt1964strong` p. 348 from Jacob and Monod (*our conclusion might be invalid if (i), (ii), or (iii); here is what would eliminate each*); a record whose entries carry no discriminating observation is a list of worries
- Definition status: **provisional** — proposed `decisions/0012` clause 3.4; the template is source-verified, the practice is the book's own framing

## rival model

- Preferred term: rival model
- Field/origin: modelling practice; philosophy of science
- Introduced in: Chapter 5 as an instrument of criticism; which rival is true is Chapter 7
- Distinct from: alternative representation (Chapter 2, for construction and perspective); competing causal hypotheses to be identified between (Chapter 7); alternatives in the decision sense (Chapter 10)
- Aliases/cautions: rival models are **instruments of criticism, not options to choose between**; **leaving both alive is a legitimate outcome** — Chapter 2's Mechanism A and Mechanism B remain unresolved after three chapters and Chapter 5 says so; a conclusion surviving across differently simplified representations is more trustworthy (`levins1966strategy` p. 423, robust theorems), but formal robustness, regret, and adaptive planning are Chapter 12, where `robustness` is registered
- Definition status: **provisional** — proposed `decisions/0012` §5

## structural uncertainty

- Preferred term: structural uncertainty
- Field/origin: modelling and simulation; uncertainty quantification
- Introduced in: Chapter 5 at recognition depth; quantification is Chapter 8
- Distinct from: parameter uncertainty; measurement uncertainty (Chapter 8); **structural identifiability** (Chapter 14 — different concept, shared word); sampling variability
- Aliases/cautions: **being unsure of a number is not being unsure of the form**; structural uncertainty is uncertainty about whether the formulation itself is right, and it is the kind that sensitivity analysis cannot see, because sensitivity analysis varies inputs *inside* a formulation; the collision with `structural identifiability` must be flagged wherever both could be read; do not teach quantification, propagation, or model-averaging
- Definition status: **provisional** — proposed `decisions/0012` §5

## failure mode

- Preferred term: failure mode
- Field/origin: engineering and reliability practice; named in this chapter's governed core competence
- Introduced in: Chapter 5
- Distinct from: a risk; an error that has occurred; a limitation; a caveat
- Aliases/cautions: a **specific predicted way this formulation would fail its purpose**, paired with the observation that would show it; **a predicted failure mode is not a prevented one** — prediction is the cheap half; how many failure modes it is worth working through is governed by what happens if the model is wrong, not by a fixed standard; detecting failures after deployment is Chapter 17
- Definition status: **provisional** — proposed `decisions/0012` clauses 1.3, 3.1
