---
chapter: 7
part: 2
title: "Targets, Identification, and Causal Claims"
status: specified
pages_target: 38
hours_target: 8
---

# Chapter 7: Targets, Identification, and Causal Claims

> **Provisional.** Built on `../../decisions/0014-chapter7-identification-terminology-and-notation.md`, which is **PROPOSED and not author-adjudicated**. The seven Chapter 7 entries in `../../canon/terminology.md`, the two entries it closes from `TODO`, and the updated `estimand`, `intervention`, and `counterfactual` entries are provisional for the same reason. **Decision 0014 clause 2 extends Decision 0013's notation exception, which is itself unadjudicated**; adjudicating this record before 0013 would be incoherent. Title, central question, core competence, and the page and hour targets are **not** provisional — they are governed by `README.md` and `../../decisions/0001`.

## Central question

Could ideal evidence establish the target, and under what assumptions?

## Core competence

Define targets and estimands, distinguish statistical identifiability from causal identification, distinguish prediction from intervention and counterfactual claims, and understand experiments and observational designs as strategies for identification.

## Role in the book

Chapter 7 is where six chapters of forward promises come due. It is the chapter that lets a reader say **no amount of this evidence can answer that question**, and defend it.

Part I taught readers to interrogate an analysis they had been given. Chapter 6 taught them to hold and move a stated uncertainty. Chapter 7 teaches the prior question that all of it depends on: whether the thing being asked is the kind of thing the available evidence could settle at all.

Its spine is taken rather than invented. `pearl2009causal` p. 122 gives four steps — **Define, Assume, Identify, Estimate** — and steps 1–3 are the central question above. Step 4 is Chapter 8.

## Hard prerequisites

- **Chapter 1** — intended use, target, the association/intervention/counterfactual previews, the conditional-on-no-new-action forecast.
- **Chapter 2** — Mechanisms A and B, and the observation that two mechanisms are drawable for the same association.
- **Chapter 4** — selection, and that absence produces no rows to notice. Positivity failure is a Chapter 4 idea in a new setting.
- **Chapter 5** — the assumption record, and that a check which could not have failed establishes nothing.
- **Chapter 6** — conditioning, and its closing statement that conditioning is not intervening. The 91% posterior is this chapter's opening object.

## Soft dependencies / spiral links

- **Chapter 3** — measurement validity is distinct from the validity of causal inference (`adcock2001validity` p. 529, already cited at `03/chapter.md` L406).
- **Chapter 6 §6** — that a property defined over an ensemble cannot be read off a single instance. Balance is that shape again.
- **Chapter 6 §7** — the three-row *more X does not fix B* table. Chapter 7 extends it to four rows and owns the four-row version.

## Established concepts to cover

### Targets and estimands

1. `target quantity` — defined before design, per `pearl2009causal` p. 122.
2. `estimand` — the specified form; five attributes from `fda2021estimands` pp. 9–10, presented as one field's answer.
3. The target-trial protocol components, `hernan2019whatif` p. 37.
4. The alignment between the two lists — **the book's own table**, labelled as such.

### The three levels

5. The demarcation line, `pearl2009causal` p. 99.
6. Association, intervention, counterfactual, worked on the anchor.
7. That the counterfactual question is the hardest and often not identifiable (`pearl2009causal` p. 121).
8. That a good predictor is not a causal lever (`shmueli2010predict`).

### Identification

9. The definition, from both traditions (`pearl2009causal` p. 109; `hernan2019whatif` p. 27).
10. `statistical identifiability` vs `causal identification` vs `structural identifiability`, the third deferred to Chapter 14.
11. `identifying assumption`, and that causal assumptions are untestable in principle (`pearl2009causal` p. 101).
12. That `confounding` is a causal concept and cannot be fixed by statistical method alone (`pearl2009causal` p. 100).
13. That controlling for more covariates can increase bias (`pearl2009causal` p. 117).

### The three conditions

14. `exchangeability`, `positivity`, `consistency` — `hernan2019whatif` p. 26, with the source's "heroic".

### Designs

15. What randomization buys and does not (`deaton2016rct` pp. 9–11).
16. `target trial` and emulation (`hernan2019whatif` pp. 37–38).
17. That observational evidence is not second-rate by nature (`hernan2019whatif` p. 25).

## Terminology to introduce or stabilize

Seven new, two closed from `TODO`, four specialised. See `../../canon/terminology.md`, Chapter 7 block, and `../../decisions/0014` §8.

### Notation

**`do(·)` inside Chapter 6's conditioning bar, and inline arrows for causal structure. Nothing else.** No potential-outcome sub/superscripts, no do-calculus rules, no d-separation vocabulary as machinery, no back-door criterion stated as a criterion. Announced to the reader with its reason at first use, per `../../decisions/0014` clause 2.4.

## Interfaces with other chapters

