# Chapter 3 Water-Pressure Case Data

Status: drafting freeze. Extension of `../02-representation-mechanisms/case-data.md`, which extends `../01-decisions-questions/case-data.md`. Both remain authoritative for every value they contain.

All values here are **synthetic authoring data**. They are not industry averages, regulatory standards, design guidance, or values from any real utility.

## Relationship to earlier chapters

Chapter 3 changes no Chapter 1 or Chapter 2 value. It adds the pressure facts that Chapter 2's role table gestured at with the phrase "adequate or not".

Carried forward unchanged and used in this chapter:

| From | Value | Used here for |
|---|---|---|
| Ch 1 | Dashboard storage **10.8 ML**; verified **9.9 ML** | The systematic-offset demonstration |
| Ch 2 | Hillcrest tank **0.6 ML** of **1.2 ML** capacity | The proxy discussion |
| Ch 2 | Hillcrest demand **0.9 ML/day**; duty pump **1.1 ML/day** | Context |

## The construct with no reference standard

The drought plan requires that service pressure remain **"adequate"**.

It does not define the word.

That is the chapter's starting point and is deliberate: this is what most real requirements look like, and the absence is not negligence but the normal condition of a term that everyone believes is obvious.

## Elevations and heads

Pressure is given in **metres of head**, which is the height of water above the point of measurement. It is used here because the arithmetic is subtraction and requires no unit conversion.

| Item | Frozen value |
|---|---:|
| Hillcrest tank water surface, when tank is full | 96 m |
| Fixed monitoring point, property elevation | 62 m |
| Highest connected property, elevation | 84 m |
| Pump station discharge point, elevation | 18 m |
| Connected properties in Hillcrest | 340 |
| Properties above 78 m elevation | 31 |
| Friction loss along the Hillcrest feeder main, evening peak | 6 m |
| Tank surface drop by end of evening peak | 3 m |

### The utility's current working definition

> Adequate pressure means **at least 20 metres of head at the fixed monitoring point**.

This is the definition in operational use. It is one of several defensible ones and was not adopted after deliberation; it was adopted because the monitoring point already had an instrument.

## The four operationalizations

Static condition, tank full:

| Operationalization | Calculation | Result | Verdict against 20 m |
|---|---|---:|---|
| At the fixed monitoring point | 96 − 62 | **34 m** | adequate |
| At the highest connected property | 96 − 84 | **12 m** | **inadequate** |

Evening peak, with 6 m friction loss and the tank surface down 3 m:

| Operationalization | Calculation | Result | Verdict against 20 m |
|---|---|---:|---|
| At the fixed monitoring point | 96 − 3 − 62 − 6 | **25 m** | adequate |
| At the highest connected property | 96 − 3 − 84 − 6 | **3 m** | **inadequate** |

### Share of properties served

At evening peak, a property fails the 20 m threshold if its elevation exceeds 96 − 3 − 20 − 6 = **67 m**.

The case supplies that **31 of 340** properties lie above 78 m and are therefore certainly failing. The case does **not** supply the count between 67 m and 78 m; a reader who needs it must say so rather than invent it.

Using only the supplied figure:

`31 ÷ 340 = 0.091`, so **at least 9%** of Hillcrest properties fall below the threshold at peak, and the utility could report "**91% of properties adequately served**" as an upper bound.

The same system, under one working definition, is recorded as fully adequate; under another, as failing for at least one property in eleven.

## Sensor facts

| Item | Frozen value | Authoring role |
|---|---:|---|
| Pump-station pressure sensor, display resolution | 0.01 bar | Looks precise |
| Pump-station pressure sensor, repeatability | ±0.02 bar | Is precise |
| Pump-station pressure sensor, offset found at last calibration check | **0.15 bar high** | Is not true |
| Approximate conversion supplied by the case | 1 bar ≈ 10.2 m of head | So the offset is about **1.5 m** |
| Hillcrest monitoring-point sensor, reading interval | every 15 minutes | Grain, carried from Chapter 2 |

The pump-station sensor is the chapter's worked case of **precise and wrong**: it returns nearly the same number every time, that number is quoted to two decimal places, and it is consistently about 1.5 m of head too high.

## The comparison utility

A neighbouring utility publishes that **95% of its properties are adequately served**.

Its working definition is **at least 15 metres of head, measured at midday**.

The two figures — 91% and 95% — look comparable and are not. Different threshold, different time of day, different measurement location.

The case does **not** supply enough information to convert one into the other, and a reader who attempts the conversion has missed the point.

## Proxy: tank level standing in for customer pressure

The utility's dashboard shows Hillcrest tank level continuously. Customer pressure is not measured continuously anywhere.

Tank level is therefore used as a proxy for whether customers are adequately served.

**When the proxy works.** When the binding constraint is how much water is in the tank, tank level tracks customer pressure closely.

**When it breaks.** When the binding constraint is friction loss along the feeder main — Chapter 2's Mechanism B — the tank can be comfortably full while the top of the zone is below threshold. At evening peak the 6 m friction loss is larger than the 3 m tank drop, so the proxy is at its least informative exactly when the answer matters most.

The failure is **structured, not random**: it happens under identifiable conditions, which is why collecting more tank-level readings does not repair it.

## Items for the Chapter 3 / Chapter 4 boundary exercise

Supplied for reader placement. Intended dispositions are recorded here for the feedback file, not in the reader copy.

| Item | Intended placement |
|---|---|
| The pump-station sensor reads 0.15 bar high | Chapter 3 — the number is off |
| Pressure sensors exist only at pump stations, none in the zones | Chapter 4 — which records exist |
| "Adequate" was defined as 20 m of head at the monitoring point | Chapter 3 — an operationalization choice |
| The monitoring point was sited where a technician could park | **On the line** — deliberately unresolved |

The fourth item is both a measurement-procedure choice and a fact about which records come to exist. It is given to the reader without an answer.

## The systematic-offset demonstration

Reusing Chapter 1's frozen facts:

- dashboard storage: **10.8 ML**
- independently verified storage: **9.9 ML**
- difference: **0.9 ML**, in one direction, from a transmitter reading high

Averaging more dashboard readings would have produced a tighter estimate of a number that was wrong by about 0.9 ML every time.

## Prohibited interpretations

Do not write or imply that:

- any of these values are typical, standard, or recommended;
- 20 m, 15 m, or any figure is a real minimum service pressure;
- metres of head is the only or preferred unit in practice;
- a property below the threshold has no water, or that any specific health or safety consequence follows;
- low pressure implies unsafe water;
- 0.15 bar is a typical sensor offset, or that sensors are generally untrustworthy;
- the neighbouring utility is misreporting — its definition is different, not dishonest;
- the utility's monitoring-point definition was adopted negligently;
- 91% is a computed exact figure rather than an upper bound from supplied data;
- a real utility may leave service pressure undefined in an operating plan.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water or distribution-engineering SME should review the pressure story for plausibility and accidental unsafe implication, alongside the Chapter 1 anchor and the Chapter 2 network extension.

**These facts inherit Chapter 1's open Gate 1, now two chapters deep.** If SME review changes the Chapter 1 operating story or the Chapter 2 network, this file must be rechecked against both.
