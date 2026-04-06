# Toggl Track Time Report: S0 Hurricane Phase II Project (04/16/2025 – 05/19/2025)

## Document Metadata
- Type: Time tracking report (internal project hours documentation)
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration)
- Program/Solicitation: [301-3] S0 Hurricane Phase II - 2025
- Date: Report period 04/16/2025 – 05/19/2025 (generated 05/20/2025)
- BST Products/Systems Referenced: S0 (uncrewed aircraft system for hurricane operations)
- Key Personnel: Jack Elston, Josh Fromm, Sam Hild, Ethan Domagala, Nate, Alex, Stachura, Austin Vera

## Executive Summary
This is a detailed time-tracking report for Black Swift Technologies' S0 Hurricane Phase II project with NOAA contact Joe Cione, covering a 5-week period (April 16 - May 19, 2025). The report documents 354 hours 57 minutes 54 seconds of work across hardware construction, software development, testing, and meetings related to pre-season hurricane operations preparation.

## Technical Work Performed

### Hardware Construction & Assembly
- **Parachute Tube Construction**: Multiple team members (Ethan Domagala, Nate) worked on construction of delivery system components
- **Mechanical Components**: 
  - Latch plate countersinking and grinding (Ethan Domagala, Austin Vera)
  - Arming lock bar beveling and drilling
  - Arming switch assembly and testing
  - Sticker cutting for deliverables
- **Deployment Battery**: Multiple sessions on battery assembly/integration (Nate: 4+ hours across 04/18-04/30)
- **MHP Potting**: Encapsulation/potting work on avionics components (Ethan Domagala, 05/07)

### Electronics & Software Development
- **VLD1 Driver/Testing**: Extensive radar altimeter setup and testing (Sam Hild: 9+ hours logged across multiple sessions 04/17-05/12)
  - New VLD1 board testing (05/08)
  - VLD1 driver setup for radar altimeter
  - Iterative testing sessions throughout reporting period

- **Moving Base RTK (Real-Time Kinematic)**: GPS positioning system development (Sam Hild: 15+ hours)
  - Fixed lost RTCM packets in base station buffering (05/06)
  - Testing rover RTCM forwarding (05/07-05/08)
  - RTCM verification tools (05/08)
  - Fixed UBX send frequency problem (05/12)
  - UBX Zero Relpos bug debugging (05/12)

- **Autopilot Setup**: System configuration (Jack Elston: 3.5 hours on 05/10-05/11)

### Avionics & Integration Testing
- **Avionics Testing**: Multiple test sessions on core avionics systems (Nate: 2+ hours on 05/13)
- Team members (Alex, Stachura, Josh Fromm) logged significant integration testing hours

### Project Management & Meetings
- **Bi-weekly prep meetings**: Pre-season testing coordination for 8-30 June operations (Jack Elston: multiple sessions)
- **UAS Hurricane Symposium**: Attendance and participation (Jack Elston: 10.75 hours on 05/01-05/02; Josh Fromm: 20 hours; Sam Hild: 11+ hours)
- **ET Industry Needs**: Meeting on extended deployment operations (Jack Elston, 05/05)
- **UK ET Summit**: Preliminary discussions (Jack Elston, 05/06)
- **S0 Meeting**: Project status coordination (Jack Elston, Stachura, 05/07)

### Key Personnel Work Distribution
- **Josh Fromm**: 76.75 hours (largest time allocation; general project work across multiple areas)
- **Sam Hild**: 48+ hours (focused on RTK and VLD1 radar altimeter systems)
- **Jack Elston**: 25+ hours (meetings, presentations, pre-season testing coordination, autopilot setup)
- **Ethan Domagala**: 8+ hours (mechanical construction and assembly)
- **Nate**: 24+ hours (avionics, batteries, mechanical assembly, testing)
- **Alex**: 18+ hours (integration/testing work)
- **Stachura**: 7+ hours (assembly, testing, meetings)
- **Austin Vera**: 0.58 hours (grinding operations)

## Key Systems & Development Focus

### 1. **Parachute/Deployment System**
Construction of physical delivery mechanism with associated latching and arming hardware.

### 2. **Radar Altimeter (VLD1)**
Primary altitude measurement system requiring iterative board development and testing across multiple sessions.

### 3. **Moving Base RTK GPS**
Real-time kinematic positioning system with multiple software iterations fixing:
- RTCM packet buffering issues
- Rover RTCM message forwarding
- UBX protocol bugs (Zero Relpos, send frequency)

### 4. **Autopilot System**
Flight control and navigation setup for autonomous hurricane operations.

## Notable Details

- **Intensive Testing Phase**: Heavy concentration of VLD1 and RTK testing work indicates these systems were critical path items requiring iterative refinement
- **Manufacturing Capability**: Onsite mechanical construction suggests BST maintains hardware fabrication capabilities (countersinking, drilling, grinding, potting operations)
- **Symposium Participation**: Significant time allocated to UAS Hurricane Symposium (May 1-2) suggests industry engagement and technical presentations on S0 platform
- **Pre-Season Timeline**: Coordination for June 8-30 pre-season testing indicates operational deployment was planned for summer 2025 hurricane season
- **Software Development**: RTK debugging work across multiple days indicates active firmware/software development occurring in parallel with hardware assembly
- **Team Composition**: Mix of hardware engineers (Ethan Domagala, Austin Vera), software/systems engineers (Sam Hild), and project leads (Jack Elston, Josh Fromm)

## Invoice Status
Document location indicates this time report was associated with Invoice 1670 (dated 05/20/25) that was **rejected by NOAA**, suggesting potential billing or contract compliance issues that may have required correction or clarification.