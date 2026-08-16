# Source Note: perdomo2020performative

## Citation

Juan Perdomo, Tijana Zrnic, Celestine Mendler-Dünner, and Moritz Hardt. 2020. “Performative Prediction.” *Proceedings of the 37th International Conference on Machine Learning*, Proceedings of Machine Learning Research 119: 7599–7609.

## Verification

Verified against the official PMLR publication page and its supplied BibTeX/metadata.

Verified metadata:
- Proceedings of the 37th International Conference on Machine Learning;
- PMLR volume 119;
- pages 7599–7609;
- year 2020.

The inspected abstract states that predictions used to support decisions can influence the outcomes they aim to predict and that ignoring this interaction can appear as distribution shift. The paper formalizes performative prediction and includes strategic feedback effects.

## Role in Chapter 1

This source supports the Chapter 1 deployment warning:

A prediction, model, metric, rule, or policy can become part of the process after deployment. If decisions or behavior respond to it, the future data-generating environment may differ from the historical environment used to construct or evaluate the analysis.

This is particularly relevant to the water-supply anchor, where a conservation action can change demand and therefore invalidate a forecast that assumed unchanged behavior.

## Cautions

- `performative prediction` is a field-specific term and is not required Chapter 1 vocabulary.
- Do not label every distribution shift performative; environmental, technological, population, measurement, and other changes can also alter distributions.
- The book generalizes the deployment warning beyond machine learning as a pedagogical synthesis; formal strategic and performative analysis remains Chapter 15.
