# Chapter 7 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0014-chapter7-identification-terminology-and-notation.md`.

## 1. Drafting objective

38 pages / 8 learning hours that leave the reader able to state a causal target quantity precisely, name the assumption a claim about it requires, and say — with reasons — when no amount of the available evidence could settle it.

The chapter must **defeat** thirteen named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

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

Roughly 360 words per page — about **13,700 words**. This is the longest chapter in the book; do not rebalance without recording the reason.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- Bold **only** for case quantities and the first appearance of a controlled term.
- **Notation: `do(·)` inside Chapter 6's bar, and inline arrows. Nothing else.**
- **Every causal claim the chapter makes carries the assumption it rests on.** The chapter models the discipline it teaches; a lapse is a defect.
- Attribution is load-bearing in this chapter. Where the book is generalising, say so.

### Register discipline

Two failure modes specific to this chapter.

**Sounding defeatist.** Six pages on what evidence cannot do will leave a reader thinking nothing can be known. §6 and §7 must both end constructively, and §4 must state early that *not identified* is a result rather than a shrug.

**Sounding like a causal-inference course.** The reader was promised no specialist training. The chapter teaches the questions, not the machinery, and every time it declines a piece of machinery it should say where the machinery lives.

## 4. Reader-facing sequence

Per `../../decisions/0008`. No new case; the anchor is Chapter 6's closing sentence.

The spine is `pearl2009causal` p. 122's **Define / Assume / Identify / Estimate**, attributed at the point of use in §2 and referred back to at each transition.

Self-explanation pauses: exactly three — §3 (which question is management asking), §4 (build the two worlds), §5 (why more zones would not help).

## 5. Section 1 — The Question the 91% Cannot Answer

**Beats.**

1. Open on Chapter 6's result: about **91%** for Mechanism A, correctly computed, carrying its conditioning.
2. The utility's next sentence, quoted: *replacing the pump will stop the pressure drops at Hillcrest.*
3. Show the gap in three lines. The 91% is about **which mechanism operates**. The sentence is about **what happens if you act**. Chapter 6 said once that these differ; this chapter is the argument.
4. **Opening task, about six minutes.** Does the 91% support the sentence? If not, what else would you need? Preserve unscored.
5. Name the spine, attributed: four steps from `pearl2009causal` p. 122, of which this chapter is the first three and Chapter 8 is the fourth.
6. Close by saying the chapter's most useful output is sometimes a verdict of *not answerable with this*, and that such a verdict is a finding.

**Do not** introduce identification, conditions, or notation here.

## 6. Section 2 — Define

**Beats.**

1. Step 1 is **Define**, and the source insists it comes before design: defining the target quantity "before specifying the process of treatment selection" [@pearl2009causal, p. 122].
2. Why readers resist: it feels like the question is already clear. Take the utility's sentence and show it is not.
3. **The five attributes** [@fda2021estimands, pp. 9–10]. Present as one field's answer, arrived at under regulatory pressure. Do not present as universal.
4. Run all five at the utility's sentence — five blanks. Table.
5. Fill them, twice, to produce **two different legitimate target quantities** from the same sentence. This is the section's payoff: the sentence was not one question.
6. The `target` → `target quantity` → `estimand` → `estimator`/`estimate` hierarchy, one paragraph, with estimator and estimate routed to Chapter 8.
7. **The target trial protocol** [@hernan2019whatif, p. 37], component list quoted.
8. **The alignment table** — ICH attributes against target-trial components. **Label as the book's own alignment.** Neither source draws it.
9. What the convergence licenses and what it does not.
10. **Reader task.** Fill the five attributes for the utility's sentence, then say which of your choices someone could reasonably disagree with.

## 7. Section 3 — Three Different Questions

**Beats.**

1. The demarcation line, quoted [@pearl2009causal, p. 99].
2. The test the reader can run: could this be written down using only what you observe?
3. The two lists [@pearl2009causal, pp. 99–100]. Point at `confounding` and `randomization` sitting on the causal side.
4. **The three questions about Hillcrest**, worked, each one sentence:
   - association — among zones that were upgraded, what happened;
   - intervention — if we upgrade Hillcrest, what happens;
   - counterfactual — Hillcrest was not upgraded and complaints rose; would they have risen had it been.
