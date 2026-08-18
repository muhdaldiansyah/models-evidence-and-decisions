# Chapter 14 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0021`.

## 1. Drafting objective

28 pages / 6 learning hours that leave the reader able to state a rule somebody else could apply, compare rules across histories, say what the instruments cannot distinguish, say which parameters cannot be separated, and tell a fixable problem from an unfixable one.

The chapter must **defeat** thirteen named collapses (`spec.md`, "Failure modes").

## 2. Fixed architecture and budget

| § | Title | Words |
|---|---|---:|
| 1 | The Thing You Are Choosing Is a Rule | 1,080 |
| 2 | Policies, and Why One Summer Cannot Rank Them | 1,800 |
| 3 | What the Instruments Determine | 1,440 |
| 4 | Two Parameters That Cannot Be Told Apart | 1,800 |
| 5 | Measure More, or Model Less | 1,080 |
| 6 | Buying an Instrument | 1,080 |
| 7 | Exploration, and Why Most Years Teach Nothing | 1,080 |
| 8 | Cold-Start Practice and Retrieval | 720 |

About **10,080 words**.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the case.
- Bold **only** for case quantities and the first appearance of a controlled term.
- **No new notation.** Third consecutive chapter to add none.
- **No quotation may contain a comparison symbol.** Åström's Definition 7.1 is paraphrased and said to be.
- **No quotation may contain an `ff`.** `sutton2018reinforcement`'s ligature does not survive extraction; affected sentences are paraphrased and the paraphrase is declared.
- Every figure the chapter reports appears in `case-data.md`.

### Register discipline

Four failure modes specific to this chapter.

**Sounding like a machine-learning chapter.** Two of the three sources belong to fields with large apparatus, and `README.md` excludes all of it. Where the chapter stops short, it should say what it is stopping short of and why, so the reader knows the omission is deliberate.

**Sounding like the utility was foolish.** P1 is dominated, which is stronger than anything the book has said about the utility so far. The manuscript must show that P1 was a reasonable rule to write in the absence of a comparison, and that the comparison is what nobody did.

**Sounding like an instrument is always the answer.** Chapter 11 settled that more information is not always worth buying, and §5's *measure more or model less* has two options for a reason.

**Sounding certain about the exploration trade.** The source says it is unresolved. So does the chapter.

## 4. Reader-facing sequence

Per `../../decisions/0008`. Self-explanation pauses: exactly three — §2 (which rule would you keep?), §4 (what would settle it?), §7 (how many years would you need?).

## 5. Section 1 — The Thing You Are Choosing Is a Rule

**Beats.**

1. Pick up Chapter 13's closing question directly.
2. **Opening task, about ten minutes, before any vocabulary.** Give the utility's rule from Chapter 13 and the finding that it fired too late. Ask the reader to **write a better rule**, precisely enough that somebody who was not in the room could apply it, and to say how they would know it was better. **Preserve unscored.**
3. Name the shift: thirteen chapters asked for an analysis, an estimate, or a choice. This one asks for a rule.
4. Say what a rule has to have to be applicable — a trigger with a number, a response, a stand-down — and note that Chapter 12's signpost discipline is the same standard.
5. Name the second half of the task as the harder half: *how would you know it was better?*
6. Close on what the chapter will do: compare four rules across five summers, then ask what the utility can see at all.

## 6. Section 2 — Policies, and Why One Summer Cannot Rank Them

**Beats.**

1. **`policy`**, from [@sutton2018reinforcement, p. 58], quoted.
2. **A plan says what to do on given days; a policy says what to do given what you see.** The chapter's own gloss, and the distinction the section turns on.
3. The four rules from `case-data.md` §2, each stated as a rule.
4. **The five summers**, and why five: one history cannot rank rules.
5. **The results table**, from `case-data.md` §4.
6. **Self-explanation pause 1.** Which rule would you keep, and what does your choice say about what you are willing to pay?
7. **Finding one: P1 is dominated.** Worse on all four measures than P4. State it plainly and then defend the utility: **nobody had run the comparison**, and a rule that has never been compared is not a rule anybody chose.
8. **Finding two: P4 differs from P1 in one respect — what it watches.**
9. **Finding three: the remaining choice is a judgment.** One day below the service standard against 94 ML. Route it to Chapter 10 and do not settle it.
10. **Evaluative versus instructive feedback** [@sutton2018reinforcement, p. 25], quoted. This is *why* nine years under one rule cannot rank rules.
11. Note once that Chapters 6 and 8 were working with evaluative feedback without the word.
12. **Say what is being withheld** [@sutton2018reinforcement, p. 2]: this chapter teaches the problem, not the solution methods, and `README.md` says why.
13. **Reader task.** Write a fifth rule and predict its row.

## 7. Section 3 — What the Instruments Determine

**Beats.**

1. Frame: every rule in §2 fires on a signal. What if the signal has two causes?
2. The utility's four instruments, from `case-data.md` §7.
3. The two states — hot-weather demand, and a burst — and that they produce the same record.
4. **`observability`**, paraphrased from [@astrom2008feedback, p. 202], **with the paraphrase declared and the reason given.**
5. The prose quoted: no hidden dynamics; observation **over time**; and the practical form — whether a set of sensors is sufficient.
6. **Unobservable is not unmeasured.** Work the distinction on the case.
7. **The consequence for every rule in §2.** All four fire on the same signal, and on a burst the response makes it worse — Chapter 13's policy resistance inside a Chapter 14 rule.
8. **Third appearance of the relation-not-property shape**, after Chapter 3's `validity` and Chapter 9's `transportability`. Prose only; Chapter 7 owns the table.
9. **`virtual sensor`** named, with the Chapters 3 and 4 caution attached immediately.
10. **Reader task.** Name one state pair in the water case, other than this one, that the utility's instruments cannot separate.

