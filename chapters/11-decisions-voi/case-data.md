# Chapter 11 Decision Case Data

Status: drafting freeze. Extension of the Chapter 1–10 case-data files, all of which remain authoritative for every value they contain.

All values here are **synthetic authoring data**. They are not industry averages, regulatory standards, design guidance, or values from any real utility.

## What this file adds

Chapter 11 introduces **no new case and no new uncertainty**. Its two states are Chapter 2's mechanisms and its probabilities are Chapter 6's, unchanged.

It adds three acts narrowed from Chapter 10's seven, a payoff table, and the arithmetic that closes the book's longest-running thread.

## Carried forward, unchanged

| From | Item |
|---|---|
| Ch 2 | **Mechanism A** — pump capacity limits refill; **Mechanism B** — friction loss along the old feeder main |
| Ch 6 | Prior odds **7 : 4** for Mechanism A, so `p(A) = 7/11 ≈ 0.636` |
| Ch 6 | Pump-test likelihoods: recovery expected with probability **0.85** under A, **0.15** under B |
| Ch 6 | Posteriors: **0.908** for A after a recovery; **0.236** for A after none, i.e. **76%** for B |
| Ch 10 | Seven alternatives, three fundamental objectives, four stated conflicts |

## The narrowing, and its criterion

Chapter 10 produced seven alternatives. Three are carried into the table, and **the criterion is stated rather than assumed**: one act for each mechanism, plus one act that works under either.

| | Act | Capital / cost | Why it is in the table |
|---|---|---:|---|
| **A** | Fit a variable-speed drive to the existing duty pump | **£40,000** | acts on Mechanism A |
| **B** | Reline the feeder main | **£260,000** | acts on Mechanism B |
| **C** | Targeted contingency for the 40 households, three years | **£36,000** | acts on neither mechanism, and works under both |

**Dropped, with reasons:** the pressure-managed sub-zone and local storage are variants of C at higher cost; the deliberate arranged upgrade and the instrument-and-defer option are information-gathering acts and belong to §5 rather than to the table; the like-for-like replacement was dominated by A on Chapter 10's own constraint analysis.

## The payoff table

Total cost over three years, in **£ thousands**, **lower is better**. Each cell is capital plus a stated monetisation of remaining household-events.

| Act | If Mechanism A operates | If Mechanism B operates |
|---|---:|---:|
| **A** — variable-speed drive | **130** | **250** |
| **B** — reline the main | **330** | **300** |
| **C** — targeted contingency | **216** | **216** |

**Act C has no spread.** That is deliberate: it makes risk attitude visible without any machinery.

**The monetisation is a value judgment, not a measurement.** Chapter 10 produced three fundamental objectives; reducing them to one number per cell is exactly the single-currency step `colyvan2016voi` p. 305 names as a limitation of this machinery. A different monetisation gives a different table.

## Every figure, computed and checked

### Expected cost at the prior

| Act | Arithmetic | Expected cost |
|---|---|---:|
| A | `0.636 × 130 + 0.364 × 250` | **173.6** |
| B | `0.636 × 330 + 0.364 × 300` | **319.1** |
| C | — | **216.0** |

**Best act at the prior: A, at £173,600.**

### The test

`P(recovery) = (7/11)(0.85) + (4/11)(0.15) = ` **0.596**; `P(no recovery) = ` **0.404**.

| Branch | p(A) | Act A | Act B | Act C | Best |
|---|---:|---:|---:|---:|---|
| Recovery | 0.908 | **141.0** | 327.3 | 216.0 | **A** |
| No recovery | 0.236 | 221.7 | 307.1 | **216.0** | **C** |

**The test changes the act only on the no-recovery branch, and only by £5,700.**

### The value of the test

| | £ thousands |
|---|---:|
| Expected cost **with** the test | `0.596 × 141.0 + 0.404 × 216.0 = ` **171.3** |
| Expected cost **without** it | **173.6** |
| **Value of the test** | **2.3** |

**The test costs £8,000** — a day of elevated pumping, a crew, instrumentation, and a planned service risk.

**Value £2,300 against a cost of £8,000. Do not run it.**

### The ceiling

Under perfect knowledge: choose A if Mechanism A (130), choose C if Mechanism B (216).

`0.636 × 130 + 0.364 × 216 = ` **161.3**

**Value of perfect information = 173.6 − 161.3 = £12,400.**

**No study of this question, however good, can be worth more than £12,400.**

### The indifference point

Act A beats Act C when `130p + 250(1−p) < 216`, that is when `p > 34/120 = ` **0.283**.

| | p(Mechanism A) | Relative to 0.283 |
|---|---:|---|
| Prior | **0.636** | comfortably above |
| After a recovery | **0.908** | far above |
| After no recovery | **0.236** | just below |

**Which is why the value of information is small.** The critical value is far from where belief sits, so almost nothing the utility could learn moves the act.

## Prohibited interpretations

Do not write or imply that:

- any figure here is typical of water utilities, or that the monetisation is a measurement;
- the £2,300 shows Chapter 6 was wrong — the 91% was correct and about a different question;
- a low value of information means the mechanism question does not matter, rather than that it does not matter **for this decision**;
- Act C is the safe choice, or that risk aversion is an error;
- expected value is the right rule, rather than **a** rule whose use is a choice;
- the three acts are the only acts, or that the narrowing was neutral;
- perfect information is available, or that £12,400 is what anyone would pay;
- the analysis itself is free;
- any of this tells the utility what to do.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water utility SME should review the three acts, their costs, the plausibility of the payoff table, and in particular the monetisation of household-events — which carries more of the result than any other number in this file.

**These facts inherit Chapter 1's open Gate 1, now eleven chapters deep.** Eleven case-data files now extend one anchor whose operating story has never been reviewed by a domain expert.
