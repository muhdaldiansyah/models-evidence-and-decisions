# Research 04 — Examples, Exercises, and the Chapter 15 Boundary

Status: bounded design dossier. Proposals for author adjudication; **not** author decisions.

Cluster R04 of `research-plan.md` §7. Written after R01–R03, using their vocabulary.

## 1. Anchor selection

### The requirement

`readiness-audit.md` §7: a record set whose **composition** — not whose values — produces a wrong answer, with the composition traceable to identifiable decisions by identifiable actors, and whose real difficulty is not measurement, estimation, or strategic response.

### Recommendation: the water utility, on the Hillcrest demand figure

Chapter 3 closes by handing this over explicitly:

> Hillcrest has no zone meter. That figure was produced by taking the town total and subtracting the zones that **are** metered. So the record exists, it has a number in it, and the number was never measured at all — it is what was left over after measuring somewhere else.

This is the ideal Chapter 4 anchor because **every value involved is correct**. The town total is correctly metered. Each metered zone is correctly metered. The subtraction is correct arithmetic. And the resulting figure is not a demand figure.

### What the residual actually contains

A subtraction residual absorbs everything the metered zones did not capture:

- genuine Hillcrest consumption;
- leakage anywhere in the network, metered zones included;
- under-registration by the metered zones' own meters;
- unbilled operational use — mains flushing, firefighting, tank overflow;
- any error in the town total.

Labelled *Hillcrest demand*, used as *Hillcrest demand*, and it is a bucket for everything nobody measured.

### Why this is the right difficulty

The reader has already used this number twice.

In Chapter 2 it produced the sixteen-hour Hillcrest endurance figure — `0.6 ÷ 0.9` — which drove the aggregation lesson. In Chapter 3 it sat in the role table while the chapter interrogated *adequate*.

So Chapter 4 does not introduce a flaw. It reveals that a number the reader has been reasoning with for two chapters was never what its label said. That is the strongest available demonstration that Chapters 2 and 3 cannot catch this, which is R01 §3's claim.

### What the anchor exposes

| Chapter 4 element | How the anchor exposes it |
|---|---|
| Two processes | Water use versus meter installation and billing |
| Eligibility | Which zones were ever candidates for metering |
| Coverage | Which properties the installed meters reach |
| Capture | Meters that fail and are not replaced |
| Retention | Readings kept for the billing cycle and discarded after |
| Reporting | Monthly totals passed to the regulator in the regulator's categories |
| Missingness related to the value | Meters failing more often under high flow |
| Censoring | A logger that saturates at its maximum |
| Absence | Unbilled operational use, which no meter was ever meant to capture |
| Institutional purpose | The meters exist to **bill customers**, not to model the network |

The last row is the chapter's thesis in one line, and it is true of most datasets anyone will ever be handed.

### Cost

New synthetic facts extending three prior case-data files. All of it **inherits Chapter 1's open SME gate, now three chapters deep**. That accumulation should be stated plainly and is becoming a real risk to record rather than a formality.

## 2. Short contrasts

**C1 — complete is not representative.** A dataset covering every unit of something, which still cannot answer the question, because the units it covers were determined by a process related to the answer. Two paragraphs; no numbers needed.

**C2 — the response rate that told you nothing.** Two datasets, one with a high capture rate and serious bias for the quantity at issue, one with a low capture rate and none. Sourced from `davern2013nonresponse`.

**C3 — the gap you cannot see.** A dataset with no nulls, no flags, and no anomalies, which is missing an entire category of unit. The point is that inspection finds nothing, because there is nothing to find.

### Deliberately not used

- Anything whose difficulty is really measurement (Chapter 3), estimation (Chapter 8), or metric gaming (Chapter 15).
- Medical or clinical trial examples, which pull toward Chapter 7's identification machinery.

## 3. The Chapter 15 boundary

`readiness-audit.md` §3 calls this the chapter's hardest boundary, because Chapter 4's governed core competence names "institutional incentives, and possible manipulation."

### Proposed reader-facing test

> **Chapter 4:** the records were shaped by what the institution needed them for.
> **Chapter 15:** the records changed because people learned they were being used.

Chapter 4 is the recording process **as it is**. Chapter 15 is that process **responding to being used**.

