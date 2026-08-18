# Chapter 4 Transfer Design

Status: governed design source for the Chapter 4 cold-transfer forms.

**Contains answer commentary for both transfer forms. Do not read this file if you intend to complete the Chapter 4 transfer exercises**; use the reader copies `transfer-form-a.md` and `transfer-form-b.md`, which the manuscript links at the right moment.

Where a reader copy conflicts with this file, this file controls.

## Transfer target

> Given an unfamiliar dataset and a question it is being used to answer, describe the process that produced the records separately from the process being asked about, identify one unit or category that could never have appeared, state whether being recorded is related to the quantity at issue, and say why collecting more of the same records would not help.

## Form design

Two parallel forms, one physical/operational and one institutional, following the pattern governed by `../../decisions/0005`.

| | Form A | Form B |
|---|---|---|
| Domain | City pothole repair records | Food bank client records |
| The dataset is really of | **reports**, not potholes | **registered visits**, not need |
| Question it cannot answer | Which roads are in worst condition | How food insecurity changed |
| Institutional purpose | Scheduling repair crews | Acquitting a grant |
| Eligibility | Council-maintained roads only | Catchment postcodes; referral required |
| Coverage | App requires smartphone and account | Two weekday mornings; hourly bus |
| Capture related to value | Photo upload fails on slow connections, which are rural | Households in most acute difficulty least likely to complete registration |
| Retention | Closed 90 days after repair; severity and photo discarded | Individual records archived at funding-year end |
| Reporting | Return counts defects **repaired**, not reported | Funder's five categories, not the site's |
| Censoring | Severity capped at 5 | Visits capped at 12 per year |
| Absence | Roads with no residential frontage | People without a referral, or unable to attend on a weekday morning |
| Chapter 15 item | Councillor's reporting campaign after crews allocated by report volume | Registering adults individually after funder compared sites on clients served |

Both demand the same five structural outputs. Only the surface domain differs.

### Domain exclusions

Every previously used domain is excluded: refrigerated warehouse, emergency housing, municipal water, pendulum, student assessment, regional blood supply, city rental assistance, school indoor air quality, hospital emergency department waiting time.

## What a strong Form A answer should notice

- The register is a record of **reports**, not of potholes. A road with no reports may have no defects or no residents. This is the whole case and most of the marks.
- The absence item is roads with **no residential frontage** — the industrial estate, the bypass, the two link roads. Nobody lives there, so nobody reports, so those roads generate no rows at all. A strong answer explains that this produces no gap to notice.
- **Direction matters.** The relationship runs so that better-connected, more populated, more app-using areas produce more reports. If crews and resurfacing follow report counts, the register systematically underserves exactly the roads it under-records.
- The photo-upload fact is a **capture failure related to the value** — rural roads produce photo-less reports, which are deprioritised. Strong answers connect the technical detail to the consequence.
- Severity capped at 5 is **censoring**: a defect worse than 5 is recorded as 5, and the worst hazards are indistinguishable from ordinary ones in the data.
- Retention discards severity and photograph after 90 days, so any historical condition analysis has only date, road, and closure code.
- The return counts **repairs, not reports** — a different quantity again, and the one the committee has probably been seeing.
- More reports do not help: another two years changes none of eligibility, coverage, the photo problem, the cap, or the retention rule.
- The Chapter 15 item is the **councillor's reporting campaign**.

## What a strong Form B answer should notice

**Register discipline is especially important on this form.** The correct analysis is about the **dataset's structural blind spots** — a referral requirement, a catchment boundary, weekday-daytime opening, a bus that runs hourly. It is not about the people who do not appear. Nothing in this form supports, and the rubric penalises, any inference about the character, motivation, or circumstances of people absent from the register. They are absent because of how the register was built.

- The register is a record of **registered visits to one site**, not of food insecurity in a district. A strong answer says so in the first sentence.
- The absence item is people **without a referral**, **outside the catchment**, or **unable to attend on a Tuesday or Thursday morning**. Each is a structural barrier created by how the service is organised, and each produces no row.
- The staff observation — that households in the most acute difficulty are least likely to complete registration on a first visit, and are often given a parcel unrecorded — is the **capture failure related to the value**, and it is the hardest and most valuable item on the form. The register under-records exactly the cases the partnership most needs to see.
- The 12-visit cap is **censoring**: households continue to be seen informally without a record, so the register shows 12 where the true figure is higher.
- Individual records are archived at funding-year end, leaving only monthly totals — so an eighteen-month trend spans a retention boundary.
- The funder's five categories are a **reporting** reshape imposed from outside.
- The dataset is **one site**. Even were it perfect, it would describe this food bank, not the district.
- More records do not help: another eighteen months changes none of the referral requirement, the catchment, the opening hours, or the registration barrier.
- The Chapter 15 item is the **change to registering adults individually** after the funder began comparing sites on clients served — which would produce a rising "clients served" trend with no change in need whatsoever, and is the trap most likely to catch a reader answering the partnership's question anyway.

## Parallelism check

Both forms supply: a dataset of interactions with a system rather than of the underlying condition; an eligibility rule; a coverage channel reaching some and not others; a capture failure **related to the value**; a censoring cap; a retention boundary; an externally imposed reporting format; an institutional purpose that is not the reader's; and one Chapter 15 item.

Both also make the same trap available: a reader can produce a plausible ranking or trend from the register and be entirely wrong. The rubric treats doing so as a major category error.

## Ethical note on Form B

This form concerns food insecurity. It was written so that:

- every absent group is absent for a **structural** reason stated in the form;
- no supplied fact invites inference about individuals' choices or character;
- the food bank's staff and the funder are both portrayed as acting reasonably under constraint;
- the Chapter 15 item is a practice change, not misconduct.

**The form has not been reviewed by anyone with expertise in food-bank operations or in research involving vulnerable populations.** `spec.md` records this as an open question and as evidence needed before prose is considered stable. If a reviewer judges the domain unsuitable for a teaching exercise, the form should be replaced rather than softened — a version that avoids the difficulty by making the case less real would not teach the same thing.

## Pilot notes

- Target duration **40 minutes**, a design parameter pending pilot evidence.
- Form order counterbalanced (A→B and B→A), per `../../decisions/0008`.
- Record prior familiarity with local-government operations and with charitable food provision before the first task.
- The delayed form must not be previewed.
- Watch for readers who answer the substantive question anyway. That is the single most informative failure this form can produce and should be coded, not just marked wrong.
