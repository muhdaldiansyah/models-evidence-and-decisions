# Research 04 — Designs, and the Chapter's Own Examples

Cluster R04 of `research-plan.md`. Closed.

Sources read directly: `deaton2016rct` printed pp. 7–11; `hernan2019whatif` printed pp. 25–26, 37–38.

## 1. What randomization actually buys

`deaton2016rct` p. 10 states it, and states what it is not:

> "This was Fisher's innovation: not that randomization balanced other causes between treatments and controls but that, conditional on our caveat above, randomization provides the basis for calculating the size of the error."

And, on the same page:

> "Given the absence of treatment-related post-randomization changes in other causes, randomization yields an unbiased estimate of the ATE in the trial sample as well as a sound method for measuring error of estimation in that sample; therein lies its virtue, not that it yields precise estimates through balance."

The mechanism, p. 9:

> "We do not know the size of this error term, and there is nothing in randomization that limits its size; by chance the randomization in our single trial can over-represent an important excluded cause(s)"

The chapter's usable form: **randomization buys control in expectation, not balance in your trial.** p. 10 names the confusion directly — "There is often confusion between perfect control, on the one hand … and control in expectation on the other, which is what randomization contributes."

### The line most likely to be resisted

`deaton2016rct` p. 10:

> "Randomization is an alternative when we do not know enough, but is generally inferior to good control."

This is a strong claim from a contested source and the manuscript should present it as the authors' position rather than as settled fact. It is useful because it corrects the common ordering in which randomization sits at the top of an evidence hierarchy regardless of what else is available.

## 2. The documented overstatement

§1.2 of `deaton2016rct` is titled "Misunderstandings: claiming too much" and quotes four published sources getting balance wrong. The one the chapter should use, from a jointly issued Inter-American Development Bank and World Bank impact-evaluation manual, quoted at `deaton2016rct` p. 10:

> "We can be confident that our estimated impact constitutes the true impact of the program, since we have eliminated all observed and unobserved factors that might otherwise plausibly explain the difference in outcomes."

And the diagnosis, p. 11:

> "This statement is false, because it confuses actual balance in any single trial with balance in expectation over many (hypothetical) trials."

Then the detail that makes it teachable, p. 11:

> "Note that the statement contains no reference to sample size; we get the truth by virtue of balance, not from a large number of observations."

**This connects directly to Chapter 6 §6 and the connection is worth making.** Chapter 6 established that calibration is a property of a forecaster over a record, and that reading it off a single forecast is a category error. Balance is a property of a randomization procedure over hypothetical replications, and reading it off a single trial is the same category error in a different setting. A reader who has done Chapter 6's forty-briefing table has already met the shape.

**Attribution discipline.** The quotations above are *quoted by* `deaton2016rct`. The manuscript must cite them as reported there and must not cite the underlying manuals directly, none of which were obtained. `hernan2019whatif` and `pearl2009causal` are cited from direct reading; the World Bank manual is not.

## 3. Observational designs as emulation

`hernan2019whatif` p. 26 frames the strategy: "We analyze our data as if treatment had been randomly assigned conditional on measured covariates –though we often know this is at best an approximation."

And p. 37 supplies the question that operationalises it:

> "Therefore 'what randomized experiment are you trying to emulate?' is a key question for causal inference from observational data."

The protocol components, p. 37: "eligibility criteria, interventions (or treatment strategies), outcome, follow-up, causal contrast, and statistical analysis."

The payoff, p. 37:

> "An explicit emulation of the target trial prevents investigators from conducting an oversimplified analysis"

**This is the chapter's most transferable single device**, and it is what the transfer forms should test. A reader who can ask *what experiment are you emulating* and then notice that the emulated experiment is absurd has the chapter's competence.

## 4. Observational evidence is not second-rate by nature

`hernan2019whatif` p. 25 heads this off before the reader concludes that only experiments count:

> "Many scientific studies are not experiments. Much human knowledge is derived from observational studies. Think of evolution, tectonic plates, global warming, or astrophysics. Think of how humans learned that hot coffee may cause burns."

The chapter must carry this. Collapse 9 of the readiness audit — *causal inference requires experiments* — is a real risk in a chapter that spends its length on what can go wrong observationally.

The same page also gives the balancing warning, p. 26: "The best explanation for an association between treatment and outcome in an observational study is not necessarily a causal effect of the treatment on the outcome."

## 5. The anchor: what the case must supply

The causal question follows from Chapter 6 without any new setup. The utility is at about 91% for Mechanism A, and the next sentence writes itself — *so replace the pump*. That sentence is the chapter's subject.

