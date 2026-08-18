# Chapter 7 Identification Case Data

Status: drafting freeze. Extension of the Chapter 1–6 case-data files, all of which remain authoritative for every value they contain.

All values here are **synthetic authoring data**. They are not industry averages, regulatory standards, design guidance, or values from any real utility.

## What this file adds

Chapter 7 introduces **no new case**. It takes the sentence Chapter 6 left hanging — *we are about 91% sure it is the pump, so replace the pump* — and asks what would have to be true for any available evidence to support it.

It adds a network-wide upgrade record, a feeder-main age fact, and a list of what "replace the pump" could mean.

## Carried forward

| From | Item |
|---|---|
| Ch 2 | **Mechanism A** — the duty pump's capacity limits refill, so the hilltop tank falls |
| Ch 2 | **Mechanism B** — friction loss along an old, undersized feeder main drops pressure at the top of the zone |
| Ch 2 | Duty pump capacity **1.1 ML/day** |
| Ch 6 | Prior odds **7 : 4** for A from the pumped-zone investigation register |
| Ch 6 | After a recovery on the pump test, about **91%** for Mechanism A |
| Ch 1 | Demand forecast conditional on **no new action** |
| Ch 4 | The Hillcrest zone figure is a **subtraction residual** |
| Ch 5 | The storage model has **no spill term** |

## The claim under examination

> *Replacing the pump will stop the pressure drops at Hillcrest.*

**Every one of the five estimand attributes is missing from that sentence.** That is the §2 demonstration and it is why the sentence is quoted verbatim in the manuscript.

## The upgrade record

The utility has **fifteen pumped zones**. Six had duty-pump upgrades during a capital programme over the last twelve years; nine did not.

Mean low-pressure complaints per heat event:

| | Zones | Before the programme | After |
|---|---:|---:|---:|
| Upgraded | **6** | **6.8** | **4.1** |
| Not upgraded | **9** | **2.9** | **2.6** |

### Three comparisons, all arithmetically correct

| Comparison | Arithmetic | Result | Reads as |
|---|---|---:|---|
| Cross-section, after | `4.1 − 2.6` | **+1.5** | upgrades made it **worse** |
| Before and after, upgraded only | `4.1 − 6.8` | **−2.7** | upgrades helped a great deal |
| Difference in differences | `(4.1 − 6.8) − (2.6 − 2.9)` | **−2.4** | upgrades helped |

**The first points the wrong way.** That is deliberate and is the reason this record exists rather than a gentler one.

Network-wide means, for reference: **4.46** before, **3.20** after.

### Why each comparison is what it is

**The allocation rule.** The six zones chosen for upgrade were **the six worst-complaining zones at the time the programme was funded.** Allocation was made on past values of the outcome itself.

**The unrelated trend.** A separate mains renewal programme ran across the network over the same period. The non-upgraded zones' fall of **0.3** is its visible trace.

**And the difference in differences is not safe either.** It requires that the upgraded zones would have moved like the others had nothing been done. They were selected for being extreme, so part of the 2.7 fall is regression to the mean, and nothing in the table separates it.

**The manuscript must not present any of the three as the answer.** All three rest on assumptions; only one of the assumptions is nameable from the data at hand.

## The feeder-main ages

| Group | Oldest feeder main |
|---|---:|
| Hillcrest | **68 years** |
| The six upgraded zones | none older than **40 years** |
| The nine non-upgraded zones | two over 60, Hillcrest among them |

**For zones like Hillcrest, the probability of having been upgraded in this record is zero.** Not small — zero. There is no comparable upgraded case anywhere in the data.

This is the chapter's positivity failure. It is structural, stateable in one sentence, and completely invisible in the three comparisons above.

## What "replace the pump" could mean

Four things the utility could actually do, all recorded in the register as *pump upgrade*:

| Option | Action |
|---|---|
| 1 | Like-for-like replacement at the existing **1.1 ML/day** |
| 2 | A higher-capacity duty pump at **1.5 ML/day** |
| 3 | A second pump in parallel |
| 4 | A variable-speed drive on the existing pump |

**They may have different effects, and two of them may have opposite signs.** Under Mechanism B, friction loss grows sharply with flow, so pushing more water through the same 68-year-old main — options 2 and 3 — could reduce pressure at the top of the zone rather than raise it.

This is the chapter's consistency failure, and it is not pedantic: the four options differ in cost, in disruption, and plausibly in direction.

## The target trial

> Randomly assign the fifteen pumped zones to receive a duty-pump upgrade or not, follow them through the next several heat events, and compare mean complaints per heat event.

Writing it exposes three things at once:

- there are only **fifteen** zones;
- you cannot ethically withhold an upgrade from a zone that needs one;
- heat events do not arrive on a schedule.

**The trial is infeasible, and the infeasibility is informative.** The protocol names exactly which assumption the observational analysis is being asked to carry: that allocation was as good as random given what was measured, which the allocation rule above flatly contradicts.

## Prohibited interpretations

Do not write or imply that:

- any of these values are typical, standard, or recommended for water utilities;
- fifteen zones is enough to support any of the three comparisons;
- the difference in differences is the right answer, or that any of the three is;
- allocating upgrades to the worst-complaining zones was a mistake by the utility — it is a reasonable operational policy that happens to destroy exchangeability, and saying so is the point;
- the positivity failure would be fixed by more zones, more years, or more records;
- Mechanism B is established because option 2 might backfire — the point is that the sign is unknown, not that it is negative;
- the 91% from Chapter 6 is wrong; it is correct and about a different question;
- running the target trial is being recommended;
- any of this establishes what the utility should do, which needs Chapter 11.

## Publication gate

Frozen for first drafting.

Before publication freeze, a drinking-water utility SME should review the fifteen-zone record, the allocation rule, the feeder-main ages, and the four pump options for plausibility — and in particular should confirm that option 2 could plausibly worsen pressure under Mechanism B, since the manuscript leans on it.

**These facts inherit Chapter 1's open Gate 1, now seven chapters deep.** Seven case-data files now extend one anchor whose operating story has never been reviewed by a domain expert. This is a standing risk and remains a book-level decision the author has not yet made.
