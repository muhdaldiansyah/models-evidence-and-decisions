# Chapter 12 Transfer Design

Status: drafting control. Governs `transfer-form-a.md`, `transfer-form-b.md`, and `transfer-rubric.md`.

Provisional in the same sense as `spec.md`: built on proposed `../../decisions/0019-chapter12-optimization-terminology-and-boundary.md`.

## Transfer target

Per `spec.md`:

> Given a portfolio decision under a binding budget, several candidate schemes including one that is phaseable, and three futures with different benefits, produce the marginal ranking and say where it fails, compute what the budget constraint is worth, build a regret table, identify a robust portfolio, and turn it into an adaptive plan with named signposts.

## The changed task shape

Chapter 11 asked for a recommendation among three acts, under two states, with a probability supplied.

**Chapter 12 asks for a recommendation among many portfolios, under three futures, with no probabilities at all.**

That is the largest single jump in task size the book makes, and it is deliberate. Both of Part IV's chapters end in a recommendation; what changes between them is that Chapter 12's cannot be reached by taking an expectation, because there is nothing to take an expectation over.

**The recommendation is still required.** Chapter 10 forbade one, Chapter 11 required one, and Chapter 12 requires one under worse conditions. A reader who declines to recommend because the probabilities are missing has learned the wrong thing from §6.

## Form design

Both forms supply the same eight things, in the same order:

1. **A programme of seven candidate schemes**, one of which is very cheap with a high ratio.
2. **A large scheme available in two mutually exclusive versions** — a phase and a full build.
3. **A binding budget**, set by a process outside the programme.
4. **A benefit column** under the organisation's central forecast, openly monetising several things.
5. **Three futures**, one of which makes the large scheme nearly worthless.
6. **A stated staging premium** for building the second phase later.
7. **Eight produce items** plus a four-sentence recommendation.
8. **No probabilities anywhere**, and no invitation to supply any.

| | Form A | Form B |
|---|---|---|
| Domain | Port and harbour infrastructure | Health system diagnostic capacity |
| Budget | **£3,600k** | **£4,200k** |
| Benefit unit | vessel delay-hours avoided per year | diagnostic episodes completed in target time per year |
| Phaseable scheme | channel deepening, U1 / U2 | imaging centre, N1 / N2 |
| Collapsing future | feeder shift | community shift |
| Ranking's answer | **P+Q+U1+R = 1,270**, £840k unspent | **H+J+K+N1 = 1,490**, £940k unspent |
| Forecast optimum | **P+Q+U2 = 1,560**, spend £3,380k | **H+J+N2 = 1,830**, spend £3,950k |
| Ranking misses by | **290** | **340** |
| Third future's optimum | Q+R+S+T = 1,680 | H+K+L+M = 1,760 |
| Minimax-regret portfolio | **P+R+S+U1**, max regret **560** | **H+K+L+N1**, max regret **520** |
| Optimal in how many futures | **none** | **none** |
| Ranking's portfolio, max regret | 590 | 550 |
| Forecast optimum, max regret | 970 | 890 |
| Cost of robustness if forecast right | **260** (16.7%) | **310** (16.9%) |
| Staging premium | **£150k** | **£170k** |

All figures computed and checked by enumerating every feasible portfolio before the forms were written.

### The three structural features, and why each is there

**The very cheap scheme with the high ratio** (P, H) is in every future's optimum and every robust portfolio. It is there so that a reader who concludes *ranking is useless* is immediately wrong: the ranking gets the first item right in every case, and the chapter's claim is narrower than that.

**The phaseable scheme** is what makes §7 possible. Without a scheme that can be half-built, an adaptive plan has nothing to defer, and "adaptive" collapses into "we will review it".

**The future that makes the large scheme nearly worthless** is what makes robustness cost something. If every future rewarded the deepening, the robust portfolio and the forecast optimum would coincide and the reader would learn nothing.

### The central inversion

