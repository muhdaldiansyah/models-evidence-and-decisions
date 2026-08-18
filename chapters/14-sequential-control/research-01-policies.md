# Research 01: Policies, and Comparing Rules Rather Than Actions

Cluster 1 of four. Every locator below was taken from reading the document directly.

**Extraction note.** `sutton2018reinforcement` typesets `ff` as a ligature that extracts as a stray character. No quotation below contains one; where a good sentence did, it is paraphrased and the paraphrase is declared.

## 1. The definition

`sutton2018reinforcement` p. 58, in the section headed *Policies and Value Functions*:

> "Accordingly, value functions are defined with respect to particular ways of acting, called policies."

And formally, on the same page:

> "Formally, a policy is a mapping from states to probabilities of selecting each possible action."

**Two things the chapter must draw out of that sentence.**

**A policy is a mapping, not a sequence.** It says what to do *given what you see*, so it produces different actions on different histories. A plan says what to do on days one through seven; a policy says what to do whenever the reservoir is below 150.

**The domain is states.** A policy can only use what is available to it — which is why §4's observability question is not a separate topic but the immediate next question about any policy.

Same page, on what learning does:

> "Reinforcement learning methods specify how the agent's policy is changed as a result of its experience."

**Useful as a boundary marker.** The book teaches what a policy is and how to compare two of them. It does not teach any method for changing one automatically, and `README.md` excludes the algorithms that do.

## 2. Where the formalism begins, and where the book stops

`sutton2018reinforcement` p. 2:

> "We formalize the problem of reinforcement learning using ideas from dynamical systems theory, specifically, as the optimal control of incompletely-known Markov decision processes."

**Read this as a map of what Chapter 14 is adjacent to and does not enter.** Optimal control, Markov decision processes, and the whole apparatus of value functions and Bellman equations sit one page beyond every idea this chapter uses.

Same page, a distinction the book should borrow:

> "In particular, the distinction between problems and solution methods is very important in reinforcement learning; failing to make this distinction is the source of many confusions."

**Chapter 14 teaches the problem and not the solution methods**, and it should say so in those words, because a reader who meets the field later will otherwise assume the book withheld something.

## 3. Evaluative versus instructive feedback

`sutton2018reinforcement` p. 25 opens the bandit chapter with a distinction that is worth more to this book than the bandit formalism it introduces:

> "The most important feature distinguishing reinforcement learning from other types of learning is that it uses training information that evaluates the actions taken rather than instructs by giving correct actions."

> "Purely evaluative feedback indicates how good the action taken was, but not whether it was the best or the worst action possible. Purely instructive feedback, on the other hand, indicates the correct action to take, independently of the action actually taken."

**This is the reason a rule cannot be judged from one history**, stated more precisely than the book could state it unaided. The utility's nine summers under one rule tell it how that rule did. They do not tell it what a different rule would have done, because nothing in the record is instructive.

**And it connects backwards.** Chapter 6 scored forecasts against outcomes — evaluative. Chapter 8's four defensible analyses agreed in direction and disagreed in verdict — evaluative. The book has been working with evaluative feedback throughout and has not had the word.

## 4. What the source does not claim

`sutton2018reinforcement` p. 27, on the methods it is about to teach:

> "However, most of these methods make strong assumptions about stationarity and prior knowledge that are either violated or impossible to verify in most applications and in the full reinforcement learning problem that we consider in subsequent chapters. The guarantees of optimality or bounded loss for these methods are of little comfort when the assumptions of their theory do not apply."

**This is a source disqualifying its own guarantees**, in the register Chapters 5, 7, and 8 spent forty pages establishing, and the chapter should quote it and say so.

Same page, the depth choice:

> "In this book we do not worry about balancing exploration and exploitation in a sophisticated way; we worry only about balancing them at all."

**Chapter 14 takes the same position and should say whose it is.**

## 5. What the chapter takes

| Claim | Locator |
|---|---|
| A policy is a mapping from states to action probabilities | p. 58 |
| Value functions are defined with respect to ways of acting called policies | p. 58 |
| Learning methods specify how a policy changes with experience | p. 58 |
| The formalism is optimal control of incompletely-known MDPs | p. 2 |
| Problems and solution methods must be kept apart | p. 2 |
| Evaluative versus instructive feedback | p. 25 |
| The theory's guarantees rest on assumptions often violated or unverifiable | p. 27 |
| The book's own depth choice: balance them at all | p. 27 |

## 6. What was not taken

- Value functions, returns, discounting, and the Bellman equations, all developed on the pages read.
- The MDP formalism.
- Any algorithm.
- The golf example at p. 61 and the gridworld at p. 60.
