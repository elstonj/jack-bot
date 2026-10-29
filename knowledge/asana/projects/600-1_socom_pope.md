_Asana snapshot as of 2026-10-29: 60 open tasks, 2 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Project Owner:** Dan Prendergast
- **Priority:** High
- **Timeline:** October 2026 – May 2027
- **Status:** Active — Early stage (2 of 62 tasks completed; kickoff done, prototype design underway)
- **Team Members:** Dan Prendergast (lead), Josh Fromm (mechanical/prototype), Ethan Domagala (build/test), Alex Lomis (datalink), Ben Busby (software/UI), Maciej Stachura (sensors/software)
- **Risk Signals:** Multiple tasks due late October 2026 are imminent; foundational design tasks (requirements, camera selection) due within weeks

## Key Deliverables & Milestones
Multi-phased delivery across 6 CLINs, each culminating in closeout and milestone:

| CLIN | Focus | Key Deliverables | Milestone Due |
|------|-------|------------------|---------------|
| 1 | Prototype PCLT (Pressure-Controlled Launch Tube) | Build S0 w/ accelerometer, site visit & launch, design refinement, closeout | 2026-12-15 |
| 2 | METAR (Meteorological) sensors | Requirements, trade studies (precipitation, cloud, visibility), prototype build & test, closeout | 2027-02-26 |
| 3 | Auto-METAR integration | Sensor data processing, UI updates, prototype build & test, closeout | 2027-03-26 |
| 4 | EO/IR R&R (Reconnaissance & Recovery) | Camera/storage hardware, datalink, prototype build & test, closeout | 2027-04-30 |
| 5 | EO/IR Real-time ATR (Automatic Target Recognition) | ATR model selection, edge compute, datalink, prototype build & test, closeout | 2027-05-14 |
| 6 | EO/IR FMV (Full Motion Video) | Gimballed camera trade study, gimbal control UI, no-comm transit mode, prototype build & test, closeout | 2027-05-31 |

**Dollar value:** Not provided in custom fields or task names.

## Task Summary
- **Total:** 62 tasks (60 open, 2 completed)
- **Completion Rate:** 3% (early project phase)
- **Assignments by Owner:**
  - Dan Prendergast: 15 tasks (requirements, camera selection, operational evaluations, closeouts)
  - Josh Fromm: 8 tasks (mechanical/electrical design, prototyping, site visit)
  - Ethan Domagala: 8 tasks (prototype builds, bench/flight testing)
  - Ben Busby: 6 tasks (software/UI updates across multiple CLINs)
  - Alex Lomis: 5 tasks (datalink & comm protocol development)
  - Maciej Stachura: 4 tasks (sensor trade studies, software)
  - Unassigned: 3 tasks (2 milestones, 1 mechanical/electrical design)

- **Patterns:** 
  - Heavy use of phased delivery structure (requirements → design → build → test → closeout for each CLIN)
  - Prototyping bottleneck: Ethan Domagala owns all hardware builds and flight tests
  - Cross-functional dependencies: Josh (mech/elec design) → Ethan (build) → Dan (operational eval)

## Recent Activity
- **Completed (Oct 2026):** Kickoff (2026-10-01), Design and order PCLT end cap (completed 2026-10-15 vs. due 2026-10-02 — 13 days late)
- **Imminent (next 2 weeks):**
  - Build prototype PCLT S0 with accelerometer — Ethan Domagala (due 2026-10-20)
  - Write requirements and top-level design — Dan Prendergast (due 2026-10-19)
  - EO/IR camera selection and purchase — Dan Prendergast (due 2026-10-28)
  - SOCOM site visit and instrumented S0 launch — Josh Fromm (due 2026-10-27)

## Notes & Context
- **SOCOM Site Visit (CLIN 1):** Task notes indicate critical pre-site questions: Can PCLT tube be loaded inflight or must S0 load on ground? Is power switch accessible when inside tube? These design constraints directly affect prototype build timeline.
- **ATR (CLIN 5):** Task notes show questions ready for stakeholder review — datasets, validation results, classification level, and label list all marked as unclassified/open-source.
- **Gimbal Trade Study (CLIN 6):** Dan Prendergast owns gimballed camera selection, due 2026-11-25.
- **No custom dollar field populated** — Budget tracking unclear.
- **Mechanical/Electrical bottleneck:** Josh Fromm is single point of failure for all mech/elec design across 6 CLINs; two tasks (CLIN 2, CLIN 5) currently unassigned.