# Decision 0021: Chapter 14 Sequential Control Terminology and Boundary

## Status

**PROPOSED (2026-08-18) — awaiting author adjudication.**

Written in the form of a decision so its consequences are inspectable, but **not** adjudicated by the author. `readiness-audit.md` §9 reserves these choices to the author, and `CLAUDE.md` requires that architectural changes be surfaced rather than silently applied.

`spec.md`, the drafting blueprint, the manuscript, and the Chapter 14 entries in `canon/terminology.md` are built on this record and inherit its provisional status.

**Two clauses need author attention beyond the usual.** Clause 6 registers a term `README.md`'s Chapter 14 block does not name. Clause 8 records that the chapter's principal concept is taught from a review rather than from the paper that named it.

Evidence base: `../chapters/14-sequential-control/research-01-policies.md`, `research-02-observability.md`, `research-03-identifiability.md`, `research-04-information-exploration-and-examples.md`.

## Decision

Chapter 14's organizing claim is:

> In a repeated decision the object of choice is a rule, not an action — and a rule can only use what the instruments reveal, which is a question you can answer before collecting any data.

### 1. The governed block excludes, and the exclusions are binding

**1.1** `README.md`'s Chapter 14 entry is the only chapter block in the book that names its own exclusions: "Formal dynamic programming, filtering, LQR, MPC, POMDP, and reinforcement-learning algorithms belong in the depth curriculum."

**1.2** All six are honoured, and `research-plan.md` records for each one what was read up to the line and what was not opened.

**1.3** **The line runs mid-source twice.** `astrom2008feedback` introduces observability and then constructs an observer on the following pages; the chapter takes the concept and refuses the construction. `sutton2018reinforcement` defines exploration and exploitation and then gives methods for balancing them; the chapter takes the definitions and refuses the methods.

### 2. A policy is the object of choice

**2.1** `policy` is taught from [@sutton2018reinforcement, p. 58]: a mapping from states to probabilities of selecting each possible action.

**2.2** **The chapter's central move is that a rule, not an action, is what gets chosen.** A plan says what to do on given days; a policy says what to do given what you see.

**2.3** **A policy cannot be evaluated on one history.** The chapter's case gives five summers, and on one of them all four rules are identical.

**2.4** The problem/solution-method distinction is taken from [@sutton2018reinforcement, p. 2] and stated to the reader: **this chapter teaches the problem and not the solution methods**, so that a reader who meets the field later does not assume something was withheld silently.

### 3. Evaluative feedback names something the book has been doing since Chapter 6

**3.1** [@sutton2018reinforcement, p. 25] distinguishes evaluative from instructive feedback.

**3.2** **This is why the utility's nine years under one rule cannot rank rules.** The record says how that rule did; nothing in it says what another rule would have done.

**3.3** The manuscript notes once that Chapters 6 and 8 were working with evaluative feedback without the word.

### 4. Observability

**4.1** Closed from `TODO` in `canon/terminology.md`, where it has stood since Chapter 1.

**4.2** **The source's Definition 7.1 is paraphrased and not quoted**, because it carries a quantifier, an inequality, and an interval. The paraphrase is declared in the manuscript. This is the second time the standing rule from Chapter 8 has cost the book a definition rather than a flourish.

**4.3** The prose at [@astrom2008feedback, p. 202] carries the teaching: no hidden dynamics; understanding through observation **over time**; and the practical form — observability "will determine if a set of sensors is sufficient for controlling a system."

**4.4** **Unobservable does not mean unmeasured.** Two different states producing identical records are unobservable however carefully the existing instruments are read.

**4.5** **Third appearance of the relation-not-property shape**, after Chapter 3's `validity` and Chapter 9's `transportability`. Observability is a property of a system paired with a set of instruments. Named in prose; Chapter 7 owns the table.

**4.6** `virtual sensor` is taken from the same page **with an immediate caution**: it is a model output being treated as a measurement, and Chapters 3 and 4 spent forty pages on why that substitution needs watching.

**4.7** **No observer, no state estimation, no separation principle, no Kalman filter, and no rank test.**

