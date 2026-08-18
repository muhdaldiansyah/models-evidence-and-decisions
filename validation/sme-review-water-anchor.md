# Cumulative Water-Anchor SME Review Packet

Status: **provisional.** Built on [Decision 0025](../decisions/0025-validation-architecture.md), **PROPOSED and not author-adjudicated**. Ready to send.

This packet closes **Gate 1 for sixteen chapters at once**. It exists because the book's anchor case is one fictional municipal water utility that sixteen chapters extend, and asking a reviewer to read that operating story sixteen times to reach the part that is new would waste most of their attention.

Chapter 1's own packet, [`../chapters/01-decisions-questions/sme-review-water-anchor.md`](../chapters/01-decisions-questions/sme-review-water-anchor.md), is **not superseded**. It is more detailed on the founding facts and it is what Chapter 1's gates are written against. Read it first; this file covers everything built on top of it.

## What you are being asked

Whether the **fictional operating story** is coherent, whether its wording sounds natural to someone who works in drinking water, and whether anything in it could be read as implying unsafe practice, universal industry practice, regulatory guidance, or municipal law.

## What you are explicitly **not** being asked

To validate any number as an industry average, a design criterion, a regulatory threshold, or a recommended operating value. **Every figure in this book is synthetic and instructional.** A number being unusual is not by itself a finding; a number implying an unsafe or impossible mechanism is.

You are also not being asked whether the reasoning the book teaches is correct. That is the author's problem, not yours.

## How much time this needs

The founding facts are about 20 minutes. Each chapter section below is 5–10 minutes. **A useful partial review is welcome** — if you can only review Chapters 1–5, say so and stop there; a partial review with a stated boundary is worth more than a complete one done quickly.

## The founding facts — Chapter 1

Read [`../chapters/01-decisions-questions/anchor.md`](../chapters/01-decisions-questions/anchor.md) and [`../chapters/01-decisions-questions/case-data.md`](../chapters/01-decisions-questions/case-data.md) in full. The five focused questions in Chapter 1's own packet are the ones to answer, and they concern:

- an independent local tank-level check derived from a pressure measurement, disagreeing with a remote level transmitter;
- 8.8 ML/day as a supplied permitted temporary operating limit;
- a six-hour production ramp-up, and a separate six-hour delay for a mandatory restriction;
- whether any wording implies a general reserve standard, inherent SCADA unreliability, or a typical response time.

**Everything below assumes those facts and adds to them.**

---

## What each chapter adds, and what to check

Read the chapter's `case-data.md`. Each ends with a **publication gate** stating the review ask in the author's own words; this table is the index to them.

### Chapter 2 — the network

**Adds:** the distribution network, its zones, and the Hillcrest hilltop zone that loses pressure first.

**Check:** whether the network extension is plausible as a distribution layout, and whether "Hillcrest loses pressure first" is the kind of phenomenon a hilltop zone would actually exhibit.

### Chapter 3 — pressure and elevation

**Adds:** elevations and heads, four competing operationalizations of "pressure", sensor facts, and tank level standing in as a proxy for customer pressure.

**Check:** whether the pressure story is technically defensible, whether the four operationalizations are ones a real utility would recognise as genuinely different, and whether the systematic-offset demonstration is a realistic instrument behaviour.

### Chapter 4 — where the numbers come from

**Adds:** the provenance of the Hillcrest figure, the composition of the residual, a censored observation, and an absence.

**Check — this one wants metering or revenue-management experience.** Whether the residual's composition is realistic, and whether the censoring mechanism described is one that occurs.

### Chapter 5 — the nursery, and the order-of-magnitude check

**Adds:** a commercial nursery, its draw, and household bounding figures — the numbers whose division implies about five times a plausible household's water use.

**Check:** whether the nursery's draw is plausible for such a customer, and whether the household bounding figures are defensible as a sanity check rather than as a norm.

### Chapter 6 — the investigation register

**Adds:** an investigation register, supplied likelihoods for two competing mechanisms, and a forecasting record.

**Check:** whether the register resembles what a utility would actually hold, and whether an afternoon's test could plausibly move belief about a pump the way the case says.

### Chapter 7 — fifteen zones and four pump options

**Adds:** a fifteen-zone upgrade record, an allocation rule, feeder-main ages, and four pump options.

**Check — the manuscript leans hard on this one.** Whether **option 2 could plausibly worsen pressure** under the second mechanism. If it could not, an argument in Chapter 7 fails.

Also: whether it is realistic that no zone with a feeder main older than 40 years had ever been upgraded.

### Chapter 8 — the forecast record

**Adds:** 24 forecast events with errors, and a SCADA changeover part-way through.

**Check:** whether a systematic low bias of the stated size is plausible, and whether a SCADA changeover is a defensible reason to split a record.

### Chapter 9 — five outside sources

