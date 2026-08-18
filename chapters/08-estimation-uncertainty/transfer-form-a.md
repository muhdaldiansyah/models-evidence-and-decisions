# Chapter 8 Cold-Transfer Task — Form A

Status: reader-delivery copy. Governed by `spec.md` (Transfer target) and `transfer.md`.

Without consulting the Chapter 8 chapter text, the water case, or the rubric, work the situation below.

**You are the reviewer.** Produce a written examination of the reported result.

Every fact you need is supplied. Do not look anything up; if something you need is missing, say what it is and whether it would change your answer.

Current pilot target: **50 minutes**. This is a design parameter pending pilot evidence, not a universal standard.

## The report

A regional electricity distributor changed its transformer loading regime four years ago. An engineering review has examined whether failures have increased.

The review's summary reads:

> **Across 30 substations, the mean change in transformer failures is +3.1 per substation per year (95% interval −0.04 to +6.24). This is not statistically significant, so there is no evidence that the new loading regime has increased failures. The failure model reproduces the observed record to within 4% over the fitting period, confirming that it is sound.**

The asset committee is deciding whether to reverse the loading regime.

## The record

Change in failures per substation per year, before the regime change against after:

| | Substations | Mean change | Spread | Standard error |
|---|---:|---:|---:|---:|
| All substations | **30** | **+3.1** | 8.4 | 1.53 |

## Four supplied facts

**1. Four substations were refurbished.** During the same four years, four of the thirty had major refurbishment unrelated to the loading regime, replacing transformers that were near end of life. Excluding those four gives a mean change of **+4.2** across 26 substations, spread 8.0, standard error 1.57.

**2. Eleven substations have incomplete records.** Failure logging was inconsistent at eleven sites before the regime change. Restricting to the nineteen with complete records throughout gives a mean change of **+3.8**, spread 7.6, standard error 1.74.

**3. Substations differ greatly in size.** They carry between two and eleven transformers each, and each substation contributes one number to the average regardless. Weighting by transformer count gives a mean change of **+3.5**, spread 8.2, standard error 1.50.

**4. The failure model was built from this record.** The model that produces the 4% figure was fitted to the same four years of failure data it is being checked against. It has not been used to predict anything it was not fitted to.

For reference, at these sample sizes the conventional threshold is crossed when the mean is roughly **two standard errors** from zero.

## Produce

Write a response containing all seven items.

1. **State what the +3.1 is an estimate of.** Be specific about the quantity — what population, what comparison, over what window. Where the report does not say, choose and mark your choice.
2. **What does the interval −0.04 to +6.24 cover?** And list at least four things it does not.
3. **The report's second sentence.** Say exactly what is wrong with "not statistically significant, so there is no evidence".
4. **Work the four analyses.** For each of facts 1 to 3 and the headline, say whether it crosses the conventional threshold, and set the four estimates side by side.
5. **Say what the dichotomy has done here.** Compare the four estimates with the four verdicts, and say which of the four analyses is arguably the most defensible.
6. **The model check.** Say why the 4% figure establishes less than the report claims, and propose one check that **could have failed**.
7. **Rewrite the summary.** Four short paragraphs, reporting what the record supports, with everything it is conditional on.

**Stop when your response is complete. Do not open the rubric until then, and do not open Form B at all.**
