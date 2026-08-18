# Chapter 15 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0022`, four of whose clauses need author attention.

## 1. Drafting objective

30 pages / 6 learning hours that leave the reader able to date the moment a measure acquired consequences, look for a discontinuity there, name which of four mechanisms is at work, and see a two-party interaction as a game whose stable outcome nobody chose.

The chapter must **defeat** thirteen named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

| § | Title | Words |
|---|---|---:|
| 1 | The Number Fell and Nothing Changed | 1,080 |
| 2 | Thirteen Words, One Claim | 1,080 |
| 3 | Four Ways a Measure Comes Apart | 1,800 |
| 4 | Purpose or Response: a Discriminator | 1,440 |
| 5 | When the Prediction Changes the Target | 1,440 |
| 6 | Two Parties, and an Equilibrium Nobody Wanted | 1,800 |
| 7 | The Vocabulary, and What It Is Missing | 1,440 |
| 8 | Cold-Start Practice and Retrieval | 720 |

About **10,800 words**. The largest chapter in the book after Chapter 8.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- Bold **only** for case quantities and the first appearance of a controlled term.
- **One new notation object**, per `../../decisions/0022` clause 5: a two-by-two payoff table, in §6, once.
- **No quotation may contain a comparison symbol.** Osborne's Nash equilibrium definition is paraphrased and said to be.
- **No quotation from `perdomo2020performative` may contain an `fi`.**
- **`perdomo2020performative` is cited by section, never by page.**
- Every figure the chapter reports appears in `case-data.md`.

### Register discipline

Five failure modes specific to this chapter, and the first is the most dangerous the book has faced.

**Sounding like an exposé.** Everything the utility did was legal, documented, and compliant. A chapter that reads as indignation teaches the reader to look for villains, which is the exact failure §3 exists to prevent — three of the four mechanisms need no villain at all.

**Sounding like the regulator was foolish.** The regulator wanted service to improve and attached a consequence to the best available measure of it. That is what a regulator should do, and it did not work.

**Sounding cynical about measurement.** Goodhart's law does not say metrics are useless. It says a regularity collapses under pressure, and `manheim2019goodhart` p. 1 says the effect scales with the pressure — which is a diagnostic, not a counsel of despair.

**Sounding like game theory.** One table, four cells, one section. No payoff functions, no solution concepts, no notation beyond the table.

**Sounding certain about the discriminator.** It fails safely in one direction only, and §4 must say so where the reader will not miss it.

## 4. Reader-facing sequence

Per `../../decisions/0008`. Three pauses: §1 (what happened?), §4 (which is it?), §6 (what should the regulator do?).

## 5. Section 1 — The Number Fell and Nothing Changed

**Beats.**

1. Pick up Chapter 14's last paragraph directly.
2. **Opening task, about ten minutes, before any vocabulary and without the words strategy, metric, incentive, or gaming.** Give the seven-year series from `case-data.md` §2 and the single fact that no capital work was done. Ask: what happened, and what would you need to know to be sure? **Preserve unscored.**
3. **Self-explanation pause 1** is the task itself; do not add a second prompt.
4. Give the pre/post comparison — 37.9% down, 1.7% up — and stop there. **Do not reveal the mechanism in §1.**
5. Name what the chapter is for: every chapter so far has assumed the thing being measured does not know it is being measured.
6. Close on the Chapter 3 connection, stated and not developed: Chapter 3 found a zone recorded as adequately served because of where an instrument happened to be. **Happened to be** is the phrase this chapter will take apart.

## 6. Section 2 — Thirteen Words, One Claim

**Beats.**

1. State plainly that the book's own architecture names thirteen things here, and list them.
2. **Say that they are one claim and a vocabulary**, per `../../decisions/0022` clause 1, and give the claim.
3. Map the seven that are the claim; name the six that are the vocabulary and say they arrive in §7.
4. **This is unusual and the manuscript should say why it is being done**: a reader checking the chapter against the book's architecture should be able to see that nothing was dropped.
5. Distinguish the chapter from Chapter 13 once: policy resistance needs no agent who knows the policy exists; a reservoir resists by physics.
6. **Reader task.** Before §3, write down which of the thirteen you would expect the water case to illustrate.

