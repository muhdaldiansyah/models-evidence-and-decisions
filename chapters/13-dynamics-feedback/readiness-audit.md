# Chapter 13 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 13: **Dynamics, Feedback, and Stability** — the first chapter of Part IV.

**Process note.** As in Chapters 3–12, this audit was written alongside its research. Findings taken from sources are marked. Every locator was taken from reading the document directly.

Current architecture from `README.md` and `spec.md`:

- central question: **How does the system evolve once acted upon?**
- core competence: **Reason about state, accumulation, stocks and flows, delay, feedback, equilibrium versus stability, oscillation, overshoot, and policy resistance.**
- target: 28 pages / 5 serious learning hours.

## 1. Readiness verdict

**Drafting-ready after adjudication**, and unusually well governed, because this chapter is the only one in the book whose scope was written out in advance by an *accepted* decision rather than a proposed one.

Four observations.

**`decisions/0007` is the most detailed boundary document in the repository, and it is Accepted, not proposed.** It was written for Chapter 1 and it says, repeatedly and specifically, what Chapter 13 owns: stocks and flows, formal delays, feedback loops, equilibrium, stability, oscillation, and policy resistance. It also names three sources for the material. **Chapter 13 is the first chapter whose scope arrives pre-adjudicated**, and the drafting decision is correspondingly narrower than its predecessors.

**The core competence names nine things and they are not nine topics.** They are one claim seen at nine angles: *a system that carries something forward reacts to what you do to it, on a schedule you did not choose.* State, accumulation, and stocks and flows are the carrying-forward. Delay is the schedule. Feedback is the reacting. Equilibrium, stability, oscillation, and overshoot are what the combination produces. Policy resistance is what it feels like from inside.

**The chapter has an empirical warrant available that no other chapter in the book has had.** `boothsweeney2000bathtub` tested 182 to 225 MIT Sloan graduate students on stock-flow and delay reasoning and found mean scores of **0.77, 0.48, and 0.41**. A chapter that teaches accumulation can therefore say *this is hard, and here is the measurement*, rather than asserting that readers will find it hard. **No previous chapter has been able to justify its own difficulty from a study.**

**And one debt comes due rather than needing to be found.** `../../sources/sterman2002models.md` carries a verified p. 504 definition of policy resistance and an explicit instruction: "Do not teach policy resistance. `README.md` assigns policy resistance to Chapter 13's core competence... Chapter 2 may not." Chapter 2 recorded the locator and refused to use it. Chapter 13 uses it.

## 2. Unique-job hypothesis

> Teach readers that a system which accumulates, delays, and responds will defeat reasoning that treats an action as a one-way cause — and that the defeat is regular enough to be anticipated rather than merely regretted.

The reader who finishes Chapter 13 should be able to take an intervention, say what stock it changes and through which flow, say what is delayed and by roughly how long, name at least one loop through which the system's response returns to the decision, distinguish *the system settles* from *the system settles back after a knock*, and predict whether the likely failure is overshoot, oscillation, or resistance.

## 3. What earlier chapters have promised

| Promised in | Text | Settled by |
|---|---|---|
| `../../decisions/0007` | "Chapter 13 owns stocks and flows, formal delays, feedback loops, equilibrium, stability, oscillation, and policy resistance" | the whole chapter |
| `../../decisions/0007` | "Formal stock-flow representation and accumulation analysis remain Chapter 13" | §§2–3 |
| `../../decisions/0007` | "Do not introduce `positive feedback` or `negative feedback` in Chapter 1... Formal dynamical feedback belongs primarily to Chapter 13" | §5 |
| `01/spec.md` | dynamic screen deferred here for formal treatment | §§2–6 |
| `02/spec.md` | `state` formal home; "`state space` is not named until Chapter 13" | §2 |
| `02/chapter.md` | dynamics distinguished from mechanism, deferred here | §1 |
| `../../sources/sterman2002models.md` | policy resistance definition recorded and reserved | §7 |
| `12/chapter.md` L1050 | "Chapter 13 starts with the simplest version of the problem: what happens when the effect of an action feeds back into its own cause" | §5 |
| `canon/terminology.md` | `stability` and `equilibrium` both `TODO — verify against canonical sources`, introduced Chapter 13 | §6 |

