# [001-03] S0 IRAD & Fleet Maintenance

## Overview
- **Client/Customer**: Internal BST research and development
- **Dollar Value**: No specific dollar amounts identified, but includes 2025 Phase II and 2026 funding scope items
- **Timeline**: Active operations through 2025; 2026 funding items pending. Key deadline: 2026-03-31 (IAS diagnostics)
- **Status**: Active — 3 open tasks (IAS failures, GCS power control); 1 historically completed (S0 AD, April 2026). Project redesignated as "Low" priority per custom field, but active operational issues suggest higher urgency.
- **Team Members**: Josh Fromm (project owner), Maciej Stachura (IAS diagnostics), Ben Busby (IAS telemetry), Jack Elston (GCS power), Nate Straus (airframe/AD), 7+ unassigned contributors in broader scope
- **Risk Signals**:
  - **Critical**: IAS (Indicated Airspeed) detector failures during 2025-10-26 flights caused data loss and **loss of UA (unmanned aircraft)**. Increasingly frequent failures.
  - GCS power-off task unscheduled (no due date) — unclear urgency
  - S0 AD completion was 54 days past due (due 2026-01-09, completed 2026-04-17) — historical schedule pressure
  - IAS telemetry issues affecting mission-critical wind measurements and aircraft recovery

## Key Deliverables & Milestones
- **[OPEN] IAS Detector Diagnostics** | Maciej Stachura | Due: 2026-03-31 | Funding: 2025 Phase II
  - Diagnose IAS fail-to-throttle root cause (detector not running during freefall, 3D velocity calculation)
  - Critical: Recent flights show increasing failure frequency; lost aircraft on 2025-10-26
  
- **[OPEN] IAS Telemetry Fix** | Ben Busby | Due: 2026-03-31 | Funding: 2025 Phase II
  - Eliminate false "red" status on IAS LED and telemetry field during takeoff
  - Blocking proper mission status indication
  
- **[OPEN] GCS Power-Off Logic** | Jack Elston | Due: Unscheduled | Status: Unknown
  - Ground Control Station power management implementation
  - No due date assigned — recommend prioritization review

- **[COMPLETED] Construct BST owned S0 AD for 2025 season** | Nate Straus | Due: 2026-01-09 | Completed: 2026-04-17
  - Airworthiness Directive documentation (54 days overrun)

## Task Summary
- **Total Tasks**: 3 open, 0 completed in current view (1 historically completed)
- **Open Tasks by Assignee**:
  - Maciej Stachura: 1 task (IAS detector diagnostics) — 2026-03-31 deadline
  - Ben Busby: 1 task (IAS telemetry) — 2026-03-31 deadline
  - Jack Elston: 1 task (GCS power-off) — **no due date**
- **Historical Backlog** (from prior sync):
  - 168-task backlog documented for 2026 Funding Scope
  - Power control, comms, and flight control tasks remain in queue
  - 9 historically open tasks; current view shows 3 — suggests task consolidation or reassignment

## Recent Activity
- **2025-10-26**: Multiple IAS detector failures during flights; loss of aircraft; significant wind measurement data loss
  - Escalated to active diagnostics tasks (Maciej Stachura, Ben Busby)
- **2026-04-17**: S0 AD airworthiness documentation completed (54 days late)
- **Current**: IAS failures and GCS power control are active blockers for fleet operations

## Notes & Context

### Critical IAS Failure Pattern
**Escalating Issue**: IAS detector failures on 2025-10-26 have become "increasingly frequent," culminating in loss of UA (aircraft). Root cause investigation urgent:
- Suspected: Detector not running during freefall phase, 3D velocity calculation errors
- Impact: Mission-critical wind measurement loss, aircraft recovery failure
- Mitigation: 2026-03-31 deadline for diagnostics and fix suggests Q1 2026 completion target

### Telemetry False Alerts
IAS LED and telemetry field display red status during normal takeoff, masking true system failures and confusing crew. Diagnostic fix required by 2026-03-31.

### GCS Power Management (Unscheduled)
Jack Elston's power-off task lacks due date. Recommend:
- Clarify relationship to prior documented GCS sys_init bug (rapid power cycling)
- Determine urgency relative to 2025-10-26 operational incidents
- Assign target date

### Project Priority Downgrade
Custom field shows "Low" priority, but:
- Active operational aircraft loss (2025-10-26)
- Safety-critical IAS failures affecting flight operations
- Two Q1 2026 deadlines for fixes

**Recommendation**: Reassess priority classification; this project contains mission-critical flight safety work.

### Historical Context
Prior knowledge base documented:
- 168-task backlog for 2026 Funding Scope (power, sensors, flight control, comms, airframe)
- Compliance requirements (NDAA, UN38.3, airworthiness directives)
- External partnerships (Molicel, ERAU, Skyfora)
- Hurricane research operational focus

Current 3 open tasks are subset of broader S0 IRAD portfolio; confirm alignment with full scope.

---

**Action Items**:
- **Urgent**: Investigate 2025-10-26 IAS detector failures; assign root cause analysis
- Escalate IAS tasks to appropriate priority; confirm 2026-03-31 deadline feasibility
- Assign due date and prioritize GCS power-off task (Jack Elston)
- Confirm status of 6 historical unassigned tasks (GCS sys_init, PSNS hardware, comms, waypoint ETA)
- Review project priority classification (currently "Low" with mission-critical flight safety work)