## 7. Section 3 — Four Ways a Measure Comes Apart

**Beats.**

1. **Goodhart's law**, quoted **as reported at** [@manheim2019goodhart, p. 1 n.1], with the provenance stated in the sentence that introduces it: the original could not be obtained.
2. **The definition** [@manheim2019goodhart, p. 1], with its three parts separated: a goal, a proxy, and optimization.
3. **The diagnostic sentence** [@manheim2019goodhart, p. 1]: importance scales with the power directed at the proxy. **The question is not "is there a metric" but "how hard is somebody pushing on it".**
4. **The four mechanisms**, quoted [@manheim2019goodhart, p. 2].
5. Each one worked on the case, from `case-data.md` §5, with the agent column.
6. **Only the fourth involves anybody deciding anything**, and this is the section's main result.
7. **Regressional cannot be avoided** [@manheim2019goodhart, p. 2]. Connect backwards: Chapter 3's score-is-not-the-construct plus Chapter 8's estimator properties, meeting selection.
8. **Campbell's law**, quoted as reported at [@manheim2019goodhart, p. 8 n.5], with provenance stated.
9. **The Lucas critique named, not quoted, and the book saying it has not read Lucas (1976).** One short paragraph. State its content in the book's own words.
10. **The source's caveat** [@manheim2019goodhart, p. 1 n.1]: the categories do not match the original formulations. Quote it.
11. Say the source is a preprint whose taxonomy began informally, and that the book uses the taxonomy and not the framing.
12. **Reader task.** Which mechanism would remain if the utility had done nothing at all?

## 8. Section 4 — Purpose or Response: a Discriminator

**Beats.**

1. Restate Chapter 4's debt in Chapter 4's own words, quoted from its spec.
2. **Why inspection cannot do it.** Both produce the same signature; a reader looking for a pattern finds whichever they expected.
3. **Self-explanation pause 2.** Given the series alone, can you tell whether the utility's records were shaped by institutional purpose or by response? Try, before reading the answer.
4. **The discriminator: find the date the measure acquired consequences; look for a discontinuity there and not before.**
5. **Why it works.** Institutional purpose is standing and drifts; response has a start date.
6. **Three properties that make it applicable**: documentary date, no counterfactual needed, fails safely.
7. **The failure mode, stated where it cannot be missed.** A discontinuity at the date is strong evidence. **No discontinuity is weak evidence of nothing** — response may be gradual or the measure anticipated.
8. Apply it to the case. 2019 is documentary; the discontinuity is at 2019; the pre-period is flat.
9. **And apply it to Chapter 3's finding, which is the payoff.** Chapter 3's zone was recorded as adequately served because of where an instrument happened to be. **Before 2019 that was purpose. After 2019 the same fact is response** — and Chapter 3, working from inside its own data, could not have told the difference.
10. **Reader task.** Name one dataset you have used where you could find the date and one where you could not.

## 9. Section 5 — When the Prediction Changes the Target

**Beats.**

1. **`endogenous response`**, and the case's version: the utility's forecast of complaints stopped working because of what the utility did about the count.
2. **The broken relationship, quantified**, from `case-data.md` §4: 0.72 fitted on three flat years, forecasting 439 against an outcome of 930.
3. **`performativity`** [@perdomo2020performative, §1], quoted.
4. **The scope claim** [@perdomo2020performative, Abstract], quoted, and the reason it matters: without it, a reader takes performativity for a machine-learning problem.
5. **The ordinary-English collision**, once.
6. **Performative stability and Chapter 6's calibration** [@perdomo2020performative, Abstract]. Chapter 6 scored forecasts against what happened; here what happens depends on the forecast.
7. **The retraining reframing** [@perdomo2020performative, §1], and its transfer: a model that keeps needing refitting may be a system converging.
8. **Not policy resistance**, once, with the distinction stated.
9. **Say the source is cited by section and why** — one sentence, because the reader will notice.
10. **Reader task.** Name one forecast in this book whose publication would change what it forecasts.

## 10. Section 6 — Two Parties, and an Equilibrium Nobody Wanted

