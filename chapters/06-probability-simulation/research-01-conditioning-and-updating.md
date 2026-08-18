# Research 01 — What a Probability Is: Conditioning and Updating

Status: bounded research dossier. Evidence for author adjudication; **not** an author decision. Written under the no-write boundary in `research-plan.md` §11.

Cluster R01 of `research-plan.md` §4. Research conducted 2026-08-18.

**This dossier is unusual.** Most of its subject matter is mathematics rather than empirical claim, so it contains fewer citations and more adjudication than its predecessors. `research-plan.md` §2 sets the dividing line: a claim about what people do needs a source; a claim about what conditioning does needs a demonstration. This cluster is almost entirely the second kind, and saying so is the honest report rather than an evasion.

## 1. Q1 — What a probability is predicated of

### The recommendation

> **A probability is not a property of an event. It is a property of an event *given stated information*.**

This is the chapter's spine, and it makes Chapter 6 the sixth instance of the book's recurring shape rather than a departure from it.

| Chapter | What is not self-standing | Relative to |
|---|---|---|
| 1 | adequacy | the stated use |
| 2 | representation content | the purpose |
| 3 | validity | the interpretation |
| 4 | trustworthiness | the quantity estimated |
| 5 | how much criticism | what happens if wrong |
| 6 | **a probability** | **the information conditioned on** |

By Chapter 6 the reader has met this five times. The pattern is the book's own observation, not a finding, and Chapter 5 already stated it once — so Chapter 6 should **not** restate the table. It should assume it.

### Why this framing rather than another

It does three things at once, which is rare.

It makes **conditioning the central concept**, rather than Bayes' rule. Bayes then becomes the arithmetic of moving between conditioning sets, which is a much less intimidating thing to introduce.

It **dissolves the frequency objection** before it arrives. "You can't put a probability on a one-off event" assumes probability is a property of the event. Once it is a property of *your information about* the event, the objection loses its grip — Mechanism A either operates or does not, and your probability describes your evidential position, not the pipe.

It makes **stating the conditioning information a required part of stating a probability**, which is the discipline the chapter is actually trying to install.

## 2. Q2 — Frequency and degree of belief

**Recommendation: name the distinction once, then set it aside.**

The book needs both readings and cannot pick one. A coin has a long-run frequency. Mechanism A does not — it either operates or it does not, and there is no sequence of Hillcrests to average over. A chapter that insisted on frequencies could not touch the anchor case; a chapter that insisted on beliefs would be needlessly strange about coins.

The unifying move is the one in §1: in both cases the number is conditional on stated information. Where a long-run frequency is available it is usually the right thing to condition on.

**Caution.** The interpretations debate is genuine, long-running, and unresolved. The chapter should say that it exists, say that this book does not adjudicate it, and move on. Presenting either reading as settled would misrepresent the field.

## 3. Q3 — Why "filtering" is an inadequate account of conditioning

The mechanical shadow of conditioning is: restrict attention to the cases where B holds, and look at how often A holds among them. That is correct arithmetic and a poor account of the concept, for two reasons the chapter should demonstrate rather than assert.

**It has nothing to filter when the event is unique.** There is no set of Hillcrests to restrict.

**It hides the direction problem.** Filtering makes P(A|B) and P(B|A) look like the same operation performed on the same table, which is precisely the confusion the chapter must defeat. A reader who thinks of conditioning as filtering has no natural defence against the inversion error, because filtering does not obviously have a direction.

**Recommended framing:** conditioning changes **what you are taking as given**. That is a statement about the reference position, not about a subset of rows, and it survives the unique-event case.

## 4. Q4 — How to present Bayes

Three candidate presentations were considered.

| Form | Strength | Weakness |
|---|---|---|
| Standard formula with denominator | Complete; matches later reading | The denominator is where readers stall, and it carries no intuition |
| Odds form: **prior odds × likelihood ratio = posterior odds** | One multiplication; makes "how far does this evidence move me" directly visible; no denominator | Requires odds, which some readers must be taught |
| Purely verbal procedure | No mathematics | Cannot answer "how much", which is the chapter's whole question |

**Recommendation: the odds form**, with odds taught in two sentences.

The decisive argument is that Chapter 5 handed this chapter a two-hypothesis problem — Mechanism A versus Mechanism B — and the odds form is exactly the right tool for two hypotheses. The likelihood ratio is then a single number answering the question Chapter 5 could not: *how much would that observation move belief?*

It also makes the chapter's most useful practical result visible: **an observation with a likelihood ratio near 1 is not worth making**, however interesting it sounds. That is the bridge to Chapter 11's value of information, stated without trespassing on it.

## 5. Q5 — The notation question

**This is the chapter's most consequential decision and it cannot be dodged.**

Chapters 1–5 used no notation at all, deliberately and successfully. Chapter 6 cannot fully sustain that. A chapter about conditioning that never writes a conditioning bar must say "the probability of A given that B holds" every time, which is longer, harder to scan, and — the real problem — makes the *asymmetry between the two directions* harder to see rather than easier.

**Recommendation: a minimal, explicitly bounded exception.**

Permitted:

- `P(A | B)` — the conditioning bar, which is the chapter's subject;
- odds written as `3 : 1`;
- ordinary arithmetic.

Not permitted:

- summation, integration, or any calculus;
- distributions written as functions;
- random variables as symbols;
- expectation operators;
- the Bayes formula with its denominator.

The exception should be **announced to the reader** — the book has gone five chapters without notation and readers will notice — with the reason given: this chapter is about a distinction that the notation makes visible and prose obscures.

## 6. Cautions — claims the manuscript must NOT make

1. Do not adjudicate the interpretations debate. Name it, decline it, move on.
2. Do not present conditioning as filtering.
3. Do not imply that conditioning tells you what would happen under an intervention. That is Chapter 7, and `pearl2009causal` already supports the distinction.
4. Do not introduce `likelihood` as a technical term. Chapter 8 owns its estimation sense; Chapter 6 needs only "how expected is this observation, under each hypothesis".
5. Do not present expectation as a decision rule. Chapter 11.
6. Do not cite a source for Bayes' rule or for conditioning. They are mathematics; the chapter demonstrates them.
7. Do not let the notation exception expand. It is bounded above and the boundary is the whole point.

## 7. Verdict on the stop condition

`research-plan.md` §4 requires the reader-facing account of what a probability is, and the notation policy settled.

**Met.** Both are proposed in §1 and §5, and both are author decisions rather than findings, which is stated.

## 8. Unresolved author decisions

1. Accept "a probability is relative to the information conditioned on" as the chapter's spine?
2. Accept the bounded notation exception, breaking a five-chapter policy — and is it announced to the reader?
3. Odds form for Bayes, or the standard formula?
4. Is the frequency/belief distinction named at all, or handled entirely by the conditioning framing?
5. Is the five-row pattern table restated here, or assumed from Chapter 5?

Decision 2 is the one to settle first; everything downstream is written differently depending on it.
