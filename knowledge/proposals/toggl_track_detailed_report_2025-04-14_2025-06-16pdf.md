# Toggl Track Time Report - S0 Hurricane Phase II Project

## Document Metadata
- **Type**: Time tracking report (detailed time entries)
- **Client/Agency**: NOAA
- **Program/Solicitation**: [301-3] S0 Hurricane Phase II - 2025
- **Date**: April 14, 2025 – June 16, 2025
- **Report Generated**: June 17, 2025
- **BST Products/Systems Referenced**: S0 (Hurricane observation system)
- **Key Personnel**: Josh Fromm, Sam Hild, Jack Elston, Nate (last name not provided), Ethan Domagala, Stachura, Alex, Dan, Alec Mallinger, Austin Vera

## Executive Summary
This is a detailed time tracking report documenting 1,252 hours and 37 minutes of work by Black Swift Technologies staff on the S0 Hurricane Phase II project for NOAA (contact: Joe Cione) from mid-April through mid-June 2025. The work spans hardware construction, firmware development, avionics testing, and system integration activities in preparation for pre-season testing (planned for June 8-30).

## Technical Approach & Activities

### Primary Work Categories

**Firmware Development (Jack Elston - primary responsibility)**
- Continuous firmware development and debugging
- Moving Base RTK (Real-Time Kinematic) GPS system implementation and fixes
- Hurricane Controller Algorithm fixes (Dan - software engineer)
- PSNS (Payload System) firmware development
- Autopilot setup and configuration
- UBX protocol debugging (Zero Relpos Bug fixes, UBX Send Frequency problems)
- RTCM packet handling (Fixed Lost RTCM Packets in Base Station Buffering; Fixed missing RTCM Packet for fw HPG 1.12 Bug)
- Rover RTCM forwarding testing
- Board-level testing (VLD1 new board testing, S0 Deployment board testing)

**Hardware Construction & Assembly (Ethan Domagala, Alec Mallinger, Austin Vera)**
- Parachute tube construction and deployment systems
- Arming switch and arming flap assembly
- Latch mechanism construction (latch plate countersink, latch grinding, latch tray installation)
- Battery assembly and deployment battery preparation
- PCB soldering and attachment
- Elevator assembly and linkages
- Wing construction and servo wiring
- Deployment tube construction, riveting, and finishing
- Aircraft clasp assembly and grinding
- Release button construction and filing
- Antenna/bushing preparation
- Tail reaming and antenna attachment
- Test lead creation
- Component finishing and quality control

**Testing & Verification (Sam Hild - lead)**
- VLD1 Driver testing (radar altimeter setup and testing)
- Moving Base RTK system testing and verification
- S0 Hurricane Deployment Board testing
- S0 Hurricane AP (Autopilot) bringup
- S0 Hurricane Moving Baseline RTK testing
- RTCM verification tools development
- Hardware integration testing
- Wiring diagram creation and verification (05/19, 05/20, 05/21)

**System Integration (Nate, Josh Fromm, Stachura)**
- General avionics testing
- Wing servo testing and preparation
- Radar testing
- Arming and deployment system testing
- Hardware checklist development
- Data transmission and communications for June ET test block (Jack Elston)

**Project Planning & Coordination (Jack Elston)**
- Bi-weekly prep meetings for ET pre-season testing (8-30 June)
- S0 project status meetings
- Hurricane Controller Algorithm fixes discussions
- ET (Environmental Test) industry needs assessment
- UK ET Summit preliminary discussions
- DCA Event - UxS participation planning
- Hurricane app improvements discussions
- Black Swift ET Flight Plans
- NOAA/BST IP Discussion (Intellectual Property)
- Data processing coordination

**Training & Compliance**
- Aviation Safety Course (Stachura - 5+ hours across 05/25-05/26)

### Key Technical Systems Addressed

1. **Moving Base RTK GPS System**
   - Base station buffering fixes
   - Rover RTCM packet forwarding
   - UBX protocol message handling
   - Firmware versioning and compatibility (HPG 1.12)
   - Fixed/relative positioning calculations

2. **Radar Altimeter (VLD1 Driver)**
   - Multiple testing phases
   - Integration with autopilot
   - Signal verification

