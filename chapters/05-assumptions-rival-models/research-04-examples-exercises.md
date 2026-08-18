# Research 04 — Examples, Exercises, and the Chapter 8 Boundary

Status: bounded design dossier. Proposals for author adjudication; **not** author decisions.

Cluster R04 of `research-plan.md` §7. Written after R01–R03.

## 1. Q1 — The anchor is the reader's own analysis

**Recommendation: no new case.** Chapter 5 criticizes the artifact Chapters 1–4 jointly produced.

Every other chapter in Part I introduced something. Chapter 5 introduces nothing and turns on what is already there, which is what makes it the closing chapter rather than a fifth topic.

This also solves a problem the earlier chapters had. Their transfer forms needed fresh unfamiliar domains each time; Chapter 5's anchor needs the opposite — maximum familiarity, so that the criticism is about the analysis rather than about learning a case.

## 2. Q2 — The check that catches what four chapters missed

**The order-of-magnitude check on Hillcrest consumption. This is the chapter's centrepiece.**

Two numbers the reader already has, from two different chapters:

- **340** connected properties in Hillcrest (Chapter 3 case data);
- **0.62 ML/day** Hillcrest customer consumption, from the temporary insertion meter (Chapter 4 case data).

Divide them.

`620,000 L ÷ 340 = 1,824 L per property per day`

Now bound a household. Two and a half people at 150 litres each is about **375 L/day**.

**1,824 is roughly five times that.**

Something is wrong, and it took one division and one estimate. No provenance interview, no elevation survey, no metrology.

### What the check does not tell you

It says the numbers are inconsistent. It does not say which is wrong. Three candidates, and the reader should generate them before being told:

- the property count is wrong;
- the 0.62 figure is wrong;
- Hillcrest properties are not households.

### The resolution, and why it matters more than the catch

The case supplies the third. Hillcrest contains a **commercial horticultural nursery** drawing about **0.40 ML/day** on irrigation days.

Take it out: `0.22 ML ÷ 339 properties ≈ 649 L per property per day` — high, and plausible for large-plot hillside properties with gardens during a heatwave.

The arithmetic now reconciles. But that is not the payoff.

**The payoff is that the nursery is one customer, on a commercial contract, whose irrigation is schedulable.**

Four chapters of analysis never saw it. Chapter 1 had one demand number. Chapter 2 had three zone numbers. Chapter 3 asked what *adequate* meant. Chapter 4 asked where the numbers came from. At no point did anything reveal that **65% of Hillcrest's consumption is a single account that could be asked to shift its watering by twelve hours.**

That is an alternative — a cheap, fast, low-cost one — that none of Part I's machinery produced, and it falls out of dividing two numbers.

It also closes the loop on Chapter 2's finding that a representation can only contain the alternatives it can express, and on Chapter 4's that records are shaped by institutional purpose: the billing system knows perfectly well that the nursery is a large account. Nothing that reached the analysis did.

## 3. Q3 — The Chapter 8 boundary

The reader-facing test:

> **Chapter 5:** could this be the wrong model?
> **Chapter 8:** given this model, how uncertain is the answer?

Worked pairs on the anchor:

| Situation | Chapter |
|---|---|
| The residual stays positive when Hillcrest consumption is zero, so it is not a demand | **5** — the formulation is wrong |
| The 0.62 figure is a two-week measurement from three years ago and may be off | **8** — uncertainty in a quantity |
| Mechanism A and Mechanism B are both still alive | **5** — structural uncertainty |
| Varying the friction-loss estimate between 4 m and 8 m to see what changes | **8** — sensitivity within a formulation |

**The fourth is the trap.** Sensitivity analysis feels like criticism and is not: it varies inputs *inside* a formulation and therefore cannot see the formulation. A model that is structurally wrong will produce a beautifully stable sensitivity analysis.

That should be given to the reader as a placement exercise, with the fourth item deliberately included.

## 4. Q4 — Cold-transfer forms

### The problem this chapter's transfer has

Every other chapter's transfer used an unfamiliar domain to test whether a skill survived away from the anchor. Chapter 5's skill is *criticizing an analysis*, which requires an analysis to criticize — and a reader cannot build a four-chapter analysis in forty minutes.

**Proposed solution: supply a short completed analysis and ask the reader to criticize it.** The reader is a reviewer, not an analyst.

This is a different task shape from Chapters 1–4 and it is the right one for this competence.

### Domain exclusions

