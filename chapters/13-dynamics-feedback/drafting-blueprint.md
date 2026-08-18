# Chapter 13 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0020`, which itself rests on **Accepted** `../../decisions/0007`.

## 1. Drafting objective

28 pages / 5 learning hours that leave the reader able to run a stock forward, find where it turns, say why a trigger fired too late, and tell equilibrium from stability.

The chapter must **defeat** thirteen named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

| § | Title | Words |
|---|---|---:|
| 1 | The Reservoir Does Not Hold Still | 720 |
| 2 | What Carries Forward | 1,440 |
| 3 | Accumulation, and Why It Is Hard | 1,800 |
| 4 | Two Delays, and Their Sum | 1,440 |
| 5 | Closing the Loop | 1,440 |
| 6 | Equilibrium Is Not Stability | 1,440 |
| 7 | Policy Resistance | 1,080 |
| 8 | Cold-Start Practice and Retrieval | 720 |

About **10,080 words**. The shortest chapter since Chapter 9, and deliberately: the material is conceptually dense and arithmetically light, and padding it would turn a demonstration into a survey.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- Bold **only** for case quantities and the first appearance of a controlled term.
- **No new notation.** Arithmetic on a table, and nothing else.
- **No quotation may contain a comparison symbol.** Åström and Murray's formal stability definitions are paraphrased and said to be paraphrased.
- Every trajectory figure the chapter reports appears in `case-data.md`.

### Register discipline

Four failure modes specific to this chapter.

**Sounding like systems-thinking advocacy.** The sources belong to a tradition with a programme. The book uses their descriptive claims about stocks, delays, and feedback, and does not adopt their recommendation of a modelling school. Where a source makes an advocacy claim, say whose claim it is.

**Sounding like the reader is being caught out.** The chapter opens by asking for something `boothsweeney2000bathtub` shows most people get wrong. The register must be *this is hard and here is the measurement*, never *most people fail this*.

**Sounding like the utility was careless.** The rule that overshoots is a written operating instruction that has worked for nine years. It fails because the loop delay is four days and the event lasted seven.

**Sounding like everything is a loop.** `sterman2002models`'s "(almost) nothing is exogenous" is a position, and `../../sources/sterman2002models.md` already records that Chapter 2 must not treat it as a rule. Chapter 13 inherits that restraint.

## 4. Reader-facing sequence

Per `../../decisions/0008`. The case is the water anchor's thirteenth recurrence, run forward.

Self-explanation pauses: exactly three — §3 (why is storage still falling?), §4 (when should the order have been placed?), §6 (is 88 ML an equilibrium?).

## 5. Section 1 — The Reservoir Does Not Hold Still

**Beats.**

1. Pick up Chapter 12's last paragraph directly: the system responds to what you do.
2. Name what Parts I–III assumed. The network sat there and the utility acted on it.
3. **Opening task, about eight minutes, before any vocabulary.** Give the seven days of demand, the standing production of 100, and the starting storage of 220. Ask for the storage on each day, the day of minimum storage, and one sentence on when the utility should have become worried. **Preserve unscored.**
4. Say plainly that the task is a version of an instrument that has been administered to graduate students, and that the results are in §3. Do not say more yet.
5. Name the chapter's position: Chapter 1 taught the reader to ask these questions; this chapter answers them.

## 6. Section 2 — What Carries Forward

**Beats.**

1. Chapter 2's `state`, recalled in one line, not re-taught.
2. **`stock` and `flow`**, from `sterman2006evidence` p. 508, with the four-vocabulary point quoted.
3. **Flows come in pairs.** A stock with only its inflow named has not been analysed.
4. **A stock is not any quantity that changes.** The warehouse temperature guard from `../../decisions/0007`, restated in one paragraph.
5. The case's stock and its two flows, named.
6. **`state space` named once** and not developed, discharging Chapter 2's promise. One sentence.
7. **Reader task.** Name the stock, both flows, and one quantity in the case that varies and is not a stock.

