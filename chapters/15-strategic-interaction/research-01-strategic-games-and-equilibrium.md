# Research 01: Strategic Games, Strategic Dependence, and Equilibrium as Consistency

Cluster 1 of four. Every locator below was taken from reading the document directly.

**Edition note.** `osborne2004game` is the author-hosted draft of Chapter 2 of *An Introduction to Game Theory* (Oxford University Press, 2004), version dated 2002/7/23. Printed page numbers appear in the running heads and feet; **printed page equals PDF page plus 10**. It is a pre-publication draft posted by the author and the source note says so.

## 1. Strategic dependence

`osborne2004game` p. 11:

> "A STRATEGIC GAME is a model of interacting decision-makers. In recognition of the interaction, we refer to the decision-makers as players."

And the sentence that defines the dependence:

> "The model captures interaction between the players by allowing each player to be affected by the actions of all players, not only her own action."

**That is `strategic dependence` in one clause**, and it is exactly what every chapter before this one assumed away. The reservoir was affected by the utility's action and by nothing else that had an opinion.

The formal object, same page, Definition 11.1:

> "A strategic game (with ordinal preferences) consists of • a set of players • for each player, a set of actions • for each player, preferences over the set of action profiles."

**Three ingredients, and the third is the one that matters here.** Preferences over *profiles* — over the whole list of everybody's actions — not over one's own action alone. A player who preferred only over their own actions would not be in a game.

## 2. Belief, and why it is required

`osborne2004game` p. 19:

> "In a game, the best action for any given player depends, in general, on the other players' actions. So when choosing an action a player must have in mind the actions the other players will choose. That is, she must form a belief about the other players' actions."

**Note what this does to Chapter 11.** Chapter 11's decision-maker faced states of the world with probabilities attached. Here the "states" are other people's choices, and those choices depend on beliefs about your choice.

Where the belief comes from, same page:

> "The assumption underlying the analysis in this chapter and the next two chapters is that each player's belief is derived from her past experience playing the game, and that this experience is sufficiently extensive that she knows how her opponents will behave."

**That is a strong assumption and the source says so.** It is also directly connected to Chapter 14: experience of a repeated interaction is what supplies the belief, and Chapter 14 established how slowly such experience accumulates.

## 3. Equilibrium as consistency

`osborne2004game` p. 20, the two components stated before the definition:

> "First, each player chooses her action according to the model of rational choice, given her belief about the other players' actions. Second, every player's belief about the other players' actions is correct."

**The second component is the whole of `equilibrium as consistency`**, and it is why the governed core competence uses that phrase rather than "equilibrium".

The definition, same page:

> "A Nash equilibrium is an action profile a ∗ with the property that no player i can do better by choosing an action different from a ∗i , given that every other player j adheres to a ∗j ."

**Contains symbols and subscripts**; the manuscript **paraphrases** it and says so: an outcome in which no player could do better by changing their own action alone, given what everybody else is doing.

The steady-state reading, same page:

> "a Nash equilibrium corresponds to a steady state. If, whenever the game is played, the action profile is the same Nash equilibrium... then no player has a reason to choose any action different from her component... there is no pressure on the action profile to change."

> "Expressed differently, a Nash equilibrium embodies a stable 'social norm': if everyone else adheres to it, no individual wishes to deviate from it."

And the phrase the chapter should adopt:

> "For this reason, the condition is sometimes said to be that the players' 'expectations are coordinated'."

## 4. The distinction Chapter 13 requires

`canon/terminology.md`'s `equilibrium` entry records both senses and states that they must not be conflated. Chapter 13 closed the dynamic sense from `astrom2008feedback` p. 100: **a stationary condition for the dynamics**.

**The strategic sense is a different kind of object entirely.**

| | Chapter 13 | Chapter 15 |
|---|---|---|
| What it is a property of | a point in the state space | a profile of actions |
| The condition | the dynamics are stationary there | nobody can do better alone, and beliefs are correct |
| What it says about goodness | nothing | nothing |
| Who has to believe anything | nobody | everybody |

**A pendulum has an equilibrium and has no beliefs.** That is the cleanest available statement of the difference, and it uses the book's own standing counterexample.

## 5. The source's own caution, which the chapter must carry

`osborne2004game` p. 20:

> "The situations to which we wish to apply the theory of Nash equilibrium do not in general correspond exactly to the idealized setting described above. For example, in some cases the players do not have much experience with the game; in others they do not view each play of the game in isolation. Whether or not the notion of Nash equilibrium is appropriate in any given situation is a matter of judgment."

> "Ultimately, the test of the appropriateness of the notion of Nash equilibrium is whether it gives us insights into the problem at hand."

**Fourth time in this book that a source has disqualified its own generality on the page that introduces it** — after `greenland2016misinterpretations`, `deaton2016rct`, and `sutton2018reinforcement` p. 27. The chapter should quote it and note the pattern once.

## 6. Notation

`osborne2004game` p. 19 displays a two-player payoff table — Figure 19.1, a variant of the Stag Hunt — as a two-by-two grid of paired numbers.

**This is a notation question and it is referred to `../../decisions/0022` clause 5.** Chapters 12, 13, and 14 added nothing; Chapter 11's Decision 0018 permits a decision table with one act per row.

## 7. What was not taken

- §§2.2–2.5, the named example games (Prisoner's Dilemma, Bach or Stravinsky, Matching Pennies, Stag Hunt), read only far enough to see the table convention. **None is taught**; the book uses its own case.
- §2.7 onward: examples of equilibrium, best response functions, dominated actions, symmetric equilibria — **unread**.
- Mixed strategies, extensive form, subgame perfection, repeated games, bargaining — not in this chapter of the source and not sought.

## 8. What the chapter takes

| Claim | Locator |
|---|---|
| A strategic game is a model of interacting decision-makers | p. 11 |
| Each player is affected by the actions of all players | p. 11 |
| The three ingredients; preferences over profiles | p. 11 |
| The best action depends on others' actions, so a belief is required | p. 19 |
| Beliefs come from experience of the game | p. 19 |
| The two components: rational choice, and correct beliefs | p. 20 |
| Nash equilibrium, paraphrased | p. 20 |
| Equilibrium as steady state and as stable social norm | p. 20 |
| "Expectations are coordinated" | p. 20 |
| Appropriateness is a matter of judgment | p. 20 |
