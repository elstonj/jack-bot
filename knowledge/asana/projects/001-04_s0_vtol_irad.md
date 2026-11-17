_Asana snapshot as of 2026-11-17: 42 open tasks, 3 completed (last 90 days)._

# [001-04] S0 VTOL IRAD

## Overview
- **Client/Customer:** Internal IRAD (Internal Research and Development) — multi-customer platform (NOAA, ERAU, Barbados noted as future deliveries)
- **Dollar Value:** Not specified in custom fields
- **Timeline:** 
  - Current focus: Hover testing (starting week of Feb 26, 2024)
  - Near-term milestones: Dec 2026 (avionics build/integration, 50 transition flights, delivery)
  - Future deliveries: ERAU (Apr 30, 2025), Barbados (Jun 13, 2025), NOAA (no date)
- **Status:** [YELLOW] Active development. As of Feb 21, 2024, two tasks recently completed; hover testing to begin imminently.
- **Team Members:** Alex Lomis (owner, lead), Jack Elston, Sam Hild, Ali Sulehria, Spencer Hoehl, Ethan Domagala, Josh Waldman
- **Priority:** Low (custom field)
- **Risk Signals:** 
  - "Identify motor imbalance bug" is overdue (due Feb 20, 2024)
  - Many critical milestones have no assignees (e.g., most subtasks under Instrumented Bench/Flight Test, Autopilot-Based Bench Rig)
  - Significant unassigned work on ISR Payload, Visual Observation Bench Test, Instrumented Bench Test (6 subtasks), Instrumented Flight Test (8 subtasks)
  - Customer delivery dates approaching (ERAU Apr 30, 2025; Barbados Jun 13, 2025) with many foundational tasks still unassigned

## Key Deliverables & Milestones

| Milestone | Assignee | Due Date | Status | Subtasks |
|-----------|----------|----------|--------|----------|
| Build up new avionics/bench test | Jack Elston | Dec 4, 2026 | Open | 2 (16h Elec Eng, 24h Test Eng) |
| Integrate new avionics into platform | Alex Lomis | Dec 11, 2026 | Open | 3 (fuse mod, power-up, QC; 32h total) |
| 50 transition flights | Spencer Hoehl | Dec 18, 2026 | Open | 40h Test Eng |
| Pack and Deliver | Ethan Domagala | Dec 21, 2026 | Open | 8h Technician |
| Build guides/work instructions | Josh Waldman | Jan 1, 2027 | Open | — |
| Visual Observation Bench Test | Alex Lomis | Apr 30, 2026 | Open | 2 (sinusoidal, crash replay) — **unassigned** |
| Instrumented Bench Test | Alex Lomis | May 15, 2026 | Open | 6 subtasks — **all unassigned** (sensor selection, firmware, install, long test, log analysis, repeat) |
| Instrumented Flight Test | Alex Lomis | Jun 5, 2026 | Open | 8 subtasks — **all unassigned** (integration, bench test, log analysis, parachute design, parachute integration, hover w/ instrumentation, full flight test) |
| Autopilot-Based Bench Test Rig for Future Testing | Alex Lomis | No due date | Open | 2 — **unassigned** |
| ERAU S0 Delivery | Unassigned | Apr 30, 2025 | Open | — |
| Barbados S0 Delivery (1) | Unassigned | Jun 13, 2025 | Open | — |
| NOAA (2) | Alex Lomis | No due date | Open | — |

## Task Summary

- **Total:** 42 open, 3 completed (93% open rate)
- **Tasks by Assignee:**
  - **Alex Lomis:** ~24 tasks (mix of milestones, design/engineering decisions, most without due dates)
  - **Jack Elston:** 3 tasks (2 completed; avionics build, design updates, Remote ID)
  - **Spencer Hoehl:** 1 task (50 transition flights)
  - **Ethan Domagala:** 1 task (pack/deliver)
  - **Josh Waldman:** 1 task (build guides)
  - **Sam Hild:** 1 task (electronics bench test)
  - **Ali Sulehria:** 1 task (test engineer bench test, final QC)
  - **Unassigned:** ~14 tasks (critical path: ISR Payload, most bench/flight test subtasks, both customer deliveries, autopilot bench rig)

- **Completion Rate:** 7% (3/45 tasks) — project heavily weighted toward future work

- **Notable Pattern:** 
  - Most design exploration and open-ended engineering tasks assigned to Alex Lomis with no due dates (motor imbalance, aileron mount, battery design, wire management, autopilot mounting, etc.)
  - Critical test and delivery milestones (Instrumented Flight Test, customer deliveries) have no assigned personnel
  - Heavy use of estimated hours in custom fields for labor tracking

## Recent Activity

- **Feb 21, 2024 Status Update:** "Should be able to begin hover testing next week" (week of Feb 26)
- **Feb 2024 Completed:**
  - Order S0-VTOL avionics stacks (Jack Elston, completed Nov 4, 2026)
  - Finish DFM checks (Jack Elston, completed Nov 4, 2026)
  - Ensure new avionics stack physically fits (Alex Lomis, completed Nov 4, 2026)
- **Overdue:** "Identify motor imbalance bug" (due Feb 20, 2024)

## Notes & Context

- **Project Nature:** Development of a VTOL UAS platform (S0) with progression from bench testing through instrumented flight testing to multi-unit customer delivery
- **Testing Roadmap:** Heavily structured with multiple validation phases (visual observation → instrumented bench → instrumented flight → operational delivery), but most subtasks lack assignment and owners
- **Design Maturity:** Many open-ended design decisions flagged (motor imbalance, optimal battery config, landing sensor strategy, autopilot mounting, wiring standardization, Remote ID solution), suggesting ongoing design refinement concurrent with testing
- **Staffing Risk:** Customer delivery dates (ERAU Apr 30, 2025; Barbados Jun 13, 2025) are ~11 months away but no detailed plan or assignment; most flight-test infrastructure (instrumentation, parachute, logging) is unassigned and far down the queue
- **Low Priority Flag:** Despite aggressive near-term customer commitments, project is marked Priority: Low — may indicate resource constraints or sequencing behind higher-priority initiatives