# Chapter 9 Evidence-Synthesis Case Data

Status: drafting freeze. Extension of the Chapter 1–8 case-data files, all of which remain authoritative for every value they contain.

All values here are **synthetic authoring data**. They are not industry averages, regulatory standards, design guidance, or values from any real utility or manufacturer.

## What this file adds

Chapter 9 introduces **no new case** and, for the first time, needs sources **outside** the utility.

Chapter 7 found the pump-upgrade effect **not identified** from the utility's own record. Chapter 8 estimated a different, identified quantity. Neither told the utility what happens if it upgrades Hillcrest's pump — and next summer is coming.

So the utility does what organisations do: it collects everything that bears on the question.

## Carried forward

| From | Item |
|---|---|
| Ch 2 | Mechanism A (pump capacity) and Mechanism B (friction loss in an old feeder main) |
| Ch 2 | Duty pump capacity **1.1 ML/day** |
| Ch 6 | About **91%** for Mechanism A after the pump test |
| Ch 7 | The 15-zone upgrade record; difference-in-differences **−2.4** |
| Ch 7 | **Positivity failure**: no upgraded zone has a feeder main older than **40 years**; Hillcrest's is **68** |
| Ch 7 | Four different actions are recorded as *pump upgrade* |
| Ch 8 | Forecast errors run low; the interval covers sampling variability only |

## The five sources

All estimates are the change in **mean low-pressure complaints per heat event** following a duty-pump upgrade. Negative means fewer complaints.

| | Source | Size | Estimate | Stated defect |
|---|---|---:|---:|---|
| **A** | The utility's own 15-zone upgrade record | 15 zones | **−2.4** | Not identified (Chapter 7): allocation was to the six worst-complaining zones |
| **B** | A neighbouring utility's before-and-after study | 40 zones | **−3.1** | Every zone is on **flat ground** |
| **C** | An industry benchmarking dataset | 1,400 zones | **−0.6** | **Self-reported**; participation voluntary; no definition of "complaint" is enforced across members |
| **D** | The pump manufacturer's rig test | 6 rigs | **−4.8** | A rig has **no feeder main at all** |
| **E** | An expert panel | 5 engineers | **−1.5** (median) | Judgment; the panel has **never been scored** |

## The four weighting rules

| Rule | Arithmetic | Result |
|---|---|---:|
| Simple average of all five | `(−2.4 − 3.1 − 0.6 − 4.8 − 1.5) ÷ 5` | **−2.48** |
| Median of all five | middle of `−4.8, −3.1, −2.4, −1.5, −0.6` | **−2.40** |
| Weight by sample size, A–D | `(15×−2.4 + 40×−3.1 + 1400×−0.6 + 6×−4.8) ÷ 1461` | **−0.70** |
| Drop C, average A, B, D | `(−2.4 − 3.1 − 4.8) ÷ 3` | **−3.43** |

**Four rules, a range of −0.70 to −3.43** — a factor of nearly five, with no arithmetic error anywhere.

### The weight table for the size rule

| Source | n | Share of weight | Contribution |
|---|---:|---:|---:|
| A | 15 | 1.0% | −36.0 |
| B | 40 | 2.7% | −124.0 |
| **C** | **1,400** | **95.8%** | **−840.0** |
| D | 6 | 0.4% | −28.8 |
| **Total** | **1,461** | 100% | **−1,028.8** |

**The rule that sounds most principled hands 95.8% of the weight to the source with a stated participation defect.**

## The transport facts

**Terrain.** Hillcrest is a **hilltop** zone: the duty pump lifts water against static head as well as overcoming friction. Every one of source B's forty zones is on flat ground, where an upgrade relieves friction loss and nothing else.

**The mechanism by which an upgrade would help at Hillcrest is absent from every zone in source B.**

**Feeder main age.** No zone in any of the five sources has a feeder main older than **40 years**. Hillcrest's is **68**.

**Rig composition.** Source D's rigs have no feeder main, so Mechanism B cannot occur in them at all. The rig measures what a pump does, not what a zone does.

## Dependence among the sources

Three facts the utility could establish by asking:

- The neighbouring utility (**B**) is a member of the benchmarking scheme (**C**), so its forty zones are inside the fourteen hundred.
- Two of the five panel members (**E**) served on the working group that designed the benchmarking scheme's complaint definition.
- The manufacturer's rig protocol (**D**) was written against the same scheme's definition.

**None of this is visible in the five numbers**, and all of it is answerable by three emails.

## Prohibited interpretations

Do not write or imply that:

- any of these values are typical of water utilities, or that any of the sources resembles a real dataset;
- any of the four rules is the right one;
- source C is worthless — it is the only source with national coverage, and its defect is stated rather than assumed;
- source D is worthless — a rig isolates pump behaviour, which is exactly what a rig is for;
- the expert panel is unreliable because it is judgment;
- combining the five yields a number the utility may act on;
- the terrain fact makes source B wrong — it makes source B about a different quantity;
- Chapter 7's positivity verdict has been overturned by adding sources;
- any of this tells the utility what to do.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water utility SME should review the five sources for plausibility, and in particular should confirm that static lift versus friction loss is a real terrain-dependent distinction of the kind the manuscript leans on.

**These facts inherit Chapter 1's open Gate 1, now nine chapters deep.** Nine case-data files now extend one anchor whose operating story has never been reviewed by a domain expert. This is a standing risk and remains a book-level decision the author has not yet made.
