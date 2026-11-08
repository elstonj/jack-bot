_Asana snapshot as of 2026-11-08: 6 open tasks, 17 completed (last 90 days)._

# Flight Testing

## Overview
- **Client/Customer:** Internal BST flight testing operations (multiple aircraft platforms including NASA, ByLight)
- **Dollar Value:** Not specified in task data
- **Timeline:** Ongoing testing cycle; most recent completions Nov 2026; multiple aircraft in active testing rotation
- **Status:** **ACTIVE** — 6 open tasks, 17 recently completed (most within last month)
- **Team Members:** Spencer Hoehl (primary test pilot/lead), Alex Lomis, Ethan Domagala, Jack (occasional)
- **Risk Signals:** 
  - No due dates on any open tasks (unclear prioritization/deadlines)
  - One unassigned task: "S10022 Transition Flights to prepare for"
  - Multiple release candidate tests pending with no timeline

## Key Deliverables & Milestones
All milestones are aircraft-specific release candidate testing and QC flights:

| Aircraft | Task | Status | Completed |
|----------|------|--------|-----------|
| S10022 | Release Candidate Testing (GPS climbout fix verification) | OPEN | — |
| S20003 | Release Candidate Testing | OPEN | — |
| E20006 | Release Candidate Testing | OPEN | — |
| FW0002 | Release Candidate Testing | **DONE** | 2026-11-04 |
| FW0001 | Release Candidate Testing | **DONE** | 2026-11-04 |
| S10021 | Release Candidate Testing (VTOL) | **DONE** | 2026-11-04 |
| S10005 | Release Candidate Testing | **DONE** | 2026-11-04 |
| S10011 | Release Candidate Testing | **DONE** | 2026-11-04 |
| ERAU E2 | Instability Investigation | OPEN | — |
| Swiftab App | Release Candidate Version Upload | OPEN | — |
| NASA S2 | QC Flight | **DONE** | 2026-09-21 |
| ByLight Mustang | Flight Test (stability/range characterization) | **DONE** | 2026-09-22 |

## Task Summary
- **Total Tasks:** 23 (6 open, 17 completed)
- **Tasks by Assignee:**
  - **Spencer Hoehl:** 22 tasks (17 completed, 5 open) — ~77% completion rate on assigned work
  - **Alex Lomis:** 2 tasks (both completed) — ~100%
  - **Ethan Domagala:** 1 task (completed) — ~100%
  - **Unassigned:** 1 open (S10022 Transition Flights)

- **Notable Patterns:**
  - Spencer Hoehl carries the vast majority of flight testing workload
  - Heavy use of "Ready for Flight Testing" status custom field
  - QC Required field used selectively (some tasks marked No QC, others marked Yes)
  - Release candidate testing is the primary focus; many tasks lack due dates (may indicate ad-hoc scheduling)
  - Multiple aircraft platforms in parallel testing (VTOL, fixed-wing, specialized sensors)

## Recent Activity
- **November 4, 2026:** Major completion spike — 5 release candidate tests completed in one day (FW0001, FW0002, S10005, S10011, S10021)
- **October 14, 2026:** S10022 Test Flights and S10021 VTOL QC flights completed
- **September–October:** Steady completion of specialized tests (soil moisture, VTOL transitions, ByLight Mustang, NASA S2 QC)
- **Current Open Queue:** 6 tasks remain, focused on additional release candidates (S20003, E20006) and instability investigation (ERAU E2)

## Notes & Context

### Team Feedback
Daniel Prendergast asserted "Mine's correct. Stop hazing me, Mr. Flight Director" (2026-10-15 and 2026-10-16). This appears to be a correction to flight test data or parameters; recommend clarifying with Daniel what specific item was being disputed.

### Key Technical Notes
- **ERAU E2 Instability:** Issue could not be reproduced as of 9/29; testing with/without wind sensor mast ongoing
- **S10022 GPS Issue:** Lost GPS on climbout — fix pending verification in release candidate test
- **Firmware Prerequisites:** Multiple tasks note "Needs Params downloaded before firmware uploaded" (FW0001, FW0002, S10011)
- **Historical Issues Resolved:**
  - S10020 ESC failure (power loss on VTOL transition) — appears resolved in later firmware builds
  - Magnetometer startup faults on S10020 — addressed in firmware update tested 8/21
  - SOCOM ground station switching capability tested and verified (8/17)

### Observation
This is a high-throughput QC/release validation pipeline with Spencer Hoehl as the bottleneck. Open tasks lack due dates, which may reflect flexible scheduling around weather/aircraft availability or indicate need for better milestone tracking. The unassigned "S10022 Transition Flights" task should be assigned.