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
- **Firmware Approach:** Clarification needed regarding which suggested changes were implemented in v0.5 rework by Matt; if v0.4 or v0.41 boards are needed for future use, additional changes would be required beyond current state (October 28, 2026)

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

**Power Supply & Battery Management:**
- **PSNS Sleep Mode Issues:** Jack Elston diagnosed root cause of ~4 mA "fake sleep" condition in power supply network system (PSNS); issue traced to MC33772C BMS remaining awake after PSNS loses power without entering sleep mode; LTC2954 (U13) normally enables buck from VBATT, but when tube enters SHUTDOWN, TurnOffAircraft() holds PSNS power line low for ≥7s; however, PSNS previously ignored this line while CHARGING and RUNNING_PROTECTED; fix implemented in new firmware (v0.4, v0.41, v0.5) for PSNS and deployment tube (October 23, 2026); firmware ready for testing but not yet flashed or bench-tested
- **PSNS Firmware CAN Communication Issue:** New firmware versions on v0.4 and v0.5 boards only transmit supply packets over CAN bus; QC testing failed to read serial numbers; Ali Sulehria confirmed issue by testing v0.4 board before and after firmware flash—expected packets were present before update but only supply packets appeared after flashing (October 23, 2026); issue requires investigation and resolution

## Projects & Initiatives

**S0 Aircraft Development & Production**
- Ongoing design refinement and manufacturing of hurricane reconnaissance aircraft
- Active quality control testing and verification processes
- Multiple aircraft builds in various stages of completion (13 aircraft owed to partner due for shipment end of week or start of following week as of October 28, 2026)
- Continuous iteration on components, firmware, and operational procedures
- S0 refurbishment underway replacing PSNS boards with v0.5 versions (expected completion by end of week of October 28, 2026)

**PSNS (Power Supply Network System) Sleep Mode Bug Fix & Hardware Migration**
- Root cause identified by Jack Elston (October 23, 2026)
- New firmware deployed for testing on v0.4, v0.41, and v0.5 boards
- ~4 mA "fake sleep" case resolved; ~1 mA case still open
- Testing phase underway to validate fixes
- CAN communication regression in new firmware requires resolution
- **Hardware transition strategy:** v0.4 and v0.41 boards being retired from service; v0.5 boards becoming standard (October 28, 2026)
- All PSNS boards in hand to be QC'd by close of business (October 28, 2026)
- Remaining S0 kits to be built up by end of week (October 28, 2026)
- S0 refurbishment (PSNS replacement) scheduled for completion by end of following week (week of October 28, 2026)

**Vertiq Motor Integration Project**
- Motor controller switched from previous system to Vertiq propulsion (October 2, 2026 completion)
- Supply chain challenges resolved with final shipment received
- Integration now complete with adjustable slew-rate limiters operational

**GCS Dual-Channel and Higher-Rate Data Implementation**
- Firmware updates completed for dual radio control capability
- RADIO A/B nomenclature standardized across all systems
- Comprehensive procurement process underway for new GCS builds
- Higher-rate data recording modification integrated for operational deployment
- Systems being prepared for NOAA operational handover

**Deployment Tube & Parachute System Refinement**
- Parachute cap design updated to tighter-fitting version (July 29, 2026)
- Spring-loaded switch replacement procedure documented
- All old caps scheduled for replacement

## Action Items & Commitments

**Outstanding/In-Progress:**
- Jack Elston: Coordinate visit by Russel and others; finalize draft agenda/schedule document (October 23, 2026)
- Jack Elston & Ali Sulehria: Bench-test new PSNS firmware (v0.4, v0.41, v0.5) for sleep mode fixes and CAN communication regression (October 23, 2026)
- Joshua Fromm: Verify with Vertiq if 3-week lead time for qty150 motors is standard or instance-specific (as of October 2, 2026)
- Joshua Fromm: Ensure RPM feedback requirement is established upfront for 6S ESC/motor combo selection to avoid missing critical specifications (September 23, 2026)
- Ali Sulehria: QC all PSNS boards in hand by close of business (October 28, 2026)
- Team: Build up remaining S0 kits by end of week (as of October 28, 2026)
- Team: Refurbish S0 aircraft (replace PSNS with v0.5 boards) by end of following week (as of October 28, 2026)
- Team: Ship 13 S0 aircraft by end of week of October 28 or start of following week
- Joshua Fromm: Coordinate with Matt B via Jack Elston regarding logistics of returning 3 aircraft from AOC and shipping 13 aircraft; clarify whether to wait on consolidated pallet shipment or proceed with separate shipments to save money (October 28, 2026)

## Client & External References

**NOAA (National Oceanic and Atmospheric Administration)**
- Admiral Cary (leadership contact)
- Operational user of S0 aircraft system
- Requested higher-rate data recording capability for 2026 season operations
- Established single-operator-per-aircraft as acceptable operational rule
- Will receive GCS units for operational deployment

