# Research 04: Information Acquisition, Exploration, and the Chapter's Case

Cluster 4 of four. Source locators were taken from reading the documents directly. Case arithmetic was computed and checked by simulation before this dossier was written.

## 1. Exploration and exploitation, defined

`sutton2018reinforcement` p. 26, on a set of options whose values are estimated:

> "When you select one of these actions, we say that you are exploiting your current knowledge of the values of the actions. If instead you select one of the nongreedy actions, then we say you are exploring, because this enables you to improve your estimate of the nongreedy action's value."

And the trade in one sentence, same page:

> "Exploitation is the right thing to do to maximize the expected reward on the one step, but exploration may produce the greater total reward in the long run."

> "Reward is lower in the short run, during exploration, but higher in the long run because after you have discovered the better actions, you can exploit them many times."

**All three extract cleanly.** The framing sentence at p. 3 that names the dilemma does not — it contains the `ff` ligature — and is paraphrased in the manuscript with the paraphrase declared.

Two further sentences from p. 3, both clean and both load-bearing:

> "The dilemma is that neither exploration nor exploitation can be pursued exclusively without failing at the task."

> "The exploration–exploitation dilemma has been intensively studied by mathematicians for many decades, yet remains unresolved."

**The second is the one the chapter needs most.** A chapter that presented a resolution would be misrepresenting the field, and the source says so itself.

## 2. What the source refuses, and the book follows

`sutton2018reinforcement` p. 27:

> "In this book we do not worry about balancing exploration and exploitation in a sophisticated way; we worry only about balancing them at all."

**Chapter 14 takes the same position at one further remove**: it does not balance them at all, it establishes that the trade exists and that the utility has never made it.

The k-armed bandit is **named once**, from p. 26's own gloss — the problem is "so named by analogy to a slot machine, or 'one-armed bandit,' except that it has k levers instead of one" — and no method for it is taught.

## 3. Information acquisition, and why it is not recomputed

Chapter 11 taught value of information as arithmetic, with the perfect-information ceiling as a screening rule, from `colyvan2016voi`. Chapter 12 then established that there are decisions with no probabilities to be had.

**Chapter 14's instrument decision is in the second kind of setting**, so the chapter reuses Chapter 11's **ceiling** and does not compute a value. The manuscript says why, in one paragraph, rather than inventing a prior.

`colyvan2016voi` was not re-read; its locators were verified during Chapter 11 and nothing new is claimed from it.

## 4. The chapter's case — design constraints and arithmetic

**The eleventh recurrence of the water anchor, and the first run across several years.**

Constraints from `readiness-audit.md` §8, all met.

### 4.1 Five summers, four rules

Reservoir capacity **260 ML**, critical level **120 ML**, standing production **100 ML/day**, as in Chapter 13. Verification delay two days, production delay two days, as in Chapter 13. Each summer starts from its own storage level.

**The four rules**, all stated as rules rather than as actions:

- **P0 — do nothing.** Hold production at the standing level.
- **P1 — stock-keyed.** The utility's actual rule, unchanged from Chapter 13: when verified storage is below 150, set production to verified demand plus 20; when above 210, return to standing.
- **P2 — flow-keyed.** Chapter 13's repair: when verified demand exceeds 115, set production to that demand plus 20; otherwise standing.
- **P4 — both.** Act only when verified demand exceeds 115 **and** verified storage is below 200; otherwise standing.

**Results, computed by simulation.** Each cell is minimum storage / days below the critical level / spill / extra production.

| Summer | Start | P0 | P1 | P2 | P4 |
|---|---:|---|---|---|---|
| Heatwave | 220 | 88 / 14 / 0 / 0 | 88 / 3 / 30 / 202 | **124** / 0 / 44 / 216 | 104 / 1 / **6** / 178 |
| Mild | 220 | 190 / 0 / 0 / 0 | 190 / 0 / 0 / 0 | 190 / 0 / 0 / 0 | 190 / 0 / 0 / 0 |
| Long moderate | 210 | 66 / 13 / 0 / 0 | 106 / 2 / 28 / 222 | 130 / 0 / 0 / 148 | 130 / 0 / 0 / 148 |
| Double peak | 220 | 80 / 13 / 0 / 0 | 84 / 3 / 38 / 218 | **148** / 0 / 66 / 246 | 132 / 0 / **28** / 208 |
| False alarm | 250 | 192 / 0 / 0 / 0 | 192 / 0 / 0 / 0 | 192 / 0 / **18** / 86 | 192 / 0 / **0** / 0 |

**Aggregate across all five:**

| Rule | Worst minimum | Days below critical | Total spill | Total extra production |
|---|---:|---:|---:|---:|
| P0 do nothing | 66 | 40 | 0 | 0 |
| P1 stock-keyed | 84 | 8 | 96 | 642 |
| **P2 flow-keyed** | **124** | **0** | 128 | 696 |
| **P4 both** | 104 | 1 | **34** | 534 |

### 4.2 The three findings the chapter is built on

**The utility's own rule is dominated.** P4 beats P1 on all four measures — higher worst minimum, fewer days below the critical level, less spill, less extra production. **A rule that is worse on every count is not a trade-off, it is a mistake**, and it has been in force for nine years.

