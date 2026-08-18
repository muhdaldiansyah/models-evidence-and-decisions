# Chapter 7 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 7: **Targets, Identification, and Causal Claims** — the second chapter of Part II.

**Process note.** As in Chapters 3–6, this audit was written alongside its research. Findings taken from sources are marked. Every locator was taken from reading the document directly.

Current architecture from `README.md` and `spec.md`:

- central question: **Could ideal evidence establish the target, and under what assumptions?**
- core competence: **Define targets and estimands, distinguish statistical identifiability from causal identification, distinguish prediction from intervention and counterfactual claims, and understand experiments and observational designs as strategies for identification.**
- target: 38 pages / 8 serious learning hours — **now the largest chapter in the book**, overtaking Chapter 6.
- `README.md` records one deferral in the governed block: **structural identifiability goes to the dynamic-systems part.**

## 1. Readiness verdict

**Drafting-ready after adjudication**, and better supplied with sources than any chapter since Chapter 1.

Three things distinguish it.

**It is the most heavily pre-promised chapter in the book.** Chapters 1, 2, 3, 4, 5, and 6 all defer something here — by name, in their specifications, and in six manuscript sentences that tell the reader Chapter 7 will do this. The debts are itemised in §3. A chapter carrying that much forward promise cannot quietly redefine its scope.

**It has a cited spine.** `pearl2009causal` p. 122 sets out "the four major steps that should be part of every exercise in causal inference": **Define, Assume, Identify, Estimate.** Steps 1–3 are this chapter's central question almost word for word; step 4 is Chapter 8. The chapter does not need a structure of the book's own invention, and per `../../CLAUDE.md` it should not manufacture one.

**Its central concept has two clean published definitions**, from different traditions, that agree. `pearl2009causal` p. 109 Definition 2 and `hernan2019whatif` p. 27 Fine Point 3.1 both say the same thing in different vocabularies: a quantity is identified when the assumptions plus everything observable pin it to one value, and not identified when they leave several values open. Chapter 7's hardest idea arrives sourced twice.

## 2. Unique-job hypothesis

> Teach readers to say what quantity a causal claim is about, and then to ask whether any amount of the available kind of evidence could establish it.

The reader who finishes Chapter 7 should be able to take a sentence like *replacing the pump will stop the pressure drops*, turn it into a stated target with its comparison and population, name what would have to be true for the available data to settle it, and say plainly when the answer is that nothing in the data can.

The last of those is the chapter's real work. Chapters 3–5 taught readers to find defects in an analysis. This chapter teaches a stronger and more uncomfortable verdict: **that some questions are not answerable with the evidence in hand, and no amount of that evidence changes it.**

## 3. What six chapters have already promised

Every entry below is a live debt, located.

| Promised in | Text | Settled by |
|---|---|---|
| `01/chapter.md` L359–360 | "Association alone is not enough … Formal causal identification belongs to Chapter 7." | §§3–4 |
| `01/spec.md` L149, L159–160 | `estimand`, `intervention`, `counterfactual` — "formal home Chapter 7" | §2, §3 |
| `01/spec.md` L227 | targets, estimands, statistical identifiability, causal identification, causal graphs, identification strategies, experiments, observational designs, intervention, counterfactual formalism | §§2–6 |
| `02/chapter.md` L596 | "Chapter 7 is where the machinery for closing that gap lives" | §§4–6 |
| `02/spec.md` L251 | "Two mechanisms are drawable for the same association … Hands off to Chapter 7" | §1, §5 |
| `03/chapter.md` L406 | "Whether a measurement means what you think is Chapter 3. Whether an effect has been identified is Chapter 7." | §4 |
| `04/spec.md` L140 | "selection as an identification threat: Chapter 7" | §5 |
| `06/chapter.md` L409, L1051 | "conditioning is not intervening"; Chapter 7 asks what would have to be true for evidence to establish a causal claim | §1, §3 |