| Chapter | Line |
|---|---|
| 1 | Informal `target`; this chapter supplies the formal specialization |
| 3 | Measurement validity ≠ validity of causal inference |
| 4 | Selection as an identification threat; absence and positivity |
| 5 | The assumption record must contain identifying assumptions |
| 6 | Conditioning is not intervening; the 91% is the opening object |
| **8** | **`pearl2009causal` p. 117 §3.3.3: from identification to estimation.** Nothing about estimators here |
| 9 | Extending beyond the trial sample "requires further argument" (`deaton2016rct` p. 8) — one sentence |
| 11 | Whether to act, given an identified effect |
| 14 | Structural identifiability, deferred by `README.md` |
| 15 | Intervention that provokes strategic response |

## Scope boundary

### Core

- Defining a target quantity before design.
- The five estimand attributes and the target-trial protocol.
- Association / intervention / counterfactual.
- Identification, in both published definitions, and the three-way name distinction.
- The three identifiability conditions, demonstrated on the anchor.
- What randomization buys.
- Observational designs as target-trial emulation.
- Non-identification as a reportable result.

### Deferred to later chapters

- Estimators, standard errors, intervals, model checking — Chapter 8.
- Transportability, external validity, generalization — Chapter 9.
- Whether to act on an identified effect — Chapter 11.
- Structural identifiability — Chapter 14.
- Strategic response to intervention — Chapter 15.

### Deferred to depth curriculum

- Do-calculus and its rules.
- d-separation, blocking, colliders, the back-door criterion as machinery.
- Instrumental variables.
- Mediation, direct and indirect effects, probabilities of causation.
- Propensity scores, IP weighting, standardization, matching.
- The potential-outcomes / graphs framework debate.

## Section architecture

| § | Title | Pages | Hours |
|---|---|---:|---:|
| 1 | The Question the 91% Cannot Answer | 2 | 0.30 |
| 2 | Define: What Quantity Are You Asking About? | 6 | 1.25 |
| 3 | Three Different Questions About the Same Pipe | 5 | 1.05 |
| 4 | Identification: Could Any Amount of This Evidence Settle It? | 6 | 1.35 |
| 5 | Three Conditions, and How the Anchor Fails Them | 6 | 1.35 |
| 6 | Designs as Strategies for Identification | 6 | 1.35 |
| 7 | What More Data Cannot Do | 4 | 0.75 |
| 8 | Cold-Start Practice and Retrieval | 3 | 0.60 |

**38 pages, 8.00 hours.** The largest chapter in the book, overtaking Chapter 6.

### Drafting constraints

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- **No medical, clinical, or epidemiological example in the body**, per `research-04` §6.
- The World Bank manual quotation is cited **as reported at** `deaton2016rct` p. 10.
- `deaton2016rct` described as a working paper stating it is not peer-reviewed; its strongest claim attributed, not asserted.
- Every causal claim in the manuscript carries the assumption it rests on. The chapter models the discipline it teaches.

## Examples / recurring cases

### The anchor: the seventh recurrence

Chapter 6 left the utility at about 91% for Mechanism A. The next sentence — *so replace the pump* — is this chapter's subject.

`case-data.md` freezes: the fifteen-zone upgrade record with its three contradictory comparisons, the positivity failure by feeder-main age, the four pump options, and the target trial.

### Deliberately not used

- Heart transplants, obesity, or any medical treatment — the sources' own examples.
- Smoking and lung cancer — the standard vehicle, which would import a century of contested history.
- Any example where the naive comparison is merely imprecise rather than backwards.

## Exercise architecture

1. **Opening attempt (§1).** Does the 91% answer the utility's question? Six minutes, preserved unscored.
2. **Five blanks (§2).** Fill the five attributes for the utility's sentence.
3. **Three questions (§3).** Write the association, intervention, and counterfactual versions of one claim.
4. **Two worlds (§4).** Construct two states of the world consistent with the same data and different answers.
5. **Three comparisons (§5).** Compute all three from the four numbers and say what each assumes.
6. **The target trial (§6).** Write the protocol; say why it is infeasible; say what that tells you.
7. **Planted-defect diagnosis (§7).** Five defects.
8. **Cold transfer (§8).** One assigned parallel form.
9. **Retrieval and delayed retest (§8).**

### Planted defects

| Planted defect | Collapse targeted |
|---|---|
| "We controlled for every variable in the dataset, so the estimate is unbiased" | control-for-everything is safe |
| "It was a randomized trial, so the groups were balanced" | randomization balances your trial |
| "We have twelve years of records, so we can settle this" | more data fixes identification |
| "The model predicts pressure drops with 94% accuracy, so we know what causes them" | a good predictor is a causal lever |
| "The effect isn't identified, so there's nothing we can say" | non-identification ends the exercise |

### Rubric dimensions

1. A target quantity stated with its comparison and population.
2. The intervention specified precisely enough to have one effect.
3. Association, intervention, and counterfactual kept apart.
4. At least one identifying assumption named explicitly.
5. A positivity or exchangeability failure found and stated structurally.
6. A target trial written, and its infeasibility used rather than lamented.
7. A verdict that says what would change the answer.

## Transfer target

> Given a claim that an action caused an outcome, a supplied observational record, and a supplied structural fact about how the action was allocated, state the target quantity, name the identifying assumption the claim requires, find the condition that fails and say why it is structural rather than a sample-size problem, and write the target trial that would answer the question.

