# Project Charter - Additional Testing

## Document Metadata
- Type: Project Charter
- Client/Agency: NOAA Air Resources Laboratory, Atmospheric Turbulence and Diffusion Division (NOAA/ARL/ATDD)
- Program/Solicitation: Not specified (internal project)
- Date: January 29, 2018 (Version 1.3)
- BST Products/Systems Referenced: SwiftCore FMS, SwiftPilot autopilot system
- Key Personnel: Jack Elston (BST Project Manager), Maciej Stachura (BST team member), Edward Dumas (NOAA client/sponsor), Bruce Baker (NOAA)

## Executive Summary
Black Swift Technologies will integrate its SwiftPilot autopilot system into a Penguin BE small unmanned aircraft system (sUAS) purchased by NOAA/ARL/ATDD, including SwiftCore FMS integration and testing of an upgraded propulsion system to improve climb rate and takeoff distance performance. The project includes training of NOAA personnel and iterative flight testing leading to fully autonomous operations.

## Technical Approach
- Integration of SwiftCore FMS into Penguin BE airframe equipped with 2.7kW electric motor, 100W power distribution unit, 4-servo V-tail assembly, and swappable universal payload mount
- Autopilot airborne unit with ground station tablet for flight path, altitude, and airspeed control
- Communication range: 5 nautical miles at 5,000 feet AGL on 900 MHz frequency
- Futaba T14SG transmitter and R7008SB receiver for radio-control system enabling conventional RC operation during initial testing
- Independent Li-Fe battery power for autopilot system
- Four PWM-driven payload interface channels for in-flight instrument control
- Incremental automation approach: manual RC flight → gradual autopilot engagement for controlled evaluation

## Products & Capabilities Described

**SwiftCore FMS**
- Flight management system integrated into Penguin BE airframe
- Provides automatic control of aircraft and payload
- Requires integration training and simulation training at BST facility

**SwiftPilot Autopilot System**
- Airborne unit installed in aircraft
- Ground station tablet interface
- Controls flight path, altitude, and airspeed
- 5 NM range at 5,000' AGL
- 900 MHz communication frequency
- Independent power source (Li-Fe battery)
- Four PWM channels for payload control

**Penguin BE Aircraft**
- Small UAS platform from UAV Factory
- 2.7kW electric motor
- 100W power distribution unit
- 4-servo V-tail assembly
- Swappable universal payload mount
- Original performance (climb rate and takeoff distance) below NOAA requirements; addressed through propulsion system upgrade

## Use Cases & Applications
- NOAA atmospheric research and monitoring operations
- Autonomous flight operations requiring distance control up to 5 NM
- Payload operation through in-flight PWM control
- Scientific instrument deployment and operation via swappable payload interfaces

## Key Results
Not applicable—this is a project charter defining scope and approach, not a results report. However, Phase 3 testing of the new propulsion system was scheduled for February 1 - March 15, 2018, with planned assessment of:
- Takeoff distance vs. baseline (with 10-degree flaps)
- Climb rate improvement vs. baseline
- Endurance (extrapolated from flight data and battery verification)

## Notable Details

**Project Phases & Milestones:**
- Phase 3: Testing of Updated Propulsion System (Feb 1 - Mar 15, 2018) - follow-on to address shortfalls in original Penguin UAS climb rate and takeoff distance

**Budget:** $3,716 total
- Testing of updated propulsion system: $1,200
- Manual pilot from CU (Colorado University): $1,500
- Data analysis and report: $1,016

**Training Approach:**
- Two NOAA employees travel to BST Boulder, Colorado facility for integration training and simulation training
- On-site training during test flights at NOAA-selected location
- Training covers SwiftCore FMS integration and operations

**Test Approach:**
- Benchtop and simulation testing without flying before live testing
- Initial manual RC flights using CU IRISS flight time for tuning
- Incremental autopilot engagement as pilot experience increases
- Aircraft returned to NOAA/ARL/ATDD after completion

**Key Constraints & Risks:**
- Contract negotiation delays could impact milestone completion
- Flight testing risk of airframe damage/loss could significantly delay project
- BST maintains IP for SwiftCore FMS integration methodology
- BST responsible for providing pilot, facilities, and flight testing insurance