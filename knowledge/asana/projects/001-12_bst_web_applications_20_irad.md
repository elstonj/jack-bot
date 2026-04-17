# [001-12] BST Web Applications 2.0 IRAD

## Overview
- **Client/customer**: Internal R&D (IRAD - Independent Research and Development)
- **Dollar value**: Not specified
- **Timeline**: No specific dates provided; no due dates set on any tasks
- **Status**: Active development — 5 tasks completed (21% completion rate; 5 completed, 0 open remaining from original 19)
- **Team members**: Dan Prendergast (Owner), Ben Busby (primary developer/infrastructure lead), whole BST team involved
- **Risk signals**: None currently — project shows recent momentum with 5 tasks completed on 2026-04-16; infrastructure decisions resolved

## Key Deliverables & Milestones
- Mission planning web application
- Aircraft/Payload Analysis Tool (mission data analysis web application)
- System architecture and concept design
- User database and authentication system (AWS-based) — **COMPLETED 2026-04-16**
- Offline/GCS-specific capabilities (offline flight plan generation) — **COMPLETED 2026-04-16**
- System manuals and training materials

## Task Summary
- **Total tasks**: 0 open, 5 completed (21% of original 19-task scope)
- **Tasks by assignee**:
  - Ben Busby: 5 completed tasks (100% of completed work) — all infrastructure, database, and offline capability decisions
  - Dan Prendergast: Assigned to system architecture (status unknown)
  - Unassigned: Remaining tasks likely archived or pending reassignment
- **Notable patterns**: Ben Busby completed all foundational infrastructure work in a single batch on 2026-04-16; core development tasks (mission planner coding, analysis tool coding) status unclear

## Recent Activity
**2026-04-16 — Major infrastructure completion batch:**
- Decided on cloud vs on-premises infrastructure split for production site
- Initialized AWS user database with local SQLite sync capability
- Finalized offline/GCS-specific capabilities scope (flight plan generation API endpoint)
- Added user input tracking to log uploads
- Defined database sync architecture (AWS ↔ local SQLite)

## Notes & Context
- **Priority**: Low
- **Infrastructure decisions finalized**:
  - Hybrid cloud/on-premises approach (office-based storage for faster netCDF access, cloud for scalability)
  - AWS database + local SQLite sync for offline capability
  - Offline scope: flight plan generation API endpoint (not full feature set)
  - User input logging integrated with uploads
- **Technical scope**:
  - Mission planning web application
  - Aircraft/Payload analysis tool with netCDF file integration
  - Flight plan generation via API endpoint
  - User authentication and database management (AWS)
  - Offline/disconnected operation support (SQLite sync)
- **Status**: Foundation phase complete; ready for core application development (mission planner UI, analysis tool implementation, API development)
- **Next likely phases**: Mission planner application coding, analysis tool coding, testing, documentation