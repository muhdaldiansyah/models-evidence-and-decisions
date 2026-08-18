# Source note: `hernan2019whatif`

## Bibliographic record

Hernán, Miguel A., and James M. Robins. *Causal Inference: What If*. Boca Raton: Chapman & Hall/CRC.

**The version read is the freely distributed manuscript dated 10 November 2019**, obtained as a PDF and read directly.

## A pagination warning that must not be lost

**Page numbers cited in this book are those of the 10 November 2019 manuscript version. They do not correspond to the printed Chapman & Hall/CRC edition.**

The authors distribute successive revisions of this text and state that they may revise and correct without documenting changes. Anyone verifying a locator must use the same dated version, and anyone updating this book to a later version must re-verify every locator rather than assume it carried over.

This is recorded prominently because it is the kind of provenance fact that quietly rots. It is exactly the sort of thing Chapter 4 teaches readers to ask about.

## Verification status

Read directly at printed pp. 25–27, 30–33, and 37–38. Table of contents inspected. **Nothing outside those pages has been read, and no claim is made about the rest of the book.**

Mathematical notation is set in italic variables that text extraction drops silently. Every quotation below was checked against its surrounding paragraph and contains no inline mathematics; passages that could not be quoted cleanly are paraphrased and marked as paraphrase.

## Verified locators

### Chapter 3, Observational studies

- **p. 25**, chapter opening: "Many scientific studies are not experiments. Much human knowledge is derived from observational studies. Think of evolution, tectonic plates, global warming, or astrophysics. Think of how humans learned that hot coffee may cause burns."
- **p. 26**: "The best explanation for an association between treatment and outcome in an observational study is not necessarily a causal effect of the treatment on the outcome."
- **p. 26**: "We analyze our data as if treatment had been randomly assigned conditional on measured covariates –though we often know this is at best an approximation."
- **p. 26**, the three conditions, numbered in the source as the conditions under which an observational study can be conceptualized as a conditionally randomized experiment; named on the same page as consistency, exchangeability, and positivity, and collectively as "identifiability conditions or assumptions".
- **p. 26**: "We will see that these conditions are often heroic, which explains why causal inferences from observational studies are viewed with suspicion."
- **p. 26**: "Importantly, in ideal randomized experiments the identifiability conditions hold by design."
- **p. 26**: "Causal inference from observational data requires two elements: data and identifiability conditions."
- **p. 27**, Fine Point 3.1: "We say that an average causal effect is (non parametrically) identifiable under a particular set of assumptions if these assumptions imply that the distribution of the observed data is compatible with a single value of the effect measure. Conversely, we say that an average causal effect is nonidentifiable under the assumptions when the distribution of the observed data is compatible with several values of the effect measure."
- **p. 27**, Fine Point 3.1: "To identify the causal effect in observational studies, we need an assumption external to the data, an identifying assumption."
- **p. 27**, §3.2: in marginally randomized experiments "the treated and the untreated are exchangeable because the treated, had they remained untreated, would have experienced the same average outcome as the untreated did, and vice versa."
- **p. 30**, §3.3: "we must ensure that there is a probability greater than zero–a positive probability–of being assigned to each of the treatment levels. This is the positivity condition."
- **p. 31**, paraphrase: when a covariate value has no untreated units, the data contain no information with which to simulate what would have happened had the treated units been untreated.
- **p. 31**, §3.4: "The apparent simplicity of the consistency condition is deceptive."
- **p. 33**: an obesity treatment has "multiple versions of the treatment" defined by duration, recency, and intensity, and the investigator would need to specify how to intervene; otherwise the causal effect "will be ill-defined".
- **p. 33**: "each of these options may have different effects on mortality even if they are all could somehow set adiposity at the same level" — **quoted as printed; the source contains a typographical error in this sentence.**
- **pp. 37–38**, §3.6: "Therefore 'what randomized experiment are you trying to emulate?' is a key question for causal inference from observational data."
- **p. 37**: the target trial's protocol components — "eligibility criteria, interventions (or treatment strategies), outcome, follow-up, causal contrast, and statistical analysis."
- **p. 37**: "An explicit emulation of the target trial prevents investigators from conducting an oversimplified analysis".

## Role in Chapter 7

- supplies the potential-outcome definition of identifiability (p. 27), which agrees with `pearl2009causal` p. 109 from a different tradition;
- supplies the three identifiability conditions and their names;
- supplies the source's own hedge that the conditions are "often heroic", which the manuscript must carry;
- supplies the design contrast — the conditions hold by design in an ideal experiment;
- supplies the well-defined-intervention problem, which the anchor's four pump options instantiate;
- supplies the target trial as the chapter's most transferable device;
- supplies the defence against concluding that only experiments can establish causes.

## Cautions

**Do not import the source's examples.** Heart transplants and obesity are its running cases; `chapters/07-targets-identification/research-04-designs-and-examples.md` §6 prohibits medical examples in the manuscript body, and the anchor supplies equivalents.

**Do not present the three conditions as a checklist.** The source calls them heroic. A manuscript that lists them as boxes to tick misreports it.

**Do not take the book's Chapter 3 as its whole position.** Only pp. 25–38 were read. The book has three parts and treats models, time-varying treatments, and much else; nothing here characterises any of that.

**Do not attribute the identifiability definition to this source alone.** It appears in a Fine Point, which the book uses for supplementary material, and an equivalent definition appears in `pearl2009causal`. The chapter's claim is that two traditions agree, which requires both.
