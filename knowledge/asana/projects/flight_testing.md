_Asana snapshot as of 2026-11-04: 10 open tasks, 12 completed (last 90 days)._

# Flight Testing

## Overview

- **Team:** Black Swift Technologies (Whole Team)
- **Status:** Active – ongoing release candidate testing and flight validation
- **Timeline:** Continuous testing cycle; recent activity through 2026-10-16
- **Team members:** Spencer Hoehl (primary flight test lead), Alex Lomis, Ethan Domagala
- **Risk signals:** 10 open tasks with no due dates; all "Ready for Flight Testing" tasks awaiting execution; several completed tasks marked "More Info Requested" indicating possible blockers

**Note:** Team feedback from Daniel Prendergast (2026-10-16, 2026-10-15) confirms data accuracy; no project-level corrections override Asana records.

## Key Deliverables & Milestones

| Task | Status | Notes |
|------|--------|-------|
| S10022 Test Flights (VTOL) | Completed 2026-10-14 | Vertiq motors firmware validation |
| S10021 VTOL QC Flights | Completed 2026-10-14 | VTOL-specific firmware changes |
| S1 Fixed Wing & FlameWheel QC | Completed 2026-10-09 | Firmware changes validation |
| ByLight Mustang Flight Test | Completed 2026-09-22 | Stability characterization, range testing (Ethan Domagala) |
| NASA S2 QC Flight | Completed 2026-09-21 | Customer readiness validation |
| S0-MAD Flight Testing | Completed 2026-09-17 | Catapult compatibility testing |

## Task Summary

- **Total:** 22 tasks (10 open, 12 completed)
- **Completion rate:** ~55%
- **Assignees:**
  - **Spencer Hoehl:** 19 tasks (9 open, 10 completed) — primary flight test engineer
  - **Alex Lomis:** 2 tasks (0 open, 2 completed)
  - **Ethan Domagala:** 1 task (0 open, 1 completed)
- **Pattern:** Heavy concentration on Spencer Hoehl; most open tasks lack due dates but are flagged "Ready for Flight Testing"

## Recent Activity

**Completed (Oct 2026):**
- S10022 Test Flights & S10021 VTOL QC flights completed 2026-10-14
- S1 fixed wing QC completed 2026-10-09

**In Progress (no due dates):**
- 10 open release candidate testing tasks across multiple airframe models (S20003, E20006, S10021, S10022, FW0001, S10005, S10011, FW0002, plus Swiftab app release)
- ERAU E2 instability investigation ongoing; issue not reproducible as of 9/29
- Several tasks carry implementation notes: S10011 and FW0002 require "Params downloaded before firmware uploaded"

## Notes & Context

- **Custom Field Usage:** "Status" field consistently populated (e.g., "Ready for Flight Testing," "More Info Requested," "Passed"); indicates structured test workflow
- **Blockers Noted:** Multiple completed tasks marked "More Info Requested" (S10022 Test Flights, S10021 VTOL QC, S0 VTOL, S0-MAD) suggest pending information or decision points
- **Known Issues:** 
  - S10020: repeated "Hardware fault error" on startup with updated firmware (8/21)
  - S10020 ESC: power loss immediately post-transition hover→forward flight
  - S0 VTOL: transient MAG signal issues; parameters not saving on update
  - ERAU E2: instability issue unresolved despite testing with/without wind sensor mast
- **No Financial Data:** No dollar amounts visible in task data
- **QC Flag Usage:** Some tasks require/exempt QC review; pattern not consistent across all tasks

**Release Candidates:** Project appears to be validating multiple firmware and hardware candidates (FW0001, FW0002, S-series, E-series variants) across fixed-wing and VTOL platforms, plus Swiftab app.