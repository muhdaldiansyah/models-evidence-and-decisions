# Chapter 11 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 11: **Decisions Under Uncertainty and Value of Information** — the second chapter of Part III.

**Process note.** As in Chapters 3–10, this audit was written alongside its research. Findings taken from sources are marked. Every locator was taken from reading the document directly.

Current architecture from `README.md` and `spec.md`:

- central question: **Which act is defensible, and would more evidence change it?**
- core competence: **Use decision trees, expected utility, risk attitudes, sensitivity analysis, value of information, decision-quality reasoning, ambiguity awareness, and recognition of when further analysis itself is not worthwhile.**
- target: 33 pages / 7 serious learning hours.

## 1. Readiness verdict

**Drafting-ready after adjudication**, and it is the chapter the whole book has been walking toward.

**It is the most heavily pre-promised chapter after Chapter 7.** Chapters 1, 5, 6 (three separate promises), 7, and 10 (eight promises) all defer here, and the deferrals are not vague — they name expected utility, risk attitude, the worth of an informative observation, trade-offs, and value of information.

**The last item in the core competence is the chapter's own escape hatch**, and it is governed text: *recognition of when further analysis itself is not worthwhile.* A chapter that taught eight techniques and stopped would have failed its own brief. This one has to turn on itself.

**And the arithmetic came out better than hoped.** The anchor's value-of-information calculation returns **£2,300** for the pump test — the most informative observation in the entire book, named in Chapter 2, confirmed obtainable in Chapter 5, and computed in Chapter 6 as moving belief from 2:1 to 10:1. Against a test cost of £8,000, **it is not worth running.**

That is the honest close to the book's evidence arc, and it is not a rhetorical flourish: it falls out of the numbers.

## 2. Unique-job hypothesis

> Teach readers to lay a decision out, choose defensibly under uncertainty, and — before any of that — ask whether the answer could turn on anything they might go and find out.

The reader who finishes Chapter 11 should be able to build a small decision table, compute expected values, notice that using them is itself a choice, find the point at which the best act changes, compute what perfect information would be worth as a ceiling, and decline a study whose result could not move the decision.

## 3. What earlier chapters have promised

| Promised in | Text | Settled by |
|---|---|---|
| `01/chapter.md` L535 | "Chapter 11 will later formalize questions about the value of information" | §5 |
| `05/chapter.md` L621 | "*We should find out* and *finding out is worth what it costs* are different claims" | §5 |
| `06/chapter.md` L394, L1035 | whether an observation that moves belief is worth its cost | §5 |
| `06/chapter.md` L625 | "expected utility, risk attitude, and what to do when the consequences of being wrong are not symmetric" | §3 |
| `07/chapter.md` L1063 | whether to act, given consequences and an attitude to risk | §3 |
| `10/chapter.md` ×8 | weighting, trade-offs, value of information, "Chapter 11 solves it" | §§2–5 |
| `canon` `expectation` | the slide to *therefore act as if X* "belongs to Chapter 11 and must be made deliberately there" | §3 |
| `canon` `consequence` | "formal decision-under-uncertainty treatment remains Chapter 11" | §2 |

**Fourteen located promises.** The canon entry on `expectation` is the sharpest: it does not merely defer, it instructs this chapter to make a move deliberately that Chapter 6 refused to make silently.

## 4. Neighbouring-chapter boundaries

### Chapter 10 — what precedes

Chapter 10 produced seven alternatives, three fundamental objectives, and four stated conflicts, and stopped. Its closing section names both halves of this chapter.

**A narrowing is required and must be visible.** Seven alternatives will not fit a decision table at this depth, and the chapter must say that narrowing is itself a choice rather than letting three appear from nowhere.

### Chapter 12 — optimization and robustness

Choosing an act that performs acceptably across a range of assumptions, rather than best under one, is Chapter 12's. Chapter 11 picks a best act under stated beliefs; Chapter 12 asks what to do when you decline to state them.

The line to state: **Chapter 11 optimises. Chapter 12 hedges.**

### Chapter 15 — strategic response

`colyvan2016voi` moves into cooperation games at printed p. 306. **That is Chapter 15's material and this chapter stops before it.**

### Chapter 17 — monitoring

Monitoring appears in the source as a use of information. Chapter 11 treats whether to buy information before deciding; Chapter 17 treats watching after deploying.

## 5. Terminology readiness

| Term | State | Source position |
|---|---|---|
| `decision tree` | new | the book's own layout device; no source teaches it here |
| `expected value` | `expectation` exists from Chapter 6; the **decision rule** is new | canon already instructs this chapter |
| `risk attitude` | new | **no source obtained — see §9** |
| `sensitivity analysis` | Chapter 5 named it and deferred to Chapter 8; Chapter 8 used it as a model check | the **decision** sense is new here |
| `value of information` | new | `colyvan2016voi` pp. 302–305 |
| `value of perfect information` | new | `colyvan2016voi` p. 303 |
| `ambiguity` | new | `colyvan2016voi` p. 302's interval example |
| `decision quality` | new | treated as a disposition, not a framework |

