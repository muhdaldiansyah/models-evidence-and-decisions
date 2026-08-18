# Chapter 5 Criticism Case Data

Status: drafting freeze. Extension of the Chapter 1–4 case-data files, all of which remain authoritative for every value they contain.

All values here are **synthetic authoring data**. They are not industry averages, regulatory standards, design guidance, or values from any real utility.

## What this file adds

Chapter 5 introduces **no new case**. It criticizes the analysis Chapters 1–4 produced.

It adds only what the checks need: bounding figures the reader can use, and the resolution of the inconsistency the order-of-magnitude check exposes.

## Carried forward and used here

| From | Value |
|---|---:|
| Ch 2 | Hillcrest tank usable capacity **1.2 ML**; contents at 08:25 **0.6 ML** |
| Ch 2 | Hillcrest demand figure **0.9 ML/day**; duty pump **1.1 ML/day** |
| Ch 3 | Connected properties in Hillcrest **340** |
| Ch 4 | Hillcrest customer consumption, insertion-meter study **0.62 ML/day** |
| Ch 4 | Residual decomposition totalling **0.90 ML/day** |

## The order-of-magnitude check

Two numbers, from two different chapters, that nobody has divided.

`620,000 L ÷ 340 properties = 1,824 L per property per day`

### The bounding figure

The case supplies, for use as a rough regional planning figure: household water use of about **150 litres per person per day**, and an average household of about **2.5 people**.

`150 × 2.5 = 375 L per household per day`

`1,824 ÷ 375 ≈ 4.9`

**About five times too high.** The check took one division and one estimate.

### What the check does and does not establish

It establishes that the figures are **mutually inconsistent**. It does not say which is wrong.

Three candidates, all live before the resolution is supplied:

1. the property count is wrong;
2. the 0.62 ML/day figure is wrong;
3. Hillcrest properties are not households.

## The resolution

The case supplies the third.

**One of the 340 Hillcrest connections is a commercial horticultural nursery.** It draws about **0.40 ML per day on irrigation days**, which in summer is most days.

| | Value |
|---|---:|
| Hillcrest consumption, total | 0.62 ML/day |
| Nursery | **0.40 ML/day** |
| Remaining 339 properties | **0.22 ML/day** |
| Per remaining property | `220,000 ÷ 339 ≈` **649 L/day** |

649 L/day is high against the 375 L/day bounding figure and is plausible: the case supplies that Hillcrest properties are large-plot hillside properties with gardens, and that summer garden watering is a substantial share of their use.

The arithmetic now reconciles.

## Why this matters more than the catch

**The nursery is a single customer, on a commercial contract, whose irrigation is schedulable.**

It is roughly **65%** of Hillcrest's customer consumption — `0.40 ÷ 0.62 ≈ 0.65`.

Four chapters of analysis never saw it:

- Chapter 1 had one town-wide demand number;
- Chapter 2 had three zone numbers;
- Chapter 3 asked what *adequate* meant;
- Chapter 4 asked where the numbers came from and found the residual.

None of them revealed that most of the zone's consumption is one account that could be asked to shift its watering by twelve hours.

The billing system knows perfectly well that the nursery is a large commercial account. Nothing that reached the analysis did — which is Chapter 4's institutional-purpose finding recurring, and Chapter 2's finding that a representation can only contain the alternatives it can express.

## The limiting case

Set Hillcrest customer consumption to zero.

The Chapter 4 residual — town total minus the two metered zones — **does not go to zero.** From the Chapter 4 decomposition, leakage elsewhere (0.08), unbilled operational use (0.06), and meter under-registration (0.04) remain, plus Hillcrest-zone leakage (0.10) which is not customer consumption either.

A quantity labelled *Hillcrest demand* that stays positive when Hillcrest customers use nothing is not a demand.

**This flags Chapter 4's entire central finding in about a minute, with no provenance work at all.**

It does not *explain* it. Chapter 4's investigation produced the explanation. The check produced the alarm.

## The extreme-condition check

Set demand to zero and let treated-water input run at **8.4 ML/day**.

The Chapter 1 and Chapter 2 storage representation says storage rises without limit. There is no spill, no overflow, and no tank ceiling anywhere in the arithmetic — even though the Hillcrest tank has a stated usable capacity of **1.2 ML** and the system has **14.0 ML**.

Real tanks overflow. The model has no term for it.

This was harmless for the question Chapters 1 and 2 asked, which only ever ran storage downward. It would be wrong for any question involving refill, recovery after a drought, or what happens when demand collapses.

## The dimensional check

`0.6 ML ÷ 0.9 ML/day = 0.67 days`

Megalitres divided by megalitres-per-day gives days. The check is trivial and catches a specific error: a quotient reported as "0.67" without units, where a reader supplies the wrong ones.

Chapter 3 already exploited this deliberately in choosing metres of head, which made every pressure calculation a subtraction.

## What the analysis is adequate for, and at what risk

Supplied so that §2 can be worked rather than asserted.

The Part I analysis is adequate for: **deciding whether to request voluntary conservation during a seven-day heatwave**, at day-level resolution, for total system storage.

It is **not** adequate for: deciding which zone to restrict, sizing a pump, planning capital works, or reporting service performance.

**What happens if it is wrong:** a pressure zone falls below the operating threshold during a hot evening, and some households at the top of the zone experience low pressure until the tank refills overnight.

That is a real service consequence and it is a service consequence, not a safety event. It bounds how much criticism the analysis warrants — more than a routine monthly report, less than a decision with irreversible or safety-critical consequences.

## Prohibited interpretations

Do not write or imply that:

- any of these values are typical, standard, or recommended;
- 150 L per person per day, 2.5 people per household, or 649 L per property is a real planning figure;
- a nursery at 65% of a zone's consumption is a normal configuration;
- low pressure implies unsafe water or any specific health consequence;
- the nursery is doing anything improper, or that commercial irrigation is wasteful;
- the nursery could certainly be asked to reschedule — that is an option to be investigated, not an established remedy;
- Chapters 1–4 contained errors — they reasoned correctly from what was available;
- the cheap checks make Chapter 4's investigation unnecessary; the checks raise alarms, the investigation produces explanations;
- a real utility can operate without knowing its largest customers;
- passing all four checks would make the analysis adequate.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water utility SME should review the nursery extension and the household bounding figures for plausibility and accidental unsafe implication.

**These facts inherit Chapter 1's open Gate 1, now four chapters deep.** Five case-data files now extend one anchor whose operating story has never been reviewed by a domain expert. This is a standing risk and should be treated as a book-level decision rather than a per-chapter formality.
