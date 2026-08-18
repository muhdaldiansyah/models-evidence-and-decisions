# Chapter 8 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0015-chapter8-estimation-terminology-and-notation.md`.

## 1. Drafting objective

40 pages / 8 learning hours that leave the reader able to say what a computed number is conditional on, what its interval does and does not cover, and why a threshold verdict throws away almost everything the number contains.

The chapter must **defeat** thirteen named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | The Number You Were Told Not to Trust | 2 | 0.30 |
| 2 | Estimand, Estimator, Estimate | 5 | 1.00 |
| 3 | Everything You Compute Is Conditional on a Model | 6 | 1.20 |
| 4 | How Uncertain, and About What? | 6 | 1.25 |
| 5 | The Threshold Ritual | 6 | 1.25 |
| 6 | Four Defensible Analyses | 5 | 1.05 |
| 7 | Checking the Assumptions You Were Not Interested In | 6 | 1.20 |
| 8 | Cold-Start Practice and Retrieval | 4 | 0.75 |

Roughly 360 words per page — about **14,400 words**. The largest chapter in the book by pages; do not rebalance without recording the reason.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- Bold **only** for case quantities and the first appearance of a controlled term.
- **No new notation.** Ordinary arithmetic and an interval as two numbers.
- **No quotation from `greenland2016misinterpretations` may contain a comparison symbol.** Paraphrase and say so.
- Every number the chapter reports carries what it is conditional on.

### Register discipline

Three failure modes specific to this chapter.

**Sounding anti-statistical.** The chapter criticises a ritual, not a discipline. Principle 1 says P values can indicate incompatibility with a model, and the manuscript must carry that.

**Sounding like a statistics course.** No procedures, no distributions, no derivations. Every idea lands on the anchor's numbers.

**Becoming a survey.** Eight named topics, one claim. If a passage cannot be traced back to the spine, it is a survey paragraph and should be cut or routed forward.

## 4. Reader-facing sequence

Per `../../decisions/0008`. No new case; the anchor is Chapter 6's unjustified spread.

Self-explanation pauses: exactly three — §4 (why the answer went down), §5 (what the dichotomy destroyed), §7 (which check could have failed).

## 5. Section 1 — The Number You Were Told Not to Trust

**Beats.**

1. Quote Chapter 6's own admission: the spread "is supplied and is not derived from anything".
2. Note that Chapter 6 nonetheless used it and got about **77%**, and told the reader the stability was about the arithmetic.
3. State this chapter's job: go and get the records.
4. **Opening task, about six minutes.** Where should the ±0.6 have come from, and what would you do with what you found? Preserve unscored.
5. Name the position in the four-step spine — step 4, Estimate — and that Chapter 7's *not identified* verdict still stands and is not being revisited.
6. Close on the promise the chapter cannot keep as stated: Chapter 6 said deferred symbols belonged here. Say plainly that the material belongs here and the symbols do not, and give the reason. Per `../../decisions/0015` clause 2.4.

## 6. Section 2 — Estimand, Estimator, Estimate

**Beats.**

1. Three words, three jobs. What you want to know, how you work it out, what you got.
2. The four confusions table from `research-01` §2.
3. **Three estimator properties**: bias, variance, consistency — all properties of the **procedure**.
4. **"This is an unbiased estimate" is a category error.** Work it.
5. **Chapter 3's parallel**: a calibrated instrument is not a correct reading.
6. **Third appearance of the ensemble-property shape.** Calibration over a record (Ch 6), balance over replications (Ch 7), estimator properties over repeated application (Ch 8). Name it; do not tabulate it.
7. **The `consistency` collision, announced** — fourth such announcement in the book. Both senses stated.
8. **`confidence` declined**, with the source's reason quoted [@greenland2016misinterpretations, p. 339]. The book writes `interval estimate`; `confidence interval` named once.
9. **Reader task.** Label three statements.

## 7. Section 3 — Conditional on a Model

**Beats.**

1. **The spine, quoted in full** [@greenland2016misinterpretations, p. 339]. Three claims unpacked.
2. The consequence that reorganises the chapter: analytic conduct is **inside** the model.
3. Compute the anchor's mean error: **+1.8 ML** over 24 events. List what that number assumes.
4. **When the number is surprising, you have learned that something is wrong and not what** [@greenland2016misinterpretations, p. 339]. Chapter 5's structure, sharper.
5. **And a large one says very little** [@greenland2016misinterpretations, p. 339].
6. The eight-topics-one-claim mapping, in prose, so the reader can see the chapter's shape.
7. **Reader task.** Write down five assumptions the +1.8 depends on that are not statistical assumptions.

## 8. Section 4 — How Uncertain, and About What?

**Beats.**

1. Compute the standard error: `2.4 ÷ √24 = 0.49`. Then the interval: **+0.84 to +2.76**.
2. **What it covers**: how much the average of 24 errors would move on another 24 events from the same process.
3. **What it does not cover** — the enumeration, drawn from Part I: Chapter 1's conditionality, Chapter 4's residual, Chapter 5's missing spill term, and which events got logged.
4. `meng2018paradox` p. 687 for the general form.
5. **A reported interval is "a range between two numbers"** [@greenland2016misinterpretations, p. 343]. Not a 95% chance of containing anything.
6. **The four corrections table.** 77%, 62%, over 99%, 85%.
7. **Self-explanation pause 1.** Why did widening the interval move the answer down?
8. The answer: the threshold sits below the central forecast. Draw it out.
9. **Correcting one thing was worse than correcting neither**, and the reassuring direction is the one most analysts reach for.
10. **Fifth appearance of the *more X* shape**, in prose. Chapter 7 owns the table; do not restate it.
11. **Reader task.** Both one-sided corrections, and the direction explained.

