# Chapter 6 Cold-Transfer Task — Form A

Status: reader-delivery copy. Governed by `spec.md` (Transfer target) and `transfer.md`.

Without consulting the Chapter 6 chapter text, the water case, or the rubric, work the situation below.

**You are the analyst.** Produce numbers and the reasoning that supports them.

Every fact you need is supplied. Do not look anything up; if something you need is missing, say what it is and whether it would change your answer.

Current pilot target: **45 minutes**. This is a design parameter pending pilot evidence, not a universal standard.

## The situation

A regional delivery operator runs a fleet of light vans.

One van, **Unit 14**, stalls intermittently. It has stalled eleven times in six weeks, always under load, never on the workshop rig. Two explanations are on the table.

> **Explanation P — an intermittent fault in the wiring loom.**
> A chafed or corroded connection interrupts supply to the injector control momentarily under vibration, and the engine cuts.

> **Explanation Q — a fuel delivery restriction.**
> A partially blocked filter or a weakening lift pump fails to maintain delivery when demand is highest, and the engine starves.

Both are consistent with everything observed so far. They point at different repairs — a loom section or a fuel system overhaul — and at very different costs.

## The workshop register

The operator's workshop keeps a register of intermittent-stall investigations, restricted to **vans of this class and age**, which is the population the fleet engineer considers relevant:

| Investigation outcome | Count |
|---|---:|
| Loom fault | **9** |
| Fuel delivery | **6** |
| **Total** | **15** |

The register covers seven years. Two of the fifteen were investigated by a contractor whose records the workshop no longer holds.

## The proposed observation

Run Unit 14 on the rig with a datalogger recording supply voltage at the injector control, and drive it loaded over a rough test route until it stalls.

The observation of interest is a **recorded voltage dropout at the moment of the stall**.

The fleet engineer supplies what to expect:

| | Voltage dropout recorded | No dropout recorded |
|---|---:|---:|
| If Explanation P holds | **0.80** | 0.20 |
| If Explanation Q holds | **0.20** | 0.80 |

The test costs a day of the van's availability and half a day of a technician's time.

## A further detail

The driver, asked for anything else, adds:

> *It happens more often on hot days.*

The fleet engineer's assessment of that report:

| | Driver reports more stalls on hot days |
|---|---:|
| If Explanation P holds | **0.65** |
| If Explanation Q holds | **0.60** |

## The workshop's forecasting record

For every vehicle sent for diagnosis, the workshop supervisor states the chance it will be **back in service within 24 hours**. Over the last 36 vehicles:

| Stated probability | Vehicles | Back within 24h | Observed frequency |
|---:|---:|---:|---:|
| 80% | 12 | 6 | |
| 60% | 12 | 7 | |
| 40% | 12 | 5 | |
| **Total** | **36** | **18** | |

## Produce

Write a response containing all six items.

1. **State a probability for Explanation P before the test**, and write what it is conditional on. Name the population your number comes from.
2. **Work out what the test is worth.** Compute the ratio between the two supplied numbers and say in words what it means.
3. **Work both branches.** What should the fleet engineer believe if a dropout is recorded? If none is recorded? Give both as probabilities.
4. **The driver's report.** Compute what it does to your number, and say what follows about acting on it.
5. **The forecasting record.** Complete the observed column. State the pattern in one sentence a fleet manager could act on, and say what a supervisor who stated 50% for every vehicle would score.
6. **Should the operator run the test?** One paragraph, using your own numbers.

**Stop when your response is complete. Do not open the rubric until then, and do not open Form B at all.**
