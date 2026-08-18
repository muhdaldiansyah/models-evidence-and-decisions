# Research 04 — When Analysis Is Not Worthwhile, and the Chapter's Own Examples

Cluster R04 of `research-plan.md`. Closed.

Sources: `colyvan2016voi` pp. 304–306 and footnote 16 at p. 308, read directly; `bradley2016structured` p. 7, read for Chapter 10.

## 1. The chapter turns on itself

The governed core competence ends with "recognition of when further analysis itself is not worthwhile", and two read sources support it.

**The analysis has a cost.** `colyvan2016voi` footnote 16, printed p. 308:

> "In some cases we also need to factor in the cost of the value of information study itself. Sometimes these studies require considerable resources (additional scenario modelling and the like) and this cost should not be ignored."

**A value-of-information study is itself a study**, and it can cost more than the information it is pricing. That is not a paradox; it is a reason the cheap version — the perfect-information ceiling — is the one worth running first.

**And formal method is not always warranted.** Carried from Chapter 10, `bradley2016structured` p. 7: "single issue, well-defined decisions do not need a formal methodology for successful outcomes."

## 2. Three kinds of information gathering

`colyvan2016voi` p. 306 makes a distinction the chapter needs:

> "(1) information gathered for pure science, for intellectual curiosity and with no intended benefits for practical decisions (2) information gathered for the purposes of improving a specific well-defined decision and (3) information gathered because it might be useful for some ill-defined or unknown decision down the track."

And the operative worry:

> "The question is how to guard against cases of (3) which might slip though under the guise of (1) or gesturing towards (2)". [@colyvan2016voi, p. 306]

**Value of information applies to (2) and only to (2).** The paper accepts that (1) has a place — "Surely there should be a place for (1), pure scientific research, and it might be argued that such research is not an appropriate target for value of information studies" [@colyvan2016voi, p. 306].

**Category (3) is where most organisational data collection lives**, and it is the category the machinery cannot price and should not be used to bless.

## 3. The anchor, and what it must close

Chapter 2 named the pump test. Chapter 5 confirmed it was obtainable and had not been done. Chapter 6 computed that it moves belief from roughly 2:1 to either 10:1 or 1:3 and called it "decisive in both directions". Chapter 7 established the pump *effect* was not identified. Chapter 9 found that five sources do not transport.

**Chapter 11 asks whether the test is worth running, and the answer is no.**

That is the honest close to the book's evidence thread, and the manuscript must not soften it into a lesson about being careful.

## 4. The decision, narrowed

Chapter 10 produced seven alternatives. Three are carried forward, and **the criterion for the narrowing is stated rather than assumed**: one act per mechanism, plus one act that works under either.

| | Act | Why it is in the table |
|---|---|---|
| **A** | Fit a variable-speed drive to the existing duty pump — **£40,000** | acts on Mechanism A |
| **B** | Reline the feeder main — **£260,000** | acts on Mechanism B |
| **C** | Targeted contingency for the 40 households, three years — **£36,000** | acts on neither mechanism, and works under both |

The four dropped alternatives are named in the manuscript with the reason.

## 5. The payoff table

Total cost over three years, in £ thousands, **lower is better**. Each cell is capital plus a stated monetisation of remaining household-events.

| Act | If Mechanism A operates | If Mechanism B operates |
|---|---:|---:|
| **A** — variable-speed drive | **130** | **250** |
| **B** — reline the main | **330** | **300** |
| **C** — targeted contingency | **216** | **216** |

**Act C has no spread.** That is deliberate and it is what makes risk attitude demonstrable without any machinery.

**The monetisation is a value judgment**, not a measurement, and `colyvan2016voi` p. 305's single-currency limitation applies to it directly. The manuscript must say so.

## 6. Every number, computed and checked

Prior from Chapter 6, unchanged: **7 : 4** for Mechanism A, so `p(A) = 7/11 ≈ 0.636`.

### Expected cost at the prior

| Act | Arithmetic | Expected cost |
|---|---|---:|
| A | `0.636 × 130 + 0.364 × 250` | **173.6** |
| B | `0.636 × 330 + 0.364 × 300` | **319.1** |
| C | — | **216.0** |

**Best act: A, at £173,600.**

### The test, from Chapter 6's likelihoods

Recovery expected with probability 0.85 under Mechanism A, 0.15 under Mechanism B.

`P(positive) = (7/11)(0.85) + (4/11)(0.15) = ` **0.596**
`P(negative) = ` **0.404**

Posteriors, matching Chapter 6 exactly: **0.908** for A after a positive; **0.236** for A after a negative, i.e. **76%** for B.

### Best act on each branch

| | p(A) | Act A | Act B | Act C | Best |
|---|---:|---:|---:|---:|---|
| Positive | 0.908 | **141.0** | 327.3 | 216.0 | **A** |
| Negative | 0.236 | 221.7 | 307.1 | **216.0** | **C** |

**The test changes the act only on the negative branch, and only by £5,700.**

### The value of the test

`Expected cost with the test = 0.596 × 141.0 + 0.404 × 216.0 = ` **171.3**
`Expected cost without it = ` **173.6**

**Value of the test = £2,300.**

The test costs **£8,000** — a day of elevated pumping, a crew, instrumentation, and a planned service risk.

**Do not run it.**

### The ceiling

Under perfect knowledge of which mechanism operates: choose A if Mechanism A (130), choose C if Mechanism B (216).

`0.636 × 130 + 0.364 × 216 = ` **161.3**

**Value of perfect information = 173.6 − 161.3 = £12,400.**

**No study of this question, however good, can be worth more than £12,400.** That is one line of arithmetic and it disposes of every study proposal before any of them is costed.

### The indifference point

Act A beats Act C when `130p + 250(1−p) < 216`, that is when `p > 34/120 = ` **0.283**.

The prior is **0.636**, comfortably above. Even the negative branch's **0.236** is only just below.

**Which is why the value of information is small**, and it is the same finding from the other direction: the critical value is far from where belief sits, so almost nothing you could learn moves the act.

*All figures above were computed and checked before the manuscript was written.*

## 7. What the chapter must not do

- Present the £2,300 as a criticism of Chapter 6. The 91% was correct and about a different question.
- Present the monetisation as a measurement.
- Teach utility functions, certainty equivalents, or risk premiums.
- Write any formula; every figure is arithmetic.
- Cite Rhodes et al. (2011) or Møller and Fiedler (2010) directly; both are as reported.
- Use the term "Ellsberg paradox" or describe those experiments; the source was not obtained.
- Enter game theory, which `colyvan2016voi` reaches at p. 306.
- Present VOI as applicable to category (1) or (3) information gathering.
- Recommend an act for the utility.

## 8. Stop condition

Met. The three-cases distinction recorded; the cost of the analysis recorded from footnote 16; the acts, table, and every derived figure computed and checked; the narrowing criterion stated.