### The observational record

The utility has fifteen pumped zones. Six had duty-pump upgrades over the last twelve years; nine did not. Mean low-pressure complaints per heat event:

| | Zones | Before | After |
|---|---:|---:|---:|
| Upgraded | 6 | **6.8** | **4.1** |
| Not upgraded | 9 | **2.9** | **2.6** |

**Four numbers, three different answers**, all arithmetically correct:

| Comparison | Arithmetic | Result |
|---|---|---|
| Upgraded versus not, after | `4.1 − 2.6` | **+1.5** — upgrades made it *worse* |
| Before and after, upgraded zones | `4.1 − 6.8` | **−2.7** — upgrades helped a great deal |
| Difference in differences | `(4.1 − 6.8) − (2.6 − 2.9)` | **−2.4** — upgrades helped |

Every one of the three is defensible under some assumption and none of the assumptions is stated in the table. That is the demonstration, and it is stronger than a case where the naive answer is merely imprecise: here the first comparison points the **wrong way**.

### Why the cross-section is backwards

The six upgraded zones were the six worst-complaining zones at the time the programme was funded. Assignment was made on the outcome's own past values. Exchangeability fails, visibly, and the failure is not exotic — **selecting the worst cases for treatment is how most real programmes allocate**.

### Why the before-and-after is wrong too

Network-wide complaints fell over the period for a reason unrelated to pumps: a separate mains renewal programme. The non-upgraded zones' fall of **0.3** is the visible trace of it.

### And why the difference in differences is not safe either

DiD requires that the upgraded zones would have moved like the non-upgraded ones had nothing been done. The zones were selected for being extreme, so some of the 2.7 fall is regression to the mean and nothing in the table separates it.

**This matters for the chapter's honesty.** A manuscript that arrived at DiD and stopped would have taught the reader to trust the third number, which is exactly the habit Chapter 5 exists to prevent. The correct verdict is that all three comparisons rest on assumptions and only one of them is nameable and checkable.

### The positivity failure

Hillcrest's feeder main is the oldest in the system at **68 years**. None of the six upgraded zones has a main older than **40**. Two of the nine non-upgraded zones have mains over 60, Hillcrest among them.

So for zones like Hillcrest, the probability of having been upgraded in this record is **zero**. Not small — zero. There is no comparable upgraded case anywhere in the data.

**This is the cleanest positivity failure the book can construct**, because it is structural, stateable in one sentence, and completely invisible in any of the three comparisons above. It also connects backwards: Chapter 4 taught that absence produces no rows to notice.

### The well-definedness failure

"Upgrade the pump" covers four things the utility could actually do:

1. like-for-like replacement at the existing **1.1 ML/day**;
2. a higher-capacity duty pump at **1.5 ML/day**;
3. a second pump in parallel;
4. a variable-speed drive on the existing pump.

The register records all four as *pump upgrade*. They have different costs, different failure modes, and — the point — plausibly different effects. Under Mechanism B, where friction loss in the feeder main is the constraint, pushing more flow through the same old main could make matters **worse**, so options 2 and 3 might have opposite signs to option 4.

This is the anchor's version of `hernan2019whatif` pp. 32–33, reached without importing a medical example.

### The target trial

*Randomly assign pumped zones to upgrade or no upgrade, follow them through the next several heat events, and compare complaint rates.*

Stating it exposes three things at once: there are only fifteen zones; you cannot ethically deny an upgrade to a zone that needs one; and heat events do not arrive on a schedule. The trial is infeasible.

**And the infeasibility is informative rather than defeating.** Writing the protocol tells you exactly which assumption the observational analysis is being asked to carry.

## 6. Prohibitions for the manuscript

- No medical, clinical, or epidemiological example in the body. Both principal sources are epidemiological; their examples stay in the source notes.
- No claim that any of the fifteen-zone numbers is typical of water utilities.
- No claim that DiD is the right answer, or that any of the three comparisons is.
- No estimator, standard error, or interval anywhere.
- No back-door criterion, no d-separation, no do-calculus rules, no propensity scores.
- The World Bank manual quotation is cited **as reported at** `deaton2016rct` p. 10 and never directly.
- `deaton2016rct` must be described as a working paper that states on its cover that it has not been peer-reviewed.

## 7. Stop condition

Met. Randomization's contribution recorded with wording; one documented overstatement recorded as the source presents it; emulation recorded; the anchor's four failures specified numerically and the arithmetic checked.

Not read: `deaton2016rct` beyond printed p. 11 of 70. The chapter makes no claim about its second part, which concerns using trial results and is Chapter 9's territory.
