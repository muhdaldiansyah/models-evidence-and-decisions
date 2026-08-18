# Chapter 4 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0011-chapter4-observation-process-terminology-and-boundary.md`.

## 1. Drafting objective

28 pages / 5 learning hours that leave the reader unable to accept a dataset without asking who made it, for what purpose, and what never entered it.

The chapter must **defeat** twelve named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | The Number That Was Never Measured | 2 | 0.25 |
| 2 | Two Processes | 5 | 0.90 |
| 3 | Where the Recording Process Intervenes | 5 | 0.90 |
| 4 | Why More Records Do Not Help | 5 | 0.95 |
| 5 | Gaps, Bounds, and What Is Not There | 5 | 0.85 |
| 6 | Reading the Residual | 3 | 0.60 |
| 7 | Cold-Start Practice and Retrieval | 3 | 0.55 |

Roughly 360 words per page. Do not rebalance without recording the reason.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- Bold **only** for case quantities and the first appearance of a controlled term.
- **No notation whatsoever.** No identity, no ρ, no N, no formulas. Meng's three factors are described in words.
- Citations use Pandoc syntax with locators: `[@key, p. 685]`.
- `meng2018paradox` may be cited **only to p. 687**. `rubin1976missing` carries **one claim and no locator**.
- When the book generalises beyond a source, say so in the sentence that does it.

### Register discipline

Nobody in this case did anything wrong. The prose must not adopt an exposé tone. Every decision described — where meters went, how a gap was filled, what the return form asks for — is ordinary and defensible, and the chapter is weaker, not stronger, if it implies otherwise.

## 4. Reader-facing sequence

Per `../../decisions/0008`. Anchor developed incrementally through §2–§5, consolidated in §6.

Self-explanation pauses: exactly three — §2 (the two-process split), §4 (the size result), §5 (what cannot be seen).

## 5. Section 1 — The Number That Was Never Measured

**Purpose.** Land the handoff and produce an unscaffolded baseline.

**Beats.**

1. Restate what Chapter 3 left: Hillcrest has no zone meter; **0.9 ML/day** is **9.0 − 5.4 − 2.7**.
2. Note that the reader has used this number twice already — Chapter 2's sixteen-hour endurance, Chapter 3's role table.
3. State plainly that every value is correct. The subtraction is right, the three meters are right.
4. **Opening task, about seven minutes.** What is the 0.9 figure a measurement of? List everything it could contain. Preserve unscored.
5. Close on the chapter's question and on why Chapters 2 and 3 cannot reach it: both examine what is in front of you; this one asks what determined what is in front of you.

**Do not** introduce observation process, selection, or any Chapter 4 vocabulary here.

## 6. Section 2 — Two Processes

**Beats.**

1. The claim: a dataset is the output of two processes, not one.
2. **The sourced form.** Error decomposition uses "the correlation between X_j and the response/recording indicator R_j" [@meng2018paradox, p. 685] — for each unit there is the value, and separately whether it got recorded. Two variables from two processes.
3. `observation process` introduced concretely: the process that decides which things get written down.
4. **The key idea, stated early per Decision 0011 clause 1.2:** being recorded is something that happens to a unit, and it can depend on the unit's value.
5. The utility's two processes, written side by side: water moving through a network, and meters being installed, read, filled in, and reported.
6. **The thesis line:** the meters exist to bill customers, not to model the network. Collapse 1 defeated here.
7. `record` and provenance — the history of how a record came to exist. Say explicitly that provenance is not a metadata field. Collapse 7 defeated here.
8. **Self-explanation pause 1.** Chapters 2 and 3 both scrutinised this figure and neither caught it. Why not?
9. **Reader task.** Write the observation process for the anchor, separately from the water-use process.

## 7. Section 3 — Where the Recording Process Intervenes

**Purpose.** Give the reader somewhere to look.

**Beats.**

1. Five stages: **eligibility, coverage, capture, retention, reporting.**
2. **Label the device honestly.** Eligibility is sourced [@censusndtargetpopulation, §1.1]; capture is sourced [@davern2013nonresponse; @meng2018paradox, p. 685]. The five-stage enumeration is the book's own, taught because it can be verified on the case.
3. **Eligibility.** Only connections with a billing account are metered. Firefighting draw and the utility's own operational use have no account.
4. **Coverage.** Meters in Lowfield (1998) and Millbrook (2004), where revenue justified capital. Hillcrest is 10% of demand and never did.
5. **Capture.** The Millbrook meter failed **11 days** last year; filled by carrying forward the previous week's average.
6. **Retention.** 15-minute readings kept **90 days**, then aggregated to daily and the fine data discarded. Tie to Chapter 3: the evening peak becomes unrecoverable.
7. **Reporting.** The monthly return reports **non-revenue water** as one line — leakage, unbilled use, and metering error combined before anyone outside sees them.
8. Restate the Chapter 2 boundary: representational aggregation is a modelling choice made before data exist; this is aggregation done to the records. Collapse 10 defeated here.
9. **Selection is not one event.** It operated at all five stages. Collapse 8 defeated here.
10. **Reader task.** For each stage, name what it decided and who decided it.

## 8. Section 4 — Why More Records Do Not Help

**Purpose.** The chapter's counterintuitive core.

**Beats.**

