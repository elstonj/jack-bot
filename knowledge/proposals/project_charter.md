# NOAA Penguin BE SwiftCore Integration Project Charter

## Document Metadata
- Type: Project Charter
- Client/Agency: NOAA Air Resources Laboratory, Atmospheric Turbulence and Diffusion Division (NOAA/ARL/ATDD)
- Program/Solicitation: Not specified (appears to be a direct procurement/integration contract)
- Date: Created March 14, 2017; Final version August 8, 2017
- BST Products/Systems Referenced: SwiftCore FMS, SwiftPilot autopilot, Xeta 9M
- Key Personnel: Jack Elston (BST Project Manager), Maciej Stachura (BST), Edward Dumas (NOAA Client/Sponsor), Bruce Baker (NOAA)

## Executive Summary
Black Swift Technologies will integrate its SwiftCore/SwiftPilot autopilot system into a Penguin BE small unmanned aircraft system (sUAS) purchased by NOAA/ARL for atmospheric research operations. The project includes hardware integration, ground station development, training of NOAA personnel, and iterative flight testing leading to fully autonomous operations at up to 5 nautical miles range and 5,000 feet AGL.

## Technical Approach

**Integration Architecture:**
- Installation of SwiftCore FMS (Flight Management System) airborne unit into Penguin BE airframe
- Ground station control via tablet interface communicating on 900 MHz frequency
- Independent power system using Li-Fe battery for autopilot (separate from propulsion power)
- Four PWM channels for payload control

**Radio/Communications:**
- Upgrade radio system to guarantee 5 NM communications at 5,000' AGL
- Futaba T14SG transmitter and R7008SB receiver for manual radio-control fallback
- Configuration for conventional RC operation during initial testing

**Control Architecture:**
- SwiftCore FMS with 4-servo V-tail assembly control
- Hybrid manual/autonomous capability with incremental automation engagement
- Trim capture and doublet analysis for gain tuning

**Integration Phases:**
1. **Mechanical Integration:** Wiring development, Xeta 9M case/firmware development, surface calibration, thrust testing
2. **Flight Dynamics:** Aircraft modeling, simulation testing, control gain tuning
3. **Payload Integration:** Physical mounting, electrical integration with SwiftCore, tablet interface development
4. **Testing & Validation:** Bench testing, manual flight with data capture, auto-transition testing, payload verification

## Products & Capabilities Described

**SwiftCore FMS / SwiftPilot Autopilot:**
- Airborne autopilot unit for aircraft control
- Ground station tablet interface for flight path, altitude, and airspeed control
- 5 NM operational range at 5,000 feet AGL
- 900 MHz communication frequency
- Four PWM output channels for payload device control (start/stop functions)
- Automated control surfaces (4-servo V-tail configuration on Penguin BE)
- Hybrid manual/autonomous operation modes

**Xeta 9M:**
- Component of SwiftCore integration
- Required custom case development and firmware customization for Penguin BE
- Integrated with autopilot avionics stack

## Use Cases & Applications

**Primary Mission:**
- NOAA atmospheric research and monitoring (Air Resources Laboratory focus)
- Scientific payload deployment and in-flight control
- Autonomous flight operations for extended mission duration

**Operational Capabilities Enabled:**
- Fully autonomous waypoint-based missions
- Manual RC backup capability
- Real-time payload sensor control (start/stop via PWM channels)
- Data collection at altitude with automated flight management

## Key Results
This is a project charter (planning document), not a report with results. No flight testing or operational results are documented. The charter establishes planned milestones:
- **Phase 1 (Integration):** June 30 - September 8, 2017
- **Phase 2 (Operations & Flight Testing):** August 28 - September 15, 2017

## Notable Details

**Training Component:**
- Two NOAA employees to attend integration and simulator training at BST facility in Boulder, Colorado
- On-site operational training during flight testing
- Use of BST simulator for preliminary training

**Operational Support:**
- BST to provide pilot from CU (University of Colorado) for manual flights during testing
- Use of CU IRISS (likely Integrated Remote and In Situ Sounding) flight test facility
- BST provides flight testing facilities and insurance

**Intellectual Property & Operational Model:**
- BST retains IP for SwiftCore integration into Penguin BE
- Aircraft to be returned to NOAA after project completion
- Incremental autonomous capability testing approach (manual → partial automation → full autonomy)

**Budget:**
- Phase 1 (Integration): $31,475
- Phase 2 (Operations & Training): $8,780
- Total: $40,255

**Test Location:**
- SLV (San Luis Valley) test range in southern Colorado for flight operations

**Risk Management:**
- Primary risk identified: airframe damage/loss during flight testing causing schedule delays
- Mitigation through gradual automation transition and manual RC fallback capability