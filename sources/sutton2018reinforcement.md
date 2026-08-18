# Source Note: sutton2018reinforcement

## Citation

Richard S. Sutton and Andrew G. Barto. 2018. *Reinforcement Learning: An Introduction*, second edition. Cambridge, MA: MIT Press.

## Verification

**Obtained in full and read directly.** The publisher-licensed PDF was used; the title page reads "Reinforcement Learning: An Introduction, second edition, Richard S. Sutton and Andrew G. Barto, The MIT Press", with the copyright line "© 2018, 2020 Richard S. Sutton and Andrew G. Barto" and a Creative Commons Attribution-NonCommercial-NoDerivs licence.

Printed page numbers appear in the running heads on even pages. **Printed page equals PDF page minus 22**, calibrated against the head on printed p. 2.

Read at pp. 2–3, 25–28, and 58 — five pages of roughly 550.

## Role in Chapter 14

This is the book's source for `policy` and for the exploration–exploitation trade.

`README.md`'s Chapter 14 block excludes "reinforcement-learning algorithms" from the core book, so this source is read for its **problem statements and its definitions** and not for any of its methods.

## Verified locators

- p. 2: "We formalize the problem of reinforcement learning using ideas from dynamical systems theory, specifically, as the optimal control of incompletely-known Markov decision processes."
- p. 2: "In particular, the distinction between problems and solution methods is very important in reinforcement learning; failing to make this distinction is the source of many confusions."
- p. 3: "The dilemma is that neither exploration nor exploitation can be pursued exclusively without failing at the task."
- p. 3: "The agent must try a variety of actions and progressively favor those that appear to be best."
- p. 3: "On a stochastic task, each action must be tried many times to gain a reliable estimate of its expected reward."
- p. 3: "The exploration–exploitation dilemma has been intensively studied by mathematicians for many decades, yet remains unresolved."
- p. 25: "The most important feature distinguishing reinforcement learning from other types of learning is that it uses training information that evaluates the actions taken rather than instructs by giving correct actions."
- p. 25: "Purely evaluative feedback indicates how good the action taken was, but not whether it was the best or the worst action possible. Purely instructive feedback, on the other hand, indicates the correct action to take, independently of the action actually taken."
- p. 26, the k-armed bandit's name: the problem is "so named by analogy to a slot machine, or 'one-armed bandit,' except that it has k levers instead of one."
- p. 26: "When you select one of these actions, we say that you are exploiting your current knowledge of the values of the actions. If instead you select one of the nongreedy actions, then we say you are exploring, because this enables you to improve your estimate of the nongreedy action's value."
- p. 26: "Exploitation is the right thing to do to maximize the expected reward on the one step, but exploration may produce the greater total reward in the long run."
- p. 26: "Reward is lower in the short run, during exploration, but higher in the long run because after you have discovered the better actions, you can exploit them many times."
- p. 27: "However, most of these methods make strong assumptions about stationarity and prior knowledge that are either violated or impossible to verify in most applications and in the full reinforcement learning problem that we consider in subsequent chapters. The guarantees of optimality or bounded loss for these methods are of little comfort when the assumptions of their theory do not apply."
- p. 27: "In this book we do not worry about balancing exploration and exploitation in a sophisticated way; we worry only about balancing them at all."
- p. 58: "Accordingly, value functions are defined with respect to particular ways of acting, called policies."
- p. 58: "Formally, a policy is a mapping from states to probabilities of selecting each possible action."
- p. 58: "Reinforcement learning methods specify how the agent's policy is changed as a result of its experience."

## Cautions

- **Extraction hazard, recorded because it cost quotations.** The typesetting renders `ff` as a ligature that extracts as a stray character: *trade-off* becomes *trade-o↵*, *different* becomes *di↵erent*, *effective* becomes *e↵ective*. The substitution is deterministic and unambiguous, but under the standing rule adopted in Chapters 7 and 8 the book quotes only prose that survives extraction cleanly. **No quotation taken from this source contains an `ff`.** The sentence at p. 3 that names the exploration–exploitation trade-off is one of the casualties and is paraphrased in the manuscript, with the paraphrase declared.
- **Five pages of about 550 were read.** Nothing is claimed about reinforcement learning as a field beyond what those pages state.
- **No algorithm, value function, return, discount factor, Bellman equation, or MDP formalism is taken**, all of which are developed on the pages read. `README.md` excludes them.
- **The book's own depth choice at p. 27 is quoted and followed at one further remove**: Chapter 14 does not balance exploration and exploitation at all, it establishes that the trade exists.
- Do not present this source as recommending anything about water utilities, or about decision-making outside its own subject.
