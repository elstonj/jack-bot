_Asana snapshot as of 2026-11-05: 6 open tasks, 17 completed (last 90 days)._

# Flight Testing

## Overview
- **Client/Customer:** Multiple (ByLight Mustang, NASA S2, ERAU E2, internal BST platforms)
- **Dollar value:** Not specified in task data
- **Timeline:** Active ongoing testing; recent completions through November 2026
- **Status:** Active — steady completion rate (17 completed, 6 open); no risk signals of stalled work
- **Team members involved:** Spencer Hoehl (primary test pilot/lead), Alex Lomis, Ethan Domagala, Jack (mentioned for NASA flights), Unassigned (1 task)
- **Risk signals:** None critical; 6 open tasks lack due dates but appear staged for upcoming flight windows

## Key Deliverables & Milestones
- **Release Candidate Testing Suite** (ongoing)
  - FW0002, S10021, S10005, S10011, FW0001 completed (2026-11-04)
  - Pending: S20003, S10022, E20006 release candidate testing
- **Platform-Specific QC**
  - S0 VTOL (completed 2026-10-01, had mag signal issues)
  - S10020 VTOL ESC (completed 2026-08-21, power-loss issue during transition)
  - S1 fixed wing and FlameWheel (completed 2026-10-09)
- **Customer Deliverables**
  - ByLight Mustang Flight Test (completed 2026-09-22; Ethan Domagala)
  - NASA S2 QC flight (completed 2026-09-21; passed for customer readiness)
- **Sensor/Payload Testing**
  - Soil Moisture E2 (completed 2026-10-05)

## Task Summary
- **Total:** 6 open, 17 completed (74% completion rate)
- **By Assignee:**
  - Spencer Hoehl: ~22 tasks (primary lead; near 100% of testing)
  - Alex Lomis: 2 tasks (completed; both August)
  - Ethan Domagala: 1 task (ByLight; September)
  - Unassigned: 1 task (S10022 Transition Flights)
- **Pattern:** No due dates on open or recent completed tasks; work appears driven by "Ready for Flight Testing" status milestones rather than calendar deadlines. Custom field "QC Required" used selectively for firmware/ESC tests.

## Recent Activity
- **Most recent completions (2026-11-04):** Five release candidate firmware tests completed same day (FW0002, S10021, S10005, S10011, FW0001)
- **Ongoing investigation:** ERAU E2 instability — Spencer ready to fly for troubleshooting; attempt 9/29 to reproduce issue with/without wind sensor mast was unsuccessful
- **Staged for testing:** S20003, S10022, E20006 release candidate testing; S10022 transition flights (unassigned)
- **Recent payoff:** Multiple platforms moved through QC pipeline in September–October 2026

## Notes & Context
- **Known Issues Addressed:**
  - S10020 firmware update (8/21) targeted "no mag on startup" issue; field testing found Hardware fault errors during jump-start
  - S10020 VTOL ESC power-loss during hover-to-forward transition (8/21)
  - S0 VTOL MAG signal/params saving issues noted mid-August; MAG not sending signal blocking hover/transition tests
  - ByLight Mustang required maintenance post-test (2026-09-22)
  
- **Testing Workflow:** "Ready for Flight Testing" status indicates aircraft/firmware cleared to proceed; "More Info Requested" or "Maintenance Required" indicate issues requiring rework before next cycle
- **Parameter Management:** Multiple notes flag "Params need to be downloaded before firmware uploaded" — recurring procedural dependency
- **Pilot Notes Style:** Detailed field observations (e.g., throttle strapping, transient issues) suggest Spencer is recording live troubleshooting data in-task

**No team corrections provided.** All dates and status reflect raw Asana data.