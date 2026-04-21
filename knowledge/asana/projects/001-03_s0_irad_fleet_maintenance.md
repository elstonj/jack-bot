# [001-03] S0 IRAD & Fleet Maintenance

## Overview
- **Client/Customer**: Internal BST research and development
- **Dollar Value**: No specific dollar amounts identified; funding scope: 2025 Phase II (active), 2026 (pending)
- **Timeline**: Active operations through 2025; key deadlines 2026-03-31 (IAS diagnostics & telemetry fix). Historical milestone: S0 AD completed 2026-04-17 (54 days overrun)
- **Status**: **Active — Critical operational issues**. Three open tasks addressing mission-critical flight safety failures. Project classified as "Low" priority in custom field, but recent aircraft loss (2025-10-26) and escalating IAS failures indicate this should be reassessed as high-urgency safety work.
- **Team Members**: Josh Fromm (project owner), Maciej Stachura (IAS diagnostics), Ben Busby (IAS telemetry), Jack Elston (GCS power control), Nate Straus (airframe/AD, historically), 7+ unassigned contributors in broader portfolio
- **Risk Signals**:
  - **CRITICAL**: IAS detector failures increasingly frequent on 2025-10-26 flights → **loss of unmanned aircraft (UA)** and mission-critical wind measurement data
  - GCS power-off task completely unscheduled (no due date); unclear urgency and dependencies
  - Two Q1 2026 deadlines (2026-03-31) for critical safety fixes

## Key Deliverables & Milestones

| Deliverable | Owner | Due Date | Status | Funding | Priority |
|---|---|---|---|---|---|
| **IAS Detector Diagnostics** (root cause: detector not running during freefall, 3D velocity calculation errors) | Maciej Stachura | 2026-03-31 | OPEN | 2025 Phase II | **CRITICAL** |
| **IAS Telemetry Fix** (eliminate false red LED/telemetry status during takeoff) | Ben Busby | 2026-03-31 | OPEN | 2025 Phase II | **CRITICAL** |
| **GCS Power-Off Logic** | Jack Elston | *Unscheduled* | OPEN | Unknown | **Unassigned priority** |
| Construct BST owned S0 AD (Airworthiness Directive) | Nate Straus | 2026-01-09 | COMPLETED 2026-04-17 | Historical | Completed (54 days overrun) |

## Task Summary

- **Total Tasks**: 3 open; 0 completed in current cycle (1 historically completed)
- **Open Tasks by Assignee**:
  - **Maciej Stachura**: 1 task (IAS detector diagnostics) — Due 2026-03-31
  - **Ben Busby**: 1 task (IAS telemetry) — Due 2026-03-31
  - **Jack Elston**: 1 task (GCS power-off) — **No due date; unscheduled**
- **Custom Field Patterns**:
  - Subject: All IAS tasks tagged [ias]
  - Funding Scope: IAS tasks assigned to 2025 Phase II; GCS power unspecified
  - Fix or Feature: Both IAS tasks classified as "Malfunction Fix" (not enhancements)

## Recent Activity

- **2025-10-26**: Multiple IAS detector failures during flights; **loss of unmanned aircraft**; significant wind measurement data loss. Failures described as "increasingly frequent"
- **2026-04-17**: S0 AD (airworthiness directive) completed by Nate Straus, 54 days past due date (originally 2026-01-09)
- **Current**: IAS detector and telemetry failures are active operational blockers. GCS power-off work status unclear (no due date, no recent updates)

## Notes & Context

### Critical Safety Issue: IAS Detector Failures
The 2025-10-26 incident was catastrophic: escalating IAS detector failures resulted in:
- Loss of unmanned aircraft
- Failure to maintain throttle during freefall phase
- Mission-critical wind measurement data loss
- Crew/mission confusion from telemetry false alerts

**Root cause hypothesis** (Maciej's task): Detector not running during freefall; potential 3D velocity calculation error. Diagnostic work due 2026-03-31.

### Telemetry False Alert Pattern
IAS LED and telemetry field display red status during normal takeoff, masking true system failures and creating false crew alerts. Ben Busby to diagnose and fix by 2026-03-31.

### GCS Power-Off Logic (Unscheduled)
Jack Elston's task has **no due date, no funding scope, and no documented urgency**. Clarification needed:
- Is this related to known GCS sys_init power-cycling bug from prior scope?
- Is this blocking current operations or future capability?
- Should this be prioritized before or after IAS fixes?

### Priority Misalignment
Project is classified "Low" priority in custom field, but contains:
- Active aircraft loss (2025-10-26)
- Safety-critical failures affecting flight operations
- Two urgent Q1 2026 deadlines for mission-critical fixes

**Recommendation**: Escalate to appropriate safety/mission-critical priority; current "Low" classification does not reflect operational reality.

### Historical Context
Prior knowledge base documented a 168-task backlog for 2026 Funding Scope (power, sensors, flight control, comms, airframe, compliance). Current 3 open tasks are the active subset; broader portfolio tracking should be confirmed.

---

## Action Items
1. **URGENT**: Escalate IAS detector/telemetry failures to safety review; confirm 2026-03-31 diagnostics deadline is feasible given mission criticality
2. Assign due date and priority to Jack Elston's GCS power-off task; clarify scope and dependencies
3. Review project priority classification (currently "Low"; recommend reassessment to "Critical" or mission-safety tier)
4. Confirm status of 2026 Funding Scope backlog (168 tasks) relative to current active work