## 9. Section 5 — The Threshold Ritual

**Beats.**

1. What a P value is: a compatibility summary [@greenland2016misinterpretations, p. 339], quoted.
2. **The six ASA principles**, quoted in full [@asa2016pvalue]. Say the document is the association's press release and that the article was not obtained.
3. **The dichotomy, named** [@greenland2016misinterpretations, p. 339].
4. **Four misinterpretations**, each with its book analogue:
   - not a hypothesis probability (p. 340) → Chapter 6's inversion;
   - small does not mean the hypothesis is false (p. 341, paraphrased) → Chapter 5;
   - large does not mean no effect (p. 341, paraphrased) → Chapter 5's absence-of-failure;
   - a reported interval is a range between two numbers (p. 343) → Chapters 6 and 7's ensemble shape.
5. **Intervals do not escape it** [@greenland2016misinterpretations, p. 344]. Quote. Close the escape route explicitly.
6. **Overlapping intervals are not agreement** — the source's worked pair, `(1.04, 4.96)` and `(4.16, 19.84)`, testing at `P = 0.03`.
7. **Matrixx, once**, as reported at [@greenland2016misinterpretations, p. 347].
8. **The mechanism is institutional** [@asa2016pvalue], Utts on the file-drawer effect.
9. **The four guidelines**, quoted [@greenland2016misinterpretations, p. 347].
10. **The closing judgment** [@greenland2016misinterpretations, p. 348]: "especially pernicious statistical practice".
11. Say what the chapter is **not** claiming: not that P values are worthless, not that a replacement is agreed.

## 10. Section 6 — Four Defensible Analyses

**Beats.**

1. Frame: nobody cheated, and that is the point.
2. **The four analyses table.** `+1.8`, `+2.4`, `+1.1`, `+2.0`.
3. Two of the choices are arguably **required** — and requiring both leaves a handful of events.
4. **Three cross the threshold, one does not.**
5. **Self-explanation pause 2.** What did the dichotomy destroy?
6. The answer: the four estimates agree in direction and order of magnitude. The disagreement is manufactured.
7. **This is why analytic conduct is inside the model**, not beside it — §3's spine arriving on the anchor.
8. **Preregistration is one device with limits, not a solution.** Say what it does and does not fix; the post-SCADA question could not have been settled in advance by anyone who did not yet know the SCADA changed.
9. **Silberzahn et al. (2018) could not be obtained**; say the demonstration is the book's own and claim nothing about that study.
10. **Reader task.** Produce a fifth defensible analysis and predict its verdict.

## 11. Section 7 — Model Checking

**Beats.**

1. Frame: checking the assumptions you were not interested in.
2. **Fit is not a check** — Chapter 5 established it, and the manuscript must not undo it.
3. **The split-half check**, worked: 14 post-SCADA at **+1.1** against 10 earlier at **+2.78**, with the arithmetic shown.
4. What it establishes and what it does not — a Chapter 7 caution, one sentence.
5. **The honest check: hold out data the model was not fitted to.** Reuse `gneiting2007scoring` p. 359's calibration and sharpness, unchanged.
6. **Self-explanation pause 3.** Which of the checks proposed could actually have failed?
7. Guideline (b), quoted [@greenland2016misinterpretations, p. 347], as the summary of the whole section.
8. **Sensitivity analysis arrives**, as Chapter 5 promised — a model-checking device, not criticism, with the Chapter 5 limit restated in one line and decision-theoretic robustness routed to Chapter 12.
9. **Planted-defect diagnosis task.** Five defects per `spec.md`. Feedback linked only after production.

## 12. Section 8 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 answer. Compare, do not score. Name the common patterns.
2. **Cold transfer.** Both forms listed, one assigned.
3. **Retrieval from memory** — the procedure, ten steps.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form.
6. Short diagnostic if the transfer went badly.
7. **What this chapter did not give you.**
8. Close: Chapter 9 asks what happens when there is more than one body of evidence, and when the answer has to move to a population it did not come from.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production.

## 13. What the draft may not do

- Introduce any notation beyond what Decisions 0013 and 0014 permit.
- Derive an estimator or an interval, or state a formula for a standard error.
- Teach a test procedure, a distribution, or a power calculation.
- Teach regression as a technique, or Bayesian estimation.
- Quote `greenland2016misinterpretations` with a comparison symbol in the quotation.
- Cite Wasserstein and Lazar (2016), or characterise the ASA statement's elaborating paragraphs.
- Cite Matrixx directly, or characterise its reasoning.
- Claim anything about Silberzahn et al. (2018) or about the replication literature.
- Present P values as worthless, or claim a replacement is agreed.
- Present preregistration as a solution.
- Re-estimate anything Chapter 7 declared not identified.
- Restate Chapter 7's four-row table, or Chapter 5's five-row table.
- Recommend an action for the utility.
- Present synthetic case values as typical, standard, or recommended.