**Suppliers & Vendors:**
- Lee: Deployment tube machining ($700 NRE, $95 per tube)
- Vertiq: Motor controller and propulsion system supplier; 3-week lead time for qty150 (October 2, 2026)
- Winsource: Removed from future supplier selection (June 29, 2026)
- T-Motor: Propulsion components (F60)
- Samsung: Battery cells (INR21700-50S)
- Panasonic: Previous battery cells (NCR18650GA, discontinued)
- AOC: Holds 3 S0 aircraft and other pallets for return; Matt B (contact) coordinating logistics

**Internal/Team Contacts:**
- Beck Cotter: External coordination and scheduling; confirming preferences regarding shipment consolidation (October 28, 2026)
- Ali Sulehria: PSNS firmware testing and QC; board QC responsibility (October 28, 2026)
- Alex Lomis: 6S battery configuration research
- Maciej: Motor/ESC RPM feedback requirements
- Matt: PSNS rework engineer conducting v0.5 board changes; warehouse space management (October 28, 2026)

## Recurring Topics & Themes

1. **Motor/Propulsion System Integration:** Repeated cycles of motor selection, ESC compatibility, RPM feedback requirements, and supplier delays; Vertiq integration completed but required extended problem-solving
2. **Power Management Issues:** Ongoing work on PSNS sleep modes, battery configuration, power consumption optimization across multiple voltage systems; hardware migration strategy now in place (v0.5 standardization)
3. **Ground Station Development:** Continuous updates to GCS firmware, radio configuration, channel naming conventions, and data recording capabilities
4. **Component Quality & Supply Chain:** Regular evaluation of suppliers, parts quality (defects detected and addressed), manufacturing standards
5. **Firmware Testing & Deployment:** Iterative testing and debugging of new firmware versions before deployment to operational systems
6. **NOAA Integration:** Regular coordination with NOAA on operational requirements, handover preparation, and capability enhancements
7. **Deployment Tube System:** Ongoing refinement of parachute deployment timing, cap design, and associated mechanical components
8. **Production Scheduling & Logistics:** Coordination of aircraft builds, QC procedures, and customer shipments with timeline management

## Important Resources

- [GCS Visit Draft Document](https://docs.google.com/document/d/1e57pxbMghsVvhTZb2QxfVlT7O80-tV__Nub3umt1PlM/edit?usp=drive_link) (October 23, 2026) - Agenda/planning for Russel and others visit
- PSNS Firmware Versions: v0.4, v0.41, v0.5 (with sleep mode and CAN communication fixes)
- Deployment Tube Firmware: Updated to address SHUTDOWN sequence
- 2026 DUAL Procurement Spreadsheet: Comprehensive GCS and testing equipment components list
- QC Site Configuration: Modified no_ias_a parameter (-2.4989) applied to all existing S0s
- RADIO A/B Nomenclature: Standardized across all GCS and aircraft systems (replacing CH1/CH2)
- Microhard Radio: ATS108 configuration implemented

## Recent Activity

**October 28, 2026:**
- Jack Elston issued comprehensive production timeline and hardware strategy updates:
  - v0.4 and v0.41 PSNS boards to be removed from service and separated into different bin; no rework planned
  - Clarification needed on which firmware changes were implemented in Matt's v0.5 rework; if v0.4/v0.41 needed in future, additional changes required
  - PSNS boards in hand to be QC'd by close of business (Ali Sulehria responsibility)
  - Remaining S0 kits to be built up by end of week
  - S0 refurbishment (PSNS replacement with v0.5) scheduled for completion by end of following week
  - 13 S0 aircraft shipment planned for end of week or start of following week
  - Suggested including 3 AOC aircraft in return shipment to recover pallets; requested Joshua Fromm to check with Matt B about this addition
- Joshua Fromm raised concern about potential change to previously discussed shipping logistics plan: clarified that original plan was to ship 13 aircraft in pallet and have NOAA return all 3 AOC aircraft stacked to save money; questioned whether new proposal (separate shipments) represented abandonment of consolidated approach
- Jack Elston acknowledged not recalling written plan documentation; indicated he had emailed Matt B (warehouse manager wanting to clear space) to verify waiting was acceptable
- Joshua Fromm confirmed either approach acceptable; primary concern was ensuring coordination

**October 23, 2026:**
- Jack Elston diagnosed PSNS sleep mode "fake sleep" issue (~4 mA case): MC33772C BMS remains awake when PSNS loses power without proper sleep sequence; LTC2954 (U13) and TurnOffAircraft() behavior analyzed; fix implemented in new firmware for v0.4, v0.41, v0.5 boards and deployment tube; ~1 mA case remains open; firmware ready for testing but not yet flashed/bench-tested
- Ali Sulehria identified regression in new PSNS firmware: v0.4 and v0.5 boards only transmitting supply packets over CAN after update; serial number QC reads failing; confirmed by testing v0.4 board before/after flash showing expected multi-packet transmission before update and supply-only packets after update; root cause requires investigation
- Jack Elston drafted visit agenda document for Russel and others; Beck Cotter indicated informal preference but confirmed document would be helpful for coordination