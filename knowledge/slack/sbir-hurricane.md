# #sbir-hurricane

## Overview
The #sbir-hurricane channel is the primary workspace for Black Swift Technologies' SBIR Hurricane project, focused on developing the S0 unmanned aircraft system for hurricane reconnaissance missions. The channel is highly active with extensive technical discussions, operational updates, and mission planning spanning 2020-2026. Key participants include Joshua Fromm, Jack Elston, Maciej, Danny Troke, Dan Prendergast, Alex Lomis, Nate, Sam Hild, Beck Cotter, Paige Smith, Meredith Needham, Todd, Ethan Domagala, Spencer Hoehl, Cory Dixon, Joe (AOC contact), Thinh (contract manufacturing contact), Laura (UASD operator), Nick, Roger (Vertiq liaison), Admiral Cary (NOAA leadership), Ali Sulehria, Frank (electronics engineer), and additional engineering staff.

## Key Decisions

**Aircraft Design & Configuration:**
- User panel positioned on bottom of NOAA S0 for easier access through outer tube (June 2020)
- Selected T-Motor F60 for propulsion due to discontinued KDE motor (September 2020)
- Switched from Castle ESC to 36A version for improved reliability (November 2020)
- Spring steel antenna wrapped around fuselage confirmed as optimal design (November 2020)
- Wing pivot system designed to "fall away" after deployment to save weight (December 2020)
- Deployment timing set at 1s door open detection, 3s later chute deploy, 5s later tube jettison, 5s later aircraft release (updated July 6, 2026; previously April 2021: 5 seconds parachute flap, 10 seconds tube release)

**Sensor & Electronics:**
- Selected SF20 laser altimeter over SF22 due to Ardupilot/PX4 integration issues (January 2021)
- Eliminated datalogging requirement after presentation feedback (April 2021)
- Selected MLX90614ESF-DCH thermal sensor per Terry's recommendation (December 2021)
- Direct soldering battery/ESC to AP due to space constraints (November 2021)
- Dual USB-A ports on front panel instead of USB-C for GCS (May 2022)
- Motor controller switched to Vertiq propulsion system (serial numbers approximately 37-42 onward in 2024 batch; earlier units used different system) (August 2026)
- **Pitch-to-Power Controller Adjustment:** Modified no_ias_a parameter from -2.8 to -2.4989 to address throttle performance issues caused by voltage drop over longer flights; parameter change applied to QC site for all existing S0s (August 6-7, 2026)
- **6S Battery Configuration & ESC/Motor Selection:** Evaluation underway for ESC + motor combo suitable for new 6S setup; Alex Lomis leading research into options; Jack Elston noted initial components on hand were unsuitable but expects multiple viable alternatives exist; testing commitment required but not anticipated as difficult redesign effort (September 23, 2026). **RPM Feedback Requirement:** Maciej specified that selected ESC/motor combo must have RPM feedback capability for band pass filter integration with magnetometer; Joshua Fromm confirmed requirements will be established upfront to avoid missing critical specifications (September 23, 2026)

**Manufacturing & Components:**
- 50/50 cost split between Air Force and Hurricane for KMac tubes (June 2020)
- Lee selected for deployment tube machining at $700 NRE, $95 per additional tube (March 2022)
- Aluminum caps chosen over 3D printed ones after high-Q deployment failure (May 2022)
- Switched to Samsung INR21700-50S cells replacing Panasonic NCR18650GA (February 2024)
- Decision to use 76gsm wing skins instead of 160gsm for 50g weight savings (October 2024)
- Winsource removed from future supplier selection due to defective PMXB120EBE parts and other questionable components (June 29, 2026)
- Two battery pack versions in circulation: newer packs used in all new builds (post-2026), older packs in previously built aircraft; characterized by ability/inability to accept higher power charging (July 8, 2026)
- Parachute cap design improved to tighter-fitting version (similar to SOCOM design) to prevent cordage fallout during flap opening; all old caps to be replaced with new design (July 29, 2026)
- **Vertiq Motor Integration:** Motor controller switched to Vertiq propulsion with adjustable slew-rate limiters; motors repeatedly delayed through August-September 2026; 29 motors shipped September 25, 2026 for Monday arrival; 20 additional motors shipped September 29; Vertiq production scare on September 24 required dismantling and reassembling packed motors (September 24-25, 2026); Joshua Fromm continuing to pursue Vertiq updates (September 22-25, 2026); **Remaining motors shipped by Vertiq (October 2, 2026)** with Vertiq quoting 3-week lead time for qty150 going forward (Joshua Fromm to verify if this is standard or instance-specific)

