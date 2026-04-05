# #2025-nasa-autonomy

## Overview
This channel is for the 2025 NASA SBIR Phase I autonomy project focused on developing a layered, modular flight control architecture for rapid integration and testing of advanced autonomy flight components. The project ran from September 2025 to March 2026, aiming to advance from TRL-5 to TRL-7.

**Key participants:** Jack Elston, Dan Prendergast, Maciej, Ben Busby, Beck Cotter, Meredith Needham

**Activity level:** High activity throughout the project period with regular meetings and deliverables

## Key Decisions
- **October 2025:** Decided against using NASA's Core Flight System (cFS) due to being too heavyweight for BST's needs, despite it being designed for spacecraft
- **November 2025:** Selected Data Distribution Service (DDS) for software communications in SwiftCore 4.0, specifically considering RTI International's Connext products
- **December 2025:** Established all control/low-level sensing goes through the autopilot (AP) board, with SBC handling high bandwidth/processing sensors like cameras and SDR
- **December 2025:** Decided not to mark any information as proprietary in the interim report since it was developed using SBIR funds

## Projects & Initiatives
- **SwiftCore 4.0/SwiftPilot Architecture:** Development of modular flight control system with layered approach
- **Safe Sandbox Environment:** Creating supervisory control system capable of overriding experimental control inputs
- **ML Controller Development:** Training simple ML controllers for terrain following using altitude control datasets
- **Hardware Integration:** Porting FreeRTOS to AP hardware and implementing Nix on Raspberry Pi

## Action Items & Commitments
- **Dan Prendergast:** Led architecture design, slide deck creation, and report writing
- **Beck Cotter:** Project management, report coordination, client communications
- **Jack Elston:** Hardware implementation, sensor integration, technical oversight
- **Ben Busby:** Simulation environment development and testing
- **Maciej:** System architecture input and technical guidance

## Client & External References
- **NASA technical monitor:** Regular check-ins scheduled
- **RTI International:** DDS middleware provider (Connext Cert and Connext Express products)
- **Anduril:** Referenced for AI system swapping demonstration capabilities
- **JSBSim:** Flight simulation software integration

## Recurring Topics & Themes
- Weekly meetings on Thursdays at 2pm
- Regular deliverable deadlines and report submissions
- Architecture refinement discussions
- Hardware-software integration challenges
- Phase II proposal preparation (delayed due to Congressional reauthorization)

## Important Resources
- [Project Brief](https://docs.google.com/document/d/1xfT370jdPLRoWR2VJVo4v83mDSp7kEqQv0qcRbBXN34/edit?usp=sharing)
- [Interim Report Template](https://docs.google.com/document/d/1zB5fkJEJmn-KII4yVmLDrRTQFNqrQrmycCZCCDq1ZxE/edit?usp=sharing)
- [Final Report](https://docs.google.com/document/d/1Dg9tzGtKsSBTjYPShF7k4-jW6oDg_4mDccaysqntCow/edit?usp=drive_link)
- [Requirements Spreadsheet and Class Diagrams](https://drive.google.com/drive/u/1/folders/1fU4wNZkqyi-Sp6FQAon63HDnblM5ZkBw)
- [NotebookLM Project](https://notebooklm.google.com/notebook/4646fa50-3289-490f-a5c5-883f0f2a95a9)
- [ECAMS Spreadsheet](https://docs.google.com/spreadsheets/d/1zalkQfdGo6Y4M7P1ZSqfJZ_AmIS_GbK6q-DSee9jGdo/edit?gid=1240731158#gid=1240731158)

## Recent Activity
- **March 27, 2026:** Final report and all deliverables successfully submitted by Meredith Needham
- **March 2026:** Completed ML-enabled control function substitution and testing
- **January 2026:** Interim Demonstration Report approved, $50k payment received
- **February 2026:** NASA SBIR Phase II solicitation delayed pending Congressional reauthorization
- **Architecture Evolution:** Developed comprehensive deployment diagrams showing sensor/actuator connections, NNG messaging, and container-based experimental controllers

The project successfully achieved its TRL-7 goal by developing a safe sandbox environment for testing experimental flight control algorithms with proper supervisory oversight.