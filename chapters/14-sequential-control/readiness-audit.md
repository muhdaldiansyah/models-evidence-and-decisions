# Chapter 14 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 14: **Sequential Decisions, Information, and Control** — the second chapter of Part IV.

**Process note.** As in Chapters 3–13, this audit was written alongside its research. Findings taken from sources are marked. Every locator was taken from reading the document directly.

Current architecture from `README.md` and `spec.md`:

- central question: **How should choices be made through time as information arrives?**
- core competence: **Reason with policies rather than one-shot actions, feedback decisions, observability, structural identifiability, information acquisition, exploration versus exploitation, and control at a foundational conceptual level.**
- target: 28 pages / 6 serious learning hours.
- **`README.md` states its own exclusions**, which no other chapter's block does: "Formal dynamic programming, filtering, LQR, MPC, POMDP, and reinforcement-learning algorithms belong in the depth curriculum."

## 1. Readiness verdict

**Drafting-ready after adjudication.**

Four observations.

**The governed block excludes more than it includes, and that is unusual.** Chapter 14's README entry names seven competences and then names six bodies of machinery that are *not* to be taught. Every one of the six is the standard way its competence is formalised. The chapter therefore has to teach what each idea is *for* without teaching the apparatus that makes it precise — which is the hardest exposition problem in the book so far.

**Two `TODO` entries in `canon/terminology.md` close here**, and they are the last two that were ever scheduled: `observability` and `structural identifiability`. After this chapter the only open entry is `utility`, which the registry assigns to the already-drafted Chapter 11 and which Decision 0020 clause 12.4 surfaced as unclosed.

**The chapter's material is already latent in three earlier chapters, and the reader has not been told.** Chapter 4 found the demand figure was production minus metered consumption — a residual. That is not merely a data-quality complaint: it is a **structural non-identifiability**, and it can be diagnosed from the model and the instruments alone, before any data is collected. Chapter 6 got the Hillcrest mechanism to 91% and Chapter 7 refused the causal sentence. Chapter 14 can ask the prior question neither asked: **is the state the utility wants to know observable from the instruments it has?**

**And Chapter 13 handed this chapter a specific question in its last paragraph**: the utility made the same decision over and over with a rule that could not have worked, so what is the rule for choosing, and how would you know a good one?

## 2. Unique-job hypothesis

> Teach readers that in a repeated decision the object of choice is a **rule**, not an action; that a rule can only use what the instruments reveal; and that what a set of instruments cannot reveal is a question answerable before any data is collected.

The reader who finishes Chapter 14 should be able to state a decision rule precisely enough to be applied by somebody else, evaluate it across several histories rather than one, say which states the available instruments cannot distinguish, say which parameters the available measurements cannot separate, decide whether to buy an instrument or simplify the model, and recognise that trying a different rule is the only way to learn about it.

## 3. What earlier chapters have promised

| Promised in | Text | Settled by |
|---|---|---|
| `../../decisions/0007` | "Chapter 14 owns sequential decisions, policies, information/control, observability, structural identifiability, filtering, and exploration/exploitation" | the whole chapter |
| `../../decisions/0007` | "Formal policies, dynamic programming, filtering, exploration/exploitation, control, and observability remain Chapter 14" | §§2, 4, 7 |
| `01/spec.md` L234 | repeated-decision screen deferred here | §2 |
| `02/spec.md` L190 | state-space machinery, reachability, observability deferred here | §4 |
| `05/chapter.md` L509 | "Chapter 14 uses `structural identifiability` for something entirely different... Different concept, shared adjective" | §5 |
| `06/spec.md` L153 | sequential updating deferred here | §6 |
| `07/chapter.md` L454, `07/spec.md` L63, L119 | `structural identifiability` "named here only so that the three-way distinction is on the record" | §5 |
| `12/spec.md` L93 | sequential decision-making deferred here | §2 |
| `13/chapter.md` L1070, L1086 | "Choosing what to do about it — what to watch, how hard to respond, when to stop — is control, and it is Chapter 14's" | §§2–3 |
| `canon/terminology.md` | `observability` and `structural identifiability`, both `TODO — verify against canonical sources` | §§4–5 |

**Nine chapters have deferred here.** Chapter 14 is the third-most pre-promised chapter in the book, after Chapters 7 and 9.

## 4. Neighbouring-chapter boundaries

### Chapter 7 — the three-way distinction comes due

Chapter 7 registered `statistical identifiability`, `causal identification`, and `structural identifiability` as three different things sharing a word, and taught the first two. **Chapter 14 owes the third**, and it owes the distinction as a distinction rather than as a fourth definition.

The research adds a fourth term the book did not anticipate: **practical identifiability**, which is what Chapter 8 was doing without the name. That is a gift and a hazard — four terms with one adjective between them, and the chapter must not turn into a glossary.

### Chapter 11 — value of information

Chapter 11 computed what one study was worth to one decision. Chapter 14 asks what an instrument is worth to a *rule* that will run for years. The machinery is the same and the object is not, and the chapter must reuse rather than re-teach.

**One honest limit carries forward.** Chapter 11's arithmetic needed a prior. Chapter 12 established that there are settings with no probabilities to be had. Chapter 14's instrument decision is in the second kind of setting, and the chapter should use Chapter 11's **ceiling** as a screening rule rather than pretending to a computed value.

### Chapter 12 — robustness

Chapter 12 chose a portfolio robust across futures. Chapter 14 chooses a rule robust across histories. The shape is the same and the manuscript should say so once, without rebuilding the regret table.

