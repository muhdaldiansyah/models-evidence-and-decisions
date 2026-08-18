# Research 04: The Discriminator, the Chapter's Case, and Exercise Design

Cluster 4 of four. Source locators were taken from reading the documents directly. Case arithmetic was computed and checked before this dossier was written.

## 1. The debt Chapter 4 left

`../04-observation-provenance/spec.md` L36 requires that Chapter 15's distinction arrive "in a form the reader can apply, since institutional purpose and strategic response look identical from inside a dataset."

**That is a demand for a discriminator, not a definition**, and it is the sharpest specification any chapter has handed another in this book.

`../04-observation-provenance/chapter.md` L710–722 sets it up:

> "Chapter 15 is about what happens when the people in a system respond to being measured. This chapter is not about that, and the difference is worth being able to see."

> "the records changed because people learned they were being used."

> "nothing about the network changed. What changed was the recording process, in response to being watched."

## 2. Why inspection cannot do it

Both produce the same signature inside a dataset: a recorded quantity that does not correspond to the thing it names, systematically, in a direction that suits whoever kept the record.

**Chapter 4's version** — records exist because a process created them for a purpose, and the purpose shapes what gets recorded. This is present from the beginning and has no author who intended the distortion.

**Chapter 15's version** — the record changed because somebody with an interest in the number learned it had consequences.

**No pattern in the values distinguishes them**, and a reader who goes looking for one will find whichever they expected.

## 3. The discriminator, and it is a date

**Find the moment the measure acquired consequences. Then look for a discontinuity at that moment and not before.**

**Why this works.** Institutional purpose is a standing property of a recording process. It produces distortion that is present throughout the record, drifts slowly as the institution changes, and has no reason to move sharply on any particular day.

**Strategic response has a start date**, because it begins when somebody learns the number matters — the day the metric is published, penalised, bonused, or league-tabled.

**Three things make the check applicable rather than merely correct.**

**The date is usually documentable.** Regulatory determinations, incentive schemes, and published league tables have commencement dates in public documents.

**The check needs no counterfactual.** Compare the record with itself, before and after.

**And it fails safely.** A discontinuity at the date is strong evidence of response. No discontinuity is weak evidence of anything — the response may be gradual, or the measure may have been anticipated — and the chapter must say so, because a discriminator presented as decisive would be worse than none.

## 4. The chapter's case

**The twelfth recurrence of the water anchor, and the first with a second party.**

### 4.1 The metric and the date

The regulator has always collected **properties below minimum pressure**, counted at a **representative measurement point** in each zone — the arrangement Chapter 3 established.

**In 2019 it became an incentive.** The count entered a published comparative table with a financial consequence attached, and **£1.8m** was at stake for this utility across the price-control period. Before 2019 it was reported and unpenalised.

**That is the date**, and it is documentary rather than inferred.

### 4.2 The series

| Year | Properties reported below minimum pressure | Low-pressure complaints | Complaints per reported property |
|---|---:|---:|---:|
| 2016 | 1,280 | 875 | 0.68 |
| 2017 | 1,210 | 884 | 0.73 |
| 2018 | 1,230 | 911 | 0.74 |
| **2019** | **770** | **905** | **1.18** |
| 2020 | 690 | 880 | 1.28 |
| 2021 | 640 | 915 | 1.43 |
| 2022 | 610 | 930 | 1.52 |

**Pre-2019 mean: 1,240 reported, 890 complaints, ratio 0.72.**

**2019 against that mean: reported down 37.9%, complaints up 1.7%.**

**2022 against that mean: reported down 50.8%, complaints up 4.5%.**

### 4.3 What actually happened

**No capital work was done and nothing in the network changed.**

Between 2018 and 2020 the utility re-designated the representative measurement point in **9 of its 15 zones**. **Seven of the nine moved to a point at lower elevation**, where pressure is higher.

**Every move was documented, justified in writing, and compliant with the regulator's guidance**, which delegates point selection to the licensee.

