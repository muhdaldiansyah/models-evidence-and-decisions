# Chapter 13 Case Data

Status: frozen case facts. The manuscript may not contradict this file.

**The water anchor's thirteenth recurrence, and the first run forward in time.** No new mechanism, no new physical fact about Hillcrest. Every figure below was computed by simulating the stated rules and checked before drafting.

## 1. The system

| | |
|---|---:|
| Reservoir capacity | **260 ML** |
| Operating target | **220 ML** |
| Critical level (below which the utility's own standard is breached) | **120 ML** |
| Storage at the start of the heatwave | **220 ML** |
| Standing production | **100 ML/day** |
| Pre-heatwave demand | **100 ML/day** |

**The stock** is usable stored water. **The inflow** is treated production. **The outflow** is demand, which includes leakage.

**The two delays**, both established in Chapter 1's screen:

- **Verification delay — two days.** Storage telemetry is verified against the manual dip reading before it is used operationally. The most recent figure an operator has is two days old.
- **Production delay — two days.** A change to production ordered today reaches the network in two days: treatment ramp, then travel time.

**The loop delay is their sum: four days.**

## 2. Demand over the heatwave

| Day | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 onward |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Demand (ML/day) | 118 | 124 | 128 | 126 | 120 | 112 | 104 | **100** |

**Peak demand is day 3, at 128 ML/day.**

## 3. Trajectory A — the utility does nothing

Production held at 100 ML/day throughout.

| Day | Demand | Net flow | Storage |
|---|---:|---:|---:|
| 1 | 118 | −18 | 202 |
| 2 | 124 | −24 | 178 |
| 3 | 128 | −28 | **150** |
| 4 | 126 | −26 | 124 |
| 5 | 120 | −20 | **104** |
| 6 | 112 | −12 | 92 |
| 7 | 104 | −4 | **88** |
| 8 | 100 | 0 | 88 |
| 9–18 | 100 | 0 | **88** |

**Four facts, all checked.**

**Peak demand is day 3. Minimum storage is day 7. Four days apart.**

**Storage crosses the critical level of 120 on day 5** — two days after demand peaked and began falling. Total drawdown 220 to 88 is **132 ML**, which equals the sum of the seven net flows.

**From day 4 the deficit shrinks every day** — 28, 26, 20, 12, 4 — **and storage falls every day**. This is the chapter's central demonstration.

**Doing nothing does not recover.** From day 8 production and demand are both 100, the system is at an equilibrium, and storage sits at **88 ML indefinitely** — 32 ML below the utility's own critical level. The flows re-balanced; the stock did not refill.

## 4. The utility's written rule

From the utility's operating instruction, unchanged for nine years:

> When the most recent verified storage figure is below **150 ML**, set production to the most recent verified demand plus **20 ML/day**. When the most recent verified storage figure is above **210 ML**, return production to the standing level of 100 ML/day.

## 5. Trajectory B — the stock-triggered rule

| Day | Demand | Storage seen (2 days old) | Order placed | Production | Net | Storage | Spill |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 118 | — | — | 100 | −18 | 202 | 0 |
| 2 | 124 | — | — | 100 | −24 | 178 | 0 |
| 3 | 128 | 202 | none | 100 | −28 | 150 | 0 |
| 4 | 126 | 178 | none | 100 | −26 | 124 | 0 |
| 5 | 120 | 150 | none | 100 | −20 | 104 | 0 |
| 6 | 112 | **124** | **146** | 100 | −12 | 92 | 0 |
| 7 | 104 | 104 | 140 | 100 | −4 | **88** | 0 |
| 8 | 100 | 92 | 132 | **146** | +46 | 134 | 0 |
| 9 | 100 | 88 | 124 | 140 | +40 | 174 | 0 |
| 10 | 100 | 134 | 120 | 132 | +32 | 206 | 0 |
| 11 | 100 | 174 | none | 124 | +24 | 230 | 0 |
| 12 | 100 | 206 | none | 120 | +20 | 250 | 0 |
| 13 | 100 | 230 | **100** | 120 | +20 | **260** | **10** |
| 14 | 100 | 260 | 100 | 120 | +20 | **260** | **20** |
| 15 onward | 100 | 260 | 100 | 100 | 0 | 260 | 0 |

**Extra production: 202 ML. Spilled over the weir: 30 ML. Minimum storage: 88 ML on day 7.**

**The rule cannot work, and the reason is arithmetic.**

Actual storage first falls below 150 on **day 4**. With the two-day verification delay the utility sees it on **day 6**. With the two-day production delay the extra water arrives on **day 8** — **one day after the trough**.

**Every megalitre of the intervention arrives too late to prevent what it was ordered to prevent**, and thirty of them go over the weir.

### Retuning the trigger — computed, not asserted

| Trigger | Fires | Arrives | Minimum storage | Extra production | Spill |
|---|---:|---:|---:|---:|---:|
| **150** (the actual rule) | day 6 | day 8 | **88** (day 7) | 202 | **30** |
| **180** | day 4 | day 6 | **104** (day 5) | 242 | **70** |

**A higher trigger helps and does not fix it.** The minimum rises by 16 ML and remains below the critical level of 120. The spill more than doubles. And a trigger only 40 ML below the operating target will fire in ordinary summers.

## 6. Trajectory C — a flow-triggered rule

The same rule keyed to demand rather than storage: *when the most recent verified demand exceeds 115 ML/day, set production to that demand plus 20; otherwise return to standing.*

Demand rises on day 1, so the rule fires on day 3 and water arrives on day 5.

| Day | Demand | Production | Net | Storage | Spill |
|---|---:|---:|---:|---:|---:|
| 1–4 | 118, 124, 128, 126 | 100 | −18, −24, −28, −26 | 202, 178, 150, **124** | 0 |
| 5 | 120 | 138 | +18 | 142 | 0 |
| 6 | 112 | 144 | +32 | 174 | 0 |
| 7 | 104 | 148 | +44 | 218 | 0 |
| 8 | 100 | 146 | +46 | **260** | **4** |
| 9 | 100 | 140 | +40 | **260** | **40** |
| 10 onward | 100 | 100 | 0 | 260 | 0 |

**Extra production: 216 ML. Spilled: 44 ML. Minimum storage: 124 ML on day 4 — the critical level is never breached.**

## 7. The comparison

| | Do nothing | Stock-triggered | Flow-triggered |
|---|---:|---:|---:|
| Minimum storage | 88 (day 7) | 88 (day 7) | **124** (day 4) |
| Days below the critical level | day 5 onward, permanently | days 5–7 | **none** |
| Extra production | 0 | 202 ML | 216 ML |
| Spilled | 0 | 30 ML | **44 ML** |
| Storage at day 18 | **88 ML** | 260 ML | 260 ML |

**Neither rule dominates.** The stock rule wastes less and does not protect. The flow rule protects and spills about half as much again.

**The manuscript must present this as a choice with a cost, not as a solution.**

## 8. The policy-resistance instance

Restoring pressure at the Hillcrest inlet, on the sixty-eight-year-old feeder main Chapter 7 identified.

| Step | Extra delivered to Hillcrest | Extra leakage | Total extra draw | Share delivered |
|---|---:|---:|---:|---:|
| First pressure increase | **3.0** | **4.0** | **7.0** | **43%** |
| Second increase | **2.0** | **6.0** | **8.0** | **25%** |
| Both together | **5.0** | **10.0** | **15.0** | **33%** |

All figures ML/day.

**The loop.** Higher inlet pressure delivers more water to Hillcrest households and simultaneously drives more water out through the main's existing defects. The lost water lowers pressure downstream, which is the observation that prompts the next increase.

**Two thirds of the water drawn to fix Hillcrest never reaches Hillcrest.**

No new physical fact: Chapter 7 established the main's age, and Chapter 12's scheme B established that pressure management changes leakage.

## 9. What this case may not be used for

- Re-estimating anything Chapter 7 declared not identified.
- Recommending a capital programme — Chapter 12 did that.
- Any claim about how often overshoot occurs in practice. The mechanism is sourced; no frequency is claimed.
- Any suggestion that these values are typical, standard, or recommended for a real utility. They are synthetic and internally consistent, and nothing more.
