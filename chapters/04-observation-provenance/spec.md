---
chapter: 4
part: 1
title: "Observation Processes and Data Provenance"
status: specified
pages_target: 28
hours_target: 5
---

# Chapter 4: Observation Processes and Data Provenance

> **Provisional.** Built on `../../decisions/0011-chapter4-observation-process-terminology-and-boundary.md`, which is **PROPOSED and not author-adjudicated**. The seven Chapter 4 entries in `../../canon/terminology.md` are provisional for the same reason. Rejecting a clause of Decision 0011 invalidates the corresponding sections here. Title, central question, core competence, and the page and hour targets are **not** provisional — they are governed by `README.md` and `../../decisions/0001`.

## Central question

Why did these records, and not others, come to exist in this form?

## Core competence

Describe the observation process separately from the process being modeled, including sampling, selection, missingness, censoring, aggregation, reporting, institutional incentives, and possible manipulation.

## Role in the book

Chapter 3 closed by naming this chapter's problem outright. Hillcrest has no zone meter; its **0.9 ML per day** was produced by subtracting the metered zones from the town total. The record exists, it has a number in it, and the number was never measured.

Chapter 4's unique job:

> Teach readers to treat the process that produced their records as a **second system**, with its own actors, purposes, and failure modes — separate from the process they are trying to model, and requiring its own description.

The chapter must accomplish five things.

1. Establish that a dataset is the output of two processes, and that the second one is invisible from inside the data.
2. Make it concrete where the recording process intervenes, so the reader has somewhere to look rather than a warning to remember.
3. Deliver the chapter's counterintuitive core: more records do not repair a selection problem, and can make confidence worse.
4. Separate three kinds of gap — missing, censored, and never present — and show that the third is both the worst and the only one invisible to inspection.
5. Draw the line to Chapter 15 in a form the reader can apply, since institutional purpose and strategic response look identical from inside a dataset.

Chapter 4 is not a survey-methodology chapter. Most readers' records will be administrative, operational, or incidental — meters, logs, tickets, filings — where no sampling design ever existed, and the chapter must serve those readers first.

The five-stage enumeration (eligibility, coverage, capture, retention, reporting) is **the book's own pedagogical device**; only two stages are sourced. It must be labelled as such per `../../canon/pedagogy.md`.

## Hard prerequisites

- Chapters 1–3. Specifically: a representation containing named quantities (Ch 2), and the habit of asking what a number stands for (Ch 3).
- Arithmetic and percentages. No statistics, no probability, no notation.
- Willingness to accept that a correct number can be useless.
- No domain expertise. All case facts are supplied.

## Soft dependencies / spiral links

| Spiral element | Treatment in Chapter 4 | Later development |
|---|---|---|
| The record is not the target | Completed: the record set's *composition* is itself produced | Chapters 7, 8, 9 |
| Selection | Recognized and described, never modelled | Chapters 7, 8 |
| Missingness | A question to ask, not a taxonomy | Chapter 8 |
| Aggregation | Observation- and reporting-level; Chapter 2 owns representational | Chapters 8, 9 |
| Population coverage | Whether records represent the population asked about, here | Chapter 9 |
| Institutional purpose | Records are shaped by what they were needed for | Chapters 15, 17 |

## Established concepts to cover

### The two processes

- Error decomposition uses "the correlation between X_j and the response/recording indicator R_j" (`meng2018paradox` p. 685) — being recorded is a separate variable from the value.
- Eligibility: `target population` names the units about which inference is intended, distinguished from the status of a sampled unit (`censusndtargetpopulation` §1.1).

### Selection and size

- Three multiplied factors: data quality, data quantity, problem difficulty (`meng2018paradox` p. 685).
- Probabilistic sampling "ensures high data quality by controlling ρ_{R,X} at the level of N^{−1/2}" (insight I).
- "When we lose this control … our estimation error, relative to the benchmarking rate 1/√n, increases with √N" (insight II).
- "bigness" should be measured by relative size f = n/N, not absolute size n (insight III).
- The 2016 CCES result: ρ ≈ −0.005, n ≈ 2,300,000 with the same mean squared error as a random sample of n ≈ 400 (`meng2018paradox` p. 685).
- The Big Data Paradox: "without taking data quality into account … the more the data, the surer we fool ourselves" (`meng2018paradox` p. 686).
- The proposed shift from `Standard Error ∝ σ/√n` to `Relative Bias ∝ ρ√N` (`meng2018paradox` p. 687).

