_Asana snapshot as of 2026-11-15: 42 open tasks, 3 completed (last 90 days)._

# S0 VTOL IRAD

## Overview
- **Client/Customer:** Internal R&D (IRAD — Independent Research and Development)
- **Dollar Value:** Not specified in project data
- **Timeline:** 
  - Active development phase: Nov 2026 – Jan 2027 (near-term milestones)
  - Long-term deliveries: Apr–Jun 2025 (ERAU, NOAA, Barbados)
  - **⚠️ Date anomaly:** Some milestones show 2025 due dates despite current data from 2026; likely aspirational or stale
- **Status:** ACTIVE — Intensive development underway; avionics bench testing and integration scheduled through December 2026
- **Team Members:** Alex Lomis (owner/lead), Jack Elston, Sam Hild, Ali Sulehria, Spencer Hoehl, Ethan Domagala, Josh Waldman
- **Priority:** Low (custom field)

## Key Deliverables & Milestones

| Milestone | Owner | Due Date | Status |
|-----------|-------|----------|--------|
| Build up new avionics/bench test | Jack Elston | 2026-12-04 | Open (40h estimated) |
| Integrate new avionics into platform | Alex Lomis | 2026-12-11 | Open (32h estimated) |
| 50 transition flights | Spencer Hoehl | 2026-12-18 | Open (40h estimated) |
| Pack and Deliver | Ethan Domagala | 2026-12-21 | Open (8h estimated) |
| Build guides/work instructions | Josh Waldman | 2027-01-01 | Open |
| Visual Observation Bench Test | Alex Lomis | 2026-04-30 | Open, unassigned |
| Instrumented Bench Test | Alex Lomis | 2026-05-15 | Open, unassigned (6 subtasks) |
| Instrumented Flight Test | Alex Lomis | 2026-06-05 | Open, unassigned (8 subtasks) |
| ERAU S0 Delivery | — | 2025-04-30 | Open, unassigned |
| Barbados S0 Delivery (1) | — | 2025-06-13 | Open, unassigned |
| NOAA (2) | Alex Lomis | No due date | Open |

## Task Summary

**Completion:** 3 completed / 42 open = **7% completion rate**

**Recent Completions (Nov 4, 2026):**
- Order S0-VTOL avionics stacks and other required electronics
- Finish DFM checks
- Ensure new avionics stack physically fits within S0-VTOL design

**Tasks by Assignee (open only):**
| Assignee | Open Tasks | Notes |
|----------|-----------|-------|
| Alex Lomis | 20+ | Heavy load: integration, design iterations, component specs, assembly guidance |
| Jack Elston | 3 | Avionics bench test, design updates, Remote ID solution |
| Unassigned | 15+ | Critical path items: bench tests, flight tests, payload integration, customer deliveries |
| Sam Hild | 1 | Electronics bench test (due 2026-12-04) |
| Ali Sulehria | 2 | Test bench & final QC (due 2026-12-04, 2026-12-11) |
| Spencer Hoehl | 1 | 50 transition flights (due 2026-12-18) |
| Ethan Domagala | 1 | Pack and deliver (due 2026-12-21) |
| Josh Waldman | 1 | Build guides/work instructions (due 2027-01-01) |

**Notable Patterns:**
- **Heavy unassigned load** on critical path (bench tests, flight tests, customer deliveries)
- **Alex Lomis carries most design/integration work** — potential bottleneck
- **Overdue task:** "Identify motor imbalance bug" (due 2026-02-20, now open)
- **Stale task:** "Build up another S0-VTOL" (due 2026-03-04, now open)
- **No custom field usage for $ tracking**

## Recent Activity

**Latest Status Update:** Feb 21, 2024 — "Should be able to begin hover testing next week" (outdated; subsequent activity shows avionics procurement/integration ongoing as of Nov 2026)

**Recent Completions (Nov 4, 2026):**
- Avionics stack procurement completed
- DFM validation complete
- Physical fit confirmed in CAD

**Upcoming Pressure Points:**
- **Dec 4, 2026:** Avionics bench test gate (Sam Hild, Ali Sulehria)
- **Dec 11, 2026:** Avionics integration complete (Alex Lomis)
- **Dec 18, 2026:** 50 transition flights (Spencer Hoehl) — aggressive timeline
- **Dec 21, 2026:** Pack and deliver
- **Jan 1, 2027:** Documentation and guides due

## Notes & Context

### Process Gap (Daniel Prendergast, Oct 19–20, 2026)
**Quote:** "Currently we don't have a well-defined process for transitioning proposed system builds/deliveries into the production pipeline."

*Context:* LMUK project (mentioned as example) requires 2×S0-AD Magnetometer, 2×S0-AD Camera plus additional variants. This IRAD feeds into production, but handoff process is unclear.

### Production Tracking & Tooling (Daniel Prendergast, Oct 20, 2026)
No centralized spreadsheet tracks all planned production. The **S0 Production QC Website** (built by Jack, <https://qc.bst.aero/>) is the closest artifact — currently tracks S0-AD orders only with an "Orders" dashboard (quantities, due dates, add-new-order button). Potential future extension to holistic tracking.

### Asana Restructuring (Maciej, Oct 27, 2026)
**Planned change:** Two-level planning system:
- Asana: long-term milestones + upcoming weekly tasks
- Physical Kanban board: weekly engineering execution
- 6-month rolling milestone plan TBD

*Impact:* This Asana project may be restructured; verify alignment with Kanban board.

### Design Maturity
Project contains **18+ open design/research tasks** (unassigned, no due dates):
- Motor imbalance investigation
- Battery/power distribution (4S2P vs. 2×2 design)
- Landing sensor strategy (laser vs. radar)
- ESC telemetry, autopilot mounting, wiring harness standardization
- Non-yellowing nose material
- IR temp sensor necessity

These are foundational but not on critical path to Dec 2026 delivery.

### Customer Deliveries
- **ERAU S0** — due 2025-04-30 (likely stale; before current date)
- **Barbados S0** — due 2025-06-13 (likely stale)
- **NOAA (×2)** — no due date

*Recommend clarification:* Are these 2025 dates aspirational, rescheduled, or archived?