3. **Autopilot System**
   - Setup and configuration
   - Firmware integration
   - Control algorithm development
   - Flight plan compatibility

4. **Mechanical Deployment Systems**
   - Parachute deployment mechanism
   - Arming sequences
   - Battery power management
   - Aircraft attachment and release mechanisms

## Products & Capabilities Described

### S0 System
- **What it is**: Hurricane observation/sampling aerial vehicle designed for NOAA
- **Key subsystems**:
  - Avionics suite (autopilot, GPS/RTK, radar altimeter)
  - Deployment system (parachute module with arming mechanism)
  - Power system (batteries with deployment sequencing)
  - Telemetry and data communications
  - Control surfaces (elevator, wing control via servos)
- **Status**: In Phase II development with hardware construction and system integration ongoing

### Moving Base RTK System
- **What it is**: Real-time kinematic GPS positioning system for accurate aircraft localization
- **Application**: Provides precision positioning for hurricane tracking missions
- **Technical focus**: RTCM protocol handling, rover/base station synchronization, packet buffering

### VLD1 Radar Altimeter Driver
- **What it is**: Hardware/firmware module interfacing to radar altimeter
- **Application**: Altitude measurement for flight control and deployment triggering
- **Development status**: Active testing phase during reporting period

## Use Cases & Applications

**Hurricane Observation & Sampling**
- S0 system designed for deployment into hurricane environments
- Real-time position tracking via Moving Base RTK
- Altitude measurement via radar altimeter
- Data transmission during operational deployment
- Pre-season testing planned for June 8-30, 2025 (Atlantic hurricane season preparation)

**Environmental Testing (ET) Campaign**
- System being prepared for field testing with NOAA
- Integration with NOAA's hurricane research operations
- Equipment trials during pre-season period before active hurricane season

## Key Results & Accomplishments

**Hardware Status (as of 06/16/2025)**
- Multiple S0 units under active construction with components nearing completion
- Parachute deployment systems: In assembly phase
- Avionics: Autopilot bring-up underway
- Mechanical systems: Wing, elevator, and control surfaces in assembly

**Firmware Maturity**
- Moving Base RTK: Multiple bug fixes completed; system approaching operational readiness
- Autopilot: Setup phase with integration testing ongoing
- Hurricane Controller Algorithm: Active development with fixes being implemented
- All major subsystem firmware in integration/testing phase

**Testing Progress**
- Board-level testing: Deployment boards undergoing verification
- System-level integration: Avionics bring-up in progress
- Scheduled for pre-season field testing June 8-30, 2025

## Notable Details

**Project Scale**
- 1,252+ hours of effort over 9 weeks indicates substantial development intensity
- Team size: ~12+ core contributors with specialized roles
- Distributed expertise: Software (firmware/control algorithms), hardware (mechanical/assembly), systems integration (avionics/testing)

**Critical Path Items**
- Firmware development (Jack Elston) consuming significant hours, indicating complexity
- Hardware assembly proceeding in parallel with firmware work
- Testing and validation (Sam Hild) heavily focused on Moving Base RTK and deployment systems

**Project Timeline**
- Mid-April: Assembly and component testing initiated
- Late April-Early May: Major testing push on radar altimeter and RTK systems
- Mid-May: Deployment board testing begins; assembly accelerates
- Early-Mid June: Intensive final assembly and system integration; autopilot bringup
- Late June: Planned transition to field testing (ET pre-season campaign)

**Technical Challenges Addressed**
- RTK packet loss and buffering issues (resolved 05/06)
- RTCM protocol compatibility (firmware version specific)
- UBX message send frequency and formatting (debugging 05/12)
- Rover positioning calculations (Zero Relpos bug fixes)

**Coordination with NOAA**
- Direct contact: Joe Cione (NOAA point of contact)
- Meetings bi-weekly for pre-season planning
- IP discussion conducted (06/11) indicating contractual/ownership considerations
- Integration with NOAA test infrastructure and procedures

This report reflects a project in active production phase with hardware reaching maturity and software systems moving through integration testing toward field deployment within 2-3 weeks of the report end date.