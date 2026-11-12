_Asana snapshot as of 2026-11-12: 3 open tasks, 20 completed (last 90 days)._

# Flight Testing

## Overview
- **Client/Customer**: Internal BST flight testing program; includes customer aircraft (NASA S2, ByLight Mustang, ERAU E2)
- **Dollar value**: Not specified in task data
- **Timeline**: Active ongoing program; recent completions through November 2026
- **Status**: **Active** — 3 open tasks, 20 recently completed (most within last 6 weeks)
- **Team members**: Spencer Hoehl (primary test pilot), Alex Lomis, Ethan Domagala, Jack (QC flights)
- **Risk signals**: Open tasks lack due dates; ERAU E2 instability investigation has incomplete notes (9/29 issue reproduction attempt cut off)

## Key Deliverables & Milestones
No formal milestone structure in task data. Notable completed test programs:
- **S10022 Release Candidate Testing** (completed 2026-11-09) — GPS climbout fix verification
- **S10022 Transition Flights** (completed 2026-10-14) — VTOL firmware with Vertiq motors
- **S10021 VTOL QC flights** (completed 2026-10-14) — VTOL-specific firmware changes
- **NASA S2 QC flight** (completed 2026-09-21) — Customer readiness check
- **ByLight Mustang Flight Test** (completed 2026-09-22) — Stability characterization and range testing
- **S0 VTOL** (completed 2026-10-01) — Hover and transition testing (MAG signal issues noted)

## Task Summary
- **Total**: 3 open, 20 completed (87% completion rate)
- **By assignee**:
  - **Spencer Hoehl**: 22 tasks (primary test pilot) — ~95% completion
  - **Alex Lomis**: 2 tasks (S0 VTOL, S10020 ESC) — both completed
  - **Ethan Domagala**: 1 task (ByLight Mustang) — completed
  - **Unassigned**: 1 task (S10022 Transition Flights prep)
- **Pattern**: Overwhelming majority of work on Spencer Hoehl; no formal due dates in open tasks

## Recent Activity
- **2026-11-09**: Three major release candidate tests completed (S10022, S20003, app release)
- **2026-11-04**: Firmware/RC testing campaign (FW0001, FW0002, S10005, S10011, S10021)
- **2026-10-14**: VTOL test flights completed (S10022 Test Flights, S10021 QC)
- **Ongoing**: ERAU E2 instability investigation (ready for flight, last note 9/29 — issue could not be reproduced)

## Open Tasks
1. **ERAU E2 instability investigation** (Spencer Hoehl) — No due date
   - Status: Ready for Flight Testing
   - Notes indicate investigation attempt on 9/29 (wind sensor mast tests inconclusive); aircraft ready to fly to continue troubleshooting
2. **E20006 Release Candidate Testing** (Spencer Hoehl) — No due date
3. **S10022 Transition Flights to prepare for S3 Flying** (Unassigned) — No due date
   - Status: Ready for Flight Testing

## Notes & Context
- **Known technical issues in recent tests**:
  - S0 VTOL: MAG (magnetometer) not sending signal; params not saving on updates (8/20 note)
  - S10020 ESC: Aircraft powered off immediately after hover-to-forward transition (8/21)
  - S10020 firmware: Repeated "Hardware fault" errors on startup despite intended fix (8/21)
  - ERAU E2: Instability could not be reproduced in testing (9/29)
- **Test patterns**: Heavy emphasis on release candidate firmware testing, VTOL transition validation, and customer aircraft QC
- **Data quality note**: ERAU E2 investigation task has truncated notes (cuts off mid-sentence); last update 9/29, but task remains open with no due date

**Team Feedback**: Daniel Prendergast's corrections (2026-10-15, 2026-10-16) note "Mine's correct. Stop hazing me, Mr. Flight Director" — context unclear from Asana data alone; may reflect internal workflow or status dispute.