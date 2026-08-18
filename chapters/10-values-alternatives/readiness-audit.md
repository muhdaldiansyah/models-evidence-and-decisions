# Chapter 10 Readiness Audit

Status: pre-drafting working control; not a final chapter decision.

Chapter 10: **Values, Objectives, and Alternatives** — the first chapter of **Part III: Choose**.

**Process note.** As in Chapters 3–9, this audit was written alongside its research. Findings taken from sources are marked. Every locator was taken from reading the document directly.

Current architecture from `README.md` and `spec.md`:

- central question: **What matters, to whom, and what options exist beyond those offered?**
- core competence: **Structure values and consequences, distinguish values from measurable objectives and metrics, identify stakeholders and constraints, and generate alternatives instead of accepting a fixed option set.**
- target: 30 pages / 5 serious learning hours.

## 1. Readiness verdict

**Drafting-ready after adjudication**, with one obstacle that turned out to have a clean solution.

**Chapter 10 is a change of subject, not a change of topic.** Parts I and II asked what the evidence supports. From here the book asks what should be done, and the first move is to establish that this is a different kind of question with different failure modes. A reader arriving from nine chapters of evidential discipline will want to keep applying it, and much of what this chapter teaches cannot be settled by evidence at all.

**The obvious source could not be obtained, and the book already knew it.**

`../../sources/keeney1996valuefocused.md` records that the article was verified "at the official metadata-and-abstract level rather than a complete line-by-line inspection of the full article", and carries an explicit prohibition:

> "Do not attribute specific value-focused-thinking procedures, objective hierarchies, or formal alternative-generation methods to this source in Chapter 1 without full-text verification."

**Chapter 10 is precisely the chapter that needs those procedures, and full-text verification was attempted and failed.** Four routes were tried.

**The resolution is the book's standard one.** `bradley2016structured` — a 248-page EPA report, obtained in full and read at the relevant chapters — *reports* the value-focused framework at printed pp. 5–8 and 49–54, with its own attributions to Keeney (1992, 2007) and Gregory et al. (2012). The chapter takes the framework **as reported there**, exactly as Chapter 6 took Brier through `gneiting2007scoring`, Chapter 8 took Matrixx through `greenland2016misinterpretations`, and Chapter 9 took Russell through `deaton2016rct`.

The `keeney1996valuefocused` prohibition therefore stands unmodified, and the chapter honours it.

## 2. Unique-job hypothesis

> Teach readers that the option set they were handed is a claim about what matters, that nobody has written down what matters, and that doing so produces options nobody listed.

The reader who finishes Chapter 10 should be able to take a paper offering two options, find that it states no objective in usable form, produce a set that passes a stated test, identify who is affected and who was asked, separate real constraints from assumed ones, and generate at least one alternative that was not on the paper.

## 3. What earlier chapters have promised

| Promised in | Text | Settled by |
|---|---|---|
| `decisions/0006` L46, L65 | "Chapter 10 owns formal value structuring, objectives, measurable attributes or metrics, systematic alternative generation, and trade-off structure" | §§2–6 |
| `01/spec.md` L161, L230, L574 | `alternative`; value structuring; "require at least one additional plausible alternative" | §6 |
| `02/spec.md` L186 | values, objectives, metrics, alternatives generation | §§2–3 |
| `03/spec.md` L116; `decisions/0010` 6.5 | `metric` registered to Chapter 10 | §3 |
| `04/spec.md` L143 | metrics as objectives | §3 |
| `09/chapter.md` L789 | "Chapter 10 starts where Part II stops: with values, objectives, and the alternatives that were never on the table" | §1 |
| `canon` | `objective` and `metric` at `Definition status: TODO` since Chapter 1 | §3 |

**One boundary is explicitly shared.** `decisions/0006` assigns "trade-off structure" to Chapter 10, and `README.md` assigns trade-offs and value of information to Chapter 11. The reading adopted here is that Chapter 10 establishes **that objectives conflict and that trade-offs will therefore be required**, and Chapter 11 does the machinery. This is flagged for adjudication as `../../decisions/0017` clause 5.

## 4. Neighbouring-chapter boundaries

### Chapter 9 — what precedes

Chapter 9 ended by listing four things the utility cannot settle from evidence, all of them value questions: fewer complaints at what cost, complaints from whom, what the money would otherwise fund, and whether an average improvement that worsens the worst days is an improvement.

**Those four are Chapter 10's opening, already written.**

### Chapter 11 — decisions under uncertainty