**Adds:** five sources bearing on one quantity, of which the largest is the worst, and a terrain-based transport failure.

**Check:** whether **static lift versus friction loss** is a real terrain-dependent distinction of the kind the manuscript relies on. The transport argument fails without it.

### Chapter 10 — the committee paper

**Adds:** a capital committee paper, a stakeholder roster, a capital-envelope convention, and like-for-like procurement practice.

**Check:** whether the paper reads like a real committee paper, and whether **a variable-speed drive would in fact fit an existing pump housing**.

### Chapter 11 — three acts and a payoff table

**Adds:** three candidate acts with costs, and a payoff table that monetises household-events.

**Check:** the monetisation of household-events **carries more of the result than any other number in the book**. If it is indefensible, the chapter's negative result is too.

### Chapter 12 — seven schemes and three futures

**Adds:** seven capital schemes with costs and benefits, three futures without probabilities, and an adaptive plan with signposts.

**Check:** whether a trunk reinforcement can be **usefully staged at roughly half cost**, and whether the three futures are a fair span rather than a straw set.

### Chapter 13 — the reservoir, run forward

**Adds:** a 260 ML reservoir with a 220 ML target and a 120 ML critical level, a seven-day heatwave, a two-day observation delay and a two-day production delay, and spill over a weir.

**Check:** whether the delays are plausible as stipulated facts — the four-day loop delay carries the chapter's whole argument — and whether spilling 30 to 44 ML on late refill is a realistic consequence rather than an artefact.

Also: whether **two thirds of the water drawn to fix Hillcrest never reaching Hillcrest** is a defensible synthetic magnitude for a leaking main under raised pressure.

### Chapter 14 — five summers, and one instrument

**Adds:** four operating rules run across five summers, a night-flow meter at £18,000, and a £380,000 pressure-management scheme whose value depends on a leakage split the records cannot resolve.

**Check — this one wants leakage or network-analysis experience.** Whether night-flow measurement at 03:00 is a recognised method, whether £18,000 is a plausible order of magnitude, and — most importantly — **whether a utility of this size could genuinely lack the instrumentation to tell hot-weather demand from a burst.** If that is a straw man, the chapter's central claim is one too.

### Chapter 15 — the regulator

**Adds:** a second party. A reported low-pressure count that became an incentive in 2019 with £1.8m at stake, nine measurement points moved, and no capital work done.

**Check — this chapter needs a second reviewer with regulatory or price-control experience.** Whether measurement-point selection is in practice delegated to the licensee, and whether a published comparative table with that much at stake is a plausible structure.

**And the single most important question in this packet:** could anything in Chapter 15 be read as describing, alleging, or resembling the conduct of a **real** utility or regulator? The manuscript states that nothing in the case is illegal and that every move was documented and compliant. Please confirm that survives a hostile reading.

### Chapter 17, Case 1 — the plan, operated

**Adds:** four years of operating Chapter 12's adaptive plan. Peak-week demand against forecast, heat events per year, and a capital committee that minuted "signposts reported; no action required" in a year a threshold fired.

**Check:** whether those two indicators are ones a utility would watch, whether heat events are plausibly already counted for a regulator, and whether the committee's behaviour is organisationally realistic.

**And one wording question.** The chapter's position is that **not acting was defensible on the arithmetic, and that nobody in the room could have said so.** It is not a chapter about careless people. Please confirm the text sustains that, and flag any sentence that reads as blame.

---

## Response format

**Overall disposition**, one of:

- **PASS** — no realism or safety wording changes required;
- **PASS WITH WORDING CHANGES** — mechanisms are sound but specific phrases should change;
- **REVISE MECHANISM** — one or more supplied mechanisms create a substantive realism or safety problem.

Per issue:

| Chapter | Location | Current wording / issue | Why it matters | Suggested minimal repair | Severity |
|---|---|---|---|---|---|
| | file / section | quote or summary | operational / safety / interpretation | replacement wording | minor / material |

**If you review only part of the book, state where you stopped.** A bounded review is usable; an unbounded one that quietly thinned out is not.

## What a PASS does not certify

Regulatory compliance for any real utility; engineering design adequacy; typicality of any number; transferability of the authority structure to any jurisdiction; effectiveness of any action in a real event; or publication readiness of any chapter.

It closes only the **human water-utility realism and accidental-unsafe-implication gate** for a fictional instructional case.

## After the review

1. Adjudicate every material comment.
2. Update `../chapters/01-decisions-questions/anchor.md` **first** if a founding fact or wording boundary changes.
3. Synchronise every downstream `case-data.md` — **sixteen files extend this anchor**, and a change to a founding fact propagates through all of them.
4. Record unresolved disagreement explicitly rather than silently choosing a side.
5. Update [gate-status.md](gate-status.md), and only that file, for gate status.
