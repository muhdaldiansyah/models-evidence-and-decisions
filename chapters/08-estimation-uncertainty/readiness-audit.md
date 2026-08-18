# Chapter 8 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 8: **Estimation, Uncertainty, and Model Checking** — the third chapter of Part II.

**Process note.** As in Chapters 3–7, this audit was written alongside its research. Findings taken from sources are marked. Every locator was taken from reading the document directly.

Current architecture from `README.md` and `spec.md`:

- central question: **What does finite evidence say, with what reliability?**
- core competence: **Use likelihood, estimation, regression, uncertainty quantification, predictive evaluation, measurement-error reasoning, analytic-flexibility awareness, and model checking without reducing evidence to threshold rituals.**
- target: 40 pages / 8 serious learning hours — **the largest chapter in the book by pages**, overtaking Chapter 7.

## 1. Readiness verdict

**Drafting-ready after adjudication**, with one structural problem that no previous chapter has had.

**The core competence names eight things.** Likelihood, estimation, regression, uncertainty quantification, predictive evaluation, measurement-error reasoning, analytic flexibility, and model checking. Each is a subject with textbooks. Forty pages divided eight ways is five pages each, which is enough for none of them.

A chapter that tried to cover eight topics at five pages apiece would be a survey, and a survey is exactly what `README.md`'s Intellectual Principle forbids — the book is an integrated architecture, not a tour of specialist machinery.

**So the chapter needs a spine that makes the eight into consequences of one thing**, and research found one.

> "In logical terms, the P value tests all the assumptions about how the data were generated (the entire model), not just the targeted hypothesis it is supposed to test (such as a null hypothesis). Furthermore, these assumptions include far more than what are traditionally presented as modeling or probability assumptions—they include assumptions about the conduct of the analysis, for example that intermediate analysis results were not used to determine which analyses would be presented." [@greenland2016misinterpretations, p. 339]

**Everything you compute is a statement about a whole set of assumptions, only one of which you were interested in — and the set includes how you conducted the analysis.**

From that one claim the eight follow. An estimate is conditional on the model. An interval is conditional on the model. Analytic flexibility is not a separate ethics topic; it is *inside* the model's assumptions. Model checking is checking the assumptions you were not interested in. Predictive evaluation is checking them against something they were not fitted to. Measurement error is one of them. And the threshold ritual is the practice of throwing away the number's actual content.

That is one chapter, not eight.

## 2. Unique-job hypothesis

> Teach readers that a computed result is a statement about an entire model — including how the analysis was conducted — and that reporting it as a fact about the world, or as a verdict against a threshold, discards almost everything it contains.

The reader who finishes Chapter 8 should be able to take an estimate with an interval, say what the interval does and does not cover, name three defensible analyses that would have produced different numbers from the same records, and refuse a significance verdict without being merely contrarian about it.

## 3. What earlier chapters have promised

| Promised in | Text | Settled by |
|---|---|---|
| `04/chapter.md` L491 | ignoring missingness is permitted under conditions, "the conditions themselves are Chapter 8's business" | §3, briefly |
| `06/chapter.md` L149 | "If something in this chapter seems to want a symbol that is not on that list, it belongs to Chapter 8." | **§1, and the answer is no — see §5 below** |
| `07/chapter.md` L55, L1075 | step 4 of the four-step spine | §1 |
| `07/chapter.md` L179 | `estimator` and `estimate` get their formal treatment here | §2 |
| `07/chapter.md` L665 | the statistical sense of `consistency` | §2, with the collision announced |
| `05/chapter.md` L702, L713 | "given this model, how uncertain is the answer?"; sensitivity analysis belongs here | §4, §7 |
| `canon` | `estimator` and `estimate` at `Definition status: TODO` since Chapter 1 | §2 |
| `canon` | measurement-error correction, missingness methods, structural-uncertainty quantification, the technical sense of `confidence` | §3, §4 |

## 4. Neighbouring-chapter boundaries

### Chapter 7 — what precedes

Chapter 7 ended with a verdict of **not identified** for the pump question. Chapter 8 cannot simply estimate it, and pretending otherwise would undo the previous chapter.

**The anchor must therefore be a quantity that *is* identified**, and one is sitting in the open: Chapter 6 put a spread of ±0.6 ML on daily demand, said in terms that the spread was supplied and justified by nothing, and used it to compute a breach probability. Chapter 8's job is to earn that spread from records.

That is the cleanest possible opening. The chapter repairs a defect the book itself flagged two chapters ago, which is a stronger motivation than any new case could supply.

### Chapter 9 — synthesis and transport

Combining several studies, and moving a result to a new population, are Chapter 9's. Chapter 8 estimates one quantity from one body of evidence. The line should be stated once.

### Chapter 12 — robustness and optimization

Sensitivity analysis appears in both. Chapter 5 already said sensitivity analysis is not criticism and routed it here; Chapter 8 should use it as a model-checking device and route decision-theoretic robustness to Chapter 12.

### Chapter 15 — gaming

If reporting an estimate changes behaviour, that is Chapter 15's. Not here.

### Chapter 17 — monitoring

Checking a model after deployment is Chapter 17. Chapter 8 checks it before.

## 5. The notation question, and a recommendation to decline