**One term arrives for the third time.** `sensitivity analysis` was named in Chapter 5 (and refused as criticism), used in Chapter 8 (as a model check), and is used here in its decision sense — does the best act change? The canon entry must carry all three and say they are one technique with three jobs.

## 6. High-risk conceptual collapses to prevent

1. **Expected value is the decision.** Chapter 6 flagged this; canon instructs this chapter to make the choice deliberately.
2. **A decision tree is the decision.** It is a layout.
3. **More information is better.** `colyvan2016voi` p. 302 opens on exactly this assumption and spends the paper against it.
4. **Informative means valuable.** The broken-toe example at p. 303, and the anchor's £2,300.
5. **Value of information is about the information.** It is about the decision — "it depends on what you're going to do with the information" [@colyvan2016voi, p. 304].
6. **A study worth commissioning is one that would tell you something.** It is one whose result could change the act.
7. **Sensitivity analysis means varying inputs ±20%.** It means finding where the answer changes.
8. **Risk aversion is irrationality.** It is a preference the arithmetic cannot supply.
9. **Ambiguity is the same as risk.** Not knowing the probability is different from knowing it.
10. **The analysis is free.** The chapter must cost its own machinery.
11. **A single currency is available.** `colyvan2016voi` p. 305 records that VOI "typically do require a single currency", which Chapter 10's multiple objectives make hard.
12. **Zero value of information means the question does not matter.** It means it does not matter *for this decision*.

## 7. Research clusters

1. **Laying a decision out**, and what a tree is and is not.
2. **Expected value as a rule**, and risk attitude.
3. **Value of information**, its ceiling, and its limits.
4. **When analysis is not worthwhile**, and the chapter's own examples.

## 8. Candidate example constraints

The anchor is available for an **eleventh** recurrence, and it must now close the book's longest-running thread.

Constraints:

- Three acts, narrowed from Chapter 10's seven, **with the narrowing shown as a choice**.
- Two states, which must be Chapter 2's Mechanisms A and B — no new uncertainty may be invented.
- Probabilities must be Chapter 6's, unchanged.
- **The value of the pump test must come out small**, and the arithmetic must be checked rather than arranged.
- One act must have **no spread across the two states**, so risk attitude is demonstrable without utility functions.
- The indifference point must be **far from the prior**, so that sensitivity analysis and VOI agree.

**Gate 1 remains open and is now eleven chapters deep.**

## 9. The risk-attitude gap, stated before drafting

**No source was obtained for a formal treatment of risk attitude.** Four candidates were considered; the economics guidance that mentions risk aversion does so only in passing, in regulatory contexts, and would not support teaching.

**The proposed handling is to name and demonstrate, not to formalize.**

The chapter shows, on the anchor's own numbers, that one act has no spread and costs more in expectation — so preferring it is a preference the arithmetic cannot supply. It states that using expected value is therefore a choice, which is what `canon/terminology.md` instructs this chapter to do. It routes utility functions, certainty equivalents, and risk-premium machinery to the depth curriculum.

**This is deliberately not a fifth instance of the demonstrate-because-unsourced disposition** that `../../decisions/README.md` has on notice at four. There, a *practice* was taught with no source. Here the chapter declines to teach the practice and states only what its own arithmetic displays. `../../decisions/0018` clause 4.4 records the distinction rather than assuming it, and it is the closest the book has come.

## 10. Decisions likely required after research

1. **Notation.** A decision tree is a diagram. Recommend permitting an inline text tree, as Decision 0014 permitted inline arrows, and nothing else. Fifth notation decision.
2. **The risk-attitude handling** — clause 4.4 above.
3. **How far into VOI arithmetic** — recommend the full calculation on the anchor, since it is arithmetic, and no formulas.
4. **Whether EVPI is taught as a screening rule** — recommend yes; it is the cheapest thing in the chapter.
5. **The narrowing from seven acts to three**, and how visibly.
6. **The eleventh water-case recurrence, and whether the book's evidence thread should close on a negative result.**

## 11. Drafting gate

Do not draft until:

- `../../decisions/0018` exists in proposed form with the notation and risk-attitude clauses settled;
- the eight canon entries are written, including the three-job `sensitivity analysis` entry;
- `case-data.md` freezes the three acts, the payoff table, and **every one of the expected values, the two branch values, the VOI, the EVPI, and the indifference point, all computed and checked**;
- `spec.md` records the risk-attitude gap.
