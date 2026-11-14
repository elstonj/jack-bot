_Asana snapshot as of 2026-11-14: 3 open tasks, 20 completed (last 90 days)._

# Flight Testing

## Overview
- **Client/Team:** Black Swift Technologies (whole team project)
- **Status:** Active — ongoing test flight operations with release candidate validation
- **Team Members:** Spencer Hoehl (primary test pilot — 22 of 23 tasks), Alex Lomis, Ethan Domagala
- **Risk Signals:** 
  - 3 open tasks with no due dates (may indicate unclear scheduling)
  - ERAU E2 instability issue unresolved as of 9/29 (investigation ongoing)
  - Multiple completed tasks note firmware/hardware issues requiring follow-up (e.g., S10020 ESC power-off mid-flight, MAG signal loss on S0 VTOL)

## Key Deliverables & Milestones
- **S10022 Release Candidate Testing** — Completed 2026-11-09 (verify GPS fix on climbout)
- **S20003 Release Candidate Testing** — Completed 2026-11-09
- **FW0002 & FW0001 Release Candidate Testing** — Completed 2026-11-04
- **ByLight Mustang Flight Test** — Completed 2026-09-22 (stability characterization, max range testing)
- **NASA S2 QC Flight (S20009)** — Completed 2026-09-21, passed
- **S10022 Transition Flights** — In progress (unassigned, no due date; prepares for S3 flying)
- **E20006 Release Candidate Testing** — Open, no due date

## Task Summary
- **Total:** 23 tasks (3 open, 20 completed)
- **By Assignee:**
  - Spencer Hoehl: 22 tasks (~87% of workload), nearly all open and recent completions
  - Alex Lomis: 1 task (S0 VTOL, completed 2026-10-01)
  - Ethan Domagala: 1 task (ByLight Mustang, completed 2026-09-22)
  - Unassigned: 1 open task (S10022 Transition Flights)
- **Completion Rate:** 87% (20/23)
- **Notable Pattern:** Heavy concentration on release candidate testing and QC flights; no dollar amounts tracked in Asana

## Recent Activity
- **Nov 9, 2026:** Multiple release candidate tests completed (S10022, S20003, Swiftab app)
- **Nov 4, 2026:** Batch of firmware/RC tests closed (FW0002, FW0001, S10021, S10011, S10005)
- **Oct 14, 2026:** VTOL and transition flight tests completed (S10022 test flights, S10021 VTOL QC)
- **Ongoing:** ERAU E2 instability investigation (Spencer Hoehl, no due date; last note 9/29 showed issue could not be reproduced)

## Notes & Context

### Team Feedback (Authoritative Override)
**Daniel Prendergast** [2026-10-15 & 2026-10-16]: Indicated his data/status is correct and objected to external corrections ("Stop hazing me, Mr. Flight Director"). This suggests potential data conflicts in Asana; his actual status should be trusted over task records if discrepancies exist.

### Key Technical Issues Noted
- **ERAU E2 instability:** Under investigation; wind sensor mast removal did not isolate cause (9/29)
- **S10020 VTOL ESC failure:** Aircraft powered off immediately after transition from hover to forward flight; did not power on with simple boot (8/21)
- **S10020 firmware issue:** Repeated "Hardware fault error" on startup despite firmware update intended to fix "no mag" issue (8/25)
- **S0 VTOL MAG signal loss:** Parameters not saving when updated; transient MAG issues prevent hover/transition testing (8/20)
- **ByLight Mustang:** Test flight completed with stability data and max range characterization via current draw (9/22)

### Process Notes
- Release candidates require firmware parameter downloads before upload (noted on FW0002, FW0001, S10011)
- QC flights often preceded customer handoff (e.g., NASA S2 QC before delivery)
- No formal due dates on most tasks suggest agile/rolling flight test schedule based on aircraft readiness