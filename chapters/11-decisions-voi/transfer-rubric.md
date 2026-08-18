# Chapter 11 — Cold-Transfer Rubric

Status: reader-delivery copy. Governed by `spec.md` (Rubric dimensions) and `transfer.md`.

**Do not read this before your response is complete.** It contains the answers.

Score each dimension 0, 1, or 2. Both forms use the same rubric.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Dominance | Missed | Act B noticed as expensive | Named as dominated, **with the point that it needs no probabilities** |
| Expected values | Not computed | Computed | Computed **and** the best act named |
| The rule named | Not addressed | Called "expected value" | Named **and** what using it assumes stated |
| Risk | Not addressed | Act C noticed as flat | The cost of choosing it computed, **and not called an error** |
| Critical value | Not found | Found | Found **and** compared with the prior |
| Value of Study 1 | Not computed | Computed | Computed **and** compared with its cost, with a verdict |
| The ceiling used | Not computed | Computed | Used to dispose of Study 2 **without further computation** |
| Value judgments named | None | One | Two, **both genuinely non-measurements** |

## Form A — rail grinding

### Dominance

**Act B is dominated by Act C.** 3,400 against 2,000 in one state and 3,300 against 2,000 in the other — worse in both.

**It needs no probabilities to eliminate**, which is the scored point. A panel debating a £3.2m rail replacement is debating something the table settled before anyone weighted anything.

### Expected costs

`p(rolling contact fatigue) = 5/8 = ` **0.625**

| Act | Arithmetic | Expected cost |
|---|---|---:|
| **A** | `0.625 × 1100 + 0.375 × 2600` | **1,662.5** |
| B | `0.625 × 3400 + 0.375 × 3300` | 3,362.5 |
| C | — | 2,000.0 |

**Best: A, at £1,662,500.**

### The rule, and risk

Expected value. Using it treats a certainty of £1.66m as equivalent to a gamble between £1.1m and £2.6m — which assumes indifference to spread.

**Act C has no spread**, at 2,000 either way. A panel that will not accept a £2.6m outcome chooses C and pays `2000.0 − 1662.5 = ` **£337,500** in expectation for it.

**That is not an error**, and a response calling it one loses the mark.

### Critical value

A beats C when `1100p + 2600(1−p) < 2000`, so `p > 600/1500 = ` **0.400**.

The register's odds put p at **0.625**. Above, but **not comfortably** — the prior would have to fall by a third for the answer to change. That is a much closer call than it first appeared, and it is why Study 1 turns out to be worth having.

### Study 1

`P(positive) = 0.625 × 0.80 + 0.375 × 0.25 = ` **0.594**; `P(negative) = ` **0.406**

Posteriors: **0.842** after positive; **0.308** after negative.

| Branch | Act A | Act C | Best |
|---|---:|---:|---|
| Positive | **1,336.8** | 2,000.0 | **A** |
| Negative | 2,138.5 | **2,000.0** | **C** |

`Expected cost with the study = 0.594 × 1336.8 + 0.406 × 2000.0 = ` **1,606.2**

`Value = 1662.5 − 1606.2 = ` **£56,200**

**Study 1 costs £45,000. Commission it.**

### The ceiling, and Study 2

Perfect knowledge: choose A if rolling contact fatigue (1,100), C if a formation defect (2,000).

`0.625 × 1100 + 0.375 × 2000 = ` **1,437.5**

`EVPI = 1662.5 − 1437.5 = ` **£225,000**

**Study 2 costs £280,000. Refuse it, and no further computation is needed.** It cannot pay for itself even if it settles the question with certainty, because certainty itself is worth only £225,000 here.

**Full marks require declining Study 2 on the ceiling alone.** A response that works out Study 2's value in detail has done unnecessary work and missed the point of the ceiling.

### Two value judgments

Available answers include: what a delay minute is worth; what reputational exposure is worth; the five-year horizon; and the exchange rate between capital spend and passenger disruption. **Any two that are genuinely decisions rather than measurements.**

## Form B — returns fraud

### Dominance

**Act B is dominated by Act C.** 1,700 against 1,050 and 1,650 against 1,050.

### Expected costs

`p(organised) = 9/15 = ` **0.600**

| Act | Arithmetic | Expected cost |
|---|---|---:|
| **A** | `0.6 × 620 + 0.4 × 1340` | **908.0** |
| B | `0.6 × 1700 + 0.4 × 1650` | 1,680.0 |
| C | — | 1,050.0 |

**Best: A, at £908,000.**

### The rule, and risk

**Act C has no spread**, at 1,050 either way. A committee avoiding the £1,340 outcome chooses C and pays `1050 − 908 = ` **£142,000** in expectation.

### Critical value

A beats C when `620p + 1340(1−p) < 1050`, so `p > 290/720 = ` **0.403**.

The register puts p at **0.600** — above, and again not by much.

### Study 1

`P(positive) = 0.6 × 0.75 + 0.4 × 0.20 = ` **0.530**; `P(negative) = ` **0.470**

Posteriors: **0.849** after positive; **0.319** after negative.

| Branch | Act A | Act C | Best |
|---|---:|---:|---|
| Positive | **728.7** | 1,050.0 | **A** |
| Negative | 1,110.2 | **1,050.0** | **C** |

`Expected cost with the study = 0.530 × 728.7 + 0.470 × 1050.0 = ` **879.7**

`Value = 908.0 − 879.7 = ` **£28,300**

**Study 1 costs £20,000. Commission it.**

### The ceiling, and Study 2

`0.6 × 620 + 0.4 × 1050 = ` **792.0**

`EVPI = 908.0 − 792.0 = ` **£116,000**

**Study 2 costs £150,000. Refuse it on the ceiling alone.**

### Two value judgments

Available answers include: what a pound of fraud loss is worth against a pound of friction imposed on a legitimate customer; what lost goodwill is worth; the three-year horizon. **Any two that are genuinely decisions.**

## The trap in both forms

**In the chapter, the study was not worth running. In both forms, the small study is.**

That is deliberate. A reader who learned *studies are usually not worth it* has learned a pattern rather than a principle, and both forms punish it.

**What separates them is where the prior sits relative to the critical value.** In the chapter, 0.636 against a critical value of 0.283 — far away, so almost nothing could move the act. In both forms, the prior sits about half again above the critical value rather than more than twice it, so the negative branch crosses and the study earns its cost.

**A strong response says this**, in one sentence, without being asked.

## Three answers that look right and are not

**"The study is cheap relative to the decision, so run it."** The decision is worth over a million in Form A and the study is £45,000, which sounds obviously worth it and is not the argument. A £280,000 study on the same decision is refused. **Cost is compared to value, not to the size of the decision.**

**"Act C is the safe option and should be recommended."** It costs £337,500 or £142,000 in expectation. Whether that is worth paying is the panel's judgment, and stating it as the answer takes a value decision away from the people entitled to make it.

**"We should do Study 1, and then Study 2 if it comes back negative."** Tempting, and it needs the ceiling recomputed after Study 1 — which will be lower than £225,000, not higher, because some uncertainty has already been resolved. A response that proposes this without noticing gets 1 rather than 2 on the ceiling dimension.

## A note on tone

Two dimensions — using the ceiling to dispose of Study 2 without further work, and naming the value judgments in the table — are the ones this chapter exists to install, and both are commonly scored 0 by readers whose arithmetic is perfect.

## Post-task self-explanation

Write two or three sentences, before the delayed retest.

> In the chapter the study was not worth running; here it was. **Nothing about the studies explains the difference.** What does?