**Two canon entries have stood open as `TODO` since Chapter 1 and close here.** Only `observability` remains, and it belongs to Chapter 14.

## 4. Neighbouring-chapter boundaries

### Chapter 1 — the screen

Chapter 1 taught the reader to *ask* what carries over, what is delayed, and whether the system responds. It deliberately withheld the vocabulary. Chapter 13 supplies it, which means the chapter must resist re-teaching the screen; the reader has been screening for twelve chapters.

### Chapter 2 — representation and `state`

Chapter 2 introduced `state` as *what must be carried forward*, from `astrom2008feedback` p. 34, and forbade state-space form, order, linearity, reachability, and observability. Chapter 13 may name `state space` and must still refuse the rest.

### Chapter 5 — model criticism

Chapter 5 taught that a model can fail its purpose. Chapter 13's failure modes are dynamic: a model can be right about equilibrium and wrong about the path. This must not become a second general treatment of criticism.

### Chapter 12 — robustness, and a live collision

Chapter 12 taught `robustness` as least-bad-across-futures, and the canon entry already says `robustness` is **distinct from stability (Chapter 13)**. Chapter 13 must announce the collision, because the two words are used interchangeably in ordinary speech and the book has now made both technical.

Chapter 12 also ended by naming this chapter's subject in its last paragraph. That handoff is the strongest in Part III and should be picked up directly rather than restated.

### Chapter 14 — sequential decisions and control

Chapter 14 owns policies, control, filtering, observability, and exploration/exploitation. **The line is sharp and easy to cross:** Åström and Murray's Chapter 1 contains on-off, proportional, and PID control, and the on-off material is genuinely about oscillation. Chapter 13 may use the *mechanism* by which overreaction produces oscillation; it may not teach a controller.

### Chapter 15 — strategic response

Chapter 15 owns incentives, gaming, and performativity. `perdomo2020performative` stays there. Chapter 13's feedback is structural, not strategic: a reservoir does not have interests.

### Chapter 17 — monitoring

Whether a deployed policy is still working is post-deployment. Chapter 13 stops at predicting the dynamic failure.

## 5. Terminology readiness

| Term | State | Source position |
|---|---|---|
| `stock` | new | `sterman2006evidence` p. 508 |
| `flow` | new | same |
| `accumulation` | new | same; empirical difficulty from `boothsweeney2000bathtub` |
| `delay` | new as controlled term | `sterman2006evidence` p. 508 |
| `open loop` / `closed loop` | new | `astrom2008feedback` p. 2 |
| `reinforcing feedback` / `balancing feedback` | new | `sterman2006evidence` p. 507 names self-reinforcing and self-correcting; `astrom2008feedback` p. 22 names positive and negative |
| `state space` | new, named only | `astrom2008feedback` p. 28 |
| `equilibrium` | exists as `TODO`; **closed here** | `astrom2008feedback` p. 100 |
| `stability` | exists as `TODO`; **closed here** | `astrom2008feedback` pp. 102–104 |
| `oscillation` | new | `astrom2008feedback` pp. 24, 101 |
| `overshoot` | new | `sterman2006evidence` p. 508 |
| `policy resistance` | new | `sterman2002models` p. 504 |
| `feedback` | exists at Chapter 1 depth; **developed to formal home** | both sources |

**One collision requiring announcement: `robustness` versus `stability`.** This is the fifth such announcement in the book, after `validation`, `consistency`, `significance`, and `sensitivity analysis`.

**One terminological hazard.** `positive feedback` and `negative feedback` collide with the book's `positive` and `normative`, which is exactly why Decision 0007 banned them from Chapter 1. Recommend the book prefer **reinforcing** and **balancing**, name the positive/negative pair once as the terms readers will meet, and say why the book does not use them.

## 6. High-risk conceptual collapses to prevent

