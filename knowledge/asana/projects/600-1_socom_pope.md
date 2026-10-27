_Asana snapshot as of 2026-10-27: 60 open tasks, 2 completed (last 90 days)._

# [600-1] SOCOM Pope

## Overview
- **Client/Customer:** SOCOM
- **Priority:** High
- **Owner:** Dan Prendergast
- **Timeline:** Project spans October 2026 – May 2027 (6 CLINs with staggered delivery dates)
- **Status:** Active — 60 open tasks, 2 completed. Project is in early phases (CLIN 1 design/prototype work underway)
- **Team Members:** Dan Prendergast (lead), Josh Fromm (mechanical/build), Ethan Domagala (prototyping/testing), Alex Lomis (datalink/comms), Ben Busby (software/UI), Maciej Stachura (sensors/software)
- **Risk Signals:** 
  - CLIN 1 prototype build tasks (Ethan, Josh) due 2026-10-20 and 2026-10-27 are imminent and critical path
  - Site visit prep task (Josh, due 2026-10-27) has incomplete notes; questions about in-flight loading and power switch access remain unanswered
  - No dollar value visible in custom fields or task names

## Key Deliverables & Milestones

| CLIN | Capability | Key Deliverables | Milestone Due |
|------|-----------|-----------------|--------------|
| **1** | PCLT (Prototype Compact Launch Tube) S0 | Prototype build, site visit & launch, design refinement | 2026-12-15 |
| **2** | METAR (weather) S0 | Requirements, sensor trade studies (precipitation, cloud, visibility), prototype build & test | 2027-02-26 |
| **3** | Auto-METAR S0 | Requirements, sensor integration, software for data processing, prototype build & test | 2027-03-26 |
| **4** | EO/IR R&R (Reconnaissance & Recovery) S0 | Camera/storage selection, datalink protocol, prototype build & test | 2027-04-30 |
| **5** | EO/IR Real-time ATR (Automatic Target Recognition) S0 | ATR model selection, edge compute, real-time processing, prototype build & test | 2027-05-14 |
| **6** | EO/IR FMV (Full Motion Video) S0 | Gimballed camera, gimbal control UI, no-comm transit mode, prototype build & test | 2027-05-31 |

Each CLIN includes prototype build, bench/ground/local testing, operational flight evaluation, and closeout slides/report.

## Task Summary

**Overall:**
- Total: 60 open, 2 completed (97% incomplete)
- Project is ~2 weeks old; only kickoff and end cap design finished

**By Assignee (open tasks):**
| Assignee | Count | Notes |
|----------|-------|-------|
| Dan Prendergast | 18 | Requirements writing, EO/IR selections, operational evaluations, closeout reporting across all CLINs |
| Josh Fromm | 10 | Mechanical/electrical design, prototype builds, design refinement, integration across CLINs 1–4 |
| Ethan Domagala | 10 | All prototype builds and bench/flight testing (PCLT, METAR, Auto-METAR, EO/IR R&R, EO/IR ATR, EO/IR FMV) |
| Ben Busby | 5 | Software/UI updates for image capture, METAR display, EO/IR UI, gimbal control |
| Alex Lomis | 4 | Datalink and comm protocol development across CLINs 1–5 |
| Maciej Stachura | 4 | Sensor trade studies (CLIN 2), software for data processing (CLIN 2), no-comm transit mode (CLIN 6) |
| Unassigned | 9 | Mostly milestone closure tasks; one mechanical/electrical integration task (CLIN 5) |

**Patterns:**
- Heavy concentration on Dan (strategy/requirements/evaluation), Ethan (prototyping/testing), and Josh (mechanical/integration)
- No custom budget fields visible; value tracking not available from task list
- Clear cascade: requirements → design → build → test → closeout for each CLIN

## Recent Activity

**Completed (last 2 weeks):**
- Kickoff meeting (2026-10-01)
- Design and order prototype PCLT end cap (completed 2026-10-15, ~2 weeks late)

**Imminent (next 7–14 days):**
- **2026-10-19:** Write requirements and top-level design (Dan) — overdue status unknown
- **2026-10-20:** Build prototype PCLT S0 with accelerometer (Ethan) — critical path, due in days
- **2026-10-27:** SOCOM site visit and instrumented S0 launch (Josh) — includes unanswered site prep questions
- **2026-10-28:** EO/IR camera selection and purchase (Dan); EO/IR Camera and hardware selection (Dan) — duplicate or overlapping tasks

**Approaching (late October–early November):**
- Design refinement for launch survival (2026-11-03)
- CLIN 1 closeout and milestone (2026-12-15)

## Notes & Context

1. **Site Visit (2026-10-27):** Josh's task notes contain incomplete prep questions:
   - Can PCLT tube be loaded inflight, or must S0 load on ground?
   - Is power switch accessible when inside tube?
   - **Action:** These need to be resolved before site visit or addressed during it.

2. **ATR Selection (CLIN 5):** Notes indicate all candidate models are unclassified, open-source trained, with publicly available validation results and label lists. Simplifies compliance/development.

3. **Architecture:** Project is modular—each CLIN builds a different capability (launch tube, weather sensors, ATR, video, gimbal) for the same S0 platform. Suggests parallel workstreams possible.

4. **Unassigned Mechanical/Electrical Task (CLIN 5, due 2027-01-26):** Should be assigned or clarified.

5. **Duplicate Task Names:** Multiple "Bench, ground, and local flight test" and "Write requirements and top-level design" tasks across CLINs—this is intentional (per CLIN structure) but confirm no unintended duplication.

6. **No Corrections Block Provided:** All data reflects raw Asana; no team overrides or status corrections supplied.