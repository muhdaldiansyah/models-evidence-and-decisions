# Decision 0015: Chapter 8 Estimation Terminology and Notation

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `readiness-audit.md` §10 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 8 entries in `canon/terminology.md` are built on this record and inherit its provisional status.

**Clause 2 declines to extend the notation exception, and in doing so departs from a promise Chapter 6 made to the reader.** That is this record's most consequential clause and it is unlike its two predecessors: 0013 opened an exception, 0014 extended it, and 0015 refuses.

Evidence base: `../chapters/08-estimation-uncertainty/research-01-estimand-estimator-estimate.md`, `research-02-what-a-number-is-conditional-on.md`, `research-03-thresholds.md`, `research-04-uncertainty-checking-examples.md`.

## Decision

Chapter 8's organizing claim is:

> Every number you compute is a statement about a whole set of assumptions, only one of which you were interested in — and the set includes how you conducted the analysis.

### 1. Eight topics, one chapter

**1.1** `README.md`'s core competence for Chapter 8 names eight things: likelihood, estimation, regression, uncertainty quantification, predictive evaluation, measurement-error reasoning, analytic-flexibility awareness, and model checking.

**1.2** The chapter does **not** allocate five pages to each. Each is presented as a consequence of the organizing claim, per the mapping in `research-02` §5. A chapter organized as eight surveys would violate `README.md`'s Intellectual Principle, which forbids the book from becoming a tour of specialist machinery.

**1.3** The spine is sourced: [@greenland2016misinterpretations, p. 339] states that a computed result tests the entire model, and that the model's assumptions include "assumptions about the conduct of the analysis". [@asa2016pvalue] principle 4 states the same requirement institutionally.

**1.4** Consequence for scope: **analytic flexibility is not a research-ethics topic in this book.** It is an assumption inside the statistical model, on the same footing as independence, and the manuscript treats it there.

### 2. Notation — the exception is declined

**2.1** Chapter 6 told the reader: "If something in this chapter seems to want a symbol that is not on that list, it belongs to Chapter 8" (`chapters/06-probability-simulation/chapter.md`).

**2.2** **Chapter 8 introduces no new notation.** Permitted: everything Decisions 0013 and 0014 already permit — the conditioning bar, odds, `do(·)`, inline arrows — plus ordinary arithmetic and an interval written as two numbers.

**2.3** Not permitted: summation or integration; distributions written as functions; random variables as symbols; estimator notation of any kind; hats, tildes, or subscripted parameters; any test statistic; any formula for a standard error.

**2.4** **The refusal is stated to the reader**, because Chapter 6 promised otherwise and a silent reversal would be a broken promise rather than a change of plan. The manuscript says: Chapter 6 was right that the *material* belongs here; the symbols turn out to be needed for **deriving** estimators, and this chapter derives none.

**2.5** Rationale. Everything the chapter teaches is demonstrable on the anchor's actual numbers — a mean is a mean, a spread is a spread, an interval is two numbers. Adding notation would buy nothing the chapter uses and would cost the reader the register the book has maintained for eight chapters.

**2.6** The machinery that genuinely needs the symbols — deriving estimators, deriving interval formulas, likelihood as an object to maximise — is **depth curriculum**, and the manuscript says where it lives rather than gesturing at it.

### 3. Estimand, estimator, estimate

**3.1** The three are separated at concept depth and never blurred: `estimand` is what you want to know, `estimator` is the procedure, `estimate` is the number you got.

**3.2** Three estimator properties are named — **bias**, **variance**, **consistency** — and all three are taught as properties of the **procedure**, never of the number.

**3.3** "This is an unbiased estimate" is named as a category error, per `research-01` §4.

**3.4** This is the **third** appearance of the ensemble-property shape: calibration over a record (Chapter 6), balance over replications (Chapter 7), estimator properties over repeated application (Chapter 8). The manuscript names the recurrence once.

### 4. Two words

**4.1** `consistency` collides with Chapter 7's causal condition. **Announced once**, both senses stated, as Chapter 6 handled `calibration` and Chapter 5 handled `validation`. Fourth such announcement in the book.

**4.2** `confidence` is **declined for the book's own prose.** [@greenland2016misinterpretations, p. 339] records that the statistical usage is at odds with ordinary English. The book writes `interval estimate`, introduces `confidence interval` once as the term the reader will meet everywhere else, and never writes `confidence` alone in the technical sense.

**4.3** This mirrors Chapter 3's disposition toward `validation` — decline the word, name why, route the reader to what they will encounter.