## 8. Section 4 — Two Parameters That Cannot Be Told Apart

**Beats.**

1. The utility's demand model, and its exact fit to the heatwave week.
2. **The 82.** Base demand plus leakage, and the three splits that fit identically.
3. **Self-explanation pause 2.** What data would settle which split is right?
4. The answer, and it is the section: **no amount of the data the utility collects will settle it**, because the two parameters enter only as a sum.
5. **`structural identifiability`** [@wieland2021identifiability, p. 61], quoted, with the compensation clause as the diagnostic.
6. **The claim that makes this chapter different: it was knowable before any data existed.** Chapter 8 needed twenty-four records; this needs none.
7. **`practical identifiability`** [@wieland2021identifiability, p. 63], quoted, as a property of model **and** data — and Chapter 8's interval re-described as an instance.
8. **The source's own reservation** [@wieland2021identifiability, p. 60], quoted.
9. **The four-way collision table**, once. Per `../../decisions/0021` clause 7.
10. Say that the source is written for systems biology and that the widening is the book's own.
11. **Say that the term's origin could not be obtained**, and that this chapter closes a canon entry from a review. One paragraph, per clause 8.
12. **And the consequence: a live decision is undecidable.** Chapter 12's £380,000 scheme.
13. **Reader task.** Find a second pair of quantities in the book that were only ever observed as a sum.

## 9. Section 5 — Measure More, or Model Less

**Beats.**

1. **The two options** [@wieland2021identifiability, p. 64], quoted.
2. **Nobody proposes the second**, and it is often cheaper and always faster. Chapter 10's alternative-set point, arriving with a technical warrant.
3. **Chapter 4 found the utility had already taken it, silently.** Its demand figure is a model with the leakage parameter removed by fiat, and the residual containing a third of things that are neither Hillcrest nor demand is what that costs.
4. **The difference between doing it and recording it.** Modelling less is a legitimate choice; doing it without writing it down is how a residual becomes a measurement.
5. **Reader task.** Write the sentence the utility should have put in its records in 2014.

## 10. Section 6 — Buying an Instrument

**Beats.**

1. The night-flow meter, from `case-data.md` §7, and why 03:00.
2. **One instrument, two problems.** It separates the two states *and* splits the 82.
3. **No probability is available**, and the chapter does not invent one. Say why in one paragraph: Chapter 11's arithmetic needs a prior, Chapter 12 established there isn't one.
4. **Chapter 11's ceiling, reused.** £18,000 against £380,000 — 4.7%.
5. **What a ceiling argument does and does not say.** It cannot be screened out on cost; that is not the same as being worth buying, and Chapter 11 taught exactly this use.
6. **`control`**, defined [@astrom2008feedback, pp. 3–4], and the sensing–computation–actuation loop — with the observation that the utility has been doing all three badly at the first step.
7. **A system can be controlled and still do badly.** Control names an activity, not an achievement.
8. **Reader task.** Name the one measurement that would most change the book's analysis, across all fourteen chapters.

## 11. Section 7 — Exploration, and Why Most Years Teach Nothing

**Beats.**

1. The utility has nine years under P1 and none under anything else.
2. **`exploration` and `exploitation`** [@sutton2018reinforcement, p. 26], quoted.
3. **The trade**, quoted from the same page.
4. **Self-explanation pause 3.** How many summers would the utility need to run P4 before it knew whether P4 was better?
5. **The answer is worse than the reader expects.** On the mild summer every rule is identical; between P2 and P4, two summers in five are identical. **Most years teach nothing**, and the utility gets one year per year.
6. **The dilemma is unresolved** [@sutton2018reinforcement, p. 3], quoted. Say the source says so.
7. **And the source's own guarantees passage** [@sutton2018reinforcement, p. 27], quoted, connecting to Chapters 5, 7, and 8.
8. **`k-armed bandit` named once**, method refused, with the source's own depth statement quoted.
9. **Planted-defect diagnosis task.** Five defects per `transfer.md`. One is true of the case and false as a general claim.

## 12. Section 8 — Cold-Start Practice and Retrieval

**Beats.**

1. Return to the §1 rule. Compare, do not score. Three patterns: no threshold; no stand-down; and no answer to *how would you know it was better*.
2. **Cold transfer.** Both forms listed, one assigned.
3. **Retrieval from memory** — the procedure, seven steps.
4. Rubric linked **after** production only.
5. **Delayed retest** on the other form.
6. Short diagnostic if the transfer went badly.
7. **What this chapter did not give you** — and here the list is long and specific, because `README.md` names six exclusions and the reader should know their names.
8. Close: Chapter 15 asks what happens when the system contains people who know what the rule is.

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production.

## 13. What the draft may not do

- Introduce notation of any kind.
- Teach dynamic programming, filtering, LQR, MPC, POMDPs, or reinforcement-learning algorithms.
- Teach observers, state estimation, the separation principle, the Kalman filter, the observability rank test, reachability, or state feedback.
- Teach profile likelihood, the Fisher information matrix, or any identifiability test.
- Teach any bandit algorithm, action-value method, or exploration schedule.
- Teach a control law.
- Quote Åström's Definition 7.1, or any sentence containing an `ff` from Sutton and Barto.
- Compute a value of information. The ceiling only.
- Claim anything about Bellman and Åström (1970) beyond its existence and its title.
- Present `practical identifiability` as governed vocabulary; it is flagged for review.
- Claim a frequency for dominated rules in practice.
- Re-teach Chapter 13's stocks, delays, or feedback.
- Re-estimate anything Chapter 7 declared not identified.
- Present the case values as typical, standard, or recommended.
