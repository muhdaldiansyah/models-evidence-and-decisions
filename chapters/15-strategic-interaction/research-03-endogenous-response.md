# Research 03: Endogenous Response and Performativity

Cluster 3 of four. Every locator below was taken from reading the document directly.

## 1. Two problems with this source, both recorded

**No printed pagination.** `perdomo2020performative` was obtained as the official PMLR PDF for *Proceedings of the 37th International Conference on Machine Learning*, volume 119. The published page range 7599–7609 is verified metadata from the publication page and was recorded in the source note during Chapter 1. **The PDF itself carries no page numbers**, only the running head "Performative Prediction".

Chapter 9 met this before — with the Pearl and Bareinboim transportability paper — and **declined the source**. That is not available here: `../../decisions/0007` assigns this source to Chapter 15 by name and it has been in the bibliography since Chapter 1.

**The chapter therefore cites it by numbered section and by Abstract**, both of which are visible and checkable. Recorded at `../../decisions/0022` clause 8.

**Ligature extraction.** The typesetting renders `fi` and `ffi` as single characters: *influence* extracts as *inﬂuence*, *sufficient* as *sufﬁcient*, *traffic* as *trafﬁc*. **No quotation below contains an `fi`**, and several good sentences were lost to it.

## 2. The definition

`perdomo2020performative` §1:

> "We call such predictions performative; the prediction causes a change in the distribution of the target."

**Six words carry the whole idea**: the prediction causes a change in the distribution of the target.

Abstract:

> "A conceptual novelty is an equilibrium notion we call performative stability."

> "Performative stability implies that the predictions are calibrated not against past outcomes, but against the future outcomes that manifest from acting on the prediction."

**That second sentence is the chapter's connection to Chapter 6**, and it is worth stopping on. Chapter 6 taught calibration as a property of forecasts scored against what happened. **Here the thing to be calibrated against is what happens *because of* the forecast**, which is not available at the time of forecasting and does not exist independently of it.

## 3. The scope claim, which corrects a likely misreading

Abstract:

> "Performativity is a well-studied phenomenon in policy-making that has so far been neglected in supervised learning."

**Read that direction carefully.** The authors are not claiming to have discovered something about the world. They are claiming that a phenomenon long recognised in policy had been neglected in their own field.

**The book should quote this**, because a reader meeting the term in a machine-learning paper will otherwise take performativity for a machine-learning problem, and the chapter's whole point is that it is a general one.

§1, on how widespread:

> "Once recognized, performativity turns out to be ubiquitous."

And the examples, §1:

> "recommendations shape preferences and thus consumption, stock price prediction determines trading activity and hence prices."

## 4. What it looks like when you do not name it

Abstract:

> "When ignored, performativity surfaces as undesirable distribution shift, routinely addressed with retraining."

§1:

> "Retraining is often considered an undesired—yet necessary—cat and mouse game of chasing a moving target."

And the reframing:

> "Performativity therefore suggests a different perspective on retraining, exposing it as a natural equilibrating dynamic rather than a nuisance."

**This is the source's most transferable observation and it is not about machine learning.** An organisation whose model keeps needing to be refitted is usually treating that as maintenance. **The alternative reading is that the refitting is the system converging** — and which reading is right changes what you should do.

## 5. Where the chapter stops

§1 states the framing:

> "we formalize performative prediction, tying together conceptual elements from statistical decision theory, causal reasoning, and game theory."

**Everything after §1 is that formalisation** — the distribution map, repeated risk minimisation, repeated gradient descent, and the convergence results. **None was read beyond noting that it exists**, and the chapter teaches none of it.

## 6. What performativity is not

Two boundaries the manuscript must hold, both recorded in `../../sources/perdomo2020performative.md` since Chapter 1.

**Not every distribution shift is performative.** Populations change, instruments drift, seasons turn. The source's claim is that performativity *surfaces as* distribution shift, not that distribution shift is performativity.

**And `performative` here is a technical term with no relation to its ordinary English sense**, where it means done for show. The manuscript says this once, because the collision is severe and the ordinary sense is far commoner.

## 7. The relation to Chapter 13, which must not be blurred

Chapter 13 taught **policy resistance** — an intervention defeated by the system's response to the intervention itself — from `sterman2002models` p. 504.

**These are different.** Policy resistance needs no agent who knows the policy exists: a reservoir resists by physics. **Performativity needs somebody who acts on the prediction**, and the change in the world runs through that action.

**The chapter states the difference once and does not reuse Chapter 13's sources**, which is why `sterman2002models` and `sterman2006evidence` appear nowhere in this chapter's evidence plan despite being read and available.

## 8. What the chapter takes

| Claim | Locator |
|---|---|
| The prediction causes a change in the distribution of the target | §1 |
| Performative stability as an equilibrium notion | Abstract |
| Calibrated against outcomes that manifest from acting on the prediction | Abstract |
| Well-studied in policy-making, neglected in supervised learning | Abstract |
| Once recognized, ubiquitous | §1 |
| Recommendations and stock prices as instances | §1 |
| Ignored performativity surfaces as distribution shift | Abstract |
| Retraining as a cat-and-mouse game | §1 |
| Retraining reread as an equilibrating dynamic | §1 |
| The framework ties together decision theory, causality, and game theory | §1 |
