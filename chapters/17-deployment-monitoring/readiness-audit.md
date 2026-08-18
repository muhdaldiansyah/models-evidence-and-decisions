# Chapter 17 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 17: **Deployment, Monitoring, and Revision** — the last chapter of the book.

**Process note.** As in Chapters 3–16, this audit was written alongside its research. Findings taken from sources are marked. Every locator was taken from reading the document directly.

Current architecture from `README.md` and `spec.md`:

- central question: **Is the deployed reasoning still working — and if not, which stage failed?**
- core competence: **Design monitoring, distinguish signal from ordinary variation, recognize drift and tampering, diagnose failure by stage, define revision triggers, and return deliberately to earlier parts of the reasoning process.**
- target: 18 pages / 5 serious learning hours — **the shortest chapter in the book.**
- **`README.md` permits, without requiring**: "Concept-level monitoring machinery may include common-cause versus special-cause variation and control-chart reasoning where appropriate."

## 1. Readiness verdict

**Drafting-ready after adjudication**, and it is the chapter with the most inherited obligations and the fewest pages to discharge them in.

Five observations.

**Fourteen chapters defer here** — more than to any other chapter in the book. Chapters 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, and 16 all name Chapter 17 in their specs, and Chapters 10, 12, and 16 name it in their manuscripts.

**Two of those deferrals are specific enough to be requirements rather than topics.**

`canon/terminology.md`'s `signpost` entry: "**Chapter 12 designs signposts and Chapter 17 operates them**, which is where the question of whether anyone is actually looking belongs."

`chapters/16-integration-full-loop/chapter.md` hands over its own case: the repairs-triage tool "has been running for eighteen months, and the analysis in §4 is a photograph of a system that was moving while it was photographed."

**The chapter therefore has two cases handed to it**, and it should take both: the water utility's adaptive plan from Chapter 12, and Chapter 16's automated tool.

**And the water anchor comes home.** Chapter 16 left it deliberately. **This is the last chapter of the book and the anchor's sixteenth and final appearance**, and it appears in order to have its own Chapter 12 output criticised.

**The permitted machinery is permitted, not required.** "May include... where appropriate" is the only permissive phrasing of its kind in the book's architecture. The audit's recommendation is that the chapter take the **distinction** — signal against ordinary variation — and refuse the **charts**, because the core competence names the distinction and not the technique.

## 2. Unique-job hypothesis

> Teach readers that monitoring catches failures which show up in outputs and is constitutionally incapable of catching failures in what the thing was built to represent — and that knowing which is which is a diagnosis, made by stage, before anything has gone visibly wrong.

The reader who finishes Chapter 17 should be able to say what a deployed piece of reasoning would have to show to be judged still working, distinguish a signal from ordinary variation by reference to a baseline rather than to a threshold somebody invented, recognise when a trigger is a timer, diagnose which stage a failure entered through, and say which failures no monitoring arrangement could have caught.

## 3. What earlier chapters have promised

| Promised in | Text | Settled by |
|---|---|---|
| `04/spec.md` L145 | "Monitoring design, drift detection, tampering detection, revision triggers: Chapter 17" | §§2, 4, 6 |
| `05/spec.md` L60, L147 | predicted failure modes; "monitoring design, drift and tampering detection, revision triggers" | §§5, 6 |
| `06/spec.md` L58, L154 | calibration in the forecast sense, and monitoring design | §3 |
| `08/spec.md` L100 | "post-deployment monitoring" | §3 |
| `09/spec.md` L96 | "post-deployment checking of a transported result" | §5 |
| `10/spec.md` L96, `10/chapter.md` L192 | "implementation and monitoring"; "the sequence closes" here | §6 |
| `11/spec.md` L98 | monitoring | §3 |
| `12/spec.md` L94, `12/chapter.md` L1031 | "operating signposts"; "where the question of whether anyone is actually looking belongs" | §§2–4 |
| `13/spec.md` L91, `14/spec.md` L89, `15/spec.md` L86 | whether a deployed rule is still working after the response | §§4–5 |
| `16/chapter.md` L908 | "what gets monitored, what would count as a signal, what would trigger a revision — and, when something has clearly gone wrong, which of the fifteen stages it entered through" | §§2–5 |
| `canon` `failure mode` | "detecting failures after deployment is Chapter 17" | §5 |
| `canon` `model checking` | "distinct from Chapter 17's post-deployment monitoring, which is the same activity after the model is in use" | §3 |
| `canon` `signpost` | "Chapter 12 designs signposts and Chapter 17 operates them" | §§2–4 |

**And one obligation of a different kind.** This is the last chapter, and the book ends here. It has to close.

## 4. Neighbouring-chapter boundaries

### Chapter 5 — model checking, and the sentence that separates them

`canon/terminology.md`'s `model checking` entry already draws the line: post-deployment monitoring is "**the same activity after the model is in use**".

**That is a smaller distinction than it looks and the chapter should say so.** What changes after deployment is not the activity but the stakes, the audience, and the fact that somebody has to be assigned to do it — which is the whole of §2.

### Chapter 12 — signposts

