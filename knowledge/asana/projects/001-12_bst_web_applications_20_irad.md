# [001-12] BST Web Applications 2.0 IRAD

## Overview
- **Client/customer**: Internal R&D (IRAD - Independent Research and Development)
- **Dollar value**: Not specified
- **Timeline**: No specific dates provided
- **Status**: Early development phase - 0% completion (0/19 tasks completed)
- **Team members**: Dan Prendergast (Owner), Ben Busby (primary developer), whole BST team involved
- **Risk signals**: Project shows signs of early planning stage with no completed tasks and no due dates set

## Key Deliverables & Milestones
- Mission planning web application
- Mission data analysis web application (Aircraft/Payload Analysis Tool)
- System architecture and concept design
- User database and authentication system
- Offline/GCS-specific capabilities
- System manuals and training materials

## Task Summary
- **Total tasks**: 19 open, 0 completed (0% completion rate)
- **Tasks by assignee**:
  - Ben Busby: 5 tasks (infrastructure decisions, database setup, offline capabilities, user input features)
  - Dan Prendergast: 2 tasks (system architecture, software engineering)
  - Unassigned: 12 tasks (various engineering, testing, documentation, and maintenance tasks)
- **Notable patterns**: Heavy focus on infrastructure decisions and database setup in assigned tasks; many core development tasks remain unassigned; broad scope including mechanical engineering and fabrication tasks

## Recent Activity
No completed tasks to indicate recent activity. Project appears to be in initial planning and architecture phase.

## Notes & Context
- **Priority**: Low (per custom field)
- **Purpose**: Develop web-based applications for mission planning and mission data analysis
- **Technical considerations**: 
  - Deciding between cloud vs on-premises infrastructure for production site
  - Need for offline functionality without internet connection for GCS usage
  - Integration with netCDF files and flight plan generation APIs
  - AWS database implementation with local SQLite sync capability
  - User input functionality for log uploads
- **Project scope**: Unusually broad scope including mechanical engineering, fabrication, procurement, training materials, and ongoing maintenance tasks beyond typical web application development
- **Status**: Very early stage with fundamental architecture and infrastructure decisions still pending
- **Key infrastructure decisions pending**: Cloud vs on-prem split (considering faster netCDF access with on-premise storage), offline GCS capabilities for flightplan generation