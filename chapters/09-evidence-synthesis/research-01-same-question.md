# Research 01 — Are the Sources About the Same Thing?

Cluster R01 of `research-plan.md`. Closed.

Sources read directly: `bareinboim2016fusion` printed pp. 7345, 7350, 7352.

## 1. The problem has a name

The framing this chapter needs is stated in the abstract of a PNAS colloquium paper:

> "we address the problem of data fusion—piecing together multiple datasets collected under heterogeneous conditions (i.e., different populations, regimes, and sampling methods) to obtain valid answers to queries of interest." [@bareinboim2016fusion, p. 7345]

**Three kinds of heterogeneity, named on the page:** different populations, different regimes, different sampling methods. Not different noise levels — different circumstances of production.

The same abstract states both halves of the opportunity:

> "The availability of multiple heterogeneous datasets presents new opportunities to big data analysts, because the knowledge that can be acquired from combined data would not be possible from any individual source alone. However, the biases that emerge in heterogeneous environments require new analytical tools." [@bareinboim2016fusion, p. 7345]

**Both sentences are load-bearing and the chapter must carry both.** Combining is genuinely more powerful than any single source. And it introduces biases that no single source has.

## 2. The claim the paper opens with

> "The exponential growth of electronically accessible information has led some to conjecture that data alone can replace substantive knowledge in practical decision making and scientific explorations. In this paper, we argue that traditional scientific methodologies that have been successful in the natural and biomedical sciences would still be necessary for big data applications" [@bareinboim2016fusion, p. 7345]

That is the same structural claim Chapter 7 took from `pearl2009causal` p. 99 — that a conclusion of a certain kind requires an assumption the data cannot supply — arriving in the setting of many datasets rather than one.

## 3. Design is part of what a dataset is

The paper names a feature it calls essential:

> "One unique feature of the SCM framework, essential in big data applications, is the ability to encode mathematically the method by which data are acquired, often referred to generically as the 'design.' This sensibility to design, which we can label proverbially as 'not all data are created equal'" [@bareinboim2016fusion, p. 7345]

**"Not all data are created equal" is the chapter's usable slogan and it is the source's own.**

The book has been building to it for five chapters. Chapter 4 asked how records came to exist. Chapter 7 asked how treatment was allocated. Chapter 8 asked how the analysis was conducted. This chapter asks the same question of five sources at once, and the paper supplies the vocabulary for treating the answer as part of the data rather than as context around it.

## 4. Three biases, distinguished

The paper separates biases that are usually run together:

> "The problems represented in these archetypal examples are known as confounding bias (Fig. 1, tasks 1 and 2), sample selection bias (Fig. 1, task 3), and transportability bias (Fig. 1, task 4)." [@bareinboim2016fusion, p. 7345]

Mapped onto what this book has already taught:

| The paper's term | Where the book met it |
|---|---|
| confounding bias | Chapter 7 §§4–5 |
| sample selection bias | Chapter 4, and Chapter 7's positivity |
| **transportability bias** | **new here** |

**Only the third is new**, which is the argument for a 28-page chapter rather than a 40-page one. Two of the three failures a reader will meet when combining sources are failures they can already diagnose.

## 5. Before any weighting: the same-question test

Nothing in the sources tells you when two numbers may be combined. The book already has the apparatus, from Chapter 7.

An estimand has attributes: treatment, comparison, population, variable, handling of intervening events, and a summary. **Two sources are about the same quantity when those attributes match, and about different quantities when they do not** — and the second is the ordinary case.

**This is the book's own application of Chapter 7's material and is labelled as such.** Neither source states it. What the sources supply is that heterogeneity in populations, regimes, and sampling methods is the general problem [@bareinboim2016fusion, p. 7345]; the attribute-by-attribute test is how this book proposes to make that operational for a reader with five reports on a desk.

The consequence for the manuscript's ordering is firm: **§2 comes before §3.** Asking how to weight five numbers before asking whether they are about one quantity is the error the chapter exists to prevent, and putting the weighting section first would commit it structurally.

## 6. Stop condition

Met. The data-fusion framing is recorded verbatim with locators; the design point and the three-bias separation are recorded; the same-question test is stated as the book's own extension of Chapter 7 and labelled.

Not read: `bareinboim2016fusion` pp. 7346–7349, 7351, which develop the formal machinery. The chapter uses none of it.
