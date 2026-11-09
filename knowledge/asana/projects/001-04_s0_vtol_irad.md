_Asana snapshot as of 2026-11-09: 42 open tasks, 3 completed (last 90 days)._

# [001-04] S0 VTOL IRAD

## Overview
- **Client/Customer:** Internal R&D (IRAD); deliveries planned to Barbados, ERAU, and NOAA
- **Team:** Alex Lomis (owner), Jack Elston, Josh Waldman, Spencer Hoehl, Ethan Domagala
- **Timeline:** 
  - Current phase: Hover testing with updated avionics (due 2026-12-18)
  - Final delivery: Pack and Deliver (due 2027-03-26)
  - Known customer commitments: ERAU (2025-04-30), Barbados (2025-06-13) — **these dates are in the past and require clarification**
- **Status:** **ACTIVE** — Recent avionics work completed (2026-11-04); proceeding toward hover testing phase
- **Priority:** Low (per custom field)

---

## Key Issues & Process Gaps

**From Daniel Prendergast (2026-10-19 & 2026-10-20):**  
No well-defined process exists for transitioning proposed system builds/deliveries into the production pipeline. Example cited: LMUK project requires 2× S0-AD with Magnetometer + 2× S0-AD with Camera + 2× additional units, but transition pathway unclear.

**S0 Production QC Website:**  
Jack has built a web dashboard (`qc.bst.aero`) currently tracking S0-AD orders only. "Orders" tab shows customer orders, quantities, and due dates. Daniel suggests this may be extensible to broader production tracking, but no holistic production spreadsheet currently exists.

**Asana Restructuring (Maciej, 2026-10-27):**  
Planned two-level planning model:
- Asana: long-term milestones + weekly upcoming tasks
- Physical Kanban board: weekly engineering execution
- 6-month rolling milestone plan (details cut off in feedback)

---

## Key Deliverables & Milestones

| Milestone | Owner | Due Date | Status |
|-----------|-------|----------|--------|
| Build up new avionics | Jack Elston | 2026-11-27 | Open |
| Hover Test With Updated Avionics | Alex Lomis | 2026-12-18 | Open |
| Visual Observation Bench Test | Alex Lomis | 2026-04-30 | Open (subtasks unassigned) |
| Instrumented Bench Test | Alex Lomis | 2026-05-15 | Open (6 subtasks, all unassigned) |
| Instrumented Flight Test | Alex Lomis | 2026-06-05 | Open (8 subtasks, all unassigned) |
| 50 transition flights | Spencer Hoehl | 2027-01-29 | Open |
| Build guides/work instructions | Josh Waldman | 2027-01-29 | Open |
| Pack and Deliver | Ethan Domagala | 2027-03-26 | Open |
| ERAU S0 Delivery | Unassigned | 2025-04-30 | **OVERDUE** |
| Barbados S0 Delivery (1) | Unassigned | 2025-06-13 | **OVERDUE** |
| NOAA (2) | Alex Lomis | No due date | Open |

---

## Task Summary

- **Total tasks:** 42 open, 3 completed
- **Completion rate:** ~7% (3 of 45 tasks)
- **Recent completions (2026-11-04):**
  - Order S0-VTOL avionics stacks (Jack Elston)
  - Finish DFM checks (Jack Elston)
  - Ensure new avionics stack fits in OnShape (Alex Lomis)

**Tasks by assignee:**
- **Alex Lomis:** 25 open tasks (design, optimization, testing, bench work)
- **Jack Elston:** 3 open (avionics build, design updates, Remote ID)
- **Josh Waldman:** 1 open (build guides)
- **Spencer Hoehl:** 1 open (50 transition flights)
- **Ethan Domagala:** 1 open (pack and deliver)
- **Unassigned:** 11 open (ISR payload, bench test subtasks, two customer deliveries)

**Patterns:**
- Heavy concentration on Alex Lomis for design/optimization work
- Many bench and flight test subtasks unassigned and without due dates
- Customer deliveries (ERAU, Barbados) significantly overdue and unassigned
- Low priority rating suggests this is foundational R&D, not a revenue-critical project at present

---

## Recent Activity

**Completed (2026-11-04):**
- Avionics procurement and DFM validation complete
- New avionics stack confirmed to fit in airframe

**Upcoming (next 30 days):**
- Build up new avionics (due 2026-11-27)
- Hover testing with updated avionics (due 2026-12-18)

**Status note from Feb 21, 2024:** "Should be able to begin hover testing next week" — this appears to be from a prior project phase and is now stale.

---

## Notes & Context

1. **OVERDUE CUSTOMER DELIVERIES:** ERAU (2025-04-30) and Barbados (2025-06-13) are both in the past. These appear to be committed orders without assigned owners or current status. Requires immediate clarification on actual delivery status.

2. **Large backlog of design/optimization tasks:** Alex Lomis owns 25 open tasks spanning design improvements (battery, nose material, autopilot mount), component sourcing, and assembly/wiring optimization. Most have no due dates, suggesting they are backlog or exploratory.

3. **Test phase subtasks mostly unassigned:** Bench test and flight test phases (April–June 2026) have 14 subtasks with no assignee and no individual due dates. This may reflect that detailed execution planning will occur closer to each phase.

4. **Process gap on production transition:** Team is aware that the path from R&D prototype to production orders (e.g., LMUK 6-unit build) is not yet formalized. S0 Production QC Website exists but is S0-AD focused; extension to cover broader builds may be needed.

5. **Kanban restructuring planned:** Expect Asana to shift toward milestone + rolling 6-month planning while weekly execution moves to physical Kanban board.