**In the chapter, the ranking's portfolio spends £460k less than the envelope and misses by 70. In both forms it misses by more — 290 and 340 — and strands more money.**

This is not a different lesson; it is the same lesson at a size where it is harder to dismiss as an artefact of small numbers. A reader who thought the chapter's example had been rigged should find the forms uncomfortable.

**And in both forms the minimax-regret portfolio contains the phase rather than the full build**, which is the structural reason robustness and adaptivity are the same subject rather than two.

### Deliberate difficulty features

**The ranking's answer looks fine.** Four schemes, funded in ratio order, each individually justified, money left over that reads as prudence. Nothing about it announces a problem, and item 3 is where the reader has to go and look.

**The two versions of the large scheme sit adjacent in the ratio ranking** — U1 at 0.431 and U2 at 0.411 in Form A, N1 at 0.421 and N2 at 0.406 in Form B. A reader who takes the higher-ratio version without asking what the leftover money can buy has made exactly the error §3 describes, and the ratios are close enough that the choice feels like a rounding decision.

**The shadow price is zero at the increment most readers will test.** Both forms leave slack — £220k in A, £250k in B — so an extra £100k buys nothing, and the reader who reports *the budget is not binding* has drawn a large conclusion from one probe. The lesson lands only if they test more than one increment.

**Cutting the budget is asymmetric, and the first cut is free.** In both forms a £200k cut costs nothing and a £300k cut costs a great deal. Readers who assume symmetry get both directions wrong.

**Item 7 asks for a signpost with a threshold and a measurement.** Answers that name a review date instead are the expected failure, and the chapter's fifth planted defect is the same error.

**Item 8 asks for value judgments in a column presented as engineering or clinical output.** Nothing flags them.

### Domain exclusions

Every previously used transfer or contrast domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time, city pothole records, food bank client records, household waste recycling centres, clinic appointment reminders, light-van fleet maintenance, social-landlord damp reporting, manufacturing machine guarding, city bus corridors, electricity distribution, charity fundraising, hospital estates, banking risk, higher education, food manufacturing, rail infrastructure, retail loss prevention.

Port and harbour infrastructure is new.

**One judgment recorded.** Form B is set in a health system, and three earlier forms have used health or care settings — emergency department waiting time (Chapter 4), clinic appointment reminders (Chapter 7), hospital estates (Chapter 10). None is a capital programme, none shares an actor or a question with this one, and this form asks about allocating a multi-year capital envelope across diagnostic services. Flagged rather than left for a reader to notice.

**Neither domain is sensitive** in the sense `spec.md` uses. Form A is commercial throughput. Form B concerns waiting times for diagnostic tests, and the form takes no position on any health system's policy; every scheme in it increases capacity, and the question is which combination.

## What a strong Form A answer should notice

- **The ranking is P, Q, U1, U2, R, S, T** — and U2 is unreachable once U1 is taken.
- **Funding down the list gives P+Q+U1+R = 1,270 and strands £840k**, which no remaining scheme can absorb.
- **The best affordable portfolio is P+Q+U2 = 1,560**, and the difference is 290.
- **The reason**: U1 has the better ratio and the worse consequence. Taking it leaves £1,720k, and the best the remaining list can do with that is R at 300 — while the £1,500k more that U2 costs buys 590.
- **An extra £100k buys nothing; an extra £200k buys 40; an extra £660k buys 300.** The zero is about the increment, not about the envelope.
- **A £200k cut costs nothing and a £300k cut costs 260.** The £220k of slack absorbs the first; the second forces Q out of the portfolio.
- **Regrets**: P+Q+U2 → 970; Q+R+S+T → 1,380; P+R+S+U1 → **560**; the ranking's P+Q+R+U1 → 590.
- **P+R+S+U1 is optimal in no future**, which is the point rather than an objection.
- **Robustness costs 260 of 1,560 if the forecast is right** — about a sixth.
- **The adaptive plan defers the second deepening phase**, names a draught or call-mix threshold with a stated measurement, and prices the £150k premium against what the deferral protects.
- **The value judgments** are in the delay-hour: what an hour of vessel delay is worth, whose delay counts, and the horizon over which benefits are summed.