**Five canon entries are waiting with `Definition status: TODO`**: `statistical identifiability`, `causal identification`, plus the Chapter 7 halves of `target`, `estimand`, `intervention`, and `counterfactual`. Closing them is Chapter 7 work and is not optional.

## 4. Neighbouring-chapter boundaries

### Chapter 6 — what precedes

Chapter 6 ends by saying that conditioning cannot answer what would happen under intervention, and that the gap does not close with more data, better priors, or sharper forecasts. Chapter 7 opens on exactly that sentence. The 91% posterior for Mechanism A is the perfect hostile witness: a well-conditioned, correctly computed number that does not answer the question the utility actually wants answered.

### Chapter 8 — estimation

The line is Pearl's own step 4. Chapter 7 stops at *is this quantity identified, and under what assumptions*. Chapter 8 takes an identified quantity and estimates it from finite data. `pearl2009causal` p. 117 §3.3.3 "From identification to estimation" states the order explicitly and is the right thing to cite for the boundary rather than an assertion of the book's own.

**Nothing about estimators, standard errors, intervals, or model checking may appear here.**

### Chapter 11 — decisions

Chapter 7 can say a causal effect is identified and roughly which way it points. It cannot say whether to act, which needs consequences and risk attitude. Same line Chapter 6 drew for expectation.

### Chapter 14 — dynamic systems

`README.md` defers **structural identifiability** there by name. Chapter 7 must name the three-way distinction (statistical / causal / structural) because the canon entries require it, then hand the third away in one paragraph. Naming it is not teaching it.

### Chapter 15 — gaming and strategic response

Deferred from Chapter 4. If an intervention changes the process that generates the data, that is Chapter 15's problem, not this chapter's, and the manuscript must not drift into it.

### Chapter 9 — generalization

The trial-sample-versus-population-of-interest problem is real and `deaton2016rct` p. 8 raises it directly ("any such extension requires further argument"). Chapter 7 should name it once and route it forward. Transportability is not Chapter 7's job.

## 5. Terminology readiness

Nine entries expected, five of which already exist as stubs.

| Term | State | Source position |
|---|---|---|
| `estimand` | stub, "formal home Chapter 7" | `fda2021estimands` pp. 9–10 gives five attributes for a clinical-trial estimand; the source note already forbids presenting it as the book's universal definition |
| `target quantity` | new | `pearl2009causal` p. 122 uses "target quantity" as the thing defined at step 1 |
| `statistical identifiability` | stub, TODO | `pearl2009causal` p. 109 Definition 2 |
| `causal identification` | stub, TODO | `hernan2019whatif` p. 27 Fine Point 3.1; `pearl2009causal` p. 109 |
| `identifying assumption` | new | `hernan2019whatif` p. 27, the term is used verbatim |
| `exchangeability` | new | `hernan2019whatif` pp. 26–27 |
| `positivity` | new | `hernan2019whatif` pp. 26, 30–31 |
| `consistency` (causal sense) | new, **collision** | `hernan2019whatif` pp. 26, 31–33 |
| `target trial` | new | `hernan2019whatif` pp. 37–38 |
| `confounding` | new | `pearl2009causal` p. 114 |

**One collision needs the same handling `calibration` got in Chapter 6.** `consistency` in the causal-inference sense — the observed outcome equals the counterfactual outcome under the treatment actually received — has nothing to do with the statistical sense of a consistent estimator, which Chapter 8 will need. Two fields, one word, and this book will use both. The manuscript must announce it, exactly as Chapter 6 announced `calibration`, and `../../decisions/0014` must record it.

**A second collision is milder but real.** `intervention` in Chapter 15 will mean an action that provokes strategic response. Here it means an action whose effect is the target of inquiry. Same word, compatible senses, no announcement needed — but the canon entry should say so.

## 6. High-risk conceptual collapses to prevent