1. **A stock is any quantity that changes over time.** It is not; a stock is what accumulates its net flows. Decision 0007 already guards this with the warehouse-temperature case.
2. **Inputs and outputs are correlated.** `sterman2006evidence` p. 508: a stock rises even as its net inflow falls, provided the net inflow stays positive.
3. **The stock looks like the flow.** `boothsweeney2000bathtub` p. 278 found subjects drawing the stock with the same qualitative shape as the net rate.
4. **Equilibrium means stable.** It does not. The inverted pendulum has an equilibrium pointing straight up.
5. **Stable means it will return to where it was.** Lyapunov stability means nearby solutions *stay near*, not that they converge; that stronger property is asymptotic stability.
6. **Stability is the same as robustness.** Chapter 12's word and this chapter's word are different concepts.
7. **Feedback is a kind of causation you can follow forwards.** `astrom2008feedback` p. 1: reasoning about feedback "leads to a circular argument", and Chapter 7's causal machinery does not straightforwardly apply.
8. **Oscillation means someone is doing something wrong.** It can be the predictable result of a correct-looking correction applied through a delay.
9. **Overshoot is a failure of nerve or discipline.** `sterman2006evidence` p. 508 gives its mechanism: continuing to correct after enough correction has been applied but before its effect is visible.
10. **Policy resistance is the system being perverse.** It is the system responding to the intervention, which is what a system does.
11. **Side effects are a category of effect.** `sterman2002models` p. 505: "There are no side effects—only effects."
12. **A dynamic system contains agents.** The pendulum is Decision 0007's standing counterexample and Åström and Murray use it too.

## 7. Research clusters

1. **Stocks, flows, accumulation — and the evidence that it is hard.**
2. **Delay, and how delay plus correction produces overshoot and oscillation.**
3. **Feedback, equilibrium, and stability.**
4. **Policy resistance, the chapter's own case, and exercise design.**

## 8. Candidate example constraints

The anchor is available for a **thirteenth** recurrence, and for the first time the book must run the case **forward in time** rather than analysing a snapshot.

Constraints:

- The stock must be one the reader has known since Chapter 1 — **usable stored water** — so that accumulation is taught on a quantity whose provenance the reader already distrusts.
- The chapter must contain **one arithmetic accumulation the reader works by hand**, because `boothsweeney2000bathtub` shows that reading about accumulation does not produce it.
- The delay must be **two delays of different lengths** — one information, one physical — because Decision 0007 requires both in the anchor and because overshoot needs the physical one.
- The overshoot must be **produced by a defensible decision rule**, not by an error, or the chapter teaches carelessness instead of dynamics.
- The policy-resistance instance must be one **the book has already recorded**: Chapter 1's conservation request changed demand and invalidated the forecast. No new mechanism.
- No new physical fact about Hillcrest, and no reopening of Chapter 7's identification verdict.

**Gate 1 remains open and is now thirteen chapters deep.**

## 9. Decisions likely required after research

1. **Whether to teach loop polarity, and under what names.** Recommend **yes**, using `reinforcing` and `balancing`, with `positive`/`negative` named once as the terms in circulation and refused for the stated collision.
2. **How far into stability to go.** Recommend the three grades — unstable, neutrally stable, asymptotically stable — stated in words from `astrom2008feedback` pp. 102–103, with **no Lyapunov function, no eigenvalues, no linearization**.
3. **Whether `state space` is named.** Recommend named once, not developed, discharging Chapter 2's promise.
4. **Whether simulation returns.** Chapter 6 taught Monte Carlo. Recommend a bounded return: the chapter simulates a *trajectory*, not a distribution, and carries `sterman2006evidence` p. 512's warning that a poor model in a potent interface "may teach harmful lessons more effectively than ever before."
5. **Whether `boothsweeney2000bathtub` is promoted.** Recommend **yes**. Decision 0007 made promotion conditional on the book making an explicit empirical claim about learner difficulty; Chapter 13 makes exactly that claim, and the primary source is obtainable with checkable pagination.
6. **The `robustness`/`stability` collision announcement.**
7. **The thirteenth water-case recurrence, run forward in time.**

## 10. Drafting gate

Do not draft until:

- `../../decisions/0020` exists in proposed form;
- the terminology block is written, including the two `TODO` closures standing since Chapter 1;
- `case-data.md` freezes the trajectory and **every accumulation figure is computed and checked**;
- `spec.md` records where the Chapter 14 line falls, in terms specific enough to be enforced against the Åström and Murray control material.