**Deployment Tube Components:**
- Spring-loaded switches under flap available for replacement; extras stored on wire rack shelf or pre-wired in a bin ready to use (September 22, 2026); replacement procedure involves using pliers/channel locks but should not involve twisting the black lead portion (risk of internal breakage), only grab metal housing sleeve; existing loctite residue is sufficient, no reapplication needed (September 22, 2026)

**PSNS (Power Supply Network System) Hardware Strategy:**
- **v0.4 and v0.41 Board Retirement Decision:** All v0.4 and v0.41 boards to be removed from service and placed into separate bin; no rework planned for these boards (October 28, 2026); indicates shift to v0.5 boards as primary PSNS hardware going forward
- **v1.5 Firmware Implementation:** New firmware version v1.5 developed to address sleep mode and CAN communication issues; additional testing and fixes required from Ali Sulehria (October 30, 2026)
- **Firmware Approach:** v0.5 boards being deployed with updated firmware fixes; v1.5 additional fix planned for next week; clarification needed regarding which changes were implemented in earlier reworks (October 28, 2026)

**Ground Control Station Operations:**
- Single operator per aircraft confirmed as acceptable by NOAA operational rules (April 2026)
- GCS firmware updates for dual-channel radio control implemented (April 2026)
- Use of Channel 1 designated for flight operations over Avon Park (April 2026)
- Channel 1 selected for operational use after RF cable replacement on Channel 2 (April 2026)
- Radio channel designation decided as "RADIO A / RADIO B" to minimize confusion with other numbering schemes (May 7, 2026)
- Jack Elston approved RADIO A/B nomenclature over alternatives (RADIO 1/2, CH 1/2, etc.) (May 7, 2026)
- Channel labeling standardized across all systems from CH1/CH2 to A/B nomenclature for consistency (July 9, 2026)
- Jack Elston implemented major firmware and QC tool overhaul to update channels from "one and two" to "a and b" (July 9, 2026)
- Color coding updates applied alongside channel labeling changes (July 9, 2026)
- Joshua Fromm to review and modify ground station parts procurement list before finalization (May 7, 2026)
- RF connector modification implemented for radio compatibility (May 7, 2026)
- Jack Elston's suggested quantities approved as baseline for testing + 2 upcoming builds with overage on cheap parts (May 7, 2026)
- Joshua Fromm confirmed procurement list would only require cable change; most major components (USB hub, power brick, etc.) can be ordered (May 8, 2026)
- Jack Elston submitted openups and batteries for purchase to avoid duplication (May 8, 2026)
- Joshua Fromm updated comprehensive procurement spreadsheet (2026 DUAL tab) with all components except stocked materials like ring terminals and clikmates (May 8, 2026)
- **GCS Operational Handover:** Discussion initiated regarding whether GCS units being produced are intended for NOAA operational handover; proposal suggested duplicate testing station at BST for troubleshooting issues NOAA may encounter with remotely operated stations (May 7, 2026)
- **Higher-Rate Data Recording:** NOAA requested modification to ground stations to enable higher-rate data availability for operational use as early as 2026 season; Jack Elston planning to integrate this modification into new GCS builds with P3 simulator testing prior to implementation (May 27, 2026)
- **GCS 001 Connectivity Issues Resolved:** Jack Elston provided command sequence for updating gcsDaemon to fix connection issues: scp/ssh into station, stop daemon, move new binary, restart daemon (August 20, 2026)
- **Microhard Radio Configuration:** Implemented ATS108 (October 23, 2026)
- **GCS Radio Heating Issue Resolution:** New firmware version identified that fixes radio heating problems; limited testing in fuselage requested to verify (October 30, 2026)

**Power Supply & Battery Management:**
- **PSNS Sleep Mode Issues - RESOLVED & NEW VERSION DEPLOYED:** Jack Elston diagnosed root cause of ~4 mA "fake sleep" condition in power supply network system (PSNS); issue traced to MC33772C BMS remaining awake after PSNS loses power without entering sleep mode; LTC2954 (U13) normally enables buck from VBATT, but when tube enters SHUTDOWN, TurnOffAircraft() holds PSNS power line low for ≥7s; however, PSNS previously ignored this line while CHARGING and RUNNING_PROTECTED; fix implemented in new firmware (v0.4, v0.41, v0.5) for PSNS and deployment tube (October 23, 2026); v1.5 additional fix proceeding for testing (October 30, 2026); ~1 mA case remains open
- **PSNS Firmware CAN Communication Issue - REQUIRES FURTHER INVESTIGATION:** New firmware versions on v0.4 and v0.5 boards only transmit supply packets over CAN bus; QC testing failed to read serial numbers; Ali Sulehria confirmed issue by testing v0.4 board before and after firmware flash—expected packets were present before update but only supply packets appeared after flashing (October 23, 2026); v1.5 fix addressing this regression now requires testing

