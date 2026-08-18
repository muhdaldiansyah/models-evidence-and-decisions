# Source note: `bareinboim2016fusion`

## Bibliographic record

Bareinboim, Elias, and Judea Pearl. 2016. "Causal Inference and the Data-Fusion Problem." *Proceedings of the National Academy of Sciences* 113(27): 7345–7352. DOI 10.1073/pnas.1510507113.

An Arthur M. Sackler Colloquium paper. Edited by Richard M. Shiffrin; approved 15 March 2016; received for review 29 June 2015.

Read from the authors' reprint, issued as UCLA Technical Report R-450 (July 2016). **That reprint carries the published PNAS pagination — 7345 through 7352 — printed on its pages**, and the locators below are published page numbers, checked against the running footers.

## Verification status

Read directly at printed pp. 7345, 7350, and 7352. **Pages 7346–7349 and 7351 were not read**; they develop the formal machinery — do-calculus derivations, selection diagrams, the S-backdoor criterion, and the transport formulas — none of which this book uses or characterises.

## A companion paper, obtained and declined

The standard transportability reference is Pearl and Bareinboim, "External Validity: From do-calculus to Transportability across Populations", *Statistical Science*.

It was obtained, as UCLA Technical Report R-400 (last revised May 2014, marked "Forthcoming, Statistical Science"). **It carries no printed page numbers at all** — its pages are stamped only with a LaTeX build footer.

**It is therefore not cited anywhere in this book**, under the rule recorded at `../chapters/09-evidence-synthesis/research-plan.md`: cite the version whose pagination you can see. This is a declined source rather than an unobtainable one, and the distinction is recorded so that a later reader does not assume it was unavailable.

## Verified locators

- **p. 7345**, abstract: "we address the problem of data fusion—piecing together multiple datasets collected under heterogeneous conditions (i.e., different populations, regimes, and sampling methods) to obtain valid answers to queries of interest."
- **p. 7345**, abstract: "The availability of multiple heterogeneous datasets presents new opportunities to big data analysts, because the knowledge that can be acquired from combined data would not be possible from any individual source alone. However, the biases that emerge in heterogeneous environments require new analytical tools."
- **p. 7345**, opening: "The exponential growth of electronically accessible information has led some to conjecture that data alone can replace substantive knowledge in practical decision making and scientific explorations. In this paper, we argue that traditional scientific methodologies that have been successful in the natural and biomedical sciences would still be necessary for big data applications".
- **p. 7345**: "One unique feature of the SCM framework, essential in big data applications, is the ability to encode mathematically the method by which data are acquired, often referred to generically as the 'design.' This sensibility to design, which we can label proverbially as 'not all data are created equal'".
- **p. 7345**: "The problems represented in these archetypal examples are known as confounding bias (Fig. 1, tasks 1 and 2), sample selection bias (Fig. 1, task 3), and transportability bias (Fig. 1, task 4)."
- **p. 7350**: transportability "lies at the heart of every scientific investigation because, invariably, experiments performed in one environment are intended to be used elsewhere, where conditions are likely to be different."
- **p. 7350**: "This disparity is indeed a major threat to the validity of randomized trials. Because participation cannot be mandated, we cannot guarantee that the study population would be the same as the population of interest."
- **p. 7350**: study populations "may consist of volunteers, who respond to financial and medical incentives offered by pharmaceutical firms or experimental teams, so the distribution of outcomes in the study may differ substantially from the distribution of outcomes under the policy of interest."
- **p. 7352**, conclusion: the framework aims to "combine datasets collected under heterogeneous conditions so as to synthesize consistent estimates of causal effects in a target population."

## Role in Chapter 9

- supplies the name and framing of the general problem — data fusion — with its three kinds of heterogeneity;
- supplies both halves of the position: combining is more powerful than any single source, **and** introduces biases no single source has;
- supplies "not all data are created equal" and the treatment of design as part of what a dataset is;
- separates confounding, sample selection, and transportability bias, of which only the third is new to this book;
- supplies the second tradition's statement that results do not travel by default, agreeing with `deaton2016rct` p. 28 from a different method.

## Cautions

**None of the formal machinery is used.** Selection diagrams, the S-backdoor criterion, and the transport formulas are on pages this book did not read and would require the graphical apparatus Chapter 7 declined.

**Do not present the paper as claiming the problems are solved for practitioners.** Its conclusion says two problems "can thus be considered 'solved'" in the sense of having a complete formal characterisation, which is a mathematical claim and not a statement that a reader can apply it to five reports on a desk.

**Do not use the paper to argue against large datasets.** Its argument is that heterogeneous sources need analytical tools, not that they should be distrusted.

**"Not all data are created equal" is the authors' phrase**, offered by them as a proverbial label. Quote it as theirs.