5. **Announce the notation**, with the reason quoted [@pearl2009causal, p. 100]. `P(… | do(replace the pump))` against `P(… | the pump was replaced)`. Say `do(·)` was chosen because it is the smaller change and that this is pedagogy, not a verdict on frameworks.
6. The golden rule, quoted [@pearl2009causal, p. 99].
7. **Self-explanation pause 1.** Which of the three is the utility's board actually asking?
8. The answer: usually the third, which is the hardest, and [@pearl2009causal, p. 121] records that attributional queries are generally not identifiable nonparametrically.
9. **The prediction leg**, one paragraph [@shmueli2010predict]. A model that predicts pressure drops well is not thereby a guide to acting on its inputs — which stings, because Chapter 6 just made the reader good at prediction.
10. **Reader task.** Write all three versions of one supplied claim.

## 8. Section 4 — Identification

**Beats.**

1. Frame: step 3, and the chapter's central question.
2. **The definition, from both traditions**, quoted: [@pearl2009causal, p. 109] prose restatement and [@hernan2019whatif, p. 27] Fine Point 3.1.
3. Note that they agree, and that this matters because the traditions disagree publicly about much else. Do **not** claim the frameworks are equivalent.
4. **The book's reader-facing form**, labelled as the book's phrasing: two worlds, same data forever, different answers.
5. **Two consequences, drawn out.** Identification is settled before data arrives. Identification is relative to assumptions — quote "an assumption external to the data, an identifying assumption" [@hernan2019whatif, p. 27].
6. **The sixth instance of the relativity shape.** Adequacy/use, validity/interpretation, trustworthiness/quantity, criticism/stakes, probability/information, identification/assumptions. Prose, not a table — Chapter 5 owns that table.
7. **Self-explanation pause 2.** Build two states of the world for Hillcrest that fit the same twelve years of records and imply different answers.
8. Work the answer on the anchor.
9. **The three-way name distinction.** Statistical identifiability, causal identification, structural identifiability. Third deferred to Chapter 14 in one paragraph.
10. **Confounding is a causal concept** [@pearl2009causal, p. 100], with the short argument reproduced, and the consequence quoted: confounding bias "cannot be detected or corrected by statistical methods alone".
11. **Not identified is a result.** [@pearl2009causal, p. 122] step 4 includes approximating. State the verdict format: what is not identified, which assumption would change it, what to go and get.
12. **Reader task.** Two worlds, written out.

## 9. Section 5 — Three Conditions

**Beats.**

1. Introduce the three from [@hernan2019whatif, p. 26], quoted, with their names.
2. **Carry the source's hedge**: "often heroic". Not a checklist.
3. Quote the thesis: "Causal inference from observational data requires two elements: data and identifiability conditions."
4. **The record** — six upgraded, nine not, four numbers. Table.
5. **The three comparisons**, computed: `+1.5`, `−2.7`, `−2.4`. The first points the wrong way.
6. **Exchangeability**, and why the cross-section is backwards: the six upgraded were the six worst. Note that allocating to the worst cases is ordinary good practice, not a blunder.
7. **Why before-and-after fails too**: the mains renewal programme, visible as the control group's `0.3`.
8. **And why difference-in-differences is not safe**: selection on extremes, regression to the mean, nothing in the table separating it. Defeat collapse 13 here explicitly.
9. **Positivity**, quoted [@hernan2019whatif, p. 30]. Then the feeder-main ages: **68** against a maximum of **40**. Probability zero, not small.
10. **Self-explanation pause 3.** Would another fifty zones fix it? Answer: no, and say precisely why — the failure is structural, and it is Chapter 4's absence lesson in a new setting.
11. **Consistency**, quoted [@hernan2019whatif, pp. 31, 33], with **the naming collision announced** exactly as Chapter 6 announced `calibration`.
12. **The four pump options.** Say plainly that options 2 and 3 could have the opposite sign under Mechanism B.
13. **Reader task.** All three comparisons, and what each assumes.