1. Pose it as the reader would: eleven years of readings, surely that helps?
2. **Three multiplied factors**, in words only [@meng2018paradox, p. 685]: how related being recorded is to the value; how much of the population you have; how variable the quantity is. A product is small only if a factor is small.
3. What a designed random sample actually buys: it *arranges* for the first factor to be near zero — probabilistic sampling "ensures high data quality by controlling ρ_{R,X} at the level of N^{−1/2}" [@meng2018paradox, p. 685].
4. What happens without that arrangement: "our estimation error, relative to the benchmarking rate 1/√n, increases with √N" [@meng2018paradox, p. 685].
5. The practical restatement [@meng2018paradox, p. 687]: attention shifts from a standard error that falls as you collect more, to a relative bias that does not contain the number you collected at all. **Describe; do not write the formulas.**
6. **The 2016 result, with numbers** [@meng2018paradox, p. 685]: ρ ≈ −0.005, and 1% of US eligible voters — about **2,300,000** — carrying the same mean squared error as a genuine random sample of about **400**. Attribute to that dataset and question specifically.
7. **The Big Data Paradox**, quoted with its conditional intact [@meng2018paradox, p. 686]. Collapse 2 defeated here.
8. **Self-explanation pause 2.** The utility has eleven years of these records. What would eleven more years fix?
9. `coverage`: complete is not representative; bigness is relative size, not absolute [@meng2018paradox, p. 685]. Collapse 6 defeated here.
10. `nonresponse`: "Response rates lack validity in that there is not even a moderate correlation with nonresponse bias" [@davern2013nonresponse]. Say clearly this does not mean nonresponse is harmless. Collapse 4 defeated here.
11. Bias is **per estimate, not per dataset** [@davern2013nonresponse]. Collapse 5 defeated here. Note this is the same move as Chapter 1's adequacy and Chapter 3's validity.
12. **The parallel with Chapter 3, once**, labelled as the book's own observation: more measurements improve precision and not trueness; more records shrink sampling variability and not the data-quality term.

## 9. Section 5 — Gaps, Bounds, and What Is Not There

**Beats.**

1. Three kinds of gap, and only one is visible.
2. **Missing.** The question, not the taxonomy: is whatever caused this absence related to what the value would have been? Three plain-language cases; **no acronyms**.
3. `rubin1976missing` cited once, for one claim, no locator: whether the missingness process may be ignored depends on why the data are missing, and the stated conditions are the weakest general ones under which ignoring it always works. State in the sentence that this is an abstract-level citation.
4. **The anchor's gap, worked.** Nine of the eleven Millbrook failure days fell in the two hottest weeks. Filled from a cooler week, so Millbrook is understated, so the residual is **inflated on exactly the hottest days** — the days the drought plan concerns. Collapse 3 defeated here.
5. Note that the fill rule was reasonable, consistent, and documented. It makes the number worst where it is used.
6. **Censored.** The outlet meter maxes at **10.0 ML/day**; three days last summer were recorded as 10.0 when true output was higher. Partial information, not none. Treating it as missing discards information; treating 10.0 as true understates the total. **Both errors run in known directions.** Say plainly that no source is cited for this distinction. Collapse 9 defeated here.
7. **Absent.** Firefighting draw. No meter, no account, no row, no null, no flag. Collapse 12 defeated here.
8. **Self-explanation pause 3.** Which of the three could you find by inspecting the dataset?
9. The detectability table: patterns of missingness visible, causes not, never-present invisible.
10. **The method that follows:** Chapter 4's work is an interview with whoever built the dataset, not an analysis of it.
11. **Reader task.** Three supplied gaps: classify each, name the direction of error a mistake would introduce.

## 10. Section 6 — Reading the Residual

**Beats.**

1. Decompose the **0.90**: consumption 0.62, Hillcrest-zone leakage 0.10, leakage elsewhere 0.08, unbilled operational 0.06, under-registration 0.04.
2. Note the components are themselves estimates.
3. **Redo Chapter 2's arithmetic.** Tank draw is 0.62 + 0.10 = **0.72**; `0.6 ÷ 0.72 ≈ 20 hours`, against Chapter 2's **16**.
4. **State the direction and the luck.** Chapter 2's figure was conservative. Nobody was harmed, nobody noticed, and the conservatism would reverse if the composition shifted. Chapter 2's arithmetic was not an error; it was correct arithmetic on the number available.
5. Institutional purpose, restated: the meters exist to bill customers. Collapse 11 defeated here — nobody behaved badly, and the records are still shaped.
6. **Planted-defect diagnosis task.** Five defects per `spec.md`. Feedback linked only after production.
7. **Chapter 15 placement task.** Four supplied situations, one of which — flushing rescheduled after the reading date once operators learn the residual is watched — belongs to Chapter 15. Show the boundary rather than announcing it.

## 11. Section 7 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 opening list. Compare, do not score. Name the common patterns.
2. **Cold transfer.** Link exactly one assigned form; state that the other must not be opened.
3. **Retrieval from memory** before checking: the provenance questions.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form.
6. Short diagnostic if the transfer went badly, as in Chapters 2 and 3 §7.
7. Close: Chapter 5 asks how this whole formulation could fail, and what would show it.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production. The delayed form is never linked in §7.

## 12. What the draft may not do

- Write any formula or notation.
- Cite `meng2018paradox` beyond p. 687.
- Cite an internal locator in `rubin1976missing`, or attribute MCAR/MAR/MNAR to it.
- Cite Groves (2006) directly.
- Say "big data is bad", or drop Meng's conditional clause.
- Present the 400-equivalent as a general property of large datasets.
- Describe ρ as a bias, a rate, or a percentage.
- Teach weighting, imputation, deletion rules, or selection models.
- Teach strategic response, Goodhart, or gaming.
- Imply that anyone in the case acted carelessly or dishonestly.
- Present the five-stage enumeration as a sourced framework.
- Present synthetic case values as typical, standard, or recommended.