### 5. Structural identifiability

**5.1** Closed from `TODO`, where it has stood since Chapter 1, and reserved for here by `0014` clause 3.

**5.2** Taught from [@wieland2021identifiability, p. 61]: a model is structurally identifiable if a unique parameterization exists for any given model output.

**5.3** **The diagnostic is the compensation clause** — a parameter is non-identifiable when changing it need not alter the trajectory "because the changes can be fully compensated by altering other parameters."

**5.4** **The chapter's most consequential claim is that this is knowable before any data exists.** It follows from the model's form and the measurement setup. Chapter 8 needed twenty-four records to produce an interval; Chapter 14's non-identifiability needs none.

**5.5** The source's own connection to observability is used: on the surface of parameter values producing identical outputs, the model's internal variables can change without the observations changing.

### 6. Practical identifiability — registered, and not named in the governed block

**6.1** **This clause needs author attention.** `README.md`'s Chapter 14 core competence names seven things and `practical identifiability` is not among them.

**6.2** It is registered anyway, on three grounds. **The source introduces the two terms in one sentence** [@wieland2021identifiability, p. 61] and the structural sense is hard to hold without its contrast. **Chapter 8 taught the thing without the name** — an interval of finite size from twenty-four events is a practical-identifiability finding. And **the distinction is what tells a reader whether more data would help**, which is the operative question.

**6.3** Taught from [@wieland2021identifiability, p. 63]: a *combination of model and data* is practically identifiable if the confidence intervals of all estimated parameters are of finite size.

**6.4** **The source's own reservation is quoted** [@wieland2021identifiability, p. 60]: practical nonidentifiability "has not been investigated at the same conceptually clear level."

**6.5** **If the author declines the registration, the honest response is to cut the term and keep the contrast in prose** — not to teach the structural sense alone, which would leave readers unable to tell a fixable problem from an unfixable one.

### 7. The four-way collision, announced once

**7.1** Four terms now share the adjective *identifiable*. `0014` clause 3 registered three of them as a three-way distinction; the research found a fourth.

| Term | The question it asks | Home |
|---|---|---|
| `statistical identifiability` | Can the parameter be determined from the distribution the data come from? | Chapter 7 |
| `causal identification` | Can the causal effect be determined from available data plus stated assumptions? | Chapter 7 |
| `structural identifiability` | Can the model's parameters be determined from its input-output behaviour, in principle? | **Chapter 14** |
| `practical identifiability` | Can they be determined from the data in hand, with adequate precision? | **Chapter 14** |

**7.2** **This is the sixth collision announcement in the book** — after `validation`, `consistency`, `significance`, `sensitivity analysis`, and `robustness`/`stability` — and the first involving four senses rather than two.

**7.3** **Standing instruction proposed: no chapter may add a fifth sense of `identifiable`.** If one is needed, the table is reopened at book level rather than extended in a chapter.

### 8. The chapter's principal concept is taught from a review

**8.1** **This clause needs author attention.** `structural identifiability` originates with Bellman and Åström (1970), confirmed from [@astrom2008feedback, p. 378]. **That paper could not be obtained**, and no route to a copy with checkable pagination was found.

**8.2** The concept is therefore taught from a 2021 review. **This is the first time a canon `TODO` has been closed from a secondary source**, and the book's source discipline prefers primary verification.

**8.3** It is **not** an instance of the demonstrate-because-unsourced disposition: a source was obtained, read directly, and quoted. It is a weaker citation than the book prefers, and it is recorded rather than smoothed over.

### 9. Information acquisition — Chapter 11's ceiling, not Chapter 11's arithmetic

**9.1** Chapter 11 computed a value of information from a prior. Chapter 12 established that this book's settings frequently supply none.

**9.2** **The chapter's instrument decision is in the second kind of setting**, so it uses Chapter 11's perfect-information **ceiling** as a screening rule and **computes no value**. The manuscript says why in one paragraph rather than inventing a prior.

**9.3** `colyvan2016voi` is not re-read and nothing new is claimed from it.

### 10. Exploration and exploitation

