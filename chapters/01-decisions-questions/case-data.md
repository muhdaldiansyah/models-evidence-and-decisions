# Chapter 1 Water-Supply Case Data

Status: drafting freeze; companion to `anchor.md`.

All values in this file are synthetic authoring data. They are not industry averages, regulatory standards, or empirical estimates from a real utility.

## Fixed case values

| Item | Frozen value | Authoring role |
|---|---:|---|
| Usable storage capacity | 14.0 ML | Defines physical scale only |
| Case-specific operating reserve | 4.5 ML | Decision trigger; explicitly fictional |
| Dashboard storage at 08:00 | 10.8 ML | Initial recorded state |
| Verified physical storage at 08:25 | 9.9 ML | Triggers observation revision |
| Normal treated-water input | 8.4 ML/day | Baseline operation |
| Temporary treated-water input | 8.8 ML/day | Candidate intervention |
| Delay before higher input arrives | 6 hours | Physical/action delay |
| Incremental cost at higher input | $2,000 per 24 hours | Consequence/trade-off |
| Independent verification time | 25 minutes | Information-gathering alternative |
| Voluntary request authority | Utility Director | Fictional governance fact |
| Mandatory restriction authority | City Manager | Fictional governance fact |
| Earliest mandatory restriction after request | 6 hours | Fictional governance/timing fact |

## No-new-action demand forecast

The forecast is conditional on **no new conservation request or restriction**.

| Day | Forecast high | Forecast demand |
|---:|---:|---:|
| 1 | 36°C | 9.0 ML |
| 2 | 38°C | 9.3 ML |
| 3 | 40°C | 9.6 ML |
| 4 | 40°C | 9.5 ML |
| 5 | 39°C | 9.4 ML |
| 6 | 37°C | 9.2 ML |
| 7 | 35°C | 8.9 ML |
| **Total** |  | **64.9 ML** |

These are synthetic central forecasts, not probabilistic intervals.

## Arithmetic checks

### Dashboard-based baseline

Seven-day input:

`8.4 × 7 = 58.8 ML`

Projected ending storage:

`10.8 + 58.8 - 64.9 = 4.7 ML`

Interpretation:
the dashboard-based first pass lands just above the 4.5 ML case reserve.

### Verified-state baseline

`9.9 + 58.8 - 64.9 = 3.8 ML`

Interpretation:
the independent level check moves the same operating plan below the reserve.

### Temporary production increase

Six-hour delay means:

`8.4 × 0.25 + 8.8 × 6.75 = 61.5 ML`

Central-demand projection:

`9.9 + 61.5 - 64.9 = 6.5 ML`

### Supplied high-demand stress

Stress the demand forecast by `+0.4 ML/day`:

`64.9 + (0.4 × 7) = 67.7 ML`

Then:

`9.9 + 61.5 - 67.7 = 3.7 ML`

Interpretation:
the production increase helps materially but does not make the decision robust to the supplied stress.

## Post-conservation observation

After a voluntary conservation request:

- pre-action forecast for the next 24 hours: **9.0 ML**
- observed demand: **8.6 ML**
- several monitored large users report reducing nonessential use in response to the request

Do **not** interpret `9.0 - 8.6 = 0.4 ML` as an identified causal effect.

Its pedagogical role is to show that the action has changed the process generating future demand, so the no-new-action forecast must be reconsidered.

## Reveal order

### Opening
- seven-day heatwave
- 10.8 ML dashboard value
- 4.5 ML reserve
- 8.4 ML/day current input
- seven-day demand table
- Utility Director and broad candidate actions

### Observation revision
- independent check takes 25 minutes
- physical storage is 9.9 ML
- remote transmitter is biased high

### Choice
- 8.8 ML/day temporary input
- six-hour action delay
- $2,000/day incremental cost
- authority split between voluntary request and mandatory restriction

### Responsive-system revision
- no-action forecast condition
- 8.6 ML post-request observation
- reported behavioral response

## Prohibited interpretations

Do not write or imply that:

- 4.5 ML is a general reserve standard;
- the storage capacity or input rates are typical;
- the six-hour delay is typical;
- the cost is representative;
- the voluntary request has a known 0.4 ML causal effect;
- the authority structure is normal municipal law;
- reserve crossing guarantees immediate service loss;
- SCADA is inherently unreliable.

## Publication gate

The data are frozen for first drafting.

Before publication freeze, a drinking-water utility / engineering SME should review the fictional operating story for plausibility and accidental unsafe implications. The SME is not being asked to validate these synthetic values as industry averages.