Worked pairs on the anchor:

| Situation | Chapter |
|---|---|
| Meters were installed where billing revenue justified them | **4** — institutional purpose |
| Readings are kept for one billing cycle and then discarded | **4** — retention |
| Categories on the monthly return follow the regulator's form | **4** — reporting |
| Operators begin flushing mains just before the reading date, once they learn the residual is scrutinised | **15** — response to being used |

The fourth is Chapter 15 and should be shown to the reader **as an example of what this chapter is not doing**, so the boundary is concrete rather than announced.

### Caution

The word *manipulation* appears in Chapter 4's governed competence. It must be read as "records can be shaped, including deliberately" — not as an invitation to teach strategic behaviour. The chapter should say plainly that deliberate distortion is one way records get shaped, that it is usually indistinguishable from ordinary institutional purpose when viewed from the dataset, and that the systematic treatment is Chapter 15.

## 4. Cold-transfer forms

### Domain exclusions

Every previously used domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time.

### Proposed forms

**Form A — a city's pothole repair records** (physical/operational).
The dataset is of **reports**, not of potholes. A road with no reports may have no potholes or no residents who report. Eligibility: only roads the authority maintains. Capture: reports arrive by phone and by an app, and the two channels reach different people. Censoring: repairs are logged on completion, so open defects are absent. Retention: reports are closed and archived after ninety days. Institutional purpose: the register exists to schedule crews, not to describe road condition.

**Form B — a food bank's client records** (institutional).
The dataset is of **visits**, not of need. Absence: people who needed help and did not come — transport, hours, stigma, not knowing. Eligibility: a catchment boundary and a referral requirement. Capture: registration requires proof of address, which some cannot produce. Reporting: monthly returns use the funder's categories, which do not match how clients describe their situations. Institutional purpose: the register exists to acquit a grant, not to measure food insecurity.

### Why these are parallel

Both datasets record an **interaction with a system**, not the underlying condition. Both have an eligibility rule, a capture channel that reaches some people and not others, a retention rule, a reporting format imposed from outside, and an institutional purpose that is not the reader's purpose.

Both also contain at least one item that belongs to Chapter 15 and must be recognised as out of scope.

### The Chapter 4 transfer target

> Given an unfamiliar dataset and a question it is being used to answer, describe the process that produced the records separately from the process being asked about, identify one unit or category that could never have appeared, state whether being recorded is related to the quantity at issue, and say why collecting more of the same records would not help.

## 5. Exercise progression

Per `../../decisions/0008`:

1. **Opening attempt** — before any Chapter 4 vocabulary, say what the Hillcrest demand figure is a measurement of.
2. **Worked development** — the residual decomposed, the five stages walked on the anchor.
3. **Self-explanation pauses** — at the two-process split, at the size result, at what cannot be seen.
4. **Faded contrasts** — C1–C3 with reduced prompting.
5. **Error diagnosis** — planted defects.
6. **Cold transfer** — Form A or Form B.
7. **Retrieval** — reconstruct the provenance questions from memory.
8. **Delayed retest** — the other form.

### Planted defects

| Planted defect | Collapse targeted |
|---|---|
| "We have records for 100% of connections, so the dataset is representative" | complete = representative |
| "The gaps are only 2% of rows, so we dropped them" | missing = random; deletion is neutral |
| "This is our most reliable dataset — it has eleven years of readings" | more data = better data |
| "There are no nulls, so the data is clean" | absence in the record = absence in the world |
| "The 94% response rate means bias is negligible" | response rate = bias |

## 6. Open design questions

1. Accept the fourth recurrence of the water case, with SME risk now three chapters deep?
2. Is the 2016 election used as the Meng illustration, or is a neutral case substituted with the source cited for the principle?
3. Is the Chapter 15 example shown to the reader as an out-of-scope contrast, or omitted?
4. Do the transfer forms need SME or ethical review? Form B concerns food insecurity and could carry a careless implication about people who do not seek help.
5. Is `rubin1976missing` cited in manuscript prose, given it is abstract-verified only?

Question 4 is the most pressing. Question 1 is becoming a standing decision the author should settle for the book rather than chapter by chapter.
