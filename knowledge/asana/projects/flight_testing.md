_Asana snapshot as of 2026-11-10: 3 open tasks, 20 completed (last 90 days)._

# Flight Testing

## Overview
- **Team:** BST (Whole Team)
- **Status:** Active — ongoing release candidate and QC flight testing with continuous firmware/hardware validation
- **Primary Focus:** Aircraft firmware release candidate testing, VTOL systems validation, and mission-specific flight characterization
- **Key Personnel:** Spencer Hoehl (primary test pilot — 18 of 20 completed tasks), Alex Lomis, Ethan Domagala
- **Risk Signals:** 
  - 3 open tasks with no due dates (low urgency tracking but still active)
  - ERAU E2 instability issue unresolved as of 9/29 (investigation ongoing)
  - S10022 Transition Flights task unassigned

## Key Deliverables & Milestones
- **S10022 Release Candidate Testing** — Completed 2026-11-09 (GPS climbout fix verification)
- **S20003 Release Candidate Testing** — Completed 2026-11-09
- **Multiple firmware RC tests** (FW0001, FW0002) — Completed 2026-11-04
- **VTOL system validation flights** (S10021 VTOL QC, S10022 VTOL test) — Completed 2026-10-14
- **NASA S2 QC flight** (S20009) — Completed 2026-09-21, status "Passed"
- **ByLight Mustang Flight Test** — Completed 2026-09-22 (stability characterization, range testing via current draw)
- **S0 VTOL testing** — Completed 2026-10-01 (hover/transition work; MAG signal issue noted)

## Task Summary
- **Total:** 23 tasks (3 open, 20 completed)
- **Completion Rate:** 87%
- **Assignees:**
  - **Spencer Hoehl:** 22 tasks (18 completed, 3 open) — de facto project lead/primary test pilot
  - **Alex Lomis:** 1 completed task (S0 VTOL)
  - **Ethan Domagala:** 1 completed task (ByLight Mustang)
  - **Unassigned:** 1 open task (S10022 Transition Flights)
- **Pattern:** Heavy reliance on Spencer Hoehl for flight testing; most tasks use custom field "Status" (Ready for Flight Testing, More Info Requested, Passed, Maintenance Required) for workflow tracking

## Recent Activity
- **2026-11-09:** Major completion batch — S10022 and S20003 release candidate testing complete; Swiftab app RC version uploaded
- **2026-11-04:** Firmware and aircraft RC testing surge (FW0001, FW0002, S10021, S10005, S10011 all completed)
- **Ongoing:** ERAU E2 instability investigation (task open, last note 9/29 — issue could not be reproduced with or without wind sensor mast)
- **Awaiting Assignment:** S10022 Transition Flights to prepare for S3 Flying (unassigned, no due date)
- **E20006 Release Candidate Testing:** Open, no progress notes yet

## Notes & Context
- **No dollar values or customer names** are visible in task data — this appears to be internal BST flight testing infrastructure rather than a customer project
- **Release candidate pattern:** Project shows systematic firmware and aircraft validation before deployment (multiple RC testing tasks with "Ready for Flight Testing" status)
- **Technical issues encountered:**
  - S0 VTOL: MAG signal issues, parameter saving failures (8/20)
  - S10020 VTOL: ESC failure — loss of power immediately post-transition hover→forward flight
  - ERAU E2: Instability issues (investigation inconclusive)
- **QC requirements tracked:** Some tasks flagged "QC Required: Yes/No" (custom field)
- **No due dates on most open/recent tasks** — suggests flexible scheduling or internal-only work
- **External customer noted:** ByLight (Mustang test) and NASA (S2 QC flight, completed/passed)