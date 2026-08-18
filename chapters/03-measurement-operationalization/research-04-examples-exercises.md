# Research 04 — Examples, Exercises, and the Chapter 4 Boundary

Status: bounded design dossier. Proposals for author adjudication; **not** author decisions.

Cluster R04 of `research-plan.md` §7. Written after R01–R03, using their vocabulary.

## 1. Anchor selection

### The requirement

`readiness-audit.md` §7 requires a construct that is **not directly readable off an instrument**, that can be operationalized in several defensible ways which **disagree**, with the disagreement mattering to a decision — and that is not really about sampling (Chapter 4), estimation (Chapter 8), or objective-setting (Chapter 10).

### Recommendation: the water utility, on "adequate service pressure"

Chapter 2's role table recorded one row as:

> Zone pressure | what customers experience | observed | per zone, adequate or not

The phrase **"adequate or not"** does enormous unexamined work, and Chapter 2 deliberately left it standing. Chapter 3 opens it.

This satisfies the recurrence condition — a genuinely new operation on a familiar case — and it is the tightest possible spiral: Chapter 2's own artifact contains the placeholder that Chapter 3 fills.

### Why the construct is the right kind

*Adequate service pressure* is not a quantity you can read off a gauge. It requires a chosen formulation, and several are defensible:

| Operationalization | What it measures | Who it favours |
|---|---|---|
| Pressure at the pump station discharge | what the utility produces | the operator; easiest to instrument |
| Pressure at a fixed monitoring point mid-zone | a representative location | whoever chose the location |
| Pressure at the highest connected property | the worst-served customer | the customer at the top of the hill |
| Share of properties above threshold during evening peak | the distribution of service | the analyst, and nobody operationally |

They disagree, all four are defensible, and the choice among them decides whether Hillcrest is recorded as adequately served.

### What the anchor exposes

| Chapter 3 element | How the anchor exposes it |
|---|---|
| Background vs systematized concept | "adequate pressure" as an idea, versus a specific threshold at a specific place at a specific time |
| Operationalization | four procedures, all defensible, from one systematized concept |
| Score | the number the chosen procedure produces |
| Validity | do these scores support the interpretation "Hillcrest is adequately served"? |
| Contextual specificity | a threshold defensible in flat Lowfield may not be in elevated Hillcrest |
| Proxy | tank level standing in for customer pressure |
| Precision vs trueness | a sensor reading to 0.01 bar while sitting 0.15 bar high |
| Reliable but invalid | the pump-station sensor is highly repeatable and measures the wrong location |
| Systematic error not fixed by repetition | Chapter 1's own **10.8 ML** dashboard against **9.9 ML** verified |
| No reference standard | there is a true tank volume; there is no true "adequate" |

The last row is the chapter's structural point from R03 §5, and the anchor delivers both halves of it inside one case: storage has a reference value, adequacy does not.

### Cost

New synthetic facts are required — thresholds, sensor placements, sensor specifications. These extend `../02-representation-mechanisms/case-data.md`, which itself extends Chapter 1's. All of it **inherits Chapter 1's open SME gate**, now two chapters deep. That coupling should be stated plainly in the case-data file and in `spec.md`.

## 2. The Chapter 3 / Chapter 4 boundary, in worked form

The audit calls this the hardest boundary. It needs a form the reader can apply, not a definition.

**Proposed reader-facing test:**

> Chapter 3: *the number is here — does it mean what I think?*
> Chapter 4: *why is this number here, and not another?*

Worked pairs on the anchor:

| Situation | Chapter | Why |
|---|---|---|
| The pump-station sensor reads 0.15 bar high | **3** | the number is off |
| Pressure sensors exist only at pump stations, none in the zones | **4** | which records exist |
| "Adequate" was defined as 20 m of head at the monitoring point | **3** | an operationalization choice |
| The monitoring point was sited where a technician could park | **on the line** | both a procedure choice and a fact about which records come to exist |

**The third row is a genuine boundary case and should be given to the reader as one**, rather than resolved for them. A boundary the reader can place cases against is worth more than a boundary they are told about.

## 3. Short contrasts

Each isolates one distinction.

**C1 — reliable and wrong.** A sensor that returns the same value every time, and that value is wrong. Two sentences. Defeats the reliability-equals-validity collapse without machinery.