Chapter 10 stops before any method for choosing. It produces objectives, stakeholders, constraints, and alternatives. Weighing them under uncertainty, and asking what information would be worth buying, is Chapter 11.

The line to state: **Chapter 10 makes the decision well-posed. Chapter 11 solves it.**

### Chapter 12 — optimization and robustness

Formal optimization over the alternative set is Chapter 12's.

### Chapter 15 — strategic response

`metric` carries a forward reference already in canon: gaming and Goodhart-type failures are Chapter 15. Chapter 10 introduces metrics as attributes and hands the failure mode forward.

### Chapter 17 — monitoring

Bradley's process includes implementation and monitoring as a step that sets the context for the next decision. Chapter 10 names that the loop exists and routes it to Chapter 17.

## 5. Terminology readiness

| Term | State | Source position |
|---|---|---|
| `value` | new | `bradley2016structured` p. 5 |
| `objective` | stub, TODO since Chapter 1 | closed here; p. 50 supplies a testable format |
| `fundamental objective` | new | p. 51, with the "why is this important" test |
| `means objective` | new | p. 49's "messy mix of means and ends" |
| `attribute` | new | p. 51 |
| `metric` | stub, TODO since Chapter 1 | closed here, with the Chapter 15 warning retained |
| `stakeholder` | new | p. 7 |
| `constraint` | new | p. 7's "accepting constraints as immoveable" |
| `alternative` | exists, Chapter 1; systematic generation reserved here | closed here |

**No collisions requiring announcement.** Second consecutive chapter with none.

**One near-collision worth a line.** `attribute` was used in Chapter 7 for the components of an estimand. Here it is the measurable quantity at the bottom of an objectives hierarchy. Different objects, compatible senses, and the canon entry should say so.

## 6. High-risk conceptual collapses to prevent

1. **The options on the paper are the options.** The chapter's reason for existing.
2. **Objectives are obvious and need not be written.** p. 49: what decision-makers have is "a messy mix of means and ends, targets, policies and vision statements".
3. **A vision statement is an objective.** It has no direction of preference and no item of value.
4. **A metric is an objective.** Chapter 3's construct/measure distinction, in a new setting.
5. **More evidence will settle what matters.** It cannot, and nine chapters of evidential skill make this collapse more likely rather than less.
6. **Stakeholders are the people who were consulted.** They are the people affected.
7. **Constraints are given.** p. 7 names accepting them as immoveable as a documented trap.
8. **Generating alternatives is brainstorming.** It is derivation from objectives.
9. **One alternative per objective.** p. 54: "Most alternatives will affect more than one objective."
10. **Values are subjective and therefore not analysable.** They are structurable, and the whole chapter is the method.
11. **This is a stakeholder-engagement exercise.** The chapter is about making a decision well-posed, and engagement is one input.

## 7. Research clusters

1. **The values-objectives-alternatives structure**, and the AFT/VFT reversal.
2. **What counts as an objective**, and the tests available.
3. **Stakeholders and constraints.**
4. **Alternative generation, and the chapter's own examples.**

## 8. Candidate example constraints

The anchor is available for a **tenth** recurrence, and for the first time the chapter must produce a **decision** rather than an analysis.

Constraints:

- The committee paper must offer exactly **two** options, so that the fixed option set is visible on the page.
- The stated aim must **fail** the objective test — no item of value, no direction of preference.
- At least one generated alternative must be one the book has already produced for a different reason, so that the reader sees the same act from two framings.
- At least one "constraint" must dissolve on inspection.
- No new physical fact about Hillcrest.

**Gate 1 remains open and is now ten chapters deep.**

## 9. Decisions likely required after research

1. **The Keeney handling** — recommend as-reported-at-Bradley, with the existing prohibition intact.
2. **The Chapter 10 / Chapter 11 trade-off boundary**, which two governing documents divide differently.
3. **How much stakeholder-process material** — recommend the minimum that makes the concept usable, since the book is not a facilitation manual.
4. **Notation** — recommend none. Fourth consecutive chapter.
5. **Whether the objectives hierarchy is taught as a structure** — recommend yes, at concept depth, since two canon entries depend on it.
6. **The tenth water-case recurrence.**

## 10. Drafting gate

Do not draft until:

- `../../decisions/0017` exists in proposed form with the trade-off boundary settled;
- the nine canon entries are written, including `objective` and `metric`, TODO since Chapter 1;
- `case-data.md` freezes the committee paper, the stakeholder list, the constraint list, and the generated alternatives;
- `spec.md` records the Keeney handling explicitly.