1. **Identification is a data problem.** It is not. It is a question about whether assumptions plus the observable distribution pin down one answer, and it is settled before any data arrives.
2. **More data helps.** `pearl2009causal` p. 101 is explicit that sensitivity to prior causal assumptions "remains substantial regardless of sample size". Fourth instance of the book's recurring shape, and the first one that arrives cited rather than as the book's own observation.
3. **Randomization balances the groups.** `deaton2016rct` pp. 10–11 shows this is false as usually stated and quotes four published sources getting it wrong. Randomization gives control *in expectation*, not balance in any one trial.
4. **A randomized trial answers your question.** Only if the trial's target is your target. The population, the version of treatment, and the comparison all have to match.
5. **"Replace the pump" is a well-defined intervention.** `hernan2019whatif` pp. 32–33 shows why vague treatments make the causal effect ill-defined. The utility's four pump options are the book's version of the obesity example.
6. **The association is the answer, with a caveat attached.** The chapter must show a case where the naive comparison points the *wrong way*, not merely a case where it is imprecise.
7. **Confounding is a list of variables to control for.** Controlling for the wrong covariate can increase bias; `pearl2009causal` p. 117 says so directly and names the practice of "conditioning on as many pre-treatment measurements as possible" as one to approach with caution.
8. **Not identified means give up.** It means say so, state what would change it, and bound the answer if you can. `pearl2009causal` p. 122 step 4 explicitly includes "approximate it, if it is not".
9. **Causal inference requires experiments.** `hernan2019whatif` p. 25 rejects this in terms the chapter should reuse: "Think of evolution, tectonic plates, global warming, or astrophysics."
10. **Identification is estimation.** The two are separate steps in the source that supplies the spine.

## 7. Research clusters

1. **Targets and estimands** — what has to be specified before a causal question exists.
2. **The three-level distinction** — association, intervention, counterfactual.
3. **Identification** — definitions, the three conditions, and what fails.
4. **Designs** — what randomization buys, what it does not, and observational designs as emulation.

## 8. Candidate example constraints

The water case is available for a **seventh** recurrence and the causal question is already sitting there: Chapter 6 left the utility at about 91% for Mechanism A, and the obvious next sentence — *so replace the pump* — is exactly the inference this chapter exists to interrogate.

Constraints:

- **No medical or clinical examples in the manuscript body.** The two best sources are epidemiological and their examples are heart transplants and obesity. Borrowing those would import Chapter 3's measurement problems and would break the book's habit of working one anchor.
- The observational comparison must run the **wrong way**, so that the naive reading is not merely imprecise but backwards.
- Positivity must fail for a **stateable structural reason**, not because of small numbers.
- The four pump options must be **genuinely different interventions**, so that well-definedness is a real problem rather than a pedantic one.

**Gate 1 remains open and is now seven chapters deep.** This is the same standing risk recorded in every case-data file since Chapter 2 and it is not improving.

## 9. Decisions likely required after research

1. **Notation.** Chapter 6 opened a bounded exception (the conditioning bar, odds). Chapter 7 needs a way to write *intervene* as distinct from *observe*, and probably a way to draw a causal structure. Extending 0013's exception or refusing it is the single largest adjudication.
2. **Which framework.** Potential outcomes, graphs, or both. Teaching both properly does not fit in 38 pages.
3. **The `consistency` collision** — announce, or avoid the word.
4. **How far into confounding** — the back-door criterion is graphical and would import d-separation. Recommend the intuition, cited, without the criterion's machinery.
5. **The seventh water-case recurrence.**

## 10. Drafting gate

Do not draft until:

- `../../decisions/0014` exists in proposed form, with the notation clause settled;
- the nine canon entries are written, including the two that have been sitting at `TODO` since Chapter 1;
- `case-data.md` freezes the pump-upgrade comparison, and every number in it has been computed and checked rather than asserted;
- `spec.md` records the Chapter 8 line in Pearl's own step-4 terms.
