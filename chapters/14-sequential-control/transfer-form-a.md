# Chapter 14 Cold-Transfer Task — Form A

Allow about **50 minutes**.

Work from this page alone.
Do not open the chapter, the water case, the rubric, or Form B.
Every fact you need is here. Do not look anything up.

---

## The situation

A **regional electricity grid operator** decides each afternoon how much **operating reserve** to procure for the following day.

Reserve is generation held back and paid for whether or not it is used. Too little and the system margin falls below the security standard; too much and the operator has paid for capacity nobody needed.

| | |
|---|---:|
| Standing reserve procurement | **400 MW** |
| Security standard — margin must not fall below | **500 MW** |
| Annual reserve contract portfolio | **£5,100,000** |

## The operator's written rule

The operational policy has contained this paragraph for eleven years.

> When the day-ahead margin forecast is below **900 MW**, procure reserve equal to the day-ahead demand forecast plus **250 MW**. Otherwise procure the standing 400 MW.

## Three alternatives, and five winters

The operator has never run any rule but its own. A planning analyst has simulated four rules against the last five winters.

- **R0** — procure the standing 400 MW, always.
- **R1** — the operator's actual rule, above.
- **R2** — procure standing plus 250 MW whenever **yesterday's demand-forecast error exceeded 300 MW**.
- **R3** — procure standing plus 250 MW when the day-ahead margin forecast is below 900 MW **and** yesterday's forecast error exceeded 300 MW.

Each cell reads **worst margin (MW) / hours below the security standard / unused reserve paid for (MWh) / total extra reserve procured (MWh)**.

| Winter | R0 | R1 | R2 | R3 |
|---|---|---|---|---|
| Cold snap | 210 / 9 / 0 / 0 | 210 / 4 / 120 / 1,600 | 560 / 0 / 380 / 1,900 | 470 / 1 / 90 / 1,450 |
| Mild | 880 / 0 / 0 / 0 | 880 / 0 / 0 / 0 | 880 / 0 / 0 / 0 | 880 / 0 / 0 / 0 |
| Long cold | 150 / 11 / 0 / 0 | 380 / 3 / 240 / 1,750 | 620 / 0 / 0 / 1,150 | 620 / 0 / 0 / 1,150 |
| Twin peaks | 190 / 10 / 0 / 0 | 260 / 4 / 300 / 1,700 | 640 / 0 / 520 / 2,050 | 540 / 0 / 210 / 1,600 |
| False alarm | 900 / 0 / 0 / 0 | 900 / 0 / 0 / 0 | 900 / 0 / 150 / 700 | 900 / 0 / 0 / 0 |

## What the operator measures

**Metered demand** at grid supply points, every half hour.
**Declared availability** from every contracted generator, submitted the day before.
**System frequency**, continuously.
**Settlement data**, six weeks in arrears.

## The operator's demand model

> system demand = baseline + temperature sensitivity × (18 °C − forecast temperature) + embedded generation shortfall

Fitted to the last five winters, the model returns a **temperature sensitivity of 620 MW per °C** and a value of **31,400 MW** for **baseline plus embedded generation shortfall**.

The fit is close. Any of these splits fits equally well:

| Baseline | Embedded generation shortfall | Sum |
|---:|---:|---:|
| 31,000 | 400 | 31,400 |
| 30,200 | 1,200 | 31,400 |
| 29,000 | 2,400 | 31,400 |

The operator is currently deciding whether to contract **distributed flexibility** — a decision worth about **£5,100,000 a year** — and what that is worth depends on which split is right.

## An instrument on offer

A vendor has quoted **£240,000** to install **per-unit real-time output telemetry at one-minute resolution** across the contracted fleet, replacing declared availability with measured output, and metering embedded generation directly.

## Produce

1. **Compute the totals row for each of the four rules**: worst margin across the five winters, total hours below the security standard, total unused reserve, total extra reserve procured.

2. **Identify any rule that is dominated** — worse than another on every one of the four measures. Name it and name what dominates it. Then say, in one sentence, what the operator did wrong, being careful to distinguish it from writing a bad rule.

3. **Count the winters that carry no information about the choice between R2 and R3.** Say what that implies about how long it would take the operator to settle the choice by running one of them.

4. **State what the remaining choice depends on**, and say why the table cannot settle it.

5. **The operator's margin can fall for two different reasons: unexpectedly high demand, or a contracted generator that declared availability it cannot deliver.** Say whether the four instruments listed above can tell these apart, and say precisely what follows for every rule in the table.

6. **Look at the demand model.** Say whether collecting five more winters of the same data would determine the baseline and the embedded generation shortfall separately. Explain your answer in terms of the model rather than in terms of the data.

7. **Say which of the two problems — item 5 or item 6 — more data would fix, and which it would not.** Then say what the alternative to collecting more data would be.

8. **Decide on the instrument.** Say what it would resolve, what it costs relative to the decision it informs, and what your recommendation is. If you cannot compute what it is worth, say why not.
