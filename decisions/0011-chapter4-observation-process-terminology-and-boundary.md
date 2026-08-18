# Decision 0011: Chapter 4 Observation-Process Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `research-plan.md` §10 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 4 entries in `canon/terminology.md` are built on this record and inherit its provisional status. Clauses are numbered so that rejecting one identifies the downstream text it invalidates.

Evidence base: `research-01-two-processes.md`, `research-02-selection-and-size.md`, `research-03-missingness-censoring-absence.md`, `research-04-examples-exercises.md`.

## Decision

Chapter 4 teaches the reader to treat the process that produced their records as a second system with its own logic. Its organizing claim is:

> Your dataset is the output of two processes, not one: the process you are trying to understand, and the separate process that decided which of its facts got written down.

The separation is not this book's framing device. It appears in the statistical literature as a separate variable per unit — `meng2018paradox` p. 685 decomposes error using "the correlation between X_j and the response/recording indicator R_j".

### 1. The two processes

**1.1** The governed chapter title fixes **observation process** as the term. The manuscript introduces it concretely — *the process that decides which things get written down* — rather than abstractly.

**1.2** The reader is taught that **being recorded is something that happens to a unit, and can depend on the unit's value.** This is the chapter's key idea and everything else follows from it.

**1.3** Chapter 4's distinguishing claim against Chapters 2 and 3 is stated explicitly: Chapters 2 and 3 examine what is in front of you; Chapter 4 asks what determined what is in front of you, which no scrutiny of the present data can answer.

### 2. Provenance and stages

**2.1** `provenance` is taught as **the history of how a record came to exist** — who produced it, for what purpose, under what requirement. It is explicitly **not** a metadata field.

**2.2** `provenance` is **not** registered as controlled technical vocabulary. No inspected source defines it as a term of art.

**2.3** Five stages at which the observation process intervenes are taught: **eligibility, coverage, capture, retention, reporting.**

**2.4** Only eligibility (`censusndtargetpopulation` §1.1) and capture (`davern2013nonresponse`; `meng2018paradox`) are sourced. **The five-stage enumeration is the book's own** and must be labelled as such per `canon/pedagogy.md`. It is taught because a reader can verify each stage on the anchor case, not because a framework establishes it.

### 3. Selection and size

**3.1** The chapter's central counterintuitive claim:

> More records do not fix a selection problem. Where being recorded is related to the value, error grows with the size of the population you drew from, rather than shrinking with the number you collected.

Sourced from `meng2018paradox` p. 685, insights (I) and (II), and p. 687's shift from `Standard Error ∝ σ/√n` to `Relative Bias ∝ ρ√N`.

**3.2** The **Big Data Paradox** is quoted and attributed: "without taking data quality into account, population inferences with Big Data are subject to a *Big Data Paradox*: the more the data, the surer we fool ourselves" (`meng2018paradox` p. 686). The conditional clause is **not** dropped.

**3.3** The 2016 CCES result is given **with its numbers** — ρ ≈ −0.005, n ≈ 2,300,000 behaving like n ≈ 400 — because it is empirical, memorable, and exactly quotable. It is attributed to that specific dataset and question and is **not** presented as a general property of large datasets.

**3.4** The three factors — data quality, data quantity, problem difficulty — are described **as three multiplied factors, in words, without notation**. No identity is written. ρ is never presented as a number the reader computes.

**3.5** A high coverage or response rate is **not** evidence of trustworthiness: "Response rates lack validity in that there is not even a moderate correlation with nonresponse bias" (`davern2013nonresponse`). The chapter states clearly that this does not mean nonresponse is harmless.

**3.6** Trustworthiness is **per quantity, not per dataset**: nonresponse bias "is an estimate level measure and it cannot be easily summarized by a survey level proxy measure" (`davern2013nonresponse`). This is the same move Chapter 1 made about adequacy and Chapter 3 about validity.

**3.7** The parallel with Chapter 3 is made **explicit, once**: more measurements improve precision and not trueness; more records shrink sampling variability and not the data-quality term. Each is independently established; the observation that they rhyme is the book's own.

### 4. Missingness, censoring, absence

**4.1** The reader is taught **the question, not the taxonomy**:

> Is whatever caused this to be absent related to what it would have been?

