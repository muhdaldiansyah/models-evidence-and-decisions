# Decision 0018: Chapter 11 Decision Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `readiness-audit.md` §10 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 11 entries in `canon/terminology.md` are built on this record and inherit its provisional status.

**Clause 4.4 is the one to read first.** It records the closest the book has come to a fifth instance of the demonstrate-because-unsourced disposition, and states why it is not one.

Evidence base: `../chapters/11-decisions-voi/research-01-laying-it-out.md`, `research-02-expected-value-and-risk.md`, `research-03-value-of-information.md`, `research-04-when-not-to-analyse-and-examples.md`.

## Decision

Chapter 11's organizing claim is:

> Before asking what the evidence says, ask whether any answer it could give would change what you do — because the answer is frequently no, and the test is one afternoon's arithmetic.

### 1. The chapter turns on itself

**1.1** The governed core competence ends with "recognition of when further analysis itself is not worthwhile". That is treated as the chapter's brief rather than as an afterthought.

**1.2** The chapter therefore costs its own machinery. [@colyvan2016voi, p. 308, footnote 16] records that a value-of-information study is itself a study with a cost, and §6 of the manuscript carries it.

**1.3** **The anchor's result is negative and stays negative.** The pump test — named in Chapter 2, confirmed obtainable in Chapter 5, computed in Chapter 6 as moving belief from roughly 2:1 to 10:1 — is worth **£2,300** against a cost of **£8,000**. The manuscript does not soften this into a lesson about care.

### 2. Notation — a third bounded extension

**2.1** Chapter 8 declined to extend; Chapters 9 and 10 added nothing. This chapter needs one thing.

**2.2** Permitted: **a decision table** with acts as rows and states as columns, and **one inline text tree** in the section where sequence matters. Nothing else.

**2.3** Not permitted: expectation operators, utility functions, any formula for value of information, probability notation beyond Decisions 0013 and 0014, formal tree conventions with node symbols.

**2.4** The tree is permitted on the same footing as Decision 0014's inline arrows: it displays a structure that prose obscures, and it is drawn in text rather than as a figure.

**2.5** **No read source teaches the decision tree as a device.** The layout is standard material in a literature this book did not obtain, and it is presented as **the book's own presentation of standard material** rather than attributed. Recorded rather than glossed over.

### 3. Laying the decision out

**3.1** Acts, states, consequences. The relation to the six-step process at [@bradley2016structured, p. 8] is stated once.

**3.2** **The narrowing from Chapter 10's seven alternatives to three is shown as a choice**, with its criterion stated: one act per mechanism, plus one act that works under either.

**3.3** **The collapse of Chapter 10's three objectives into one currency is stated as a value judgment**, not a neutral step, and [@colyvan2016voi, p. 305]'s single-currency limitation is cited for it.

### 4. Expected value, and risk attitude

**4.1** Expected value is used, and **using it is stated as a choice**. `canon/terminology.md`'s `expectation` entry instructs this chapter to make that move deliberately, and the chapter does.

**4.2** The positive case is made: expected value is the only rule in the chapter that uses all the information in the table, and it is what makes value of information computable.

**4.3** Risk attitude is **named and demonstrated, not formalized.** The anchor's Act C has no spread across the two states and costs more in expectation, so preferring it is visibly a preference the arithmetic cannot supply. Utility functions, certainty equivalents, and risk premiums are named as existing and routed to the depth curriculum.

**4.4 — the clause to read.** **No source was obtained for a formal treatment of risk attitude**, and this is the closest the book has come to a fifth instance of the disposition that `README.md` in this directory has on notice at four.

**It is not one**, and the distinction is stated rather than assumed. In the four recorded instances a **practice** was taught with no source — the reader was given something to do. Here the chapter **declines to teach the practice** and states only what its own table displays. There is no method and no procedure.

**If the author disagrees, the honest response is to cut the risk-attitude material**, not to source it retrospectively. Clause 4.3 would then be struck and the chapter would say that risk attitude exists, matters, and is not treated.

### 5. Sensitivity analysis, for the third time

