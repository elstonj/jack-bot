_Asana snapshot as of 2026-11-06: 6 open tasks, 17 completed (last 90 days)._

# Flight Testing

## Overview
- **Client/Customer**: Multiple internal projects (NASA S2, ByLight Mustang, ERAU E2) and internal BST airframes (S-series, FW-series, Flamewheel)
- **Timeline**: Active ongoing testing; recent completions in October–November 2026; no project-level due date
- **Status**: **Active** — 6 open tasks, 17 completed; recent completions as of 2026-11-04; mix of firmware QC flights and release candidate testing
- **Team Members**: Spencer Hoehl (primary test pilot/lead), Alex Lomis, Ethan Domagala, Jack (mentioned for NASA flights)
- **Risk Signals**: 
  - Multiple open release candidate testing tasks with **no due dates** (S20003, S10022, E20006)
  - ERAU E2 instability issue remains unresolved (9/29 note: "Issue could not be reproduced")
  - S10022 GPS loss on climbout still under investigation

## Key Deliverables & Milestones

### Completed (Recent)
- **FW0001 & FW0002 Release Candidate Testing** — completed 2026-11-04
- **S10005, S10011, S10021 Release Candidate Testing** — completed 2026-11-04
- **NASA S2 QC Flight** — completed 2026-09-21 (Passed; ready for customer)
- **ByLight Mustang Flight Test** — completed 2026-09-22 (stability characterization, range testing)

### Open / In Progress
- **ERAU E2 Instability Investigation** — ongoing; aircraft ready to fly but issue reproducibility uncertain
- **S20003, S10022, E20006 Release Candidate Testing** — open, no due dates assigned
- **S10022 Transition Flights** — preparation phase, unassigned
- **Swiftab App Release Candidate Upload** — awaiting testing/validation

## Task Summary

| Metric | Count |
|--------|-------|
| **Total Tasks** | 23 (6 open, 17 completed) |
| **Completion Rate** | 74% |
| **Tasks by Spencer Hoehl** | 22 of 23 (96%) |
| **Other Assignees** | Alex Lomis (2), Ethan Domagala (1), Unassigned (1) |

**Patterns**:
- Spencer Hoehl carries nearly all testing workload
- Release candidate testing is the dominant workflow (FW, S-series airframes)
- Firmware QC flights often note parameter/configuration requirements ("Params downloaded before firmware uploaded")
- Multiple ongoing issues with comms/MAG signal retention across different airframes

## Recent Activity

**November 2026**: 
- Heavy completion of release candidate testing batches (FW0001/FW0002, S10005/S10011/S10021) on 2026-11-04

**October 2026**:
- S10022 Test Flights (VTOL Vertiq) completed 2026-10-14
- S10021 VTOL QC completed 2026-10-14
- Soil Moisture E2 sensor testing completed 2026-10-05
- S1/Flamewheel QC completed 2026-10-09

**September 2026**:
- ByLight Mustang flight test (9/22) — characterized stability, measured range
- NASA S2 QC flight (9/21) — approved for customer delivery
- S0-MAD catapult testing (9/17)

**Ongoing Issues**:
- ERAU E2: instability cannot be reproduced (with/without wind sensor mast) as of 9/29
- S10022: GPS loss on climbout—fix pending verification

## Notes & Context

### Firmware & Configuration Patterns
- Multiple tasks note "Params downloaded before firmware uploaded" as a prerequisite
- Recurring hardware faults (e.g., S10020 "no mag" issue on startup; S10020 ESC power-loss mid-transition)
- SOCOM ground station switching and dual-GCS testing in progress

### Test Airframe Inventory & Status
- **S0 (VTOL)**: Transient MAG signal issues, params not saving during updates
- **S10022 (Vertiq VTOL)**: GPS loss on climbout; transition flight prep pending
- **S10020**: ESC power-loss during hover→forward transition; firmware fix attempted
- **S10021**: VTOL-specific firmware; QC passed
- **ERAU E2**: Instability issue under investigation; wind sensor mast not the culprit
- **FW0001/FW0002**: Release candidates completed
- **NASA S2 (S20009)**: Approved for customer handoff
- **ByLight Mustang**: Flight-tested; stability/range characterized

### Missing Information
- No dollar values or budget tracking visible in current task data
- No explicit project end date or delivery deadline
- Several open RC testing tasks lack priority or due date guidance
- S10022 Transition Flights task remains unassigned