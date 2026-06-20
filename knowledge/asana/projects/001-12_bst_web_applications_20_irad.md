# [001-12] BST Web Applications 2.0 IRAD

## Overview
- **Client/customer**: Internal R&D (IRAD - Independent Research and Development)
- **Dollar value**: Not specified
- **Timeline**: No specific dates or due dates set
- **Status**: Active development — infrastructure foundation complete (April 2026); core application development phase initiated
- **Team members**: Dan Prendergast (Owner), Ben Busby (infrastructure lead), whole BST team involved
- **Risk signals**: None — project has clear foundation and next steps, but no timeline pressure

## Key Deliverables & Milestones
- **Infrastructure & Database Architecture** — **COMPLETED 2026-04-16**
  - Cloud vs on-premises infrastructure split (hybrid approach)
  - AWS user database with local SQLite sync
  - Offline/GCS-specific capabilities (flight plan generation API endpoint)
  - User input tracking and database sync architecture
- **Mission Planning Web Application** — In progress (Coding task open, unassigned)
- **Aircraft/Payload Analysis Tool** — Pending (netCDF data analysis)
- **System manuals and training materials** — Pending

## Task Summary
- **Total tasks**: 1 open, 5+ completed (majority of foundation work done)
- **Tasks by assignee**:
  - Unassigned: 1 open (Coding for Mission Planner) — awaiting implementation assignment
  - Dan Prendergast (Owner): Oversight/direction
  - Ben Busby: Infrastructure foundation (completed)
- **Notable patterns**: Infrastructure phase closed out; single coding task remains open for Mission Planner with "Optional Improvements" note, suggesting secondary/deferred priority within broader development roadmap

## Recent Activity
**2026-04-16 — Infrastructure completion**:
- Hybrid cloud/on-premises split finalized
- AWS database + local SQLite sync initialized
- Offline flight plan generation API scoped
- User input tracking architecture defined

**Current state**: Foundation phase complete; Mission Planner coding task open but marked as optional improvements (secondary priority), remains unassigned with no due date

## Notes & Context
- **Priority**: Low
- **Infrastructure decisions finalized**:
  - Hybrid approach: office-based storage for netCDF performance, cloud for scalability
  - AWS user database with local SQLite sync for offline operation
  - Offline scope: flight plan generation API endpoint
  - User input logging integrated
- **Technical scope**:
  - Mission planning web application (coding task open, unassigned)
  - Aircraft/Payload analysis tool with netCDF integration
  - Flight plan generation via API
  - User authentication and database management
  - Offline/disconnected operation support
- **Current focus**: Mission Planner "Optional Improvements" — coding task available but deprioritized relative to core features; no blocker preventing assignment and work
- **Status**: Ready for implementation phase; no blockers identified