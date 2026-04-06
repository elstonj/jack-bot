# A Ruggedized UAS for Scientific Data Gathering in Harsh Environments - Phase I Final Report

## Document Metadata
- Type: SBIR Phase I Final Report - Solution Specification section
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR (topic not specified in document)
- Date: September 10, 2016 (report date); Section completed November 7 - December 9, 2016
- BST Products/Systems Referenced: SuperSwift, SuperSwift XT, SwiftCore (FMS), SwiftPilot, SwiftTab
- Key Personnel: Jack Elston (PI), Dr. Dixon, Dr. Stachura, Dr. Diaz, Dr. Wardell

## Executive Summary
This Phase I final report documents Black Swift Technologies' plan to develop a ruggedized, high-altitude UAS (SuperSwift XT) with integrated sensor payload for volcanic plume observation and sampling. The document specifies the system design, identifies technical and operational risks with mitigation strategies, and provides a detailed 24-month Phase II implementation plan covering aircraft modifications, sensor integration, flight testing at three domestic test sites, and final validation at an active volcano (Turrialba, Costa Rica or Hawaii's Volcano National Park).

## Technical Approach

### System Design & Modifications
- **Base Platform**: SuperSwift airframe ruggedized into "SuperSwift XT" variant
- **Key Design Elements**:
  - Custom pitot-static tube for airspeed measurement in ash-laden plumes
  - Multi-hole probe (MHP) integrated into modular nose cone for wind measurement
  - Custom motor cowl designed to cool motor and protect against airborne particulates
  - Sensor payload tray and nose cone mechanical integration
  - IP 63 rating sealing on all hatches and openings for environmental protection
  - Independent battery packs for propulsion and flight controls
  - Bungee catapult launch system

### Avionics & Control Systems
- **SwiftCore**: Flight management system
- **SwiftPilot**: Autopilot system with state estimation algorithm and inertial wind calculation capability
- **SwiftTab**: Tablet-based user interface with gesture-based mission planning
- Features automatic mission planning, lost-link procedures, geo-fencing, autonomous landing

### Sensor Integration Architecture
- On-board Linux computer interfaced with autopilot for data logging
- All sensor data time-tagged and synchronized with autopilot telemetry
- Custom firmware development for sensor initialization and data streaming
- Modular design allowing rapid reconfiguration of sensor packages

## Products & Capabilities Described

### SuperSwift XT Aircraft
- **What it is**: Ruggedized, high-altitude small UAS derivative of SuperSwift platform
- **Key Specifications**:
  - Designed for operations up to 14,000+ ft altitude
  - Capable of sustained flight in turbulent conditions
  - Payload capacity sufficient for scientific instrument package (nephelometer ~18 kg, miniGAS ~5 kg estimated)
  - Catapult launch capability (launch possible from 6+ miles away from sampling site per FAA updates)
  - Can operate from difficult mountainous terrain with modifications to landing approach
- **Proposed Use**: Primary platform for volcanic plume profiling and sampling missions
- **Design Status**: CAD models finalized in Phase I; manufacturing to begin Phase II Q1

### Multi-Hole Probe (MHP)
- **What it is**: Custom-designed 5-hole wind measurement probe integrated into nose cone
- **How Used**: Measures wind vector in 3D; provides airspeed measurement backup if pitot tube clogs from ash
- **Key Features**:
  - Designed and validated through CFD analysis in Phase I
  - Requires wind tunnel testing to validate accuracy claims
  - Modular nose cone integration allows independent sensor swaps
  - Partnership with iMet planned for commercialization as part of XF sensor suite
  - Design-for-manufacturability work planned for Phase II
- **Performance Claims**: Capable of providing wind measurement accuracy sufficient for meteorological/volcanic applications (specific accuracy not quantified in this section)

### Integrated Sensor Payload
- **Nephelometer** (~$59,000): Measures aerosol concentration/optical properties
  - Risk mitigation: Can provide airspeed measurement via particle velocity tracking
