# Research 04 — Transport, Support Factors, and the Chapter's Own Examples

Cluster R04 of `research-plan.md`. Closed.

Sources read directly: `deaton2016rct` printed pp. 27–29; `bareinboim2016fusion` printed p. 7350. `adcock2001validity` p. 530 reused as verified for Chapter 3.

## 1. What is wrong with `external validity`

The term exists, the reader will meet it, and the source that supplies this chapter's treatment objects to it.

The definition first:

> "Suppose a trial has established a result in a specific setting. If `the same' result holds elsewhere, it is said to have `external validity'. External validity may refer just to the transportability of the causal connection, or go further and require replication of the magnitude of the ATE. Either way, the result holds—everywhere, or widely, or in some specific elsewhere—or it does not." [@deaton2016rct, p. 27]

Then the objection:

> "This binary concept of external validity is often unhelpful because it asks the results of an RCT to satisfy a condition that is neither necessary nor sufficient for a trial to be useful, and so both overstates and understates their value. It directs us toward simple extrapolation—whether the same result holds elsewhere—or simple generalization—it holds universally or at least widely—and away from more complex but more useful applications of the results." [@deaton2016rct, p. 27]

**Neither necessary nor sufficient.** Not necessary, because a study can be useful without its result holding elsewhere. Not sufficient, because a result holding elsewhere does not make the study useful for your decision.

**Recommended handling: register the term and register the objection**, exactly as Chapter 8 registered `statistical significance` as a hazard. The reader must recognise the phrase in other people's writing and must not organise their own thinking around it.

The paper also notes that some uses of a trial "do not require transportability beyond the original context" [@deaton2016rct, p. 27], which is why the binary framing understates value.

## 2. What actually makes a result carry

This is the cluster's most useful finding and it is a physical idea rather than a statistical one.

> "The operation of a cause generally requires the presence of 'support factors', without which a cause that produces the targeted effect in one place, even though it may be present and have the capacity to operate elsewhere, will remain latent and inoperative." [@deaton2016rct, p. 28]

The source's own example, on the same page: a house burns down because a television was left on, "although televisions do not operate in this way without support factors, such as wiring faults, the presence of tinder, and so on."

And the consequence for averages, p. 29:

> "two populations will have the same ATE if and only if they have the same average for the net effect of the support factors necessary for the treatment to work" [@deaton2016rct, p. 29]

Followed by the observation that makes it bite:

> "These are however just the kind of factors that are likely to be differently distributed in different populations" [@deaton2016rct, p. 29]

**So transport is not a statistical adjustment.** It is a question about whether the conditions a cause needs in order to operate are present in the new setting, and answering it requires knowing what those conditions are — which is subject-matter knowledge, not data.

The paper puts the general form at p. 29: "Causal processes often require highly specialized economic, cultural, or social structures to enable them to work."

**Attribution note.** The paper attributes the underlying analysis of such conditions to Mackie (1974) under the name INUS causality, and gives an example from Cartwright and Hardie (2012). **Neither was obtained**, and the book uses only `support factor` and the television example, both from the page in front of it.

## 3. The same idea from the other tradition

`bareinboim2016fusion` reaches the transport problem as its fourth task and states the general position:

> transportability "lies at the heart of every scientific investigation because, invariably, experiments performed in one environment are intended to be used elsewhere, where conditions are likely to be different." [@bareinboim2016fusion, p. 7350]

And it identifies the specific threat with unusual bluntness:

> "This disparity is indeed a major threat to the validity of randomized trials. Because participation cannot be mandated, we cannot guarantee that the study population would be the same as the population of interest." [@bareinboim2016fusion, p. 7350]

With the mechanism named: study populations "may consist of volunteers, who respond to financial and medical incentives offered by pharmaceutical firms or experimental teams, so the distribution of outcomes in the study may differ substantially from the distribution of outcomes under the policy of interest" [@bareinboim2016fusion, p. 7350].

**Two traditions, one conclusion**, which is worth stating because they disagree about method. One reaches it through support factors and subject-matter structure; the other through formal characterisation of how populations differ. Both say a result does not travel by default.

## 4. Chapter 3's contextual specificity, reused

