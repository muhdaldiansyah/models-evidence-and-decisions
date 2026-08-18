# Chapter 4 Metering and Records Case Data

Status: drafting freeze. Extension of `../03-measurement-operationalization/case-data.md`, `../02-representation-mechanisms/case-data.md`, and `../01-decisions-questions/case-data.md`. All three remain authoritative for every value they contain.

All values here are **synthetic authoring data**. They are not industry averages, regulatory standards, design guidance, or values from any real utility.

## The design rule for this chapter

**Every number in this file is correct.** Nothing is falsified, miscalculated, or badly maintained.

The chapter's force depends on the reader being unable to find an error in any value, and discovering that the problem is entirely in which values exist.

## Where the Hillcrest figure comes from

| Item | Value | Source of the number |
|---|---:|---|
| Town total, day 1 | **9.0 ML** | Meter at the treatment works outlet |
| Lowfield | **5.4 ML** | Zone meter, installed 1998 |
| Millbrook | **2.7 ML** | Zone meter, installed 2004 |
| **Hillcrest** | **0.9 ML** | **None. Computed as 9.0 − 5.4 − 2.7** |

The subtraction is correct. The three meters are correct. The figure has been reported as *Hillcrest demand* for as long as anyone remembers.

## What the residual actually contains

A one-off study three years ago fitted a temporary insertion meter to the Hillcrest feeder main for two weeks. It found Hillcrest customer consumption averaging **0.62 ML/day** at the time.

A night-flow study the following year attributed network leakage as follows. Operational records supply the remaining components.

| Component | Value | In the Hillcrest zone? |
|---|---:|---|
| Hillcrest customer consumption | 0.62 ML/day | yes |
| Leakage, Hillcrest feeder main and zone | 0.10 ML/day | yes |
| Leakage, rest of network | 0.08 ML/day | **no** |
| Unbilled operational use — mains flushing, firefighting, tank cleaning | 0.06 ML/day | mostly no |
| Under-registration by the Lowfield and Millbrook meters | 0.04 ML/day | **no** |
| **Total** | **0.90 ML/day** | |

Each component is itself an estimate. They are supplied so the reader can see the residual decompose; they are not presented as precisely known.

### What follows for Chapter 2's arithmetic

Chapter 2 computed Hillcrest tank endurance with no pump as `0.6 ÷ 0.9 = 0.67 days`, about **16 hours**.

The draw actually on the Hillcrest tank is consumption plus Hillcrest-zone leakage:

`0.62 + 0.10 = 0.72 ML/day`

`0.6 ÷ 0.72 = 0.83 days`, about **20 hours**.

The residual overstated the tank draw by **0.18 ML/day** — the leakage elsewhere, the unbilled operational use, and the metering error, none of which draws the Hillcrest tank at all.

**Note the direction.** Chapter 2's figure was conservative: it gave less time than the utility actually had. Nobody was harmed and nobody noticed. The conservatism was luck, not design, and it would reverse if the composition shifted — for instance if Hillcrest-zone leakage grew while leakage elsewhere was repaired.

This is the chapter's most important arithmetic and should be produced by the reader, not read.

## The five stages, on this case

| Stage | What happened | Who decided |
|---|---|---|
| **Eligibility** | Only connections with a billing account are metered. Standpipes, firefighting draw, and the utility's own operational use have no account and therefore no meter. | The billing system's design |
| **Coverage** | Zone meters went into Lowfield (1998) and Millbrook (2004), where revenue justified the capital. Hillcrest is 10% of demand and never did. | Capital-planning decisions, two decades apart |
| **Capture** | The Millbrook zone meter failed for **11 days** last year. The gap was filled by carrying forward the previous week's average. | A technician, following standing practice |
| **Retention** | Readings are logged every 15 minutes, kept for **90 days**, then aggregated to daily totals and the fine data discarded. | A storage-cost decision |
| **Reporting** | The monthly regulatory return reports **non-revenue water** as a single line. Leakage, unbilled operational use, and metering error are combined before anyone outside the utility sees them. | The regulator's return form |

**Only eligibility and capture are sourced concepts** (`censusndtargetpopulation` §1.1; `davern2013nonresponse`, `meng2018paradox`). The five-stage enumeration is the book's own device.

## The gap that is related to the value

The Millbrook meter's 11 failed days were **not** spread evenly through the year.

The case supplies that the meter's failure mode is heat-related: it faults more often at high ambient temperature. Nine of the eleven days fell in the two hottest weeks of the year.

Now follow it through.

Those days were filled by carrying forward the previous week's average — a cooler week, so a **lower** Millbrook figure than the true one. A lower Millbrook subtrahend leaves a **larger** residual.

So the Hillcrest figure is inflated **specifically on the hottest days** — the days on which the drought plan is invoked, the days Chapter 1's whole analysis concerned, and the days when Hillcrest's supply actually matters.

The gap-filling rule was reasonable, applied consistently, and documented. It makes the number worst exactly where it is used.

**Nothing in the dataset reveals this.** The eleven filled days look like ordinary readings.

## The censored observation

The treatment-works outlet meter registers to a maximum of **10.0 ML/day**.

On three days last summer, true output exceeded that maximum. Each was recorded as **10.0**.

Those three records are **censored**, not missing. They carry real information — output was *at least* 10.0 — and treating 10.0 as the true value understates the town total, which understates the residual on those days.

The three records are indistinguishable, in the dataset, from days when output genuinely was 10.0.

## The absence

Firefighting draw.

There is no meter, no billing account, and no record of any kind. When the fire service opens a hydrant, water leaves the network and nothing anywhere registers that it did.

It is not missing. It never had a place to be. There is no row, no null, and no flag — and no amount of inspecting the data will produce one.

## The Chapter 15 situation, supplied as an out-of-scope contrast

If operators learned that the residual was being scrutinised, and began scheduling mains flushing for the day *after* the monthly reading rather than the day before, the residual would fall without anything about the network changing.

That is a recording process **responding to being used**, and it is Chapter 15. It is supplied here so the boundary can be shown rather than announced.

## Prohibited interpretations

Do not write or imply that:

- any of these values are typical, standard, or recommended;
- 0.7% meter under-registration, 11 failure days, or a 90-day retention period is a normal figure;
- the utility's staff behaved carelessly or dishonestly — every decision described here is ordinary and defensible;
- subtraction residuals are always wrong, or that non-revenue water reporting is a defect;
- the fire service should be metered, or that unmetered firefighting draw is a problem to be fixed;
- a real utility can operate without accounting for non-revenue water;
- the components of the residual are precisely known;
- Chapter 2's 16-hour figure was an error — it was the correct arithmetic on the number available.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water utility SME with metering or revenue-management experience should review this extension for plausibility and accidental unsafe implication.

**These facts inherit Chapter 1's open Gate 1, now three chapters deep.** Chapters 2, 3, and 4 all extend a case whose operating story has never been reviewed by a domain expert. If SME review changes the Chapter 1 anchor, three case-data files must be rechecked. This accumulation is a real risk and should be treated as a standing item rather than a formality.
