# Chapter 1 Water-Anchor Human SME Review Packet

Status: ready for human drinking-water utility / engineering review; pre-publication gate.

## Purpose of this review

Review the **fictional operating story and wording** of the Chapter 1 municipal water-supply anchor for:

- operational plausibility;
- natural drinking-water utility / engineering wording;
- hidden assumptions that a nonexpert author may have missed;
- accidental unsafe implications;
- wording that could be misread as universal industry practice, regulatory guidance, or municipal law.

This is **not** a request to validate the synthetic numbers as industry averages, design criteria, regulatory thresholds, or recommended operating values.

## Files to review

Primary:

1. `anchor.md` — governed case facts and interpretation boundaries.
2. `case-data.md` — compact synthetic values, arithmetic, reveal order, and prohibited interpretations.
3. `chapter.md`, especially Section 4 — reader-facing worked case.

Supporting only if needed:

- `drafting-blueprint.md`;
- `decision-framing.md`;
- `dynamics-response.md`.

## Frozen synthetic facts

Please do **not** judge these values by whether they are typical of a real utility. They are deliberately synthetic instructional values:

- usable storage capacity: 14.0 ML;
- case reserve: 4.5 ML;
- dashboard storage: 10.8 ML;
- verified storage: 9.9 ML;
- normal treated-water input: 8.4 ML/day;
- permitted temporary treated-water input: 8.8 ML/day;
- production ramp-up: six hours;
- incremental cost: $2,000 per 24 hours;
- independent verification time: 25 minutes;
- demand forecast and +0.4 ML/day stress;
- Utility Director / City Manager authority split;
- six-hour earliest effect for a mandatory restriction request.

The review question is whether the **story built around these supplied values** is coherent and does not imply unsafe or universal practice.

## Pre-SME wording controls already adopted

### 1. Independent level verification

The intended mechanism is:

> an independent local **tank-level check derived from a pressure measurement**, using a different observation path from the remote level transmitter feeding the dashboard.

The case supplies the utility's conversion from measured tank level to usable volume using known tank geometry and calibration. The reader is not asked to perform this engineering conversion or diagnose sensor physics.

The case must **not** imply that an arbitrary distribution-pressure reading directly determines storage volume.

### 2. Temporary production increase

The intended wording is:

> 8.8 ML/day is already a **supplied permitted temporary operating limit** for the fictional event within the utility's treatment, source, water-quality, and pumping constraints.

The case must **not** imply that a director can raise treated-water output independently of treatment performance, water-quality requirements, source limits, pumping limits, permits, or other applicable operating constraints.

### 3. Six-hour production delay

The intended wording is:

> the case stipulates a **six-hour production ramp-up** before the higher permitted output becomes available.

This is a synthetic case-specific action delay. It is not claimed to be a typical utility response time.

The separate six-hour delay for mandatory restriction is a fictional governance/implementation fact and should not be conflated with production ramp-up.

## Five focused reviewer questions

Please answer these directly.

### Q1 — Level-check wording

Does **“independent local tank-level check derived from a pressure measurement”** sound operationally natural and technically defensible for a fictional storage facility when the case also states that the utility has the needed tank geometry/calibration to convert level to usable volume?

If not, please suggest a more natural phrase that preserves the instructional distinction between:

- physical tank state;
- remote transmitter / telemetry record;
- independent observation path.

### Q2 — Independent-path plausibility

Is it credible, at the level required for this introductory case, that a local pressure-derived tank-level check could disagree materially with a remote level transmitter and help identify a transmitter/calibration problem?

Please flag any wording that would make this sound implausible or misleading.

### Q3 — Permitted temporary production wording

Does stating that **8.8 ML/day is already within the supplied treatment, source, water-quality, and pumping limits** adequately prevent the case from implying unsafe or unauthorized production changes?

What additional qualifier, if any, would a utility professional expect?

### Q4 — Six-hour ramp-up

Is a **case-stipulated six-hour production ramp-up** acceptable as a synthetic teaching fact if it is explicitly not presented as typical?

If the number itself creates an implausible mechanism despite being synthetic, explain why and suggest a mechanism-neutral alternative wording. Do not replace the value merely because another value would be more common.

### Q5 — Accidental unsafe or universal implications

Across the case, is there any wording that could reasonably be read to imply that:

- 4.5 ML is a general reserve standard;
- crossing a reserve automatically means immediate pressure loss or service failure;
- SCADA/telemetry is inherently unreliable;
- pressure anywhere in the distribution system directly identifies storage volume;
- treated-water output can be raised without quality/permit/operating constraints;
- voluntary conservation has a known percentage or a known 0.4 ML causal effect;
- the Utility Director / City Manager authority split represents normal municipal law;
- six hours is a typical production or restriction-response delay?

If yes, quote the sentence and suggest the smallest safe repair.

## Reviewer response format

Please use one of these overall dispositions:

- **PASS** — no realism or safety wording changes required;
- **PASS WITH WORDING CHANGES** — mechanism is sound but specific phrases should change;
- **REVISE MECHANISM** — one or more supplied mechanisms create a substantive realism or safety problem.

For each issue, use:

| Location | Current wording / issue | Why it matters | Suggested minimal repair | Severity |
|---|---|---|---|---|
| file / section | quote or summary | operational / safety / interpretation reason | replacement wording | minor / material |

## What the review does not certify

A PASS does **not** certify:

- regulatory compliance for any real utility;
- engineering design adequacy;
- typicality of any synthetic number;
- transferability of the authority structure to another jurisdiction;
- effectiveness of conservation or restriction actions in a real event;
- publication readiness of the chapter as a whole.

It closes only the **human water-utility realism / accidental-unsafe-implication gate** for this fictional instructional case.

## Author action after review

After receiving the review:

1. adjudicate every material comment;
2. update `anchor.md` first if a governed case fact or wording boundary changes;
3. synchronize `case-data.md` and reader-facing `chapter.md`;
4. record any unresolved disagreement explicitly rather than silently choosing a side;
5. rerun the Chapter 1 terminology/reveal-order audit;
6. then proceed to timed reader and cold-transfer pilot work.
