# Source note: `meng2018paradox`

## Citation

Meng, Xiao-Li. 2018. "Statistical Paradises and Paradoxes in Big Data (I): Law of Large Populations, Big Data Paradox, and the 2016 US Presidential Election." *The Annals of Applied Statistics* 12 (2): 685–726. DOI 10.1214/18-AOAS1161SF.

## Verification status

Verified direct source. The published article was inspected. Its first page prints *The Annals of Applied Statistics*, 2018, Vol. 12, No. 2, 685–726, the DOI, and the Institute of Mathematical Statistics imprint. Received December 2017; revised April 2018. Author affiliation: Harvard University.

Printed pages 685–687 were read in full. Later pages, including the derivations in §2 and the election analysis in §4, were **not** inspected in this pass.

## Role in Chapter 4

This is Chapter 4's spine source. It supplies, from a rigorous statistical argument, the chapter's central and least intuitive claim: **a larger dataset does not protect you against a selection defect — it amplifies it.**

It also gives Chapter 4 the same structural lesson Chapter 3 took from metrology, in a different currency: there is a quantity that more data improves, and a quantity that more data does not, and the second is usually the one that decides your answer.

## Verified locators

- p. 685, abstract, the framing question: "Which one should I trust more: a 1% survey with 60% response rate or a self-reported administrative dataset covering 80% of the population?"
- p. 685, abstract, the identity: "A 5-element Euler-formula-like identity shows that for any dataset of size *n*, probabilistic or not, the difference between the sample average X̄ₙ and the population average X̄_N is the product of three terms: (1) a *data quality* measure, ρ_{R,X}, the correlation between X_j and the response/recording indicator R_j; (2) a *data quantity* measure, √((N−n)/n), where N is the population size; and (3) a *problem difficulty* measure, σ_X, the standard deviation of X."
- p. 685, insight (I): "Probabilistic sampling ensures high data quality by controlling ρ_{R,X} at the level of N^{−1/2}".
- p. 685, insight (II): "When we lose this control, the impact of N is no longer canceled by ρ_{R,X}, leading to a *Law of Large Populations* (LLP), that is, our estimation error, relative to the benchmarking rate 1/√n, increases with √N".
- p. 685, insight (III): "the 'bigness' of such Big Data (for population inferences) should be measured by the *relative size* f = n/N, not the *absolute size* n".
- p. 685, insight (IV): "When combining data sources for population inferences, those relatively tiny but higher quality ones should be given far more weights than suggested by their sizes."
- p. 685, the 2016 result: estimates from the CCES "suggest a ρ_{R,X} ≈ −0.005 for self-reporting to vote for Donald Trump. Because of LLP, this seemingly minuscule data defect correlation implies that the simple sample proportion of the self-reported voting preference for Trump from 1% of the US eligible voters, that is, n ≈ 2,300,000, has the same mean squared error as the corresponding sample proportion from a genuine simple random sample of size n ≈ 400, a 99.98% reduction of sample size (and hence our confidence)."
- p. 686, the paradox: "The CCES data demonstrate LLP vividly: on average, the larger the state's voter populations, the further away the actual Trump vote shares from the usual 95% confidence intervals based on the sample proportions. This should remind us that, without taking data quality into account, population inferences with Big Data are subject to a *Big Data Paradox*: the more the data, the surer we fool ourselves."
- p. 687, the proposed shift: from "Standard Error ∝ σ/√n" to "Relative Bias ∝ ρ√N". "Here 'Relative Bias' is the bias in the sample mean relative to a benchmarking standard error, σ and n are standard deviation and sample size, and N is the long forgotten *population size*. The unfamiliar term ρ is a *data defect correlation*, defined in this paper."
- p. 687, origin: the project "started when I was asked to help with statistical quality control by an agency. Among the first questions was 'Which one should we trust more, a 5% survey sample or an 80% administrative dataset?', which led to the development of the *data defect index*".
- p. 685, key words include: data defect correlation, data defect index (d.d.i.), data quality-quantity tradeoff, non-response bias.

## Chapter 4 use and cautions

**Chapter 4 uses the structural lesson, not the mathematics.** The identity, the derivation of the Law of Large Populations, and the data defect index are Chapter 8 and depth-curriculum material. What Chapter 4 takes is: error depends on a *correlation between being recorded and the value*, and that term is not reduced by collecting more records.

**Do not state the identity as a formula in Chapter 4.** Doing so would import notation the chapter has no room to develop.

**Do not say "big data is bad".** The paper's claim is conditional: *without taking data quality into account*, big-data population inferences are subject to the paradox. A large dataset with ρ near zero is excellent.

**Do not attribute the 400-equivalent figure to any dataset other than the CCES 2016 self-reported Trump preference.** It is a specific empirical estimate, not a general rule about surveys.

**ρ ≈ −0.005 is a data defect *correlation*, not a bias, a rate, or a percentage.** Describing it loosely as "half a percent of bias" would misstate the source.

**The insight labels (I)–(IV) are the author's own numbering in the abstract**, not this book's.

Chapter 4 does not import the Euler-identity analogy, the Monte Carlo application, or the data-confidentiality discussion.

Pages beyond 687 were not read; the manuscript may not cite them.
