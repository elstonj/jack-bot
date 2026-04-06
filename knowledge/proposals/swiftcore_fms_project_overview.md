# SwiftCore FMS Project Overview

## Document Metadata
- **Type:** Project development and integration plan (DRAFT)
- **Client/Agency:** Google / Titan Aerospace
- **Program/Solicitation:** Solara UAV Flight Management System integration
- **Date:** June 10-19, 2015
- **BST Products/Systems Referenced:** SwiftCore Flight Management System (FMS), SwiftPilot Avionics, SwiftStation, SwiftTab UI
- **Key Personnel:** Jack Elston (last editor)

## Executive Summary
Black Swift Technologies proposed a custom development and integration effort to adapt its SwiftCore Flight Management System for Google/Titan Aerospace's Solara UAV scaled test models (M2 and M3). The project includes hardware-in-the-loop simulation, avionics customization, ground control stations, and two rounds of functional aircraft with associated training environments, on a 10-month timeline for $892k in development costs.

## Technical Approach
BST proposed to develop and integrate SwiftCore FMS into the Solara airframe with the following approach:

- **Modular design philosophy:** Use whole modules and interface specifications to avoid licensing/IP issues and development delays
- **Conditional source code access:** If proprietary SwiftCore source code disclosure became necessary (due to accelerated schedule and need to avoid non-deterministic "black box" behavior), would be granted under strict NDA, non-compete, and code-sharing agreements
- **Hardware-in-the-loop (HIL) simulation:** Based on SwiftCore FMS with Google/Titan's flight dynamics and environmental models
- **Integration support:** 3-month on-site support period at 40 man-hours/month with 6 scheduled visits (kickoff, HIL testing, M2 integration, M2 flight test, M3 integration, M3 flight test)
- **Staged development:** Two major milestones aligned with Google/Titan's testing schedule

## Products & Capabilities Described

### SwiftCore Flight Management System
- **What it is:** BST's core flight management and control system, available as configurable avionics modules
- **Proposed use:** Custom adaptation for Solara M2 and M3 test aircraft with safety and security requirements for national airspace operations
- **Components:**
  - **SwiftPilot Avionics:** Core avionics module (unit pricing: $3,625 @ 5 units down to $2,562.50 @ 50 units)
  - **SwiftStation and SwiftTab UI:** Ground control station interface and displays (same pricing structure as SwiftPilot)

### Deliverables Hardware/Software
1. Hardware-in-the-loop simulation environment
2. Flight test display and analysis setup (integrating Symvionics IADS software suite)
3. 5 complete customized avionics sets
4. 2 ground control stations (modified for multi-radio support and Google tracking antenna interface)
5. Up to 2 functional M2 UAS
6. Up to 2 functional M3 UAS
7. Functional simulation environment for training

## Use Cases & Applications
- **Primary mission:** Scaled testing of Solara high-altitude platform aircraft
- **Mission requirements:** Operations requiring heightened safety and security in national airspace
- **Testing phases:**
  - **Milestone 1:** Manual piloting with G1000 glass cockpit, FPV system, manual handset control, multi-radio module support, tracking antenna control, real-time IADS analysis integration
  - **Milestone 2:** Autonomous flight with manual fallback, redundant sensor suite, in-flight control loop tuning, seamless multi-GCS handoff, lost-link functionality, full simulation/training capability

## Project Scope & Requirements
- **Requirements document:** SwiftCore FMS Requirements v1.0 (June 10, 2015) — referenced as separate specification
- **Change management:** Any requirement changes after project kickoff treated as engineering change orders with potential cost adjustments requiring mutual agreement
- **Timeline:** 10-month development cycle
- **Compression penalty:** 20% compounding fee per month for any timeline reduction

## Budget Details
- **Base development cost:** $892,000 over 10 months (excludes materials and on-site support)
- **On-site support rates:** 
  - Minimum $4,000 per person per trip (includes 16 hours of support)
  - Additional on-site support: $1,500 per person per day (8 hours)
- **Personnel:** 2 engineers and 1 senior engineer available on as-needed basis
- **Unit pricing for base SwiftCore components:** Tiered pricing from 5-50 unit quantities

## Notable Details

### Intellectual Property & Licensing Strategy
- **Module-based approach** to avoid IP conflicts and accelerate development
- **Conditional source code access** under strict terms including:
  - 5-year NDA and non-compete agreement
  - Google/Titan must return modifications to BST, with BST retaining future development rights
  - Future use of source code beyond project completion requires separate agreement
  - Code implementation restricted to BST-supplied hardware only
- This conservative IP approach reflects BST's effort to protect SwiftCore while accommodating the client's integration needs

### Integration Challenges Acknowledged
- Solara's unique design elements requiring custom development
- Demanding mission profile requiring specialized safety/security capabilities
- Accelerated schedule potentially necessitating source code access and custom implementations

### Project Status
Document marked as DRAFT; presented June 10, 2015 to Google/Titan at Moriarty, New Mexico facility. Project is now listed as "Sales Completed/Inactive" in BST's file structure, suggesting this proposal either concluded or was not fully executed as planned.