# [001-12] BST Web Applications 2.0 IRAD

## Overview
- **Client/customer**: Internal R&D (IRAD - Independent Research and Development)
- **Dollar value**: Not specified
- **Timeline**: No specific dates provided; no due dates set on any tasks
- **Status**: Active development — infrastructure foundation complete (5 tasks completed 2026-04-16); 2 open tasks representing next development phases
- **Team members**: Dan Prendergast (Owner), Ben Busby (infrastructure lead), whole BST team involved
- **Risk signals**: None — project shows completed foundation work and clear next steps, but no timeline pressure or deadlines

## Key Deliverables & Milestones
- **Infrastructure & Database Architecture** — **COMPLETED 2026-04-16**
  - Cloud vs on-premises infrastructure split (hybrid approach)
  - AWS user database with local SQLite sync
  - Offline/GCS-specific capabilities (flight plan generation API endpoint)
  - User input tracking and database sync architecture
- **Mission Planning Web Application** — In progress (Software Engineering task assigned to Dan; Coding task unassigned)
- **Aircraft/Payload Analysis Tool** — Pending (netCDF data analysis)
- **System manuals and training materials** — Pending

## Task Summary
- **Total tasks**: 2 open, 5 completed (71% of tracked work complete)
- **Tasks by assignee**:
  - Dan Prendergast: 1 open (Software Engineering) — likely high-level design/architecture
  - Unassigned: 1 open (Coding for Mission Planner) — awaiting implementation assignment
  - Ben Busby: 5 completed tasks (100% of infrastructure work) — all foundation work done
- **Notable patterns**: Infrastructure foundation work completed in single batch; core application coding tasks now open and ready for implementation phase

## Recent Activity
**2026-04-16 — Major infrastructure completion batch:**
- Decided on hybrid cloud/on-premises infrastructure split
- Initialized AWS user database with local SQLite sync capability
- Finalized offline/GCS-specific capabilities scope
- Added user input tracking to log uploads
- Defined database sync architecture

**Current state**: Foundation phase complete; 2 next-phase tasks now open (Software Engineering planning and Mission Planner coding)

## Notes & Context
- **Priority**: Low
- **Infrastructure decisions finalized**:
  - Hybrid cloud/on-premises approach (office-based storage for faster netCDF access, cloud for scalability)
  - AWS database + local SQLite sync for offline operation
  - Offline scope: flight plan generation API endpoint
  - User input logging integrated with uploads
- **Technical scope**:
  - Mission planning web application (currently in Software Engineering phase)
  - Aircraft/Payload analysis tool with netCDF file integration
  - Flight plan generation via API endpoint
  - User authentication and database management (AWS)
  - Offline/disconnected operation support (SQLite sync)
- **Next phase**: Mission Planner coding (currently marked "Optional Improvements" — may indicate deferred or secondary priority within larger mission planner development)
- **Status**: Ready for core application development; no blockers or risk signals