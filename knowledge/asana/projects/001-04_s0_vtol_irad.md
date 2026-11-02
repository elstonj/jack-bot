_Asana snapshot as of 2026-11-02: 45 open tasks, 0 completed (last 90 days)._

# S0 VTOL IRAD

## Overview
- **Client/Customer**: Internal R&D (IRAD) with external delivery commitments (ERAU, NOAA, Barbados)
- **Status**: Active but with significant process and coordination gaps. As of Feb 21, 2024, team was preparing to begin hover testing with updated avionics. **⚠️ PROCESS GAP ALERT** (per Daniel Prendergast, 2026-10-19): No well-defined process exists for transitioning proposed system builds into production pipeline. Future customer orders (e.g., LMUK: 2× S0-AD with Magnetometer, 2× S0-AD with Camera, 2× S0-AD TBD) lack clear intake/handoff procedures.
- **Team**: Alex Lomis (lead/design owner), Jack Elston, Josh Waldman, Spencer Hoehl, Ethan Domagala, plus wider BST team
- **Priority**: Low (custom field)
- **Risk Signals**: 
  - **Overdue task**: "Identify motor imbalance bug" (due 2026-02-20, far in past)
  - **Approaching deadline**: "Build up another S0-VTOL" (due 2026-03-04)
  - 45 open tasks with 0 completed; many milestones have no due dates despite sequential dependencies

## Key Deliverables & Milestones

| Milestone | Owner | Due Date | Status |
|-----------|-------|----------|--------|
| **Hover Test With Updated Avionics** | Alex Lomis | No date | Prep phase (avionics fitment check, DFM, electronics order due 2026-11-06) |
| **50 Transition Flights** | Spencer Hoehl | No date | Blocked pending hover test |
| **Visual Observation Bench Test** | Alex Lomis | 2026-04-30 | Not started (subtasks unassigned) |
| **Instrumented Bench Test** | Alex Lomis | 2026-05-15 | Not started (eRPM sensors, firmware, integration TBD) |
| **Instrumented Flight Test** | Alex Lomis | 2026-06-05 | Not started (parachute recovery system required) |
| **Autopilot-Based Bench Test Rig** | Alex Lomis | No date | Future capability (unassigned) |
| **ERAU S0 Delivery** | Unassigned | 2025-04-30 | ⚠️ **Past due** (appears stale—no recent updates) |
| **Barbados S0 Delivery (1)** | Unassigned | 2025-06-13 | ⚠️ **Past due** (appears stale—no recent updates) |
| **NOAA (2)** | Alex Lomis | No date | Undefined timeline |

## Task Summary

- **Total Open Tasks**: 45 (0 completed)
- **Assignments by Owner**:
  - **Alex Lomis**: ~26 tasks (design, avionics integration, bench/flight testing, component development)
  - **Jack Elston**: 4 tasks (DFM, electronics ordering, design updates, Remote ID)
  - **Josh Waldman**: 1 task (Build guides/work instructions)
  - **Spencer Hoehl**: 1 task (50 transition flights)
  - **Ethan Domagala**: 1 task (Pack and Deliver)
  - **Unassigned**: 12 tasks (including all subtasks under bench/flight milestones, motor imbalance debug, second S0 build, ISR payload, customer deliveries)

- **Notable Patterns**:
  - Heavy design/integration load on Alex Lomis; most subtasks unassigned despite sequential dependencies
  - Many tasks lack due dates, creating scheduling ambiguity
  - ERAU and Barbados delivery milestones appear stale (dated 2025); current Asana data does not reflect whether these have been delivered, rescheduled, or cancelled

## Recent Activity

**Feb 21, 2024** (last status update): "Should be able to begin hover testing next week." Two completed task references (URLs provided).

**Current Status** (inferred Oct 2026): 
- Near-term focus: Complete avionics fitment verification, DFM checks, and electronics procurement (all due 2026-11-06)
- Build up and avionics assembly milestones are next
- No evidence of completion on earlier delivery milestones (ERAU, Barbados) — status unclear; assume these dates are stale

**Asana has not been updated recently relative to the Feb 2024 status note.**

## Notes & Context

### Process & Coordination Gaps
Per **Daniel Prendergast (2026-10-19/20)**, the team lacks a defined process for transitioning proposed customer builds into production:
- LMUK project discussions ongoing for months; production needs (2× S0-AD with Magnetometer, 2× S0-AD with Camera, 2× S0-AD TBD) not yet formalized in production pipeline
- No holistic production planning spreadsheet; closest reference is the **S0 Production QC Website** (built by Jack Elston) currently tracking only S0-AD orders with an "Orders" dashboard and add-order button
- Recommendation: Extend QC website or create formal intake/prioritization process before committing to customer deliveries

### Asana Restructuring Plan
Per **Maciej (2026-10-27)**, planned simplification:
- **Two-level planning**: Asana tracks long-term milestones + weekly tasks; physical Kanban board manages weekly engineering execution
- **6-month rolling milestone plan**: To be implemented (discussion scheduled)

### Design & Engineering Focus
Alex Lomis owns most component/integration work:
- Avionics integration, battery design, autopilot mounting, sonde mounting, wiring standardization
- Ongoing design iterations (motor boom drill jig, aileron control horn, non-yellowing nose material, radar vs. laser landing system)
- Assembly/documentation needs (guides, wiring channels, harness design)

### External Dependencies
- Avionics stack fit/order (Jack Elston, due 2026-11-06)
- 3D printing samples from CraftCloud3D (component TBD by Alex Lomis)
- Parachute system (sizing and integration for flight safety)

### ⚠️ High Uncertainty
- Customer delivery dates (ERAU 2025-04-30, Barbados 2025-06-13) are likely stale; unclear whether delivered, delayed, or cancelled
- NOAA (2) has no timeline
- Most flight-test subtasks (Visual Observation, Instrumented Bench, Instrumented Flight) are unassigned and lack concrete start dates despite sequential dependencies