**Beats.**

1. **`strategic dependence`** [@osborne2004game, p. 11], quoted, with the observation that every chapter before Part IV assumed it away.
2. **The strategic game's three ingredients** [@osborne2004game, p. 11], with emphasis on preferences over profiles.
3. **Belief is required** [@osborne2004game, p. 19], quoted, and the Chapter 11 contrast: there the states had probabilities; here the states are other people's choices.
4. **The table**, from `case-data.md` §6. The book's fourth notation extension; introduce the convention in two sentences and say where it comes from.
5. Walk the four cells.
6. **Self-explanation pause 3.** Given the table, what should the regulator do?
7. **`equilibrium as consistency`** [@osborne2004game, p. 20]: the two components quoted, the definition paraphrased and said to be.
8. **The bottom-right cell, and why nobody can move.**
9. **It delivers what the top-left delivered, at a cost of £1.8m.** The equilibrium is no improvement on the arrangement it replaced.
10. **The unreachable cell** — 13.1 — and why it is unreachable.
11. **The two senses of `equilibrium`, as a four-row table, once.** Close with: a pendulum has an equilibrium and has no beliefs.
12. **The source's own caution** [@osborne2004game, p. 20], quoted. **Fourth time a source has disqualified its own generality on the page that introduces it**; name the pattern in prose, once.
13. **Why the obvious remedies fail.** A better metric acquires consequences too; more metrics give more surfaces; and auditing the moves finds nothing, because nothing was hidden.
14. **Reader task.** Propose a fifth option for the regulator and say what it costs.

## 11. Section 7 — The Vocabulary, and What It Is Missing

**Beats.**

1. The six machinery terms, one worked instance each, from `case-data.md` §7. **Brisk — this is a vocabulary section and should read like one.**
2. **`commitment` gets the longest treatment**, because it is the only one that suggests a remedy, and because the remedy costs the regulator something it wants.
3. **Manipulation of evidence**, distinguished from everything else in the chapter: the case contains none, and the distinction is the point. Fabricating a reading is fraud; moving a sensor and documenting it is not, **and the second is more dangerous because nothing triggers.**
4. **And then the honest paragraph.** `principal-agent` and `information asymmetry` are named in the book's governed architecture and **no source for either was obtained.** State that research was reopened, that four attempts across three routes failed, that one source was obtained and declined for unusable text, and that `../../decisions/0022` clause 9 refers the question to the author. **Do not soften this.**
5. **Planted-defect diagnosis task.** Five defects per `transfer.md`. One correctly identifies gaming and prescribes the wrong remedy.

## 12. Section 8 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 answer. Compare, do not score. Three patterns: the network improved; somebody cheated; and the right answer with no way to check it.
2. **Cold transfer.** Both forms listed, one assigned.
3. **Retrieval from memory** — the procedure, six steps.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form.
6. Short diagnostic if the transfer went badly.
7. **What this chapter did not give you.**
8. Close: Part IV is finished, and Part V begins by asking which of the machinery a new problem needs.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production.

## 13. What the draft may not do

- Introduce any notation beyond the single two-by-two table permitted by `../../decisions/0022` clause 5.
- Teach mechanism design, auction theory, voting theory, or social choice.
- Teach mixed strategies, extensive form, subgame perfection, repeated games, bargaining, or best-response functions.
- Teach contract theory of any kind.
- Teach the mathematics of performative prediction or any result from it.
- Teach the formal models inside `manheim2019goodhart`'s four sections.
- Quote Osborne's definition of Nash equilibrium, or any `perdomo2020performative` sentence containing an `fi`.
- Cite `perdomo2020performative` by page.
- Claim anything about Lucas (1976), Goodhart (1975), or Campbell (1979) beyond what the reporting source states.
- Present the case as dishonest, or the regulator as foolish.
- Present the discriminator as decisive.
- Re-teach Chapter 13's policy resistance, or cite its sources.
- Reopen Chapter 3's or Chapter 4's findings.
- Claim a frequency for measurement-point re-designation, or say anything about any real regulator or company.
- Present the payoff numbers as derived from anything.
