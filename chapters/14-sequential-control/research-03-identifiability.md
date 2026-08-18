# Research 03: Structural and Practical Identifiability

Cluster 3 of four. Every locator below was taken from reading the document directly.

**This dossier closes a `TODO` that has stood in `canon/terminology.md` since Chapter 1**, and it opens a term the architecture did not anticipate.

## 1. What could not be obtained

The term originates with **Bellman and Åström (1970), "On structural identifiability", *Mathematical Biosciences* 7:329–339**, confirmed from `astrom2008feedback`'s own bibliography at printed p. 378.

**It could not be obtained.** No route to a copy with checkable pagination was found. The chapter therefore teaches the concept from a 2021 review, which is a weaker position than the book prefers and is stated as such in the manuscript and in `../../decisions/0021`.

## 2. The distinction, which is the whole of §5

`wieland2021identifiability` p. 61:

> "Concerning identifiability, one distinguishes between structural identifiability dealing with inherently indeterminable parameters because of the model structure itself, and practical identifiability, dealing with insufficiently informative measurements to determine the parameters with adequate precision."

**One sentence, two concepts, and the difference is what more data can fix.**

**Structural** — the model structure itself makes the parameter indeterminable. More data does not help. No quantity of perfect measurements helps.

**Practical** — the measurements you have are not informative enough. More data, or better data, can help.

**This is the sentence the chapter is built on**, and it survives extraction cleanly with no symbols.

## 3. Structural identifiability

`wieland2021identifiability` p. 61:

> "A model is structurally identifiable if a unique parameterization exists for any given model output."

And the mechanism of failure, on the same page. The source's sentence carries parameter symbols, so the operative clause is quoted and the rest paraphrased: a parameter is structurally non-identifiable when changing it need not alter the model's trajectory, **"because the changes can be fully compensated by altering other parameters."**

**That clause is the diagnostic.** If two parameters can trade off against each other with no visible consequence, they are not separately determinable, and no experiment of the kind you are running will separate them.

Same page, on the consequence:

> "A structurally nonidentifiable parameter implies the existence of a manifold in parameter space upon which the trajectory y is unchanged."

Contains a symbol; paraphrase — there is a whole surface of parameter values that all produce exactly the same predictions.

**And the source connects it to §4's concept explicitly.** Its section heading is "Definition of structural identifiability and connection to observability", and it observes that on that surface the model's internal variables can change without the observations changing — "This is denoted as nonobservability."

**So the two ideas Chapter 14 owns are two faces of one thing**, which is why they belong in one chapter and why the book has been right to hold both here.

## 4. Practical identifiability

`wieland2021identifiability` p. 63:

> "we consider a combination of model and data as practically identifiable if the confidence intervals of all estimated parameters are of finite size"

**Note the object.** Not the model. A *combination of model and data*. Practical identifiability is a property of a pairing, exactly as observability is a property of a system-plus-instruments pairing and validity is a property of an interpretation.

**And note what this makes of Chapter 8.** Chapter 8 computed an interval of `+0.84 to +2.76` from twenty-four events. That was a practical-identifiability finding in everything but name: the interval was finite, so the quantity was practically identifiable, and the chapter's whole discussion of what the interval did and did not cover was a discussion of how nearly it failed to be.

The source also records that the field is unsettled here, p. 60:

> "Practical nonidentifiability, on the other hand, has not been investigated at the same conceptually clear level."

**Quote it.** A chapter that presents four crisp identifiabilities without saying that one of them is contested would be misrepresenting the state of the field.

## 5. The repair, and it is a decision

`wieland2021identifiability` p. 64, on what to do when predictions are not precise enough:

> "one has two principal options to tailor the model complexity to the information content of the data: (1) measure additional data, corresponding to an increase of the dimension of the observation function g in Equation (2) or (2) reduce the model complexity according to the available data, corresponding to a decrease of the dimension of the parameter space"

**Measure more, or model less.**

**This is the chapter's practical payoff** and it is a decision in Chapter 10's sense — an alternative set with two members, one of which nobody proposes. Organisations reach for the first and rarely consider the second, and the second is often cheaper and always faster.

**And Chapter 4 found the utility had already taken the second option without noticing.** Its demand figure is production minus metered consumption, which is a model with the leakage parameter removed by fiat. That is option (2), taken silently, and its consequence — a figure containing about a third of things that are neither Hillcrest nor demand — is what happens when you reduce model complexity without recording that you did.

## 6. Cautions

**Written for systems biology.** Every example in the source is a cell-signalling model. The book applies the structural/practical distinction across domains, and that widening is the book's own pedagogical synthesis.

**A review, not a primary source.** See §1.

**The profile-likelihood machinery at pp. 62–64 is the source's principal contribution and is not taught.** The Fisher-information critique at pp. 63–64 was read and is not used; it would require Chapter 8 to have taught estimation theory it declined to teach.

**The source's own framing is normative about modelling practice** — "bad, good, and useful models" at p. 60 — and the book does not adopt it.

## 7. The four-way collision

The book now has four terms sharing one adjective, three of them already registered.

| Term | Question | Home |
|---|---|---|
| `statistical identifiability` | Can the parameter be determined from the distribution the data come from? | Chapter 7 |
| `causal identification` | Can the causal effect be determined from available data plus stated assumptions? | Chapter 7 |
| `structural identifiability` | Can the model's parameters be determined from its input-output behaviour, in principle? | **Chapter 14** |
| `practical identifiability` | Can they be determined from the data actually in hand, with adequate precision? | **Chapter 14** |

**`../../decisions/0014` clause 3 registered the first three as a three-way distinction and reserved the third for here.** The fourth is new and is not named in `README.md`'s Chapter 14 block; its registration is flagged for author review.

**Recommendation: one table, once, and a standing instruction that no chapter add a fifth sense.**

## 8. What the chapter takes

| Claim | Locator |
|---|---|
| Structural versus practical, and what more data can fix | p. 61 |
| A model is structurally identifiable if a unique parameterization exists for any given output | p. 61 |
| Non-identifiability means changes can be fully compensated by other parameters | p. 61 |
| The connection to observability | p. 61 |
| Practical identifiability is a property of model **and** data | p. 63 |
| Practical nonidentifiability is less conceptually settled | p. 60 |
| Measure more, or model less | p. 64 |
