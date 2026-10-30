_Asana snapshot as of 2026-10-30: 10 open tasks, 15 completed (last 90 days)._

# Flight Testing

## Overview
- **Client/Customer**: Internal BST flight testing operations; includes customer aircraft (NASA S2, ByLight Mustang)
- **Timeline**: Active ongoing testing program (last completed tasks in October 2026)
- **Status**: Active — 10 open tasks, 15 recently completed; no end date defined
- **Team Members**: Spencer Hoehl (primary test pilot — 23 of 25 tasks), Alex Lomis, Ethan Domagala, Maciej Stachura
- **Risk Signals**: 
  - No due dates on any open tasks (makes prioritization unclear)
  - Multiple release candidate tests queued but not yet started (S20003, E20006, S10021, S10022, FW0001, S10005, S10011, FW0002)
  - Two open RC test tasks note parameter issues (S10011, FW0002 require "Params downloaded before firmware uploaded")
  - ERAU E2 instability issue remains unresolved as of 9/29 (investigation inconclusive)

## Key Deliverables & Milestones
- **Release Candidate Testing Pipeline**: 8 aircraft/firmware variants queued for testing (S20003, E20006, S10021, S10022, FW0001, S10005, S10011, FW0002, Swiftab app)
- **Customer Deliverables**: 
  - NASA S2 QC flight (completed 2026-09-21, marked "Passed")
  - ByLight Mustang Flight Test (completed 2026-09-22)
- **Firmware Validation**: Multiple VTOL and fixed-wing firmware updates require QC flights before release
- **No documented dollar values or formal milestones in task data**

## Task Summary
- **Total Tasks**: 25 (10 open, 15 completed)
- **Tasks by Assignee**:
  - Spencer Hoehl: 23 tasks (21 completed, 9 currently open) — 91% completion rate on his assigned work
  - Alex Lomis: 2 tasks (both completed)
  - Ethan Domagala: 1 task (completed)
  - Maciej Stachura: 1 task (completed)
- **Notable Pattern**: Spencer Hoehl is the sole test pilot; entire testing workload concentrated on one person
- **Custom Field Usage**: "Status" field used heavily (e.g., "Ready for Flight Testing", "More Info Requested", "Maintenance Required"); "QC Required" checkbox used sporadically

## Recent Activity
- **October 2026 (most recent)**: 
  - S10022 Test Flights (VTOL, Vertiq motors) completed 10/14
  - S10021 VTOL QC flights completed 10/14
  - S1 fixed wing and FlameWheel QC completed 10/09
  - Soil Moisture E2 sensor testing completed 10/05
- **September 2026**: 
  - NASA S2 QC flight completed 9/21 (customer aircraft, marked "Passed")
  - ByLight Mustang flight test completed 9/22
  - S0-MAD catapult testing completed 9/17
  - ERAU E2 instability investigation ongoing (issue not reproduced as of 9/29)
- **Current Queue**: 10 release candidate and app tests waiting to be started — no movement on these since they entered "Ready for Flight Testing" status

## Notes & Context
- **Timeline Ambiguity**: All open tasks lack due dates; completion dates on closed tasks show activity in 2026 but no clear release schedule
- **Outstanding Issues**:
  - ERAU E2 instability remains unresolved; investigation inconclusive (tried with/without wind sensor mast, could not reproduce)
  - S10011 and FW0002 have blocking prerequisites (parameter download before firmware upload) — unclear if these are blocking test execution
  - Multiple VTOL firmware variants completed QC (S10021, S10022) but release status unclear
- **Historical Context** (from completed tasks):
  - S10020 VTOL had power loss on transition (Aug 2026) — fixed or still in testing?
  - S10019 had autopilot takeoff/climb issues (Aug 2026) — maintenance required, unclear if resolved
  - SOCOM ground station switching was being tested for S0-AD variant (Aug 2026)
- **Resource Constraint**: Single test pilot (Spencer Hoehl) is bottleneck for 10 queued tests; no secondary testers listed