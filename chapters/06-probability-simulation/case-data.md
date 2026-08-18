# Chapter 6 Probability Case Data

Status: drafting freeze. Extension of the Chapter 1–5 case-data files, all of which remain authoritative for every value they contain.

All values here are **synthetic authoring data**. They are not industry averages, regulatory standards, design guidance, or values from any real utility.

## What this file adds

Chapter 6 introduces **no new case**. It takes Chapter 5's list of open items and works them probabilistically.

It adds only the numbers that arithmetic needs: a base rate, two likelihoods, a forecasting record, and a demand spread.

## Carried forward

| From | Item |
|---|---|
| Ch 2 | **Mechanism A** — the duty pump's capacity limits refill, so the hilltop tank falls |
| Ch 2 | **Mechanism B** — friction loss along an old, undersized feeder main drops pressure at the top of the zone |
| Ch 2 | The discriminating observation, named and never made: run the duty pump at elevated output through a hot afternoon and record pressure at the top of the zone |
| Ch 5 | Both mechanisms still alive; the observation obtainable and not obtained |
| Ch 1 | Seven-day demand forecast totalling **64.9 ML**; input **8.4 ML/day**; verified storage **9.9 ML**; reserve **4.5 ML** |

## The base rate

The utility keeps a register of low-pressure investigations across its network. Restricting to **pumped zones**, which is the relevant population:

| Outcome of investigation | Count |
|---|---:|
| Pump-capacity limited | **7** |
| Main-related | **4** |
| **Total** | **11** |

Prior odds for Mechanism A over Mechanism B: **7 : 4**, or about **1.75 : 1**.

**The population matters and must be stated whenever this number is used.** It is investigations in *pumped zones*, not all pressure complaints, and not all zones. The register covers eighteen years and three different network configurations.

## The discriminating observation

Run the duty pump at elevated output through one hot afternoon and record pressure at the top of the Hillcrest zone. The threshold of interest is a recovery of **more than 8 metres of head**.

Supplied likelihoods, from the utility's engineering judgment informed by the register:

| | Recovery > 8 m | No recovery |
|---|---:|---:|
| If Mechanism A operates | **0.85** | 0.15 |
| If Mechanism B operates | **0.15** | 0.85 |

**These numbers are supplied, and the manuscript must say so.** Where such likelihoods come from in real work is the hardest step in the whole procedure, and handing them to the reader hides it. The chapter should hand them over and then say what it has just done.

### The update, both branches

| Outcome | Ratio | Posterior odds | Posterior |
|---|---:|---|---|
| Recovery > 8 m | 0.85 ÷ 0.15 ≈ **5.7** | 1.75 × 5.7 ≈ **9.9 : 1** for A | about **91%** for A |
| No recovery | 0.15 ÷ 0.85 ≈ **0.18** | 1.75 × 0.18 ≈ 0.31 : 1 | about **76%** for B |

One afternoon moves belief from roughly 2 : 1 to either 10 : 1 or 1 : 3.

## The detail that moves nothing

During the investigation, the caller who reported low pressure adds: **it has been getting worse since the hot spell began.**

This sounds informative. It is consistent with both mechanisms — hot weather raises demand, which strains the pump **and** raises flow through the main, increasing friction loss.

Supplied likelihoods:

| | Caller reports worsening with the hot spell |
|---|---:|
| If Mechanism A operates | **0.80** |
| If Mechanism B operates | **0.75** |

Ratio: `0.80 ÷ 0.75 ≈ 1.07`. Posterior odds `1.75 × 1.07 ≈ 1.87 : 1` — essentially unchanged from 1.75.

**This is the chapter's instantiation of worthless evidence.** It arrives vividly, it feels like a clue, and it moves belief by almost nothing.

## The forecasting record

The utility has issued a probabilistic statement — *the chance that usable storage falls below the operating reserve during this event* — in each of **40 past heat-event briefings**.

| Stated probability | Briefings | Reserve breached | Observed frequency |
|---:|---:|---:|---:|
| 90% | 10 | 5 | **50%** |
| 70% | 10 | 5 | **50%** |
| 50% | 10 | 5 | **50%** |
| 30% | 10 | 3 | **30%** |
| **Total** | **40** | **18** | **45%** |

Well calibrated at 50% and 30%. Badly overconfident at 70% and 90% — both bins delivered 50%.

**The overall base rate is 18/40 = 45%.** A forecaster who stated 45% in every briefing would be perfectly calibrated across this record and would have told nobody anything.

## Simulation inputs

Chapter 1 used point forecasts for the seven days. For the simulation demonstration, the case supplies a spread.

| Item | Value |
|---|---|
| Day-1 forecast demand | **9.0 ML** (Ch 1) |
| Seven-day forecast total | **64.9 ML** (Ch 1) |
| Supplied spread on each day's demand | ±**0.6 ML**, treated as equally likely anywhere in that range |
| Treated-water input | **8.4 ML/day** (Ch 1) |
| Starting verified storage | **9.9 ML** (Ch 1) |
| Operating reserve | **4.5 ML** (Ch 1) |

The seven daily central forecasts are Chapter 1's: **9.0, 9.3, 9.6, 9.5, 9.4, 9.2, 8.9 ML**, totalling 64.9 ML.

### The derived output

End-of-week storage falls below the reserve exactly when weekly demand exceeds `9.9 + 58.8 − 4.5 = `**`64.2 ML`**.

Simulating the seven days independently against the supplied ±0.6 ML spread:

| Runs | Result across repeated runs |
|---:|---|
| 100 | 72% – 80% |
| 1,000 | 76% – 79% |
| 10,000 | 76.7% – 77.9% |
| 1,000,000 | 77.3% |

**About 77%**, conditional on the Chapter 1 forecast, the supplied spread, and the storage model as it stands.

**The spread is supplied and is not derived from anything.** That is the point of the demonstration: running the projection ten thousand times will produce a stable answer about a spread nobody has justified.

And every question Part I raised about the demand figures remains untouched by the run count — the forecast was conditional on no new action (Ch 1), and Chapter 4 established that one of its zone components was a subtraction residual.

## Prohibited interpretations

Do not write or imply that:

- any of these values are typical, standard, or recommended;
- 7:4 is a general base rate for pressure faults, or that eighteen years and three network configurations make a clean reference class;
- the supplied likelihoods are measured quantities rather than engineering judgment;
- 0.85 and 0.15 are the kind of numbers that are usually available in real work;
- a 40-briefing record is enough to assess calibration reliably;
- the utility's forecasters are incompetent — overconfidence at the high end is common and the record is otherwise good;
- the caller's report is worthless information about the world; it is uninformative **for discriminating between these two mechanisms**, which is a different claim;
- running the simulation resolves anything Part I left open;
- probability of breaching the reserve implies any specific health or safety consequence.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water utility SME should review the investigation register, the supplied likelihoods, and the forecasting record for plausibility.

**These facts inherit Chapter 1's open Gate 1, now five chapters deep.** Six case-data files now extend one anchor whose operating story has never been reviewed by a domain expert. This is a standing risk and remains a book-level decision the author has not yet made.