### Nonresponse

- "Response rates lack validity in that there is not even a moderate correlation with nonresponse bias" (`davern2013nonresponse`).
- Bias "is an estimate level measure and it cannot be easily summarized by a survey level proxy measure" (same).

### Missingness

- Whether the missingness process may be ignored depends on why the data are missing, and the stated conditions are "the weakest general conditions under which ignoring the process that causes missing data always leads to correct inferences" (`rubin1976missing`, published summary — **abstract-verified only**).

## Terminology to introduce or stabilize

Seven terms registered provisionally under the Chapter 4 block.

| Term | Treatment | Distinction or caution |
|---|---|---|
| observation process | Required | The process deciding what gets written down; five stages, enumeration is the book's own |
| record | Required | Exists because something caused it to; `provenance` is ordinary language, not registered |
| selection | Required | Operates at every stage, not just sampling; what matters is whether it relates to the value |
| coverage | Required | Complete is not representative; relative size, not absolute |
| nonresponse | Required | Response rate is a poor indicator of bias; bias is per estimate, not per dataset |
| missingness | Required, as a **question** | MCAR/MAR/MNAR **not** attributed to `rubin1976missing` |
| censoring | Recognition depth | Carries partial information; **unsourced**, taught by demonstration |

**Not re-registered:** `aggregation` — its existing entry carries the Chapter 2 / Chapter 4 split; Chapter 4 restates it in prose.

**No notation of any kind.** No identity, no ρ, no N, no formulas.

## Interfaces with other chapters

| Chapter | Interface established here | Boundary Chapter 4 must respect |
|---|---|---|
| Ch. 2 | Observation/reporting aggregation, versus representational | Do not redo boundary, grain, or roles |
| Ch. 3 | **The number is here — does it mean what I think?** versus **why is this number here?** | Every value in the anchor is correct; do not relitigate measurement |
| Ch. 5 | Records can be inadequate for a stated use | Do not import assumption records, verification, or credibility frameworks |
| Ch. 7 | Selection threatens what evidence can establish | Do not define estimands, identifiability, or identification strategies |
| Ch. 8 | Gaps and selection have consequences | Do not teach weighting, imputation, deletion rules, or selection models |
| Ch. 9 | Whether records represent the population asked about **here** | Do not teach transportability or external validity |
| Ch. 10 | — | Do not treat metrics as objectives |
| Ch. 15 | **Shaped by institutional purpose** versus **changed because people learned they were watched** | Teach no strategic behaviour, no Goodhart, no gaming |
| Ch. 17 | A recording process can change over time | Do not teach monitoring design, drift detection, or tampering detection |

## Scope boundary

### Core

- Describe the observation process separately from the process being modelled, in writing.
- Identify who produced a set of records, for what institutional purpose, and under what requirement.
- Walk the five stages on an unfamiliar dataset and say what each decided.
- Recognize that being recorded can depend on the value, and say whether it does for the quantity at issue.
- State why collecting more of the same records would not repair a selection problem.
- Reject a coverage or response rate as evidence of trustworthiness, and say what would be evidence.
- Ask, of any gap: is whatever caused this absence related to what the value would have been?
- Distinguish a missing observation from a censored one, and state the direction of error each mistake introduces.
- Identify one unit or category that could never have appeared in a dataset, and explain why nothing in the data reveals it.
- Distinguish observation-level aggregation from representational aggregation.
- Recognize that a dataset is trustworthy per quantity, not as a whole.
- Place a case on the Chapter 4 / Chapter 15 line.
- Say what question to ask the person who built the dataset.

### Deferred to later chapters

- Assumption records, verification, validation, credibility frameworks: Chapter 5.
- Probability and sampling distributions: Chapter 6.
- Estimands, identifiability, causal identification, selection as an identification threat: Chapter 7.
- Weighting, calibration, post-stratification, imputation, deletion rules, selection models, measurement-error models: Chapter 8.
- Target-population refinement, external validity, generalizability, transportability: Chapter 9.
- Metrics as objectives: Chapter 10.
- Strategic response, incentives, equilibrium, Goodhart-type failure, metric gaming: Chapter 15.
- Monitoring design, drift detection, tampering detection, revision triggers: Chapter 17.

### Deferred to depth curriculum

