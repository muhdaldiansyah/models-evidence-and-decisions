# Chapter 17 Drafting Blueprint

Status: drafting control. Governs how `chapter.md` is written. Scope, terminology, and sources are governed by `spec.md` and are not restated here.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0024`, three of whose clauses need author attention.

## 1. Drafting objective

18 pages / 5 learning hours that leave the reader able to tell a trigger from a timer, say what a monitoring arrangement cannot see, and diagnose a failure by the stage it entered through rather than the stage it appeared in.

The chapter must **defeat** twelve named collapses (`spec.md`, "Failure modes").

**And it must end the book.**

## 2. Fixed architecture and budget

| § | Title | Words |
|---|---|---:|
| 1 | Eighteen Months Later | 720 |
| 2 | Deployment Is Not a State | 1,080 |
| 3 | Signal, or Ordinary Variation | 1,440 |
| 4 | A Trigger That Was a Timer | 1,080 |
| 5 | What Monitoring Cannot See | 1,080 |
| 6 | Diagnosis by Stage | 720 |
| 7 | Retirement | 360 |
| 8 | Cold-Start Practice, and What This Book Has Not Established | 360 |

About **6,840 words**. **The shortest chapter in the book.**

### As drafted — recorded, not silently rebalanced

The manuscript came in at **6,398 words**, 93.5% of budget, which is where Chapters 14, 15, and 16 also landed. The distribution, however, is not the one this table planned.

| § | Planned | As drafted |
|---|---:|---:|
| 1 | 720 | 557 |
| 2 | 1,080 | 922 |
| 3 | 1,440 | 1,207 |
| 4 | 1,080 | 905 |
| 5 | 1,080 | 913 |
| 6 | 720 | 637 |
| 7 | 360 | 274 |
| 8 | 360 | **983** |

**§8's budget was wrong when it was written.** It was set at 360 words as a standard closing section, before §12's beat list was written — and that beat list asks §8 to carry the ordinary transfer-and-retrieval apparatus *and* the book's ending: five named things the book has not established, one registry entry that does not close, and retirement applied to the book itself. Those are not compressible into 360 words, and cutting them to fit the table would cut the material clause 10 of `../../decisions/0024` governs.

**§§1–7 are each about 85% of plan and are not short of beats.** Every beat in §§5–11 below is present in the manuscript; the shortfall is density, not omission. No beat was dropped to make room for §8.

The table above is left as written so the gap between plan and draft stays visible.

## 3. Voice and exposition rules

- One sentence per line in manuscript prose.
- Second person for reader tasks; third person for the cases.
- Bold **only** for case quantities and the first appearance of a controlled term.
- **No new notation.** Six of the last seven chapters have added none.
- **No quotation may contain a comparison symbol.**
- **No quotation from `sumanprajapati2018control` may contain an `fi`.**
- **`perdomo2020performative` is cited by section, never by page.**
- **`nasa2024models` is cited by printed page**, which `research-01` establishes coincides with the file page.
- Every figure the chapter reports appears in `case-data.md`.

### Register discipline

Five failure modes specific to this chapter, and the last two are about it being last.

**Sounding like quality management.** The architecture permits control-chart machinery and the chapter declines it. What it must not do is gesture at the machinery it declined, or use its vocabulary decoratively.

**Blaming the committee.** Case 1's committee misread a disjunction and reached, by accident, the defensible answer. **A chapter that treats them as careless has missed both halves of the finding**, and the second half is that nobody in the room could have known the answer was defensible.

**Sounding as though monitoring were the problem.** The monitoring in Case 2 was competent and reported monthly. **It was watching outputs, and the failure was not in the outputs.** That is not a criticism of the monitoring.

**Ending with a summary.** Chapter 16 already refused the recapitulation, and doing it here would be worse, because there is nothing after it to correct the impression.

**Ending with congratulation.** `../../decisions/0023` clause 5.4 forbade a transfer claim and `../../decisions/0024` clause 10.5 repeats it for the last page. **The book closes on what it has not established.**

## 4. Reader-facing sequence

Per `../../decisions/0008`. Three pauses: §3 (is seven a signal?), §4 (what should the committee have done?), §6 (where did it enter?).

## 5. Section 1 — Eighteen Months Later

**Beats.**

1. Pick up Chapter 16's closing sentence directly.
2. Say what has changed: sixteen chapters built things, and nothing in the book has yet asked whether a built thing is still working.
3. **The water case returns**, and say plainly that this is its thirteenth and last appearance.
4. **Opening task, about twelve minutes, before any vocabulary.** Give Chapter 12's plan verbatim and the four operating years from `case-data.md` §3. Ask: **what should the October report have said each year, and what would have counted as a signal?** **Preserve unscored.**
5. Do not reveal the baseline. §3 does.

## 6. Section 2 — Deployment Is Not a State

**Beats.**

1. **`monitoring`**, and the canon's own line: it is the same activity as Chapter 5's model checking, after the model is in use.
2. **Say the distinction is smaller than it looks**, and that what changes is the stakes, the audience, and the fact that somebody must be assigned.
3. **`permissible use`** [@nasa2024models, p. 87], with the release passage quoted.
4. **The sentence the chapter turns on**, quoted: "Each application of the M&S restarts the M&S use/operation with an assessment of permissible uses against the needs of that specific proposed use."
5. **Deployment is a repeated act, not a state**, and the manuscript says so in those words.
6. **`placarding`**, from the same page, as the third option.
7. **Fourth appearance of the relation-not-property shape**, in prose. Chapter 7 owns the table.
8. **`revision trigger`** [@nasa2024models, p. 18] — re-established on any change to **the world or the model**. Chapter 12's signposts watch only the first.
9. **Reader task.** Name a change to the *model* — not the world — that should reopen the water utility's plan.

## 7. Section 3 — Signal, or Ordinary Variation

**Beats.**

1. **The architecture permitted control-chart machinery and this chapter declines it.** Say so, say what is being declined, and say why. Per `../../decisions/0024` clause 2.
2. **The distinction and its attribution** [@sumanprajapati2018control, p. 1], with the provenance stated: Shewhart (1931) could not be obtained.
3. **`ordinary variation`** and **`signal`**, defined.
4. **The baseline**, from `case-data.md` §2. Both series, both sets of statistics.
5. **Self-explanation pause 1.** Heat events reached seven in 2025. Is that a signal?
6. The answer: **seven equals the baseline maximum and sits 1.84 standard deviations above the baseline mean.**
7. **The threshold-as-timer result**, stated as the book's own derivation: **the demand limb sits 2.12 standard deviations above its baseline mean and was never reached in seven years; the heat limb fires on a one-in-seven-year value, which is 2.1 expected firings over a fifteen-year horizon from baseline variation alone.**
8. **One limb was a trigger. The other was a timer.**
9. **And the calculation is four lines on data the utility already had.**
10. **Say that Chapter 8 gave the reader this habit nine chapters ago**, and that the book itself did not apply it in Chapter 12.
11. **Reader task.** Set a heat-event threshold that would be a trigger, and say what it costs.

## 8. Section 4 — A Trigger That Was a Timer

**Beats.**

1. The four operating years from `case-data.md` §3.
2. **The demand limb never fired, and Chapter 12 said it might not.** Quote Chapter 12's own warning.
3. **The heat limb fired in 2025.** The report recorded it. The minute says "signposts reported; no action required."
4. **Self-explanation pause 2.** What should the committee have done?
5. **Why nothing happened**, and it is not carelessness: the two limbs were reported together, one had been watched for two years and had not fired, and **the disjunction was read as a conjunction.** The rule said **or**.
6. **And now the uncomfortable part.** Given §3's arithmetic, not acting was defensible — and nobody in the room could have said so.
7. **A right answer reached by misreading is not a right answer.** State it plainly.
8. **`tampering`** arrives here: had the committee acted on every firing of a limb that fires once in seven years by chance, it would have been adjusting a stable process. **The mechanism is Chapter 13's** [@sterman2006evidence, p. 508], quoted, with the precondition added.
9. **Say the term is the book's own and that no source was obtained for it**, in one sentence, per clause 6.
10. **Reader task.** Rewrite the "If" clause so that it cannot be misread.

## 9. Section 5 — What Monitoring Cannot See

**Beats.**

1. Case 2. The three monitored indicators from `case-data.md` §6, all fine or better.
2. **The completion figure improved for a reason**, and the reason is the failure.
3. **The unreported ratio**, from §7: 6.83 to 8.08, up 18.3%.
4. **Both numbers were collected by different teams and the ratio is nobody's report.** Note that this repeats Chapter 15's finding exactly, once.
5. **`drift`** [@perdomo2020performative, Abstract and §1], quoted — and the point that **detecting drift is not diagnosing it.**
6. **Calibration as the one instrument that generates a signal automatically**, one sentence, from Chapter 6.
7. **The central claim**: monitoring observes outputs, so it cannot see failures in what the thing was built to represent.
8. **The visibility table**, from `case-data.md` §9.
9. **The early stages are invisible and the late ones visible**, which is the reverse of where attention goes.

## 10. Section 6 — Diagnosis by Stage

**Beats.**

1. **Self-explanation pause 3.** The symptom is a queue. Where did the failure enter?
2. The answer: **Chapter 4, nine stages and eighteen months earlier.**
3. **A failure is diagnosed where it entered, not where it was noticed.**
4. **Chapter 16 routed forward from a problem; this chapter routes backward from a symptom.** Same fifteen categories, opposite directions. One sentence.
5. **And no monitoring arrangement could have caught this one**, which is not a criticism of the monitoring.
6. **Reverse-flow loops** [@nasa2024models, p. 88], quoted — a standards body saying the same thing Chapter 16 said about the teaching order. One sentence, no more.
7. **Planted-defect diagnosis task.** Five defects. **One correctly identifies a monitoring gap and proposes a monitoring fix for a failure no monitoring could catch.** Feedback linked only after production.

## 11. Section 7 — Retirement

**Beats.**

1. **[@nasa2024models, p. 39], quoted**: a plan for "acquisition, development, operation, maintenance, and retirement", with responsible organisations named.
2. **Five verbs, and this book has discussed four of them.**
3. **`retirement`**, defined: the planned end of a model's working life.
4. **A model nobody has retired is not thereby still fit for use.** It is a model nobody has looked at.
5. **One page, and no more.** The point is that the item exists.

## 12. Section 8 — Cold-Start Practice, and What This Book Has Not Established

**Beats.**

1. Return to the §1 answer. Compare, do not score. Two things to look for.
2. **Cold transfer.** Both forms listed, one assigned. Retrieval from memory, five steps. Rubric after production. Delayed retest.
3. **Then the book's ending**, and it is short.
4. **What has not been established**, named: no pilot data for any exercise in the book; Gate 1 open since Chapter 1 and now fourteen chapters deep; sixteen decision records unadjudicated; and the book's claim about its own transfer, which is nil.
5. **One registry entry does not close.** `utility`, belonging to Chapter 11, with no later chapter to close it in.
6. **And close on retirement**, applied to the book: the last item in the standard's five-verb plan is the one nothing here has discussed, including about itself.
7. **No summary. No congratulation.**

### Concealment discipline

`transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, and `diagnosis-feedback.md` are linked exactly once each, at the moment of use. The rubric is never linked before production.

## 13. What the draft may not do

- Introduce notation, machinery, or a new case.
- Teach control charts, control limits, run rules, chart types, or sampling plans — and not gesture at them either.
- Teach drift-detection methods of any kind.
- Teach governance or assurance frameworks.
- Re-read or re-cite `fda2023credibility`, `asme2025credibility`, or `nrc2012reliability`.
- Quote `sumanprajapati2018control` with an `fi`, or cite `perdomo2020performative` by page.
- Claim anything about Shewhart (1931) or about Deming.
- Present the committee as careless, or the monitoring as inadequate.
- Rework the water case beyond operating the plan Chapter 12 wrote.
- Draw any conclusion about climate from the heat-event series.
- Claim that this book produces transfer, or summarise the book, or congratulate the reader.
