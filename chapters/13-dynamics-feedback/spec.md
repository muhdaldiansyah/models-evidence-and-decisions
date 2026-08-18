---
chapter: 13
part: 4
title: "Dynamics, Feedback, and Stability"
status: drafted
pages_target: 28
hours_target: 5
---

# Chapter 13: Dynamics, Feedback, and Stability

**Provisional.** This specification is built on proposed `../../decisions/0020-chapter13-dynamics-terminology-and-boundary.md` and inherits its status. Its scope, however, rests substantially on **Accepted** `../../decisions/0007`, which set Chapter 13's boundary in advance.

## Central question

How does the system evolve once acted upon?

*Governed by `README.md`. Not amendable here.*

## Core competence

Reason about state, accumulation, stocks and flows, delay, feedback, equilibrium versus stability, oscillation, overshoot, and policy resistance.

*Governed by `README.md`. Not amendable here.*

## Role in the book

Chapter 13 opens Part IV, and Part IV is where the book stops treating the system as something that holds still while it is analysed.

**Parts I–III assumed an open loop.** Chapter 1 framed a decision, Chapters 2–5 built and criticised a representation, Chapters 6–9 estimated and combined, Chapters 10–12 chose. In all of it the network sat there and the utility acted on it. Chapter 13 closes the loop.

**Its unique job:**

> Teach readers that a system which accumulates, delays, and responds will defeat reasoning that treats an action as a one-way cause — and that the defeat is regular enough to be anticipated rather than merely regretted.

The chapter is where three of the book's threads meet. Chapter 1's dynamic screen gets its vocabulary. Chapter 7's causal machinery meets a case it cannot be applied to in its usual form. Chapter 12's adaptive plan gets the theory of why a trigger fires too late.

## Hard prerequisites

- Chapter 1's dynamic-and-responsive screen, and its finding that the demand forecast was conditional on no new action.
- Chapter 2's `state` — what must be carried forward.
- Chapter 4's finding that the demand figure is a subtraction residual.
- Chapter 7's identification verdict and the sixty-eight-year-old Hillcrest main.
- Chapter 12's adaptive plan, signposts, and `robustness`.

## Soft dependencies / spiral links

- Chapter 5's model criticism — the chapter's failures are dynamic, not a second general treatment.
- Chapter 6's simulation — returns as a trajectory rather than a distribution.
- Chapter 8's discipline about threshold verdicts — applied here to one of the book's own sources.
- Chapter 11's expected value — not used; there are no probabilities in this chapter.

## Established concepts to cover

State and what carries forward. Stocks, flows, and accumulation. Information delay and action delay. Open and closed loop. Reinforcing and balancing feedback. Equilibrium. Stability, in three grades. Oscillation. Overshoot. Policy resistance.

## Terminology to introduce or stabilize

**Introduced:** `stock`, `flow`, `accumulation`, `delay`, `open loop`, `closed loop`, `reinforcing feedback`, `balancing feedback`, `oscillation`, `overshoot`, `policy resistance`, `state space` (named only).

**Closed from `TODO`:** `equilibrium`, `stability` — both open since Chapter 1.

**Developed:** `feedback`, from Chapter 1's screening depth to its formal home.

**Collision announced:** `robustness` (Chapter 12) versus `stability` (here). The fifth such announcement in the book.

**Refused:** `positive feedback` and `negative feedback`, named once and not adopted, because `positive` is a controlled term in this book paired with `normative`. Per `../../decisions/0007` and `0020` clause 3.

## Interfaces with other chapters

| Chapter | Interface |
|---|---|
| 1 | supplies the screen; Chapter 13 supplies the vocabulary and must not re-teach the screen |
| 2 | supplies `state`; Chapter 13 names `state space` and develops no further |
| 5 | supplies model criticism; Chapter 13's failures are dynamic |
| 6 | supplies simulation; Chapter 13 runs a trajectory and carries the pitfall warning |
| 7 | supplies causal machinery; Chapter 13 states once where it does not apply |
| 12 | supplies signposts; Chapter 13 explains why a stock-keyed trigger fires late |
| 14 | owns control, policies, filtering, observability |
| 15 | owns strategic response, incentives, performativity |
| 17 | owns whether a deployed policy is still working |

## Scope boundary

### Core

Accumulation worked by hand. Two delays and their sum. The feedback loop as a configuration. Equilibrium as a stationary condition. Stability as a property of nearby solutions, in three grades. Overshoot from delayed correction. Oscillation from overreaction. Policy resistance.

### Deferred to later chapters

Control laws, policies, filtering, observability, structural identifiability, exploration/exploitation (Chapter 14). Strategic response, incentives, gaming, performativity (Chapter 15). Post-deployment monitoring (Chapter 17).

### Deferred to depth curriculum

Differential equations. Phase portraits and vector fields. Limit-cycle analysis. Lyapunov functions, eigenvalues, linearization. Transfer functions, Laplace, Nyquist, Bode, PID. Chaos, bifurcation, catastrophe. Causal loop and stock-and-flow diagramming conventions. Agent-based and discrete-event simulation.

