# Research 03 — Identification

Cluster R03 of `research-plan.md`. Closed.

Sources read directly: `pearl2009causal` printed pp. 109–110, 113–114, 116–117; `hernan2019whatif` printed pp. 25–27, 30–33.

## 1. Two definitions, two traditions, one idea

### The structural definition

`pearl2009causal` p. 109, Definition 2, attributed there to Pearl (2000a, p. 77), states that a quantity is identifiable given a set of assumptions if any two models satisfying those assumptions that agree on the observable distribution also agree on the quantity.

**A recorded defect in the printed source.** The displayed equation on p. 109 reads `P(M1) = P(M1) ⇒ Q(M1) = Q(M2)`, where the argument requires `P(M1) = P(M2)` in the antecedent. This is a typographical error in the published article; the surrounding prose makes the intended statement unambiguous. **The chapter must quote the prose, not the equation.** Recorded here because a paraphrase assembled from a summary would have reproduced the error invisibly.

The prose restatement on the same page:

> "In words, the details of M1 and M2 do not matter; what matters is that the assumptions in A (e.g., those encoded in the diagram) would constrain the variability of those details in such a way that equality of P's would entail equality of Q's."

### The potential-outcome definition

`hernan2019whatif` p. 27, Fine Point 3.1:

> "We say that an average causal effect is (non parametrically) identifiable under a particular set of assumptions if these assumptions imply that the distribution of the observed data is compatible with a single value of the effect measure. Conversely, we say that an average causal effect is nonidentifiable under the assumptions when the distribution of the observed data is compatible with several values of the effect measure."

### They agree, and the agreement is the teachable form

Both say: **fix the assumptions; ask whether everything you could ever observe pins the answer to one value.** One value, identified. Several values, not.

Two traditions that disagree publicly about frameworks state the central concept compatibly. The chapter can note this, because a reader who later encounters the framework argument should know it is not an argument about what identification means.

**The reader-facing form**, which is the book's phrasing and must be labelled as such:

> If two different states of the world would produce exactly the same data — however much of it you collected — and they give different answers to your question, then no amount of that data can settle your question.

Two things follow immediately and are worth drawing out in the manuscript.

**Identification is settled before any data arrives.** It is a property of the question, the assumptions, and the kind of data — not of the dataset. You can determine it on a whiteboard.

**Identification is relative to assumptions.** There is no such thing as identified full stop. `hernan2019whatif` p. 27 puts it exactly: "To identify the causal effect in observational studies, we need an assumption external to the data, an identifying assumption."

That relativity is the sixth instance of the book's other recurring shape — adequacy relative to use, validity relative to interpretation, trustworthiness relative to quantity, criticism relative to stakes, probability relative to information, and now **identification relative to assumptions**.

## 2. Statistical identifiability versus causal identification

The canon has carried both entries at `Definition status: TODO` since Chapter 1. This cluster closes them.

**Statistical identifiability** asks whether the parameters of a model are determined by the distribution the model implies. Two parameter settings that imply the same distribution are indistinguishable by any amount of data. `pearl2009causal` p. 109 introduces its Definition 2 precisely because the classical notion — "has a unique solution" — "does not directly apply to causal quantities", which tells you the classical notion exists and is about parametric uniqueness.

**Causal identification** asks whether a causal quantity is determined by the observable distribution *together with causal assumptions*. `pearl2009causal` p. 116 states the mechanism for the graphical tradition: the calculus transforms causal quantities "into do-free expressions derivable from P(z, x, y), since only do-free expressions are estimable from non-experimental data. When such a transformation is feasible, we are ensured that the causal quantity is identifiable."

**The line the chapter should teach.** Statistical identifiability is about whether your model has a unique answer given the distribution. Causal identification is about whether a causal quantity has a unique answer given the distribution *plus assumptions that are not in the distribution*. The first can fail because a model is over-parameterised. The second can fail even when every parameter is perfectly estimated.

`README.md` defers **structural identifiability** — whether a dynamic system's parameters can be recovered from its input-output behaviour — to Chapter 14. The chapter names the three-way distinction and hands the third forward.

## 3. The three conditions

`hernan2019whatif` p. 26 gives them as the conditions under which an observational study "can be conceptualized as a conditionally randomized experiment":

> 1. the values of treatment under comparison correspond to well-defined interventions that, in turn, correspond to the versions of treatment in the data
> 2. the conditional probability of receiving every value of treatment, though not decided by the investigators, depends only on measured covariates
> 3. the probability of receiving every value of treatment conditional on [the covariates] is greater than zero, i.e., positive

The same page names them: condition 1 **consistency**, condition 2 **exchangeability**, condition 3 **positivity**, and calls them collectively "identifiability conditions or assumptions".

### The source's own hedge, which the chapter must carry

> "We will see that these conditions are often heroic, which explains why causal inferences from observational studies are viewed with suspicion." [@hernan2019whatif, p. 26]

**Heroic** is the source's word. A chapter that presented the three conditions as a checklist to tick would misreport it.