## 7. Section 3 — Accumulation, and Why It Is Hard

**Beats.**

1. Return to the §1 answer. Give the correct trajectory from `case-data.md` §3.
2. **The four facts.** Peak demand day 3; minimum storage day 7; four days apart; critical level crossed on day 5, after demand had already turned.
3. **Self-explanation pause 1.** From day 4 the deficit shrinks every day. Why does storage keep falling?
4. The answer, and the principle: **stocks integrate their net inflows** [@sterman2006evidence, p. 508], quoted in full with its two worked instances.
5. **The named error.** "Most people assume that system inputs and outputs are correlated" — and on this case that means turning storage upward on day 4.
6. **Now the measurement.** `boothsweeney2000bathtub`: 0.77, 0.48, 0.41; "In general, performance is poor"; slope-of-stock 0.66 and area-under-net-rate 0.63 on the simplest task.
7. **The authors' answer to the two dismissals** — elementary calculus that every subject had studied, and "conceptual confusion, not arithmetical error."
8. **Say what kind of claim this is.** Single institution, convenience sample, published 2000. And say that the book uses the study's measurements and none of its threshold verdicts — Chapter 8's discipline applied to the book's own source, which is a first.
9. **Doing nothing does not recover.** Storage sits at 88 forever. "Doing and undoing have fundamentally different time constants" [@sterman2006evidence, p. 507].
10. **Reader task.** Say what would have to happen for storage to return to 220, and how long it would take at a stated surplus.

## 8. Section 4 — Two Delays, and Their Sum

**Beats.**

1. The two delays from `case-data.md` §1, named as the two kinds `../../decisions/0007` distinguishes.
2. **They add.** Four days.
3. The utility's written rule, quoted from `case-data.md` §4.
4. Walk trajectory B. The rule fires on day 6; water arrives on day 8; the trough was day 7.
5. **Self-explanation pause 2.** When would the order have had to be placed?
6. The answer, and the finding: **no rule keyed to storage could have fired in time**, because storage does not fall far enough to trigger it until it is already too late.
7. **The overshoot.** 202 ML of extra production, 30 ML over the weir. Quote the mechanism in full [@sterman2006evidence, p. 508].
8. **The rule is a correct rule.** It is the principle of feedback [@astrom2008feedback, p. 17], applied through a delay.
9. **Worse-before-better** [@sterman2006evidence, p. 507], and that it is indistinguishable in the moment from a failing policy.
10. **Reader task.** Compute what the trough would have been with a one-day verification delay.

## 9. Section 5 — Closing the Loop

**Beats.**

1. **`feedback`, formally** [@astrom2008feedback, p. 1], quoted.
2. **The spine, quoted in full**: causal reasoning about a feedback system "leads to a circular argument", and it is "necessary to resort to formal methods".
3. **Aimed at Chapter 7, once.** Chapter 7 asked what it takes to establish that A causes B. Where feedback is present the question is the wrong shape. **State it once; do not retract Chapter 7.**
4. **`open loop` and `closed loop`** [@astrom2008feedback, p. 2]. Name that Parts I–III were open loop.
5. **`reinforcing` and `balancing`**, with the terminology decision stated to the reader: `positive` is already this book's word, paired with `normative`. Name the standard pair once.
6. **The saturation clause** — a reinforcing loop is not a prediction of unbounded growth.
7. **Balancing does not mean stabilising.** The utility's rule is a balancing loop and it overshot.
8. **The two-sided property** [@astrom2008feedback, p. 3], both halves quoted from one page. **Seventh appearance of the shape**; name it in prose, do not tabulate — Chapter 7 owns that table.
9. **Feedback is reactive** [@astrom2008feedback, p. 22], and feedforward requires good process models. One paragraph: the book has been doing feedforward for twelve chapters.
10. Trajectory C — the flow-keyed rule — introduced here as feedforward's version. **It protects and it spills more.** Neither dominates.
11. **Reader task.** Identify one reinforcing and one balancing loop in the case.

