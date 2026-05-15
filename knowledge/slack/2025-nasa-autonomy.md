# #2025-nasa-autonomy

## Overview
This channel is for the 2025 NASA SBIR Phase I autonomy project focused on developing a layered, modular flight control architecture for rapid integration and testing of advanced autonomy flight components. The project ran from September 2025 to March 2026, aiming to advance from TRL-5 to TRL-7.

**Key participants:** Jack Elston, Dan Prendergast, Maciej, Ben Busby, Beck Cotter, Meredith Needham, Paige (documentation coordination)

**Activity level:** High activity throughout the project period with regular meetings and deliverables. Project completion phase (March-April 2026) shows transition to Phase II planning. Currently in active Phase II proposal development stage with multiple BAA opportunities under evaluation. Recent focus (May 2026) on Phase II proposal requirements including capital commitments documentation, budget refinement, aircraft platform acquisition specifications, equipment necessity assessment, and ProSAMS submission refinement. Final documentation polish and submission preparation phase continuing through May 13-14, 2026, with confirmations of completion.

## Key Decisions
- **October 2025:** Decided against using NASA's Core Flight System (cFS) due to being too heavyweight for BST's needs, despite it being designed for spacecraft
- **November 2025:** Selected Data Distribution Service (DDS) for software communications in SwiftCore 4.0, specifically considering RTI International's Connext products
- **December 2025:** Established all control/low-level sensing goes through the autopilot (AP) board, with SBC handling high bandwidth/processing sensors like cameras and SDR
- **December 2025:** Decided not to mark any information as proprietary in the interim report since it was developed using SBIR funds
- **April 2026:** Proceeding with Phase II proposal under new NASA SBIR BAA structure following Congressional reauthorization
- **April 27, 2026:** Evaluating Phase II proposal fit across multiple NASA BAA opportunities (SBIR 26A-1, SBIR 26B-1, STTR 26B-1) with May 21, 2026 deadline
- **May 8, 2026:** Phase II aircraft platform acquisition strategy finalized—shifting from daily rental model to dedicated platform purchases for testing campaign:
  - **1x S3 VTOL**
  - **2x S0-VTOL** (with potential redesign opportunity)
  - **2x E2 multirotor** (with potential redesign opportunity)
  - **Dropped S2 fixed-wing** from original platform list
- **May 11, 2026:** TABA/Ed service excluded from Phase II budget—determined not to provide sufficient value when drawn from project budget as non-separate line item ($25K/year cost)
- **May 11, 2026:** Avionics equipment procurement reconsidered—evaluating whether 5x avionics for bench testing are still necessary given purchase of 5 dedicated platforms; seeking clarification on standalone SwiftCore pricing vs. platform-inclusive bundles
- **May 13, 2026:** Technical documentation graphics updated and ProSAMS entries refined for accuracy; documentation submission completed with confirmatory feedback (Jack Elston confirmation May 14, 2026)

## Projects & Initiatives
- **SwiftCore 4.0/SwiftPilot Architecture:** Development of modular flight control system with layered approach
- **Safe Sandbox Environment:** Creating supervisory control system capable of overriding experimental control inputs
- **ML Controller Development:** Training simple ML controllers for terrain following using altitude control datasets
- **Hardware Integration:** Porting FreeRTOS to AP hardware and implementing Nix on Raspberry Pi
- **Phase II Proposal:** Active development complete as of May 13-14, 2026. Strategic alignment assessment completed across multiple NASA SBIR/STTR BAA opportunities; Phase II proposal components finalized including capital commitments addendum, detailed budget specifications for hardware/components/aircraft platforms, equipment necessity assessment, and ProSAMS submission refinement with documentation submission confirmed by May 14, 2026

## Action Items & Commitments
- **Dan Prendergast:** Led architecture design, slide deck creation, and report writing; made refinements to ProSAMS entries (Technical Abstract, Potential Non-NASA Applications, Identification and Significance of the Innovation) with corrections to ensure accuracy (May 13, 2026) - **COMPLETED**
- **Beck Cotter:** Project management, report coordination, client communications; initiated Phase II draft proposal (April 9, 2026); forwarded NASA '26 BAA announcements (April 21, 2026); identified Phase II proposal fit across multiple BAA opportunities and evaluated subtopic alignments (April 27, 2026); identified capital commitments addendum requirement (May 6, 2026); clarified Phase II budget details for components and platform acquisition (May 8, 2026); evaluated TABA/Ed service inclusion in Phase II budget (May 11, 2026); sought clarification from Meredith on standalone SwiftCore pricing for bench testing equipment assessment (May 11, 2026); re-uploaded ProSAMS entries following Dan's refinements (May 13, 2026) - **COMPLETED**
- **Jack Elston:** Hardware implementation, sensor integration, technical oversight; coordinated capital commitment letters from Adria, Bob, and Lisa Marie (May 6, 2026); provided specification guidance for Phase II aircraft platform acquisition strategy (May 8, 2026); provided technical assessment of TABA/Ed value for Phase II project (May 11, 2026); updated graphics in technical documentation for improved readability (May 13, 2026); notified Paige of documentation updates (May 13, 2026); confirmed documentation completion and submission (May 14, 2026) - **COMPLETED**
- **Ben Busby:** Simulation environment development and testing
- **Maciej:** System architecture input and technical guidance
- **Meredith Needham:** Successfully submitted all Phase I deliverables to ProSAMS (March 27, 2026); confirmed acceptance (April 9, 2026); provided QuickBooks pricing information for SwiftCore and platform bundles to support Phase II budget refinement (May 11, 2026) - **COMPLETED**
- **Paige:** Documentation coordination and technical documentation updates; notified of graphics updates (May 13, 2026); updated technical documentation to incorporate graphics changes - **COMPLETED**

## Client & External References
- **NASA technical monitor:** Regular check-ins scheduled
- **NASA SBIR Program:** 2026 Broad Agency Announcement (BAA) released with three separate solicitations:
  - SBIR 26A-1
  - SBIR 26B-1
  - STTR 26B-1
- **NASA AERO Mission Directorate (Aeronautics Research):** Primary focus for Phase II proposal opportunities
- **RTI International:** DDS middleware provider (Connext Cert and Connext Express products)
- **Anduril:** Referenced for AI system swapping demonstration capabilities
- **JSBSim:** Flight simulation software integration
- **TABA/Ed:** Service provider for [service type unspecified]; $25K/year cost; excluded from Phase II budget May 11, 2026
- **Internal Capital Commitment Sources:** Adria, Bob, Lisa Marie, and KS (for market validation/capital commitment letters)

## Recurring Topics & Themes
- Weekly meetings on Thursdays at 2pm
- Regular deliverable deadlines and report submissions
- Architecture refinement discussions
- Hardware-software integration challenges
- Phase II proposal preparation and BAA guidance
- Identification and evaluation of best-fit subtopics across multiple NASA solicitations
- Phase II proposal component completion and capital commitment documentation
- Phase II budget specifications, equipment necessity assessment, and platform acquisition planning
- Bench testing equipment and tooling requirements optimization
- ProSAMS submission content refinement and accuracy verification

## Important Resources
- [Project Brief](https://docs.google.com/document/d/1xfT370jdPLRoWR2VJVo4v83mDSp7kEqQv0qcRbBXN34/edit?usp=sharing)
- [Interim Report Template](https://docs.google.com/document/d/1zB5fkJEJmn-KII4yVmLDrRTQFNqrQrmycCZCCDq1ZxE/edit?usp=sharing)
- [Final Report](https://docs.google.com/document/d/1Dg9tz