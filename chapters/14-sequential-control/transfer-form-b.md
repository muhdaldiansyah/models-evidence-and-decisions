# Chapter 14 Cold-Transfer Task — Form B

Allow about **50 minutes**.

Work from this page alone.
Do not open the chapter, the water case, the rubric, or Form A.
Every fact you need is here. Do not look anything up.

---

## The situation

A **county highways authority** decides each evening between November and March whether to send out its **gritting fleet**.

A run costs money and salt. A missed night leaves ice on the network.

| | |
|---|---:|
| Service standard — nights with ice-affected roads above the threshold, per winter | **no more than 2** |
| Annual winter service budget | **£2,100,000** |

## The authority's written rule

The winter service plan has contained this paragraph for eleven years.

> Send the fleet when the road-surface temperature sensor at the depot reads below **+1 °C** at 18:00.

## Three alternatives, and five winters

The authority has never run any rule but its own. A consultant has simulated four rules against the last five winters.

- **G0** — send the fleet only when the forecast minimum air temperature is below **−2 °C**.
- **G1** — the authority's actual rule, above.
- **G2** — send the fleet when the **forecast minimum** is below **+1 °C**.
- **G3** — send the fleet when the forecast minimum is below **+1 °C** **and** the depot sensor reads below **+3 °C**.

Each cell reads **ice-affected road-hours / nights above the service threshold / wasted runs / salt used (tonnes)**. For ice-affected road-hours, lower is better.

| Winter | G0 | G1 | G2 | G3 |
|---|---|---|---|---|
| Hard freeze | 340 / 9 / 0 / 0 | 210 / 4 / 6 / 1,240 | 60 / 0 / 19 / 1,480 | 95 / 1 / 5 / 1,120 |
| Mild | 20 / 0 / 0 / 0 | 20 / 0 / 0 / 0 | 20 / 0 / 0 / 0 | 20 / 0 / 0 / 0 |
| Long frost | 480 / 11 / 0 / 0 | 260 / 3 / 12 / 1,360 | 110 / 0 / 0 / 890 | 110 / 0 / 0 / 890 |
| Twin cold spells | 410 / 10 / 0 / 0 | 290 / 4 / 15 / 1,320 | 80 / 0 / 26 / 1,590 | 130 / 0 / 11 / 1,240 |
| False alarm | 30 / 0 / 0 / 0 | 30 / 0 / 0 / 0 | 30 / 0 / 8 / 540 | 30 / 0 / 0 / 0 |

## What the authority records

**Road-surface temperature** at the depot and at three outstations, every ten minutes.
**Forecast minimum air temperature**, from the met provider, each afternoon.
**Runs completed** and **salt spread**, per run.
**Ice-related incident reports**, from the police and from the public.

## The authority's ice model

> predicted ice-affected hours = base exposure + moisture sensitivity × overnight humidity − residual salt protection

Fitted to the last five winters, the model returns a **moisture sensitivity of 1.4 hours per percentage point** and a value of **46** for **base exposure minus residual salt protection**.

The fit is close. Any of these splits fits equally well:

| Base exposure | Residual salt protection | Difference |
|---:|---:|---:|
| 50 | 4 | 46 |
| 68 | 22 | 46 |
| 88 | 42 | 46 |

The authority is currently deciding whether to **spread more salt per run and run less often, or spread less and run more often** — a choice that determines most of a **£2,100,000** annual budget — and what the right answer is depends on how much protection survives from one night to the next.

## An instrument on offer

A supplier has quoted **£96,000** to install **road-surface state sensors at twelve sites**, measuring actual surface condition and residual salt concentration rather than temperature alone.

## Produce

1. **Compute the totals row for each of the four rules**: worst ice-affected road-hours across the five winters, total nights above the service threshold, total wasted runs, total salt used.

2. **Identify any rule that is dominated** — worse than another on every one of the four measures. Name it and name what dominates it. Then say, in one sentence, what the authority did wrong, being careful to distinguish it from writing a bad rule.

3. **Count the winters that carry no information about the choice between G2 and G3.** Say what that implies about how long it would take the authority to settle the choice by running one of them.

4. **State what the remaining choice depends on**, and say why the table cannot settle it.

5. **A night with no ice-related incident reports could be a night with no ice, or a night with ice that nobody drove on.** Say whether the four records listed above can tell these apart, and say precisely what follows for every rule in the table.

6. **Look at the ice model.** Say whether collecting five more winters of the same data would determine base exposure and residual salt protection separately. Explain your answer in terms of the model rather than in terms of the data.

7. **Say which of the two problems — item 5 or item 6 — more data would fix, and which it would not.** Then say what the alternative to collecting more data would be.

8. **Decide on the instrument.** Say what it would resolve, what it costs relative to the decision it informs, and what your recommendation is. If you cannot compute what it is worth, say why not.