### And the design contrast

> "Importantly, in ideal randomized experiments the identifiability conditions hold by design." [@hernan2019whatif, p. 26]

This is the sentence that makes §6 of the manuscript possible: a design is a way of making identifying assumptions true rather than assumed.

### The summary line

> "Causal inference from observational data requires two elements: data and identifiability conditions." [@hernan2019whatif, p. 26]

**Two elements.** The chapter should treat that sentence as its thesis.

## 4. Each condition, and what it rules out

**Exchangeability** (pp. 26–27). In a marginally randomized experiment "the treated and the untreated are exchangeable because the treated, had they remained untreated, would have experienced the same average outcome as the untreated did, and vice versa" [@hernan2019whatif, p. 27]. It fails when whatever determined who got treated also bears on the outcome.

**Positivity** (pp. 30–31). "we must ensure that there is a probability greater than zero–a positive probability–of being assigned to each of the treatment levels. This is the positivity condition." [@hernan2019whatif, p. 30]. It fails when some kind of unit never receives one of the treatment levels. The source's intuition, p. 31: if there were no untreated individuals of a given covariate value, "the data would contain no information to simulate what would have happened had all treated individuals been untreated". **Positivity failure is not a small-sample problem.** It is structural, and it is invisible in any summary statistic.

**Consistency** (pp. 31–33). "Consistency means that the observed outcome for every treated individual equals her outcome if she had received treatment" [@hernan2019whatif, p. 31] — and immediately:

> "The apparent simplicity of the consistency condition is deceptive."

The source splits it in two: a precise definition of the counterfactual outcome, and the linkage of counterfactual to observed outcomes. The first half is where the real difficulty lives. p. 33 works it on obesity: there are "multiple versions of the treatment" defined by duration, recency, and intensity, and the investigator "would need to specify how to intervene on body weight" — genetic modification, inactivity with high caloric intake, microbiota replacement, surgery — because "each of these options may have different effects on mortality even if they are all could somehow set adiposity at the same level" [@hernan2019whatif, p. 33; typographical error in the source, quoted as printed].

**Otherwise the effect "will be ill-defined"** [@hernan2019whatif, p. 33].

This is the anchor's pump problem exactly, and the chapter should say so rather than importing the obesity example.

### The naming collision

`consistency` in this sense is unrelated to the statistical sense — an estimator that converges to the estimand as the sample grows — which Chapter 8 will need. Two fields, one word.

Same situation as `calibration` in Chapter 6 and `validation` in Chapter 5. Same handling: announce it once, at the point of use, and record it in `../../decisions/0014`.

## 5. Covariate selection: the caution that overturns common practice

`pearl2009causal` p. 113 introduces the problem: selecting a set of factors such that comparing treated and untreated units with the same values of those factors gives the correct effect. Such a set is called admissible or sufficient. p. 114 records that "The problem of defining an admissible set, let alone finding one, has baffled epidemiologists and social scientists for decades."

The back-door criterion (Definition 3, p. 114) settles it graphically. **The research plan stops here**, because stating the criterion requires blocking, paths, and collision nodes.

What the chapter may carry is the intuition, which p. 114 states in prose:

> "The back-door paths in the diagram carry spurious associations from X to Y, while the paths directed along the arrows from X to Y carry causative associations."

And the practical caution, p. 117, which is the load-bearing finding of this section:

> "the prevailing practice of conditioning on as many pre-treatment measurements as possible should be approached with great caution; some covariates (e.g., Z3 in Fig. 3) may actually increase bias if included in the analysis"

**Controlling for more things can make the answer worse.** The same page records that simulation and parametric analysis by other authors "confirmed the bias-raising potential of certain covariates in propensity-score methods".

The chapter needs this because *control for everything you measured* is the most common applied response to a confounding worry, and it is not safe.

The same page also separates identification from estimation in the source's own words — propensity-score methods "are merely efficient estimators of the right hand side of (25); they cannot be expected to reduce bias in case the set S does not satisfy the back-door criterion" — which is the Chapter 7 / Chapter 8 line stated by the source rather than asserted by the book.

## 6. Not identified is a finding

`pearl2009causal` p. 122 step 4: "Estimate the target quantity if it is identifiable, or approximate it, if it is not." `hernan2019whatif` p. 26 routes non-identification to other approaches with different conditions, naming instrumental variables and deferring them to its own Chapter 16.

The chapter's position, which follows from both and is the book's own formulation:

> A verdict of *not identified* is a result. It says which assumption would have to be added, and it tells you what to go and get.

## 7. Stop condition

Met. Both definitions verbatim; the three conditions with the source's own hedge; the covariate caution with locator; the statistical/causal/structural three-way line settled for canon.

Not read: `pearl2009causal` §§3.3.2 general control of confounding beyond p. 116's framing sentence, §4 potential-outcome framework, §5. `hernan2019whatif` beyond p. 38 except the target-trial pages recorded in R01.
