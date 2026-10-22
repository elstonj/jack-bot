# [001-14] SwiftCore 3.3

## Overview
- **Client/customer**: Internal BST development project
- **Dollar value**: Not specified
- **Timeline**: Active development branch; no target release date specified
- **Status**: **ACTIVE DEVELOPMENT.** As of Nov 28, 2023: **10 open tasks, 2 completed** in this snapshot. Project shows ongoing simulator-driven bug intake and resolution. Note: timestamp inconsistency in raw data (Nov 2023 status vs. Oct 2026 task completion dates) suggests data import lag or concurrent development cycles. Current work dominated by S3 simulator sensor/flight logic issues and critical GPS/throttle response bugs.
- **Team members**: Jack Elston (owner), Maciej Stachura (primary developer), BST team
- **Risk signals**: 
  - **10 open tasks with no due dates** — work is unscheduled; priority unclear (custom field: Low)
  - Critical GPS error escalation blocking joystick mode abort (emergency descent cannot be prevented)
  - S2 throttle kill response delayed; emergency descent triggers "bad flight plan" error
  - Multiple S3 simulator sensor failures in flying mode (GPS, pitot, mags, static pressure) with unclear response logic
  - High-altitude false IAS alarm (SIM-0028) on healthy pitot at 4–5 km

## Key Deliverables & Milestones

**Open Milestones:**
- Adds initial VTOL support (unassigned, no due date)

**Completed Milestones (Oct 2026):**
- S3 model ground contact carry-over (Maciej Stachura, 2026-10-22)
- S3 BAD IAS false alarm at altitude (Maciej Stachura, 2026-10-22)

## Task Summary
- **Total tasks**: 10 open, 2 completed (Nov 28, 2023 snapshot)
- **Tasks by assignee**:
  - **Maciej Stachura**: 8 open (all S3 simulator sensor issues: lost GPS in flying mode, killed engine stall, clogged pitot, pitot loss in flying mode, mags loss, static pressure loss, climbout clogged pitot); 2 completed
  - **Jack Elston**: 2 open (critical GPS/PDOP error escalation preventing abort, S2 throttle kill response with emergency descent / "bad flight plan" error)
  
- **Notable patterns**:
  - **Sensor failure focus**: 8 of 10 open tasks are S3 simulator sensor loss/degradation scenarios (GPS, pitot, mags, static pressure)
  - **Critical path bugs**: Both Jack Elston tasks represent high-impact failure modes (GPS error prevents emergency descent abort; throttle kill triggers cascading errors)
  - **No due dates** — work prioritized by team triage

## Recent Activity
**Completed (2026-10-22):**
- S3 JSBSim model ground contact preservation (Maciej Stachura) — prevents loss of belly/tail-fin ground reactions on model regeneration
- S3 BAD IAS false alarm resolution (Maciej Stachura) — from simulator bug report SIM-0028; confirmed no active simulator faults when alarm triggered at 4–5 km altitude

**Active unresolved critical issues:**
- **GPS/PDOP error cascade** (Jack Elston): Low PDOP warning → critical error commanding emergency descent → joystick mode cannot prevent entry into emergency descent
- **S2 throttle kill response** (Jack Elston): Delayed "loss of motor power" warning (only after 30m altitude loss); emergency descent selection triggers map error point and "bad flight plan" error
- **S3 sensor loss in flying mode** (Maciej Stachura): 6 open tasks covering GPS loss, pitot blockage/loss, mag loss, static pressure loss, engine stall — all with "unexpected response" noted; unclear what correct behavior should be

## Notes & Context
- **Data timestamp anomaly**: Status update dated Nov 28, 2023 but task completion dates Oct 2026. Treat task dates (Oct 2026) as authoritative work timeline.
- **Simulator-driven development**: All open work stems from S3/S2 simulator testing. Heavy focus on sensor failure modes and flight logic robustness.
- **Critical vs. scheduled work**: Custom field priority is "Low," but GPS error blocking abort and throttle kill error cascade represent **medium-to-high tactical risk** for flight safety validation.
- **Scope clarity needed**: S3 sensor loss tasks lack detail on expected behavior vs. observed response; may benefit from clearer acceptance criteria (e.g., "should revert to nav mode" vs. "should trigger alert and hold current mode").
- **Release readiness**: No target date. Current work is stabilization/robustness; new feature milestones (VTOL support) are open but not active.