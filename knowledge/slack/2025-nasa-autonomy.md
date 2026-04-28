# #2025-nasa-autonomy

## Overview
This channel is for the 2025 NASA SBIR Phase I autonomy project focused on developing a layered, modular flight control architecture for rapid integration and testing of advanced autonomy flight components. The project ran from September 2025 to March 2026, aiming to advance from TRL-5 to TRL-7.

**Key participants:** Jack Elston, Dan Prendergast, Maciej, Ben Busby, Beck Cotter, Meredith Needham

**Activity level:** High activity throughout the project period with regular meetings and deliverables. Project completion phase (March-April 2026) shows transition to Phase II planning. Currently in active Phase II proposal development stage with multiple BAA opportunities under evaluation.

## Key Decisions
- **October 2025:** Decided against using NASA's Core Flight System (cFS) due to being too heavyweight for BST's needs, despite it being designed for spacecraft
- **November 2025:** Selected Data Distribution Service (DDS) for software communications in SwiftCore 4.0, specifically considering RTI International's Connext products
- **December 2025:** Established all control/low-level sensing goes through the autopilot (AP) board, with SBC handling high bandwidth/processing sensors like cameras and SDR
- **December 2025:** Decided not to mark any information as proprietary in the interim report since it was developed using SBIR funds
- **April 2026:** Proceeding with Phase II proposal under new NASA SBIR BAA structure following Congressional reauthorization
- **April 27, 2026:** Evaluating Phase II proposal fit across multiple NASA BAA opportunities (SBIR 26A-1, SBIR 26B-1, STTR 26B-1) with May 21, 2026 deadline

## Projects & Initiatives
- **SwiftCore 4.0/SwiftPilot Architecture:** Development of modular flight control system with layered approach
- **Safe Sandbox Environment:** Creating supervisory control system capable of overriding experimental control inputs
- **ML Controller Development:** Training simple ML controllers for terrain following using altitude control datasets
- **Hardware Integration:** Porting FreeRTOS to AP hardware and implementing Nix on Raspberry Pi
- **Phase II Proposal:** Active development across multiple NASA SBIR/STTR BAA opportunities; strategic alignment assessment underway for best fit subtopics

## Action Items & Commitments
- **Dan Prendergast:** Led architecture design, slide deck creation, and report writing
- **Beck Cotter:** Project management, report coordination, client communications; **initiated Phase II draft proposal (April 9, 2026); forwarded NASA '26 BAA announcements (April 21, 2026); identified Phase II proposal fit across multiple BAA opportunities and evaluated subtopic alignments (April 27, 2026)**
- **Jack Elston:** Hardware implementation, sensor integration, technical oversight
- **Ben Busby:** Simulation environment development and testing
- **Maciej:** System architecture input and technical guidance
- **Meredith Needham:** Successfully submitted all Phase I deliverables to ProSAMS (March 27, 2026); confirmed acceptance (April 9, 2026)

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

## Recurring Topics & Themes
- Weekly meetings on Thursdays at 2pm
- Regular deliverable deadlines and report submissions
- Architecture refinement discussions
- Hardware-software integration challenges
- Phase II proposal preparation and BAA guidance
- Identification and evaluation of best-fit subtopics across multiple NASA solicitations

## Important Resources
- [Project Brief](https://docs.google.com/document/d/1xfT370jdPLRoWR2VJVo4v83mDSp7kEqQv0qcRbBXN34/edit?usp=sharing)
- [Interim Report Template](https://docs.google.com/document/d/1zB5fkJEJmn-KII4yVmLDrRTQFNqrQrmycCZCCDq1ZxE/edit?usp=sharing)
- [Final Report](https://docs.google.com/document/d/1Dg9tzGtKsSBTjYPShF7k4-jW6oDg_4mDccaysqntCow/edit?usp=drive_link)
- [Requirements Spreadsheet and Class Diagrams](https://drive.google.com/drive/u/1/folders/1fU4wNZkqyi-Sp6FQAon63HDnblM5ZkBw)
- [NotebookLM Project](https://notebooklm.google.com/notebook/4646fa50-3289-490f-a5c5-883f0f2a95a9)
- [ECAMS Spreadsheet](https://docs.google.com/spreadsheets/d/1zalkQfdGo6Y4M7P1ZSqfJZ_AmIS_GbK6q-DSee9jGdo/edit?gid=1240731158#gid=1240731158)
- [Phase II Draft Proposal](https://docs.google.com/document/d/1dFh7orVpGlvggoF2mXrAlYtKE9wuXRrIh4_cJIk/edit?usp=sharing) - Initiated April 9, 2026 using NASA SBIR forms library template
- [NASA SBIR/STTR BAA Documents](https://drive.google.com/drive/folders/1CPn4AgjvOKnof-YCX55ABB80w_EMDrES?usp=drive_link) - Located in Proposals-In Development folder; contains SBIR 26A-1, SBIR 26B-1, and STTR 26B-1 solicitations

## NASA Phase II BAA Fit Analysis (April 27, 2026)

### AERO (Aeronautics Research Mission Directorate) - Key Alignment Opportunities
- **AERO.4.01 – Advanced Air Mobility (AAM) Autonomy and Safety**
  - Focus: Autonomous operations, safety in complex/uncertain environments
  - *BST Fit:* Strong for BVLOS (Beyond Visual Line of Sight) + degraded condition autonomy
  
- **AERO.4.02 – Resilient Control and Navigation for UAS**
  - Focus: Robust flight control, operations under disturbances and uncertainty
  - *BST Fit:* Direct alignment with Black Swift's high-wind/turbulence operations capabilities
  
- **AERO.5.01 – Intelligent Flight Systems and Autonomy**
  - Focus: Adaptive decision-making, real-time autonomy
  - *BST Fit:* Edge autonomy + adaptive sampling capabilities

## Recent Activity
- **April 27, 2026:** Beck Cotter analyzes three separate NASA BAA opportunities (SBIR 26A-1, SBIR 26B-1, STTR 26B-1) and identifies strong technical fit across multiple AERO subtopics; May 21, 3:00pm Mountain deadline identified
- **April 21, 2026:** Beck Cotter forwards NASA '26 BAA announcements to team
- **April 14, 2026:** NASA confirms SBIR/STTR program reauthorization; Phase II guidance expected shortly
- **April 9, 2026:** All Phase I deliverables officially accepted in ProSAMS system; Beck Cotter initiates Phase II draft proposal in anticipation of NASA guidance
- **March 27, 2026:** Final report and all deliverables successfully submitted by Meredith Needham
- **March