# Research 04: The Two Cases, and Exercise Design

Cluster 4 of four. Case arithmetic was computed and checked before this dossier was written.

## 1. Both cases are inherited

**Neither case is new**, and that is the point of a closing chapter: it operates what the book already built.

**Case 1** is the adaptive plan Chapter 12 wrote, run for four years. `canon/terminology.md`'s `signpost` entry assigns this here: "Chapter 12 designs signposts and Chapter 17 operates them, which is where the question of whether anyone is actually looking belongs."

**Case 2** is the automated tool Chapter 16 analysed. Chapter 16's own last section hands it over: "Chapter 17 asks what happens next."

**Case 1 is the water anchor's thirteenth and final appearance.** The chapter says so.

## 2. Case 1 — operating Chapter 12's signposts

### 2.1 The plan, quoted from Chapter 12 unchanged

> **Watch.** Peak-week demand against the Chapter 1 forecast, reported each September. Heat events per year, already counted for the regulator.
>
> **If.** Peak-week demand exceeds the forecast by more than four per cent in two consecutive summers, **or** heat events exceed six in a single year, stage 2 of the trunk reinforcement enters the following year's programme at an assumed **£1,150k**.
>
> **Owner.** The asset planning lead reports both signposts to the capital committee each October, whether or not either has triggered.

**Chapter 12 also wrote, in its own text:** "Four per cent, two consecutive summers, six heat events — those numbers are arguable, and being arguable is the property that matters."

**This chapter argues with them**, which is what that sentence invited.

### 2.2 The baseline nobody computed

**Peak-week demand against the Chapter 1 forecast, the seven years before the plan:**

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 |
|---:|---:|---:|---:|---:|---:|---:|
| +0.4% | −1.2% | +2.1% | −0.8% | +1.6% | +3.3% | −0.5% |

**Mean +0.70%. Standard deviation 1.55. Maximum +3.3%.**

**The 4% threshold sits 2.12 standard deviations above the baseline mean and was never reached in seven years.** That is a well-set threshold, and nobody checked.

**Heat events per year, same seven years:**

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 5 | 2 | **7** | 4 | 3 | 5 |

**Mean 4.14. Standard deviation 1.55. Maximum 7.**

**"Exceeds six" fires on seven, and seven occurred once in the seven baseline years.**

**That is a rate of one in seven per year. Over the plan's fifteen-year horizon it is 2.1 expected firings from baseline variation alone.**

**One limb of the signpost was a trigger. The other was a timer**, and the difference is four lines of arithmetic on data the utility already had.

### 2.3 What happened over four years

| Year | Peak-week demand vs forecast | Heat events | What the October report said |
|---|---:|---:|---|
| 2023 | +1.8% | 4 | Neither signpost triggered |
| 2024 | **+5.2%** | 5 | Demand exceeded four per cent; not two consecutive summers; no trigger |
| 2025 | +2.9% | **7** | **Heat events exceeded six** |
| 2026 | **+4.6%** | 5 | Demand exceeded four per cent; not consecutive with 2024; no trigger |

**Two findings, and they are different in kind.**

**The demand limb never fired, and the plan foresaw it.** Chapter 12's own text says: "If demand jumps in a single year rather than two, stage 1 will be inadequate and the trigger will not have fired." **Demand exceeded four per cent in two of four years and never in consecutive ones**, so the rule behaved exactly as written and exactly as Chapter 12 warned.

**The heat-events limb fired in 2025 and nothing happened.** The October 2025 report recorded the value. The committee minute records "signposts reported; no action required." **The plan says stage 2 "enters the following year's programme", and it did not.**

**Why not**, and this is the chapter's material rather than a story about incompetence: the report presented both signposts together, the demand limb — which everybody had been watching for two years — had not fired, and the disjunction in the rule was read as a conjunction by people reading quickly. **The rule said "or". The report was read as "and".**

### 2.4 What the arithmetic says about the firing

**The 2025 value of seven equals the baseline maximum**, and sits 1.84 standard deviations above the baseline mean.

**So the firing is not strong evidence that anything changed.** A limb that fires on a one-in-seven-year value produces firings at about that rate whether or not the climate is moving.

**The uncomfortable conclusion** is that the committee's decision not to act was, by accident, defensible — and that nobody at the meeting could have said so, because nobody had the baseline. **A right answer reached by reading "or" as "and" is not a right answer.**

## 3. Case 2 — monitoring the repairs tool

Everything below is frozen in Chapter 16's `case-data.md` except the monitoring arrangements, which are new here and add no new fact about the tool.

### 3.1 What the authority monitored

| Indicator | 2022 | 2024 | Read as |
|---|---|---|---|
| Weekly job volume | 1,180–1,290 | 1,180–1,290 | stable |
| Repairs completed within target time | 94.1% | 95.6% | **improved** |
| Tenant satisfaction | 81% | 82% | flat |

**All three were reported monthly. All three looked fine or better.**

### 3.2 What nobody reported

**Emergency jobs divided by statutory hazard referrals: 6.83 in 2022, 8.08 in 2024 — up 18.3%.**

**Both numbers were collected. Neither team reported the ratio, because the ratio is nobody's report** — which is the same finding Chapter 15 reached about a different pair of numbers, and the chapter should note the repetition once.

### 3.3 Diagnosis by stage

**The symptom appeared at Chapter 13**: an emergency queue whose inflow doubled against a fixed servicing capacity.

**The failure entered at Chapter 4**: the tool was trained on a label that is a scheduler's decision.

**Nine stages and eighteen months apart.**

**And no monitoring arrangement could have caught it**, because a tool that reproduces its label produces outputs that look right by construction. The completion-within-target figure **improved**, and it improved for a reason: routing more jobs as emergencies gets them attended sooner, which is what the target measures.

**That is the chapter's central result on this case.** The monitoring was not inadequate. It was watching outputs, and the failure was not in the outputs.

## 4. Exercise design notes

**The opening task must ask for a monitoring design before the chapter says anything.** Give Chapter 12's plan and four years of data, and ask what should have been reported and what would have counted as a signal. **Preserve unscored.**

**The predicted failure is to check the values against the thresholds** and stop — which is what the utility did, and which produces the right answer to the wrong question.

**The second predicted failure is to blame the committee.** The chapter must make that unavailable: the rule was read wrongly, and the reading produced the defensible answer for the wrong reason.

**The diagnosis task should include one statement that correctly identifies a monitoring gap and proposes a monitoring fix for a failure no monitoring could catch** — the chapter's central claim inverted.

**The transfer forms need**: a deployed rule with thresholds, a baseline period against which those thresholds can be assessed, an operating period in which one limb fires and one does not, a set of monitored indicators that all look fine, one unreported ratio that does not, and a failure whose entry stage is early and whose symptom is late.

**And because this is the last chapter, the forms should be the last exercise.** No new machinery is introduced anywhere, and every routing decision must be traceable to a chapter the reader has read.