**C2 — the same construct, two thresholds.** Two utilities both report "95% of properties adequately served" using different thresholds. The numbers are comparable in appearance and not in meaning. Exposes that a score without its systematized concept is uninterpretable.

**C3 — a proxy with a stated cost.** Tank level as a proxy for customer pressure. Cheap, continuous, already instrumented — and it goes wrong exactly when the feeder main is the constraint rather than the tank, which is the Chapter 2 Mechanism B case. Shows a proxy's failure mode is not random but structured.

### Deliberately not used

- Any anchor turning on sampling, missingness, or non-response — Chapter 4.
- Test scores and educational assessment — the natural psychometric example, deliberately avoided so the chapter does not read as a psychometrics chapter, and because Chapter 1 already used a student-assessment contrast for a different purpose.
- Anything requiring the reader to evaluate whether a target is the right target — Chapter 10.

## 4. Cold-transfer forms

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment (Chapters 1–2), regional blood supply, city rental assistance (Chapter 2).

### Proposed forms

**Form A — indoor air quality in a school** (physical/technical).
The construct is *air adequate for occupancy*. Operationalizations disagree: carbon dioxide at a wall sensor, carbon dioxide averaged across rooms, particulate concentration, ventilation rate per occupant. Sensor placement matters — a unit above a radiator or beside a door reads its own microclimate. Precision-versus-trueness is available: a sensor resolving to 1 ppm while drifted 80 ppm high. A proxy is natural: carbon dioxide standing in for ventilation adequacy generally.

**Form B — hospital emergency department waiting time** (institutional).
The construct is *how long patients wait*, which readers believe is obvious and is not. Operationalizations disagree sharply: arrival to triage, arrival to first clinician contact, arrival to treatment decision, arrival to departure. The clock's start is a choice, and the recorded start is the registration timestamp, which follows physical arrival by an unmeasured interval — a systematic offset that more observations will not remove.

### Why these are parallel

Both require: a background concept distinguished from a chosen systematized concept; at least two operationalizations that disagree, with the disagreement quantified; identification of one systematic offset and a statement of why repetition will not fix it; one proxy with its failure mode named; and one item to be placed on the Chapter 3 / Chapter 4 line.

The last requirement is the same in both forms and is what makes them genuinely parallel rather than merely different.

### The Chapter 3 transfer target

> Given an unfamiliar construct and a decision it must support, produce a defensible operationalization, state what the resulting scores can and cannot be interpreted as, identify one systematic offset that repetition will not remove, and place one supplied item on the line between "the number is wrong" and "the wrong numbers exist".

## 5. Exercise progression

Per `../../decisions/0008`:

1. **Opening attempt** — define "adequate service pressure" precisely enough to measure it, unscaffolded.
2. **Worked development** — the four operationalizations, worked, with their disagreement computed.
3. **Self-explanation pauses** — at the background/systematized split, at precise-but-wrong, at what validity is predicated of.
4. **Faded contrasts** — C1–C3 with reduced prompting.
5. **Error diagnosis** — planted defects.
6. **Cold transfer** — Form A or Form B.
7. **Retrieval** — reconstruct the measurement checklist from memory.
8. **Delayed retest** — the other form.

### Planted defects

Each maps to one collapse from `readiness-audit.md` §5:

| Planted defect | Collapse targeted |
|---|---|
| A report stating the sensor "is validated, so the figure is reliable" | validity is a property of the instrument; reliability = validity |
| A specification quoting accuracy as "±0.4%" | accuracy is a reportable number |
| A proposal to average more dashboard readings to resolve the storage discrepancy | error = noise |
| A definition reading "adequate pressure is what the monitoring point records" | operationalization = definition |
| Two utilities' "95% served" figures compared directly | a score is interpretable without its systematized concept |

## 6. Open design questions

1. Accept the third recurrence of the water case, now two chapters deep in inherited SME risk?
2. Is the boundary case given to the reader unresolved, or resolved for them?
3. Should Form B be replaced, given that waiting-time definitions edge toward Chapter 4?
4. Are four operationalizations too many for a 5-hour chapter — would three carry the lesson?
5. Do the transfer forms need SME review, given that one concerns a hospital and one a school?

Question 1 should be settled first. Question 5 is more pressing here than in Chapter 2, because both proposed domains involve settings where a careless implication could matter.
