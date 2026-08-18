# Chapter 12 Programme Case Data

Status: drafting freeze. Extension of the Chapter 1–11 case-data files, all of which remain authoritative for every value they contain.

All values here are **synthetic authoring data**. They are not industry averages, regulatory standards, design guidance, or values from any real utility.

## What this file adds

For the first time the anchor **scales**. Every previous chapter concerned one zone and, from Chapter 10, one choice. The governed central question says *at scale*, so the object of choice becomes the whole capital programme.

Nothing physical is new. The envelope is Chapter 10's, the zones are the network's, and the uncertainty is about demand rather than about mechanisms.

## Carried forward

| From | Item |
|---|---|
| Ch 1 | Demand forecast conditional on no new action |
| Ch 10 | Capital envelope **£2.4m** for 2027/28 — an annual planning convention with a precedent for exceptions |
| Ch 10 | Three zones scheduled for mains renewal from the same envelope |
| Ch 10 | The variable-speed drive, and the housing constraint that dissolved |
| Ch 11 | Expected value as a rule whose use is a choice |

## The seven candidate schemes

| | Scheme | Cost £k |
|---|---|---:|
| **A** | Hillcrest variable-speed drive | **40** |
| **B** | Network pressure management | **380** |
| **C** | Zone 4 mains renewal | **620** |
| **D** | Zone 9 mains renewal | **540** |
| **E** | Zone 12 mains renewal | **700** |
| **F1** | Trunk main reinforcement, **stage 1 only** | **900** |
| **F2** | Trunk main reinforcement, **full** | **1,900** |

**F1 and F2 are mutually exclusive**; the full scheme includes stage 1.

Everything would cost **£5,080k** against an envelope of **£2,400k**. The constraint binds hard.

## Three futures

Benefits are household-events avoided per year.

| | A | B | C | D | E | F1 | F2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| **As forecast** | 95 | 190 | 210 | 168 | 175 | 420 | 700 |
| **Demand high** | 70 | 150 | 190 | 150 | 160 | 620 | 1,400 |
| **Demand flat** | 130 | 260 | 280 | 230 | 240 | 60 | 80 |

Under **demand high** the trunk main dominates. Under **demand flat** it is close to a stranded asset and the local schemes carry everything.

**The futures are an ensemble, not forecasts**, and no probabilities are attached to them.

## Every figure, computed and checked

### Ratios under the central forecast

| Scheme | Benefit per £k |
|---|---:|
| **A** | **2.375** |
| B | 0.500 |
| F1 | 0.467 |
| F2 | 0.368 |
| C | 0.339 |
| D | 0.311 |
| E | 0.250 |

### The optimum at £2,400k, central forecast

**A + B + F2**, costing **£2,320k**, benefit **985**.

**£80k left unspent, with nothing to buy.** The cheapest remaining scheme is D at £540k.

### What the ratio ranking gives instead

Funding down the ratio order until the money runs out gives **A + B + F1 + C** — £1,940 spent, benefit **915**, **£460k left over**.

**The ranking misses the optimum by 70**, and it misses because F2 has a worse ratio than F1 and still belongs in the answer.

**And it lands on A + B + C + F1**, which reappears below as the near-tied robust portfolio. The ratio rule found a defensible portfolio for the wrong reason.

### The shadow price of the envelope

**If the schemes were divisible**: A, B and F2 in full, then 12.9% of C, giving **1,012.1** — and the shadow price would be C's ratio, **0.339 per £k**. Smooth and single-valued.

**They are not divisible.** Re-optimising at different envelopes:

| Envelope moves | Benefit gained | Per £k |
|---|---:|---:|
| 2,400 → 2,450 | +3 | **0.060** |
| 2,560 → 2,610 | **+0** | **0.000** |
| 2,400 → 2,600 | +98 | 0.490 |
| 2,900 → 2,950 | +42 | **0.840** |

**Three findings.** An extra £50k can be worth nothing. The value depends on how far you move. And the marginal value is **higher** at a larger envelope than at a smaller one — which cannot happen under convexity.

### The optimum in each future

| Future | Optimal portfolio | Cost | Benefit |
|---|---|---:|---:|
| As forecast | **A + B + F2** | 2,320 | 985 |
| Demand high | **A + B + F2** | 2,320 | 1,620 |
| Demand flat | **A + B + C + D + E** | 2,280 | 1,140 |

### The regret table

| Portfolio | Cost | As forecast | Demand high | Demand flat | **Max regret** |
|---|---:|---:|---:|---:|---:|
| A + B + F2 | 2,320 | 0 | 0 | 670 | **670** |
| A + B + C + D + E | 2,280 | 147 | 900 | 0 | **900** |
| **A + C + E + F1** | 2,260 | 85 | 580 | 430 | **580** |
| A + B + C + F1 | 1,940 | 70 | 590 | 410 | **590** |

**The minimum-maximum-regret portfolio is A + C + E + F1, and it is optimal in no future.**

**580 against 590 is not a real difference.** Savage's own first pathology — that the rule "often yields neither a best strategy nor a simple ordering among strategies" — arrives on the anchor's own numbers, and the manuscript says so rather than presenting a winner.

**A + B + C + F1 costs £1,940k, leaving £460k uncommitted.** That is not waste in a decision about an uncertain future.

## The adaptive plan

Using the structure reported at `lempert2003shaping` p. 58:

**Shaping actions** — B, network pressure management, which reduces demand across every zone and makes several futures less bad.

**Hedging actions** — A and C, useful in every future; and **F1 rather than F2**, buying the trunk capacity all futures need without committing to the capacity only one future needs.

**Signposts** — the utility already collects both: peak-week demand against the Chapter 1 forecast, and heat events per summer. **A named threshold on each, agreed in advance, is what turns a portfolio into a plan.**

**The staging premium.** Building the trunk main's second stage later is assumed to cost **£1,150k**, against the **£1,000k** it would have added today — a **£150k premium**.

**This is an assumption, not a measurement**, and stating it is what stops adaptive planning being a way of avoiding decisions.

## Prohibited interpretations

Do not write or imply that:

- any cost or benefit here is typical of water utilities;
- any portfolio is recommended;
- the ratios give the optimal programme — greedy ranking happens to agree at £2.4m and does not in general;
- a shadow price is a fixed property of the envelope;
- the three futures are probabilities, or exhaust the possibilities;
- minimax regret is the right rule;
- 580 is meaningfully better than 590;
- robustness is free — it costs performance in whichever future arrives;
- the staging premium is measured;
- annual review is a signpost;
- any of this tells the utility what to build.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water utility SME should review the seven schemes, the plausibility of a phaseable trunk reinforcement, the three futures, and in particular whether a trunk main can be usefully staged at roughly half cost.

**These facts inherit Chapter 1's open Gate 1, now twelve chapters deep.** Twelve case-data files now extend one anchor whose operating story has never been reviewed by a domain expert.