**And P4 differs from P1 in one respect: what it watches.** Both act on the same information delay and the same production delay. P1 watches the stock; P4 watches the stock *and* the flow. Nothing about the timing, the response size, or the stand-down changed.

**The remaining choice is a genuine judgment.** P2 never breaches the critical level and spills 128 ML across five summers. P4 breaches it on one day and spills 34. **One day below the service standard against 94 megalitres of treated water** — and nothing in the arithmetic settles it. That is Chapter 10's question arriving inside a Chapter 14 problem.

### 4.3 The fact that makes §7 possible

**On the mild summer, all four rules produce identical results.** Nothing happens, nothing is learned, and a year of operating experience contains no information whatever about which rule is better.

**Between P2 and P4, two of the five summers are identical** — mild and long moderate — and three differ.

**So roughly three years in five carry information about this choice, and two do not.** The utility has nine years of experience with P1 and none with anything else, and in a substantial fraction of those years the experience would not have discriminated even if it had been looking.

## 5. Observability in the case

**What the utility measures:** reservoir level (verified, two days old), total production (daily), metered customer consumption (quarterly), and Zone 4 inlet pressure (continuous).

**The state it needs in order to act well:** whether high draw is hot-weather demand, or a burst.

**Both produce the same record.** Total draw rises, the reservoir falls, Zone 4 inlet pressure drops. There is nothing in the four instruments that separates them.

**This is unobservability in `astrom2008feedback` p. 202's sense** — two states, one record — and it has a direct consequence for every rule in §4.1. All four fire on the same signal. If the cause is a burst, making more water pushes more water through the burst, which is Chapter 13's policy resistance arriving inside a Chapter 14 rule.

**The repair is one instrument.** A night-flow meter at the Zone 4 inlet, reading at 03:00 when legitimate demand is near zero. Normal night flow runs about **4 ML/day-equivalent**; a burst of the kind that would move the daily figures adds about **9**. Hot weather adds essentially nothing at 03:00 — nobody waters a garden at three in the morning.

**One instrument, and the two states separate.** Cost: **£18,000** installed.

## 6. Structural non-identifiability in the case

The utility's demand model, fitted to the heatwave week:

> daily draw = base demand + heat sensitivity × maximum temperature + background leakage

Fitted values: **heat sensitivity 2.0 ML per °C**, and **base demand plus leakage equal to 82 ML/day**.

**The fit is exact.** At maximum temperatures of 18, 21, 23, 22, 19, 15 and 11 °C the model returns 118, 124, 128, 126, 120, 112 and 104 ML/day — the seven demand figures the book has been using since Chapter 13.

**And base demand and leakage cannot be told apart.** They enter the model only through their sum. Every split of 82 fits identically:

| Base demand | Leakage | Total | Fits? |
|---:|---:|---:|---|
| 78 | 4 | 82 | exactly |
| 60 | 22 | 82 | exactly |
| 40 | 42 | 82 | exactly |

This is `wieland2021identifiability` p. 61's mechanism: the change in one parameter "can be fully compensated by altering other parameters."

**Two things follow, and both matter.**

**The non-identifiability was knowable before any data existed.** It follows from the model's form and the fact that only total draw is measured. Nobody needed twelve years of records to discover it; anyone could have seen it on a napkin.

**And it makes a live decision undecidable.** Chapter 12 costed network pressure management at £380,000. What that scheme is worth depends on how much of the 82 is leakage — and the utility's records cannot say. At 4 ML/day of leakage the scheme has almost nothing to work on; at 22 it has a great deal.

**The instrument that resolves the observability failure also resolves this one.** Night flow at 03:00 is leakage, near enough, because base demand is near zero then. The £18,000 meter splits the 82.

## 7. Information acquisition in the case

**No probability is available and none is invented.** Chapter 11's arithmetic needs a prior over the states; Chapter 12 established that this book's setting frequently has none, and this is such a setting.

**Chapter 11's ceiling is used instead.** The most that perfect knowledge of the leakage split could be worth is bounded by the cost of misallocating the decision it affects, and the decision it affects is a £380,000 scheme. **The meter costs 4.7% of that.**

**A ceiling argument does not say the meter is worth buying.** It says the meter cannot be screened out on cost, which is what a ceiling is for — and Chapter 11 taught exactly that use.

## 8. Exercise design notes

**The opening task must ask for a rule, not an action.** The reader has spent thirteen chapters producing analyses, estimates, and choices. Asking for a rule — stated precisely enough for somebody else to apply — is the shift, and it should happen before any vocabulary arrives.

**The predicted failure is a rule that cannot be applied.** *Increase production when storage looks low* is not a rule; it has no threshold, no response size, and no stand-down. Chapter 12's signpost discipline is the standard, and readers who met it will do better.

**The comparison task must use more than one summer**, because the point cannot be made on one. Readers given one summer will rank the rules confidently and wrongly.

**The diagnosis task should include one statement that is true of the case and false as a general claim**, so that the exercise tests the distinction between a finding and a rule.

**The transfer forms need**: a repeated decision with a stated rule; several histories over which to compare rules; two states the instruments cannot distinguish; two model parameters that enter only as a sum; and one instrument that would fix both, priced against a decision already on the table.