**10.1** Taught from [@sutton2018reinforcement, p. 26], with the trade stated in the source's own words.

**10.2** **The dilemma is presented as unresolved**, quoting [@sutton2018reinforcement, p. 3]: it "has been intensively studied by mathematicians for many decades, yet remains unresolved."

**10.3** The `k-armed bandit` is **named once** and no method for it is taught. The source's own depth statement at p. 27 is quoted, and the chapter takes the same position one step further back.

**10.4** **The case supplies what assertion could not**: on one of five summers every rule is identical, and between the two live candidates two of five are identical. **Information about a rule arrives only in years that test it, and most years do not.**

### 11. Control

**11.1** Taught at definitional depth only, from [@astrom2008feedback, pp. 3–4]: control as the use of algorithms and feedback in engineered systems, and the sensing–computation–actuation loop.

**11.2** **Nothing else.** No controller, no tuning, no stability margin, no design method. Chapter 13 already refused the controller on the page that gave it the oscillation mechanism, and Chapter 14 does not pick it up.

### 12. Notation

**12.1** **None is added.** The sequence stays where 0018 left it; 0019, 0020, and now 0021 add nothing.

**12.2** **Third consecutive chapter to add nothing.**

**12.3** No state-space form, no policy notation, no value functions, no Bellman equation, no block diagrams.

### 13. Vocabulary

**13.1** Introduced here: `policy`, `feedback decision`, `practical identifiability`, `information acquisition`, `exploration`, `exploitation`, `control`.

**13.2** Closed here: `observability` and `structural identifiability`, both `TODO` since Chapter 1.

**13.3** **After this chapter, one `TODO` remains in the registry** — `utility`, which the registry assigns to the already-drafted Chapter 11 and which Chapter 11 did not close. It was surfaced by `0020` clause 12.4 and is **still not repaired**; it now stands alone, which makes it harder to overlook.

### 14. What Chapter 14 does not do

- Teach dynamic programming, filtering, LQR, MPC, POMDPs, or reinforcement-learning algorithms. `README.md` excludes all six.
- Teach observers, state estimation, the separation principle, or the Kalman filter.
- Teach the observability rank test, reachability, or state feedback.
- Teach profile likelihood, the Fisher information matrix, or any identifiability test.
- Teach any bandit algorithm, action-value method, or exploration schedule.
- Teach a control law of any kind.
- Re-teach Chapter 13's stocks, delays, and feedback, which it uses on every page.
- Re-teach Chapter 11's value-of-information arithmetic.
- Reopen Chapter 7's identification verdict.
- Treat rules that agents respond to *because they are the rules* — Chapter 15.
- Treat whether a deployed rule is still working — Chapter 17.

## Sources promoted

`sutton2018reinforcement` and `wieland2021identifiability` are new to `references.bib`. `astrom2008feedback` is extended to pp. 201–202 and to its bibliography at p. 378.

## Known gaps carried forward

1. **Bellman and Åström (1970) not obtained** — clause 8. The chapter's principal concept is taught from a review.
2. **`wieland2021identifiability` is written for systems biology**, and the book widens its distinction across domains as its own synthesis.
3. **`sutton2018reinforcement` read at five pages of roughly 550.**
4. **`astrom2008feedback` observability read at pp. 201–202 only**; the rank test, observers, and Kalman filtering are unread and unclaimed.
5. **An `ff`-ligature extraction problem in `sutton2018reinforcement`** cost several quotable sentences, which are paraphrased with the paraphrase declared.
6. **`practical identifiability` is not named in `README.md`'s Chapter 14 block** — clause 6.
7. **No source was sought for how often a decision rule is dominated in practice.** The case shows one that is; no frequency is claimed.
8. The **Chapter 14 case is the water anchor's fourteenth recurrence**, and Chapter 1's Gate 1 remains open.

## No architecture change

This record proposes no change to `README.md`'s parts, chapters, sequence, or governed fields. **Clause 6 registers a term the governed core competence does not name**, which is the closest this record comes, and it is flagged for author review rather than applied silently.
