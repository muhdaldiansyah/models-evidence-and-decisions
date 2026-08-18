# Source note: `gneiting2007scoring`

## Citation

Gneiting, Tilmann, and Adrian E. Raftery. 2007. "Strictly Proper Scoring Rules, Prediction, and Estimation." *Journal of the American Statistical Association* 102 (477): 359–378. DOI 10.1198/016214506000001437.

## Verification status

Verified direct source. The published article was inspected. Its first page prints *Journal of the American Statistical Association*, March 2007, Vol. 102, No. 477, Review Article, the DOI, and the American Statistical Association copyright line. Authors are identified as of the University of Washington.

Printed pages **359–360** were read in full. Pages 361–378 were **not** inspected in this pass and may not be cited.

## Role in Chapter 6

This supplies two things Chapter 6 cannot do without.

**Propriety** — the reason a good scoring rule cannot be gamed, which is the deep answer to "why should I report what I actually believe?"

**The calibration/sharpness split** — which separates two things readers merge, and which turns "was that a good forecast?" into a question with a structure.

It also lets the chapter reference Brier's contribution accurately without citing a source that was not obtained.

## Verified locators

- p. 359, abstract: "Scoring rules assess the quality of probabilistic forecasts, by assigning a numerical score based on the predictive distribution and on the event or value that materializes. A scoring rule is proper if the forecaster maximizes the expected score for an observation drawn from the distribution F if he or she issues the probabilistic forecast F, rather than G ≠ F. It is strictly proper if the maximum is unique."
- p. 359, §1: "the goal of probabilistic forecasting is to maximize the sharpness of the predictive distributions subject to calibration."
- **p. 359, §1, the split: "Calibration refers to the statistical consistency between the distributional forecasts and the observations, and is a joint property of the forecasts and the events or values that materialize. Sharpness refers to the concentration of the predictive distributions and is a property of the forecasts only."**
- p. 359, §1, on what scoring is for: "In terms of elicitation, the role of scoring rules is to encourage the assessor to make careful assessments and to be honest."
- p. 359, §1: "In terms of evaluation, scoring rules measure the quality of the probabilistic forecasts, reward probability assessors for forecasting jobs, and rank competing forecast procedures."
- p. 359, §1, propriety stated: "The forecaster has no incentive to predict any P ≠ Q and is encouraged to quote his or her true belief, P = Q, if S(Q, Q) ≥ S(P, Q) with equality if and only if P = Q. A scoring rule with this property is said to be strictly proper. If S(Q, Q) ≥ S(P, Q) for all P and Q, then the scoring rule is said to be proper."
- pp. 359–360: "Propriety is essential in scientific and operational forecast evaluation; and we present a case study that provides a striking example of the potential issues that result from the use of intuitively appealing but improper scoring rules."
- p. 359, §1: meteorologists refer to this task as "forecast verification"; in a Bayesian context scores are often referred to as utilities.
- **p. 360, on provenance: "The term *proper* was apparently coined by Winkler and Murphy (1968, p. 754), whereas the general idea dates back at least to Brier (1950) and Good (1952, p. 112)."**
- p. 359, key words include: Brier score; Calibration is discussed alongside sharpness; Continuous ranked probability score; Scoring rule; Strictly proper.

## Chapter 6 use and cautions

**Propriety is the concept, not the formula.** Chapter 6 should teach that a proper scoring rule is one under which your best expected score comes from stating what you actually believe — and that this is why scoring works as an honesty mechanism rather than merely as a report card. The mathematics on pp. 360 onward is depth-curriculum material.

**Calibration and sharpness must not be merged.** The source is precise about why they differ: calibration is a **joint property** of forecasts and outcomes; sharpness is a property of **the forecasts alone**. A forecaster who always says "50%" can be perfectly calibrated and useless. That consequence follows from the definitions and is the book's own way of putting it.

**Brier 1950 may be referenced only as reported here.** That paper was **not obtained** — it sits behind a publisher paywall. Chapter 6 may say the idea dates at least to Brier, citing p. 360 of this source, and may **not** cite Brier directly or attribute wording to it.

**Do not write the notation.** S(P, x), S(P, Q), and the propriety inequality belong to the source, not to this chapter, which teaches no notation.

**Do not cite beyond p. 360.**

**Do not extend to estimation.** The article's second half concerns optimum score estimation, cross-validation, and interval scores. Estimation is Chapter 8.

**Domain.** Written for statisticians, with meteorological and econometric applications. The book's use for ordinary analytical forecasting is an extension.
