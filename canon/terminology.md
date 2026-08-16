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
- Aliases/cautions: Chapter 1 should normally say `adequate for the stated use` or `adequate for the stated intended use`; the book does not claim that this phrase denotes one universal standardized adequacy framework; individual traditions operationalize adequacy differently
- Definition status: verified for the Chapter 1 use-dependent principle; framework-specific formalization deferred to Chapter 5

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
- Field/origin: measurement science / psychometrics
- Introduced in: Chapter 3
- Distinct from: measure; proxy; target
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

## measure

- Preferred term: measure
- Field/origin: measurement science
- Introduced in: Chapter 3
- Distinct from: construct; proxy; metric
- Aliases/cautions: distinct from the measure-theoretic sense, which this book does not use
- Definition status: TODO — verify against canonical sources

## proxy

- Preferred term: proxy
- Field/origin: measurement / econometrics
- Introduced in: Chapter 3
- Distinct from: construct; measure; target
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

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