### 4.4 The relationship that broke, quantified

The utility's planning model used **0.72 complaints per reported property**, fitted on 2016–2018 and stable across those years.

**Applied to 2022's reported count of 610, it forecasts 439 complaints. The actual figure was 930.**

**The outcome is 112% higher than the forecast**, and the forecast is 53% below what happened — wrong by more than a factor of two either way you state it, on a relationship that had held for years, broken by nothing that happened to the network.

**That is Goodhart's law with a number attached**, and it is the chapter's central demonstration.

## 5. The four mechanisms on the case

Using `manheim2019goodhart` p. 2's taxonomy:

**Regressional.** Zones are selected into the count by measured pressure at one point, which contains noise. Present before 2019 and unavoidable.

**Extremal.** Pushing the count down moves the utility into a region — sensors sited at the most favourable points — where the old count-to-complaints relationship no longer describes anything.

**Causal.** Moving a sensor intervenes on the proxy and not on the goal. Nobody's water pressure changed.

**Adversarial.** The utility selected a measurement protocol knowing which protocol the regulator would score. `manheim2019goodhart` p. 8's Campbell's Law case exactly.

**All four are present, which the source says is usual**, and separating them is what lets the chapter say that only the fourth involves anybody deciding anything.

## 6. The strategic structure

The regulator and the utility are two players with different objectives, and each is affected by what the other does.

**A two-by-two, in the convention of `osborne2004game` p. 19.** Payoffs are the book's own construction on the case, in units of the regulator's own objective — properties genuinely receiving adequate pressure, in hundreds — with the utility's payoff net of its costs.

| | Utility: report as sited | Utility: re-site to favourable points |
|---|---|---|
| **Regulator: no incentive** | 12.4 , 0 | 12.4 , −0.3 |
| **Regulator: incentive on the count** | 13.1 , −1.8 | **12.4 , +1.8** |

**The bottom-right cell is the equilibrium.** Given the incentive, the utility does better re-siting. Given re-siting, the regulator does no worse keeping the incentive than dropping it. Neither can improve alone.

**And it delivers exactly what the top-left cell delivered**, at a cost of £1.8m transferred and nine measurement points moved. **The equilibrium is worse than the situation before anybody optimised anything**, and no rule was broken to get there.

## 7. The six machinery terms, one instance each

**Strategic dependence.** The utility's best measurement protocol depends on what the regulator scores.

**Incentive.** The £1.8m, which changed no physical fact and changed behaviour.

**Equilibrium as consistency.** The bottom-right cell, where both parties' expectations about the other are correct.

**Commitment.** The regulator could bind itself to fixed measurement points for five years. That removes the response — and removes its ability to correct genuinely bad siting.

**Information asymmetry.** The utility knows which points are favourable; the regulator does not, and cannot cheaply find out.

**Delegation.** The regulator's guidance delegates point selection to the licensee, which is what makes the asymmetry actionable.

**`principal-agent` and `information asymmetry` have no obtained source** — see `research-plan.md` and `../../decisions/0022` clause 9. Their treatment here is minimal and is referred to the author.

## 8. Exercise design notes

**The opening task must not mention strategy.** Give the reader the seven-year series and the fact that no capital work was done, and ask what happened. A reader who reaches for a strategic explanation unprompted has the chapter's competence already; a reader who reaches for "the network improved" has the finding.

**The predicted failure is to call it fraud.** Every move was legal, documented, and compliant, and the manuscript must make that impossible to miss, or the chapter teaches indignation.

**The diagnosis task should include a statement that correctly identifies gaming and prescribes the wrong remedy**, because "get a better metric" is the commonest wrong answer and it is not obviously wrong.

**The transfer forms need**: a metric with a documentable date of consequence; a before-and-after series in which the metric moves and the underlying thing does not; a legal, documented mechanism; a broken planning relationship quantified as a forecast error; and a two-party structure with an equilibrium worse than the status quo ante.