- Total survey error frameworks and survey design.
- Missing-data theory: ignorability conditions, likelihood and Bayesian treatments.
- Selection models, Heckman-type corrections, and inverse-probability weighting.
- Survival analysis and formal treatment of censoring and truncation.
- Data provenance standards, lineage formalisms, and data-management frameworks.
- Record linkage and entity resolution.
- The data defect index and its derivation.

## Section architecture

One recurring anchor — the water utility, on the Hillcrest demand residual — developed through the concept sections and consolidated in §6. Three short contrasts.

| Section | Working title | Pages | Learning hours | Primary output |
|---|---|---:|---:|---|
| 1 | The Number That Was Never Measured | 2 | 0.25 | An unscaffolded statement of what the 0.9 figure measures, before any Chapter 4 vocabulary |
| 2 | Two Processes | 5 | 0.90 | A written description of the observation process, separate from the modelled process |
| 3 | Where the Recording Process Intervenes | 5 | 0.90 | The five stages walked on the anchor, each with what it decided |
| 4 | Why More Records Do Not Help | 5 | 0.95 | A statement of why more of the same records would not repair the anchor's problem |
| 5 | Gaps, Bounds, and What Is Not There | 5 | 0.85 | Three kinds of gap distinguished, with the direction of error named for each mistake |
| 6 | Reading the Residual | 3 | 0.60 | A worked decomposition of what the 0.9 figure actually contains |
| 7 | Cold-Start Practice and Retrieval | 3 | 0.55 | An independently produced provenance analysis on an unfamiliar dataset |
| **Total** |  | **28** | **5.00** |  |

### Drafting constraints

- The anchor is developed incrementally in §2–§5; §6 is consolidation.
- At least half of active learning time is prediction, production, explanation, diagnosis, or retrieval, per `../../decisions/0008`.
- Three self-explanation pauses: at the two-process split (§2), at the size result (§4), at what cannot be seen (§5).
- **Every value in the anchor must remain correct.** The chapter's force depends on the reader being unable to find an error in any number.
- No notation. No formulas. Numbers appear as numbers with units.
- The Chapter 15 example is shown once, explicitly as out of scope.

## Examples / recurring cases

### Primary anchor: the Hillcrest demand residual

Chapter 3 hands it over. The figure is town total minus metered zones, so it absorbs genuine Hillcrest consumption, leakage anywhere in the network, under-registration by the metered zones' own meters, unbilled operational use, and any error in the town total.

The reader has already used this number twice — in Chapter 2 to compute the sixteen-hour Hillcrest endurance, and in Chapter 3 while interrogating *adequate*. Chapter 4 does not introduce a flaw; it reveals that a number the reader has reasoned with for two chapters was never what its label said.

**The chapter's thesis in one line:** the meters exist to bill customers, not to model the network.

**New synthetic facts required**, extending three prior case-data files. All of it **inherits Chapter 1's open SME gate, now three chapters deep.** This accumulation is a real and growing risk, not a formality.

### Short contrasts

- **C1 — complete is not representative.** A dataset covering every unit that still cannot answer the question.
- **C2 — the response rate that told you nothing.** Sourced from `davern2013nonresponse`.
- **C3 — the gap you cannot see.** No nulls, no flags, no anomalies, and an entire category absent.

### Deliberately not used

Anything whose difficulty is measurement (Ch 3), estimation (Ch 8), or gaming (Ch 15). Medical and clinical-trial examples, which pull toward Chapter 7.

## Exercise architecture

1. **Opening attempt (§1).** What is the 0.9 figure a measurement of? Preserved unscored.
2. **Two-process description (§2).** Write the observation process for the anchor, separately from the water-use process.
3. **Five-stage walk (§3).** For each stage, name what it decided and who decided it.
4. **The size argument (§4).** State why eleven years of the same records would not help.
5. **Gap classification (§5).** Three supplied gaps: classify each and name the direction of error a mistake would introduce.
6. **Planted-defect diagnosis (§6).** Five defects.
7. **Chapter 15 placement (§6).** Four supplied situations; place each.
8. **Cold transfer (§7).** One assigned parallel form.
9. **Retrieval and delayed retest (§7).**

### Planted defects

