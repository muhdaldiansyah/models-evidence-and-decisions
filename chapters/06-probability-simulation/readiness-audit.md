# Chapter 6 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 6: **Probability, Prediction, and Simulation** — the first chapter of Part II.

**Process note.** As in Chapters 3–5, this audit was written alongside its research. Findings taken from sources are marked.

Current architecture from `README.md` and `spec.md`:

- central question: **How is uncertainty represented, updated, and scored?**
- core competence: **Use conditioning, Bayes, expectation, base rates, simulation, probabilistic prediction, and calibration to reason coherently under uncertainty.**
- target: 34 pages / 7 serious learning hours — **the largest chapter in the book.**

## 1. Readiness verdict

**Drafting-ready after adjudication**, with one structural difficulty that distinguishes it from every chapter so far.

**Chapter 6 is the first chapter that must teach a technique rather than a habit of mind.** Part I taught ways of looking; this chapter teaches conditioning, Bayes, expectation, and scoring, all of which have mathematics attached. The book's readers are assumed comfortable with algebra and unwilling to be handed a statistics course.

That tension governs almost every decision below, and it is the reason this chapter is the longest in the book.

Chapter 5 hands it a strong opening. Its closing section observes that nearly every unresolved item in Part I is now a question about evidence: how likely is it that the tank starts lower than assumed, what would the pump test actually tell us, how much would one hot afternoon's data move belief about Mechanism A.

## 2. Unique-job hypothesis

> Teach readers to hold uncertainty as a stated quantity conditional on stated information, to update it coherently when evidence arrives, and to be scored on the result.

The reader who finishes Chapter 6 should be able to take one of Chapter 5's open items, state a probability with the information it is conditional on, say what observation would move it and roughly how far, and accept being scored when the answer arrives.

## 3. Neighbouring-chapter boundaries

### Chapter 3 — a terminology collision already flagged

`canon/terminology.md` registers `calibration` for the instrument sense and states explicitly that it is "**not** to be confused with the Chapter 6 sense of calibration for probabilistic forecasts, which is a different concept sharing the word."

Chapter 6 must **reopen that collision explicitly**, exactly as Chapter 5 was required to do with `validation`. Two chapters now inherit a word Chapter 3 set aside; the pattern should be handled consistently.

### Chapter 5 — what precedes

Chapter 5 taught naming the discriminating observation. Chapter 6 asks **how much it would move belief**. That is the clean line and it should be stated to the reader.

### Chapter 7 — identification

**The most important boundary in this chapter.** Chapter 6 is associational and predictive throughout. Conditioning is not intervening, and `pearl2009causal` already supports that distinction at Chapter 1 depth.

Chapter 6 may update belief about which mechanism operates given an observation. It may **not** claim that conditioning establishes what would happen under an intervention.

### Chapter 8 — estimation

Chapter 6 represents and updates uncertainty and scores predictions. Chapter 8 estimates from finite data: likelihood, regression, intervals, uncertainty quantification.

Proposed test: Chapter 6 asks *what should I believe, given this?*; Chapter 8 asks *what does this finite sample support?*

### Chapter 11 — decisions

Chapter 6 introduces expectation as a **summary of a distribution**. Chapter 11 owns expected utility as a **decision rule**, risk attitude, and value of information.

The line matters because "take the expected value" slides from one to the other without announcement, and doing so smuggles in risk neutrality.

### Chapter 12 — robustness

Chapter 6 may note that a conclusion holding across plausible probability assignments is more trustworthy. Formal robustness is Chapter 12.

### Chapter 14 — sequential

Repeated updating through time, filtering, and observability are Chapter 14. Chapter 6 updates once, or a few times, by hand.

### Chapter 17 — monitoring

Scoring a forecast after the fact is Chapter 6. Designing a monitoring system that does it continuously is Chapter 17.

## 4. Terminology readiness

Terms requiring adjudication:

- probability, and what it is predicated of;
- conditional probability; conditioning;
- prior and posterior;
- Bayes' rule;
- base rate;
- likelihood (careful: Chapter 8 owns the estimation sense);
- expectation;
- distribution;
- probabilistic prediction / forecast;
- calibration (Chapter 6 sense — collision with Chapter 3);
- sharpness;
- scoring rule; propriety;
- simulation; Monte Carlo.

## 5. High-risk conceptual collapses to prevent

1. **Probability is a frequency and nothing else.** A one-off event can carry a probability.
2. **A probability is a property of the event.** It is relative to the information conditioned on — the chapter's spine.
3. **Conditioning is filtering.** Restricting attention to a subset is the mechanical shadow of the concept, not the concept.
4. **P(A|B) equals P(B|A).** The inversion error, and the most consequential single mistake in the chapter.
5. **Base rates can be ignored once you have evidence.** *(Sourced.)* `tversky1974judgment` p. 1125 documents that people abandon priors even when the evidence supplied is worthless.
6. **A model that fits well gives good probabilities.** Fit and calibration are different properties.
7. **Calibration is accuracy.** *(Sourced.)* `gneiting2007scoring` p. 359 makes calibration a joint property of forecasts and outcomes, and sharpness a property of forecasts alone.
8. **A single forecast can be evaluated.** One outcome cannot score one probability.
9. **Simulation produces evidence about the world.** It computes consequences of assumptions.
10. **More simulation runs make the answer better.** They reduce Monte Carlo error, not model error.
11. **The expectation is what will happen.** It may be a value the quantity cannot take.
12. **A probability for a unique event is meaningless.** This is the objection that stops readers using any of it.

## 6. Research clusters

- **R01 — What a probability is: conditioning and updating.**
- **R02 — Base rates, and what people do with evidence.**
- **R03 — Scoring: propriety, calibration, sharpness.**
- **R04 — Simulation, examples, and exercises.**

## 7. Candidate example constraints

The anchor should be **Chapter 5's open items**, worked probabilistically. Mechanism A versus Mechanism B is a two-hypothesis updating problem with a named discriminating observation — which is as close to a purpose-built teaching case as the book will get, and it arose naturally over four chapters rather than being constructed.

Avoid: medical-test examples, which are the standard vehicle for Bayes and which would import Chapter 7's identification concerns and Chapter 3's measurement concerns simultaneously.

## 8. Decisions likely required after research

1. What `probability` is predicated of, reader-facing, and whether the frequency/belief distinction is taught or sidestepped.
2. Whether Bayes' rule is given as a formula, as an odds update, or as a procedure.
3. How much notation the chapter uses — and whether "no notation", held for five chapters, survives.
4. Whether `likelihood` is used, given Chapter 8 owns its estimation sense.
5. How the Chapter 3 `calibration` collision is reopened.
6. Whether simulation is taught as a technique or signposted.
7. The anchor and the transfer forms.

Decision 3 is the consequential one and is unavoidable: a chapter on conditioning that refuses all notation may be less clear, not more.

## 9. Drafting gate

Chapter 6 becomes drafting-ready when R01–R04 have dossiers, terminology is adjudicated, the notation question is settled, the Chapter 7 and Chapter 8 boundaries are stated in applicable form, and `spec.md` no longer contains load-bearing TODOs.
