# Chapter 15 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 15: **Strategic Interaction, Incentives, and Endogenous Response** — the last chapter of Part IV.

**Process note.** As in Chapters 3–14, this audit was written alongside its research. Findings taken from sources are marked. Every locator was taken from reading the document directly.

Current architecture from `README.md` and `spec.md`:

- central question: **What changes when the system contains other modelers?**
- core competence: **Reason about strategic dependence, incentives, equilibrium as consistency, commitment, information asymmetry, principal-agent relationships, delegation, endogenous response, metric gaming, Goodhart-type failures, Campbell's law, Lucas critique, and manipulation of evidence.**
- target: 30 pages / 6 serious learning hours.

## 1. Readiness verdict

**Drafting-ready after adjudication**, and it is the hardest exposition problem in the book.

Four observations.

**The core competence names thirteen things.** That is the largest count in the book by some margin — Chapter 8 named eight, Chapter 13 nine, Chapter 14 seven. **They are not thirteen topics**, and a chapter that treated them as thirteen topics would be a glossary. The audit's central recommendation is that they be organised as one claim plus a working vocabulary.

**The one claim is available and it is sharp:**

> When the system contains people who know what you are measuring and why, the relationship you measured before they knew is not the relationship you will get after.

That covers seven of the thirteen directly — endogenous response, metric gaming, Goodhart-type failures, Campbell's law, the Lucas critique, manipulation of evidence, and (in its formal dress) performativity. The remaining six — strategic dependence, incentives, equilibrium as consistency, commitment, information asymmetry, principal-agent relationships, and delegation — are **the machinery for reasoning about why it happens**, and can be taught as a short vocabulary with one worked instance each on the chapter's own case.

**Twelve chapters have deferred here.** Chapter 15 is the most pre-promised chapter in the book, ahead of Chapters 7, 9, and 14.

**And one of those deferrals is a hard specification rather than a topic.** `../04-observation-provenance/spec.md` L36 requires that Chapter 15 supply its distinction "in a form the reader can apply, since institutional purpose and strategic response look identical from inside a dataset." That is a demand for a **usable discriminator**, not for a definition, and it is the sharpest test the chapter has to pass.

## 2. Unique-job hypothesis

> Teach readers that a measured relationship is a fact about a world in which nobody was being measured for consequences — and that once consequences attach, the relationship is not evidence about the new world but a relic of the old one.

The reader who finishes Chapter 15 should be able to date the moment a measure acquired consequences, look for a discontinuity at that date, distinguish a record shaped by institutional purpose from one shaped by response to being measured, name which of four mechanisms produced a metric failure, describe a two-party interaction as a game and say what makes an outcome stable, and recognise that the stable outcome can be worse for both parties than an unstable one.

## 3. What earlier chapters have promised

| Promised in | Text | Settled by |
|---|---|---|
| `../../decisions/0007` | "Chapter 15 owns strategic dependence, incentives, equilibrium, principal-agent reasoning, gaming, and endogenous behavioral response" | the whole chapter |
| `../../decisions/0007` | "Formal payoff functions, best response, games, equilibrium, principal-agent analysis, metric gaming, and mechanism design remain Chapter 15" | §§2, 6 |
| `../../decisions/0007` | "`performative prediction` is not required Chapter 1 vocabulary... formal strategic and performative analysis remains Chapter 15" | §5 |
| `01/chapter.md` L885, `01/spec.md` L235 | deployment-induced change deferred here | §5 |
| `02/spec.md` L191 | endogenous/exogenous treatment deferred here | §3 |
| `03/spec.md` L163 | measurement gaming deferred here | §3 |
| `04/spec.md` L36 | **the discriminator, "in a form the reader can apply"** | §4 |
| `04/chapter.md` L710–722 | "Chapter 15 is about what happens when the people in a system respond to being measured... nothing about the network changed. What changed was the recording process, in response to being watched." | §§3–4 |
| `07/spec.md` L120 | strategic confounding deferred here | §2 |
| `08/spec.md` L99 | manipulation of evidence deferred here | §7 |
| `10/chapter.md` L369, L905, `10/spec.md` L95 | "Chapter 15 is about what happens when the people being measured notice" | §3 |
| `11/chapter.md` L201 | gaming a decision rule deferred here | §6 |
| `13/chapter.md` L1075 | "The reservoir does not have interests. Chapter 15 does." | §1 |
| `14/chapter.md` L1010 | "**Chapter 15 removes that assumption.**" | §1 |
| `canon/terminology.md` | `equilibrium` — "Chapter 15 (strategic sense, 'equilibrium as consistency')"; the two senses "must not be conflated" | §6 |

## 4. Neighbouring-chapter boundaries

### Chapter 3 — measurement, and the chapter's best available demonstration

Chapter 3 found the utility's records calling a zone adequately served **because of where an instrument happened to be installed**.

**Chapter 15 can show the same fact with a different cause**: after the measure acquired consequences, instrument placement stopped being an accident and became a choice. **Chapter 3 could not have told the difference from inside its own data**, and saying so is the strongest demonstration the chapter has.

### Chapter 4 — the hard promise

Chapter 4 taught that records exist because of a process, and explicitly showed a Chapter 15 example once, as out of scope. **The debt is a discriminator the reader can apply**, and the audit's recommendation is that it be built from Chapter 4's own machinery: date the moment the measure acquired consequences, and look for a discontinuity there.

### Chapter 13 — equilibrium, and a collision the canon already anticipates

`canon/terminology.md`'s `equilibrium` entry records both senses and says they must not be conflated. Chapter 13 closed the dynamic sense. **Chapter 15 owes the strategic sense and owes the distinction**, and it is not the same distinction as any of the book's five previous collisions: this is one word with two technical senses in two different chapters of the same book, which is worse than one word used loosely.