### Parallel forms

- **Form A — a manufacturer's machine-guarding retrofit and hand injuries** (industrial/physical).
- **Form B — a city's bus lane and journey times** (transport/policy).

Both supply: a vague causal claim; a record permitting at least two contradictory comparisons; an allocation rule that breaks exchangeability; a structural positivity failure; and multiple versions of the intervention.

Every prior transfer and contrast domain is excluded. Neither domain is sensitive.

Chapter 7 must not claim durable far transfer.

## Evidence / source plan

### Load-bearing sources

| Claim | Source |
|---|---|
| The four steps; Define before design | `pearl2009causal` p. 122 |
| Definition of identifiability (structural tradition) | `pearl2009causal` p. 109 |
| Demarcation line; the golden rule | `pearl2009causal` p. 99 |
| Confounding is causal; not fixable by statistics alone | `pearl2009causal` p. 100 |
| Causal assumptions untestable in principle; sample size irrelevant | `pearl2009causal` p. 101 |
| Notation is necessary | `pearl2009causal` p. 100 |
| Back-door intuition (not the criterion) | `pearl2009causal` p. 114 |
| Controlling for everything can increase bias | `pearl2009causal` p. 117 |
| Identification precedes estimation | `pearl2009causal` p. 117 |
| Counterfactual attribution often not identifiable | `pearl2009causal` p. 121 |
| Definition of identifiability (potential-outcome tradition) | `hernan2019whatif` p. 27 |
| The three conditions; "heroic"; hold by design in experiments | `hernan2019whatif` p. 26 |
| Two elements: data and identifiability conditions | `hernan2019whatif` p. 26 |
| Observational evidence is not second-rate | `hernan2019whatif` p. 25 |
| Positivity | `hernan2019whatif` pp. 30–31 |
| Consistency; well-defined interventions | `hernan2019whatif` pp. 31–33 |
| The target trial and its protocol | `hernan2019whatif` pp. 37–38 |
| Estimand attributes | `fda2021estimands` pp. 9–10 |
| Randomization: what it buys | `deaton2016rct` pp. 9–10 |
| The documented overstatement | `deaton2016rct` pp. 10–11 |
| Extending beyond the trial sample | `deaton2016rct` p. 8 |
| A good predictor is not a causal lever | `shmueli2010predict` |
| Measurement validity ≠ causal-inference validity | `adcock2001validity` p. 529 |

### Known gaps constraining the manuscript

1. **Holland (1986) not obtained.** The fundamental problem of causal inference is stated from `hernan2019whatif`; no claim is made about Holland.
2. **The published Deaton and Cartwright not obtained.** Working paper only, pp. 7–11 of 70.
3. **`hernan2019whatif` read at pp. 25–38 only**, in a dated manuscript version whose pagination does not match the printed edition. This is recorded in the source note and must not be lost.
4. **`pearl2009causal` read at pp. 96–122 only**; §§4–6 unread.
5. **The World Bank manual and the other three quoted sources were not obtained.**
6. The reader-facing formulation of identification — *two worlds, same data, different answers* — is **the book's own phrasing of a sourced idea**, and the ICH/target-trial alignment table is **the book's own alignment**. Both are labelled.
7. Rubin (1976) still unobtained, as since Chapter 4.

### Evidence needed before prose is stable

- SME review of the fifteen-zone upgrade record and the feeder-main ages, coupled to Chapter 1's open Gate 1, **now seven chapters deep**.
- Timed reader pilot against the 8-hour target — the largest in the book and the most likely to overrun.
- A second opinion on whether `do(·)` or potential outcomes is the smaller change for this readership. The choice in `decisions/0014` clause 2.5 is argued, not tested.

## Failure modes this chapter should prevent

1. Identification is a data problem.
2. More data helps.
3. Randomization balances the groups.
4. A randomized trial answers your question.
5. "Replace the pump" is a well-defined intervention.
6. The association is the answer with a caveat attached.
7. Confounding is a list of variables to control for.
8. Controlling for more is safer.
9. Not identified means give up.
10. Causal inference requires experiments.
11. Identification is estimation.
12. A good predictor is a causal lever.
13. Difference-in-differences is the answer.

## Open questions

### Before drafting

1. Does the author accept Decision 0014 as proposed, and if not, which clauses change?
2. **Accept the second notation exception — `do(·)` and arrows — given that Decision 0013's first exception is still unadjudicated?**
3. `do(·)` or potential outcomes?
4. Is the four-row *more X* table owned here, and Chapter 6's three-row version left alone?
5. Accept the seventh recurrence of the water case?
6. Is announcing the `consistency` collision the right handling, or should the word be avoided as Chapter 3 avoided `validation`?

### Before declaring Chapter 7 verified or frozen

7. Has Holland (1986) been obtained?
8. Has the published Deaton and Cartwright been obtained, and do pp. 7–11 survive into it unchanged?
9. Has `hernan2019whatif` been re-verified against a current version, or has the book pinned the 2019 manuscript?
10. Have the fifteen-zone record and the feeder-main ages passed SME review?
11. Does the 38-page / 8-hour budget survive a timed reader pilot?
