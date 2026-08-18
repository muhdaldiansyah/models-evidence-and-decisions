# Chapter 4 — Diagnosis Feedback

Open this file only **after** you have written your diagnosis of all five defects in §6, and after you have placed the four situations.

Your wording will differ; what matters is whether you found the same fault.

## 1. "Meter records for 100% of connections, so representative of town water use"

**Defect.** Complete coverage of one population is being read as representativeness for a different population.

**What it costs.** The utility has 100% of **billed connections**. It does not have 100% of the **water**. Firefighting draw, mains flushing, tank cleaning, and every leak in the network are all water use and none has a connection. The register is complete for what it covers and silent about a category it was never designed to include.

**Repair.** Name the population the records actually cover, and then ask whether that population is the one the question is about. "100% of billed connections" is a true and useful sentence. "Representative of town water use" is not.

**Note.** The word *representative* is doing the damage. Completeness is a property of coverage; representativeness is a relationship between what was recorded and the question. They are not the same claim and the first does not imply the second.

## 2. "Missing readings comprised 2% of rows and were dropped"

**Defect.** Missingness is being treated as a tidying step rather than as an assumption about the observation process.

**What it costs.** Two per cent is a statement about *how many* are missing and says nothing about *which*. In this case the Millbrook gaps are nine-elevenths concentrated in the two hottest weeks of the year, because the meter's failure mode is heat-related. Dropping them removes precisely the days the drought analysis is about.

**Repair.** Ask the question: is whatever caused these to be absent related to what the values would have been? If the answer is unknown, say so; if the answer is yes, dropping is not available and neither is any simple fill.

**Note.** The size of a gap is nearly irrelevant. A one-per-cent gap concentrated on the decisive cases does more damage than a twenty-per-cent gap scattered at random.

## 3. "Our most reliable source — eleven years of continuous readings"

**Defect.** Duration is being read as data quality.

**What it costs.** Eleven years of records produced by one observation process is eleven years of the same five decisions. Every year of it is missing firefighting draw, missing a Hillcrest meter, filling gaps the same way, discarding fine detail after ninety days, and combining three quantities on the return.

Worse, the length actively encourages confidence. Larger datasets produce narrower intervals around estimates whose defect nothing has touched.

**Repair.** Ask which of the five stages more years would change. If the answer is none, the additional years buy precision around an unchanged bias.

**Note.** This is not an argument against long time series. It is an argument against treating length as evidence of anything other than length — and a reminder that an observation process which changed partway through makes a long series several short ones stacked together.

## 4. "There are no nulls, so the data is clean"

**Defect.** Absence of a visible gap is being read as absence of a gap.

**What it costs.** Every category that was never eligible produces no null at all. Firefighting draw has no row, no blank, and no flag. Neither does anything else the billing system was not built to see. A dataset can be free of nulls and missing an entire class of the thing it is supposed to describe.

**Repair.** Ask what could never have appeared, which is a question about the eligibility rule rather than about the data. Then ask whether any of it matters for the quantity at issue.

**Note.** This is the chapter's central irony and the reason §5 exists. Every automated data-quality check ever written operates on rows that exist. The most damaging gaps produce no rows to check.

## 5. "With a 94% response rate, nonresponse bias is negligible"

**Defect.** A response rate is being read as a measure of bias.

**What it costs.** The rate counts **how many** responded and says nothing about **who**. In the survey-research literature, "response rates lack validity in that there is not even a moderate correlation with nonresponse bias" — and bias attaches to a particular quantity being estimated rather than to a survey as a whole. A 94% rate can carry serious bias for one estimate and none for another, from the same dataset.

**Repair.** Ask whether the six per cent who did not respond are likely to differ **on the quantity being estimated**. That question has an answer, sometimes a knowable one; the response rate does not answer it.

**Note.** Be careful of the over-correction. This does not mean nonresponse is harmless or that response rates should not be reported. A low rate is a reason to investigate. It is just not a measurement of the harm.

## The four placements

| Situation | Placement |
|---|---|
| Zone meters installed where billing revenue justified the capital | **Chapter 4** — institutional purpose |
| Fifteen-minute readings discarded after ninety days | **Chapter 4** — retention |
| The regulatory return has one line for non-revenue water | **Chapter 4** — reporting |
| Operators rescheduled flushing once the residual began appearing in management reports | **Chapter 15** |

What distinguishes the fourth is not that it is deliberate. Retention policies are deliberate too, and so is the return form.

It is that the recording process **changed in response to being used**. In the first three, the process was set up for reasons that had nothing to do with your analysis and stayed put. In the fourth, your analysis became an input to the process it was analysing.

Everything in this chapter assumes a recording process that is not reacting to you. That assumption is usually reasonable and is worth knowing you have made, because the moment a number starts being watched, the assumption can fail without announcement — which is Chapter 15's subject.

## After you have compared

Do not simply correct your answers.

Pick the defect you got most wrong and write two sentences on **what made it sound reasonable**. All five of these appear verbatim in real documents written by capable people, and every one of them reads as diligence rather than as error.
