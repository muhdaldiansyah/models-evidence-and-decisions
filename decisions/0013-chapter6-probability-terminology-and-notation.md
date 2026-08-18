# Decision 0013: Chapter 6 Probability Terminology and Notation

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `research-plan.md` §10 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 6 entries in `canon/terminology.md` are built on this record and inherit its provisional status.

**Clause 2 breaks a policy the book has held for five chapters and deserves separate attention.**

Evidence base: `research-01-conditioning-and-updating.md`, `research-02-base-rates.md`, `research-03-scoring-and-calibration.md`, `research-04-simulation-examples-exercises.md`.

## Decision

Chapter 6 opens Part II. Its organizing claim is:

> A probability is not a property of an event. It is a property of an event **given stated information** — which makes conditioning the central concept and Bayes' rule the arithmetic of moving between conditioning positions.

### 1. What a probability is predicated of

**1.1** A probability is stated **conditional on information**, and stating the information is part of stating the probability.

**1.2** This makes Chapter 6 the sixth instance of the book's recurring shape. Chapter 5 already displayed the five-row table; **Chapter 6 does not restate it.** It assumes it, in one sentence, and moves on.

**1.3** The frequency / degree-of-belief distinction is **named once and set aside**. The book needs both readings — a coin has a long-run frequency; Mechanism A does not — and the conditioning framing unifies them. The chapter states that the interpretations debate exists, that this book does not adjudicate it, and moves on.

**1.4** Conditioning is **not** taught as filtering. Filtering is the mechanical shadow: it fails for unique events and it hides the direction problem, which is the chapter's most consequential error. Conditioning changes **what you are taking as given**.

### 2. Notation — a bounded exception

**2.1** Chapters 1–5 used **no notation**. Chapter 6 takes a **minimal, explicitly bounded exception**.

**2.2** Permitted:

- `P(A | B)` — the conditioning bar;
- odds written as `3 : 1`;
- ordinary arithmetic.

**2.3** Not permitted: summation, integration, calculus of any kind; distributions written as functions; random variables as symbols; expectation operators; the Bayes formula with its denominator.

**2.4** The exception is **announced to the reader**, with the reason: this chapter turns on a distinction that the notation makes visible and prose obscures — the asymmetry between `P(A | B)` and `P(B | A)`.

**2.5** The boundary is the point. If the manuscript needs a symbol not on the permitted list, that is a signal the material belongs to Chapter 8 or the depth curriculum, not a reason to widen the exception.

### 3. Bayes

**3.1** Bayes is presented in the **odds form**: prior odds × ratio = posterior odds. Odds are taught in two sentences.

**3.2** Rationale: Chapter 5 handed this chapter a two-hypothesis problem, which is exactly what the odds form suits; it is one multiplication; it avoids the denominator, which is where readers stall; and it makes *how far does this evidence move me* a visible number.

**3.3** The ratio is **not** called a likelihood ratio in reader-facing prose. `likelihood` has an estimation sense that Chapter 8 owns. The chapter says *how expected this observation is under each hypothesis*, and names the ratio plainly.

**3.4** The chapter draws the consequence that **an observation whose ratio is near 1 is not worth making**, however interesting it sounds — and stops there. Whether an informative observation is *worth its cost* is Chapter 11.

### 4. Base rates and claims about judgment

**4.1** The chapter's empirical claims about human judgment are sourced to `tversky1974judgment` pp. 1124–1125 and bounded to what those pages support.

**4.2** Base-rate neglect is **not** stated as universal. The source conditions it: priors are used correctly when no other information is offered, and abandoned when worthless information is. The chapter **quotes** the p. 1125 formulation rather than paraphrasing it.

**4.3** The heuristics are **not** presented as defects. p. 1124 calls them "quite useful, but sometimes they lead to severe and systematic errors."

**4.4** The chapter claims **nothing** about debiasing or training. It claims only that doing the arithmetic explicitly is a way of not relying on the intuition — a claim about a procedure.

**4.5** The two-directional tension is shown: worthless evidence displaces priors, and genuinely informative evidence is under-weighted ("conservatism", p. 1125). The lesson is that intuition does not track evidential weight in either direction, which is the argument for the odds form.

### 5. Scoring, calibration, sharpness