`adcock2001validity` p. 530, verified for Chapter 3, established that a measure valid in one context may be invalid in another.

`../../decisions/0010` clause 2.4 recorded explicitly: "It is **not** extended into transportability, which is Chapter 9."

**The extension is now permitted and should be made once.** Chapter 3's point was about a measure and a context; this chapter's is about a finding and a setting. They are different claims of the same shape, and the reader who has held the first for six chapters can be given the second in a sentence.

## 5. The identity worth stating once

Chapter 7's sharpest failure was **positivity**: no zone with a feeder main older than 40 years had ever received a pump upgrade, so the record contained no case resembling Hillcrest.

Chapter 9's transport failure asks whether a result established in the recorded zones applies to Hillcrest.

**These are the same fact.** Positivity asks whether the record contains cases like the target; transport asks whether a result from the record applies to the target. When no case resembles the target, the record cannot speak to it, and it does not matter which direction you approach from.

**This is the book's own observation**, not either source's, and it should be stated once and labelled. It is the strongest available evidence that the book's chapters are one architecture: a failure diagnosed in Chapter 7 with one vocabulary is rediagnosed in Chapter 9 with another, on the same numbers.

## 6. The anchor's five sources

The utility must decide about Hillcrest before next summer. Five things bear on it, and none of them is about it.

| | Source | Size | Estimate | The stated defect |
|---|---|---:|---:|---|
| A | The utility's own upgrade record | 15 zones | **−2.4** | not identified (Chapter 7) |
| B | A neighbouring utility's before-and-after study | 40 zones | **−3.1** | flat terrain throughout |
| C | An industry benchmarking dataset | 1,400 zones | **−0.6** | self-reported, participation voluntary |
| D | The pump manufacturer's rig test | 6 rigs | **−4.8** | no feeder main in the rig at all |
| E | An expert panel | 5 engineers | **−1.5** | judgment, never scored |

Estimates are the change in mean low-pressure complaints per heat event following a duty-pump upgrade.

### The four rules

| Rule | Result |
|---|---:|
| Simple average of all five | **−2.48** |
| Median of all five | **−2.40** |
| Weight by sample size (A–D) | **−0.70** |
| Drop C, average A, B, D | **−3.43** |

Arithmetic verified. Under size weighting, source C carries **95.8%** of the weight — `1400 ÷ 1461` — and it is the source with a stated participation defect.

### The support factor, and the transport failure

Hillcrest is a **hilltop** zone: the duty pump must lift water against static head as well as overcome friction.

Source B's forty zones are on flat ground. There, a pump upgrade relieves friction loss and nothing else. **The mechanism by which an upgrade helps at Hillcrest — restoring lift against static head — is absent from every zone in source B**, and terrain is precisely the support factor `deaton2016rct` p. 28 describes: present in one setting, absent in another, and decisive for whether the cause operates.

Source D's rigs have no feeder main at all, so Mechanism B cannot occur in them.

**And no source contains a zone with a feeder main older than 40 years.** Hillcrest's is 68. That is Chapter 7's positivity fact, and it now applies to all five sources rather than to one record.

### What the reader should end at

Not a number. **A statement of what would have to be true for any of the five to apply at Hillcrest**, and the observation that the two things that would settle it — terrain and main age — are known, are recorded, and were never used to select sources.

## 7. Prohibitions for the manuscript

- No synthesis method. No inverse-variance weighting, no random-effects model, no heterogeneity statistic.
- No selection diagrams, transport formulas, or graphical machinery.
- No claim that any of the four rules is correct.
- No claim that any of these values is typical of water utilities.
- Russell, Mackie, and Cartwright and Hardie are cited **as reported at** `deaton2016rct` and never directly.
- `deaton2016rct` described as an unrefereed working paper; its strongest claims attributed.
- No elicitation machinery for expert judgment; reuse Chapter 6.
- No recommendation about what the utility should do — Chapter 11.

## 8. Stop condition

Met. The objection to binary external validity recorded; `support factor` recorded with the source's own example and its consequence for averages; the second tradition's version recorded; Chapter 3's extension authorised; the positivity/transport identity stated as the book's own; five sources and four rules specified and checked.