Every previously used domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records.

### Proposed forms

**Form A — a proposal to close one of a council's four recycling depots** (physical/operational). A one-page analysis is supplied, complete with figures, concluding that closing the western depot saves money with negligible service impact. It contains: an order-of-magnitude error a division would catch; an extreme-condition failure (the model predicts negative queue length at low demand); an unstated assumption that displaced users travel to the next-nearest depot; and a rival explanation for the western depot's low usage that the analysis never considers.

**Form B — a proposal to move a clinic's appointment reminders from post to SMS** (institutional). A one-page analysis concludes the change will cut missed appointments. It contains: a figure that fails a per-patient sanity check; a limiting-case failure (the model implies zero missed appointments at 100% SMS uptake); an unstated assumption that non-attendance is caused by forgetting; and a rival explanation — that the patients who miss appointments are the ones least likely to have a working mobile number — which the analysis never raises and which would reverse its conclusion.

### Why these are parallel

Both supply a **completed, plausible, competently-written analysis** containing exactly four defects, one per Chapter 5 technique: an order-of-magnitude error, an extreme-condition or limiting failure, an unstated load-bearing assumption, and an unconsidered rival explanation.

Both rival explanations are **the reversing kind** — if true, the recommendation flips. That is what makes the task criticism rather than proofreading.

### The Chapter 5 transfer target

> Given a completed analysis and its recommendation, produce a written criticism that names at least one order-of-magnitude or dimensional problem, one behaviour the formulation implies at a limit or extreme that cannot be right, one load-bearing assumption the analysis does not state, and one rival explanation that would reverse the recommendation — and for each, name the observation that would settle it, or say that none is available.

## 5. Q5 — Stopping the reader producing generic worries

The characteristic failure of this chapter is a response consisting of *the data might be biased, the assumptions might not hold, more research is needed* — which is unfalsifiable, applies to every analysis ever written, and costs nothing.

Three design defences:

**Every criticism must name what would settle it.** A worry with no discriminating observation attached is not a criticism. This is `platt1964strong` p. 347 turned into a marking rule.

**Every criticism must be specific enough to be wrong.** "The demand figure may be unreliable" is not; "the demand figure implies 1,800 litres per property per day, which is about five times a plausible household" is.

**At least one criticism must be capable of reversing the recommendation.** Criticism that could not change the decision is, for practical purposes, decoration.

The rubric should score these directly rather than scoring coverage.

## 6. Exercise progression

Per `../../decisions/0008`:

1. **Opening attempt** — before any Chapter 5 vocabulary, list what would have to be true for Part I's conclusion about Hillcrest to be right.
2. **Worked development** — the four cheap checks run on the accumulated analysis, culminating in the nursery.
3. **Self-explanation pauses** — at what makes a check worth doing, at the nursery, at the no-experiment case.
4. **Faded contrasts** — the Chapter 8 placement exercise.
5. **Error diagnosis** — planted defects.
6. **Cold transfer** — Form A or Form B.
7. **Retrieval** — reconstruct the criticism method from memory.
8. **Delayed retest** — the other form.

### Planted defects

| Planted defect | Collapse targeted |
|---|---|
| A review consisting of six generic caveats and no discriminating observation | criticism = skepticism |
| "We listed our assumptions, so they are handled" | naming an assumption handles it |
| "The model reproduces last year's data well, so it is validated" | fit validates the model |
| A sensitivity analysis offered as the criticism section | sensitivity analysis = criticism |
| "All models are wrong, so this objection cannot be settled" | the maxim as abdication |

## 7. Open design questions

1. Accept the fifth and final recurrence of the water case — here as the object of criticism rather than as a case to build?
2. Is the reviewer-not-analyst transfer shape accepted, given it differs from Chapters 1–4?
3. Does the chapter admit that a one-minute limiting check would have flagged Chapter 4's finding? It is the strongest argument for cheap checks and mildly deflating about Part I.
4. Do the transfer forms need SME review? Form B concerns clinic non-attendance and touches on who misses appointments and why.
5. Should the nursery have appeared earlier as a plant, or is discovering it in Chapter 5 the point?

Question 5 matters. Introducing the nursery only in Chapter 5 means Chapters 1–4 contain an unstated omission. That is either the chapter's best demonstration or a retrofit, depending on how it is presented, and it should be presented as what it is: the case was built for four chapters without anyone asking the size question, which is exactly how real analyses go.
