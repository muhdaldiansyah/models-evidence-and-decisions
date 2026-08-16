# Source note: `pearl2009causal`

## Citation

Pearl, Judea. 2009. “Causal Inference in Statistics: An Overview.” *Statistics Surveys* 3: 96–146. DOI 10.1214/09-SS057.

## Verification status

Verified direct source for the Chapter 1 association/intervention/counterfactual distinction at introductory depth.

The published reprint was inspected through the UCLA author-hosted copy. Journal metadata, volume, pages, and DOI are printed on the article itself.

## Role in Chapter 1

- supports distinguishing associational/statistical questions from causal questions about changing conditions;
- supports the warning that association alone does not establish what would happen under an intervention;
- supports treating intervention and counterfactual questions as causal rather than merely distributional questions;
- supports reserving `counterfactual` for causal alternative-outcome reasoning rather than using it as a loose synonym for any hypothetical scenario;
- supports deferring the notation and assumptions required for formal causal analysis to Chapter 7.

## Verified locators

- Abstract, printed p. 96: causal inference is described as combining data and assumptions to answer intervention, counterfactual, and mediation queries.
- §1, printed pp. 97–98: causal questions require knowledge or assumptions about the data-generating process beyond the observed distribution alone.
- §2.1, printed p. 99, “The basic distinction: Coping with change”: standard statistical analysis handles association and probabilities under unchanged conditions; causal analysis addresses changes induced by treatments or external interventions.
- §2.2, printed pp. 99–100: associational concepts are defined from the joint distribution, whereas causal concepts require more than that distribution.
- §2.4, printed p. 101: potential-outcome and intervention notation are presented as ways to express causal rather than associational questions.
- §3.4, printed pp. 119–120: formal counterfactual analysis in structural models.

## Chapter 1 use and cautions

Chapter 1 uses only the high-level structural lesson. It does not adopt Pearl's formal notation, causal graphs, structural equations, do-calculus, or identification criteria at this stage.

Do not overstate the source as saying observational data can never contribute to causal inference. The Chapter 1 claim is narrower: **association alone is insufficient for an intervention-effect conclusion; causal conclusions require additional causal assumptions or design information.**

Do not present intervention and counterfactual as four-way taxonomy boxes separate from one another. Pearl's formal treatment relates intervention distributions and counterfactual outcomes closely; Chapter 1's separate prompts are a pedagogical diagnostic device.
