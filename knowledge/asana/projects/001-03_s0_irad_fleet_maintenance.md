# [001-03] S0 IRAD & Fleet Maintenance

## Overview
- **Client/Customer**: Internal BST research and development
- **Dollar Value**: No specific dollar amounts identified, but includes 2026 funding scope items
- **Timeline**: Long-term project with 2026 funding items; heavy focus on 2026 season readiness
- **Status**: Active - 9 open tasks, 0 completed. Marked "Low" priority despite substantial scope. (Note: Previous knowledge base showed 168 open tasks; this appears to be a filtered or sub-section view)
- **Team Members**: Josh Fromm (project owner/lead), Jack Elston (avionics/firmware/power control), Nate Straus (airframe/AD), 7 unassigned tasks
- **Risk Signals**:
  - All 9 open tasks lack due dates
  - Heavy concentration on Jack Elston (3 assigned power/comms tasks) with no timeline
  - Two critical PSNS power control hardware tasks unassigned
  - Comms issue (2026-04-09) indicates recent operational problem requiring investigation

## Key Deliverables & Milestones
Current task view shows no explicit milestones; see full project knowledge base for 2026 Funding Scope and near-term deadlines (Jan 2-9, 2026).

## Task Summary
- **Total Tasks**: 9 open, 0 completed
- **Tasks by Assignee**:
  - Jack Elston: 3 tasks (LCD status display, channel switching, power-off logic)
  - Unassigned: 6 tasks (GCS sys_init bug, waypoint ETA, comms slowness, PSNS power control hardware)
- **Task Focus** (current open set):
  - **Power Control** (3 tasks): LCD status display, power-off logic, PSNS external pull-down, PSNS PWR_BUTTON routing — Jack Elston driving power architecture refinement
  - **Communications** (2 tasks): Channel switching capability, slow comms on 2026-04-09 — operational issue flagged
  - **Flight Control/GCS** (2 tasks): Rapid sys_init cycling bug, waypoint ETA display
  - **Unassigned Hardware** (2 tasks): PSNS pull-down resistor, MCU GPIO routing — appear to be schematic/board-level design work blocking integration

## Recent Activity
- **Recent Issue**: Slow comms event logged for 2026-04-09 — suggests recent field operation or testing; root cause unknown
- **Active Work**: Jack Elston focused on power management and ground station LCD interface
- **Pending**: PSNS power control hardware tasks waiting for assignment/scheduling

## Notes & Context

### Current Focus vs. Historical Backlog
This 9-task view appears to be a **filtered or recently-prioritized subset** of the larger 168-task backlog documented in the full project knowledge base. These tasks represent near-term/active implementation work in:
- **Power Management**: PSNS hardware refinement (pull-down, MCU GPIO routing)
- **Ground Station UX**: LCD status display, channel switching, power logic
- **Operations**: Comms diagnostics, GCS reliability

### Critical PSNS Tasks (Unassigned)
Two hardware design tasks are blocking PSNS integration:
- **External pull-down (10K-47K) on PWR_KILLn** — May relate to power sequencing/brownout protection
- **Route !PWR_BUTTON to spare MCU GPIO** — GPIO availability/allocation needed for button debouncing or status monitoring

These are **schematic/board-level** decisions requiring engineer review before layout/manufacturing.

### Jack Elston's Power/Comms Workload
Three interrelated tasks suggest Jack is building out PSNS power state monitoring and ground station radio interface:
- LCD display (power state, radio channel, connection status, rsync status)
- Channel switching (radio frequency agility)
- Power-off logic (graceful shutdown sequencing)

**No due dates** — consider prioritization against full project timeline.

### Comms Slowness (2026-04-09)
Single task flagged for "Slow comms" on specific date. Likely field observation during testing/operations. Needs:
- Environmental context (flight conditions, P-3 position, antenna configuration)
- Frequency/channel in use
- Data throughput comparison to baseline

### GCS Stability Issues
- **Rapid power cycling**: sys_init fix causing lockup when toggled in/out of flight mode — may need state machine review
- **Waypoint ETA**: Feature gap (no timeline pressure yet)

---

**Integration with Full Project Knowledge Base**: Refer to [001-03] complete documentation for:
- 2026 Funding Scope detail (power, sensors, flight control, comms, airframe)
- 168-task backlog prioritization
- Hurricane research operational context (COC operations, NHOP/AOC standards)
- Compliance requirements (NDAA, UN38.3, documentation)
- External partnerships (Molicel, ERAU, Skyfora)