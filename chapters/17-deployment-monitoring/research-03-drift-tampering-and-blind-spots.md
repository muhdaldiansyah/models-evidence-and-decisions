# Research 03: Drift, Tampering, and What Monitoring Cannot See

Cluster 3 of four.

## 1. Drift, from a source already read

`perdomo2020performative` was read at Abstract and §1 for Chapter 15, and is **cited by section** under the arrangement `../../decisions/0022` clause 8 proposed.

Two of its sentences bear directly on monitoring.

> "When ignored, performativity surfaces as undesirable distribution shift, routinely addressed with retraining." [Abstract]

> "Performativity therefore suggests a different perspective on retraining, exposing it as a natural equilibrating dynamic rather than a nuisance." [§1]

**Chapter 15 used these to make a point about relationships breaking. Chapter 17 uses them to make a point about what a monitoring signal means.**

**A monitoring arrangement that detects drift and responds by refitting has not diagnosed anything.** It has observed that the world and the model disagree and has moved the model. Whether that is maintenance or convergence toward somewhere nobody wants is exactly what the signal does not say.

**Nothing new is claimed from this source**, and Chapter 15's cautions stand — not every distribution shift is performative, and the term has no relation to its ordinary English sense.

## 2. Calibration as a standing instrument, from a source already read

`gneiting2007scoring` was read for Chapter 6 and supplies the calibration-and-sharpness framing.

**Chapter 6 used it to score a forecaster against a record. Chapter 17 uses it as a monitoring instrument**, which is the same activity with the record still being written.

**Nothing new is claimed**, and Chapter 6's locators and cautions stand unchanged. The chapter's use is one sentence: a forecast that was calibrated over its first two years and is not calibrated over its third has produced a signal, and calibration is the only instrument in this book that generates one automatically.

## 3. Tampering, for which no source was obtained

`README.md`'s Chapter 17 core competence names "recognize drift and **tampering**".

**No source for the term was obtained.** Deming, its usual attribution, was sought twice and not found.

### What is actually missing

**The mechanism the term names is sourced, and has been since Chapter 13.**

`sterman2006evidence` p. 508, quoted in Chapter 13:

> "decision makers often continue to intervene to correct apparent discrepancies between the desired and actual state of the system even after sufficient corrective actions have been taken to restore equilibrium. The result is overshoot and oscillation"

**Tampering is that mechanism applied to a process that was not in trouble.** Somebody adjusts a stable process in response to ordinary variation, and the adjustment adds variation the process did not have.

**So what is unsourced here is a name, not a claim.** `../../decisions/0024` clause 6 records this and states plainly that it is **not** a new instance of the demonstrate-because-unsourced disposition, which concerns practices taught with nothing behind them.

### And it joins two chapters the book has already written

**Chapter 13** gave the mechanism: correction through a delay produces overshoot.

**Chapter 17 adds the precondition**: if the discrepancy you are correcting is ordinary variation, then every correction is an overshoot, because there was nothing to correct.

**Which makes §2's distinction operational rather than descriptive.** Knowing whether a value is a signal or ordinary variation is what tells you whether to act at all, and acting on the second is how a stable process is made worse by somebody trying to help.

## 4. What monitoring cannot see

**This is the chapter's central claim and it is the book's own.** No source is cited for it, and none is needed, because it follows from what the previous sixteen chapters established.

**Monitoring observes outputs.**

**So it detects failures that change outputs**, and is constitutionally incapable of detecting failures in what the thing was built to represent — because those produce outputs that look exactly right.

| Failure enters at | Example from the book | Would monitoring show it? |
|---|---|---|
| Chapter 1 — the question | The decision was misidentified | **No.** Everything downstream answers the wrong question competently |
| Chapter 3 — what a number stands for | A score named for something it does not measure | **No** |
| Chapter 4 — why the records exist | A label that is a human decision | **No.** Outputs match the label by construction |
| Chapter 7 — identification | A causal claim the evidence cannot support | **No.** Predictions can be fine |
| Chapter 8 — estimation | An interval computed on a moving process | Sometimes, and late |
| Chapter 13 — dynamics | A queue whose inflow exceeds capacity | **Yes.** Waiting times move |
| Chapter 15 — strategic response | Agents responding to the measure | **Yes, if the right ratio is watched** |

**The pattern is that the early stages are invisible to monitoring and the late ones are visible.** That is the reverse of where attention usually goes, and it is why this chapter's diagnosis runs backward through the book rather than forward.

## 5. Diagnosis by stage

**The book's own procedure, and the counterpart of Chapter 16's triage.**

**Chapter 16 routed forward from a problem** — which stages does this need?

**Chapter 17 routes backward from a symptom** — which stage did this enter through?

**The two use the same fifteen categories in opposite directions**, and the manuscript says so once.

**The discipline that makes it more than a checklist:** a failure is diagnosed where it **entered**, not where it was **noticed**. In this chapter's case the symptom appears at Chapter 13 — a queue — and the failure entered at Chapter 4, eighteen months and nine stages earlier.

## 6. What was not researched

- Drift-detection methods: no distribution-shift tests, no change-point detection, no CUSUM, no sequential analysis.
- Machine-learning monitoring, for the reason `README.md` gives about AI in this book.
- Reliability engineering, condition monitoring, maintenance scheduling.
- Governance and assurance frameworks. `fda2023credibility`, `asme2025credibility`, and `nrc2012reliability` were **not re-read**, and Chapter 1's locators stand.
