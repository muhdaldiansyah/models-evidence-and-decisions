# Chapter 7 Bounded Research Plan

Status: working control. Governs the four `research-0N-*.md` dossiers.

Bounded in the same sense as Chapters 2–6: four clusters, each with a stop condition, each closing before the next opens.

## Standing rule, carried from Chapter 2

> **Every locator must come from reading the document directly. A fetch summary is a lead, not evidence.**

This rule exists because an automated fetch once returned four confident-looking quotations with page numbers, none of which appeared in the article (`../../sources/sterman2002models.md`).

**It bit again in this chapter, in a smaller way.** `pearl2009causal` p. 109 prints Definition 2 with a typographical error — the antecedent reads `P(M1) = P(M1)` where the argument requires `P(M1) = P(M2)`. Anyone paraphrasing from a summary would never see it. The dossier records the error and quotes the author's own prose restatement instead of the equation.

## A second rule, adopted here

> **Quote only prose that survives text extraction cleanly.**

Two of this chapter's sources set variables in italic math that `pdftotext` drops silently, turning "the observed outcome for every treated individual equals her outcome" into a sentence with holes. A quotation assembled from mangled extraction would be a fabrication even though the source is genuine and open.

Every quotation used in this chapter was checked against the surrounding paragraph and contains no inline mathematics.

## Cluster R01 — Targets and estimands

### Questions

1. What has to be specified before a causal question is a question at all?
2. Does an authoritative attribute list exist, and how far does its authority extend?
3. What is the relationship between a target, a target quantity, and an estimand?
4. Does any second, independent tradition arrive at a similar list?

### Sources

`fda2021estimands` (ICH E9(R1), read at printed pp. 9–10), `hernan2019whatif` (read at printed pp. 37–38), `pearl2009causal` (read at printed p. 122), plus the existing `../../sources/fda2021estimands.md` note and its standing caution.

### Stop condition

Stop when the five ICH attributes are recorded verbatim in structure, the target-trial protocol components are recorded, and the relationship between the two lists is stated without claiming they are the same list.

### Deliverable

`research-01-targets-and-estimands.md`.

## Cluster R02 — Association, intervention, counterfactual

### Questions

1. What exactly separates the three, in the source that Chapter 1 already cites?
2. What is the argument that the separation needs notation?
3. What does the source say about the testability of causal assumptions?
4. Where is the boundary between this and Chapter 6's conditioning?

### Sources

`pearl2009causal`, read at printed pp. 99–101 and 107–110. `shmueli2010predict` for the prediction leg, already verified in Chapter 1.

### Stop condition

Stop when the three levels are distinguishable using the anchor and when the testability asymmetry at p. 101 is recorded with its exact wording.

### Deliverable

`research-02-association-intervention-counterfactual.md`.

## Cluster R03 — Identification

### Questions

1. What is the published definition of identifiability, in each of the two traditions?
2. What are the three identifiability conditions, and what does each rule out?
3. What is the difference between statistical identifiability and causal identification, stated so that a reader can apply it?
4. What does the literature say about controlling for covariates, and is "control for everything" safe?

### Sources

`pearl2009causal` printed pp. 109–110, 113–114, 116–117. `hernan2019whatif` printed pp. 25–27, 30–33.

### Stop condition

Stop when both definitions are recorded verbatim, the three conditions are recorded with their source's own hedge about how demanding they are, and the covariate-selection caution is recorded with its locator.

**Do not proceed into the back-door criterion's machinery.** Record the intuition and the criterion's existence; the definition itself requires blocking and collision concepts this book does not teach.

### Deliverable

`research-03-identification.md`.

## Cluster R04 — Designs, and the chapter's own examples

### Questions

1. What does randomization actually buy?
2. What is the most common overstatement, and is it documented?
3. How do observational designs relate to experiments?
4. What must the anchor supply, and what may the chapter not claim?

### Sources

`deaton2016rct` printed pp. 7–11. `hernan2019whatif` printed pp. 25–26, 37–38.

### Stop condition

Stop when the balance-in-expectation distinction is recorded with its wording, when at least one documented overstatement is recorded as the source presents it, and when the anchor's four failures are specified numerically.

### Deliverable

`research-04-designs-and-examples.md`.

## What this plan does not attempt

- **Do-calculus.** Named at most; never taught.
- **d-separation, colliders, blocking.** The back-door criterion is quoted as existing and not stated.
- **Instrumental variables.** Both sources treat them; both treat them as a separate apparatus. One sentence, routed forward.
- **Mediation, direct and indirect effects.** `pearl2009causal` §5 is out of scope.
- **Propensity scores, IP weighting, standardization, matching.** All are estimation, and estimation is Chapter 8.
- **The debate about whether graphs or potential outcomes are the better framework.** Both sources have positions. The book does not adjudicate, on the same grounds it declined the frequency/degree-of-belief argument in Chapter 6.
- **Transportability and external validity beyond one naming sentence.** Chapter 9.
- **Anything read past the recorded stop pages.** `deaton2016rct` runs to 70 pages and only 7–11 were read; the dossier says so.

## Known unobtainable

- The **published** version of Deaton and Cartwright, *Social Science & Medicine* 210 (2018): 2–21, could not be retrieved. What was read is NBER Working Paper 22595, September 2016, revised October 2017, which states on its cover that it has not been peer-reviewed. Cited as the working paper, with that status recorded.
- **Holland (1986)**, "Statistics and Causal Inference", the standard citation for the fundamental problem of causal inference, was not obtained. The chapter states the problem from `hernan2019whatif` instead and makes no claim about Holland's contents.
- **Rubin (1976)** remains unobtained, as recorded since Chapter 4.
