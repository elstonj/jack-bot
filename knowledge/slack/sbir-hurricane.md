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
- **Core 2 Board Testing & Voltage Optimization (November 5-6, 2026):** v0.3 core 2 board antenna power performance dependent on supply voltage; at 3.3V output to antenna: ~1.1W (significantly less than v0.2's 1.9W); at 3.6V: power jumps significantly, approaching v0.2 performance; at 3.65V: v0.3 and v0.2 outputs within 0.04W of each other (~0.3dB margin of error per rough RF loss estimates); detailed test results and setup documentation prepared by Ali Sulehria (November 5, 2026); Jack Elston inquiring about carrier board voltage specification (November 6, 2026)

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
- **Radio Power Output Testing (November 2, 2026):** Ali Sulehria investigating full power transmission capability and conditions for 2W power draw; Jack Elston confirmed radio transmits at full power when configured to do so, but supply voltage/power constraints can limit transmission

**Ground Control Station - Hurricane App Safety Issue (November 3, 2026):**
- **Auto Surface Validate Bug:** Joshua Fromm identified critical safety issue in hurricane tablet app; auto surface validate can be triggered even when hurricane app is loaded, with aircraft in deployment tube; system displays error but proceeds with validation anyway; presents dangerous operational hazard (November 3, 2026); Jack Elston acknowledged issue (November 3, 2026)

**Production & Logistics (Updated November 5, 2026):**
- **13 S0 Aircraft Rebuild Timing - REVISED (November 5, 2026):**
  - Currently on to-do list pending S3 task completion
  - Target ship date: **End of next week (targeting week of November 10-14, 2026)**
  - Estimated effort: 30-50 hours to rebuild all 13 aircraft and load onto pallet
  - Priority focus: Complete all S3 work first to clear that workload
  - Joshua Fromm and Maciej agreed on priority sequencing to maximize productivity
- **Earlier Target (Oct 28):** PSNS swap execution strategy: S0 disassembly and board replacement proceeding with target ship date no later than October 13 (November 13)
- Estimated timeline: 30-40 hours for batch assembly/pallet prep; 40-50 hours accounting for training of new personnel
- **New Priority - Core 2 Board Testing (November 2, 2026):** v0.3 core 2 board testing assigned; preliminary RF performance data shows voltage-dependent performance; rework to 3.65V operation now complete with optimal performance confirmed; wired RF setup testing complete with detailed documentation

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
- **S0 13-Aircraft Rebuild & Delivery Campaign (Nov 5-14, 2026):** Currently positioned in to-do queue pending S3 task completion
  - Revised timeline: Begin work after S3 wraps up, target end-of-week delivery (Week of November 10-14)
  - Estimated effort: 30-50 hours for complete rebuild and pallet preparation
  - All aircraft require PSNS board replacement and related updates
  - Maciej and Joshua Fromm coordinated priority sequencing to maximize efficiency
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
- **Hurricane App Safety Issue Investigation (November 3, 2026):** Auto surface validate bug identified allowing dangerous validation commands while aircraft in tube; requires fix to prevent operation when aircraft powered down or in operational state

**Web-Controller Development**
- All "Ready for Testing" features passed QC (October 30, 2026)
- Integration ongoing with broader system testing

**Core 2 Board RF Performance & Voltage Optimization - ADVANCED (November 5-6, 2026)**
- v0.3 core 2 board returned from trace cutting; testing initiated (November 2, 2026)
- **Voltage Dependency Discovered:** Antenna power output directly correlates to supply voltage to antenna connector
  - **3.3V output:** ~1.1W (significantly reduced vs v0.2 1.9W baseline)
  - **3.6V output:** Power jumps to approach v0.2 performance
  - **3.65V output:** v0.3 and v0.2 outputs within 0.04W (~0.3dB margin per rough estimates with RF loss uncertainties)
- **Testing Status:** All test setup details and RF loss estimates documented by Ali Sulehria (November 5, 2026); comprehensive analysis shared with team
- **Next Step:** Jack Elston determining carrier board voltage specification to inform implementation decision (November 6, 2026)
- **Priority:** Elevated testing priority relative to S3 QC work

**Project Management Reorganization**
- Kanban board restructure with 4 major project frameworks identified for review:
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

*Current/Ongoing:*
- Joshua Fromm: Begin 13 S0 aircraft rebuild when S3 tasks complete; complete all rebuilds and load onto pallet by end of week of November 10-14 (~30-50 hours effort); coordinate personnel and timeline for efficient execution (November 5, 2026)
- Jack Elston: Determine carrier board voltage specification to inform Core 2 board implementation decision (following up on Ali Sulehria's voltage optimization testing) (November 6, 2026)

*Earlier Outstanding:*
- Joshua Fromm: Verify with Vertiq if 3-week lead time for qty150 motors is standard or instance-specific (as of October 2, 2026)
- Joshua Fromm: Ensure RPM feedback requirement is established upfront for 6S ESC/motor combo selection to avoid missing critical specifications (September 23, 2026)
- Joshua Fromm: Query NOAA regarding EMSS (Iridium Enhanced Mobile Satellite Services) access availability as contingency communication option, if needed (November 3, 2026)
- Jack Elston: Investigate and fix auto surface validate safety bug in hurricane app to prevent dangerous validation commands when aircraft is powered down or in operational/tube state (November 3, 2026)
- Jack Elston: Complete fuselage testing of new GCS firmware to verify radio heating issue resolution (October 30, 2026)

**Completed:**
- Ali Sulehria: Core 2 v0.3 board antenna power testing and voltage optimization analysis (November 5, 2026) - **COMPLETED**; comprehensive RF test data and setup documentation provided
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
- Will receive 13 S0 aircraft delivery (targeting end of week November 10-14, 2026)
- Receiving GCS units for operational deployment with firmware that fixes radio heating issues
- May have EMSS (Iridium Enhanced Mobile Satellite Services) access capability (Joshua Fromm planning to inquire)

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
- Ali Sulehria: PSNS firmware testing and fixes, QC responsibility, v1.5 firmware additional fix implementation, core 2 board RF testing and voltage optimization analysis (November 5, 2026), RF performance measurement and documentation
- Alex Lomis: 6S battery configuration research
- Maciej: Storm weather monitoring, Kanban/project management coordination, web-controller features verification, S3 priority coordination
- Sam Hild: Kit preparation, PSNS board bin management, troubleshooting support
- Jack Elston: Project technical leadership, firmware diagnostics and testing, GCS and radio system oversight, radio heating issue resolution verification, core 2 board testing assignment, hurricane app safety bug investigation, carrier board voltage specification determination
- Joshua Fromm: S0 disassembly/swap execution, logistics coordination, personnel training, kit completion, NOAA communication, S0 rebuild project leadership
- Dan Prendergast: Project management in Asana, UK RAVEN project setup

## Recurring Topics & Themes

1. **Motor/Propulsion System Integration:** Repeated cycles of motor selection, ESC compatibility, RPM feedback requirements, and supplier delays; Vertiq integration completed but required extended problem-solving
2. **Power Management & PSNS Issues:** Ongoing work on sleep modes, battery configuration, power consumption optimization; v1.5 firmware addressing remaining issues; migration to standardized hardware strategy (v0.5/v1.5); CAN communication regression resolved through firmware iteration
3. **Ground Station & Radio Systems:** Continuous updates to GCS firmware, radio configuration, channel naming conventions, and data recording capabilities; radio heating issue identified and resolved through firmware update; limited fuselage testing underway; newly identified safety bugs in hurricane app requiring urgent attention
4. **Component Quality & Supply Chain:** Regular evaluation of suppliers, parts quality (defects detected and addressed), manufacturing standards; hardware standardization strategy (retiring older board versions)
5. **Firmware Testing & Deployment:** Iterative testing and debugging of new firmware versions before deployment to operational systems; CAN communication regression addressed in v1.5 update
6. **NOAA Integration & Operational Readiness:** Regular coordination with NOAA on operational requirements, handover preparation, capability enhancements; 13 aircraft delivery imminent (targeting end of week November 10-14); contingency communication options (EMSS) under evaluation
7. **Deployment Tube System:** Ongoing refinement of parachute deployment timing, cap design, and associated mechanical components
8. **Production Scheduling & Logistics:** Intensive focus on S0 13-aircraft order completion; clear weekly milestones established; S0 work coordinated with S3 priority
9. **Hardware Diagnostics & Troubleshooting:** Active investigation and resolution of GCS radio heating issues; systematic firmware-based solution deployed; fuselage testing underway; core board RF performance optimization through voltage tuning; emerging safety issues in ground control applications
10. **Project Management & Planning:** Kanban reorganization with 4 major project frameworks; milestone planning for multi-month roadmap; Asana integration for task tracking
11. **RF/Antenna Performance:** Core 2 board voltage-dependent antenna output optimization; v0.3 achieves v0.2 performance levels when supply voltage increased to 3.65V; detailed RF performance characterization and testing completed
12. **Safety & Risk Management:** Newly identified operational safety issues (hurricane app auto surface validate bug) requiring priority fixes to prevent dangerous commands when aircraft is in tube or non-operational state

## Important Resources

- [GCS Visit Draft Document](https://docs.google.com/document/d/1e57pxbMghsVvhTZb2QxfVlT7O80-tV__Nub3umt1PlM/edit?usp=drive_link) (October 23, 2026) - Agenda/planning for Russel and others visit
- [Core 2 Board v0.3 RF Performance Testing Results](https://docs.google.com/document/d/1TwzVkzhRJlIWcfJWMDfbuFnDnY1NEpKHOSGEBFaeqJs/edit?usp=sharing) (November 5, 2026) - Detailed antenna power testing at multiple voltages (3.3V, 3.6V, 3.65V); includes test setup details and RF loss calculations; confirms v0.3 performance matches v0.2 at 3.65V within ~0.04W (~0.3dB margin)
- [Iridium Enhanced Mobile Satellite Services (EMSS)](https://www.iridium.com/markets/governments/us-government/iridium-enhanced-mobile-satellite-services) - Contingency communication resource; NOAA access status to be confirmed by Joshua Fromm
- PSNS Firmware Versions: v0.5 (deployed), v1.5 (additional fixes for testing); sleep mode and CAN communication fixes; firmware ready for testing/deployment with v1.5 addressing earlier regressions
- Deployment Tube Firmware: Updated to address SHUTDOWN sequence
- 2026 DUAL Procurement Spreadsheet: Comprehensive GCS and testing equipment components list
- QC Site Configuration: Modified no_ias_a parameter (-2.4989) applied to all existing S0s
- RADIO A/B Nomenclature: Standardized across all GCS and aircraft systems (replacing CH1/CH2)
- Microhard Radio: ATS108 configuration implemented
- PSNS Board Bins: Separate bin designated for old v0.4/v0.41 boards during swap campaign
- Core 2 Board v0.3 Voltage Optimization: Supply voltage to antenna directly impacts performance; optimal operation at 3.65V achieves parity with v0.2 baseline; Jack Elston determining carrier board voltage specification for implementation
- Hurricane App: Identified safety issue with auto surface validate feature; requires fix to prevent operation when aircraft is powered down or in operational state
- Asana Projects:
  - 2026 IDIQ (Hurricane) - main project with 4 milestones and close-out criteria
  - 001-07 S3 IRAD
  - 600-1 SOCOM Pope
  - 001-04 S0 VTOL IRAD
  - UK RAVEN (new, with cost account number)

## Recent Activity

**November 6, 2026:**
- **Core 2 Board Voltage Specification Inquiry:** Jack Elston asks Ali Sulehria about carrier board voltage specification following Ali's comprehensive RF testing documentation (00:07 AM)

**November 5, 2026:**
- **Core 2 v0.3 RF Performance Breakthrough (15:51):** Ali Sulehria shares comprehensive antenna power testing results showing voltage-dependent performance:
  - 3.3V output: ~1.1W (significantly less than v0.2's 1.9W)
  - 3.6V output: Power jumps significantly toward v0.2 performance
  - 3.65V output: v0.3 and v0.2 within 0.04W difference (~0.3dB margin with rough RF loss estimate uncertainties)
  - Detailed test setup and calculations documented in shared Google Doc
- **S0 13-Aircraft Rebuild Timeline Revision (15:36-17:51):** Joshua Fromm communicates updated shipping timeline for 13 S0 aircraft rebuild:
  - Currently moved to to-do list pending S3 task completion
  - Target: Ship end of next week (Week of November 10-14, 2026)
  - Estimated effort: 30-50 hours to rebuild and load onto pallet
  - Maciej concurs with priority sequencing: S3 work first to clear plate
  - Light-hearted team banter about workload management (16:40-17:51)

**November 3, 2026:**
- **EMSS Contingency Communication Inquiry:** Joshua Fromm suggests querying NOAA regarding Iridium Enhanced Mobile Satellite Services (EMSS) access availability; notes this is preliminary and not currently planned for use, but useful to understand capability for potential future paths (10:51 AM)
- **Hurricane UI Compliment:** Joshua Fromm praises hurricane tablet app UI design (11:13 AM)
- **Auto Surface Validate Safety Bug Identified:** Joshua Fromm reports critical bug in hurricane app where auto surface validate can be triggered even when app is loaded with aircraft in deployment tube; system displays error but proceeds with validation anyway, creating dangerous operational hazard (14:04); Jack Elston acknowledges issue for investigation (14:27)

**November 2, 2026:**
- **Core 2 Board RF Testing Assignment:** Jack Elston includes Ali Sulehria and additional team member on email regarding v0.3 core 2 board testing following trace cutting completion (9:36 AM)
- **Testing Priority Clarification:** Ali Sulehria questions whether core 2 board testing is higher priority than S3 QC work (9:39 AM)
- **Radio Power Output Investigation (12:02 PM - 1:25 PM):** Ali Sulehria inquires with Jack Elston about inducing full 2W radio transmission and identifying when during operation radio draws full power; Jack Elston confirms radio transmits at full 2W when configured to do so, but supply voltage/power constraints can limit transmission to lower levels (confirmed yes on normal boot with antenna, but contingent on adequate power supply)
- **RF Performance Measurements (3:55 PM - 3:57 PM):** Ali Sulehria reports preliminary antenna output testing results: v0.3 core 2 board shows ~2dB lower peak readings than v0.2 after several test setup consistency attempts; cannot confirm exact differential until rework to 3.65V and wired RF setup testing; confirms measurable difference between versions exists (100% certainty noted)

---

## Updates Since Last Summary
**New Developments (November 5-6, 2026):**
- Core 2 board voltage optimization testing completed; comprehensive RF performance characterization shows v0.3 achieves v0.2 parity at 3.65V supply
- S0 13-aircraft rebuild timeline revised to end-of-week delivery (targeting November 10-14); currently sequenced after S3 task completion with estimated 30-50 hour rebuild effort
- Team collaboration on prioritization maintaining focus on S3 completion before S0 production ramp
- Jack Elston investigating carrier board voltage specification to determine implementation path for optimized Core 2 performance