### 5. Thresholds

**5.1** The six ASA principles are quoted in full from [@asa2016pvalue], with the record stating that the document read is the association's press release and that the underlying article was not obtained.

**5.2** A P value is taught as a **compatibility summary**, in the source's own framing [@greenland2016misinterpretations, p. 339].

**5.3** Four misinterpretations are taught, each paired with a book analogue the reader already has. Where the source's wording carries comparison symbols, the manuscript **paraphrases and says it is paraphrasing** — per the extraction rule recorded in `../sources/greenland2016misinterpretations.md`.

**5.4** The manuscript states that reporting intervals does not escape the ritual, citing [@greenland2016misinterpretations, p. 344].

**5.5** The chapter does **not** present P values as worthless, does not claim the field has agreed on a replacement, and does not teach any test procedure, distribution, or power calculation.

**5.6** Matrixx Initiatives v. Siracusano is cited **as reported at** [@greenland2016misinterpretations, p. 347] and used once.

### 6. Uncertainty

**6.1** An interval estimate is taught as covering **sampling variability under a stated model**, and the manuscript enumerates what it does not cover using Part I's own findings.

**6.2** **"A wider interval is more conservative" is refuted numerically**, not asserted. The anchor shows that widening alone moves the breach probability from 77% to 62% — down — because the threshold sits below the central forecast.

**6.3** Fifth appearance of the *more X does not fix B* shape. Chapter 7 owns the four-row table; Chapter 8 adds its row **in prose**, not by restating the table.

### 7. Analytic flexibility

**7.1** Demonstrated on the anchor: four defensible analyses of one record, four estimates, three crossing the conventional threshold and one not.

**7.2** The manuscript makes the point that **the four estimates do not disagree** — the disagreement is manufactured by the dichotomy.

**7.3** Preregistration is named as one device with real limits, **not** as a solution.

**7.4** Silberzahn et al. (2018) could not be obtained; the chapter makes no claim about it. Recorded in `research-plan.md`.

### 8. Vocabulary

**8.1** Introduced here: `sampling variability`, `standard error`, `interval estimate`, `P value`, `statistical significance`, `analytic flexibility`, `model checking`.

**8.2** Closed here, from `Definition status: TODO` since Chapter 1: `estimator`, `estimate`.

**8.3** `statistical significance` is registered **as a hazard**, with the source's closing characterisation attached.

**8.4** `confidence interval` is registered as an alias under `interval estimate`, not as a preferred term.

### 9. What Chapter 8 does not do

- Derive any estimator or interval.
- Teach any test procedure, distribution, or power calculation.
- Teach regression as a technique; it appears as a model whose assumptions are under discussion.
- Teach Bayesian estimation, or reopen Chapter 6's declined argument about what probability is.
- Teach multiple-comparison corrections.
- Combine studies or transport results — Chapter 9.
- Treat decision-theoretic robustness — Chapter 12.
- Treat gaming of reported estimates — Chapter 15.
- Treat post-deployment monitoring — Chapter 17.
- Re-estimate anything Chapter 7 declared not identified.
- Recommend an action for the utility — Chapter 11.

## Sources promoted

`greenland2016misinterpretations` and `asa2016pvalue` are new to `references.bib`, each with a source note recording exactly what was read and what was not. `jcgm2012vim`, `meng2018paradox`, and `gneiting2007scoring` are reused as already verified.

## Known gaps carried forward

1. **Wasserstein and Lazar (2016) not obtained.** The six principles are cited from the ASA's press release; the elaborating paragraphs are not characterised.
2. **Silberzahn et al. (2018) not obtained** after four attempts.
3. **`greenland2016misinterpretations` read at pp. 337, 339–341, 343–344, 346–348 only.** Power is unread beyond guideline (c).
4. **Matrixx Initiatives v. Siracusano not read**; reported only.
5. **Rubin (1976) still unobtained**, as since Chapter 4.
6. The **Chapter 8 case is the water anchor's eighth recurrence**, and Chapter 1's Gate 1 remains open.

## No architecture change

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields.

**It does, however, decline a commitment made in a drafted manuscript.** Chapter 6 told readers that deferred symbols belonged to Chapter 8. Clause 2 keeps the material and declines the symbols, and clause 2.4 requires the manuscript to say so rather than let the reader notice. If the author prefers the promise kept, Chapter 8 §§2 and 4 would need rewriting and Decision 0013 clause 2.3's list would need revisiting.
