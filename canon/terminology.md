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

## prediction

- Preferred term: prediction
- Field/origin: statistics / forecasting
- Introduced in: Chapter 6
- Distinct from: intervention; counterfactual
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

## intervention

- Preferred term: intervention
- Field/origin: causal inference
- Introduced in: Chapter 7
- Distinct from: prediction; counterfactual
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

## counterfactual

- Preferred term: counterfactual
- Field/origin: causal inference
- Introduced in: Chapter 7
- Distinct from: prediction; intervention
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

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
