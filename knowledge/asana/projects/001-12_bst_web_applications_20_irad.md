# [001-12] BST Web Applications 2.0 IRAD

## Overview
- **Client/customer**: Internal R&D (IRAD - Independent Research and Development)
- **Dollar value**: Not specified
- **Timeline**: No specific dates or due dates set; infrastructure foundation completed April 2026
- **Status**: Active development — infrastructure phase complete; core application development pending resource assignment
- **Team members**: Dan Prendergast (Owner), Ben Busby (infrastructure lead), BST whole team
- **Risk signals**: 
  - **CRITICAL COMPLIANCE BLOCKER**: Export Classification Number (ECCN) requests needed urgently (flagged 2026-10-07/10-08 by Daniel Prendergast) to avoid impacting Canada project and LMUK/Royal Navy project. Three platforms require classification; applications not yet drafted; no owner assigned.
  - 12 of 14 tasks unassigned with no due dates — deployment timeline unclear
  - Task list may not reflect actual infrastructure completion status

## Key Deliverables & Milestones
- **Infrastructure & Database Architecture** — **COMPLETED 2026-04-16**
  - Hybrid cloud/on-premises architecture (AWS user database + local SQLite sync)
  - Offline flight plan generation API endpoint
  - User input tracking and database sync architecture
- **Mission Planning Web Application** — In progress (Coding task open, unassigned, marked "Optional Improvements")
- **Aircraft/Payload Analysis Tool** — Pending (Coding task open, unassigned)
- **Testing & Q&A** — Pending (Unassigned)
- **System Manuals & Training Materials** — Pending (Unassigned)
- **Scientific Data Collection & Processing** — Pending (Unassigned)
- **System Repair & Maintenance** — Pending (Unassigned)
- **Admin & Logistics** — Pending (Unassigned)

## Task Summary
- **Total tasks**: 14 open, 0 completed (note: infrastructure phase marked complete April 2026 but not reflected as closed in Asana; recommend audit)
- **Tasks by assignee**:
  - **Dan Prendergast**: System-level Concept & Architecture, Software Engineering (2 tasks)
  - **Unassigned**: 12 tasks spanning mechanical engineering, procurement, fabrication, coding, testing, documentation, training, data processing, maintenance, and logistics
- **Notable patterns**: 
  - Vast majority of implementation work remains unassigned and undated
  - Wide scope spanning software, hardware, documentation, and operational support
  - No external deadlines reflected in task list despite blocking external projects (Canada, LMUK/Royal Navy)

## Recent Activity

**2026-10-07/10-08 — URGENT COMPLIANCE FLAG** (Daniel Prendergast):
- **CRITICAL**: Export Classification Number (ECCN) requests required urgently for three platforms:
  1. S0-AD with fixed EO/IR camera (high priority)
  2. S0-AD with magnetometer (high priority)
  3. S3 with gimballed EO/IR camera (lower priority)
- **Impact**: Delays will affect pending Canada project and LMUK/Royal Navy project timelines
- **Current status**: Applications not yet drafted; no owner or timeline assigned
- **Direct quote** (Prendergast, 2026-10-08): "We should be submitting Export Classification Number (ECCN) requests very soon for several platforms to avoid affecting the pending Canada project and LMUK/Royal Navy project."

**2026-04-16 — Infrastructure Completion**:
- Hybrid cloud/on-premises split finalized (AWS database + local SQLite sync)
- Offline flight plan generation API scoped and initialized
- User input tracking architecture defined

## Notes & Context

- **Project priority**: Low (per custom field) — **contradicts urgency of ECCN compliance work**
- **CRITICAL ISSUE**: ECCN classification work is **blocking external projects** (Canada, LMUK/Royal Navy) but remains decoupled from Asana task list, unassigned, and undated. Immediate action required: assign owner and establish deadline aligned with dependent project schedules.
- **Task list discrepancy**: Current Asana shows 14 open tasks with zero completed, but April 2026 infrastructure phase marked complete. Recommend clarifying which tasks should be archived vs. remain active.
- **Scope**: Web applications (Mission Planning, Aircraft/Payload Analysis), hardware integration, testing, documentation, training, and operational support — typical of broad IRAD effort.
- **Next steps** (in priority order):
  1. **URGENT**: Assign ECCN classification work owner and establish hard deadline (pending Canada/LMUK timelines)
  2. Audit task list; close or archive infrastructure phase tasks if complete
  3. Assign coding tasks (Mission Planner, Aircraft/Payload Analysis) with development timeline
  4. Coordinate ECCN timeline with Canada and LMUK/Royal Navy project leads