- **miniGAS** (~$15,000): Gas composition measurement system
- **Additional Sensors** (referenced but not detailed): Pressure, humidity, trace gas measurement
- **Data Redundancy**: Multiple backup airspeed measurement methods (MHP, nephelometer particle velocities, GPS speed estimation)

### SwiftTab User Interface & Mission Planning
- **Tablet-based interface** with gesture recognition for intuitive operation
- **Volcanic Plume Observation Mission Plans**: Five candidate flight patterns identified
  - Patterns designed to allow adequate sensor stabilization time during transitions
  - Customizable parameters for different volcano profiles
  - Validation checks for terrain collision avoidance
  - Risk-based filtering of mission plans before upload
- **Capabilities**: Automatic mission planning, real-time flight monitoring, manual override capability
- **Future Vision**: Simple language for scientists to create custom mission plans without extensive UAS training

## Use Cases & Applications

### Primary Application: Volcanic Plume Observation
- **Target Volcanoes**: Turrialba (Costa Rica) and Volcano National Park (Hawaii) as primary sites; San Luis Valley high-altitude testing
- **Mission Profile**: Profiling flights through volcanic plumes to collect gas composition, aerosol concentration, temperature, pressure, humidity, and wind data
- **Operational Context**: 
  - Flights at high altitude (10,000-14,000+ ft) in turbulent conditions
  - Hazardous ash environment requiring robust airframe and protected sensors
  - Need for sustained multi-leg profiling patterns lasting extended flight times
  - Remote mountainous landing sites

### Secondary Applications (Implied)
- High-altitude meteorological profiling in general
- Turbulence characterization
- Atmospheric profiling in challenging environments
- Commercial science missions (referenced for cost sharing)

## Risk Management

### Programmatic Risks (Identified & Mitigated)
1. **Expensive Sensor Loss** (High Risk)
   - Mitigation: Extensive local flight testing at Pawnee National Grasslands with dummy payloads; strong BST history with expensive payloads; rigorous maintenance and procedures
   
2. **Sensor Interface Evolution**
   - Mitigation: Extensible avionics system design and modular mechanical mounts allowing rapid reconfiguration

3. **Aircraft Performance Shortfalls**
   - Mitigation: Phase I simulations validated altitude/endurance; early Phase II testing at Pawnee; aircraft design owned by BST allowing feasible modifications

4. **Flight Permission Delays**
   - Mitigation: BST's 6 successful NASA flight reviews; SuperSwift already approved for Pawnee; early applications for difficult sites (volcanoes)

5. **Difficult Landing Operations in Mountainous/Volcanic Terrain** (Highest Risk)
   - Mitigation: Multi-phase testing approach; payload-free validation flights; new FAA rules enabling launch from remote location (6+ miles away) with transit to sampling area; selection of intermediate test site near BST for safer high-altitude training

### Aircraft-Specific Risks (19 identified)
Key risks with high-consequence/low-likelihood: battery fire, autopilot failure, electrical power loss, mid-air collision, loss of command/control link, GPS loss, engine failure, structural failure, lightning strike, pitot tube ash clogging.