**Production & Logistics (October 30, 2026 - Updated):**
- **Current Week (Week of Oct 30):** 
  - Perform additional v1.5 PSNS fix (Ali Sulehria)
  - Redo QC on v1.5 PSNS with fixes in place (Ali Sulehria)
  - Replace all PSNS boards on built-up S0s and re-QC
  - Finish kits needed for new S0s to complete 13-aircraft order
- **Following Week:** Finish all QCs, pack and ship 13 S0 aircraft
- **Earlier Target (Oct 28):** PSNS swap execution strategy: S0 disassembly and board replacement proceeding with target ship date no later than October 13 (November 13)
- Estimated timeline: 30-40 hours for batch assembly/pallet prep; 40-50 hours accounting for training of new personnel

**Project Management & Planning:**
- Kanban board restructure in progress; projects being organized for review including:
  - 001-07 S3 IRAD
  - 600-1 SOCOM Pope
  - 300-3 2026 IDIQ (Hurricane)
  - 001-04 S0 VTOL IRAD
- Milestones added to 2026 IDIQ (Hurricane) project with close-out criteria for next couple months
- Asana project created for UK RAVEN with cost account number; milestone planning deferred pending leadership approval
- Web-controller "Ready for Testing" features all passed QC (October 30, 2026)

## Projects & Initiatives

**S0 Aircraft Development & Production (Priority Project)**
- Ongoing design refinement and manufacturing of hurricane reconnaissance aircraft
- Active quality control testing and verification processes
- **S0 PSNS Swap & Firmware Update Campaign (Oct 30 - Nov delivery):** 13 aircraft undergoing PSNS board replacement and firmware updates
  - Current week focus: v1.5 firmware testing/implementation, QC on updated boards, PSNS board replacement on built-up S0s
  - Following week: Complete all QCs, pack and ship 13 aircraft
  - Target ship date: No later than November 13, 2026
  - Personnel training ongoing for disassembly/swap procedures
- Continuous iteration on components, firmware, and operational procedures
- S3 aircraft development remains co-priority with S0 work coordinated around S3 schedule

**PSNS (Power Supply Network System) Sleep Mode Bug Fix & Hardware Migration**
- Root cause identified by Jack Elston (October 23, 2026)
- New firmware v1.5 developed with additional fixes beyond v0.5 iteration
- ~4 mA "fake sleep" case resolved in v1.5; ~1 mA case still open
- **Testing phase underway:** CAN communication regression in earlier firmware requires v1.5 fix verification by Ali Sulehria
- **Hardware transition strategy:** v0.4 and v0.41 boards being retired from service; v0.5/v1.5 boards becoming standard
- Boards to be QC'd with new firmware before aircraft installation

**Vertiq Motor Integration Project - COMPLETED**
- Motor controller switched from previous system to Vertiq propulsion (October 2, 2026 completion)
- Supply chain challenges resolved with final shipment received
- Integration now complete with adjustable slew-rate limiters operational

**GCS Dual-Channel, Higher-Rate Data & Radio Heating Implementation**
- Firmware updates completed for dual radio control capability
- **Radio Heating Issue Resolution (October 30):** New firmware version identified that fixes radio heating problems; limited fuselage testing requested
- RADIO A/B nomenclature standardized across all systems
- Comprehensive procurement process underway for new GCS builds
- Higher-rate data recording modification integrated for operational deployment
- Systems being prepared for NOAA operational handover

**Web-Controller Development**
- All "Ready for Testing" features passed QC (October 30, 2026)
- Integration ongoing with broader system testing

**Project Management Reorganization**
- Kanban board restructure with 4 major projects identified for review:
  - 001-07 S3 IRAD
  - 600-1 SOCOM Pope
  - 300-3 2026 IDIQ (Hurricane)
  - 001-04 S0 VTOL IRAD
- Milestones with close-out criteria added to 2026 IDIQ (Hurricane) project
- UK RAVEN project setup in Asana with cost account number

**Deployment Tube & Parachute System Refinement**
- Parachute cap design updated to tighter-fitting version (July 29, 2026)
- Spring-loaded switch replacement procedure documented
- All old caps scheduled for replacement

