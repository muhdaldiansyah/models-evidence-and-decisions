# Chapter 14 Case Data

Status: frozen case facts. The manuscript may not contradict this file.

**The water anchor's fourteenth recurrence, and the first run across several years.** No new mechanism and no new physical fact. Every figure below was computed by simulation and checked before drafting.

## 1. The system, unchanged from Chapter 13

Reservoir capacity **260 ML**; critical level **120 ML**; standing production **100 ML/day**. Verification delay **two days**; production delay **two days**; loop delay **four days**.

## 2. Four rules

Each is stated as a rule, applicable by somebody who was not in the room.

- **P0 — do nothing.** Hold production at the standing level.
- **P1 — stock-keyed.** *The utility's actual rule, in force for nine years, unchanged from Chapter 13.* When the most recent verified storage figure is below 150 ML, set production to the most recent verified demand plus 20. When it is above 210 ML, return to the standing level.
- **P2 — flow-keyed.** *Chapter 13's repair.* When the most recent verified demand exceeds 115 ML/day, set production to that demand plus 20; otherwise return to standing.
- **P4 — both.** Act only when the most recent verified demand exceeds 115 **and** the most recent verified storage figure is below 200; otherwise return to standing.

**P3 is deliberately absent from the numbering.** A disjunctive rule — act on either condition — was computed during case design and is not carried into the manuscript, because it is dominated by P2 on every measure and adds a fourth column without a fourth idea.

## 3. Five summers

Demand in ML/day. Each summer starts from its own storage level and returns to 100 ML/day after the listed days.

| Summer | Start | Day-by-day demand |
|---|---:|---|
| **Heatwave** | 220 | 118, 124, 128, 126, 120, 112, 104 |
| **Mild** | 220 | 104, 106, 108, 106, 104, 102, 100 |
| **Long moderate** | 210 | 112, 116, 118, 118, 116, 114, 110, 108, 108, 108, 108, 108 |
| **Double peak** | 220 | 118, 124, 120, 110, 116, 126, 122, 104 |
| **False alarm** | 250 | 120, 126, 110, 102, 100, 100, 100 |

## 4. Results

Each cell reads: **minimum storage / days below the critical level / spill / extra production**, all in ML.

| Summer | P0 do nothing | P1 stock-keyed | P2 flow-keyed | P4 both |
|---|---|---|---|---|
| Heatwave | 88 / 14 / 0 / 0 | 88 / 3 / 30 / 202 | **124** / 0 / 44 / 216 | 104 / 1 / **6** / 178 |
| **Mild** | **190 / 0 / 0 / 0** | **190 / 0 / 0 / 0** | **190 / 0 / 0 / 0** | **190 / 0 / 0 / 0** |
| Long moderate | 66 / 13 / 0 / 0 | 106 / 2 / 28 / 222 | **130 / 0 / 0 / 148** | **130 / 0 / 0 / 148** |
| Double peak | 80 / 13 / 0 / 0 | 84 / 3 / 38 / 218 | **148** / 0 / 66 / 246 | 132 / 0 / **28** / 208 |
| False alarm | 192 / 0 / 0 / 0 | 192 / 0 / 0 / 0 | 192 / 0 / **18** / 86 | 192 / 0 / **0** / 0 |

### Aggregate over all five summers

| Rule | Worst minimum | Days below the critical level | Total spill | Total extra production |
|---|---:|---:|---:|---:|
| P0 do nothing | 66 | 40 | 0 | 0 |
| P1 stock-keyed | 84 | 8 | 96 | 642 |
| **P2 flow-keyed** | **124** | **0** | 128 | 696 |
| **P4 both** | 104 | 1 | **34** | 534 |

## 5. The three findings

**The utility's own rule is dominated.** P4 beats P1 on all four measures: higher worst minimum (104 against 84), fewer days below the critical level (1 against 8), less spill (34 against 96), less extra production (534 against 642). **A rule worse on every count is not a trade-off, it is a mistake**, and it has been in force for nine years.

**P4 differs from P1 in one respect only: what it watches.** Same delays, same response size, same stand-down. P1 watches the stock; P4 watches the stock and the flow together.

**The remaining choice is a genuine judgment.** P2 never breaches the critical level and spills 128 ML across five summers; P4 breaches it on one day and spills 34. **One day below the service standard against 94 ML of treated water**, and nothing in the arithmetic settles it.

