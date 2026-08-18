# Research 04 — Adaptive Plans, and the Chapter's Own Examples

Cluster R04 of `research-plan.md`. Closed.

Source read directly: `lempert2003shaping` printed pp. 57–58.

## 1. Why adaptivity is a route to robustness

> "People learn. Over time, they will gain new information. Accordingly, **adaptive decision strategies are the means most commonly used to achieve robustness because they are designed to evolve in response to new data.** Faced with a multiplicity of plausible futures, a decisionmaker may settle on near-term actions but plan to adjust them in specific ways as new information renders some futures implausible and others more likely." [@lempert2003shaping, p. 57]

And from the chapter opening, the same claim compressed: "Often strategies are robust **because** they are adaptive—that is, they are explicitly designed to evolve in response to new information" [@lempert2003shaping, p. 40].

**"In specific ways."** That is the difference between an adaptive plan and a vague one, and the chapter should lean on it.

The source's own illustration, p. 57–58: "a firm launching a new product in a test market follows an adaptive strategy. If the product sells well, the firm expands distribution. If not, the firm may cancel or revise the offering."

## 2. A named structure

> "Dewar's Assumption-Based Planning process (1993, 2001) provides a framework for designing adaptive strategies. This approach comprises **shaping actions** intended to influence the future that comes to pass, **hedging actions** intended to reduce vulnerability if adverse futures come to pass, and **signposts** or observations that warn of the need to change the mix of actions." [@lempert2003shaping, p. 58]

**Three parts, and the third is the one organisations omit.**

A plan with shaping and hedging actions but no signposts is a portfolio. A plan with signposts is adaptive, because it says in advance what would cause it to change.

**Dewar (1993, 2001) was not obtained**; the structure is used **as reported at** `lempert2003shaping` p. 58.

The same page records that adaptivity has been embraced across fields, naming real options analysis as a tool that has "allowed firms to begin to assign a value to flexibility in ways that were previously not possible" and adaptive management in the environmental community. **This book teaches none of that machinery**, and names it only so the reader knows where to look.

## 3. The honest limit

The source does not promise that robustness is free.

> "one is rarely fortunate enough to engage in LTPA that results in an ideal strategy with good performance properties in all plausible futures judged by all relevant value systems. In practice, long-term decisionmaking becomes an exercise in juggling difficult trade-offs and in judging which values and scenarios should weigh more heavily and which should be downplayed. The choice rests, of course, on a complicated amalgam of moral, political, and goal-defined judgments." [@lempert2003shaping, p. 57]

And the closing requirement, which is the chapter's best single sentence:

> "they should emerge with a robust strategy and a clear understanding of the values and futures for which it performs adequately. **They should also be explicitly aware of the futures and values that, by virtue of selecting the candidate strategy, have been implicitly classed as unimportant.**" [@lempert2003shaping, p. 57]

**That is the book's recurring discipline arriving one last time in Part III.** Chapter 6 made conditioning explicit, Chapter 7 identifying assumptions, Chapter 8 analytic conduct, Chapter 10 values, Chapter 11 the decision rule. Here it is the futures you have decided not to care about.

## 4. The anchor at programme scale

For the first time the anchor scales from one zone to the whole capital programme.

### Seven candidate schemes against the £2.4m envelope

The envelope is Chapter 10's, unchanged.

| | Scheme | Cost £k |
|---|---|---:|
| **A** | Hillcrest variable-speed drive | **40** |
| **B** | Network pressure management | **380** |
| **C** | Zone 4 mains renewal | **620** |
| **D** | Zone 9 mains renewal | **540** |
| **E** | Zone 12 mains renewal | **700** |
| **F1** | Trunk main reinforcement, **stage 1 only** | **900** |
| **F2** | Trunk main reinforcement, **full** | **1,900** |

F1 and F2 are mutually exclusive: the full scheme includes stage 1. Total if everything were built: **£5,080k** against an envelope of **£2,400k**, so the constraint binds hard.

### Benefits under three futures

Household-events avoided per year.

| | A | B | C | D | E | F1 | F2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| **As forecast** | 95 | 190 | 210 | 168 | 175 | 420 | 700 |
| **Demand high** | 70 | 150 | 190 | 150 | 160 | 620 | 1,400 |
| **Demand flat** | 130 | 260 | 280 | 230 | 240 | 60 | 80 |

The three futures are the ensemble. Under **demand high** the trunk main is the only thing that matters; under **demand flat** it is close to a stranded asset and the local schemes carry everything.

## 5. Every figure, computed and checked

### Ratios under the central forecast

| Scheme | Benefit per £k |
|---|---:|
| A | **2.375** |
| B | 0.500 |
| F1 | 0.467 |
| F2 | 0.368 |
| C | 0.339 |
| D | 0.311 |
| E | 0.250 |