**Critical Innovation - Pitot Tube Clogging (Risk #19)**: Rated high-likelihood/moderate-consequence for volcanic mission; mitigated through three-layer backup:
1. Multi-hole probe provides primary airspeed backup
2. Nephelometer particle velocity measurement as secondary backup
3. GPS speed with wind estimation as tertiary backup
- Strategy allows mission continuation or safe abort even if all airspeed sensors degrade

## Phase II Implementation Plan

### Timeline: 24 months (8 quarters)

**Quarter 1** (Months 1-3):
- Requirements finalization
- FAA/NASA flight approvals submitted
- SuperSwift XT CAD design finalized
- Payload sensors ordered; XT parts sent to manufacturing

**Quarter 2** (Months 4-6):
- Prototype SuperSwift XT with SwiftCore FMS ready for flight testing
- Multi-hole probe wind tunnel verification complete
- Pawnee National Grasslands (PNG) aerodynamic performance validation flights

**Quarter 3** (Months 7-9):
- Sensor package mechanically/electrically integrated
- Lab and bench-top sensor validation
- Data analysis software development begins
- SuperSwift XT design updated based on PNG results

**Quarter 4** (Months 10-12):
- SwiftTab operator interface with automatic mission planning finalized
- PNG flight testing with integrated sensor package
- In-flight sensor data validation

**Quarter 5** (Months 13-15):
- High-altitude flight testing at San Luis Valley (SLV) site complete
- High-altitude sensor data analysis
- 2nd SuperSwift XT parts ordered/manufacturing begins

**Quarter 6** (Months 16-18):
- 2nd SuperSwift XT ready for flight testing
- End-to-end system flight testing
- Final verification/validation of in-flight data and flight performance
- NASA and Costa Rican flight approvals submitted for Turrialba

**Quarter 7** (Months 19-21):
- Deployment and flight testing at Turrialba Volcano (or backup site)

**Quarter 8** (Months 22-24):
- Final documentation: Final Report, Briefing Chart, Summary Report, NTSR submitted

### Major Work Packages

**1.0 Preliminary Tasks** (432 hours total)
- Kickoff meetings with subcontractors (40 hours PI + 40 hours each team member)
- Requirements document review and update (80 team hours)
- Test site review and evaluation (32 team hours)
- Risk review and update (16 team hours)
- Ongoing project management (352 hours: 80 upfront + 4 hours/week for 22 months)

**2.0 Flight Certification** (114 hours total)
- Pawnee National Grasslands: AFSRB/FRRB resubmission, flight safety review, monthly NASA reports (20 hours Dr. Stachura + 4 hours PI)
- San Luis Valley: New flight test plan, safety telecon, FAA COA (10 hours Dr. Stachura + 10 hours PI)
- Turrialba Volcano, Costa Rica: NASA AFSRB, Costa Rican authority permission (15 hours Dr. Stachura + 20 hours Dr. Diaz + 20 hours PI)
- Volcano National Park backup: Ranger discussions, test plan, NASA AFSRB (40 hours Dr. Stachura + 40 hours PI)

**3.0 SuperSwift XT Aircraft Development** (1,680+ hours total)
- Finalize CAD models: 40 hours each Dr. Dixon & Stachura + 10 hours PI
- Acquire/integrate first XT components: 80 hours technician + 40 hours each Dr. Dixon, Stachura, PI
- Ground testing (5 major subsystems): 100 hours technician + 90 hours engineering staff
- PNG testing evaluation: Aircraft analysis (20 hours each Dr. Dixon & PI); sensor data (20 hours each Dr. Diaz & Wardell)
- Design review/modifications: 60 hours (20 hours each for Dr. Dixon, Stachura, PI)
- SLV testing evaluation: Aircraft (20 hours each Dr. Dixon & PI); sensors (20 hours Dr. Diaz + 10 hours Dr. Wardell)
- 2nd XT acquisition: 80 hours (40 hours Dr. Dixon + 20 hours each Dr. Stachura & PI)
- Design-for-Manufacturability (DFM): 142 hours (110 hours Dr. Stachura & Dixon + 32 hours PI)

**4.0 Multi-Hole Probe Development** (280+ hours total)
- Design wind measurement requirements: 8 hours PI
- Wind tunnel testing of MHP: 28 hours (8 hours PI + 20 hours technician at CU facility)
- Mechanical integration into nose cone: 16 hours Dr. Stachura
- Wind tunnel testing of nose cone assembly: 48 hours (8 hours PI + 40 hours technician)
- Design updates based on testing: 60 hours (40 hours Dr