**5.1** **Propriety** is taught as a concept, not a formula: a proper scoring rule is one under which your best expected score comes from stating what you actually believe (`gneiting2007scoring` p. 359).

**5.2** The chapter notes that invented scoring schemes are often "intuitively appealing but improper" (`gneiting2007scoring` pp. 359–360) and does **not** teach which rules are proper.

**5.3** **Calibration and sharpness are kept apart**, using the source's own definitions: calibration is a **joint property** of forecasts and outcomes; sharpness is a property of **the forecasts alone** (`gneiting2007scoring` p. 359). The goal is "to maximize the sharpness of the predictive distributions subject to calibration" (p. 359).

**5.4** The chapter demonstrates that a forecaster who always states the base rate is perfectly calibrated and useless. **This demonstration is the book's own**; the source does not give it.

**5.5** A single forecast cannot be scored. **Derived, not sourced**, and demonstrated. The chapter connects this to Chapter 5: an unscored forecast, like a check that could not have failed, establishes nothing.

**5.6** **`calibration` — the Chapter 3 collision — is reopened explicitly**, handled the same way Chapter 5 handled `validation`: name it, say why the word is now available, move on. This is the second word Chapter 3 set aside and a later chapter takes up; consistency is required.

**5.7** Brier (1950) may be referenced **only as reported at `gneiting2007scoring` p. 360**. It was not obtained. No direct citation, no attributed wording, no description of contents.

### 6. Simulation

**6.1** Simulation **computes the consequences of assumptions**. It does not produce evidence about the world.

**6.2** **More runs reduce Monte Carlo error and do nothing about model error.** This is the fourth instance of a shape the reader has met in Chapters 3 and 4, and the chapter names it as a habit: when told more of something will fix a problem, ask which term it enters.

**6.3** **Sourcing.** The simulation material needs no citation because it is arithmetic, not empirical claim — the same status as long division. `research-04` §1 records that this is **not** an instance of the demonstrate-because-unsourced pattern that `decisions/0012` clause 4.3 puts on notice, and states the distinction explicitly rather than assuming it.

**6.4** The chapter makes **no claim about how practitioners misuse simulation**. Such a claim would be empirical and is unsourced.

### 7. Vocabulary

**7.1** Controlled: `probability`, `conditional probability`, `prior`, `posterior`, `base rate`, `expectation`, `calibration` (Chapter 6 sense), `sharpness`, `scoring rule`.

**7.2** Ordinary careful language: distribution, forecast, simulation, Monte Carlo, odds, propriety.

**7.3** **Not used:** `likelihood` (clause 3.3), `random variable`, `density`, `variance`, `confidence`, `significance`.

**7.4** `calibration` is **not** re-registered. Its Chapter 3 entry already names the collision; Chapter 6 updates that entry rather than creating a duplicate.

### 8. What Chapter 6 does not do

- Not causal: conditioning is not intervening, and the chapter says so once (Chapter 7).
- Not estimation: no likelihood, regression, intervals, or uncertainty quantification (Chapter 8).
- Not decision: expectation is a summary of a distribution, not a decision rule; no expected utility, risk attitude, or value of information (Chapter 11).
- Not robustness formalism (Chapter 12).
- Not sequential updating, filtering, or observability (Chapter 14).
- Not monitoring design (Chapter 17).
- Not foundations of probability, interpretations debates, or measure theory (depth curriculum).

## Sources promoted

New and verified: `tversky1974judgment` (pp. 1124–1125 read), `gneiting2007scoring` (pp. 359–360 read).

Reused: `pearl2009causal` for the conditioning-is-not-intervening boundary.

## Known gaps carried forward

1. **Brier (1950) not obtained.** Referenced only as reported at `gneiting2007scoring` p. 360.
2. **`tversky1974judgment` read to p. 1125 only.** Availability and anchoring are on uninspected pages.
3. **`gneiting2007scoring` read to p. 360 only.**
4. **The debiasing literature was not read** and must not be characterized.
5. The always-state-the-base-rate demonstration and the single-forecast argument are **derived, not sourced**, and are marked as such.

## No architecture change

Title, central question, core competence, 34-page and 7-hour targets are unchanged and remain governed by `README.md` and `decisions/0001`.