### The optimum at £2,400k, central forecast

**A + B + F2**, costing **£2,320k**, benefit **985**.

**£80k is left unspent and there is nothing to buy with it.** The cheapest remaining scheme is D at £540k.

### The shadow price of the envelope

**If the schemes were divisible** — if you could buy a fraction of a mains renewal — the answer would be A, B, F2 in full and then 12.9% of C, giving 1,012.1, and the shadow price would be **C's ratio, 0.339 per £k**. Smooth, single-valued, and exactly what marginal reasoning promises.

**They are not divisible.** The actual marginal value of the envelope, computed by re-optimising:

| Envelope moves from | to | Benefit gained | Per £k |
|---:|---:|---:|---:|
| 2,400 | 2,450 | +3 | **0.060** |
| 2,560 | 2,610 | +0 | **0.000** |
| 2,400 | 2,600 | +98 | 0.490 |
| 2,900 | 2,950 | +42 | **0.840** |

**Three findings, all from the same table.**

An extra £50k can be worth **nothing at all**.

The value depends on how far you move, not just where you are — 0.060 for fifty thousand and 0.490 for two hundred.

And **the marginal value is higher at a larger envelope than at a smaller one** — 0.840 at £2.9m against 0.060 at £2.4m. Under convexity that cannot happen, and it is why *spend until marginal benefit equals marginal cost* has no fixed point here.

### The optimum in each future

| Future | Optimal portfolio | Cost | Benefit |
|---|---|---:|---:|
| As forecast | **A + B + F2** | 2,320 | 985 |
| Demand high | **A + B + F2** | 2,320 | 1,620 |
| Demand flat | **A + B + C + D + E** | 2,280 | 1,140 |

### The regret table

Regret is the shortfall against the best that portfolio could have achieved in that future.

| Portfolio | Cost | As forecast | Demand high | Demand flat | **Max regret** |
|---|---:|---:|---:|---:|---:|
| A + B + F2 | 2,320 | 0 | 0 | 670 | **670** |
| A + B + C + D + E | 2,280 | 147 | 900 | 0 | **900** |
| **A + C + E + F1** | 2,260 | 85 | 580 | 430 | **580** |
| **A + B + C + F1** | 1,940 | 70 | 590 | 410 | **590** |

**The minimum-maximum-regret portfolio is A + C + E + F1, at 580.**

**It is optimal in no future.** That is the demonstration, and it is what `lempert2003shaping` p. 52 predicts: a strategy that "performs reasonably well compared to the alternatives across a wide range of plausible futures" rather than best in any of them.

**And 580 against 590 is not a real difference.** Savage's first documented pathology — that the rule "often yields neither a best strategy nor a simple ordering among strategies" [@lempert2003shaping, p. 53, n. 13] — arrives immediately on the anchor's own numbers.

**A + B + C + F1 costs £1,940k, leaving £460k unspent.** That is not waste: it is uncommitted capital in a decision about an uncertain future, and §7 is where it becomes an adaptive plan.

## 6. The adaptive plan

Using the reported structure [@lempert2003shaping, p. 58]:

**Shaping actions** — B, network pressure management, which reduces demand on every zone and makes several futures less bad.

**Hedging actions** — A and C, cheap and useful in every future; and **F1 rather than F2**, which buys the trunk capacity that all futures need without committing to the capacity only one future needs.

**Signposts** — observations that would trigger stage 2. The utility already has them: peak-week demand against the Chapter 1 forecast, and the count of heat events per summer. **A named threshold on each, agreed in advance, is what turns the portfolio into a plan.**

The staging is not free. Building stage 2 later is assumed to cost **£1,150k** against the £1,000k it would have added today — a **£150k premium** for the option.

**That premium is the price of the flexibility**, and stating it is what stops adaptive planning being a way of avoiding decisions.

## 7. Prohibitions for the manuscript

- No algorithm, formulation, or notation beyond a table.
- No claim that any portfolio is recommended.
- No claim that any value is typical of water utilities.
- Savage and Dewar cited **as reported at** `lempert2003shaping`.
- Real options, adaptive management, and Lempert's own method named at most.
- No presentation of minimax regret as the right rule; its four pathologies are carried.
- The £150k staging premium is stated as an assumption, not a measurement.
- No recommendation for the utility.

## 8. Stop condition

Met. The adaptivity/robustness link recorded; the three-part structure recorded with its attribution; the honest limit and the implicitly-unimportant-futures requirement recorded; every anchor figure computed and checked — ratios, the optimum, both shadow prices, the three futures' optima, the full regret table, and the minimax portfolio.
