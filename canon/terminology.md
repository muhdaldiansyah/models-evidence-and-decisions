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

131 entries, in registry order. Navigation only — the entries below are the record.

**Adjudicated (29).** Note that `construct`, `measure`, and `proxy` appear in this sequence but were filled in from proposed Decision 0010 and are provisional; see the Chapter 3 block. Six further entries in this sequence — `statistical identifiability`, `causal identification`, `target`, `estimand`, `intervention`, and `counterfactual` — were closed or specialised from proposed Decision 0014 and are provisional; see the Chapter 7 block. `estimator` and `estimate` were closed from proposed Decision 0015; see the Chapter 8 block. `target population` was closed from proposed Decision 0016; see the Chapter 9 block. `objective` and `metric` were closed from proposed Decision 0017; see the Chapter 10 block. [intended use](#intended-use) · [context of use](#context-of-use) · [adequacy](#adequacy) · [positive](#positive) · [normative](#normative) · [decision](#decision) · [decision-maker](#decision-maker) · [alternative](#alternative) · [consequence](#consequence) · [statistical identifiability](#statistical-identifiability) · [causal identification](#causal-identification) · [structural identifiability](#structural-identifiability) · [construct](#construct) · [measure](#measure) · [proxy](#proxy) · [target](#target) · [target population](#target-population) · [estimand](#estimand) · [estimator](#estimator) · [estimate](#estimate) · [association](#association) · [prediction](#prediction) · [intervention](#intervention) · [counterfactual](#counterfactual) · [utility](#utility) · [objective](#objective) · [metric](#metric) · [robustness](#robustness) · [feedback](#feedback) · [stability](#stability) · [equilibrium](#equilibrium) · [observability](#observability)

**Provisional — Chapter 2 block (9), pending adjudication of [Decision 0009](../decisions/0009-chapter2-representation-terminology-and-boundary.md).** [representation](#representation) · [target system](#target-system) · [boundary](#boundary) · [mechanism](#mechanism) · [abstraction](#abstraction) · [idealization](#idealization) · [generality](#generality) · [aggregation](#aggregation) · [state](#state)

**Provisional — Chapter 3 block (12), pending adjudication of [Decision 0010](../decisions/0010-chapter3-measurement-terminology-and-boundary.md).** [working definition](#working-definition) · [operationalization](#operationalization) · [score](#score) · [validity](#validity) · [validation](#validation) · [reliability](#reliability) · [measurement error](#measurement-error) · [precision](#precision) · [trueness](#trueness) · [accuracy](#accuracy) · [measurand](#measurand) · [calibration](#calibration) — plus [construct](#construct), [measure](#measure), and [proxy](#proxy), filled in from the same decision in their existing positions above.

**Provisional — Chapter 4 block (7), pending adjudication of [Decision 0011](../decisions/0011-chapter4-observation-process-terminology-and-boundary.md).** [observation process](#observation-process) · [record](#record) · [selection](#selection) · [coverage](#coverage) · [nonresponse](#nonresponse) · [missingness](#missingness) · [censoring](#censoring)

**Provisional — Chapter 5 block (5), pending adjudication of [Decision 0012](../decisions/0012-chapter5-criticism-terminology-and-boundary.md).** [verification](#verification) · [assumption record](#assumption-record) · [rival model](#rival-model) · [structural uncertainty](#structural-uncertainty) · [failure mode](#failure-mode) — plus [adequacy](#adequacy) and [validation](#validation), updated from the same decision in their existing positions above.

**Provisional — Chapter 6 block (8), pending adjudication of [Decision 0013](../decisions/0013-chapter6-probability-terminology-and-notation.md).** [probability](#probability) · [conditional probability](#conditional-probability) · [prior](#prior) · [posterior](#posterior) · [base rate](#base-rate) · [expectation](#expectation) · [sharpness](#sharpness) · [scoring rule](#scoring-rule) — plus [calibration](#calibration), updated from the same decision in its existing position above. Decision 0013 clause 2 also takes a **bounded exception to the book's no-notation policy**, permitting `P(A | B)` and odds notation and nothing else.

**Provisional — Chapter 7 block (7), pending adjudication of [Decision 0014](../decisions/0014-chapter7-identification-terminology-and-notation.md).** [target quantity](#target-quantity) · [identifying assumption](#identifying-assumption) · [exchangeability](#exchangeability) · [positivity](#positivity) · [consistency](#consistency) · [target trial](#target-trial) · [confounding](#confounding) — plus [statistical identifiability](#statistical-identifiability) and [causal identification](#causal-identification), **closed from `TODO`** by the same decision, and [estimand](#estimand), [intervention](#intervention), and [counterfactual](#counterfactual), specialised from their Chapter 1 previews, all in their existing positions above. Decision 0014 clause 2 takes a **second bounded notation exception**, extending Decision 0013's with `do(·)` inside the conditioning bar and inline arrows for causal structure.

**Provisional — Chapter 8 block (7), pending adjudication of [Decision 0015](../decisions/0015-chapter8-estimation-terminology-and-notation.md).** [sampling variability](#sampling-variability) · [standard error](#standard-error) · [interval estimate](#interval-estimate) · [P value](#p-value) · [statistical significance](#statistical-significance) · [analytic flexibility](#analytic-flexibility) · [model checking](#model-checking) — plus [estimator](#estimator) and [estimate](#estimate), **closed from `TODO`** by the same decision in their existing positions above. Decision 0015 clause 2 **declines** to extend the notation exception, departing from a promise Chapter 6 made to the reader; it is the first notation clause in the book that refuses rather than permits.

**Provisional — Chapter 9 block (8), pending adjudication of [Decision 0016](../decisions/0016-chapter9-synthesis-terminology-and-boundary.md).** [evidence synthesis](#evidence-synthesis) · [heterogeneity](#heterogeneity) · [dependence](#dependence) · [replication](#replication) · [external validity](#external-validity) · [transportability](#transportability) · [support factor](#support-factor) · [expert judgment](#expert-judgment) — plus [target population](#target-population), **closed** by the same decision in its existing position above. Decision 0016 clause 2 teaches **no synthesis method**; clause 6 records a **fourth** instance of the demonstrate-because-unsourced disposition and refers it to the author rather than invoking precedent.

**Provisional — Chapter 10 block (6), pending adjudication of [Decision 0017](../decisions/0017-chapter10-values-terminology-and-boundary.md).** [value](#value) · [fundamental objective](#fundamental-objective) · [means objective](#means-objective) · [attribute](#attribute) · [stakeholder](#stakeholder) · [constraint](#constraint) — plus [objective](#objective) and [metric](#metric), **closed from `TODO`** by the same decision in their existing positions above. Decision 0017 clause 1 records that `keeney1996valuefocused` could not be obtained in full and that the framework is used **as reported at** `bradley2016structured`. Clause 5 **resolves a conflict** between `decisions/0006` and `README.md` over where trade-offs live, in favour of `README.md`.

**Provisional — Chapter 11 block (8), pending adjudication of [Decision 0018](../decisions/0018-chapter11-decision-terminology-and-boundary.md).** [decision tree](#decision-tree) · [expected value](#expected-value) · [risk attitude](#risk-attitude) · [sensitivity analysis](#sensitivity-analysis) · [value of information](#value-of-information) · [value of perfect information](#value-of-perfect-information) · [ambiguity](#ambiguity) · [decision quality](#decision-quality) — plus [consequence](#consequence), **specialised** by the same decision in its existing position above. Clause 2 takes a **third bounded notation extension** (a decision table and one inline tree); **clause 4.4 records the closest the book has come to a fifth instance of the demonstrate-because-unsourced disposition and states why it is not one.**

**Provisional — Chapter 12 block (10), pending adjudication of [Decision 0019](../decisions/0019-chapter12-optimization-terminology-and-boundary.md).** [feasible region](#feasible-region) · [marginal benefit](#marginal-benefit) · [marginal cost](#marginal-cost) · [shadow price](#shadow-price) · [convexity](#convexity) · [local optimum](#local-optimum) · [scenario](#scenario) · [regret](#regret) · [adaptive plan](#adaptive-plan) · [signpost](#signpost) — plus [robustness](#robustness), **closed from `TODO`** by the same decision in its existing position above, where Decision 0012 clause 5.4 reserved it. Clause 1 records that **nothing in this chapter is taught unsourced** and that the demonstrate-because-unsourced count **stays at four**.

**Provisional — Chapter 13 block (12), pending adjudication of [Decision 0020](../decisions/0020-chapter13-dynamics-terminology-and-boundary.md).** [stock](#stock) · [flow](#flow) · [accumulation](#accumulation) · [delay](#delay) · [open loop](#open-loop) · [closed loop](#closed-loop) · [reinforcing feedback](#reinforcing-feedback) · [balancing feedback](#balancing-feedback) · [oscillation](#oscillation) · [overshoot](#overshoot) · [policy resistance](#policy-resistance) · [state space](#state-space) — plus [equilibrium](#equilibrium) and [stability](#stability), **both closed from `TODO`** by the same decision in their existing positions above, where they had stood open since Chapter 1, and [feedback](#feedback), developed there from Chapter 1's screening depth to its formal home. Chapter 13's scope was set in advance by **Accepted** [Decision 0007](../decisions/0007-chapter1-dynamics-and-response-boundary.md); clauses 1.3, 3, 5, and 8 are the ones that go beyond it. **After this chapter three `TODO` entries remain** — `observability` and `structural identifiability`, both Chapter 14's, and **`utility`, which the registry assigns to the already-drafted Chapter 11 and which Chapter 11 did not close**. See Decision 0020 clause 12.4.

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
- Aliases/cautions: an outcome, effect, burden, benefit, cost, risk, or other material result that may occur under an alternative for a relevant stakeholder or system; evidence may inform beliefs about consequences, but the evaluation of those consequences requires values, requirements, or other decision premises; one analytical target rarely exhausts all decision-relevant consequences; **Chapter 11 adds that consequences are stated per act and per state** — the third column of a decision layout — and that reducing several of Chapter 10's objectives to one number per cell is a **value judgment, not a measurement**, since value-of-information machinery "typically do require a single currency for the relevant values" (`colyvan2016voi` p. 305)
- Definition status: **specialised** by proposed `decisions/0018` clause 8.3; the single-currency limitation source-verified against `colyvan2016voi` p. 305

## statistical identifiability

- Preferred term: statistical identifiability
- Field/origin: statistics
- Introduced in: Chapter 7
- Distinct from: causal identification; structural identifiability; estimation
- Aliases/cautions: whether the parameters of a model are pinned down by the distribution that model implies — two parameter settings implying the same distribution are indistinguishable by **any** amount of data; often just "identifiability" in statistics texts, and **always qualified in this book**; `pearl2009causal` p. 109 introduces a separate definition for causal quantities precisely because the classical notion of "has a unique solution" "does not directly apply" to them, which is the cleanest available evidence that the two senses are distinct; **this is settled before data collection**, not diagnosed from a dataset
- Definition status: **provisional** — closed by proposed `decisions/0014` clause 4.1; source-verified against `pearl2009causal` p. 109

## causal identification

- Preferred term: causal identification
- Field/origin: causal inference / econometrics
- Introduced in: Chapter 7
- Distinct from: statistical identifiability; structural identifiability; estimation; confounding
- Aliases/cautions: whether a causal quantity is pinned down by the observable distribution **together with causal assumptions that are not in the distribution**; two published definitions from different traditions agree — a quantity is identified when the assumptions constrain models so that "equality of P's would entail equality of Q's" (`pearl2009causal` p. 109) and an effect is identifiable when the assumptions "imply that the distribution of the observed data is compatible with a single value of the effect measure" (`hernan2019whatif` p. 27); **never usable unqualified** — unqualified "identification" in econometrics usually means this sense and in statistics usually means the other; **always relative to stated assumptions**, since "we need an assumption external to the data, an identifying assumption" (`hernan2019whatif` p. 27); **not identified is a result, not a failure** — `pearl2009causal` p. 122 step 4 includes approximating a non-identified quantity
- Definition status: **provisional** — closed by proposed `decisions/0014` clause 4; source-verified against `pearl2009causal` p. 109 and `hernan2019whatif` p. 27

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
- Aliases/cautions: established qualified term for population-based questions; use only when inference or generalization concerns a population; do not force onto one-off physical-system problems; **the target population is the one the decision is about, which is routinely not the one any source studied** — `bareinboim2016fusion` p. 7350 records that "we cannot guarantee that the study population would be the same as the population of interest"; distinguish it from the **study population** (whom a source actually observed) and the **source population** (whom that study's sampling drew from), and state which you mean whenever they differ; naming it is Chapter 7's second estimand attribute and is the first thing to check before combining sources
- Definition status: **closed** by proposed `decisions/0016` clause 9.2; source-verified against `bareinboim2016fusion` p. 7350 and `deaton2016rct` p. 27

## estimand

- Preferred term: estimand
- Field/origin: statistics / causal inference / clinical-trial methodology
- Introduced in: Chapter 1 as a concept preview only; formal home Chapter 7
- Distinct from: target; endpoint; estimator; estimate
- Aliases/cautions: the **specified** target of estimation — a target quantity with its attributes filled in; Chapter 1 does not require the term; `fda2021estimands` pp. 9–10 lists five attributes for a clinical-trial estimand (treatment, population, variable, handling of intercurrent events, and a population-level summary), and that list **must not be presented as the book's universal cross-disciplinary definition** — Chapter 7 generalises its *shape* and labels the generalisation as pedagogical synthesis; the same source warns that a definition must identify "an effect because of treatment and not because of potential confounders such as differences in duration of observation or patient characteristics" (p. 10); sits between `target quantity` (general) and `estimator`/`estimate` (Chapter 8) and must never be blurred into either
- Definition status: **provisional** — specialised by proposed `decisions/0014` clauses 8.4–8.5; clinical-trial attribute list source-verified against `fda2021estimands` pp. 9–10

## estimator

- Preferred term: estimator
- Field/origin: statistics
- Introduced in: Chapter 8
- Distinct from: estimand; estimate; model; algorithm
- Aliases/cautions: the **procedure** applied to data to produce a number — *how* you work it out, as against `estimand` (*what you want to know*) and `estimate` (*what you got*); its properties — **bias**, **variance**, **consistency** — are properties of the **procedure over repeated application**, never of any number it produced, which makes "this is an unbiased estimate" a category error; **`consistency` here is unrelated to the causal condition of the same name (Chapter 7)**, and the book announces the collision rather than avoiding it; no estimator is derived in this book and no estimator notation is used, per proposed `decisions/0015` clause 2
- Definition status: **provisional** — closed by proposed `decisions/0015` clause 3; concept-depth separation follows `fda2021estimands`, already verified for Chapters 1 and 7

## estimate

- Preferred term: estimate
- Field/origin: statistics
- Introduced in: Chapter 8
- Distinct from: estimand; estimator; the true value; a forecast (Chapter 6)
- Aliases/cautions: the **number** an estimator produced on the data you actually have; carries none of the estimator's properties — a single estimate is neither biased nor unbiased, in the same way a single reading from a calibrated instrument is not thereby correct (Chapter 3); **every estimate is conditional on an entire model**, including assumptions about how the analysis was conducted (`greenland2016misinterpretations` p. 339), so reporting one without its conditioning repeats the defect Chapter 6 named for probabilities; reporting more decimal places does not add information, which is Chapter 3's resolution-is-not-trueness point in a new setting
- Definition status: **provisional** — closed by proposed `decisions/0015` clause 3; source-verified against `greenland2016misinterpretations` p. 339

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
- Aliases/cautions: at Chapter 1 depth asks what would happen under an action or externally changed condition; state the action and comparison condition when material; association alone is insufficient for an intervention-effect claim, although observational evidence may contribute under additional causal assumptions and identification conditions; **Chapter 7 requires the intervention to be well defined** — where several different actions would all count as "the intervention" and could have different effects, the causal effect "will be ill-defined" (`hernan2019whatif` p. 33), which is condition 1 of the three identifiability conditions; **observing that an action was taken is not the same as imposing it**, and Chapter 7 marks the difference with `do(·)` inside the conditioning bar per proposed `decisions/0014` clause 2; the Chapter 15 sense — an action that provokes strategic response — is compatible but has a different emphasis
- Definition status: **provisional** — specialised by proposed `decisions/0014`; source-verified against `pearl2009causal` pp. 99–101 and `hernan2019whatif` pp. 26, 33

## counterfactual

- Preferred term: counterfactual
- Field/origin: causal inference / philosophy / economics
- Introduced in: Chapter 1 as an intuitive preview; formal home Chapter 7
- Distinct from: generic hypothetical scenario; ordinary association; forecast
- Aliases/cautions: at Chapter 1 depth asks about an alternative outcome under a different action or condition while retaining relevant factual or background information about the case; do not use `counterfactual` as a loose synonym for any hypothetical scenario; do not present intervention and counterfactual as mutually exclusive formal categories because causal frameworks relate them closely; **Chapter 7 adds that the counterfactual question is harder than the intervention question**, because it concerns a case whose actual outcome is already known, and `pearl2009causal` p. 121 records that "attributional queries are generally not identifiable in nonparametric models" — the practical consequence being that the *did this cause that* question managers most often ask is frequently the one no available evidence can settle; potential-outcome notation is **not** used in this book, per proposed `decisions/0014` clause 2.3
- Definition status: **provisional** — specialised by proposed `decisions/0014`; source-verified against `pearl2009causal` p. 121

## utility

- Preferred term: utility
- Field/origin: decision theory
- Introduced in: Chapter 11
- Distinct from: objective; metric
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

## objective

- Preferred term: objective
- Field/origin: decision analysis
- Introduced in: Chapter 10
- Distinct from: value; attribute; metric; utility (Chapter 11); target (Chapter 1); estimand (Chapter 7); a vision statement; a policy; a target figure
- Aliases/cautions: **an objective has an item of value and a direction of preference** — "Objectives are usually described as something that matters … and a verb indicating the preferred direction of change (e.g., maximize or minimize)" (`bradley2016structured` p. 50, reporting Keeney and others); that two-part format is a **test**, and *improve service resilience* fails both halves; objectives "become the evaluation criteria for identifying and evaluating alternatives" (p. 49), so a decision with no usable objectives has criteria supplied by whoever framed the options; **"Objectives are context specific: they are defined for the decision at hand, not for universal usage"** (p. 50), which is the book's recurring relativity shape in Part III; the documented failure is that what decision-makers have is "a messy mix of means and ends, targets, policies and vision statements, most of which are not useful for decision-making" (p. 49)
- Definition status: **provisional** — closed by proposed `decisions/0017` clause 3.1; source-verified against `bradley2016structured` pp. 49–50

## metric

- Preferred term: metric
- Field/origin: management practice / decision analysis; the decision-analytic term for the same role is `attribute`
- Introduced in: Chapter 10
- Distinct from: objective; value; attribute (the decision-analytic term this book prefers); measure (Chapter 3, the measurement procedure); score (Chapter 3)
- Aliases/cautions: the quantity actually tracked as a stand-in for an objective; **a metric is not an objective**, in the same way a `measure` is not a `construct` (Chapter 3) — choosing what to count does not fix what is valued, and the gap between them is where the failures live; effective attributes are "characterized by their measurability, understandability, and operability" (`bradley2016structured` p. 51); **metric gaming and Goodhart-type failures are treated in Chapter 15**, and Chapter 10 introduces the stand-in relationship that makes them possible without treating the failure
- Definition status: **provisional** — closed by proposed `decisions/0017` clause 3.5; source-verified against `bradley2016structured` p. 51

## robustness

- Preferred term: robustness
- Field/origin: decision analysis / policy analysis
- Introduced in: Chapter 12; reserved there by proposed `decisions/0012` clause 5.4 since Chapter 5
- Distinct from: stability (Chapter 13); reliability (Chapter 3); optimality; insensitivity to a single input; robust statistics, which is a different concept sharing the word; transportability (Chapter 9)
- Aliases/cautions: **"a strategy should be considered robust if it performs reasonably well compared to the alternatives across a wide range of plausible futures"** (`lempert2003shaping` p. 52); the criterion **replaces** optimality when the model is in doubt, since traditional decision analysis "seeks the optimal strategy, that is, the one that performs best for a fixed set of assumptions about the future" (p. 52); **assessed across value systems as well as futures** (pp. 52–53), which is why robustness does not require the single currency that value-of-information machinery does (`colyvan2016voi` p. 305) — Chapter 10's plural objectives survive here instead of being flattened as they were in Chapter 11; **a robust strategy is typically optimal in no future**, which is the point and not a defect; robustness is **not free** — it costs performance in whichever future actually arrives; the closing requirement is to be "explicitly aware of the futures and values that, by virtue of selecting the candidate strategy, have been implicitly classed as unimportant" (p. 57)
- Definition status: **provisional** — closed by proposed `decisions/0019` clause 5.2; source-verified against `lempert2003shaping` pp. 52–53, 57

## feedback

- Preferred term: feedback
- Field/origin: dynamical systems / control / system dynamics
- Introduced in: Chapter 1 as an intuitive environment screen; formal home Chapter 13 with engineered-control specialization in Chapter 14
- Distinct from: ordinary evaluative or reviewer feedback; delay; accumulation; adaptive response; strategic response; stability
- Aliases/cautions: at Chapter 1 depth, use `feedback` when consequences of a process or action return through the system and influence later behavior, outcomes, information, or actions; do not teach `positive feedback` or `negative feedback`, loop polarity, controller design, or stability analysis there; feedback does not by itself imply adaptation or strategic behavior; **at Chapter 13 depth**, feedback is the situation in which two or more dynamical systems "are connected together such that each system influences the other and their dynamics are thus strongly coupled" (`astrom2008feedback` p. 1), with the consequence that "simple causal reasoning about a feedback system is difficult... leading to a circular argument" (same page); the principle of feedback is to "base correcting actions on the difference between desired and actual performance" (`astrom2008feedback` p. 17); **feedback is reactive — "there must be an error before corrective actions are taken"** (`astrom2008feedback` p. 22)
- Definition status: verified — `astrom2008feedback` pp. 1, 17, 22; formal home reached at Chapter 13, engineered-control specialization remains Chapter 14

## stability

- Preferred term: stability
- Field/origin: dynamical systems
- Introduced in: Chapter 13
- Distinct from: equilibrium; robustness (Chapter 12); reliability (Chapter 3); a system simply not changing
- Aliases/cautions: **stability is a property of the solutions near a point, not of the point** — "the stability of a solution determines whether or not solutions nearby the solution remain close, get closer or move further away" (`astrom2008feedback` p. 102); three grades are taught in words — **unstable**, **neutrally stable** (nearby solutions stay near but need not converge), and **asymptotically stable** (nearby solutions converge); a system that is stable is not thereby in a good state, and the water case's do-nothing equilibrium is stable below the utility's own critical level; **no Lyapunov function, no eigenvalues, no linearization**; the source's formal definitions carry symbols and comparison operators and are paraphrased rather than quoted
- Definition status: verified — `astrom2008feedback` pp. 102–104 (closed from `TODO` by proposed `../decisions/0020` clause 7)

## equilibrium

- Preferred term: equilibrium
- Field/origin: dynamical systems; game theory
- Introduced in: Chapter 13 (dynamic sense); Chapter 15 (strategic sense, "equilibrium as consistency")
- Distinct from: stability; a good state; a state the system will reach; a state the system will return to
- Aliases/cautions: **"an equilibrium point of a dynamical system represents a stationary condition for the dynamics"** (`astrom2008feedback` p. 100), and "a dynamical system can have zero, one or more equilibrium points" (same page); **equilibrium is a property of a point and stability is a property of the solutions near it** — the two must never be collapsed, and the inverted pendulum's upright position is the standing counterexample; the dynamic and strategic senses must not be conflated
- Definition status: verified — `astrom2008feedback` p. 100 (closed from `TODO` by proposed `../decisions/0020` clause 7)

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
- Introduced in: Chapter 3 at recognition depth only (instrument sense); **taken up in Chapter 6** in the forecast sense
- Distinct from: validation; validity; verification; sharpness; accuracy
- Aliases/cautions: in the **Chapter 3 instrument sense**, taught only far enough to explain how a systematic offset is found, and to establish that **calibrating an instrument against a standard does not establish that the quantity it measures is the quantity you want**; traceability chains and calibration hierarchies are depth-curriculum material. In the **Chapter 6 forecast sense**, calibration "refers to the statistical consistency between the distributional forecasts and the observations, and is a **joint property** of the forecasts and the events or values that materialize" (`gneiting2007scoring` p. 359) — assessed over a record of forecasts *and* outcomes, and therefore **never from a single forecast**. **The two senses are different concepts sharing a word**, and **Chapter 6 must reopen the collision explicitly** rather than adopting the term silently, exactly as Chapter 5 was required to do with `validation`. A calibrated forecaster is not thereby a useful one — see `sharpness`
- Definition status: **provisional** — proposed `decisions/0010` clause 3.9 and `decisions/0013` clauses 5.3, 5.6; Chapter 6 sense source-verified against `gneiting2007scoring` p. 359

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

---

## Chapter 6 block — PROVISIONAL

The eight entries below were introduced by **proposed** `decisions/0013-chapter6-probability-terminology-and-notation.md`, which has **not** been author-adjudicated. The existing `calibration` entry was updated from the same decision and carries the same provisional status.

**Note on notation.** Decision 0013 clause 2 takes a bounded exception to the book's five-chapter no-notation policy, permitting `P(A | B)` and odds written as `3 : 1` and nothing else. That exception is registered here because it governs how several of these entries may be written in the manuscript.

## probability

- Preferred term: probability
- Field/origin: mathematics; the interpretations debate spans philosophy, statistics, and decision theory
- Introduced in: Chapter 6
- Distinct from: frequency alone; certainty; confidence (Chapter 8 owns a technical sense); plausibility as loose speech; odds
- Aliases/cautions: **a probability is not a property of an event — it is a property of an event given stated information**, and stating that information is part of stating the probability; this makes the frequency / degree-of-belief distinction something the book **names once and sets aside** rather than adjudicates, because it needs both readings (a coin has a long-run frequency; a one-off mechanism does not) and the conditioning framing unifies them; the objection that a unique event cannot carry a probability assumes the property belongs to the event, and dissolves once it belongs to your evidential position; **do not present a probability without its conditioning information**
- Definition status: **provisional** — proposed `decisions/0013` §1; mathematics, taught by demonstration

## conditional probability

- Preferred term: conditional probability
- Field/origin: mathematics
- Introduced in: Chapter 6
- Distinct from: filtering a dataset; intervention (Chapter 7); joint probability; the reverse conditional
- Aliases/cautions: conditioning changes **what you are taking as given**, which is a statement about your reference position rather than about a subset of rows; **do not teach conditioning as filtering** — filtering fails for unique events and hides the direction problem; **`P(A | B)` and `P(B | A)` are different quantities** and confusing them is the most consequential single error in the chapter; **conditioning is not intervening** — updating belief about which mechanism operates, given an observation, establishes nothing about what would happen under an intervention (`pearl2009causal`; Chapter 7)
- Definition status: **provisional** — proposed `decisions/0013` clause 1.4; mathematics, taught by demonstration

## prior

- Preferred term: prior
- Field/origin: Bayesian statistics
- Introduced in: Chapter 6
- Distinct from: base rate (a prior is often *set from* a base rate but need not be); assumption; guess; posterior
- Aliases/cautions: the probability held **before** the observation in question, itself conditional on whatever information was already in hand; a prior is not an arbitrary starting point to be apologised for, and where a relevant base rate exists it is usually the right thing to condition on; do not present priors as subjective in a way that implies they are unconstrained
- Definition status: **provisional** — proposed `decisions/0013` §1

## posterior

- Preferred term: posterior
- Field/origin: Bayesian statistics
- Introduced in: Chapter 6
- Distinct from: prior; a decision; a conclusion; certainty
- Aliases/cautions: the probability **after** conditioning on the new observation; obtained in this book by the **odds form** — prior odds × ratio = posterior odds — which is one multiplication and avoids the denominator where readers stall; a posterior stated without the ratio hides whether the evidence did any work; **the ratio is not called a likelihood ratio in reader-facing prose**, since `likelihood` has an estimation sense that Chapter 8 owns
- Definition status: **provisional** — proposed `decisions/0013` §3; mathematics, taught by demonstration

## base rate

- Preferred term: base rate
- Field/origin: statistics; judgment and decision-making research
- Introduced in: Chapter 6
- Distinct from: prior; sample proportion; prevalence in a different population; the observed frequency in your data
- Aliases/cautions: the prior probability or frequency of an outcome in the relevant population; **base-rate neglect is not universal** — `tversky1974judgment` p. 1125 documents that "people respond differently when given no evidence and when given worthless evidence. When no specific evidence is given, prior probabilities are properly utilized; when worthless evidence is given, prior probabilities are ignored"; the trigger for abandoning a base rate is therefore **being handed something that looks like information**, which is a sharper and more useful warning than the generic one; the same source (p. 1124) is explicit that the underlying heuristics "are quite useful", so **do not present intuition as merely broken**
- Definition status: **provisional** — proposed `decisions/0013` §4; source-verified against `tversky1974judgment` pp. 1124–1125

## expectation

- Preferred term: expectation
- Field/origin: mathematics
- Introduced in: Chapter 6 as a **summary of a distribution**; as a decision rule it is Chapter 11
- Distinct from: the most likely outcome; the median; what will happen; expected utility (Chapter 11)
- Aliases/cautions: **the expectation is not what will happen** and may be a value the quantity cannot take; do not slide from *the expected value is X* to *therefore act as if X*, which smuggles in risk neutrality — that move belongs to Chapter 11 and must be made deliberately there; no expectation operator notation
- Definition status: **provisional** — proposed `decisions/0013` clause 7.1; mathematics, taught by demonstration

## sharpness

- Preferred term: sharpness
- Field/origin: forecast verification / statistics
- Introduced in: Chapter 6
- Distinct from: calibration; accuracy; precision (Chapter 3); confidence
- Aliases/cautions: "**Sharpness refers to the concentration of the predictive distributions and is a property of the forecasts only**" (`gneiting2007scoring` p. 359) — assessable before anything happens, unlike calibration; the stated goal is "to maximize the sharpness of the predictive distributions subject to calibration" (p. 359), so **calibration is the constraint and sharpness the objective**, not the reverse; a forecaster who always states the base rate is perfectly calibrated and useless, which is the book's own demonstration of why calibration alone is not the goal
- Definition status: **provisional** — proposed `decisions/0013` clause 5.3; source-verified against `gneiting2007scoring` p. 359

## scoring rule

- Preferred term: scoring rule
- Field/origin: forecast verification / statistics / decision theory
- Introduced in: Chapter 6 at concept depth; the mathematics is depth curriculum
- Distinct from: accuracy metric; loss function in the estimation sense (Chapter 8); a performance target
- Aliases/cautions: a rule assigning a numerical score to a probabilistic forecast given what materialized; the concept that matters is **propriety** — a rule is proper when "the forecaster has no incentive to predict any P ≠ Q and is encouraged to quote his or her true belief" (`gneiting2007scoring` p. 359), so honesty is the score-maximising strategy by construction; invented scoring schemes are frequently "intuitively appealing but improper" (pp. 359–360) and reward distortion; **do not teach which rules are proper**, and do not write the notation; **a single forecast cannot be scored** — one outcome is consistent with any probability strictly between 0 and 1, and an unscored forecast is unfalsifiable in exactly Chapter 5's sense; the idea dates at least to Brier (1950) **as reported at `gneiting2007scoring` p. 360**, a source that was not obtained and may not be cited directly
- Definition status: **provisional** — proposed `decisions/0013` §5; source-verified against `gneiting2007scoring` pp. 359–360

## Chapter 7 block — PROVISIONAL

Seven entries introduced by proposed [Decision 0014](../decisions/0014-chapter7-identification-terminology-and-notation.md), which is **not author-adjudicated**.
The same decision closes `statistical identifiability` and `causal identification` — TODO since Chapter 1 — and specialises `estimand`, `intervention`, and `counterfactual` in their existing positions above.
Clause 2 takes a **second bounded notation exception**, extending Decision 0013's: `do(·)` inside the conditioning bar, and inline arrows for causal structure. Nothing else.

## target quantity

- Preferred term: target quantity
- Field/origin: causal inference; the term is used in this sense at `pearl2009causal` p. 122
- Introduced in: Chapter 7
- Distinct from: target (Chapter 1, informal); estimand (the specified form); estimator; estimate; metric; objective
- Aliases/cautions: the thing a causal inquiry is about, defined **before** any design or data is considered — `pearl2009causal` p. 122 makes "Define" step 1 of four and insists on defining it "before specifying the process of treatment selection, and without making functional form or distributional assumptions"; framework-neutral, so it presupposes neither a population nor a treatment nor a statistical model; sits between `target` and `estimand` in the hierarchy adopted by proposed `decisions/0014` clause 8.4
- Definition status: **provisional** — proposed `decisions/0014` clause 8.1; source-verified against `pearl2009causal` p. 122

## identifying assumption

- Preferred term: identifying assumption
- Field/origin: causal inference / econometrics
- Introduced in: Chapter 7
- Distinct from: modelling assumption; distributional assumption; approximation; the assumption record (Chapter 5)
- Aliases/cautions: an assumption **external to the data** that, added to the observable distribution, pins a causal quantity to a single value — the term is used verbatim at `hernan2019whatif` p. 27: "we need an assumption external to the data, an identifying assumption"; **it cannot be tested against the data it is used to interpret**, which is the whole reason it must be stated: "behind every causal conclusion there must lie some causal assumption that is not testable in observational studies" (`pearl2009causal` p. 99); a Chapter 5 assumption record that lists modelling assumptions but not identifying ones has not recorded the load-bearing ones
- Definition status: **provisional** — proposed `decisions/0014` clause 4.3; source-verified against `hernan2019whatif` p. 27 and `pearl2009causal` p. 99

## exchangeability

- Preferred term: exchangeability
- Field/origin: causal inference / epidemiology
- Introduced in: Chapter 7
- Distinct from: positivity; consistency; representativeness; the exchangeability of Bayesian statistics, which is a different concept sharing the word
- Aliases/cautions: the first of three identifiability conditions — informally, that "the treated and the untreated are exchangeable because the treated, had they remained untreated, would have experienced the same average outcome as the untreated did, and vice versa" (`hernan2019whatif` p. 27); **it fails whenever whatever determined who got treated also bears on the outcome**, which includes the extremely common case of treating the worst cases first; randomization makes it hold by design (`hernan2019whatif` p. 26), which is what randomization is for; **not a property you can check in the data** — checking covariate balance tests something weaker and cannot speak to unmeasured causes
- Definition status: **provisional** — proposed `decisions/0014` clause 5.1; source-verified against `hernan2019whatif` pp. 26–27

## positivity

- Preferred term: positivity
- Field/origin: causal inference / epidemiology
- Introduced in: Chapter 7
- Distinct from: exchangeability; consistency; sample size; coverage (Chapter 4)
- Aliases/cautions: the second identifiability condition — that "there is a probability greater than zero–a positive probability–of being assigned to each of the treatment levels" (`hernan2019whatif` p. 30), conditional on the covariates being adjusted for; **a structural failure, not a small-sample one** — when a kind of unit never receives one of the treatment levels, the data "contain no information" for the comparison (`hernan2019whatif` p. 31, paraphrased) and collecting more of the same data cannot help; **invisible in any summary statistic**, which links it to Chapter 4's lesson that absence produces no rows to notice; the source records that it "is sometimes referred to as the experimental treatment assumption"
- Definition status: **provisional** — proposed `decisions/0014` clause 5.1; source-verified against `hernan2019whatif` pp. 26, 30–31

## consistency

- Preferred term: consistency (causal sense) — **always qualify**
- Field/origin: causal inference / epidemiology
- Introduced in: Chapter 7
- Distinct from: **consistency of an estimator (Chapter 8), which is an unrelated concept sharing the word**; reliability (Chapter 3); coherence
- Aliases/cautions: the third identifiability condition — that the observed outcome under the treatment actually received equals the outcome that would have obtained under that treatment, which requires the treatment values compared to "correspond to well-defined interventions" (`hernan2019whatif` p. 26); **"The apparent simplicity of the consistency condition is deceptive"** (p. 31), because the real work is specifying the intervention precisely enough that it has one effect rather than several — where multiple versions of a treatment exist and could differ in effect, the causal effect "will be ill-defined" (p. 33); **a naming collision the book announces rather than avoids**, handled as `calibration` was in Chapter 6 and `validation` in Chapter 5, since Chapter 8 needs the statistical sense
- Definition status: **provisional** — proposed `decisions/0014` clauses 5.1 and 5.3; source-verified against `hernan2019whatif` pp. 26, 31, 33

## target trial

- Preferred term: target trial
- Field/origin: causal inference / epidemiology
- Introduced in: Chapter 7
- Distinct from: an actual experiment; a thought experiment in the general sense; a simulation (Chapter 6); a rival model (Chapter 5)
- Aliases/cautions: the hypothetical randomized experiment that would answer the causal question, whose protocol is written out in order to discipline an observational analysis — components given as "eligibility criteria, interventions (or treatment strategies), outcome, follow-up, causal contrast, and statistical analysis" (`hernan2019whatif` p. 37); the operative question is "what randomized experiment are you trying to emulate?" (p. 37); **its value does not depend on the trial being feasible** — writing an infeasible protocol still reveals which assumption the observational analysis is carrying, which is the book's own formulation; the source notes that explicit emulation "prevents investigators from conducting an oversimplified analysis" (p. 37)
- Definition status: **provisional** — proposed `decisions/0014` clause 8.1; source-verified against `hernan2019whatif` pp. 37–38

## confounding

- Preferred term: confounding
- Field/origin: causal inference / epidemiology / statistics
- Introduced in: Chapter 7
- Distinct from: correlation; selection (Chapter 4); measurement error (Chapter 3); a list of covariates
- Aliases/cautions: **a causal concept, not an associational one** — `pearl2009causal` p. 100 lists it among concepts that "cannot be defined in term of distribution functions", and argues that any associational definition must fail because it would allow a causal conclusion with no causal assumption; the consequence is blunt: "confounding bias cannot be detected or corrected by statistical methods alone" (p. 100); **controlling for more covariates is not safer** — "the prevailing practice of conditioning on as many pre-treatment measurements as possible should be approached with great caution; some covariates … may actually increase bias if included in the analysis" (p. 117); the graphical back-door criterion (p. 114) settles which sets suffice, and this book states its intuition — back-door paths "carry spurious associations" (p. 114) — **without stating the criterion**, which would require blocking and collision concepts the book does not teach
- Definition status: **provisional** — proposed `decisions/0014` clause 8.1; source-verified against `pearl2009causal` pp. 100, 114, 117

## Chapter 8 block — PROVISIONAL

Seven entries introduced by proposed [Decision 0015](../decisions/0015-chapter8-estimation-terminology-and-notation.md), which is **not author-adjudicated**.
The same decision closes `estimator` and `estimate` — TODO since Chapter 1 — in their existing positions above.
Clause 2 **declines** to extend the notation exception, departing from a promise Chapter 6 made to the reader. It is the first notation clause in the book that refuses rather than permits.

## sampling variability

- Preferred term: sampling variability
- Field/origin: statistics
- Introduced in: Chapter 8
- Distinct from: measurement uncertainty (Chapter 3); structural uncertainty (Chapter 5); Monte Carlo error (Chapter 6); the data-quality term (Chapter 4); model error
- Aliases/cautions: how much a computed quantity would move if you drew another sample of the same size from the same process — **and nothing else**; it is the only component an interval estimate ordinarily covers, which is why an interval looks like a statement about the answer and is a statement about sampling; **it shrinks with more data and the other components do not**, which is the book's recurring shape appearing for the fifth time; `meng2018paradox` p. 687 is the sharpest available statement that what matters for a defective dataset is a term whose expression does not contain the number of records at all
- Definition status: **provisional** — proposed `decisions/0015` clause 8.1; the separation from the other uncertainty components is the book's own and is labelled

## standard error

- Preferred term: standard error
- Field/origin: statistics
- Introduced in: Chapter 8 at concept depth only
- Distinct from: standard deviation; measurement uncertainty; the width of a prediction; precision (Chapter 3)
- Aliases/cautions: a summary of how much an estimate would move between repeated applications of the same procedure to fresh data — **a property of the procedure and the sample size, not of the number reported**; the book states no formula for one, per proposed `decisions/0015` clause 2.3; do not read a small standard error as evidence that the estimate is close to the estimand, since it speaks only to sampling variability and is silent about every other assumption in the model
- Definition status: **provisional** — proposed `decisions/0015` clause 8.1; concept depth, taught by demonstration on the anchor

## interval estimate

- Preferred term: interval estimate — **the book's preferred term over `confidence interval`**
- Field/origin: statistics
- Introduced in: Chapter 8
- Distinct from: a range of plausible values in ordinary speech; a prediction interval; a tolerance; a sensitivity range (Chapter 5)
- Aliases/cautions: `confidence interval` is the term the reader will meet everywhere else and is named once for that reason, but **the book does not use `confidence` alone in the technical sense** — `greenland2016misinterpretations` p. 339 records that the statistical usages of "significance" and "confidence" are "at odds with … ordinary English definitions"; **a reported interval is "a range between two numbers"** (p. 343) and does not have a 95 % chance of containing the true value; intervals share P values' weaknesses because they rest on the same model (p. 340), and reading whether an interval covers zero "force[s] the 0.05-level cutoff on the reader … and in this way [is] as bad as presenting P values as dichotomies" (p. 344); **overlapping intervals do not establish agreement** — the same page gives two overlapping 95 % intervals whose difference tests at P = 0.03
- Definition status: **provisional** — proposed `decisions/0015` clauses 4.2 and 8.4; source-verified against `greenland2016misinterpretations` pp. 339, 340, 343, 344

## P value

- Preferred term: P value
- Field/origin: statistics
- Introduced in: Chapter 8
- Distinct from: the probability a hypothesis is true; the probability the result is due to chance; an effect size; a measure of importance; a posterior (Chapter 6)
- Aliases/cautions: "a statistical summary of the compatibility between the observed data and what we would predict or expect to see if we knew the entire statistical model … were correct" (`greenland2016misinterpretations` p. 339); **it tests the entire model, not the hypothesis of interest** — including "assumptions about the conduct of the analysis, for example that intermediate analysis results were not used to determine which analyses would be presented" (p. 339); a small value "does not tell us which assumption is incorrect" (p. 339), which is Chapter 5's structure in a new setting; **it is not a hypothesis probability** (p. 340, misinterpretation 1), and reading it as one is Chapter 6's inversion again; `asa2016pvalue` principle 2 states the same institutionally
- Definition status: **provisional** — proposed `decisions/0015` clause 5.2; source-verified against `greenland2016misinterpretations` pp. 339–340 and `asa2016pvalue`

## statistical significance

- Preferred term: statistical significance — **registered as a hazard, not as a tool**
- Field/origin: statistics
- Introduced in: Chapter 8
- Distinct from: practical importance; scientific significance; effect size; evidence
- Aliases/cautions: the practice of declaring results "significant" if a P value falls on or below a cut-off and "nonsignificant" otherwise; the source that supplies this book's treatment closes by "singling out the degradation of P values into ''significant'' and ''nonsignificant'' as an especially pernicious statistical practice" (`greenland2016misinterpretations` p. 348); it "is neither necessary nor sufficient for determining the scientific or practical significance of a set of observations", a view "affirmed unanimously by the U.S. Supreme Court" in Matrixx Initiatives v. Siracusano, **as reported at** p. 347 — the judgment itself was not read; `asa2016pvalue` principle 3 says conclusions "should not be based only on whether a p-value passes a specific threshold", and principle 5 that significance "does not measure the size of an effect or the importance of a result"; **the book does not teach any test procedure**
- Definition status: **provisional** — proposed `decisions/0015` clauses 5 and 8.3; source-verified against `greenland2016misinterpretations` pp. 339, 347, 348 and `asa2016pvalue`

## analytic flexibility

- Preferred term: analytic flexibility
- Field/origin: statistics / research methodology
- Introduced in: Chapter 8
- Distinct from: fraud; sensitivity analysis (Chapter 5); model uncertainty; measurement error
- Aliases/cautions: the range of defensible analyses the same records support, each yielding a different answer; **this book treats it as an assumption inside the statistical model, not as a research-ethics topic**, because the model's assumptions include "the conduct of the analysis" (`greenland2016misinterpretations` p. 339) and proper inference "requires full reporting and transparency" (`asa2016pvalue` principle 4); the practitioners producing it are usually not dishonest — every choice is individually defensible, which is what makes the phenomenon hard to see; **preregistration is one device with real limits and is not a solution**; do not characterise the replication literature, which this book has not read
- Definition status: **provisional** — proposed `decisions/0015` clauses 1.4 and 7; source-verified against `greenland2016misinterpretations` p. 339 and `asa2016pvalue` principle 4

## model checking

- Preferred term: model checking
- Field/origin: statistics
- Introduced in: Chapter 8
- Distinct from: verification (Chapter 5); validation (Chapter 5); criticism (Chapter 5); calibration (Chapters 3 and 6); monitoring (Chapter 17)
- Aliases/cautions: examining the assumptions you were **not** interested in — the ones the computed number silently depends on; the source's guideline is that careful interpretation "demands critical examination of the assumptions and conventions used for the statistical analysis—not just the usual statistical assumptions, but also the hidden assumptions about how results were generated and chosen for presentation" (`greenland2016misinterpretations` p. 347); **fitting the data the model was built from is not model checking** — Chapter 5 established that such a check could not have failed; checking against data the model was not fitted to is the honest form, and Chapter 6's calibration-and-sharpness framing applies unchanged; distinct from Chapter 17's post-deployment monitoring, which is the same activity after the model is in use
- Definition status: **provisional** — proposed `decisions/0015` clause 8.1; source-verified against `greenland2016misinterpretations` p. 347

## Chapter 9 block — PROVISIONAL

Eight entries introduced by proposed [Decision 0016](../decisions/0016-chapter9-synthesis-terminology-and-boundary.md), which is **not author-adjudicated**.
The same decision closes `target population`, whose Chapter 1 entry recorded that formal development in Chapters 7 and 9 was outstanding.
Clause 2 teaches **no synthesis method**, on the strength of the governed core competence's phrase "at an appropriate conceptual level". Clause 6 records a **fourth** instance of the demonstrate-because-unsourced disposition and refers it to the author rather than invoking precedent.

## evidence synthesis

- Preferred term: evidence synthesis
- Field/origin: research methodology / evidence-based practice
- Introduced in: Chapter 9 at concept depth only
- Distinct from: averaging; meta-analysis as a technique; triangulation as loose speech; data fusion (the formal problem)
- Aliases/cautions: the activity of working out what several sources jointly support; **this book teaches no method for it**, per proposed `decisions/0016` clause 2, because the chapter's demonstration is that defensible weighting rules disagree and teaching one would teach the rule whose failure is being shown; the prior question is always whether the sources are about the **same quantity**, tested attribute by attribute against Chapter 7's estimand list; the formal version of the problem is named **data fusion** — "piecing together multiple datasets collected under heterogeneous conditions (i.e., different populations, regimes, and sampling methods)" (`bareinboim2016fusion` p. 7345)
- Definition status: **provisional** — proposed `decisions/0016` clause 9.1; framing source-verified against `bareinboim2016fusion` p. 7345

## heterogeneity

- Preferred term: heterogeneity
- Field/origin: meta-analysis / statistics / causal inference
- Introduced in: Chapter 9
- Distinct from: sampling variability (Chapter 8); measurement error (Chapter 3); disagreement caused by analytic flexibility (Chapter 8); noise
- Aliases/cautions: real differences between what sources studied — different populations, different regimes, different sampling methods (`bareinboim2016fusion` p. 7345); **treat it as a finding, not a nuisance to be averaged away** — when two sources differ because the settings differ, the difference is information about which settings matter; do not use the word for disagreement that arises from analytic choices, which is Chapter 8's subject and has a different remedy; the book teaches **no heterogeneity statistic**
- Definition status: **provisional** — proposed `decisions/0016` clause 9.1; source-verified against `bareinboim2016fusion` p. 7345

## dependence

- Preferred term: dependence (between sources) — **always qualify**
- Field/origin: the book's own usage in this sense
- Introduced in: Chapter 9
- Distinct from: statistical dependence between variables; correlation; conditional independence (Chapter 6)
- Aliases/cautions: two sources are dependent when they share data, authors, assumptions, training, software defaults, or a measurement standard — and **agreement among dependent sources is cheap**, being indistinguishable from agreement among independent ones when all you see is the numbers; counting five reports as five pieces of evidence assumes an independence nobody checked; **no source in this book's bibliography supports this entry**, which is the book's own reasoning from what dependence means, and proposed `decisions/0016` clause 6 records it as a fourth instance of the demonstrate-because-unsourced disposition and refers it to the author
- Definition status: **provisional and unsourced** — proposed `decisions/0016` clause 6; pending the book-level adjudication that clause requests

## replication

- Preferred term: replication
- Field/origin: research methodology
- Introduced in: Chapter 9
- Distinct from: reproduction of an analysis on the same data; verification (Chapter 5); transportability; robustness (Chapter 12)
- Aliases/cautions: **successful replication settles less than it appears to** — "even successful replication tells us little either for or against simple generalization or to support for the conclusion that the next will work in the same way" (`deaton2016rct` p. 27) — and **failed replication settles less than it appears to in the other direction**: "Nor do failures of replication make the original result useless" (same page), because "We often learn much from coming to understand why replication failed" (p. 28); the illustration this book uses is Russell's chicken, **as reported at** `deaton2016rct` p. 28, where the diagnosis is that "Her problem was not her methodology, but rather that she did not understand the social and economic structure that gave rise to the causal relations that she observed"; Russell (1912) was not obtained
- Definition status: **provisional** — proposed `decisions/0016` clause 5; source-verified against `deaton2016rct` pp. 27–28

## external validity

- Preferred term: external validity — **registered as a hazard; `transportability` is preferred**
- Field/origin: research design / social science methodology
- Introduced in: Chapter 9
- Distinct from: validity in the measurement sense (Chapter 3); internal validity; transportability; generalizability as loose speech
- Aliases/cautions: the idea that a result found in one setting "holds" elsewhere; **the binary framing is the problem** — it "asks the results of an RCT to satisfy a condition that is neither necessary nor sufficient for a trial to be useful, and so both overstates and understates their value" (`deaton2016rct` p. 27); not necessary, because a study can be useful without its result holding elsewhere; not sufficient, because a result holding elsewhere need not make the study useful for your decision; **it is a relation between a study and a target, never a property a study has**; register the term because readers will meet it, and do not organise thinking around it — the same handling `statistical significance` got in Chapter 8
- Definition status: **provisional** — proposed `decisions/0016` clause 4; source-verified against `deaton2016rct` p. 27

## transportability

- Preferred term: transportability
- Field/origin: causal inference
- Introduced in: Chapter 9
- Distinct from: external validity (the binary framing this book declines); statistical adjustment; extrapolation; interpolation; robustness (Chapter 12)
- Aliases/cautions: whether a result established in one setting applies in another, and **under what conditions** — the question form rather than the yes/no form; it "lies at the heart of every scientific investigation because, invariably, experiments performed in one environment are intended to be used elsewhere, where conditions are likely to be different" (`bareinboim2016fusion` p. 7350); **not a statistical adjustment** — answering it requires knowing how the settings differ in ways that bear on the mechanism, which is subject-matter knowledge and is in neither dataset; `bareinboim2016fusion` p. 7345 names **transportability bias** as distinct from confounding and sample selection bias; **the book teaches no transport formula**; a failure of transport and a failure of positivity (Chapter 7) are the same fact approached from opposite directions, which is the book's own observation
- Definition status: **provisional** — proposed `decisions/0016` clause 7; source-verified against `bareinboim2016fusion` pp. 7345, 7350

## support factor

- Preferred term: support factor
- Field/origin: philosophy of causation / economics; the term is used in this sense at `deaton2016rct` p. 28
- Introduced in: Chapter 9
- Distinct from: confounder (Chapter 7); moderator; covariate; mechanism (Chapter 2); necessary condition
- Aliases/cautions: a condition a cause needs in order to operate — "without which a cause that produces the targeted effect in one place, even though it may be present and have the capacity to operate elsewhere, will remain latent and inoperative" (`deaton2016rct` p. 28); the source's example is a television that burns a house down only given "wiring faults, the presence of tinder, and so on"; **the consequence for averages is exact**: two populations share an average effect only if they share the average net effect of the support factors (p. 29), and those "are however just the kind of factors that are likely to be differently distributed in different populations"; **this is why transport is a subject-matter question** — identifying the support factors requires knowing how the thing works; the source attributes the underlying analysis to Mackie (1974) under the name INUS causality, which was not obtained and which this book does not use
- Definition status: **provisional** — proposed `decisions/0016` clause 7.1; source-verified against `deaton2016rct` pp. 28–29

## expert judgment

- Preferred term: expert judgment
- Field/origin: decision analysis / risk analysis
- Introduced in: Chapter 9
- Distinct from: opinion; consensus; authority; prior (Chapter 6); assumption record (Chapter 5)
- Aliases/cautions: a source of evidence like any other, to be treated as one — **not excluded for being judgment, and not privileged for being expert**; the discipline is Chapter 6's, reused rather than re-taught: a panel that has never been scored is in exactly the position of Chapter 6's unscored forecaster, and the remedy is a record of what was said, when, conditional on what, and what happened; `tversky1974judgment` p. 1124 is explicit that the underlying heuristics "are quite useful", so do not present expert judgment as merely defective; **this book teaches no elicitation protocol and no aggregation method**, per proposed `decisions/0016` clause 8.3; experts sharing training or a literature are a dependence problem, not five independent sources
- Definition status: **provisional** — proposed `decisions/0016` clause 8; reuses `gneiting2007scoring` p. 359 and `tversky1974judgment` p. 1124, both verified for Chapter 6

## Chapter 10 block — PROVISIONAL

Six entries introduced by proposed [Decision 0017](../decisions/0017-chapter10-values-terminology-and-boundary.md), which is **not author-adjudicated**.
The same decision closes `objective` and `metric` — TODO since Chapter 1 — and specialises `alternative`, whose Chapter 1 entry recorded that systematic generation remained Chapter 10.
Clause 1 records that `keeney1996valuefocused` could **not** be obtained in full and that the framework is used **as reported at** `bradley2016structured`, honouring the prohibition standing in that source note since Chapter 1.
Clause 5 **resolves a conflict** between `decisions/0006` and `README.md` over where trade-offs live, in favour of `README.md`.

## value

- Preferred term: value
- Field/origin: decision analysis
- Introduced in: Chapter 10
- Distinct from: objective; preference; utility (Chapter 11); a number in a dataset; moral value as a subject of ethics
- Aliases/cautions: **"Values are what we fundamentally care about"** (`bradley2016structured` p. 5, reporting Keeney 1992); "The consequences that stakeholders care about are considered values" (p. 8); **values are present in every decision and the only question is whether they were written down** — "Alternative-focused decision-making does consider values, but often only implicitly. They may not be clearly stated and thus not fully considered when making a decision" (p. 5); **an option set is already a claim about what matters**, which is the book's own formulation of that point; do not confuse with the numeric sense — this book writes `value` for what is cared about and never for a datum
- Definition status: **provisional** — proposed `decisions/0017` clause 2.1; source-verified against `bradley2016structured` pp. 5, 8

## fundamental objective

- Preferred term: fundamental objective
- Field/origin: decision analysis
- Introduced in: Chapter 10
- Distinct from: means objective; constraint; metric; a vision statement
- Aliases/cautions: an objective wanted for its own sake — **"A fundamental objective is usually determined when the answer to 'why is this important' is '…just because'…. meaning that it is simply something that humans need or want"** (`bradley2016structured` p. 51); **fundamental objectives evaluate alternatives, means objectives generate them**, which is the book's own formulation of the distinction's practical use; six properties of good objectives are listed at p. 51 as "Fundamental, Complete, Concise, Sensitive, Understandable, Independent", attributed there to Gregory et al. (2012), **which was not obtained** — the book quotes the list and develops only *Fundamental* and *Independent*, since inventing glosses would attribute content to an unread source; most stakeholders "will agree on objectives high in the hierarchy even if not specific approaches" (p. 54)
- Definition status: **provisional** — proposed `decisions/0017` clause 3.2; source-verified against `bradley2016structured` pp. 51, 54

## means objective

- Preferred term: means objective
- Field/origin: decision analysis
- Introduced in: Chapter 10
- Distinct from: fundamental objective; alternative; constraint
- Aliases/cautions: an objective wanted **because it leads to something else** — it fails the "why is this important" test by producing another objective rather than "just because"; the documented failure is a "messy mix of means and ends" presented as objectives (`bradley2016structured` p. 49); **mistaking a means for an end is how an organisation optimises something completely and still fails at what it wanted**, which is the book's own statement of the consequence; means objectives are not defective — they are where alternatives come from, and the error is only in treating them as the thing evaluated against
- Definition status: **provisional** — proposed `decisions/0017` clause 3.2; source-verified against `bradley2016structured` pp. 49, 51

## attribute

- Preferred term: attribute
- Field/origin: decision analysis
- Introduced in: Chapter 10
- Distinct from: objective; value; metric (the same role in management vocabulary); measure and construct (Chapter 3); **the estimand attributes of Chapter 7, which are a different object sharing the word**
- Aliases/cautions: the measurable quantity at the bottom of an objectives hierarchy, standing in for the objective above it — "Evaluation measures, attributes that can be used to evaluate performance toward higher-level objectives, are at the bottom of the OH" (`bradley2016structured` p. 51); "Effective attributes are characterized by their measurability, understandability, and operability" (p. 51); **the objective is what is valued and the attribute is what will be assessed** (p. 51), a pairing that is Chapter 3's construct/measure ladder in a new setting; Chapter 7's use of `attribute` for the components of an estimand is a different object and a compatible sense, and neither should be read into the other
- Definition status: **provisional** — proposed `decisions/0017` clause 3.4; source-verified against `bradley2016structured` p. 51

## stakeholder

- Preferred term: stakeholder
- Field/origin: decision analysis / public-sector practice
- Introduced in: Chapter 10
- Distinct from: decision-maker (Chapter 1); expert; consultee; user; the people who were asked
- Aliases/cautions: **a party affected by the decision** — and the qualification for having a value is being affected, not expertise: "All parties, regardless of education or socio-economic status know what is important to them and can communicate those values" (`bradley2016structured` p. 7); **who knows how the system works and who has a stake in it are different rosters**, and a consultation list built for the first will silently answer the second, which is the book's own formulation; `common values` are "those that most stakeholders will agree upon, i.e., values that they share even if at different magnitudes" (p. 6) — **not consensus**; the book teaches no facilitation or elicitation technique, per proposed `decisions/0017` clause 4.4
- Definition status: **provisional** — proposed `decisions/0017` clause 4.1; source-verified against `bradley2016structured` pp. 6–7

## constraint

- Preferred term: constraint
- Field/origin: decision analysis / optimization
- Introduced in: Chapter 10
- Distinct from: objective; assumption (Chapter 5); boundary (Chapter 2); a preference
- Aliases/cautions: a limit on what alternatives may be considered — and **"accepting constraints as immoveable" is one of four documented traps** (`bradley2016structured` p. 7, attributed there to Gregory et al. 2012, which was not obtained); the practical question is **who set this and what would change it**, since a constraint accepted without examination decides the outcome while remaining unexaminable, exactly as an implicit value does — but unlike a value it usually has an author who could be asked; the book's own sorting into constraints that are physical or statutory and constraints that are conventions, budgets, or timetables is an illustration rather than a theory, and is labelled as such; the other three traps at p. 7 are anchoring on the first proposed alternative, avoiding controversial trade-offs, and rushing to premature solutions
- Definition status: **provisional** — proposed `decisions/0017` clause 4.3; the trap is source-verified against `bradley2016structured` p. 7; the sorting is the book's own

## Chapter 11 block — PROVISIONAL

Eight entries introduced by proposed [Decision 0018](../decisions/0018-chapter11-decision-terminology-and-boundary.md), which is **not author-adjudicated**.
The same decision specialises `consequence` in its existing position above.
Clause 2 takes a **third bounded notation extension**: a decision table, and one inline text tree where sequence matters. Nothing else, and **no read source teaches the tree** — the layout is the book's own presentation of standard material.
**Clause 4.4 records the closest the book has come to a fifth instance of the demonstrate-because-unsourced disposition, and states why it is not one**: no source was obtained for risk attitude, and the chapter declines to teach the practice rather than teaching it unsourced.

## decision tree

- Preferred term: decision tree
- Field/origin: decision analysis
- Introduced in: Chapter 11
- Distinct from: a causal diagram (Chapter 7); an influence diagram; a classification tree in machine learning, which is an unrelated object sharing the word; a flowchart
- Aliases/cautions: a layout of **acts**, **states**, and **consequences**, branching from a choice through what you do not control to what results; **it is a layout, not a decision** — drawing one settles nothing and its value is that it forces every act to be stated against every state; for a one-shot decision a table with acts as rows and states as columns carries the same information and is easier to read, and this book uses the tree only where sequence matters, as in test-then-act; **no source read for this book teaches the device**, which is standard material in a literature this book did not obtain, so the presentation is the book's own and is labelled; no formal node conventions are used
- Definition status: **provisional** — proposed `decisions/0018` clauses 2.2 and 2.5; presentation is the book's own

## expected value

- Preferred term: expected value (as a **decision rule**)
- Field/origin: decision analysis
- Introduced in: Chapter 6 as `expectation`, a summary of a distribution; Chapter 11 as a rule for choosing
- Distinct from: the expectation itself (Chapter 6); the most likely outcome; utility; the best worst case
- Aliases/cautions: choosing the act with the best probability-weighted average consequence; **Chapter 6 refused to make this move and instructed Chapter 11 to make it deliberately**, so the chapter states plainly that using the rule is a choice which "smuggles in risk neutrality"; the positive case is that it is **the only rule that uses all the information in the table** — best-worst-case and smallest-spread rules discard most of the numbers and all of the probabilities — and that it is what makes value of information computable at all; a source applying it records that where two acts have equal expected monetary value "decision theory recommends indifference" (`colyvan2016voi` p. 303), which shows the recommendation follows from the rule rather than from the situation
- Definition status: **provisional** — proposed `decisions/0018` clauses 4.1–4.2; source-verified against `colyvan2016voi` p. 303

## risk attitude

- Preferred term: risk attitude
- Field/origin: decision analysis / economics
- Introduced in: Chapter 11, **named and demonstrated but not formalized**
- Distinct from: risk as a hazard; uncertainty; ambiguity; variance; irrationality
- Aliases/cautions: a decision-maker's disposition toward spread in consequences, as against their average; **demonstrable without machinery**: where one act costs the same in every state and more in expectation than the act with the best average, preferring it is a preference the arithmetic cannot supply, and neither can any amount of evidence; **no source was obtained for a formal treatment**, so this book names the phenomenon, shows it in a table, and routes utility functions, certainty equivalents, and risk premiums to the depth curriculum; **do not present risk aversion as an error** — it is a value, and Chapter 10 established that values are the decision-maker's to supply; proposed `decisions/0018` clause 4.4 records this as the closest the book has come to teaching a practice unsourced and states why it is not one
- Definition status: **provisional and unsourced** — proposed `decisions/0018` clauses 4.3–4.4; the chapter states only what its own table displays

## sensitivity analysis

- Preferred term: sensitivity analysis
- Field/origin: modelling / decision analysis
- Introduced in: named and refused as criticism in Chapter 5; used as a model check in Chapter 8; used in its decision sense in Chapter 11
- Distinct from: criticism (Chapter 5); robustness (Chapter 12); uncertainty quantification; varying every input by a fixed percentage
- Aliases/cautions: **one technique with three jobs** — in Chapter 5 it is named and refused as a substitute for criticism, because varying inputs inside a formulation cannot see the formulation; in Chapter 8 it is a model check, telling you which assumptions the answer is sensitive to and therefore where checking effort should go; in Chapter 11 it asks the decision question — **at what point does the best act change?** — which is the form that makes value of information tractable; the useful output is not a range of answers but a **critical value**, and the question is whether your uncertainty straddles it (`colyvan2016voi` p. 302); **varying every input by ±20% is not sensitivity analysis** in any of the three senses, because it answers a question nobody asked
- Definition status: **provisional** — proposed `decisions/0018` clause 5; the decision sense source-verified against `colyvan2016voi` p. 302

## value of information

- Preferred term: value of information
- Field/origin: decision analysis
- Introduced in: Chapter 11
- Distinct from: how informative an observation is (Chapter 6's ratio); the cost of collection; the interest of a finding; statistical power
- Aliases/cautions: **how much better off you would be with the information than without it, measured in the decision's own currency** — and it is **zero whenever no possible result would change the act**; the standing example is a radiograph for a suspected broken toe, where "the treatment for a bruised toe or a broken toe is the same" so "The value of information delivered by the radiographic examination in this decision about treatment is zero" (`colyvan2016voi` p. 303), and the test is perfectly accurate; **always relative to a decision** — "the same information might be valuable for other purposes" (p. 303) and "it depends on what you're going to do with the information" (p. 304); **informative is not valuable**, which separates this from Chapter 6's likelihood ratio; the summary to carry is "Reducing ignorance is not the name of the game, it's improving management decisions" (p. 304); four documented limitations apply — framing, the single-currency requirement, budgets not being fungible, and value arriving later (pp. 305–306) — and **the study itself costs something** (p. 308 n. 16)
- Definition status: **provisional** — proposed `decisions/0018` §6; source-verified against `colyvan2016voi` pp. 303–306, 308

## value of perfect information

- Preferred term: value of perfect information
- Field/origin: decision analysis
- Introduced in: Chapter 11
- Distinct from: the value of a particular study; certainty; the cost of the decision being wrong
- Aliases/cautions: what it would be worth to know the state of the world exactly, before choosing — **and it is a ceiling**, since "the value of imperfect information is always less than that of perfect information" (`colyvan2016voi` p. 303); **this makes it a screening rule and the cheapest thing in the chapter**: if the ceiling is below the price of the cheapest study you could commission, no study can pay for itself and you are finished in an afternoon; it is arithmetic on a table already built, requires no new data, and is almost never run before studies are commissioned
- Definition status: **provisional** — proposed `decisions/0018` clause 6.3; source-verified against `colyvan2016voi` p. 303

## ambiguity

- Preferred term: ambiguity
- Field/origin: decision theory
- Introduced in: Chapter 11, at concept depth only
- Distinct from: risk; uncertainty in the general sense; vagueness; structural uncertainty (Chapter 5); imprecision in a measurement (Chapter 3)
- Aliases/cautions: not knowing a probability exactly, as against knowing it and facing a chance outcome; **whether it matters depends on whether the range straddles a critical value** — a source works a bet where the probability is known only to lie between 0.4 and 0.6 and concludes "No further information is required in deciding whether to accept this bet or not", and contrasts a range of 0.2 to 0.4 which "straddles the critical value of 1/3" (`colyvan2016voi` p. 302); **the book treats ambiguity only this far**; **Ellsberg (1961) was not obtained**, the term "Ellsberg paradox" is not used, and those experiments are not described
- Definition status: **provisional** — proposed `decisions/0018` §7; source-verified against `colyvan2016voi` p. 302

## decision quality

- Preferred term: decision quality
- Field/origin: decision analysis
- Introduced in: Chapter 11 as a **disposition, not a framework**
- Distinct from: outcome quality; a named commercial methodology; decision-making capability as an organisational assessment
- Aliases/cautions: **a good decision and a good outcome are different things**, since an uncertain world can punish a well-made choice — `nasem2026decisionmaking` supports the distinction between decision process and outcome, as recorded in its source note; the practical form this book teaches is that a decision is defensible when its acts, states, consequences, probabilities, and the rule used to choose are all written down and arguable, which is the same discipline Chapters 6 to 10 applied to probabilities, causal claims, estimates, sources, and objectives; **no named framework is taught**, and the commercial decision-quality literature was not obtained; do not use the term to grade decisions after their outcomes are known, which is the error it exists to prevent
- Definition status: **provisional** — proposed `decisions/0018` clause 8.1; the process/outcome distinction reuses `nasem2026decisionmaking` as verified for Chapter 1

## Chapter 12 block — PROVISIONAL

Ten entries introduced by proposed [Decision 0019](../decisions/0019-chapter12-optimization-terminology-and-boundary.md), which is **not author-adjudicated**.
The same decision closes `robustness` — TODO since Chapter 1 and reserved by Decision 0012 clause 5.4 — and specialises `constraint`.
Clause 1 records that, unlike Chapter 11, **nothing in this chapter is taught unsourced**: three sources were obtained in full and every governed competence item maps to one. **The count of demonstrate-because-unsourced instances stays at four.**
Clause 2 adds **no notation**; the governed word "intuition" is read as controlling.

## feasible region

- Preferred term: feasible region
- Field/origin: optimization
- Introduced in: Chapter 12 at concept depth only
- Distinct from: the option set (Chapter 10); the alternative set; the budget
- Aliases/cautions: the combinations of actions that satisfy every constraint — **at programme scale the object of choice is a combination, not an alternative**, which is what distinguishes Chapter 12's problem from Chapter 11's; **Chapter 10's discipline applies first**: a feasible region drawn around constraints nobody questioned is smaller than the real one, and two of the anchor's four stated constraints dissolved on inspection; the book draws no diagram and states no formulation
- Definition status: **provisional** — proposed `decisions/0019` clause 7.1; concept depth, taught on the anchor

## marginal benefit

- Preferred term: marginal benefit
- Field/origin: economics
- Introduced in: Chapter 12
- Distinct from: total benefit; average benefit; the value of a whole scheme
- Aliases/cautions: "the benefit received from an incremental increase in the consumption of a good or service. It is calculated as the increase in total benefit divided by the increase in consumption" (`epa2010economic` p. xiii); paired with `marginal cost` it supplies the classical stopping rule — spend until the two are equal — and **Chapter 12 shows that rule failing on indivisible investments**, where there is no next unit to evaluate
- Definition status: **provisional** — proposed `decisions/0019` clause 3.1; source-verified against `epa2010economic` p. xiii

## marginal cost

- Preferred term: marginal cost
- Field/origin: economics
- Introduced in: Chapter 12
- Distinct from: total cost; average cost; the price of a scheme; opportunity cost
- Aliases/cautions: "the change in total cost that results from a unit increase in output. It is calculated as the increase in total cost divided by the increase in output" (`epa2010economic` p. xiii); **the related idea the chapter leans on is opportunity cost** — "the value of the next best alternative to a particular activity or resource", which "need not be assessed in monetary terms" and "can be assessed in terms of anything that is of value to the person or persons doing the assessing" (p. xiv), a property that distinguishes marginal reasoning from the value-of-information machinery of Chapter 11, which does require a single currency
- Definition status: **provisional** — proposed `decisions/0019` clause 3.1; source-verified against `epa2010economic` pp. xiii–xiv

## shadow price

- Preferred term: shadow price — **always qualify; two unrelated senses exist**
- Field/origin: optimization
- Introduced in: Chapter 12
- Distinct from: market price; marginal cost; **the shadow price of capital, a discounting concept in cost-benefit analysis which this book does not use**
- Aliases/cautions: what it would be worth to move a binding constraint by a small amount — the optimization sense arises as "a set of prices for which there is no advantage to the firm in being allowed to pay for constraint violations" (`boyd2004convex` p. 241); **it answers a question Chapter 10 could not**: not whether a constraint is real, but what moving it is worth; **it is local**, defined for small changes, and **asymmetric** — "the results are not symmetric with respect to loosening or tightening a constraint" (p. 251); an inactive constraint has a shadow price of zero; **with indivisible investments it is a step function that need not decrease** — the anchor shows an extra £50k worth nothing at one envelope and 0.84 units per £k at a larger one, which cannot happen under convexity; the second sense appears in `epa2010economic` §6.2.4, **which was not read and is not characterised**
- Definition status: **provisional** — proposed `decisions/0019` clauses 4.1 and 4.5; source-verified against `boyd2004convex` pp. 241, 251–252

## convexity

- Preferred term: convexity
- Field/origin: mathematics / optimization
- Introduced in: Chapter 12 through its **consequence** only
- Distinct from: linearity; smoothness; simplicity; concavity as a separate technical matter
- Aliases/cautions: **the book teaches what its presence or absence does, not how to recognise it** — the source says recognising a convex function "can be difficult" (`boyd2004convex` p. 8); under convexity, local improvement reaches the global best and reliable solvers exist, so that "if you formulate a practical problem as a convex optimization problem, then you have solved the original problem" (p. 8); without it, "there are no effective methods for solving the general nonlinear programming problem" (p. 9); **the practical marker for a general reader is lumpiness** — indivisible investments break the marginal stopping rule, which the anchor demonstrates numerically; no formulation, algorithm, or diagram is given
- Definition status: **provisional** — proposed `decisions/0019` clause 4.3; source-verified against `boyd2004convex` pp. 8–9

## local optimum

- Preferred term: local optimum
- Field/origin: optimization
- Introduced in: Chapter 12
- Distinct from: global optimum; a satisfactory answer; a converged solution
- Aliases/cautions: a point that "minimizes the objective function among feasible points that are near it, but is not guaranteed to have a lower objective value than all other feasible points" (`boyd2004convex` p. 9); **two consequences a reader can act on without any mathematics** — the answer depends on where the search started, since the "initial guess or starting point is critical, and can greatly affect the objective value of the local solution obtained" (p. 9); and **"Little information is provided about how far from (globally) optimal the local solution is"** (p. 9); so a nonconvex result carries no bound on its own error, which is a different situation from an estimate with an interval (Chapter 8)
- Definition status: **provisional** — proposed `decisions/0019` clause 4.3; source-verified against `boyd2004convex` p. 9

## scenario

- Preferred term: scenario
- Field/origin: policy analysis / futures studies
- Introduced in: Chapter 12
- Distinct from: forecast; prediction; a probability-weighted state (Chapter 11); a rival model (Chapter 5, a related but distinct use); a sensitivity case
- Aliases/cautions: **a plausible future used as a challenge set, not a prediction** — ensembles "offer compelling alternative futures that can force stakeholders to question their assumptions" (`lempert2003shaping` p. 52); **diversity, not count, is the requirement**: "the diversity requirement that guides the construction of scenario ensembles is crucial to building credibility among parties to a decision" (p. 52), so twenty scenarios differing in one parameter are one scenario; plausibility is enforced as constraints — paths are excluded when they "violate known principles of economics" (p. 52) — so an ensemble is not everything imaginable; Chapter 5's `rival model` is a differently-simplified representation used for criticism, which is a compatible but distinct use
- Definition status: **provisional** — proposed `decisions/0019` clause 5.4; source-verified against `lempert2003shaping` p. 52

## regret

- Preferred term: regret
- Field/origin: decision theory
- Introduced in: Chapter 12
- Distinct from: loss; cost; the outcome of a bad decision (Chapter 11's decision quality); disappointment
- Aliases/cautions: the shortfall between what a strategy achieves in a future and the best that could have been achieved in that future; **minimax regret is Savage's rule**, described as "a practical rule of thumb for cases where individuals or groups are 'vague' about the probabilities they attach to certain events" (`lempert2003shaping` p. 53, reporting Savage 1950, **which was not obtained**); **this book does not present it as the right rule**, because the source reports four pathologies from Savage himself: it "often yields neither a best strategy nor a simple ordering among strategies"; in a group context it "can be undemocratic"; participants "can easily manipulate outcomes by lying about the weights"; and it "can be too sensitive to low-probability, high-consequence events" (p. 53, n. 13); the anchor exhibits the first immediately, with the minimax portfolio and its runner-up separated by less than the inputs can support
- Definition status: **provisional** — proposed `decisions/0019` clauses 5.5–5.6; source-verified against `lempert2003shaping` p. 53 and n. 13

## adaptive plan

- Preferred term: adaptive plan
- Field/origin: policy analysis
- Introduced in: Chapter 12
- Distinct from: a vague plan; a contingency list; a phased programme without triggers; sequential control (Chapter 14); feedback (Chapter 13)
- Aliases/cautions: a plan that specifies **in advance** how it will change — "adaptive decision strategies are the means most commonly used to achieve robustness because they are designed to evolve in response to new data", and a decisionmaker "may settle on near-term actions but plan to adjust them **in specific ways**" (`lempert2003shaping` p. 57); the reported structure has three parts (`shaping actions`, `hedging actions`, `signposts`) attributed there to Dewar (1993, 2001), **which was not obtained**; **the flexibility is not free** — this book requires a staging premium to be stated, because an adaptive plan whose optionality costs nothing is a way of avoiding a decision; adapting because you **learned** is Chapter 12, adapting because the system **responded to you** is Chapter 13
- Definition status: **provisional** — proposed `decisions/0019` §6; source-verified against `lempert2003shaping` pp. 57–58

## signpost

- Preferred term: signpost
- Field/origin: policy analysis; the term is used in this sense at `lempert2003shaping` p. 58, reporting Dewar
- Introduced in: Chapter 12
- Distinct from: a metric (Chapter 10); a monitoring indicator; a key performance indicator; a review date
- Aliases/cautions: an observation, **with a threshold agreed in advance**, that "warn[s] of the need to change the mix of actions" (`lempert2003shaping` p. 58, reporting Dewar); **the part organisations omit** — a plan with shaping and hedging actions but no signposts is a portfolio, not an adaptive plan, because nothing states what would cause it to change; a signpost without a named threshold is a metric being watched; **Chapter 12 designs signposts and Chapter 17 operates them**, which is where the question of whether anyone is actually looking belongs
- Definition status: **provisional** — proposed `decisions/0019` §6; source-verified against `lempert2003shaping` p. 58

---

## Chapter 13 block — PROVISIONAL

Ten entries below are proposed by `../decisions/0020` and are provisional pending author adjudication. Two further entries — `equilibrium` and `stability` — are **closed from `TODO`** by the same decision in their existing positions above, and `feedback` is developed there from Chapter 1's screening depth to its formal home.

Chapter 13's scope was set in advance by `../decisions/0007`, which is **Accepted**; where these entries restate it they report a settled decision rather than proposing one.

---

## stock

- Preferred term: stock
- Field/origin: system dynamics; accounting; epidemiology
- Introduced in: Chapter 13
- Distinct from: a flow; any quantity that changes over time; a parameter; a measurement
- Aliases/cautions: a stock is **what accumulates its net flows** — "stocks integrate (accumulate) their net inflows" (`sterman2006evidence` p. 508); the same distinction appears as prevalence and incidence, balance and cash flow, population and births, and is taught once rather than per domain; **a quantity that varies is not thereby a stock**, and `../decisions/0007` guards this with the refrigerated-warehouse temperature case; do not introduce stock-and-flow diagramming notation
- Definition status: verified — `sterman2006evidence` p. 508

---

## flow

- Preferred term: flow
- Field/origin: system dynamics
- Introduced in: Chapter 13
- Distinct from: a stock; a rate of change of anything; a transfer that leaves the stock unchanged
- Aliases/cautions: **flows are named in pairs — what increases the stock and what decreases it**; "a population is increased by births and decreased by mortality; the burden of mercury in a child's body is increased by ingestion and decreased by excretion" (`sterman2006evidence` p. 508); a stock with only its inflow named has not been analysed
- Definition status: verified — `sterman2006evidence` p. 508

---

## accumulation

- Preferred term: accumulation
- Field/origin: system dynamics
- Introduced in: Chapter 13
- Distinct from: growth; a trend; the net flow itself
- Aliases/cautions: **the stock does not have the same shape as the net flow** — "a stock rises even as its net inflow falls, as long as the net inflow is positive" (`sterman2006evidence` p. 508); the common error is assuming "that system inputs and outputs are correlated" (same page); this is the book's only claim of difficulty supported by a measurement — mean scores of 0.77, 0.48, and 0.41 on three tasks (`boothsweeney2000bathtub` p. 264), with "conceptual confusion, not arithmetical error" (p. 265); **doing and undoing have fundamentally different time constants** (`sterman2006evidence` p. 507)
- Definition status: verified — `sterman2006evidence` pp. 507–508; `boothsweeney2000bathtub` pp. 264–265, 278

---

## delay

- Preferred term: delay
- Field/origin: system dynamics; control
- Introduced in: Chapter 1 as a screening prompt; formal home Chapter 13
- Distinct from: slowness; a lag in a statistical model; the time an analysis takes
- Aliases/cautions: two kinds are distinguished, following `../decisions/0007` — an **information delay** between the system changing and the decision-maker observing it, and a **physical or action delay** between an action being taken and its effect on the system; **the two add**, and their sum is what determines whether a correction can arrive in time; delays "slow the accumulation of evidence", make short- and long-run impacts differ, and "create instability and fluctuations that confound our ability to learn" (`sterman2006evidence` p. 508); **no time constants, lag operators, transfer functions, or delay differential equations**
- Definition status: verified — `sterman2006evidence` p. 508

---

## open loop

- Preferred term: open loop
- Field/origin: control theory
- Introduced in: Chapter 13
- Distinct from: a system with no dynamics; an unmonitored process; an uncontrolled process
- Aliases/cautions: a configuration in which the interconnection between the two systems is broken, so that what one does no longer returns to influence it (`astrom2008feedback` p. 2); **most of this book's earlier reasoning is open loop**, and naming the configuration is what makes that visible
- Definition status: verified — `astrom2008feedback` p. 2

---

## closed loop

- Preferred term: closed loop
- Field/origin: control theory
- Introduced in: Chapter 13
- Distinct from: a repeated decision; a monitored process; a feedback *effect* without a return path
- Aliases/cautions: systems "interconnected in a cycle" (`astrom2008feedback` p. 2); closing the loop is what makes causal reasoning circular and what makes formal analysis necessary; **a decision that is revisited is not thereby closed loop** — the loop closes when the action changes what the next observation will be
- Definition status: verified — `astrom2008feedback` p. 2

---

## reinforcing feedback

- Preferred term: reinforcing feedback
- Field/origin: system dynamics (`self-reinforcing`); control theory (`positive feedback`)
- Introduced in: Chapter 13
- Distinct from: balancing feedback; growth; a trend; instability, which is a consequence and not the definition
- Aliases/cautions: a loop in which an increase in a quantity leads to that quantity being "further increased through its dynamics" (`astrom2008feedback` p. 22); **the book prefers `reinforcing` to `positive`** because `positive` is a controlled term in this book paired with `normative` since Chapter 1, and `../decisions/0007` banned the collision from Chapter 1 for that reason; `positive feedback` is named once as the term the reader will meet; **a reinforcing loop is not a prediction of unbounded growth** — it is "usually accompanied by a saturation that limits the growth of the quantity" (same page)
- Definition status: verified — `astrom2008feedback` p. 22; `sterman2006evidence` p. 507

---

## balancing feedback

- Preferred term: balancing feedback
- Field/origin: system dynamics (`self-correcting`); control theory (`negative feedback`)
- Introduced in: Chapter 13
- Distinct from: reinforcing feedback; stability, which it does not guarantee; a correction that works
- Aliases/cautions: a loop that acts to reduce the discrepancy it responds to — the principle being to "base correcting actions on the difference between desired and actual performance" (`astrom2008feedback` p. 17); **balancing does not mean stabilising**: a balancing loop with enough delay produces overshoot and oscillation; `negative feedback` is named once and not adopted, for the reason given at `reinforcing feedback`
- Definition status: verified — `astrom2008feedback` pp. 17, 22; `sterman2006evidence` p. 507

---

## oscillation

- Preferred term: oscillation
- Field/origin: dynamical systems
- Introduced in: Chapter 13
- Distinct from: noise; seasonality; measurement variation; instability, which is a different property
- Aliases/cautions: repeated over- and under-correction around a target, arising when "the system overreacts since a small change in the error makes the actuated variable change over the full range" (`astrom2008feedback` p. 24) or when corrections are applied through a delay; **oscillation is not evidence that anyone did anything wrong**; `limit cycle` — an isolated periodic solution (`astrom2008feedback` p. 101) — is named once and not developed, and the phase-plane machinery is deferred by `../decisions/0007`
- Definition status: verified — `astrom2008feedback` pp. 24, 101

---

## overshoot

- Preferred term: overshoot
- Field/origin: system dynamics; control
- Introduced in: Chapter 13
- Distinct from: overreaction as a character failing; a forecasting error; oscillation, which is what repeated overshoot produces
- Aliases/cautions: **the mechanism is that correction continues after enough correction has been applied and before its effect is visible** — decision-makers "continue to intervene to correct apparent discrepancies between the desired and actual state of the system even after sufficient corrective actions have been taken to restore equilibrium" (`sterman2006evidence` p. 508); **the rule being followed is a correct rule**, which is why overshoot must never be presented as carelessness
- Definition status: verified — `sterman2006evidence` p. 508

---

## policy resistance

- Preferred term: policy resistance
- Field/origin: system dynamics
- Introduced in: Chapter 13
- Distinct from: a policy failing; opposition to a policy; non-compliance; a bad forecast; unintended consequences in the loose sense
- Aliases/cautions: **"the tendency for interventions to be defeated by the response of the system to the intervention itself"** (`sterman2002models` p. 504) — the locator Chapter 2 verified and was instructed to reserve for here; it "arises because we do not understand the full range of feedbacks surrounding—and created by—our decisions" (`sterman2006evidence` p. 507); **"there are no side effects—just effects"** (`sterman2006evidence` p. 505); the system is not being perverse, it is responding, which is what a system does; recognising that structure shapes behaviour "does not relieve us of personal responsibility for our actions" (`sterman2006evidence` p. 510)
- Definition status: verified — `sterman2002models` p. 504; `sterman2006evidence` pp. 505, 507, 510

---

## state space

- Preferred term: state space
- Field/origin: dynamical systems; control theory
- Introduced in: Chapter 13, **named only**
- Distinct from: the state; a sample space; a set of scenarios; the feasible region (Chapter 12)
- Aliases/cautions: the set of all possible states of a system (`astrom2008feedback` p. 28); **named once to discharge the promise recorded in the `state` entry that "`state space` is not named until Chapter 13", and not developed**; no state-space form, no order of a system, no linearity, no reachability, no observability — those are Chapter 14 and the depth curriculum
- Definition status: verified — `astrom2008feedback` p. 28

---