## Action Items & Commitments

**Outstanding/In-Progress:**

*Current Week (Oct 30 - Nov 6):**
- Ali Sulehria: Perform additional v1.5 PSNS fix and redo QC on v1.5 PSNS with fixes in place (October 30, 2026; due end of current week)
- Joshua Fromm & Team: Replace all PSNS boards on built-up S0s and re-QC (October 30, 2026; due end of current week)
- Joshua Fromm & Team: Finish kits needed for new S0s to complete 13-aircraft order (October 30, 2026; due end of current week)
- Jack Elston: Complete fuselage testing of new GCS firmware to verify radio heating issue resolution (October 30, 2026)

*Following Week (Nov 6+):*
- Joshua Fromm & Team: Finish all remaining QCs on S0 aircraft (November 2026)
- Joshua Fromm & Team: Pack and ship 13 S0 aircraft to NOAA (November 2026; target NLT November 13)

*Outstanding from Earlier Dates:*
- Joshua Fromm: Verify with Vertiq if 3-week lead time for qty150 motors is standard or instance-specific (as of October 2, 2026)
- Joshua Fromm: Ensure RPM feedback requirement is established upfront for 6S ESC/motor combo selection to avoid missing critical specifications (September 23, 2026)

**Completed:**
- Ali Sulehria: QC all PSNS boards in hand by close of business (October 28, 2026) - **COMPLETED**
- Sam Hild: Prepare kits (autopilots, PSNS boards) and bin for old boards - **COMPLETED** (October 29, 2026)
- Maciej: Added 4 milestones with close-out criteria for 2026 IDIQ (Hurricane) project; cleaned up project and added all Kanban tasks (October 30, 2026) - **COMPLETED**
- Web-controller team: All "Ready for Testing" features passed QC (October 30, 2026) - **COMPLETED**
- Dan Prendergast: Created Asana project for UK RAVEN with cost account number (October 30, 2026) - **COMPLETED**

## Client & External References

**NOAA (National Oceanic and Atmospheric Administration)**
- Admiral Cary (leadership contact)
- Operational user of S0 aircraft system
- Requested higher-rate data recording capability for 2026 season operations
- Established single-operator-per-aircraft as acceptable operational rule
- Will receive 13 S0 aircraft delivery (targeting November 13, 2026)
- Receiving GCS units for operational deployment with firmware that fixes radio heating issues

**Suppliers & Vendors:**
- Lee: Deployment tube machining ($700 NRE, $95 per tube)
- Vertiq: Motor controller and propulsion system supplier; 3-week lead time for qty150 (October 2, 2026) - integration complete
- Winsource: Removed from future supplier selection (June 29, 2026)
- T-Motor: Propulsion components (F60)
- Samsung: Battery cells (INR21700-50S)
- Panasonic: Previous battery cells (NCR18650GA, discontinued)
- AOC: Holds 3 S0 aircraft and other pallets for return; Joe (contact) coordinating logistics
- Matt: PSNS rework engineer and warehouse manager; Core board/firmware development source

**Internal/Team Contacts:**
- Beck Cotter: External coordination and scheduling
- Ali Sulehria: PSNS firmware testing and fixes, QC responsibility, v1.5 firmware additional fix implementation
- Alex Lomis: 6S battery configuration research
- Maciej: Storm weather monitoring, Kanban/project management coordination, web-controller features verification
- Sam Hild: Kit preparation, PSNS board bin management, troubleshooting support
- Jack Elston: Project technical leadership, firmware diagnostics and testing, GCS and radio system oversight, radio heating issue resolution verification
- Joshua Fromm: S0 disassembly/swap execution, logistics coordination, personnel training, kit completion
- Dan Prendergast: Project management in Asana, UK RAVEN project setup

## Recurring Topics & Themes

