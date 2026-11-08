_Asana snapshot as of 2026-11-08: 42 open tasks, 3 completed (last 90 days)._

# [001-04] S0 VTOL IRAD

## Overview
- **Project Owner:** Alex Lomis
- **Team:** Black Swift Technologies (whole team)
- **Status:** Active R&D project with long development cycle; internally recognized as needing process improvements for production transition
- **Priority:** Low (per custom field)
- **Key Context:** This is an internal R&D effort (IRAD = Independent Research and Development) to develop the S0 VTOL platform. The team has identified a critical process gap: no well-defined workflow for transitioning proposed system builds/deliveries into production pipeline (flagged by Daniel Prendergast, 2026-10-20).

## Key Deliverables & Milestones

| Milestone | Owner | Due Date | Status |
|-----------|-------|----------|--------|
| Build up new avionics | Jack Elston | 2026-11-27 | Open |
| Hover Test With Updated Avionics | Alex Lomis | 2026-12-18 | Open |
| Visual Observation Bench Test | Alex Lomis | 2026-04-30 | Open |
| Instrumented Bench Test | Alex Lomis | 2026-05-15 | Open |
| Instrumented Flight Test | Alex Lomis | 2026-06-05 | Open |
| 50 transition flights | Spencer Hoehl | 2027-01-29 | Open |
| Build guides/work instructions | Josh Waldman | 2027-01-29 | Open |
| Pack and Deliver | Ethan Domagala | 2027-03-26 | Open |
| ERAU S0 Delivery | Unassigned | 2025-04-30 | Open |
| Barbados S0 Delivery (1) | Unassigned | 2025-06-13 | Open |
| NOAA (2) | Alex Lomis | No due date | Open |

**Recent Completions (Nov 2026):**
- Order S0-VTOL avionics stacks and other required electronics (Jack Elston, completed 2026-11-04)
- Finish DFM checks (Jack Elston, completed 2026-11-04)
- Ensure new avionics stack physically fits within S0-VTOL design (Alex Lomis, completed 2026-11-04)

## Task Summary

- **Total Tasks:** 42 open, 3 completed
- **Completion Rate:** ~7% (3 of 45 total)
- **Tasks by Assignee:**
  - **Alex Lomis:** 23 tasks (mostly open design/testing subtasks and engineering decisions)
  - **Jack Elston:** 4 tasks (avionics build, design updates, Remote ID)
  - **Josh Waldman:** 1 task (build guides)
  - **Spencer Hoehl:** 1 task (transition flights)
  - **Ethan Domagala:** 1 task (pack and deliver)
  - **Unassigned:** 12 tasks (including subtasks under bench/flight testing milestones and customer deliveries)

- **Notable Patterns:**
  - Heavy design and engineering workload concentrated on Alex Lomis
  - Large subtask trees under testing milestones (bench test, flight test, autopilot rig) with no assignees—indicates planning-phase work not yet staffed
  - Multiple unassigned delivery milestones (ERAU, Barbados, NOAA) suggest customer commitments not yet resourced
  - Many open tasks lack due dates, indicating backlog/design consideration items

## Recent Activity

- **Feb 21, 2024 Status Update:** Ready to begin hover testing (per original status note, though timeline appears to have shifted)
- **Nov 4, 2026:** Avionics stack ordered and design fit-check completed; cleared path for hover testing milestone (due 2026-12-18)
- **Oct 2026 Team Feedback:** Daniel Prendergast and Maciej flagged critical organizational issues:
  - **Production transition gap:** No defined process for moving proposed builds into production pipeline (Daniel Prendergast, 2026-10-20)
  - **Visibility gap:** No holistic view of planned production; S0 Production QC Website exists but only tracks S0-AD orders; lacks broader production planning (2026-10-20)
  - **Asana restructuring planned:** Maciej proposing two-level planning—Asana for long-term milestones + weekly tasks; physical Kanban board for weekly execution; 6-month rolling milestone plan (2026-10-27)

## Risk Signals & Process Notes

1. **Overdue Tasks:** "Identify motor imbalance bug" was due 2026-02-20 and remains open
2. **Unassigned Critical Path:** Testing milestones (bench, flight, instrumented flight) contain many unassigned subtasks with approaching dates—resource allocation unclear
3. **Customer Delivery Exposure:** ERAU (due 2025-04-30) and Barbados (due 2025-06-13) deliveries are unassigned and past stated due dates in original Asana; requires clarification on actual status
4. **Process Gap (Authoritative):** Per Daniel Prendergast (2026-10-20), BST lacks a well-defined workflow for transitioning research builds into production. Example: LMUK project requires 2× S0-AD with Magnetometer, 2× S0-AD with Camera, etc., but transition process undefined
5. **Organizational Change Pending:** Maciej's proposed Asana restructuring (2026-10-27) indicates current task tracking may not reflect actual execution; physical Kanban board is source of truth for weekly work

## Notes & Context

- **IRAD Nature:** This is internal R&D; no external dollar value specified in Asana
- **Technology Focus:** S0 VTOL avionics integration, autopilot tuning, instrumentation logging, parachute recovery, and assembly/manufacturing process refinement
- **Stakeholders:** Implied customer interest from ERAU, Barbados, NOAA, and LMUK (mentioned in corrections)
- **System Maturity:** Platform is in late design/early testing phase; many open questions on component selection, assembly methods, and manufacturing guides still unresolved
- **Known Production Requirements (from LMUK discussions):** Multiple variants (S0-AD with Magnetometer, S0-AD with Camera) needed, but production planning and supply chain not yet visible in Asana

**Recommendation:** Review actual delivery dates for ERAU and Barbados milestones; confirm whether they have been externally rescheduled. Align Asana structure with Maciej's proposed two-level planning system to improve visibility and reduce process friction for production transition.