_Asana snapshot as of 2026-11-04: 45 open tasks, 0 completed (last 90 days)._

# [001-04] S0 VTOL IRAD

## Overview
- **Owner:** Alex Lomis
- **Team:** Whole BST team (Jack Elston, Josh Waldman, Spencer Hoehl, Ethan Domagala, and others)
- **Dollar value:** Not specified in task data
- **Timeline:** 
  - Status update as of Feb 21, 2024
  - Immediate: Hover testing planned for week of Feb 26, 2024
  - Key milestones span through March 2027 (Pack and Deliver due 2027-03-26)
- **Status:** Active R&D, progressing toward flight testing
- **Priority:** Low (per custom field)

## Risk Signals
- **Overdue tasks:** "Identify motor imbalance bug" due 2026-02-20 (date appears to be in past relative to Feb 2024 status)
- **Process gap identified (per Daniel Prendergast, 2026-10-19/20):** No well-defined process for transitioning proposed system builds into production pipeline. This may impact delivery milestones (Barbados S0 due 2025-06-13, ERAU S0 due 2025-04-30, NOAA (2) unscheduled).
- **Structural concern (per Maciej, 2026-10-27):** Active R&D restructuring underway to improve visibility and align Asana with physical Kanban board execution. Two-level planning model being implemented with 6-month rolling milestone plan.

## Key Deliverables & Milestones

| Milestone | Owner | Due Date | Status |
|-----------|-------|----------|--------|
| Hover Test With Updated Avionics | Alex Lomis | 2026-12-18 | Open (avionics fitment, DFM checks, and parts ordering all due 2026-11-06) |
| Build up new avionics | Jack Elston | 2026-11-27 | Open |
| Build guides/work instructions | Josh Waldman | 2027-01-29 | Open |
| 50 transition flights | Spencer Hoehl | 2027-01-29 | Open |
| Pack and Deliver | Ethan Domagala | 2027-03-26 | Open |
| Visual Observation Bench Test | Alex Lomis | 2026-04-30 | Open (unassigned subtasks) |
| Instrumented Bench Test | Alex Lomis | 2026-05-15 | Open (unassigned subtasks) |
| Instrumented Flight Test | Alex Lomis | 2026-06-05 | Open (unassigned subtasks, includes parachute system development) |
| Autopilot-Based Bench Test Rig | Alex Lomis | No due date | Open (unassigned subtasks) |
| ERAU S0 Delivery | Unassigned | 2025-04-30 | Open |
| Barbados S0 Delivery (1) | Unassigned | 2025-06-13 | Open |
| NOAA (2) | Alex Lomis | No due date | Open |

## Task Summary

**Total Tasks:** 45 open, 0 completed

**Tasks by Assignee:**
- **Alex Lomis:** ~22 tasks (design, testing, avionics integration, assembly refinements)
- **Jack Elston:** 4 tasks (DFM checks, avionics ordering, build-up, design updates, Remote ID)
- **Josh Waldman:** 1 task (build guides)
- **Spencer Hoehl:** 1 task (transition flights)
- **Ethan Domagala:** 1 task (pack and deliver)
- **Unassigned:** ~15 tasks (mostly subtasks under Instrumented Bench Test, Instrumented Flight Test, and Autopilot-Based Bench Test milestones; also motor imbalance bug, build another S0-VTOL, and major delivery milestones)

**Completion Rate:** 0% (all tasks open)

**Notable Patterns:**
- Heavy design and refinement work assigned to Alex Lomis (integration, mounting, materials, wiring)
- Most bench and flight testing subtasks are unassigned despite parent milestones having dates
- Three customer deliveries are tracked (ERAU, Barbados, NOAA) but critical ownership/assignment is missing
- Substantial investigative work on payload systems (ISR, radar, temperature sensing, Remote ID)

## Recent Activity

**As of Feb 21, 2024 Status Update:**
- Completed some preparatory tasks (links provided but details not listed)
- **Immediate next step:** Begin hover testing the week of Feb 21, 2024
- **Current focus:** Integrating new avionics stack with Dec 18 target for hover test

**Per Team Feedback (Oct 2026):**
- Daniel Prendergast flagged process gap: no formal pipeline for transitioning proposed builds (e.g., LMUK project with 2×S0-AD Magnetometer + 2×S0-AD Camera + 2×S0-AD variants) into production (Oct 19–20, 2026)
- Maciej initiated Asana restructuring to align with Kanban board and implement 6-month rolling milestone planning (Oct 27, 2026)
- S0 Production QC Website (tracking S0-AD orders) exists but does not yet provide holistic view of all planned production; potential to extend (Oct 20, 2026)

## Notes & Context

1. **Avionics Integration Path:** Near-term work (Nov 2026) focuses on physical fit verification, DFM checks, and component ordering. Avionics build-up due Nov 27, 2026, followed by hover test Dec 18, 2026.

2. **Testing Complexity:** Instrumented testing roadmap is detailed but largely unassigned. Includes development of:
   - eRPM sensor and Teensy logging firmware
   - Flight parachute recovery system
   - Long-duration bench and flight validation with data analysis

3. **Design Debt & Open Questions:** Alex Lomis maintains an extensive backlog of design investigations (battery management, motor imbalance, IR sensors, radar landing, autopilot mounting, wiring standards, nose material, landing gear integration) — many without due dates. Suggests active optimization phase.

4. **Customer Delivery Risk:** ERAU (2025-04-30) and Barbados (2025-06-13) deliveries are scheduled but unassigned; NOAA (2) has no due date. Absent clear ownership and a formalized transition process (per Daniel Prendergast's Oct 2026 feedback), these may slip or conflict with internal development milestones.

5. **Organizational Context:** Maciej's Oct 2026 feedback indicates BST is restructuring R&D planning to improve visibility and synchronize Asana (long-term milestones) with physical Kanban (weekly execution). This project is likely part of that transition.