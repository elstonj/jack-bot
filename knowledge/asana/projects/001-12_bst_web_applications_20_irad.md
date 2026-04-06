# [001-12] BST Web Applications 2.0 IRAD

## Overview
- **Client/customer**: Internal R&D (IRAD - Independent Research and Development)
- **Dollar value**: Not specified
- **Timeline**: No specific dates provided; no due dates set on any tasks
- **Status**: Early development phase - 0% completion (0/19 tasks completed)
- **Team members**: Dan Prendergast (Owner), Ben Busby (primary developer), whole BST team involved
- **Risk signals**: No due dates set; 12 of 19 tasks unassigned; project appears to be in initial planning/architecture phase with no momentum yet

## Key Deliverables & Milestones
- Mission planning web application
- Aircraft/Payload Analysis Tool (mission data analysis web application)
- System architecture and concept design
- User database and authentication system (AWS-based)
- Offline/GCS-specific capabilities (offline flight plan generation)
- System manuals and training materials

## Task Summary
- **Total tasks**: 19 open, 0 completed (0% completion rate)
- **Tasks by assignee**:
  - Ben Busby: 5 tasks (63% of assigned work) — infrastructure decisions, database setup, offline capabilities, user input features
  - Dan Prendergast: 2 tasks — system architecture, software engineering
  - Unassigned: 12 tasks (63% of total) — mechanical engineering, fabrication, procurement, mission planner coding, analysis tool coding, testing, documentation, maintenance, scientific data processing, admin/logistics
- **Notable patterns**: Infrastructure and database decisions concentrated with Ben Busby; core development tasks (mission planner coding, analysis tool coding) remain unassigned; broad scope spans web development, mechanical engineering, fabrication, and ongoing maintenance

## Recent Activity
No completed tasks. Project appears static in initial planning stage with no recent progress.

## Notes & Context
- **Priority**: Low
- **Purpose**: Develop web-based applications for mission planning and mission data analysis
- **Key pending infrastructure decisions**:
  - Cloud vs on-premises split for production site (considering faster netCDF access via on-premise storage vs cloud scalability)
  - Offline GCS capabilities for flight plan generation without internet connection
  - AWS database implementation with local SQLite sync capability
  - Scope of offline functionality (flight plan generation API vs broader feature set)
- **Technical scope**:
  - Mission planning web application
  - Aircraft/Payload analysis tool with netCDF file integration
  - Flight plan generation via API endpoint
  - User authentication and database management
  - Offline/disconnected operation support
- **Unusual project scope**: Includes mechanical engineering, fabrication, procurement, scientific data processing, and system maintenance alongside web application development — suggests this may be an integrated system project rather than pure software development
- **Status**: Very early stage; foundational architecture and infrastructure decisions still pending before core development can begin effectively