## 10. Section 6 — Designs

**Beats.**

1. Frame: a design is a way of making an identifying assumption **true** rather than assumed. Quote "in ideal randomized experiments the identifiability conditions hold by design" [@hernan2019whatif, p. 26].
2. **What randomization buys** [@deaton2016rct, p. 10], quoted.
3. **What it does not** [@deaton2016rct, pp. 9–10]: control in expectation, not balance in your trial; "there is nothing in randomization that limits its size".
4. **The documented overstatement**, quoted as reported at [@deaton2016rct, p. 10], with the diagnosis at p. 11 and the sample-size observation.
5. **Connect to Chapter 6 §6.** Balance is a property over hypothetical replications; reading it off one trial is the same category error as scoring one forecast.
6. Describe `deaton2016rct` as a working paper stating it is not peer-reviewed. Attribute "generally inferior to good control" to its authors.
7. **A randomized trial answers the trial's question**, not necessarily yours — population, version of treatment, and comparison must match. Route beyond-sample extension to Chapter 9 in one sentence [@deaton2016rct, p. 8].
8. **Observational evidence is not second-rate** [@hernan2019whatif, p. 25], quoted. Defeat collapse 10 here.
9. **Emulation** [@hernan2019whatif, pp. 26, 37]: "what randomized experiment are you trying to emulate?"
10. **Write the anchor's target trial.** Show it is infeasible for three stated reasons, and that the infeasibility names the assumption the observational analysis carries.
11. **Controlling for everything is not safe** [@pearl2009causal, p. 117], quoted, with the back-door intuition [@pearl2009causal, p. 114] and an explicit statement that the criterion itself is not taught here.
12. Identification precedes estimation, in the source's own terms [@pearl2009causal, p. 117]. Hand to Chapter 8.
13. **Reader task.** Write the target trial; say why it cannot be run; say what that tells you.

## 11. Section 7 — What More Data Cannot Do

**Beats.**

1. Quote the testability asymmetry [@pearl2009causal, p. 101], both sentences.
2. **The fourth instance, four-row table.** Say that the first three were the book's own observation and this one arrives cited. Chapter 7 owns the four-row version; do not edit Chapter 6.
3. Work it on the anchor: what twelve more years of the same records would and would not change.
4. The rule, restated: when told more of something will fix a problem, ask which term it enters.
5. **The two mental barriers** [@pearl2009causal, p. 101], quoted, as the honest account of why this chapter is uncomfortable.
6. **Planted-defect diagnosis task.** Five defects per `spec.md`. Feedback linked only after production.

## 12. Section 8 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 number. Compare, do not score. Name the common patterns.
2. **Cold transfer.** Both forms listed, one assigned, per the standing convention of Chapters 4–6.
3. **Retrieval from memory** before checking — the procedure, ten steps.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form.
6. Short diagnostic if the transfer went badly.
7. **What this chapter did not give you** — the honest-limits passage, per Chapter 6's precedent.
8. Close: Chapter 8 takes an identified quantity and estimates it, and the order is the source's own.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production.

## 13. What the draft may not do

- Use any notation outside `do(·)` and inline arrows.
- State the back-door criterion, d-separation, blocking, or collider concepts as machinery.
- Teach do-calculus, instrumental variables, mediation, or probabilities of causation.
- Teach propensity scores, IP weighting, standardization, or matching.
- Use a medical, clinical, or epidemiological example in the body.
- Cite the World Bank manual or the other quoted sources directly.
- Present `deaton2016rct` as peer-reviewed, or its strongest claim as consensus.
- Present the three identifiability conditions as a checklist.
- Present difference-in-differences as the answer.
- Claim the two frameworks are equivalent.
- Restate Chapter 5's five-row relativity table, or edit Chapter 6's three-row table.
- Teach estimators, standard errors, intervals, or model checking.
- Claim any design is best.
- Recommend an action for the utility.
- Present the ICH attribute list as the book's universal definition of `estimand`.
- Present synthetic case values as typical, standard, or recommended.