Chapter 12 wrote a plan with two thresholds and said, in its own text, that "those numbers are arguable, and being arguable is the property that matters."

**Chapter 17 argues with them**, which is what Chapter 12 invited and what the canon entry assigns here.

### Chapter 16 — triage and backward revision

Chapter 16 taught diagnosis of a problem before the work. **Chapter 17 diagnoses a failure after it**, and the two use the same fifteen categories in opposite directions.

**The distinction to hold:** Chapter 16 routes forward from a problem; Chapter 17 routes backward from a symptom.

### The book's ending

Chapter 17 is the last chapter. **Its final section is the book's final section**, and the audit recommends it close on what the book has not established rather than on what it has.

## 5. Terminology readiness

| Term | State | Source position |
|---|---|---|
| `monitoring` | new as a controlled term | the book's own; distinguished from `model checking` in the canon since Chapter 8 |
| `ordinary variation` / `signal` | new | `sumanprajapati2018control` p. 1, for the common/special-cause distinction and its attribution |
| `drift` | new | `perdomo2020performative`, already read |
| `tampering` | new, **and no source obtained** | the book's own, built on Chapter 13's overshoot mechanism |
| `revision trigger` | new | the book's own; extends Chapter 12's `signpost` |
| `failure diagnosis by stage` | new | the book's own |
| `permissible use` | new | `nasa2024models` p. 87 |
| `retirement` | new | `nasa2024models` p. 39 |

**Six of the eight are the book's own or extend its own.** That is appropriate for a closing chapter whose subject is operating what the previous sixteen built.

**One term has no source: `tampering`**, which is named in the governed core competence. See §9.

**No collision requiring announcement.** The second chapter in a row with none.

## 6. High-risk conceptual collapses to prevent

1. **Monitoring catches failures.** It catches failures that show up in outputs.
2. **A threshold is a trigger.** A threshold set below a level that has already occurred is a timer.
3. **A signal is a value past a threshold.** A signal is a value that ordinary variation does not readily produce, and the threshold should have been set from the baseline.
4. **No alarm means nothing is wrong.** Chapter 15 established one reason; this chapter adds another.
5. **Drift and tampering are the same thing.** One is the world changing; the other is somebody adjusting a stable process.
6. **Monitoring is a technical activity.** It is an assignment. An unwatched signpost is a diary entry.
7. **Post-deployment checking is a new activity.** The canon already says it is the same activity later.
8. **A failure is diagnosed where it was noticed.** It is diagnosed where it entered, which is usually much earlier.
9. **Every failure could have been caught by better monitoring.** Some could not have been caught by any.
10. **A revision trigger is a plan to think again.** Chapter 12 established that a review date is not a signpost, and the same applies here.
11. **Deployment is the end of the process.** `nasa2024models` p. 87 requires that **each application restart** the assessment.
12. **A model in use is a model that was validated.** It was validated for a permissible use, and this use may not be that one.

## 7. Research clusters

1. **Deployment, permissible use, and the life cycle.**
2. **Signal against ordinary variation.**
3. **Drift, tampering, and what monitoring cannot see.**
4. **Diagnosis by stage, the two cases, and exercise design.**

## 8. Candidate example constraints

**Two cases, both inherited.**

**Case 1 — the water utility's Chapter 12 signposts, operated for four years.** The anchor's sixteenth and final appearance. Constraints: no new physical fact; the plan is quoted from Chapter 12 unchanged; and the criticism must be of a threshold rather than of the people watching it.

**Case 2 — Chapter 16's repairs-triage tool.** Constraints: no new facts beyond what Chapter 16 froze, plus the monitoring the authority actually had; and the diagnosis must land on a stage Chapter 16 already identified, because the point is that the failure was diagnosable before it was visible.

**Gate 1 remains open and is now sixteen chapters deep.** With this chapter the anchor's appearances end, and Gate 1's scope is complete: it concerns the thirteen chapters in which the water case appears.

## 9. Decisions likely required after research

1. **Whether control-chart machinery is taught.** Recommend **no** — take the distinction, refuse the charts, and say the architecture permitted more.
2. **What to do about `tampering`, for which no source was obtained.** It is named in the governed core competence. Recommend registering it as the book's own term built on Chapter 13's overshoot mechanism, with the gap recorded and referred to the author — and **explicitly not** a new instance of the demonstrate-because-unsourced disposition, because the mechanism it names is already sourced at Chapter 13.
3. **Whether the chapter criticises Chapter 12's own output.** Recommend **yes**; Chapter 12 invited it in its own text and the canon assigns it here.
4. **How the book closes.** Recommend closing on what is not established.
5. **Whether the water anchor returns.** Recommend **yes**, for the last time, and that the chapter say it is the last time.
6. **Whether any new notation is added.** Recommend **none**. That would be six of the last seven chapters.

## 10. Drafting gate

Do not draft until:

- `../../decisions/0024` exists in proposed form;
- the terminology block is written;
- `case-data.md` freezes both cases and **every baseline statistic is computed and checked**;
- `spec.md` records how the book's final section closes.