Chapter 6 told the reader that anything wanting a symbol beyond the conditioning bar "belongs to Chapter 8". That is a promise on the record and this chapter has to answer it.

**The recommendation is to decline the extension.**

Everything in §§1–8 can be taught on the anchor's actual numbers. An average is an average; a spread is a spread; an interval is two numbers. The material Chapter 6 deferred — summation, distributions written as functions, estimator notation — is needed for *deriving* estimators, and this chapter does not derive any.

That makes Decision 0015 the first notation decision in three chapters that **refuses** rather than extends, and the refusal has to be stated to the reader, because Chapter 6 promised otherwise.

The honest framing: Chapter 6 said the *material* belonged here, and it does. The symbols turn out not to be needed for the material this book teaches, and the machinery that needs them is depth curriculum.

## 6. Terminology readiness

| Term | State | Source position |
|---|---|---|
| `estimator` | stub, TODO since Chapter 1 | closed here |
| `estimate` | stub, TODO since Chapter 1 | closed here |
| `sampling variability` | new | distinguished from every other uncertainty in §4 |
| `standard error` | new | at concept depth only |
| `interval estimate` | new | `greenland2016misinterpretations` p. 340 uses the term |
| `P value` | new | `greenland2016misinterpretations` p. 339; `asa2016pvalue` |
| `statistical significance` | new, **and treated as a hazard** | `greenland2016misinterpretations` p. 348 |
| `analytic flexibility` | new | `greenland2016misinterpretations` p. 347(b) |
| `model checking` | new | §7 |
| `consistency` (estimator sense) | **collision with Chapter 7** | announced, as `calibration` was in Chapter 6 |
| `confidence` | technical sense flagged in canon since Chapter 6 | **recommend the word be handled with care rather than adopted** |

**Two collisions, and they need different handling.**

`consistency` collides with Chapter 7's causal condition. Announce, both senses, as the book has done three times before.

`confidence` is worse, because the ordinary word means something the technical term does not, and the source says so: statistical usages of "significance" and "confidence" are at odds with ordinary English definitions [@greenland2016misinterpretations, p. 339]. Recommend the chapter use `interval estimate` in its own prose and treat `confidence interval` as a term the reader will meet elsewhere.

## 7. High-risk conceptual collapses to prevent

1. **The interval covers the uncertainty.** It covers sampling variability under a model, and nothing else.
2. **A wider interval is more conservative.** The anchor demonstrates this false, numerically and in a direction that surprises.
3. **Significant means real; non-significant means no effect.** Both are on the source's misinterpretation list, at pp. 340–341.
4. **The P value is the probability the hypothesis is true.** Misinterpretation 1, p. 340.
5. **The P value tests the hypothesis.** It tests the entire model, p. 339.
6. **Analytic flexibility is a research-ethics topic.** It is inside the statistical model's assumptions.
7. **Preregistration is the fix.** It is one device with real limits; the chapter must not sell it as a solution.
8. **More data fixes it.** Fifth appearance of the shape, and Chapter 4's `meng2018paradox` already supplies the sharpest version.
9. **Fit is model checking.** Chapter 5 already established that fitting past data is weak evidence; Chapter 8 must not undo it.
10. **A good estimate rescues a bad identification.** Chapter 7 said the opposite, from a source.
11. **Reporting more decimal places is more informative.** Chapter 3's resolution/trueness point, in a new setting.

## 8. Research clusters

1. **Estimand, estimator, estimate** — closing two canon stubs.
2. **What a computed number is conditional on** — the spine.
3. **Thresholds and their misinterpretations** — the governed core competence names this explicitly.
4. **Uncertainty, checking, and the chapter's own examples.**

## 9. Candidate example constraints

The anchor is available for an **eighth** recurrence and the quantity is already specified: Chapter 6's unjustified ±0.6 ML spread.

Constraints:

- The record must permit **at least four defensible analyses with different answers**, at least one of which crosses a conventional threshold in the opposite direction from the others.
- The correction must show that **fixing the spread alone moves the answer the wrong way**, so that "widen the interval to be safe" is refuted numerically rather than asserted.
- No new mechanism, no new zone, no new physical fact.

**Gate 1 remains open and is now eight chapters deep.**

## 10. Decisions likely required after research

1. **Notation — recommend declining**, against Chapter 6's promise, with the refusal stated to the reader.
2. **How far into p-values.** Recommend: what one is, what it tests, and the misinterpretations — with no test procedures, no distributions, and no worked hypothesis test.
3. **`confidence` — use or avoid.** Recommend avoid in the book's own prose.
4. **Regression.** The core competence names it. Recommend it appears as *a model whose assumptions are the thing under discussion*, not as a technique taught.
5. **Likelihood.** Named in the core competence and colliding with Chapter 6's deliberately avoided term. Recommend one paragraph at concept depth.
6. **The eighth water-case recurrence.**

## 11. Drafting gate

Do not draft until:

- `../../decisions/0015` exists in proposed form with the notation refusal settled;
- the canon entries are written, including `estimator` and `estimate`, TODO since Chapter 1;
- `case-data.md` freezes the 24-event forecast record, the four defensible analyses, and the corrected breach probabilities — **with every number computed and checked, including the two one-sided corrections**;
- `spec.md` records how eight named topics become one chapter.