1. **Motor/Propulsion System Integration:** Repeated cycles of motor selection, ESC compatibility, RPM feedback requirements, and supplier delays; Vertiq integration completed but required extended problem-solving
2. **Power Management & PSNS Issues:** Ongoing work on sleep modes, battery configuration, power consumption optimization; v1.5 firmware addressing remaining issues; migration to standardized hardware strategy (v0.5/v1.5); CAN communication regression resolved through firmware iteration
3. **Ground Station & Radio Systems:** Continuous updates to GCS firmware, radio configuration, channel naming conventions, and data recording capabilities; radio heating issue identified and resolved through firmware update; limited fuselage testing underway
4. **Component Quality & Supply Chain:** Regular evaluation of suppliers, parts quality (defects detected and addressed), manufacturing standards; hardware standardization strategy (retiring older board versions)
5. **Firmware Testing & Deployment:** Iterative testing and debugging of new firmware versions before deployment to operational systems; CAN communication regression addressed in v1.5 update
6. **NOAA Integration & Operational Readiness:** Regular coordination with NOAA on operational requirements, handover preparation, capability enhancements; 13 aircraft delivery imminent (targeting November 13)
7. **Deployment Tube System:** Ongoing refinement of parachute deployment timing, cap design, and associated mechanical components
8. **Production Scheduling & Logistics:** Intensive focus on S0 13-aircraft order completion; clear weekly milestones established (current week: fixes and QC; following week: pack and ship); S0 work coordinated with S3 priority
9. **Hardware Diagnostics & Troubleshooting:** Active investigation and resolution of GCS radio heating issues; systematic firmware-based solution deployed; fuselage testing underway
10. **Project Management & Planning:** Kanban reorganization with 4 major project frameworks; milestone planning for multi-month roadmap; Asana integration for task tracking

## Important Resources

- [GCS Visit Draft Document](https://docs.google.com/document/d/1e57pxbMghsVvhTZb2QxfVlT7O80-tV__Nub3umt1PlM/edit?usp=drive_link) (October 23, 2026) - Agenda/planning for Russel and others visit
- PSNS Firmware Versions: v0.5 (deployed), v1.5 (additional fixes for testing); sleep mode and CAN communication fixes; firmware ready for testing/deployment with v1.5 addressing earlier regressions
- Deployment Tube Firmware: Updated to address SHUTDOWN sequence
- 2026 DUAL Procurement Spreadsheet: Comprehensive GCS and testing equipment components list
- QC Site Configuration: Modified no_ias_a parameter (-2.4989) applied to all existing S0s
- RADIO A/B Nomenclature: Standardized across all GCS and aircraft systems (replacing CH1/CH2)
- Microhard Radio: ATS108 configuration implemented
- PSNS Board Bins: Separate bin designated for old v0.4/v0.41 boards during swap campaign
- Asana Projects:
  - 2026 IDIQ (Hurricane) - main project with 4 milestones and close-out criteria
  - 001-07 S3 IRAD
  - 600-1 SOCOM Pope
  - 001-04 S0 VTOL IRAD
  - UK RAVEN (new, with cost account number)

## Recent Activity

**October 30, 2026 - Major Updates:**
- **Radio Heating Issue Breakthrough (10:20 AM):** Jack Elston confirms new GCS firmware version fixes radio heating issues; requests limited fuselage testing for verification
- **Web-Controller Status (3:42 PM):** All "Ready for Testing" features passed QC; Maciej reports positive milestone progress
- **Kanban & Project Planning (3:11 PM - 4:12 PM):** Maciej coordinates next week planning; Dan Prendergast updates on UK RAVEN project setup; Jack Elston provides detailed next week NOAA task list:
  - Perform additional v1.5 PSNS fix
  - Redo QC on v1.5 PSNS with fixes
  - Replace all PSNS boards on built-up S0s and re-QC
  - Finish kits for remaining S0s (13-aircraft order)
  - Following week: Complete all QCs, pack and ship
- **Project Roadmap Update (4:12 PM):** Maciej adds 4 milestones with close-out criteria to 2026 IDIQ (Hurricane) project; identifies 4 main Asana project frameworks for team focus
- **No Weather Threats:** Maciej notes no storms forecasted for next 7 days (October 30, 8:42 AM), enabling full schedule commitment to production

**October 29, 2026:**
- S0 PSNS swap campaign actively commenced with all kits prepared
- Jack Elston authorized work to begin when S3 allows gaps in schedule
- Joshua Fromm provided time estimates for swap execution
- Flexible timeline established with target ship date NLT November 13
- GCS radio heating problem diagnostics approach approved

**October 28, 2026:**
- Jack Elston issued comprehensive production timeline and hardware strategy updates
- v0.4 and v0.41 PSNS boards designated for retirement (no rework planned)
- v0.5 boards established as standard hardware going forward
- Clarification needed on Matt's v0.5 rework firmware changes
- S0 refurbishment planned for week following kit completion

**October 23, 2026:**
- Jack Elston diagnosed PSNS sleep mode "fake sleep" issue root cause
- Ali Sulehria identified CAN communication regression in firmware update
- New firmware versions ready for testing; ~1 mA case remains open
- GCS visit agenda drafted for upcoming Russel visit