## 6. What makes §7 possible

**On the mild summer all four rules produce identical results.** A whole year of operating experience carrying no information about which rule is better.

**Between P2 and P4, two of the five summers are identical** — mild and long moderate. Three differ.

**So roughly three summers in five carry information about this choice.** The utility has nine years of experience with P1 and none with anything else.

## 7. Observability

**What the utility measures:** reservoir level (verified, two days old); total production (daily); metered customer consumption (quarterly); Zone 4 inlet pressure (continuous).

**The state it needs:** whether high draw is hot-weather demand, or a burst.

**Both produce the same record.** Total draw rises, the reservoir falls, Zone 4 inlet pressure drops. Nothing in the four instruments separates them.

**Consequence.** All four rules in §2 fire on the same signal. If the cause is a burst, making more water pushes more water through the burst — Chapter 13's policy resistance, arriving inside a Chapter 14 rule.

**The repair, and it is one instrument.** A night-flow meter at the Zone 4 inlet, read at 03:00 when legitimate demand is near zero.

| | Night flow (ML/day-equivalent) |
|---|---:|
| Normal | **4** |
| With a burst of the size that would move the daily figures | **13** |
| Effect of hot weather at 03:00 | **negligible** |

**Cost: £18,000 installed.**

## 8. Structural non-identifiability

The utility's demand model:

> daily draw = base demand + heat sensitivity × maximum temperature + background leakage

**Fitted values: heat sensitivity 2.0 ML per °C, and base demand plus leakage equal to 82 ML/day.**

**The fit is exact** on the heatwave week:

| Max temperature (°C) | 18 | 21 | 23 | 22 | 19 | 15 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Model: 82 + 2 × T | **118** | **124** | **128** | **126** | **120** | **112** | **104** |

Those are the seven demand figures the book has used since Chapter 13.

**And base demand and leakage cannot be told apart**, because they enter only through their sum. Every split of 82 fits identically:

| Base demand | Leakage | Sum | Fit |
|---:|---:|---:|---|
| 78 | 4 | 82 | exact |
| 60 | 22 | 82 | exact |
| 40 | 42 | 82 | exact |

**Two consequences.**

**It was knowable before any data existed.** It follows from the model's form and from the fact that only total draw is measured.

**It makes a live decision undecidable.** Chapter 12 costed network pressure management at **£380,000**. What that scheme is worth depends on how much of the 82 is leakage, and the utility's records cannot say.

## 9. Information acquisition

**No probability over the leakage split is available and none is invented.** Chapter 11's arithmetic needs a prior; Chapter 12 established that this setting supplies none.

**Chapter 11's ceiling is used instead.** The meter costs **£18,000** against a scheme costing **£380,000** — **4.7%**.

**A ceiling argument does not say the meter is worth buying.** It says the meter cannot be screened out on cost.

## 10. What this case may not be used for

- Re-estimating anything Chapter 7 declared not identified.
- Any claim about how often a real operating rule is dominated. The case shows one that is; no frequency is claimed.
- Any claim that these values are typical, standard, or recommended for a real utility. They are synthetic and internally consistent, and nothing more.
- Any suggestion that 4 ML/day or 42 ML/day is a plausible leakage rate for a particular network. The three splits exist to show that the data cannot choose among them.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water utility SME with leakage or network-analysis experience should review this extension. In particular:

- whether **night-flow measurement at 03:00** is a recognised method for separating background leakage from legitimate demand, and whether **£18,000 installed** is a plausible order of magnitude for one such meter at a zone inlet;
- whether a utility of this size could genuinely lack the instrumentation to distinguish hot-weather demand from a burst, given the four instruments listed in §7 — this is the chapter's observability claim and it must not be a straw man;
- whether **base demand and background leakage entering only through their sum** is a fair description of what total-draw records can support, and whether the three candidate splits (78/4, 60/22, 40/42) span a range a practitioner would call live;
- whether a nine-year-old operating rule remaining in force unexamined is organisationally plausible.

The SME is not asked to validate the simulated policy results, which are arithmetic on stated rules, nor to treat any rule as recommended practice. The reviewer should flag any wording implying that night-flow measurement resolves leakage exactly, or that a dominated rule implies negligence by named roles.

**These facts inherit Chapter 1's open Gate 1, now fourteen chapters deep.** Fourteen case-data files now extend one anchor whose operating story has never been reviewed by a domain expert.
