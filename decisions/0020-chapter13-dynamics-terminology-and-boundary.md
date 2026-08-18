# Decision 0020: Chapter 13 Dynamics Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `readiness-audit.md` §9 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 13 entries in `canon/terminology.md` are built on this record and inherit its provisional status.

**This record differs from 0009–0019 in one respect.** Chapter 13's scope was written in advance by [Decision 0007](0007-chapter1-dynamics-and-response-boundary.md), which is **Accepted**. Where this record restates 0007, it is reporting a settled decision rather than proposing one; where it goes beyond 0007, it says so. Clauses 1, 3, 5, and 8 are the ones that go beyond.

Evidence base: `../chapters/13-dynamics-feedback/research-01-stocks-flows-accumulation.md`, `research-02-the-difficulty-of-accumulation.md`, `research-03-delay-feedback-stability.md`, `research-04-policy-resistance-and-examples.md`.

## Decision

Chapter 13's organizing claim is:

> A system that accumulates, delays, and responds will defeat reasoning that treats an action as a one-way cause — and the defeat is regular enough to be anticipated rather than merely regretted.

### 1. The chapter is governed by an Accepted decision, and says so

**1.1** `0007` names what Chapter 13 owns: "stocks and flows, formal delays, feedback loops, equilibrium, stability, oscillation, and policy resistance." Every one is treated and nothing else is.

**1.2** **This is the first chapter in the book whose scope arrived pre-adjudicated**, and the drafting decision is correspondingly narrow. Where earlier records had to establish a boundary, this one mostly has to hold one.

**1.3** **Beyond 0007:** the chapter names `state space` once, discharging the promise recorded in the `state` canon entry that "`state space` is not named until Chapter 13". It is named and not developed.

### 2. Feedback is the spine, and it is aimed at Part II

**2.1** The chapter's spine is [@astrom2008feedback, p. 1]: reasoning about a feedback system by cause and effect leads to a circular argument, "and it is therefore necessary to resort to formal methods to understand them."

**2.2** **This is aimed squarely at Chapter 7.** Chapter 7 spent thirty-eight pages on what it takes to establish that A causes B. The spine says that where feedback is present the question is not merely hard — it is the wrong shape. **The manuscript states this once and does not retract Chapter 7.**

**2.3** `open loop` and `closed loop` are taught from [@astrom2008feedback, p. 2].

**2.4** The two-sided property is taught from [@astrom2008feedback, p. 3], where the source states both halves on one page: feedback buys insensitivity to disturbance and variation, and it can create instability, oscillation, and runaway behaviour. **This is the seventh appearance of the book's "the property that buys you one thing costs you another" shape**, and the first in which a single source page states both halves unprompted.

### 3. Loop polarity is taught, under different names

**3.1** **Beyond 0007**, which banned `positive feedback` and `negative feedback` from Chapter 1 without saying what Chapter 13 should use.

**3.2** The book adopts **`reinforcing`** and **`balancing`**. Both sources supply the alternative in the same breath as the standard pair: [@sterman2006evidence, p. 507] writes "self-reinforcing (positive) and self-correcting (negative)".

**3.3** `positive feedback` and `negative feedback` are **named once** as the terms the reader will meet, with the reason for the book's preference given: `positive` is already a controlled term in this book, paired with `normative`, since Chapter 1.

**3.4** The saturation clause is carried: reinforcing feedback is "usually accompanied by a saturation that limits the growth of the quantity" [@astrom2008feedback, p. 22]. A reinforcing loop is not a prediction of unbounded growth.

### 4. Stocks, flows, and accumulation

**4.1** Taught from [@sterman2006evidence, p. 508], including the four-vocabulary point — prevalence and incidence, balance and cash flow, population and births are one distinction — and the principle that stocks integrate their net inflows.

**4.2** **A stock is not any quantity that changes over time.** `0007` already guards this with the refrigerated-warehouse temperature case, and the chapter restates the guard rather than inventing one.

**4.3** Flows are named in pairs. A stock with only its inflow named has not been analysed.

**4.4** **The reader works one accumulation by hand before any vocabulary arrives.** This is not a stylistic choice; see clause 5.

### 5. The chapter's difficulty is asserted from a measurement, not from the author

**5.1** **Beyond 0007**, which made `boothsweeney2000bathtub` conditional on the book making an explicit empirical claim about learner difficulty. **Chapter 13 makes that claim**, so the condition is met and the source is promoted.

