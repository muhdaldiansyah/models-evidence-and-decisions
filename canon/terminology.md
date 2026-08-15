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
- Field/origin: TODO
- Introduced in: Chapter 1 (informal); Chapter 7 (formal)
- Distinct from: estimand; proxy; objective
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

## estimand

- Preferred term: estimand
- Field/origin: statistics
- Introduced in: Chapter 7
- Distinct from: target; estimator; estimate
- Aliases/cautions: none recorded yet
- Definition status: TODO — verify against canonical sources

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