### Chapter 14 — rules

Chapter 14's rules acted on a system that did not care what the rule was. **Chapter 15 removes exactly that assumption**, and its own manuscript says so in its last paragraph. The chapter should pick that up in its first.

### Chapter 17 — monitoring

Whether a deployed rule is still working after people have responded to it is Chapter 17's. Chapter 15 stops at the response.

## 5. Terminology readiness

| Term | State | Source position |
|---|---|---|
| `strategic dependence` | new | `osborne2004game` p. 11 |
| `strategic game` | new | `osborne2004game` p. 11 |
| `equilibrium as consistency` | `equilibrium` exists with the strategic sense reserved; **closed here** | `osborne2004game` p. 20 |
| `incentive` | new as a controlled term | the book's own, built on the case |
| `principal-agent` | new | the book's own; **no primary source obtained** |
| `information asymmetry` | new | the book's own; **no primary source obtained** |
| `delegation` | new | the book's own |
| `commitment` | new | `osborne2004game` p. 20's steady-state reading, extended |
| `endogenous response` | new | `perdomo2020performative` §1 |
| `performativity` | new | `perdomo2020performative` Abstract, §1 |
| `metric gaming` | new | `manheim2019goodhart` §4 |
| `Goodhart's law` | new | `manheim2019goodhart` p. 1 n.1, **as reported at** |
| `Campbell's law` | new | `manheim2019goodhart` §4, **as reported at** |
| `Lucas critique` | new | `manheim2019goodhart` p. 1, **as reported at** |

**Three "as reported at" uses in one chapter** — more than any previous chapter. Goodhart (1975), Campbell (1979), and Lucas (1976) are all named in the governed core competence and **none could be obtained**. This is a substantial and recordable gap.

**Two terms have no source at all** — `principal-agent` and `information asymmetry`. See §9.

## 6. High-risk conceptual collapses to prevent

1. **Strategic response is dishonesty.** The chapter's case is entirely legal and documented.
2. **Gaming means cheating.** Manheim's four mechanisms include two that need no agent at all.
3. **Goodhart's law says metrics are bad.** It says a regularity collapses under pressure, which is narrower and more useful.
4. **All metric failures are the same failure.** `manheim2019goodhart` distinguishes four.
5. **Strategic equilibrium is Chapter 13's equilibrium.** One is a stationary condition on dynamics, the other a consistency condition on beliefs and actions.
6. **An equilibrium is a good outcome.** `osborne2004game` p. 20 defines it as a state nobody wishes to deviate from, which says nothing about whether anybody likes it.
7. **Institutional purpose and strategic response are distinguishable by inspecting the data.** They are not — Chapter 4 said so — and the discriminator is a date, not a pattern.
8. **Performativity is a machine-learning problem.** `perdomo2020performative` says it is "well-studied in policy-making" and had been neglected in supervised learning, which is the opposite claim.
9. **The fix is a better metric.** A better metric acquires consequences too.
10. **The fix is more metrics.** More surfaces to respond to.
11. **You can anticipate the response by modelling the agent.** Sometimes; and the agent is modelling you.
12. **Nobody is responsible because the system did it.** Chapter 13 carried `sterman2006evidence` p. 510 on exactly this and the point holds here.

## 7. Research clusters

1. **Strategic games, strategic dependence, and equilibrium as consistency.**
2. **Goodhart-type failures and their mechanisms.**
3. **Endogenous response and performativity.**
4. **The discriminator, the chapter's case, and exercise design.**

## 8. Candidate example constraints

The anchor is available for a **fifteenth** recurrence, and the case must for the first time contain a **second party with its own objectives** — the regulator.

Constraints:

- The metric must be one the reader already knows, and the natural choice is **properties below minimum pressure**, which Chapter 3 established the utility measures at a representative point.
- The response must be **entirely legal and documented**, or the chapter teaches fraud rather than strategy.
- There must be **a datable moment** at which the measure acquired consequences, because the discriminator Chapter 4 asked for is a date.
- A **relationship that held before and broke after** must be shown numerically, and its breaking must be quantified as a forecasting failure rather than asserted.
- The case must reuse **Chapter 3's representative-point finding** and add no new physical fact.
- The regulator must be **acting reasonably**, or the chapter teaches that regulation is foolish.

**Gate 1 remains open and is now twelve chapters deep.**

## 9. Decisions likely required after research

1. **Whether the thirteen competences are organised as one claim plus vocabulary.** Recommend **yes**, and that the manuscript say so to the reader.
2. **Whether a two-player payoff table is added.** Recommend **yes, bounded** — it is genuinely needed for strategic dependence and equilibrium, `osborne2004game` p. 19 supplies the convention, and Chapter 11 already permits a decision table. **This would be the fourth notation extension and the first in four chapters.**
3. **How to handle three unobtainable primary sources.** Recommend the **as reported at** device for all three, with the gap recorded at book level, because Goodhart, Campbell, and Lucas are named in governed text.
4. **What to do about `principal-agent` and `information asymmetry`, for which no source was obtained.** This is the live question and it is §9's real content — see the decision record.
5. **How `equilibrium`'s two senses are separated.** Recommend one paragraph and one table row, in the chapter that owns the second sense.
6. **The fifteenth water-case recurrence, with a second party.**

## 10. Drafting gate

Do not draft until:

- `../../decisions/0022` exists in proposed form;
- the terminology block is written, including `equilibrium`'s strategic sense;
- `case-data.md` freezes the seven-year series and **every ratio and forecast error is computed and checked**;
- `spec.md` records the discriminator Chapter 4 asked for, in applicable form.