**4.2** **MCAR / MAR / MNAR is not attributed to `rubin1976missing`.** The verified published summary uses *missing at random* and *observed at random* and does not contain the three-way scheme. The three plain-language cases are taught without the acronyms.

**4.3** `rubin1976missing` is **verified at abstract level only**. It may be cited in manuscript prose for one claim and one only — that whether the missingness process may be ignored depends on why the data are missing, and the conditions are restrictive. **No internal locator may be cited.** This is the first abstract-only citation in the book and is recorded as a gap to close before freeze.

**4.4** `censoring` is taught as distinct from missingness — a censored observation carries partial information, a missing one carries none — **by worked arithmetic demonstration on the anchor, not by citation.** No inspected source defines it. This mirrors `decisions/0009` clause 6.3.

**4.5** **Absence** is taught as the worst case and given the chapter's structural weight: a unit that was never eligible produces no row, no null, and no flag. Nothing in the dataset reveals it.

**4.6** The detectability asymmetry is taught: patterns of missingness are visible in the data, their causes are not, and units that never entered are invisible entirely. From which follows the chapter's method — **Chapter 4's work is an interview with whoever built the dataset, not an analysis of it.**

**4.7** Not taught: imputation, deletion rules, weighting, calibration, post-stratification, selection models, survival analysis. Chapter 8.

### 5. The Chapter 15 boundary

**5.1** The reader-facing test:

> **Chapter 4:** the records were shaped by what the institution needed them for.
> **Chapter 15:** the records changed because people learned they were being used.

**5.2** Chapter 4 is the recording process **as it is**; Chapter 15 is that process **responding to being used**.

**5.3** One Chapter 15 example is shown to the reader **as an example of what this chapter is not doing**, so the boundary is concrete rather than announced.

**5.4** The word *manipulation* in Chapter 4's governed competence is read as "records can be shaped, including deliberately". The chapter states that deliberate distortion is one way records get shaped, that from inside a dataset it is usually indistinguishable from ordinary institutional purpose, and that the systematic treatment is Chapter 15. It teaches no strategic behaviour.

### 6. Vocabulary

**6.1** Controlled: `observation process`, `selection`, `coverage`, `missingness`, `censoring`, `nonresponse`, `record`.

**6.2** Ordinary careful language: `provenance`, `eligibility`, `capture`, `retention`, `reporting`, `administrative data`, `sampling frame`, `response rate`.

**6.3** `aggregation` is **not** re-registered. Its existing entry already carries the Chapter 2 / Chapter 4 split; Chapter 4 restates the split from its own side in prose.

**6.4** No notation of any kind. No identity, no ρ, no N, no formulas.

### 7. What Chapter 4 does not do

- Not representation (Chapter 2) — it takes a representation as given.
- Not measurement (Chapter 3) — every value in the anchor is correct.
- Not adequacy criticism or verification (Chapter 5).
- Not estimands or identification (Chapter 7).
- Not weighting, imputation, or correction methods (Chapter 8).
- Not transportability or external validity (Chapter 9).
- Not metrics as objectives (Chapter 10).
- Not strategic response, Goodhart-type failure, or gaming (Chapter 15).
- Not monitoring design, drift detection, or tampering detection (Chapter 17).

## Sources promoted

New and verified: `meng2018paradox` (pp. 685–687 read), `davern2013nonresponse`, `rubin1976missing` (**abstract only**).

Reused: `censusndtargetpopulation` (eligibility and target-population membership only).

## Known gaps carried forward

1. **`rubin1976missing` verified at abstract level only.** One claim, no internal locators, recorded as a freeze blocker.
2. **`meng2018paradox` read to p. 687 only.** The derivations in §2 and the election analysis in §4 were not inspected; the manuscript may not cite beyond p. 687.
3. **Groves (2006) not read.** Cited only as reported by `davern2013nonresponse`.
4. **No source for censoring**, or for the five-stage enumeration beyond two stages. Both are taught by demonstration and labelled as the book's own.
5. **Three items in `davern2013nonresponse` are paraphrase, not verbatim**, and must be re-checked before quotation.

## No architecture change

Title, central question, core competence, 28-page and 5-hour targets are unchanged and remain governed by `README.md` and `decisions/0001`.