**5.2** The chapter reports means of **0.77, 0.48, and 0.41** across three tasks [@boothsweeney2000bathtub, p. 264], the authors' own summary that "In general, performance is poor", and the per-criterion figures of **0.66** for slope-of-stock and **0.63** for area-under-net-rate on the simplest task [@boothsweeney2000bathtub, p. 265].

**5.3** It carries the authors' answer to the two obvious dismissals [@boothsweeney2000bathtub, p. 265]: the concepts are elementary calculus that every subject had studied, and the responses show "conceptual confusion, not arithmetical error."

**5.4** **No previous chapter has been able to justify its own difficulty from a study.** This is the first, and the manuscript says what kind of claim it is.

**5.5 The study's threshold verdicts are not repeated.** [@boothsweeney2000bathtub, p. 278] reports a gender difference as "only marginally significant" and region effects similarly. The chapter uses the study's measurements and none of its significance verdicts, and the gender comparison is not used at all. **This applies Chapter 8's discipline to one of the book's own sources**, which is a first and is recorded as such.

### 6. Delay, overshoot, and oscillation

**6.1** Delay is taught from [@sterman2006evidence, p. 508], with its four consequences: slower evidence, divergent short- and long-run impacts, instability and fluctuation, and overshoot.

**6.2** **The overshoot mechanism is quoted in full**, because the sentence does what no paraphrase does: decision-makers "continue to intervene to correct apparent discrepancies between the desired and actual state of the system even after sufficient corrective actions have been taken to restore equilibrium."

**6.3** **The rule that produces overshoot is a correct rule.** It is the same rule [@astrom2008feedback, p. 17] calls the principle of feedback. The chapter must not let overshoot read as carelessness.

**6.4** Oscillation is taught through the overreaction mechanism at [@astrom2008feedback, p. 24]. **`limit cycle` is named once and not developed**; the phase-plane machinery at pp. 98–101 is deferred by 0007.

**6.5** "Worse-before-better" is taught from [@sterman2006evidence, p. 507], with the observation that it is indistinguishable in the moment from a failing policy.

### 7. Equilibrium and stability, and the distinction between them

**7.1** Both canon entries have stood as `TODO — verify against canonical sources` since Chapter 1. **Both close here.**

**7.2** `equilibrium` is closed from [@astrom2008feedback, p. 100]: a stationary condition for the dynamics; a system can have zero, one, or more.

**7.3** `stability` is closed from [@astrom2008feedback, p. 102]: whether solutions that start nearby remain close, get closer, or move further away.

**7.4** **The distinction the core competence names is the one at [@astrom2008feedback, p. 102]**: equilibrium is a property of a point, stability is a property of the solutions near it. A system can sit at an equilibrium it will not return to.

**7.5** **Three grades are taught in words** — unstable, neutrally stable, asymptotically stable. **No Lyapunov function, no eigenvalues, no linearization, no Routh–Hurwitz.** The source's formal definitions carry symbols and comparison operators and are **paraphrased, not quoted**, under the standing rules from Chapters 7 and 8.

**7.6** Local versus global stability is stated in one sentence. Sink, source, saddle, and centre are named once from [@astrom2008feedback, p. 104] and not used.

### 8. The `robustness` / `stability` collision, announced

**8.1** **Beyond 0007.** Chapter 12 made `robustness` a controlled term; the canon entry already records that it is distinct from stability. The words are near-synonyms in ordinary speech and the book has now made both technical.

**8.2** **This is the fifth collision announcement in the book**, after `validation`, `consistency`, `significance`, and `sensitivity analysis`.

**8.3** The distinction stated: robustness is a property of a **choice** across a set of futures somebody wrote down; stability is a property of a **system** near an operating point. A robust portfolio can sit in an unstable system, and a stable system can be a bad thing to be stable at — the water case's do-nothing equilibrium is stable at 88 ML, below the utility's own critical level.

### 9. Policy resistance

**9.1** Defined from [@sterman2002models, p. 504], the locator Chapter 2 verified, recorded, and was instructed not to use. **The debt is discharged here.**

**9.2** "There are no side effects—just effects" is quoted from [@sterman2006evidence, p. 505]. **Chapter 2 quoted the 2002 wording for a boundary point**; the manuscript must not appear to quote one sentence twice, and the source note records the difference.

**9.3** **Two of the source's examples are used, not ten** — forest fire suppression and flood control [@sterman2006evidence, p. 506]. A list of ten reads as a genre and stops the reader examining the mechanism.

**9.4** **[@sterman2006evidence, p. 510] is carried into the manuscript**: recognising that structure shapes behaviour "does not relieve us of personal responsibility for our actions." A chapter that teaches policy resistance without this teaches a reader to explain away every failure as systemic.