| Planted defect | Collapse targeted |
|---|---|
| "We have records for 100% of connections, so the dataset is representative" | complete = representative |
| "The gaps are only 2% of rows, so we dropped them" | missing = random; deletion is neutral |
| "Our most reliable dataset — eleven years of readings" | more data = better data |
| "There are no nulls, so the data is clean" | absence in the record = absence in the world |
| "The 94% response rate means bias is negligible" | response rate = bias |

### Rubric dimensions

1. Observation process described separately from the modelled process.
2. Institutional purpose of the records identified.
3. Stages walked, with what each decided.
4. Relationship between being recorded and the value assessed for the quantity at issue.
5. Why more records would not help, stated correctly.
6. Gaps classified, with direction of error named.
7. One unit or category identified that could never have appeared.
8. Chapter 4 / Chapter 15 placement made and defended.

## Transfer target

> Given an unfamiliar dataset and a question it is being used to answer, describe the process that produced the records separately from the process being asked about, identify one unit or category that could never have appeared, state whether being recorded is related to the quantity at issue, and say why collecting more of the same records would not help.

### Parallel forms

- **Form A — a city's pothole repair records** (physical/operational). The dataset is of **reports**, not potholes.
- **Form B — a food bank's client records** (institutional). The dataset is of **visits**, not need.

Both record an interaction with a system rather than the underlying condition. Both carry an eligibility rule, a capture channel reaching some and not others, a retention rule, an externally imposed reporting format, and an institutional purpose that is not the reader's. Both contain one item belonging to Chapter 15.

Every prior transfer and contrast domain is excluded.

Chapter 4 must not claim durable far transfer.

## Evidence / source plan

### Load-bearing sources

| Claim | Source |
|---|---|
| Recording is a separate variable from the value | `meng2018paradox` p. 685 |
| Three multiplied factors; probabilistic sampling controls data quality | `meng2018paradox` p. 685, insights I–III |
| Error grows with population size when control is lost | `meng2018paradox` p. 685, insight II; p. 687 |
| 2016 CCES: 2.3 million behaving like 400 | `meng2018paradox` p. 685 |
| The Big Data Paradox | `meng2018paradox` p. 686 |
| Response rate is a poor indicator of bias | `davern2013nonresponse` |
| Bias is per estimate, not per dataset | `davern2013nonresponse` |
| Ignoring the missingness process depends on why it is missing | `rubin1976missing`, published summary |
| Eligibility and target-population membership | `censusndtargetpopulation` §1.1 |

### Known gaps constraining the manuscript

1. **`rubin1976missing` verified at abstract level only.** One claim, no internal locators. **This is a freeze blocker.**
2. **`meng2018paradox` read to p. 687 only.** No citation beyond it.
3. **Groves (2006) not read.** Reported only via `davern2013nonresponse`.
4. **No source for censoring**, or for three of the five stages. Both taught by demonstration and labelled as the book's own.
5. **Three `davern2013nonresponse` items are paraphrase**, to be re-checked before quotation.

### Evidence needed before prose is stable

- SME review of the metering and billing extension, coupled to Chapter 1's open Gate 1.
- **Ethical review of Form B**, which concerns food insecurity and could carry a careless implication about people who do not seek help.
- Timed reader pilot against the 5-hour target.

## Failure modes this chapter should prevent

From `readiness-audit.md` §5.

1. The observation process is the process being modelled.
2. More data is better data.
3. Missing means random.
4. Response rate measures bias.
5. A dataset is biased or unbiased as a whole.
6. Complete means representative.
7. Provenance is documentation.
8. Selection happens once, at sampling.
9. Censoring is a kind of missingness.
10. Aggregation in records is the same as representational aggregation.
11. Institutional incentive means fraud.
12. Absence in the record means absence in the world.

## Open questions

### Before drafting

1. Does the author accept Decision 0011 as proposed, and if not, which clauses change?
2. Accept the fourth recurrence of the water case, with SME risk three chapters deep? This is becoming a standing book-level decision rather than a chapter one.
3. Is the 2016 election used, or a neutral case substituted with the source cited for the principle?
4. Is `rubin1976missing` cited in manuscript prose given it is abstract-verified only?
5. Is the Chapter 15 example shown, or omitted?

### Before declaring Chapter 4 verified or frozen

6. Has `rubin1976missing` been obtained in full, or the claim recarried by a fully read source?
7. Has `meng2018paradox` been read past p. 687?
8. Has the metering extension passed SME review?
9. Has Form B had ethical review?
10. Does the 28-page / 5-hour budget survive a timed reader pilot?