## 10. Section 6 — Equilibrium Is Not Stability

**Beats.**

1. **`equilibrium`** [@astrom2008feedback, p. 100], quoted, including "zero, one or more".
2. **Self-explanation pause 3.** Storage sits at 88 ML from day 8 onward. Is that an equilibrium? Is it a good one?
3. The answer: yes, and no. Equilibrium says nothing about whether you want to be there.
4. **`stability`** [@astrom2008feedback, p. 102], quoted.
5. **The hinge, quoted**: equilibrium is a property of a point; stability is a property of the solutions near it.
6. **Three grades in words** — unstable, neutrally stable, asymptotically stable. Say the source's formal definitions are paraphrased and why.
7. **The inverted pendulum.** `../../decisions/0007`'s standing counterexample, which is also the source's worked example. Note the convergence once.
8. **The 88 ML equilibrium is stable and bad.** The strongest available demonstration that the two ideas come apart.
9. **The collision announced.** `robustness` (Chapter 12) versus `stability` (here). Fifth announcement in the book. State the distinction in two sentences.
10. **`oscillation`** [@astrom2008feedback, p. 24], with the overreaction mechanism quoted. `limit cycle` named once.
11. Sink, source, saddle, centre — named once in a single sentence, not used.

## 11. Section 7 — Policy Resistance

**Beats.**

1. **The definition** [@sterman2002models, p. 504], quoted — the locator Chapter 2 recorded and reserved.
2. **"There are no side effects—just effects"** [@sterman2006evidence, p. 505]. Note in a footnote-style aside that Chapter 2 quoted a different sentence from a different paper for a different purpose.
3. **Two of the source's examples, not ten** — forest fire suppression and flood control [@sterman2006evidence, p. 506], both labelled as the source's.
4. **The book's own instance**: the Hillcrest pressure restoration, from `case-data.md` §8. Two thirds of the water drawn never arrives.
5. The loop drawn in prose, not in a diagram.
6. **The cause** [@sterman2006evidence, p. 507]: we do not understand the full range of feedbacks created by our decisions.
7. **The sentence that keeps the chapter honest** [@sterman2006evidence, p. 510], quoted: structure shaping behaviour "does not relieve us of personal responsibility for our actions."
8. **Simulation returns, bounded.** A trajectory, not a distribution. Carry the pitfall [@sterman2006evidence, p. 512].
9. **Planted-defect diagnosis task.** Five defects per `transfer.md`. One of them is dynamically fine and rhetorically bad. Feedback linked only after production.

## 12. Section 8 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 answer. Compare, do not score. Name the common patterns, including the day-4 turn.
2. **Cold transfer.** Both forms listed, one assigned.
3. **Retrieval from memory** — the procedure, eight steps.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form.
6. Short diagnostic if the transfer went badly.
7. **What this chapter did not give you.**
8. Close: Chapter 14 asks what happens when the decision is not made once but repeatedly, and when the information arrives between the decisions.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production.

## 13. What the draft may not do

- Introduce any notation. Decisions 0013–0019 are where the notation question stands, and this chapter adds nothing.
- Write a differential equation, a transfer function, a state-space form, or a diagram of any kind.
- Teach PID, proportional, or on-off control as controllers. The oscillation *mechanism* on `astrom2008feedback` p. 24 is used; the controller on the same page is not.
- Teach eigenvalues, linearization, Lyapunov functions, phase portraits, or limit-cycle analysis.
- Teach causal loop or stock-and-flow diagramming conventions.
- Quote `astrom2008feedback`'s formal stability definitions, which carry comparison symbols.
- Teach strategic response, gaming, incentives, or performativity.
- Claim a frequency for overshoot in practice.
- Repeat `boothsweeney2000bathtub`'s significance verdicts, or use its gender comparison at all.
- Present the study's finding as a claim about the general population.
- Re-teach Chapter 1's screen or Chapter 5's criticism.
- Re-estimate anything Chapter 7 declared not identified.
- Present the case values as typical, standard, or recommended.