## Section architecture

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | The Reservoir Does Not Hold Still | 2 | 0.30 |
| 2 | What Carries Forward | 4 | 0.70 |
| 3 | Accumulation, and Why It Is Hard | 5 | 0.95 |
| 4 | Two Delays, and Their Sum | 4 | 0.75 |
| 5 | Closing the Loop | 4 | 0.75 |
| 6 | Equilibrium Is Not Stability | 4 | 0.70 |
| 7 | Policy Resistance | 3 | 0.55 |
| 8 | Cold-Start Practice and Retrieval | 2 | 0.30 |

Eight sections, 28 pages, 5 hours. Roughly 360 words per page — about **10,080 words**.

Three self-explanation pauses: §3 (why is storage still falling?), §4 (when should the order have been placed?), §6 (is 88 ML an equilibrium?).

## Examples / recurring cases

**The water anchor's thirteenth recurrence, and the first run forward in time.**

The stock is usable stored water — known since Chapter 1 and distrusted since Chapter 1. Frozen in `case-data.md`. Every figure computed and checked by simulation before drafting.

Contrast cases: the inverted pendulum, which is `../../decisions/0007`'s standing counterexample and is also `astrom2008feedback`'s worked example; forest fire suppression and flood control, both from `sterman2006evidence` p. 506 and both labelled as the source's examples.

## Exercise architecture

Per `../../decisions/0008`. Opening task before any vocabulary; three pauses; a five-defect diagnosis; cold transfer on two parallel forms; retrieval from memory; delayed retest.

**One design constraint is unusual and is load-bearing.** The opening task asks the reader to produce the storage trajectory *before* §2 defines a stock, because `boothsweeney2000bathtub` measured what people do unaided and a reader who has been told the answer cannot discover that they would have got it wrong.

## Transfer target

> Given a stock with named inflows and outflows, a table of flows over time, two delays of different kinds, and a written trigger rule, produce the stock trajectory, identify the minimum and when it occurs, show why the rule fires too late, price what the delay cost, propose a rule keyed to a different variable, and say what that repair costs.

### Parallel forms

- **Form A — a hospital's blood platelet inventory** (clinical logistics).
- **Form B — a district heating network's fuel store** (municipal energy).

Both supply: a stock with two named flows; a demand table over a shock; a verification delay and a resupply delay; a written stock-keyed trigger; a capacity limit that makes overshoot cost something; and a flow-keyed alternative that protects at a price.

Every prior transfer and contrast domain is excluded. Neither domain is sensitive.

Chapter 13 must not claim durable far transfer.

## Evidence / source plan

### Load-bearing sources

| Claim | Source |
|---|---|
| Feedback, and why causal reasoning goes circular | `astrom2008feedback` p. 1 |
| Open and closed loop | `astrom2008feedback` p. 2 |
| Feedback buys insensitivity and can cause instability | `astrom2008feedback` p. 3 |
| The principle of feedback; feedback is reactive | `astrom2008feedback` pp. 17, 22 |
| Reinforcing feedback and its saturation | `astrom2008feedback` p. 22 |
| Oscillation from overreaction | `astrom2008feedback` p. 24 |
| Equilibrium as a stationary condition; zero, one, or more | `astrom2008feedback` p. 100 |
| Stability as a property of nearby solutions; neutral stability | `astrom2008feedback` p. 102 |
| Sink, source, saddle, centre | `astrom2008feedback` p. 104 |
| Stocks and flows across vocabularies | `sterman2006evidence` p. 508 |
| Stocks integrate their net inflows | `sterman2006evidence` p. 508 |
| Delay, and the overshoot mechanism | `sterman2006evidence` p. 508 |
| Doing and undoing have different time constants | `sterman2006evidence` p. 507 |
| Worse-before-better | `sterman2006evidence` p. 507 |
| Reinforcing and balancing named in the other tradition | `sterman2006evidence` p. 507 |
| There are no side effects | `sterman2006evidence` p. 505 |
| Structure does not remove responsibility | `sterman2006evidence` p. 510 |
| The simulation pitfall | `sterman2006evidence` p. 512 |
| Policy resistance defined | `sterman2002models` p. 504 |
| Accumulation is measurably hard | `boothsweeney2000bathtub` pp. 264–265, 278 |

### Not cited

`perdomo2020performative` — Chapter 15's. Sterman's *Business Dynamics* — not obtained; recorded as the chapter's largest gap.

## Failure modes this chapter should prevent

1. A stock is any quantity that changes over time.
2. Inputs and outputs are correlated.
3. The stock has the same shape as the net flow.
4. Equilibrium means stable.
5. Stable means it will return to where it was.
6. Stability is the same as robustness.
7. Feedback is a kind of causation you can follow forwards.
8. Oscillation means somebody did something wrong.
9. Overshoot is a failure of nerve or discipline.
10. Policy resistance is the system being perverse.
11. Side effects are a category of effect.
12. A dynamic system contains agents.
13. Recognising that structure shapes behaviour removes personal responsibility.

## Open questions

1. **Decision 0020 is unadjudicated**, as are 0009–0019.
2. **Sterman's *Business Dynamics* was not obtained.** The chapter teaches stocks, flows, and delays from a journal article and a test instrument.
3. **`utility` is recorded as Chapter 11's and was not closed there.** Surfaced by Decision 0020 clause 12.4; not repaired.
4. **Gate 1 remains open**, now ten chapters deep.
