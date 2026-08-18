# Chapter 6 Bounded Research Plan

Status: working research control. No manuscript drafting and no chapter-boundary decision is implied by this file.

Chapter 6: **Probability, Prediction, and Simulation**

**Process note.** As recorded in `readiness-audit.md`, this plan was written alongside its research. Stop conditions are stated as applied.

## 1. Research objective

Produce only the conceptual evidence needed to adjudicate Chapter 6's unique job, terminology, scope boundaries, notation policy, and example architecture.

Do **not** attempt a literature review of probability theory, Bayesian statistics, judgment and decision-making, forecast verification, or Monte Carlo methods.

The research ends when the author can decide:

- what a probability is predicated of, reader-facing;
- how conditioning and updating are taught, and with how much notation;
- what is established about how people handle base rates;
- what makes a scoring rule trustworthy, and how calibration differs from accuracy;
- how simulation is framed, and what more runs do and do not fix;
- where the Chapter 7 and Chapter 8 lines fall.

## 2. Source hierarchy

Chapter 6 differs from Part I: **much of its content is mathematics, not empirical claim.** Bayes' rule does not require a citation any more than long division does.

That distinction governs sourcing here and must be applied honestly rather than used as an excuse.

Priority:

1. primary experimental work where the chapter makes a claim about **what people do**;
2. primary methodological work where the chapter makes a claim about **what a procedure guarantees**;
3. established mathematics, taught by demonstration, cited to nothing;
4. review sources only where they efficiently map competing terminology.

**The dividing line to apply.** A claim that *people neglect base rates* is empirical and needs a source. A claim that *conditioning on B changes the reference set* is mathematical and needs a demonstration. Do not let the second category quietly absorb items belonging to the first.

## 3. Dossier format

As `../02-representation-mechanisms/research-plan.md` §3.

## 4. R01 — What a probability is: conditioning and updating

### Questions

1. What is a probability predicated of — an event, or an event given information?
2. Is the frequency/degree-of-belief distinction taught, sidestepped, or named and set aside?
3. What does conditioning do, and why is "filtering the data" an inadequate account of it?
4. How is Bayes' rule best presented for this reader — formula, odds form, or procedure?
5. How much notation does the chapter need, and does the book's five-chapter no-notation policy survive?

### Deliverable

`research-01-conditioning-and-updating.md`

### Stop condition

Stop when the reader-facing account of what a probability is can be written, and the notation policy settled. Do not research foundations of probability, interpretations debates, or measure theory.

## 5. R02 — Base rates, and what people do with evidence

### Questions

1. What is documented about how people handle prior probabilities when evidence arrives?
2. Is base-rate neglect universal, or conditional on something?
3. What is documented about how people weigh evidence strength against sample size?
4. What may the chapter claim about correcting these tendencies?

### Deliverable

`research-02-base-rates.md`

### Stop condition

Stop when the empirical claims the chapter makes about human judgment are sourced and bounded. Do not research the debiasing literature or the later disputes about heuristics-and-biases.

## 6. R03 — Scoring: propriety, calibration, sharpness

### Questions

1. What makes a scoring rule one you cannot game?
2. What exactly is calibration, and what is it a property of?
3. How does it differ from accuracy, and from sharpness?
4. Why can a single forecast not be scored?
5. What is the boundary to Chapter 3's `calibration`?

### Deliverable

`research-03-scoring-and-calibration.md`

### Stop condition

Stop when propriety and the calibration/sharpness split can be stated and sourced. Do not research scoring-rule mathematics, the continuous ranked probability score, or estimation by optimum score.

## 7. R04 — Simulation, examples, and exercises

R04 begins only after R01–R03 are adjudicated.

### Questions

1. How should simulation be framed at core depth?
2. What do more runs improve, and what do they not?
3. Can Chapter 5's open items carry the chapter's worked examples?
4. What cold-transfer task tests probabilistic reasoning rather than arithmetic?
5. How is the reader stopped from producing confident numbers with no stated conditioning information?

### Deliverable

`research-04-simulation-examples-exercises.md`

## 8. Sequencing

R01 → R02 → R03 → author adjudication → R04 → fill `spec.md` → drafting blueprint.

R01 first because the notation decision governs how everything else can be written.

## 9. Evidence discipline

For every candidate source: verify metadata before promoting a key; create or update `sources/<key>.md` when actually read; record exact support and cautions; do not cite beyond the inspected passage.

**Standing rule.** An automated fetch once returned four fabricated quotations with fabricated page numbers for a source in this bibliography. **Every locator must come from reading the document directly.** A fetch summary is a lead, not evidence.

**Second standing rule**, from `decisions/0012` clause 4.3. Three chapters have now taught a practice by demonstration because no source was obtained, and the rule is that a fifth such case triggers reopening research rather than invoking precedent. Chapter 6 must distinguish carefully between *established mathematics taught by demonstration*, which is legitimate and not an instance of that pattern, and *a practice taught by demonstration because a source proved hard to get*, which is.

## 10. Author-adjudication gates

After R01–R03: what a probability is predicated of; the notation policy; Bayes presentation; the `calibration` collision; empirical claims about judgment and their bounds; core versus deferred scope.

After R04: simulation framing, anchor, exercise sequence, cold-transfer target, and section architecture within 34 pages / 7 hours.

## 11. No-write boundary during bounded research

During each conceptual research cluster, do not modify `spec.md`, `canon/`, `decisions/`, or manuscript files. Research dossiers may be added as working evidence. Governed artifacts change only after explicit author adjudication.