## What a strong Form B answer should notice

- **The ranking is H, J, N1, N2, K, L, M.**
- **Funding down the list gives H+J+K+N1 = 1,490 and strands £940k.**
- **The best affordable portfolio is H+J+N2 = 1,830**, a difference of 340.
- **An extra £100k buys nothing; an extra £200k buys 40; an extra £790k buys 340.**
- **A £200k cut costs nothing and a £300k cut costs 210.**
- **Regrets**: H+J+N2 → 890; H+K+L+M → 1,700; H+K+L+N1 → **520**; the ranking's H+J+K+N1 → 550.
- **H+K+L+N1 is optimal in no future.**
- **Robustness costs 310 of 1,830 if the forecast is right.**
- **The adaptive plan defers the second scanner**, names a referral-volume or case-mix threshold with a stated measurement, and prices the £170k premium.
- **The value judgments** are in the episode count: an episode counts as one whether it changes management or not, the three services are treated as interchangeable, and the horizon is chosen.
- **A reader may object that the three futures are not exhaustive** — a workforce constraint would make every capacity scheme worth less, and it is on none of them. That is correct and should be credited.

## Parallelism check

| Feature | Form A | Form B | Matched |
|---|---|---|---|
| Schemes | 7 | 7 | ✓ |
| Cheap high-ratio scheme | ✓ P | ✓ H | ✓ |
| Phaseable scheme | ✓ U1 / U2 | ✓ N1 / N2 | ✓ |
| Futures | 3 | 3 | ✓ |
| Futures with distinct optima | 2 | 2 | ✓ |
| Ranking misses optimum | ✓ by 290 | ✓ by 340 | ✓ |
| Money stranded by ranking | £840k | £940k | ✓ |
| Shadow price at +£100k | 0 | 0 | ✓ |
| First £200k of cuts | free | free | ✓ |
| Minimax optimal in no future | ✓ | ✓ | ✓ |
| Cost of robustness | 16.7% | 16.9% | ✓ |
| Staging premium | £150k | £170k | ✓ |
| Produce items | 8 + recommendation | 8 + recommendation | ✓ |
| Word count | comparable | comparable | ✓ |

Arithmetic for both forms was computed and checked by full enumeration before the forms were written; the values in `transfer-rubric.md` are the checked values.

## Rubric-to-item mapping

| Rubric dimension | Produce item |
|---|---|
| The ranking | 1 |
| Funding down the list | 2 |
| Where the ranking fails, and why | 3 |
| The constraint priced, in both directions | 4 |
| The regret table | 5 |
| The robust portfolio, and what it costs | 6 |
| The adaptive plan and its signpost | 7 |
| Value judgments named | 8 |

**Every dimension has a dedicated item**, as in Chapters 10 and 11.

## Pilot notes

Untested. Five things a pilot should measure.

**Time.** 50 minutes for eight items, of which three require enumeration rather than a formula. This is the most search the book has asked for and may not fit; if it does not, the fix is to cut the scheme list from seven to six rather than to drop item 5.

**Whether readers actually search for the optimum in item 3**, or reason from the ranking that it must be close. Reasoning from the ranking is the failure the chapter exists to prevent, and item 3 is the only place it can be observed.

**Whether the zero shadow price is over-read.** If readers report *the budget is not binding* after one probe, §4 did not land and the fix is to state the multiple-increment rule earlier.

**Whether signposts have thresholds.** If most answers name a review date, the chapter's §7 distinction is too subtle and needs a worked negative example rather than a stated one.

**Whether readers object to the three futures.** An answer that accepts them without comment has missed that scenario sets are chosen, which §6 states plainly. A pilot in which nobody objects means the point needs to be a produce item rather than a paragraph.
