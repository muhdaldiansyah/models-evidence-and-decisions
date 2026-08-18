# Chapter 17 Cold-Transfer Task — Form A

Allow about **50 minutes**.

Work from this page alone.
Do not open the chapter, either of its cases, the rubric, or Form B.
Every fact you need is here. Do not look anything up.

---

## The situation

A **regional water company** committed in 2022 to a five-year leakage-reduction programme. The programme installed pressure-management controllers on 62 district metered areas, and the controllers adjust inlet pressure automatically against a target set by an algorithm.

**The plan carried a written revision clause**, agreed by the board:

> **Watch.** Average overnight minimum flow across the programme areas, expressed as a percentage rise on the previous year, reported each March. Burst events per quarter in the programme areas, already counted for the regulator.
>
> **If.** The overnight-flow rise exceeds **six per cent** in two consecutive years, **or** burst events exceed **three in any quarter**, the pressure-management algorithm is referred for re-specification at an assumed cost of **£420,000**.
>
> **Owner.** The network strategy manager reports both figures to the asset board each April, whether or not either has triggered.

## The seven years before the programme

**Overnight-flow rise, percentage on the previous year:**

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 |
|---:|---:|---:|---:|---:|---:|---:|
| 3.1 | 2.4 | 4.6 | 1.9 | 3.8 | 2.7 | 4.1 |

**Highest burst count in any quarter of the year:**

| 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 0 | **4** | 1 | 2 | 1 |

## The four years since

| Year | Overnight-flow rise | Highest quarterly burst count | What the April report recorded |
|---|---:|---:|---|
| 2023 | 3.4% | 2 | Neither figure triggered |
| 2024 | **6.8%** | 3 | Flow rise above six per cent; not two consecutive years; no trigger |
| 2025 | 4.2% | **4** | **Burst count exceeded three** |
| 2026 | **6.3%** | 2 | Flow rise above six per cent; not consecutive with 2024; no trigger |

**The April 2025 board minute records: "revision clause figures reported; no referral required."** The algorithm has not been re-specified.

## What the company monitors monthly

| Indicator | 2022 | 2024 | Read as |
|---|---|---|---|
| Programme areas with controllers operating | 60 of 62 | 62 of 62 | complete |
| Mean network pressure against target | within 0.4 m | within 0.3 m | **improved** |
| Customer contacts about low pressure | 1,940 | 1,905 | flat |

## Two numbers collected by different teams

| | 2022 | 2024 |
|---|---:|---:|
| Repairs raised as urgent by the control room | 2,840 | 3,510 |
| Independent pipe-failure reports logged by the street-works team | 418 | 431 |

## One further fact

**The algorithm sets its pressure target from a demand model built in 2021 on five years of consumption data.** Two of those five years were the pandemic years, when non-household consumption in these areas fell by roughly a third.

## Produce

1. **Compute the baseline** for each of the two watched figures — mean, spread, and maximum — using the seven years before the programme.

2. **For each threshold, say whether it is a trigger or a timer**, and give the arithmetic. A threshold that sits inside the range of ordinary variation will fire on ordinary variation.

3. **Say what should have happened in April 2025**, and what you can and cannot conclude from the 2025 burst count.

4. **The flow-rise limb was exceeded twice and never fired.** Say why, and say whether that is a fault in the rule or a cost that was accepted when it was written.

5. **Rewrite the "If" clause** so that it cannot be misread, and so that each threshold is defensible against the baseline.

6. **Look at the three monthly indicators.** Say what they can see and what they cannot, and name one failure that would leave all three looking acceptable.

7. **Compute the ratio of the two numbers collected by different teams**, for both years. Say what it shows and why nobody reported it.

8. **Diagnose the failure by the stage it entered through**, using the stages of this book. Say where the symptom appeared, where the failure entered, and how far apart they are.

9. **Write a revision trigger in two directions** — one condition about the world, and one about the model itself.