### 10. Simulation returns, bounded

**10.1** Chapter 6 taught Monte Carlo over a distribution. Chapter 13 runs **a trajectory**, which is a different use of the same machinery, and the manuscript says so.

**10.2** It carries [@sterman2006evidence, p. 512]: "a poor model embedded in a potent interface may teach harmful lessons more effectively than ever before."

**10.3** **No differential equations.** Every figure in the chapter is arithmetic on a table the reader can check.

### 11. Notation

**11.1** **None is added.** The sequence stays where 0018 left it and 0019 confirmed.

**11.2** No state-space form, no block diagrams, no causal loop diagrams, no stock-and-flow diagramming notation. `0007` defers the first; clause 10.3 and `research-plan.md` decline the rest.

**11.3** This is the second consecutive chapter to add nothing.

### 12. Vocabulary

**12.1** Introduced here: `stock`, `flow`, `accumulation`, `delay`, `open loop`, `closed loop`, `reinforcing feedback`, `balancing feedback`, `oscillation`, `overshoot`, `policy resistance`, `state space` (named only).

**12.2** Closed here: `equilibrium` and `stability`, both `TODO` since Chapter 1.

**12.3** Developed here: `feedback`, from Chapter 1's screening depth to its formal home.

**12.4** After this chapter, **three `TODO` entries remain in the registry**, and the third is a finding rather than a plan.

- `observability` — Chapter 14, as scheduled.
- `structural identifiability` — Chapter 14, deferred there from Chapter 7 per `../README.md`.
- **`utility` — recorded as "Introduced in: Chapter 11", which is drafted.** Chapter 11 did not close it and [Decision 0018](0018-chapter11-decision-terminology-and-boundary.md) does not mention it. This is consistent with 0018 clause 4.4, which declined to teach risk attitude for want of a source — `utility` is exactly the term that treatment would have required — but the registry still carries a closure that did not happen. **Surfaced here rather than repaired: it touches a drafted chapter and an adjudicated-pending decision, and the fix is the author's.** Logged in `README.md` in this directory.

### 13. What Chapter 13 does not do

- Teach control: no PID, no transfer functions, no Laplace, no Nyquist, no Bode, no controller tuning. Chapter 14.
- Teach stability mathematics: no eigenvalues, no linearization, no Lyapunov functions.
- Teach phase portraits, vector fields, or limit-cycle analysis.
- Teach causal loop diagrams or stock-and-flow diagramming conventions.
- Teach chaos, bifurcation, or catastrophe.
- Teach strategic response, gaming, incentives, or performativity — Chapter 15, and `perdomo2020performative` stays there.
- Teach sequential policies, filtering, observability, or exploration/exploitation — Chapter 14.
- Re-teach Chapter 1's dynamic screen, which the reader has been applying for twelve chapters.
- Reopen Chapter 7's identification verdict or Chapter 5's model criticism.
- Recommend a capital programme — Chapter 12 did that.
- Treat whether a deployed policy is still working — Chapter 17.

## Sources promoted

`boothsweeney2000bathtub` is new to `references.bib`, promoted under the condition `0007` set. `sterman2006evidence` is extended from summary level to verified locators at pp. 505–512 — reading that Chapter 1 recorded as outstanding. `astrom2008feedback` is extended from pp. 27–34 to pp. 1–4, 17–24, and 98–104. `sterman2002models` p. 504 is used for the first time, having been verified and reserved during Chapter 2.

## Known gaps carried forward

1. **Sterman's *Business Dynamics* (2000) was not obtained.** It is the standard textbook for most of this chapter's material, and the book teaches stocks, flows, and delays from a journal article and a test instrument instead. **This is the chapter's largest gap.**
2. **Åström and Murray's second edition was obtained and declined** for want of continuous printed pagination, under the standing rule from Chapter 9.
3. **Forrester (1969, 1971) not obtained**; the policy-resistance argument is taken from two secondary statements of it with checkable pagination.
4. `astrom2008feedback` **§4.4 and §4.5 unread**, deliberately.
5. `sterman2006evidence` **pp. 513–514 unread**.
6. `boothsweeney2000bathtub` **read at four pages of thirty-eight**; the instruments and the manufacturing-case analysis are uncharacterised, and the study is a single-institution convenience sample from 2000.
7. **No source was sought for how often overshoot occurs in practice.** The mechanism is sourced; no frequency is claimed.
8. The **Chapter 13 case is the water anchor's tenth recurrence**, and Chapter 1's Gate 1 remains open.

## No architecture change

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields. Chapter 13 opens Part IV as the architecture specifies.
