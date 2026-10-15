# [001-12] BST Web Applications 2.0 IRAD

## Overview
- **Client/customer**: Internal R&D (IRAD - Independent Research and Development)
- **Dollar value**: Not specified
- **Timeline**: No specific dates or due dates set
- **Status**: Active development — infrastructure foundation complete (April 2026); development roadmap defined but not yet scheduled
- **Team members**: Dan Prendergast (Owner), Ben Busby (infrastructure lead), BST whole team
- **Risk signals**: **URGENT — Export Classification Number (ECCN) requests needed soon to avoid impacting Canada project and LMUK/Royal Navy project.** Daniel Prendergast flagged (2026-10-07/10-08) that classifications are needed for three platforms: 1) S3 with gimballed EO/IR camera, 2) S0-AD with fixed EO/IR camera, 3) S0-AD with magnetometer. Applications not yet drafted. S3 classified as lower priority. **This is a legal/compliance blocker for external projects.**

## Key Deliverables & Milestones
- **Infrastructure & Database Architecture** — **COMPLETED 2026-04-16**
  - Hybrid cloud/on-premises architecture (AWS user database + local SQLite sync)
  - Offline flight plan generation API endpoint
  - User input tracking and database sync architecture
- **Mission Planning Web Application** — In progress (Coding task open, unassigned, marked "Optional Improvements")
- **Aircraft/Payload Analysis Tool** — Pending (Coding task open, unassigned)
- **Testing & Q&A** — Pending
- **System Manuals & Training Materials** — Pending
- **Scientific Data Collection & Processing** — Pending
- **System Repair & Maintenance** — Pending
- **Admin & Logistics** — Pending

## Task Summary
- **Total tasks**: 14 open, 0 completed (note: significant discrepancy with previous knowledge file showing infrastructure phase complete — see Notes)
- **Tasks by assignee**:
  - **Dan Prendergast (Owner)**: System-level Concept & Architecture, Software Engineering — 2 tasks
  - **Unassigned**: 12 tasks (Mechanical Engineering, Part Purchasing & Procurement, Fabrication & Assembly, Coding for Mission Planner, Coding for Aircraft/Payload Analysis, Testing & Q&A, Analysis, System Manuals, Training Materials, Scientific Data Collection & Processing, System Repair & Maintenance, Admin & Logistics)
- **Notable patterns**: Majority of implementation work remains unassigned with no due dates; wide scope spanning software, hardware, documentation, and logistics; infrastructure foundation work not reflected as closed in current task list

## Recent Activity
**2026-10-07/10-08 — URGENT COMPLIANCE FLAG** (Daniel Prendergast):
- Export Classification Number (ECCN) requests needed urgently for three platforms to protect Canada project and LMUK/Royal Navy project timelines
- Required classifications:
  1. S3 with gimballed EO/IR camera (lower priority)
  2. S0-AD with fixed EO/IR camera
  3. S0-AD with magnetometer
- **Status**: Applications not yet drafted; ownership/timeline unclear

**2026-04-16 — Infrastructure completion** (from prior knowledge):
- Hybrid cloud/on-premises split finalized
- AWS database + local SQLite sync initialized
- Offline flight plan generation API scoped
- User input tracking architecture defined

## Notes & Context
- **Priority**: Low (per custom field)
- **Critical issue**: ECCN compliance work is decoupled from Asana task list but flagged by Owner as urgent and blocking external projects. This requires immediate ownership assignment and scheduling.
- **Task list discrepancy**: Current raw data shows 14 open tasks with no completed items, but prior knowledge file documented infrastructure phase as complete (April 2026). Asana task list may not be synchronized with actual project status — recommend clarifying which tasks remain genuinely open vs. closed/archived.
- **Infrastructure decisions finalized** (from April 2026):
  - Hybrid approach: office-based storage for netCDF performance, cloud for scalability
  - AWS user database with local SQLite sync for offline operation
  - Offline scope: flight plan generation API endpoint
  - User input logging integrated
- **Broad scope**: Web applications (Mission Planning, Aircraft/Payload Analysis), hardware integration, testing, documentation, training, and operational support — many tasks unassigned pending resource availability
- **Next steps**: 
  1. **Urgent**: Assign and schedule ECCN classification work (blocking external projects)
  2. Clarify task list status (remove closed infrastructure tasks if applicable)
  3. Assign coding tasks (Mission Planner and Aircraft/Payload Analysis) with timeline