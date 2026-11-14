_Asana snapshot as of 2026-11-14: 42 open tasks, 3 completed (last 90 days)._

# S0 VTOL IRAD

## Overview
- **Project Type:** Internal R&D (IRAD) — S0 VTOL development platform
- **Owner:** Alex Lomis
- **Team:** BST whole team (primary contributors: Alex Lomis, Jack Elston, Spencer Hoehl, Sam Hild, Ali Sulehria, Josh Waldman, Ethan Domagala, and others)
- **Status:** Active development with near-term production milestones
- **Risk Signal:** Process gap identified (Oct 2026) — no well-defined transition from proposed system builds into production pipeline. Daniel Prendergast flagged this as affecting customer projects like LMUK (requiring 2× S0-AD with Magnetometer, 2× S0-AD with Camera, etc.)
- **Additional Context:** Team restructuring planned (Oct 2026, Maciej) to simplify active R&D projects; shifting to two-level planning (Asana for long-term milestones + 6-month rolling plan; Kanban board for weekly execution). Production tracking via S0 Production QC Website (manages S0-AD orders, quantities, due dates).

## Key Deliverables & Milestones

| Milestone | Owner | Due Date | Status |
|-----------|-------|----------|--------|
| Build up new avionics/bench test | Jack Elston | 2026-12-04 | Open (48h estimated work) |
| Integrate new avionics into platform | Alex Lomis | 2026-12-11 | Open (subtasks: fuse mod, integration, final QC) |
| 50 transition flights | Spencer Hoehl | 2026-12-18 | Open (40h estimated) |
| Pack and Deliver | Ethan Domagala | 2026-12-21 | Open (8h estimated) |
| Build guides/work instructions | Josh Waldman | 2027-01-01 | Open |
| Visual Observation Bench Test | Alex Lomis | 2026-04-30 | Open (2 subtasks unassigned) |
| Instrumented Bench Test | Alex Lomis | 2026-05-15 | Open (6 subtasks unassigned) |
| Instrumented Flight Test | Alex Lomis | 2026-06-05 | Open (8 subtasks unassigned, includes parachute integration) |
| Autopilot-Based Bench Test Rig for Future Testing | Alex Lomis | No due date | Open (2 subtasks unassigned) |
| ERAU S0 Delivery | Unassigned | 2025-04-30 | Open |
| Barbados S0 Delivery (1) | Unassigned | 2025-06-13 | Open |
| NOAA (2) | Alex Lomis | No due date | Open |

## Task Summary

**Totals:**
- Open: 42 tasks
- Completed: 3 tasks (as of Feb 21, 2024 / recent snapshot)
- Completion rate: ~7%

**Tasks by Assignee (Open):**
- **Alex Lomis:** 24 tasks (design/integration/architecture focus: battery design, autopilot mounting, sonde electronics, wiring, assembly guides, testing fixes, design updates)
- **Jack Elston:** 3 tasks (avionics bench test, design updates, Remote ID)
- **Spencer Hoehl:** 1 task (50 transition flights)
- **Ethan Domagala:** 1 task (pack and deliver)
- **Josh Waldman:** 1 task (build guides/work instructions)
- **Sam Hild:** 1 task (Electronics Engineer Bench Test)
- **Ali Sulehria:** 1 task (Test Engineer Bench Test; another: Final QC and test checkout)
- **Unassigned:** 9 tasks (motor imbalance bug, build another S0-VTOL, most instrumented bench test subtasks, customer deliveries)

**Notable Patterns:**
- **Heavy assignment to Alex Lomis** — dominates design/integration/optimization work; many open tasks lack owners
- **Unassigned critical items** — 50 transition flights, customer deliveries (ERAU, Barbados, NOAA), and most instrumented testing subtasks have no owner
- **High technical debt** — 20+ design/optimization tasks (aileron control horn, battery design, wiring, nose material, radar integration, etc.) with no due dates
- **Recent activity (Feb 21, 2024):** Status update indicated readiness to begin hover testing next week; 3 tasks recently completed (avionics ordering, DFM checks, fit verification)

## Recent Activity
- **2026-11-04:** Three tasks completed (Order S0-VTOL avionics stacks, Finish DFM checks, Ensure new avionics stack fits in OnShape)
- **2026-12-04:** Near-term critical path — avionics bench test due (Jack Elston, Sam Hild, Ali Sulehria)
- **2026-12-18:** 50 transition flights due (Spencer Hoehl) — 40h estimated
- **2026-12-21:** Pack and Deliver due (Ethan Domagala)
- **2025 Customer Deliveries:** ERAU (2025-04-30) and Barbados (2025-06-13) remain open with no assigned owners

## Notes & Context

**Key Process Issue (Daniel Prendergast, Oct 19-20, 2026):**
> "Currently we don't have a well-defined process for transitioning proposed system builds/deliveries into the production pipeline. For example, Beck and I have been talking with LMUK for a few months to define our project with them, and on that project we will need to produce and deliver 2 × S0-AD with Magnetometer, 2 × S0-AD with Camera..."

This identifies a critical gap: customer projects are being negotiated in parallel with R&D but lack clear intake into production planning.

**Production Tracking:**
- S0 Production QC Website (built by Jack) tracks S0-AD orders only; "Orders" tab shows customer orders, quantities, and due dates
- No holistic spreadsheet for planned production across all platforms (per Daniel Prendergast, Oct 20, 2026)
- Potential future extension: expand QC website to cover broader product portfolio

**Asana Restructuring (Maciej, Oct 27, 2026):**
- Two-level planning: Asana → long-term milestones & weekly task planning; Kanban board → weekly engineering execution
- Goal: simplify visibility, tie R&D projects to Kanban workflow
- 6-month rolling milestone plan to be implemented

**Priority:** Low (custom field)

**Overdue/Risky Tasks:**
- "Identify motor imbalance bug" — Due 2026-02-20 (significantly overdue, unassigned)
- "Build up another S0-VTOL" — Due 2026-03-04 (likely overdue)
- Customer deliveries (ERAU/Barbados) lack owners and sit in 2025 with no clear status