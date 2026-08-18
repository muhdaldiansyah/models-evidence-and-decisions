# Research 03 — Scoring: Propriety, Calibration, Sharpness

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision.

Cluster R03 of `research-plan.md` §6. Research conducted 2026-08-18.

Source: `gneiting2007scoring` (primary, pp. 359–360 read).

## 1. Q1 — What makes a scoring rule one you cannot game

### Propriety

`gneiting2007scoring` p. 359 states the property directly:

> "The forecaster has no incentive to predict any P ≠ Q and is encouraged to quote his or her true belief, P = Q, if S(Q, Q) ≥ S(P, Q) with equality if and only if P = Q. A scoring rule with this property is said to be strictly proper."

Strip the notation and the idea is remarkable: **the scoring rule is built so that your best expected score comes from stating what you actually believe.**

Not from hedging. Not from being bold to look decisive. Not from being cautious to avoid embarrassment. Honesty is the score-maximising strategy, by construction.

### Why this is the section's most important idea

Because it answers the question a reader will actually have, which is not *how do I compute a score* but *why would I ever commit to a number that can be held against me?*

The answer is that a proper rule removes the incentive to do anything else. The abstract puts the purpose plainly: "In terms of elicitation, the role of scoring rules is to encourage the assessor to make careful assessments and to be honest" (p. 359).

### And improper rules are a real hazard

The article is explicit that this is not a technicality: "Propriety is essential in scientific and operational forecast evaluation; and we present a case study that provides a striking example of the potential issues that result from the use of intuitively appealing but improper scoring rules" (pp. 359–360).

**"Intuitively appealing but improper"** is the phrase for Chapter 6 to carry. Scoring schemes people invent — count how often the most likely outcome happened, penalise being wrong — are frequently improper, and reward distortion.

The chapter should say this and should **not** attempt to teach which rules are proper. That is the article's mathematics and belongs to the depth curriculum.

## 2. Q2–Q3 — Calibration, and how it differs from accuracy and sharpness

### The definitions

`gneiting2007scoring` p. 359:

> "Calibration refers to the statistical consistency between the distributional forecasts and the observations, and is a joint property of the forecasts and the events or values that materialize. Sharpness refers to the concentration of the predictive distributions and is a property of the forecasts only."

Read the two second clauses carefully; they carry the distinction.

**Calibration is a joint property.** It cannot be assessed from the forecasts alone — you need what happened. When you say 70% and it happens about 70% of the time, you are calibrated.

**Sharpness is a property of the forecasts alone.** It is how concentrated your forecasts are — how far from the middle you are willing to go. You can assess it before anything happens.

### The goal, stated by the source

p. 359: "the goal of probabilistic forecasting is to maximize the sharpness of the predictive distributions subject to calibration."

That sentence is worth the whole section. Calibration is the constraint; sharpness is what you maximise subject to it. Not the reverse, and not either alone.

### The consequence Chapter 6 should demonstrate

A forecaster who says 45% every time, on a record where the base rate is 45%, is **perfectly calibrated and entirely useless.**

This follows from the definitions and is the book's own way of putting it — the source does not give this example. It is the sharpest available demonstration that calibration alone is not the goal.

And the converse: a forecaster who says 95% often and is right 60% of the time is sharp and badly calibrated, which is worse than useless because it is confidently misleading.

### Against "calibration is accuracy"

Accuracy is not the source's vocabulary here, and merging it in is how readers lose the distinction. The chapter should avoid the word in this section and use the source's two, which are precise.

## 3. Q4 — Why a single forecast cannot be scored

**Derivable, not sourced, and the chapter should demonstrate it.**

If you said 70% and the thing happened, you were not thereby right. If you said 70% and it did not happen, you were not thereby wrong. A single outcome is consistent with any probability strictly between 0 and 1.

Calibration is defined as consistency between forecasts and observations across a set (p. 359) — a *joint* property, assessed over a record. One pair is not a record.

**The practical consequence, which is the reason this matters:** a forecaster can only be held to account if they make many forecasts and someone keeps score. An organisation that issues one probabilistic statement per drought and never revisits it has built something unfalsifiable — which by Chapter 5's standard establishes nothing.

That connects Chapter 6 to Chapter 5 cleanly: Chapter 5 said a conclusion that could not have come out otherwise establishes nothing; Chapter 6 says the same of a forecast nobody scores.

## 4. Q5 — The Chapter 3 boundary

`canon/terminology.md` registers `calibration` in the instrument sense for Chapter 3 and already carries the warning: **not** to be confused with the Chapter 6 sense, "which is a different concept sharing the word."

The two are genuinely different:

| | Chapter 3 sense | Chapter 6 sense |
|---|---|---|
| What it applies to | an instrument | a forecaster, or a forecasting procedure |
| What it compares | readings against a reference standard | stated probabilities against observed frequencies |
| Assessed from | the instrument and a standard | a record of forecasts **and** outcomes |
| Fixes what | a systematic offset | overconfidence or underconfidence |

**Chapter 6 must reopen the collision explicitly**, exactly as Chapter 5 was required to do with `validation`. This is now the second word Chapter 3 set aside and a later chapter takes up, and the two should be handled the same way: name the collision, say why the word is now available, and move on.

## 5. Brier, and what may be said about it

`gneiting2007scoring` p. 360 records the provenance: "The term *proper* was apparently coined by Winkler and Murphy (1968, p. 754), whereas the general idea dates back at least to Brier (1950) and Good (1952, p. 112)."

**Brier (1950) was not obtained.** It sits behind a publisher paywall and several access routes were attempted.

So Chapter 6 may say that the idea of scoring probability forecasts dates at least to Brier in 1950, **citing p. 360 of this source**, and may not cite Brier directly, attribute wording to it, or describe what it contains.

If the chapter wants to demonstrate a specific score, it should do so as arithmetic the reader can check — squared difference between the stated probability and the outcome, averaged — without attributing that formula to a source not read.

## 6. Cautions — claims the manuscript must NOT make

1. Do not write the notation. `S(P, x)`, `S(P, Q)`, and the propriety inequality belong to the source.
2. Do not teach which rules are proper, or the mathematics of propriety.
3. Do not merge calibration with accuracy.
4. Do not present calibration as the goal. p. 359 makes it the constraint and sharpness the objective.
5. Do not cite Brier directly. Reference it only as reported at p. 360.
6. Do not cite `gneiting2007scoring` beyond p. 360.
7. Do not extend to estimation, cross-validation, or interval scores — the article's second half, and Chapter 8's territory.
8. Do not adopt `calibration` silently after Chapter 3 set it aside.

## 7. Verdict on the stop condition

`research-plan.md` §6 requires propriety and the calibration/sharpness split stated and sourced.

**Met.** Both from p. 359. The "always say 45%" demonstration and the single-forecast argument are derived, not sourced, and are marked as such.

## 8. Unresolved author decisions

1. Is `propriety` named as a term, or is the idea carried as "a scoring rule you cannot game"?
2. Is a specific score demonstrated arithmetically, or is scoring taught only conceptually?
3. Is the "always say 45%" demonstration used? It is the clearest thing available and it slightly caricatures a real practice.
4. How is the Chapter 3 collision reopened — the same way Chapter 5 handled `validation`, or differently?
5. Does the chapter press the point that an unscored forecast is unfalsifiable, given how directly it criticizes normal organisational practice?