**5.1** Chapter 5 named it and refused it as criticism. Chapter 8 used it as a model check. Chapter 11 uses it in its **decision** sense: at what point does the best act change?

**5.2** The canon entry carries all three and says they are one technique with three jobs.

**5.3** [@colyvan2016voi, p. 302]'s two-interval example is the chapter's demonstration, and the anchor's indifference point at `p = 0.283` against a prior of `0.636` is its instantiation.

### 6. Value of information

**6.1** Taught as arithmetic on the anchor. **No formula is written.**

**6.2** The broken-toe example is carried [@colyvan2016voi, p. 303], with its qualification that the same information may be valuable for another purpose — the ninth instance of the book's relativity shape.

**6.3** **The perfect-information ceiling is taught as a screening rule**, on the strength of [@colyvan2016voi, p. 303]: the value of imperfect information is always less than that of perfect information. It is the cheapest thing in the chapter.

**6.4** All four documented limitations are carried [@colyvan2016voi, pp. 305–306]: framing, single currency, budget non-fungibility, and value arriving later.

**6.5** The three kinds of information gathering are taught [@colyvan2016voi, p. 306], with the point that value of information applies to the second and that most organisational collection is the third.

**6.6** Rhodes et al. (2011) and Møller and Fiedler (2010) are cited **as reported at** `colyvan2016voi`. Neither was obtained.

### 7. Ambiguity

**7.1** Treated only as far as [@colyvan2016voi, p. 302]'s interval example supports: not knowing a probability exactly is different from knowing it, and whether it matters depends on whether the interval straddles a critical value.

**7.2** **Ellsberg (1961) was not obtained.** The chapter does not use the term "Ellsberg paradox" and does not describe those experiments.

### 8. Vocabulary

**8.1** Introduced here: `decision tree`, `expected value` (as a decision rule), `risk attitude`, `value of information`, `value of perfect information`, `ambiguity`, `decision quality`.

**8.2** `sensitivity analysis` is closed here, carrying all three of its jobs.

**8.3** `consequence` is specialised from its Chapter 1 entry, which recorded that "formal decision-under-uncertainty treatment remains Chapter 11".

### 9. What Chapter 11 does not do

- Teach utility functions, certainty equivalents, or risk premiums.
- Write any formula.
- Teach multi-attribute utility theory; the single currency is used and its cost stated.
- Reopen Chapter 6's declined argument about what probability is.
- Treat real options, dynamic programming, or sequential decisions beyond the one test-then-act tree — Chapters 12 and 14.
- Treat robustness or hedging under declined probabilities — Chapter 12.
- Enter game theory — Chapter 15.
- Treat post-deployment monitoring — Chapter 17.
- Treat discounting beyond naming it.
- Recommend an act for the utility.

## Sources promoted

`colyvan2016voi` is new to `references.bib`, read at printed pp. 302–306 and footnote 16 at p. 308. `bradley2016structured` and `nasem2026decisionmaking` are reused as already verified.

## Known gaps carried forward

1. **No source for risk attitude.** Clause 4.4.
2. **No source teaches the decision tree.** Clause 2.5.
3. **Howard's information-value papers, Raiffa and Schlaifer, and Ellsberg (1961)** were attempted and not obtained.
4. **Rhodes et al. (2011), Møller and Fiedler (2010)** cited within `colyvan2016voi`; not obtained.
5. **`colyvan2016voi` read at pp. 302–306 and one footnote only.**
6. **The monetisation in the anchor's payoff table is a value judgment**, not a measurement, and the manuscript says so.
7. The **Chapter 11 case is the water anchor's eleventh recurrence**, and Chapter 1's Gate 1 remains open.

## No architecture change

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields.

**It does close the book's longest-running thread on a negative result.** The pump test has been alive since Chapter 2 and the answer is that running it is not worth the money. The author may prefer a different narrowing or a different monetisation that reverses this; clause 1.3 records that the current arithmetic was computed and checked rather than arranged, and `../chapters/11-decisions-voi/research-04-when-not-to-analyse-and-examples.md` §6 shows every figure.
