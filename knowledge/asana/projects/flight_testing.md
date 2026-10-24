_Asana snapshot as of 2026-10-24: 10 open tasks, 15 completed (last 90 days)._

# Flight Testing

## Overview

- **Team**: Black Swift Technologies (whole team)
- **Status**: Active – ongoing release candidate and QC flight testing pipeline
- **Timeline**: Continuous operations; recent completions in October 2026; no project-level due date
- **Team Members**: Spencer Hoehl (primary test pilot/lead, ~90% of tasks), Ethan Domagala, Alex Lomis, Maciej Stachura, Jack (mentioned for NASA flights)
- **Risk Signals**: 
  - 10 open tasks with no due dates assigned (creates scheduling ambiguity)
  - Multiple tasks have "Ready for Flight Testing" status but remain open indefinitely
  - ERAU E2 instability investigation incomplete (9/29 entry notes issue could not be reproduced, investigation ongoing)
  - S10011 and FW0002 blocked pending parameter downloads before firmware upload
  - Several completed tasks marked "More Info Requested" or "Maintenance Required" (potential rework needed)

## Key Deliverables & Milestones

| Item | Status | Notes |
|------|--------|-------|
| S20003 RC Testing | Open | No due date |
| E20006 RC Testing | Open | No due date |
| S10021 RC Testing | Open | Ready for Flight Testing; VTOL-specific |
| S10022 RC Testing | Open | Ready for Flight Testing; Vertiq motors |
| FW0001 RC Testing | Open | Ready for Flight Testing |
| FW0002 RC Testing | Open | Ready for Flight Testing; blocked on param download |
| S10005 RC Testing | Open | Ready for Flight Testing |
| S10011 RC Testing | Open | Ready for Flight Testing; blocked on param download |
| ERAU E2 Instability Investigation | Open | Ongoing; instability could not be reproduced as of 9/29 |
| Swiftab App RC Version | Open | Uploaded; no further detail |

**Recent Completions (October 2026):**
- S10022 Test Flights (10/14) — VTOL firmware with Vertiq motors
- S10021 VTOL QC Flights (10/14) — VTOL firmware validation
- S1 Fixed Wing & FlameWheel QC (10/09)
- Soil Moisture E2 (10/05)
- QC Flight for New Firmware (10/01)

**External Testing:**
- ByLight Mustang Flight Test (Ethan Domagala, completed 9/22) — stability characterization and range assessment

## Task Summary

- **Total Tasks**: 25 (10 open, 15 completed)
- **Assignee Breakdown**:
  - **Spencer Hoehl**: ~23 tasks (92%) — dominates flight testing workload
  - **Ethan Domagala**: 1 task (ByLight Mustang)
  - **Alex Lomis**: 2 tasks (S0 VTOL, S10020 ESC)
  - **Maciej Stachura**: 1 task (S10019 Autopilot Test)

- **Completion Pattern**: 60% completion rate; most open tasks assigned to Spencer with no due dates, indicating they are queued or in progress
- **Custom Fields Usage**: Heavy use of "Status" (Ready for Flight Testing, More Info Requested, Maintenance Required, Passed) and "QC Required" (Yes/No) for tracking validation state
- **Blockers**: Two tasks (S10011, FW0002) explicitly require parameter downloads before firmware upload

## Recent Activity

**October 2026** (last 2 weeks):
- Completed two VTOL-related QC flights (S10022, S10021) and fixed-wing validation (10/9–10/14)
- S10022 and S10021 completion tasks marked "More Info Requested" — may require follow-up or additional testing
- Soil Moisture E2 sensor testing completed (10/5)
- QC firmware validation flight completed (10/1)

**September 2026**:
- NASA S2 QC flight passed (9/21); cleared for customer delivery
- ByLight Mustang external flight test completed (9/22, due date 9/18 — 4 days late)
- S0-MAD catapult testing completed (9/17, due date 9/11 — 6 days late)
- ERAU E2 instability investigation ongoing; issue could not be reproduced with/without wind sensor mast (9/29 note)

**August 2026**:
- Multiple QC flights and firmware validation tasks completed (S1 Fixed Wing, Flamewheel, S10019 Autopilot, S10019 SOCOM ground station, S0 VTOL)
- Known issues documented: S10019 autopilot errors (low takeoff altitude), S10020 VTOL ESC power-off during transition, S10020 firmware "no mag" hardware faults

## Notes & Context

- **No Dollar Values or Client Info** in task data — this appears to be internal R&D/validation flight testing, not client-billable work
- **VTOL Development Focus**: Multiple S1002x variants undergoing VTOL-specific testing (S10021, S10022); known issues include ESC failures during hover-to-forward transition and magnetometer initialization faults
- **Firmware Pipeline**: Tasks indicate active firmware releases moving through QC; parameters and firmware uploads are critical blockers
- **Investigation Ongoing**: ERAU E2 instability has not been resolved despite testing; remains "Ready for Flight Testing" status but root cause unconfirmed
- **Test Platforms**: Fleet includes S-series (S1, S0, S10005–S10022), Flamewheel (FW0001–FW0002), E-series (E2, E20006), and external partners (ByLight Mustang, NASA S2)
- **Maintenance Debt**: Several completed tasks tagged "More Info Requested" or "Maintenance Required" (S10019, ByLight Mustang, S10020 ESC) — rework or additional diagnostics pending
- **Scheduling Risk**: All 10 open RC testing and investigation tasks lack due dates; prioritization unclear without external context