### Chapter 13 — dynamics

Chapter 13 diagnosed why a rule failed. Chapter 14 chooses among rules. **The line is that Chapter 13 owns the system's behaviour and Chapter 14 owns the decision-maker's rule**, and the chapter must resist re-teaching stocks, delays, and feedback, all of which it uses on every page.

### Chapter 15 — strategic response

Chapter 15 owns systems containing agents who respond to the rule because it is the rule. Chapter 14's system does not care what rule is in force.

### Chapter 17 — monitoring

Whether a deployed rule is still working is post-deployment.

## 5. Terminology readiness

| Term | State | Source position |
|---|---|---|
| `policy` | new | `sutton2018reinforcement` p. 58 |
| `feedback decision` | new | built from `astrom2008feedback` pp. 2, 22 and Chapter 13's `closed loop` |
| `observability` | exists as `TODO`; **closed here** | `astrom2008feedback` p. 202 |
| `structural identifiability` | exists as `TODO`; **closed here** | `wieland2021identifiability` p. 61 |
| `practical identifiability` | new, **unanticipated by the architecture** | `wieland2021identifiability` pp. 61, 63 |
| `information acquisition` | new | extends Chapter 11's `value of information` |
| `exploration` / `exploitation` | new | `sutton2018reinforcement` pp. 3, 26 |
| `control` | new as a controlled term | `astrom2008feedback` pp. 3–4 |

**One collision requiring announcement, and it is the book's largest.** Four terms now share the adjective *identifiable*: statistical, causal, structural, and practical. Three are already in the registry. This is the sixth collision announcement in the book and the first involving four senses rather than two.

**One recommendation about depth.** `sutton2018reinforcement` states its own depth choice at p. 27 — "we do not worry about balancing exploration and exploitation in a sophisticated way; we worry only about balancing them at all" — and that is exactly the position this chapter should take, from a source that took it first.

## 6. High-risk conceptual collapses to prevent

1. **A policy is a plan.** It is a rule that maps what you see to what you do, so it produces different actions on different histories.
2. **A good rule is one that worked.** One history cannot rank rules; four of this chapter's five summers do not discriminate at all.
3. **Observability is about whether an instrument exists.** It is about whether the instruments you have determine the state.
4. **Unobservable means unmeasured.** A state can be unobservable with perfect instruments if two different states produce identical readings.
5. **Structural non-identifiability is a data problem.** It is a property of the model and the measurement setup, diagnosable before any data exists.
6. **Structural and practical non-identifiability are the same thing.** More data cures the second and cannot touch the first.
7. **Any of the four identifiabilities is any other.** Chapter 7 registered three; the research found a fourth.
8. **More information is always worth buying.** Chapter 11 settled this and Chapter 14 must not unsettle it.
9. **Exploration is a luxury.** It is the only way information about an untried rule arrives.
10. **Exploration is free because you learn either way.** In most years the rules do not differ and nothing is learned.
11. **The theory settles it.** `sutton2018reinforcement` p. 3 says the dilemma "remains unresolved".
12. **Control means being in control.** It is a defined activity — sensing, computation, actuation — and a system can be controlled and still do badly.

## 7. Research clusters

1. **Policies, and how to compare rules rather than actions.**
2. **Observability: what the instruments determine.**
3. **Structural and practical identifiability, and the four-way collision.**
4. **Information acquisition, exploration versus exploitation, and the chapter's own case.**

## 8. Candidate example constraints

The anchor is available for an **eleventh** recurrence, and for the first time the chapter must run the case over **several years** rather than one episode.

Constraints:

- The rules compared must include **the utility's actual rule from Chapter 13**, so the comparison is with something the book has already shown failing.
- At least one summer must be **completely uninformative** — every rule identical — because that is the exploration lesson and it cannot be asserted.
- The observability failure must be between **two states the book has already established**: hot-weather demand and a burst main. No new mechanism.
- The structural non-identifiability must be **Chapter 4's subtraction residual**, re-described. It is already in the book, it is a genuine instance, and re-describing it costs no new fact.
- The instrument that repairs both must be **one instrument**, and its cost must be small relative to a decision the book has already priced.
- No reopening of Chapter 7's verdict.

**Gate 1 remains open and is now eleven chapters deep.**

## 9. Decisions likely required after research

1. **How to handle four senses of `identifiable`.** Recommend a single announced table, once, and a standing instruction that no chapter add a fifth.
2. **Whether `practical identifiability` is registered**, given that the architecture did not anticipate it. Recommend **yes**, because Chapter 8 taught the thing without the name and the source's distinction is what makes the structural sense comprehensible.
3. **How far into control to go.** Recommend the definition and the sensing–computation–actuation loop, and nothing else. The README's own exclusions are binding.
4. **Whether the exploration treatment uses the bandit formalism.** Recommend naming the k-armed bandit once and refusing the formalism, following the source's own stated depth choice.
5. **Whether an instrument's value is computed.** Recommend **no computed value and a stated ceiling**, per Chapter 11's screening rule, because Chapter 12 established there is no prior here.
6. **The eleventh water-case recurrence, run across five summers.**

## 10. Drafting gate

Do not draft until:

- `../../decisions/0021` exists in proposed form;
- the terminology block is written, including the two `TODO` closures and the four-way collision table;
- `case-data.md` freezes the five summers and **every policy figure is computed and checked**;
- `spec.md` records where each of the README's six exclusions falls, in terms specific enough to be enforced.
