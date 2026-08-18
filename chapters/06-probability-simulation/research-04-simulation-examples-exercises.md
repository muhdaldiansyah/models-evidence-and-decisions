# Research 04 — Simulation, Examples, and Exercises

Status: bounded design dossier. Proposals for author adjudication; **not** author decisions.

Cluster R04 of `research-plan.md` §7. Written after R01–R03.

## 1. Q1–Q2 — How to frame simulation, and what more runs fix

### The framing

**Simulation computes the consequences of assumptions. It does not produce evidence about the world.**

That sentence should carry the section. Everything a simulation tells you was implied by what you put into it; the machine only worked out what you could not work out in your head.

Which is a real and considerable service — the Part I storage projection has seven days of uncertain demand interacting with a fixed inflow and a reserve threshold, and nobody can do that by inspection. But it is arithmetic at scale, not observation.

### The result worth teaching

**More runs reduce Monte Carlo error. They do nothing about model error.**

Run the storage projection a thousand times and the spread of results settles down. Run it ten thousand times and it settles further. What does not change is that the demand distribution came from a forecast, that the forecast was conditional on no new action, and that Chapter 4 showed one of its inputs was a subtraction residual.

The simulation will report that with great stability.

### The fourth instance of a shape the reader now knows

| Chapter | More of this improves | And does nothing for |
|---|---|---|
| 3 | measurements → precision | trueness |
| 4 | records → sampling variability | the data-quality term |
| 6 | **simulation runs → Monte Carlo error** | **model error** |

The reader has met this twice. Meeting it a third time in a completely different setting is the point at which it should become a habit rather than a fact — and it gives the chapter a cheap, checkable rule: when told that more of something will fix a problem, ask which term it enters.

Chapter 5's `sensitivity analysis is not criticism` is the same observation from another angle: varying inputs inside a formulation cannot see the formulation.

### Sourcing status, stated carefully

**Nothing in this bibliography sources the simulation material**, and `research-plan.md` §9 requires care here because of the standing rule in `decisions/0012` clause 4.3.

The honest classification:

- **Monte Carlo mechanics** — draw repeatedly from stated distributions, tabulate the results — is **arithmetic**. Teaching it by demonstration is the same as teaching long division by demonstration, and is **not** an instance of the demonstrate-because-unsourced pattern.
- **The claim that more runs do not fix model error** is likewise a mathematical consequence of what a simulation is, demonstrable on the anchor.

So R04 does **not** invoke the disposition that `decisions/0012` puts on notice. It reports that this material needs no source, which is a different thing, and the distinction is recorded rather than assumed.

**One item does not qualify** and should be flagged: any claim about *how practitioners misuse simulation* would be empirical and would need a source. The chapter should therefore make no such claim.

## 2. Q3 — The anchor

**Chapter 5's open items, worked probabilistically.** No new case.

Chapter 5 closed by observing that nearly every unresolved item was now a question about evidence. Chapter 6 takes them in order.

### The centrepiece: Mechanism A versus Mechanism B

Open since Chapter 2, named as unresolved in Chapter 5, with a discriminating observation identified and never made. It is a two-hypothesis problem, which is exactly what the odds form recommended in R01 handles best.

**Prior.** The case supplies the utility's own history: of 11 recorded low-pressure investigations in pumped zones across the network, **7** were pump-capacity limited and **4** were main-related. Prior odds **7:4**, or about **1.75 : 1** for A.

That is a base rate, drawn from the utility's own records, and introducing it here connects R02's material to the arithmetic rather than leaving it as a warning.

**The test.** Run the duty pump at elevated output through a hot afternoon and record pressure at the top of the zone. The case supplies that under Mechanism A a recovery of more than 8 m would be expected with probability **0.85**; under Mechanism B, with probability **0.15**.

**The update.**

| Outcome | Ratio | Posterior odds | Posterior probability |
|---|---|---|---|
| Recovery > 8 m | 0.85 ÷ 0.15 ≈ **5.7** | 1.75 × 5.7 ≈ **9.9 : 1** for A | about **91%** for A |
| No recovery | 0.15 ÷ 0.85 ≈ **0.18** | 1.75 × 0.18 ≈ 0.31 : 1, i.e. **3.2 : 1** for B | about **76%** for B |

**Why this is the right centrepiece.** One afternoon's work moves belief from roughly 2:1 to either 10:1 or 1:3 — decisive in either direction. That is what makes it worth doing, and the reader can now say so with a number rather than a feeling.

And the contrast that follows for free: an observation whose two likelihoods were similar would produce a ratio near 1 and move nothing, however interesting it sounded. That is the bridge to Chapter 11 stated without trespass.

### The base-rate demonstration

A low-pressure complaint arrives from Hillcrest. Before anything else, the base rate says roughly 1.75:1 for pump capacity.

