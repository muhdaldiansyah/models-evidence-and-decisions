# Models, Evidence, and Decisions

**An Integrated Course in Reasoning Under Uncertainty**

The book teaches technically literate professionals and advanced students to reason about unfamiliar consequential problems: working out what is actually being asked, what the available records can and cannot support, what a decision requires beyond evidence, and what to revise when action changes the system being acted on.

The intended reader is comfortable with algebra and willing to use light computation or simulation, but does not need prior specialist training in statistics, economics, operations research, causal inference, control theory, or decision analysis.

The book is not intended to replace specialist textbooks. Its differentiated purpose is to teach:

1. formulation before technique;
2. the interfaces between established disciplines;
3. reasoning from models and evidence to decisions and action;
4. dynamic and strategic consequences of action;
5. monitoring, criticism, and revision after deployment;
6. transfer to unfamiliar problems.

It is an integrated pedagogical architecture built from established concepts — not a proposed new discipline or unified formal theory — and it preserves the disciplinary distinctions it draws on rather than collapsing them for elegance (see [Intellectual Principle](#intellectual-principle)). A separate depth curriculum may later provide deeper technical study of specialist machinery.

## Start Here

**To read the book.** **All five parts are drafted** — seventeen chapters, written to be read in order:

> **[Chapter 1 — Decisions, Questions, and a First Complete Pass](chapters/01-decisions-questions/chapter.md)** — six sections, about four learning hours including exercises.
>
> **[Chapter 2 — Representation, Mechanisms, and Scale](chapters/02-representation-mechanisms/chapter.md)** — seven sections, about six learning hours.
>
> **[Chapter 3 — Measurement and Operationalization](chapters/03-measurement-operationalization/chapter.md)** — seven sections, about five learning hours.
>
> **[Chapter 4 — Observation Processes and Data Provenance](chapters/04-observation-provenance/chapter.md)** — seven sections, about five learning hours.
>
> **[Chapter 5 — Assumptions, Adequacy, and Rival Models](chapters/05-assumptions-rival-models/chapter.md)** — seven sections, about five learning hours.
>
> **[Chapter 6 — Probability, Prediction, and Simulation](chapters/06-probability-simulation/chapter.md)** — eight sections, about seven learning hours. The start of Part II.
>
> **[Chapter 7 — Targets, Identification, and Causal Claims](chapters/07-targets-identification/chapter.md)** — eight sections, about eight learning hours.
>
> **[Chapter 8 — Estimation, Uncertainty, and Model Checking](chapters/08-estimation-uncertainty/chapter.md)** — eight sections, about eight learning hours. The longest chapter in the book.
>
> **[Chapter 9 — Combining and Transporting Evidence](chapters/09-evidence-synthesis/chapter.md)** — seven sections, about five learning hours. The close of Part II.
>
> **[Chapter 10 — Values, Objectives, and Alternatives](chapters/10-values-alternatives/chapter.md)** — seven sections, about five learning hours. The start of Part III, and a change of subject.
>
> **[Chapter 11 — Decisions Under Uncertainty and Value of Information](chapters/11-decisions-voi/chapter.md)** — seven sections, about seven learning hours.
>
> **[Chapter 12 — Optimization, Robustness, and Adaptive Plans](chapters/12-optimization-robustness/chapter.md)** — eight sections, about seven learning hours. The close of Part III.
>
> **[Chapter 13 — Dynamics, Feedback, and Stability](chapters/13-dynamics-feedback/chapter.md)** — eight sections, about five learning hours. The start of Part IV, and the point at which the system stops holding still.
>
> **[Chapter 14 — Sequential Decisions, Information, and Control](chapters/14-sequential-control/chapter.md)** — eight sections, about six learning hours.
>
> **[Chapter 15 — Strategic Interaction, Incentives, and Endogenous Response](chapters/15-strategic-interaction/chapter.md)** — eight sections, about six learning hours. The close of Part IV, and the point at which the system starts reading the rule.
>
> **[Chapter 16 — Integration: The Full Loop on Unfamiliar Problems](chapters/16-integration-full-loop/chapter.md)** — eight sections, about six learning hours. The start of Part V, and the first chapter since Chapter 1 that adds no machinery.
>
> **[Chapter 17 — Deployment, Monitoring, and Revision](chapters/17-deployment-monitoring/chapter.md)** — eight sections, about five learning hours. The shortest chapter in the book, and the last.

Fifteen of the seventeen work one case: a small municipal water utility during a seven-day heatwave.

Chapter 1 frames the decision and discovers that the storage reading it depends on may be wrong. Chapter 2 asks what belongs inside a representation of that utility, and finds that the picture which answered Chapter 1's question cannot express who loses service first. Chapter 3 opens a phrase Chapter 2 deliberately left standing — *adequate or not* — and shows the utility's records calling a zone adequately served because of where an instrument happened to be installed. Chapter 4 turns on a figure the reader has been using since Chapter 2 and shows that it was never measured at all: it is a subtraction residual, arithmetically correct, containing about a third of things that are neither Hillcrest nor demand.

Chapter 5 introduces nothing and criticizes what the other four built. Its centrepiece is a division nobody performed for four chapters — two numbers already on the page, which turn out to imply about five times a plausible household's water use, and whose reconciliation reveals an option the entire analysis had no way to express.

Chapter 5 ends by pointing at a list of open questions that Part I had no way to answer — including one, alive since Chapter 2, about which of two mechanisms is starving a hilltop zone. Chapter 6 answers it. It asks you to write a probability down before it has taught you anything, then shows that one afternoon's test moves the case from roughly two-to-one to either ten-to-one or one-to-three, using a single multiplication. It is also where the book, after five chapters of refusing notation, takes one small announced exception.

Chapter 7 is where six chapters of deferred promises come due. It takes the 91% Chapter 6 arrived at and shows that it does not support the sentence everybody wants to write next — *so replace the pump* — then works out what would have to be true for any available evidence to support it. Its centrepiece is four numbers from the utility's own records that yield three different answers, the first of which points the wrong way, and a single fact about the age of a pipe that quietly disqualifies all three.

Chapter 8 begins by repairing a defect the book itself created. Chapter 6 needed a spread on demand, supplied one, and told you in terms that it was justified by nothing; Chapter 8 goes and gets the twelve years of records. What comes back is not what most readers expect — admitting more uncertainty moves the answer in the reassuring direction, correcting one thing turns out worse than correcting neither, and the same twenty-four records support four defensible analyses that agree on the answer and disagree on the verdict.

Chapter 9 closes Part II by putting five reports on one desk — the utility's own record, a neighbour's study, an industry benchmark of 1,400 zones, a manufacturer's rig test, and a panel of engineers — and showing that four defensible ways of combining them give answers spanning a factor of five, with the most principled-sounding rule handing 96% of the weight to the worst source. Then it asks the harder half of its own question: whether any of the five speaks to a hilltop zone with a sixty-eight-year-old pipe. None does, and the reason turns out to be a fact Chapter 7 had already found from the other direction.

Chapter 10 opens Part III on a one-page committee paper of the kind every organisation produces: two options, a stated objective, a recommendation. Neither of the two things wrong with it will be questioned in the room — there are only two options, and the stated objective cannot be used to choose between them. By the end the paper has become three testable objectives, seven alternatives that needed no new data, two of four constraints dissolved, and five affected parties nobody asked. One of the seven alternatives turns out to be an act this book already proposed twice, for entirely different reasons.

Chapter 11 closes the longest thread in the book. The pump test was named in Chapter 2, confirmed obtainable in Chapter 5, and computed in Chapter 6 as moving belief from roughly two-to-one to either ten-to-one or one-to-three. Chapter 11 asks what it is worth to the decision the utility actually faces, and the answer is **£2,300 against a cost of £8,000** — with a further line of arithmetic showing that no study of the question, however good, could be worth more than £12,400. Every one of the earlier chapters was right; the test is exactly as informative as Chapter 6 said. Informative and valuable turn out to be different things.

Chapter 12 closes Part III by widening the frame from one zone to fifteen. Seven schemes, one envelope, and the standard method — rank by benefit per pound and fund down the list — produces a programme that falls seventy household-events a year short of the best available and leaves £460,000 that nothing on the list can absorb. Then the chapter asks what the envelope itself is worth, and finds that an extra £50,000 buys three household-events while an extra £200,000 buys ninety-eight. It ends where the book's central forecast has been heading since Chapter 1: with three futures, no probabilities to weigh them by, and a portfolio that is the best choice in none of them and the one worth defending.

Chapter 13 opens Part IV by closing a loop the first twelve chapters left open. It runs the reservoir forward through a seven-day heatwave and asks a question with an arithmetic answer: demand peaks on day 3, so when does storage bottom out? The answer is day 7, and the four-day gap is the chapter. The utility's nine-year-old operating rule then fires on day 6, delivers on day 8, fails to move the trough by a single megalitre, and spills thirty megalitres of treated water over the weir — not because anybody was careless, but because the rule watches a stock and the loop takes four days. And doing nothing is worse in a way nobody expects: when the weather breaks and the flows re-balance, the reservoir does not refill. It sits at 88 megalitres, below the utility's own critical level, indefinitely, with nothing visibly wrong.

Chapter 14 asks what rule the utility should have had, and the question turns out to change what counts as an answer. Four rules run against five summers, and the utility's own — in force for nine years — is beaten on every single measure by one that differs from it in a single clause. The failure was not writing a bad rule; it was never putting anything beside it. Then the chapter asks two questions nobody in the book has asked: can the utility's instruments tell a heatwave from a burst main, and can its records tell demand from leakage? The answer is no in both cases, and the second is the one worth having — because it follows from the shape of the model rather than from any shortage of data, which means anyone could have worked it out on a napkin in 2014 and nobody did.

Chapter 15 closes Part IV by removing the assumption every earlier chapter made: that the thing being measured does not know it is being measured. In 2019 the regulator attached money to a count of properties below minimum pressure. Over the next three years that count halved — and complaints about low pressure rose. No capital work was done and nothing in the network changed; what changed was where nine of fifteen zones take their reading, in moves that were documented, justified, and entirely within the rules. The chapter's most useful product is a discriminator Chapter 4 asked for and could not supply: records shaped by institutional purpose and records shaped by people responding to being measured look identical from inside a dataset, and the thing that separates them is not a pattern but a date. Its least comfortable finding is that the resulting arrangement is stable, legal, and no better for anybody than the one it replaced.

Chapter 16 opens Part V and adds nothing. It is the first chapter since Chapter 1 with no new machinery and the first whose case is not the water utility — deliberately, because triage of an unfamiliar problem cannot be demonstrated on the most familiar one. It puts two problems in front of the reader: an automated tool that scores housing repairs for urgency, which turns out to need eleven of the book's chapters, and a charity deciding which month to post an appeal, which needs four. The interesting work in both is the negatives, and the chapter's claim is that a reason on a "not material" row is the only thing an omission cannot produce. It also does what the book has been promising since Chapter 1: it works two backward revisions, both triggered by things found late, neither of which means the earlier work was wrong — and it asks the reader to retrieve the first unaided attempt they were told to keep fifteen chapters ago, and not to score it.

Chapter 17 asks the one question nothing else in the book asks: is a thing that was built still working? It operates the adaptive plan Chapter 12 wrote, for four years, and finds that one of its two thresholds was a trigger and the other was a timer — a limb set to fire on a value that had already occurred once in seven baseline years, which over the plan's horizon is about two firings from ordinary weather alone. It fired, once, and nothing happened, because the rule said *or* and the room read *and*; and the arithmetic that would have settled it was four lines on data the utility already held, available since Chapter 8 and never done. Then it turns to Chapter 16's automated tool, where three monitored indicators all looked fine or better — one of them improved *because* of the failure — and establishes the claim the chapter exists for: monitoring observes outputs, so it cannot see failures in what a thing was built to represent. The book ends on the item a NASA standard lists fifth and this book had never mentioned, applied to itself.

Read each manuscript in order rather than skimming. Each opens by asking you to produce something unaided — a first-pass analysis, a representation, a definition, a number — before any of the chapter's vocabulary arrives, and later exercises compare against what you wrote. Skipping that opening costs you the comparison.

Each drafted chapter carries the same four exercise files beside its manuscript — `transfer-form-a.md` and `transfer-form-b.md` (parallel unfamiliar-domain cases), `transfer-rubric.md` (scoring; open it only after you have written your own analysis), and `diagnosis-feedback.md` (the discussion for the diagnosis exercise). The chapter links each one at the moment it is needed. The transfer exercises and their delayed retests only work on material you have not seen, so let the manuscript decide when you open them. Everything else in a chapter directory is authoring and validation scaffolding; some of it discusses the exercises' answers, so if you intend to do the exercises, stay out of it until you have finished the delayed retest.

**To work on the project.** Authority runs `README.md → decisions/ → canon/ → chapter spec.md → working files`; the operating contract is [CLAUDE.md](CLAUDE.md).

- [`decisions/`](decisions/) — settled decisions and their reopening conditions, indexed by scope: three book-level, five governing Chapter 1, and sixteen proposed for Chapters 2–17.
- [`canon/`](canon/) — controlled terminology and registered pedagogical syntheses.
- [`chapters/`](chapters/) — one directory per chapter; `spec.md` is each chapter's contract.
- [`references.bib`](references.bib) and [`sources/`](sources/) — one global bibliography; one note per source, named by citation key.

Chapter 1's directory, still the most developed, shows the kinds of file a chapter accumulates. Chapters 2–17 carry the same kinds, minus the validation instruments and with their research split across separate dossiers rather than a single notes file.

- **Manuscript** — `chapter.md`. The chapter itself; the only file a reader opens directly.
- **Exercise materials** — `transfer-form-a.md`, `transfer-form-b.md`, `transfer-rubric.md`, `diagnosis-feedback.md`. Linked from the manuscript at the moment they are needed.
- **Chapter contract** — `spec.md`. Governed scope, section architecture, and design targets.
- **Authoring controls** — `anchor.md`, `case-data.md`, `decision-framing.md`, `dynamics-response.md`, `learning-sequence.md`, `transfer.md`. Frozen case facts and boundary rules implementing Decisions 0004–0008.
- **Validation instruments** — `freeze-gates.md`, `sme-review-water-anchor.md`, `pilot-protocol.md`, `pilot-data-capture.md`, `validation-handoff.md`. The evidence trail from drafted toward frozen.
- **Research and drafting** — `drafting-blueprint.md`, plus `notes.md` in Chapter 1 and `readiness-audit.md`, `research-plan.md`, and numbered `research-0N-*.md` dossiers in Chapters 2–17.

## Current State

Last reviewed 2026-08-18.

- The 5-part, 17-chapter architecture is frozen for drafting ([Decision 0001](decisions/0001-book-architecture-freeze.md)).
- **Chapter 1 is fully drafted** and awaiting external validation: before it can be frozen, its water-utility anchor case needs a human subject-matter-expert review and its exercise design needs reader-pilot data ([freeze gates](chapters/01-decisions-questions/freeze-gates.md); gates 1–3 open).
- **All seventeen chapters are drafted.** Chapters 2–17 rest on specifications and terminology blocks that remain **provisional**: Decisions [0009](decisions/0009-chapter2-representation-terminology-and-boundary.md), [0010](decisions/0010-chapter3-measurement-terminology-and-boundary.md), [0011](decisions/0011-chapter4-observation-process-terminology-and-boundary.md), [0012](decisions/0012-chapter5-criticism-terminology-and-boundary.md), [0013](decisions/0013-chapter6-probability-terminology-and-notation.md), [0014](decisions/0014-chapter7-identification-terminology-and-notation.md), [0015](decisions/0015-chapter8-estimation-terminology-and-notation.md), [0016](decisions/0016-chapter9-synthesis-terminology-and-boundary.md), [0017](decisions/0017-chapter10-values-terminology-and-boundary.md), [0018](decisions/0018-chapter11-decision-terminology-and-boundary.md), [0019](decisions/0019-chapter12-optimization-terminology-and-boundary.md), [0020](decisions/0020-chapter13-dynamics-terminology-and-boundary.md), [0021](decisions/0021-chapter14-sequential-control-terminology-and-boundary.md), [0022](decisions/0022-chapter15-strategic-terminology-and-boundary.md), [0023](decisions/0023-chapter16-integration-terminology-and-boundary.md), and [0024](decisions/0024-chapter17-deployment-terminology-and-boundary.md) propose those chapters' controlled vocabulary, scope boundaries, and example architecture, and none has been author-adjudicated.
- **The book's longest thread now closes on a negative result.** [Decision 0018](decisions/0018-chapter11-decision-terminology-and-boundary.md) clause 1.3 records that the pump test's value was computed and checked rather than arranged, and clause 4.4 records the closest the book has come to a fifth instance of the demonstrate-because-unsourced disposition — no source was obtained for risk attitude, and the chapter declines to teach the practice rather than teaching it unsourced.
- **Two governing documents disagree about where trade-offs live.** [Decision 0006](decisions/0006-chapter1-decision-framing-boundary.md) assigns trade-off structure to Chapter 10; this file's Chapter 11 block assigns trade-offs and value of information there. [Decision 0017](decisions/0017-chapter10-values-terminology-and-boundary.md) clause 5 resolves it in favour of this file, which the authority order makes controlling, and records that 0006 would need amending to match. **That amendment has not been made.**
- **A book-level question is now four instances deep.** Decisions 0009, 0011, and 0012 each taught a practice by demonstration because no source was obtained for it, and `decisions/README.md` recorded the standing instruction that a fourth instance should reopen research rather than invoke precedent. [Decision 0016](decisions/0016-chapter9-synthesis-terminology-and-boundary.md) clause 6 is the fourth, and refers it to the author rather than resolving it.
- **Chapter 13 is the first chapter whose scope arrived pre-adjudicated.** [Decision 0007](decisions/0007-chapter1-dynamics-and-response-boundary.md) is **Accepted** and set Chapter 13's boundary in advance while Chapter 1 was being written; [Decision 0020](decisions/0020-chapter13-dynamics-terminology-and-boundary.md) mostly reports it rather than proposing it, and marks the four clauses that go beyond it. It is also the first chapter to justify its own difficulty from a measurement rather than an assertion, using an instrument administered to graduate students, and the first to apply Chapter 8's discipline about threshold verdicts to one of the book's own sources.
- **The last two scheduled terminology debts are paid, and one unscheduled one is now alone.** [Decision 0021](decisions/0021-chapter14-sequential-control-terminology-and-boundary.md) closes `observability` and `structural identifiability`, both `TODO` in `canon/terminology.md` since Chapter 1. **Two of its clauses need author attention**: clause 6 registers `practical identifiability`, which `README.md`'s Chapter 14 core competence does not name, and clause 8 records that `structural identifiability` is closed from a review because the 1970 paper that named it could not be obtained — the first time a registry entry has been closed from a secondary source. The chapter also announces the book's **sixth** terminology collision and its first with four senses: four things are now called identifiability or identification.
- **A registry entry assigned to a drafted chapter was never closed.** `canon/terminology.md` records `utility` as introduced in Chapter 11, and Chapter 11 did not define it — consistent with [Decision 0018](decisions/0018-chapter11-decision-terminology-and-boundary.md) clause 4.4, which declined to teach risk attitude for want of a source, but the registry still carries a closure that did not happen. Surfaced by Decision 0020 clause 12.4 and **not repaired**. After Chapter 14 it is the only `TODO` left in the registry.
- **Chapter 12 declined to add a fifth instance, and says so.** [Decision 0019](decisions/0019-chapter12-optimization-terminology-and-boundary.md) clause 1 records that three sources were obtained in full before drafting specifically so that nothing in the chapter would be taught by demonstration for want of a source, and that the count of instances therefore stays at four. It adds no notation, leaving the sequence where 0018 left it.
- **The book is drafted and nothing is validated.** Seventeen manuscripts exist; **no pilot data exists for any exercise in any of them**, Gate 1 has been open since Chapter 1 and is now fourteen chapters deep, and sixteen decision records remain unadjudicated. Chapter 17 §8 states all of this to the reader on the book's last page rather than closing on a summary.
- **Chapter 17 declines machinery its own governed block permits.** [Decision 0024](decisions/0024-chapter17-deployment-terminology-and-boundary.md) clause 2 records that the Chapter 17 entry is the only chapter block in the book with permissive phrasing — control-chart reasoning "where appropriate" — and that the chapter takes the distinction and refuses the technique. **Clause 6 registers `tampering`, named in the governed core competence, with no source for the name**; the mechanism it names is sourced at Chapter 13, so the record states plainly that this is not a new demonstrate-because-unsourced instance.
- **One registry entry closes with the book still open.** `utility` was surfaced as unclosed in Chapter 13's research and carried forward four times; **Chapter 17 is the last chapter, so there is no later chapter to close it in.**
- **Chapter 16 is the first chapter since Chapter 1 that adds no machinery, and the first whose case is not the water anchor.** [Decision 0023](decisions/0023-chapter16-integration-terminology-and-boundary.md) records three things that need attention: the chapter's **research base is the smallest since Chapter 1**, deliberately, and the manuscript says so to the reader (clause 4); the **bounded pagination exception proposed at [Decision 0022](decisions/0022-chapter15-strategic-terminology-and-boundary.md) clause 8 is applied a second time**, and falls with it if declined (clause 6); and the chapter's **central empirical warrant is an author's one-page retrospective rather than the study it describes**, the primary paper being unobtainable (clause 7). It also discharges four structural promises Chapter 1 made about itself, including the comparison against the reader's preserved first attempt.
- **Chapter 15 rests on more borrowed authority than any other chapter, and says so.** [Decision 0022](decisions/0022-chapter15-strategic-terminology-and-boundary.md) clause 7 records that **Goodhart (1975), Campbell (1979), and Lucas (1976) are all named in the governed core competence and none could be obtained**; two are quoted through a single reporting source and the third is not quoted at all. Clause 8 proposes a **bounded exception to the pagination rule** for a source that carries no page numbers, and clause 11.1a flags a second term registered outside a governed competence, after Chapter 14's.
- **A fifth demonstrate-because-unsourced instance is a live question, and the standing instruction was followed.** [Decision 0022](decisions/0022-chapter15-strategic-terminology-and-boundary.md) clause 9 records that `principal-agent` and `information asymmetry` are named in governed text with **no source obtained**, that research was reopened rather than precedent invoked, that four attempts across three routes failed, and that the question is **referred to the author**. It differs from the first four instances in one respect the author should weigh: there the disposition was adopted without a documented search, and here the search happened and is on record.
- **The notation question is open in five places.** [Decision 0013](decisions/0013-chapter6-probability-terminology-and-notation.md) clause 2 permits the conditioning bar and odds; [Decision 0014](decisions/0014-chapter7-identification-terminology-and-notation.md) clause 2 extends it with `do(·)` and inline arrows; [Decision 0015](decisions/0015-chapter8-estimation-terminology-and-notation.md) clause 2 **declines** to extend further, which departs from a promise Chapter 6 made to the reader in its own text; [Decision 0018](decisions/0018-chapter11-decision-terminology-and-boundary.md) clause 4 then extends it again with a decision table and one inline tree; [Decision 0022](decisions/0022-chapter15-strategic-terminology-and-boundary.md) clause 5 extends it a fourth time with a two-player payoff table, the first extension in four chapters. Decisions 0019, 0020, and 0021 add nothing. All five are announced in the manuscripts, **none has been adjudicated**, and they have to be settled in order.
- **No chapter remains as a skeleton spec.** The drafting phase of the book is complete; validation has not begun.

| Part | Ch. | Chapter and central question | Status |
|---|---:|---|---|
| I | 1 | **[Decisions, Questions, and a First Complete Pass](chapters/01-decisions-questions/chapter.md)**<br>What is being asked, for what use, and what would count as an adequate answer? | **Drafted** — [in validation](chapters/01-decisions-questions/freeze-gates.md) |
| I | 2 | **[Representation, Mechanisms, and Scale](chapters/02-representation-mechanisms/chapter.md)**<br>What is inside the model, at what grain, and how do parts produce behavior? | **Drafted** — [decision pending](decisions/0009-chapter2-representation-terminology-and-boundary.md) |
| I | 3 | **[Measurement and Operationalization](chapters/03-measurement-operationalization/chapter.md)**<br>What do the numbers stand for, and how well? | **Drafted** — [decision pending](decisions/0010-chapter3-measurement-terminology-and-boundary.md) |
| I | 4 | **[Observation Processes and Data Provenance](chapters/04-observation-provenance/chapter.md)**<br>Why did these records, and not others, come to exist in this form? | **Drafted** — [decision pending](decisions/0011-chapter4-observation-process-terminology-and-boundary.md) |
| I | 5 | **[Assumptions, Adequacy, and Rival Models](chapters/05-assumptions-rival-models/chapter.md)**<br>How could this formulation fail its purpose, and what would show it? | **Drafted** — [decision pending](decisions/0012-chapter5-criticism-terminology-and-boundary.md) |
| II | 6 | **[Probability, Prediction, and Simulation](chapters/06-probability-simulation/chapter.md)**<br>How is uncertainty represented, updated, and scored? | **Drafted** — [decision pending](decisions/0013-chapter6-probability-terminology-and-notation.md) |
| II | 7 | **[Targets, Identification, and Causal Claims](chapters/07-targets-identification/chapter.md)**<br>Could ideal evidence establish the target, and under what assumptions? | **Drafted** — [decision pending](decisions/0014-chapter7-identification-terminology-and-notation.md) |
| II | 8 | **[Estimation, Uncertainty, and Model Checking](chapters/08-estimation-uncertainty/chapter.md)**<br>What does finite evidence say, with what reliability? | **Drafted** — [decision pending](decisions/0015-chapter8-estimation-terminology-and-notation.md) |
| II | 9 | **[Combining and Transporting Evidence](chapters/09-evidence-synthesis/chapter.md)**<br>What do many imperfect sources jointly support — here? | **Drafted** — [decision pending](decisions/0016-chapter9-synthesis-terminology-and-boundary.md) |
| III | 10 | **[Values, Objectives, and Alternatives](chapters/10-values-alternatives/chapter.md)**<br>What matters, to whom, and what options exist beyond those offered? | **Drafted** — [decision pending](decisions/0017-chapter10-values-terminology-and-boundary.md) |
| III | 11 | **[Decisions Under Uncertainty and Value of Information](chapters/11-decisions-voi/chapter.md)**<br>Which act is defensible, and would more evidence change it? | **Drafted** — [decision pending](decisions/0018-chapter11-decision-terminology-and-boundary.md) |
| III | 12 | **[Optimization, Robustness, and Adaptive Plans](chapters/12-optimization-robustness/chapter.md)**<br>How do we choose well at scale when the model itself is uncertain? | **Drafted** — [decision pending](decisions/0019-chapter12-optimization-terminology-and-boundary.md) |
| IV | 13 | **[Dynamics, Feedback, and Stability](chapters/13-dynamics-feedback/chapter.md)**<br>How does the system evolve once acted upon? | **Drafted** — [decision pending](decisions/0020-chapter13-dynamics-terminology-and-boundary.md) |
| IV | 14 | **[Sequential Decisions, Information, and Control](chapters/14-sequential-control/chapter.md)**<br>How should choices be made through time as information arrives? | **Drafted** — [decision pending](decisions/0021-chapter14-sequential-control-terminology-and-boundary.md) |
| IV | 15 | **[Strategic Interaction, Incentives, and Endogenous Response](chapters/15-strategic-interaction/chapter.md)**<br>What changes when the system contains other modelers? | **Drafted** — [decision pending](decisions/0022-chapter15-strategic-terminology-and-boundary.md) |
| V | 16 | **[Integration: The Full Loop on Unfamiliar Problems](chapters/16-integration-full-loop/chapter.md)**<br>Which machinery does this problem need, and how do the pieces connect? | **Drafted** — [decision pending](decisions/0023-chapter16-integration-terminology-and-boundary.md) |
| V | 17 | **[Deployment, Monitoring, and Revision](chapters/17-deployment-monitoring/chapter.md)**<br>Is the deployed reasoning still working — and if not, which stage failed? | **Drafted** — [decision pending](decisions/0024-chapter17-deployment-terminology-and-boundary.md) |

Stages: **spec skeleton** (governed title, question, competence, and targets only) → **in research** (bounded pre-drafting research) → **drafting** → **drafted — in validation** (manuscript complete; external evidence pending) → **frozen**. Update a chapter's row, and the date above, in the same commit that moves the chapter across a stage boundary.

Chapter names link to the manuscript where one exists, otherwise to that chapter's `spec.md`. This table restates governed titles and central questions for orientation; the per-chapter blocks below remain the full architectural record.

## Intellectual Principle

The project does not claim to invent a new scientific discipline or unified formal theory. It is an integrated pedagogical architecture built from established concepts and terminology in fields including:

- scientific modeling;
- measurement science;
- probability;
- statistics;
- causal inference;
- econometrics;
- decision analysis;
- operations research;
- systems analysis;
- system dynamics;
- control theory;
- game theory;
- robust decision-making;
- machine learning evaluation.

Established disciplinary distinctions must be preserved. For example:

- statistical identifiability;
- causal identification;
- structural identifiability;

must remain distinct concepts.

Likewise, the book must not casually collapse:

- construct;
- measure;
- proxy;
- target;
- estimand;
- estimator;
- estimate;
- prediction;
- intervention;
- utility;
- objective;
- metric;
- robustness;
- stability;
- equilibrium;
- observability.

Pedagogical syntheses are allowed, but must be identified as pedagogical syntheses rather than presented as established formal theories.

## Book Architecture

The current architecture contains **5 parts** and **17 chapters**, at approximately:

- 500 body pages;
- 100 serious learning hours.

The intellectual progression is:

```text
Frame and Formulate
        ↓
Learn from Evidence
        ↓
Choose
        ↓
Act in Responsive Systems
        ↓
Integrate and Revise
        ↺
```

The sequence is a teaching order, not a claim that real reasoning is a one-directional pipeline. In practice, later evidence, decisions, deployment outcomes, and failures may require returning to any earlier stage.

## Part I: Frame and Formulate

### Chapter 1: Decisions, Questions, and a First Complete Pass

**Central question.** What is being asked, for what use, and what would count as an adequate answer?

**Core competence.** Frame the decision situation, identify intended use and target, distinguish relevant claim types and environment properties, and perform one informal pass through the complete reasoning process.

### Chapter 2: Representation, Mechanisms, and Scale

**Central question.** What is inside the model, at what grain, and how do parts produce behavior?

**Core competence.** Construct purpose-relative representations using boundaries, entities, variables, states, mechanisms, abstraction, aggregation, scale, and alternative representations.

### Chapter 3: Measurement and Operationalization

**Central question.** What do the numbers stand for, and how well?

**Core competence.** Connect constructs to observables through operationalization, units, proxies, validity, reliability distinctions, and measurement error.

### Chapter 4: Observation Processes and Data Provenance

**Central question.** Why did these records, and not others, come to exist in this form?

**Core competence.** Describe the observation process separately from the process being modeled, including sampling, selection, missingness, censoring, aggregation, reporting, institutional incentives, and possible manipulation.

### Chapter 5: Assumptions, Adequacy, and Rival Models

**Central question.** How could this formulation fail its purpose, and what would show it?

**Core competence.** Criticize models using assumption records, dimensional reasoning, limiting and extreme-condition checks, Fermi estimation and bounding, rival models, structural uncertainty, and predicted failure modes.

## Part II: Learn from Evidence

### Chapter 6: Probability, Prediction, and Simulation

**Central question.** How is uncertainty represented, updated, and scored?

**Core competence.** Use conditioning, Bayes, expectation, base rates, simulation, probabilistic prediction, and calibration to reason coherently under uncertainty.

### Chapter 7: Targets, Identification, and Causal Claims

**Central question.** Could ideal evidence establish the target, and under what assumptions?

**Core competence.** Define targets and estimands, distinguish statistical identifiability from causal identification, distinguish prediction from intervention and counterfactual claims, and understand experiments and observational designs as strategies for identification.

Structural identifiability is deferred to the dynamic-systems part of the book.

### Chapter 8: Estimation, Uncertainty, and Model Checking

**Central question.** What does finite evidence say, with what reliability?

**Core competence.** Use likelihood, estimation, regression, uncertainty quantification, predictive evaluation, measurement-error reasoning, analytic-flexibility awareness, and model checking without reducing evidence to threshold rituals.

### Chapter 9: Combining and Transporting Evidence

**Central question.** What do many imperfect sources jointly support — here?

**Core competence.** Reason about heterogeneous and dependent evidence, replication, evidence synthesis, expert judgment, external validity, generalizability, target populations, and transportability at an appropriate conceptual level.

## Part III: Choose

### Chapter 10: Values, Objectives, and Alternatives

**Central question.** What matters, to whom, and what options exist beyond those offered?

**Core competence.** Structure values and consequences, distinguish values from measurable objectives and metrics, identify stakeholders and constraints, and generate alternatives instead of accepting a fixed option set.

### Chapter 11: Decisions Under Uncertainty and Value of Information

**Central question.** Which act is defensible, and would more evidence change it?

**Core competence.** Use decision trees, expected utility, risk attitudes, sensitivity analysis, value of information, decision-quality reasoning, ambiguity awareness, and recognition of when further analysis itself is not worthwhile.

### Chapter 12: Optimization, Robustness, and Adaptive Plans

**Central question.** How do we choose well at scale when the model itself is uncertain?

**Core competence.** Formulate objectives and constraints, reason marginally, understand shadow-price and convexity intuition, and use scenarios, robustness, regret, adaptive plans, and computational solver handoff appropriately.

## Part IV: Act in Responsive Systems

### Chapter 13: Dynamics, Feedback, and Stability

**Central question.** How does the system evolve once acted upon?

**Core competence.** Reason about state, accumulation, stocks and flows, delay, feedback, equilibrium versus stability, oscillation, overshoot, and policy resistance.

### Chapter 14: Sequential Decisions, Information, and Control

**Central question.** How should choices be made through time as information arrives?

**Core competence.** Reason with policies rather than one-shot actions, feedback decisions, observability, structural identifiability, information acquisition, exploration versus exploitation, and control at a foundational conceptual level.

Formal dynamic programming, filtering, LQR, MPC, POMDP, and reinforcement-learning algorithms belong in the depth curriculum.

### Chapter 15: Strategic Interaction, Incentives, and Endogenous Response

**Central question.** What changes when the system contains other modelers?

**Core competence.** Reason about strategic dependence, incentives, equilibrium as consistency, commitment, information asymmetry, principal-agent relationships, delegation, endogenous response, metric gaming, Goodhart-type failures, Campbell's law, Lucas critique, and manipulation of evidence.

## Part V: Integrate and Revise

### Chapter 16: Integration: The Full Loop on Unfamiliar Problems

**Central question.** Which machinery does this problem need, and how do the pieces connect?

**Core competence.** Triage unfamiliar problems and execute the relevant reasoning process across formulation, evidence, decision, dynamics, and strategy without mechanically forcing every problem through every chapter.

This chapter should eventually contain full-loop cases, including at least one substantial automated or AI system case. AI is an application and stress test, not a separate intellectual foundation of the book.

### Chapter 17: Deployment, Monitoring, and Revision

**Central question.** Is the deployed reasoning still working — and if not, which stage failed?

**Core competence.** Design monitoring, distinguish signal from ordinary variation, recognize drift and tampering, diagnose failure by stage, define revision triggers, and return deliberately to earlier parts of the reasoning process.

Concept-level monitoring machinery may include common-cause versus special-cause variation and control-chart reasoning where appropriate.

## The Reasoning Loop

The book should repeatedly reinforce the following general pattern:

```text
Purpose / Decision
  ↓
Target and Context
  ↓
Representation
  ↓
Measurement
  ↓
Observation Process
  ↓
Assumptions and Adequacy
  ↓
Probability
  ↓
Identification
  ↓
Estimation
  ↓
Evidence Synthesis and Transport
  ↓
Values and Alternatives
  ↓
Decision
  ↓
Optimization / Robust Choice
  ↓
Dynamics
  ↓
Sequential Decision / Control
  ↓
Strategic Response
  ↓
Deployment
  ↓
Monitoring
  ↓
Revision
  ↺
```

This is a pedagogical navigation structure, not a new formal theory, and not a strict one-directional dependency graph. Real reasoning is iterative: a result discovered late in the process may invalidate an earlier representation, measurement, assumption, objective, or evidence claim, and later findings may send the reasoner back to any earlier stage. Targets themselves may be revised after representation, measurement, evidence, or deployment.

## Scope Boundary

The core book should teach readers to:

- recognize which machinery is required;
- understand why it is required;
- execute foundational versions of it;
- interpret its outputs;
- understand major assumptions and failure modes;
- know when deeper specialist methods are needed.

The book should not attempt full technical coverage of:

- measure-theoretic probability;
- advanced statistical asymptotics;
- advanced Bayesian computation;
- full psychometrics;
- formal do-calculus;
- detailed quasi-experimental estimators;
- advanced transportability algorithms;
- mathematical robust optimization;
- LP and KKT algorithms;
- stochastic dynamic programming;
- POMDP algorithms;
- reinforcement-learning algorithms;
- Kalman filtering;
- LQR or MPC;
- formal control design;
- mechanism design;
- equilibrium refinements.

Those belong in the companion depth curriculum.

## Development Principle

Every chapter should eventually distinguish among:

1. **established concepts and terminology;**
2. **pedagogical synthesis used by this book;**
3. **specialist material intentionally deferred.**

The manuscript should favor:

- production over recognition;
- worked examples followed by fading;
- prediction before explanation where pedagogically appropriate;
- self-explanation;
- contrasting cases;
- analogical transfer;
- error diagnosis;
- revision of earlier work;
- cold-transfer assessment.

Reading completion alone is not mastery.

## Current Freeze Status

Treat this architecture as the working baseline for manuscript development. Do not casually restructure parts or chapters during drafting.

The architecture should only be reopened for a genuine structural reason; the reopening conditions are recorded in [Decision 0001](decisions/0001-book-architecture-freeze.md).

Ordinary drafting difficulties should lead to chapter revision, not immediate architecture redesign.

## Governance

- `README.md` is the architectural source of truth for the book: parts, chapters, sequence, and freeze status. Chapter titles, central questions, and core competences must remain synchronized between this file and each chapter's `spec.md`; conflicts are surfaced, not silently resolved.
- The operating contract — authority order, intellectual rules, source discipline, writing conventions — is [CLAUDE.md](CLAUDE.md).
- Architectural change goes through a decision record in [`decisions/`](decisions/), never through silent edits here; each record carries its own reopening conditions.
- The manuscript must conform to [`canon/`](canon/): introducing or varying a term requires an entry in the terminology registry, and pedagogical syntheses must be labeled as such rather than presented as established theory.
- Repository structure and the citation system are settled by [Decision 0002](decisions/0002-repository-architecture.md) and [Decision 0003](decisions/0003-citation-and-source-note-system.md); new top-level systems require demonstrated need.