Then a detail arrives: the caller says it has been getting worse since the hot spell began.

That sounds informative. It is consistent with **both** mechanisms — hot weather raises demand, which strains the pump *and* raises flow through the main. Its likelihood ratio is near 1.

This is `tversky1974judgment` p. 1125's finding instantiated on the anchor: worthless evidence arrives, and the temptation is to abandon the base rate rather than to notice that the new information does not discriminate.

### The calibration demonstration

The case supplies the utility's record of probabilistic statements across 40 past heat-event briefings.

| Said | Times | Breached | Observed |
|---:|---:|---:|---:|
| 90% | 10 | 5 | 50% |
| 70% | 10 | 5 | 50% |
| 50% | 10 | 5 | 50% |
| 30% | 10 | 3 | 30% |

Well calibrated at 50% and 30%; badly overconfident at 70% and 90%. That pattern — accurate in the middle, overconfident at the extremes — is realistic and is visible from four rows of arithmetic.

And the sharpness point: the overall base rate is **18/40 = 45%**. A forecaster who said 45% every time would be perfectly calibrated across this record and would have told nobody anything.

### The simulation demonstration

The seven-day storage projection, with a spread on daily demand rather than the point forecast Chapter 1 used.

The payoff is not the output distribution. It is that increasing the run count stabilises the answer while leaving untouched every question Part I raised about where the demand figures came from.

## 3. Q4 — Cold-transfer forms

### Task shape

Back to the Part I shape — the reader produces an analysis rather than reviewing one, because the competence is using probability rather than criticizing its use.

Each form supplies a situation with a stated base rate, a proposed observation with stated likelihoods under two hypotheses, and a short forecasting record to be assessed.

### Domain exclusions

Every previously used domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, blood supply, rental assistance, school air quality, hospital waiting time, pothole records, food bank records, recycling depots, clinic reminders.

### Proposed forms

**Form A — a fleet operator's intermittent vehicle fault** (physical/technical). Two candidate causes with a historical base rate, a diagnostic test with stated detection rates under each, and a record of the workshop's past "likely cause" calls to be assessed for calibration.

**Form B — a housing team deciding whether a rise in reported damp is real** (institutional). Two hypotheses — a genuine increase versus a reporting change following a publicity campaign — with a base rate from past years, a proposed check with stated likelihoods, and a record of the team's past risk statements.

### Why parallel

Both supply: a base rate the reader must actually use; one observation whose likelihood ratio is worth computing; one distractor detail whose ratio is near 1; and a forecasting record with a calibration pattern visible from arithmetic.

Both also require the reader to state what their probability is **conditional on**, which is the chapter's spine and the thing most likely to be dropped.

## 4. Q5 — Stopping confident numbers with no stated conditioning

The characteristic failure of this chapter is a reader producing "about 80%" with nothing attached.

Three design defences:

**Every probability must carry its conditioning information.** A number without it is not an answer. The rubric should score this directly.

**Every update must show the ratio.** Stating a posterior without the ratio hides whether the evidence did any work.

**At least one supplied item must have a ratio near 1**, so that a reader who updates on everything is visibly wrong.

## 5. Exercise progression

Per `../../decisions/0008`:

1. **Opening attempt** — before any Chapter 6 vocabulary, state how likely Mechanism A is and why.
2. **Worked development** — base rate, likelihoods, the odds update.
3. **Self-explanation pauses** — at conditioning, at the worthless-evidence detail, at the always-45% forecaster.
4. **Faded contrasts** — the calibration record, the simulation.
5. **Error diagnosis** — planted defects.
6. **Cold transfer** — Form A or Form B.
7. **Retrieval** — reconstruct the update procedure from memory.
8. **Delayed retest** — the other form.

### Planted defects

| Planted defect | Collapse targeted |
|---|---|
| "There is a 70% chance the pump is the cause" with no conditioning stated | a probability is a property of the event |
| "We said 80% and it happened, so the forecast was good" | a single forecast can be scored |
| "The test was positive, so it is probably A" — inverting the conditional | P(A\|B) = P(B\|A) |
| "We ran 50,000 simulations, so the estimate is reliable" | more runs fix model error |
| "You cannot put a number on a one-off event" | probability requires a frequency |

## 6. Open design questions

1. Accept the sixth recurrence of the water case?
2. Are the Mechanism A/B numbers given as supplied case facts, or must the reader elicit them?
3. Is the calibration table given complete, or must the reader compute the observed column?
4. Is simulation taught with a worked run count, or only conceptually?
5. Do the transfer forms need SME review? Neither domain is sensitive, which is a change from Chapters 4 and 5.

Question 2 matters more than it looks: supplying the likelihoods makes the arithmetic clean and hides the hardest real-world step, which is where those numbers come from. The chapter should supply them **and say that it is doing so**.
