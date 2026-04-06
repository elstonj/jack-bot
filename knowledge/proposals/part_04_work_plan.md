# NASA 2016 SBIR Phase II: Volcano Monitoring with SuperSwift XT

## Document Metadata
- **Type:** SBIR Phase II Work Plan
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA 2016 SBIR Phase II
- **Date:** December 2016 (created Dec 2, 2009; modified Dec 9, 2016)
- **BST Products/Systems Referenced:** SuperSwift XT (sUAS), SwiftCore FMS, SwiftPilot, SwiftTab, Multi-Hole Probe (MHP), Pitot-Static Tube (PTH)
- **Key Personnel:** 
  - PI (Principal Investigator - not named)
  - Dr. Maciej Stachura (Design/Engineering)
  - Dr. Dixon (Aircraft Design/Autopilot)
  - Dr. Diaz (Volcanology/Field Operations)
  - Dr. Wardell (Sensor/Data Analysis)

## Executive Summary
This 24-month Phase II work plan details development and field validation of the SuperSwift XT small unmanned aircraft system (sUAS) equipped with a scientific sensor payload for volcanic plume observation. The project culminates in deployment to Turrialba Volcano in Costa Rica to collect in-situ atmospheric data from volcanic emissions, with progression through ground testing, high-altitude validation flights, and full system integration.

## Technical Approach

### Project Structure (8 Quarters, 24 months)
- **Q1:** Design finalization, FAA/NASA approvals, manufacturing begins
- **Q2:** First prototype ready, wind tunnel testing, PNG aerodynamic validation
- **Q3:** Sensor integration, lab validation, data analysis software development
- **Q4:** SwiftTab mission planning finalization, PNG sensor/mission testing
- **Q5:** High-altitude testing at San Luis Valley (14,000 ft), second aircraft ordered
- **Q6:** Second aircraft ready, end-to-end system validation, Costa Rica approvals
- **Q7:** Turrialba deployment and flight testing
- **Q8:** Final documentation and reporting

### Key Technical Tasks

**SuperSwift XT Aircraft Development (Section 3.0)**
- CAD model finalization in Solidworks with all integrated components
- Custom pitot-static tube design and validation
- Custom motor cowl for cooling and particulate protection
- IP 63 sealing verification for nose cone and hatches
- Two complete aircraft built and tested
- Design for Manufacturability (DFM) optimization for commercialization

**Multi-Hole Probe (MHP) Development (Section 4.0)**
- Wind tunnel testing to validate design accuracy
- Mechanical integration into modular nose cone
- CFD-informed sensor placement
- Inertial wind estimation combining MHP, SwiftPilot sensors, and state estimation algorithms
- Partnership with iMet to provide MHP as part of XF sensor suite
- Firmware development for XF expansion port interface

**Sensor Payload Integration (Section 5.0)**
- Acquisition and integration of selected science sensors
- Electrical and mechanical integration into modular nose cone
- Real-time data logging with system time tagging and autopilot telemetry
- Lab calibration and validation
- Development of data processing software and data management plan

**User Interface and Mission Planning (Section 6.0)**
- Five candidate flight patterns for volcanic plume observation
- SwiftTab tablet-based UI with gesture controls
- Automated mission planning capabilities
- Volcano plume observation mission plan catalog
- Communications protocol for mission transmission to aircraft
- Control system updates for mission plan execution
- Autopilot firmware modifications
- Software-in-the-loop validation
- Language design for custom mission plan generation

## Products & Capabilities Described

### SuperSwift XT
- **What it is:** Improved version of BST's SuperSwift sUAS with enhanced design for high-altitude operations
- **Proposed use:** Primary platform for volcanic plume observation and atmospheric profiling
- **Key specifications:**
  - Operating altitude: up to 14,000 ft (San Luis Valley testing)
  - Payload capacity sufficient for multi-sensor scientific package
  - Modular nose cone design for sensor integration
  - Improved motor cowl for environmental protection (airborne particulates)
  - IP 63 sealing rating for environmental robustness
- **Performance validation:** Empty aircraft performance, full payload performance, structural validation

### SwiftCore Flight Management System (FMS)
- **What it is:** BST's autopilot/flight management system
- **Proposed use:** Aircraft control and mission execution
- **Capabilities:** Pattern generation and execution, altitude and position hold, automated mission planning

### SwiftPilot
- **What it is:** Onboard autopilot sensors and state estimation algorithms
- **Proposed use:** Wind measurement integration; combines with MHP and state estimation for inertial wind calculation
- **Data:** Provides aircraft state telemetry time-synced to sensor data

### SwiftTab
- **What it is:** Tablet-based operator interface
- **Proposed use:** Mission planning and creation for volcanic plume observation
- **New capabilities being developed:** 
  - Gesture-based mission plan creation and modification
  - Automated volcanic plume observation mission planning
  - Custom mission plan language for scientists
  - Real-time operator control

### Multi-Hole Probe (MHP)
- **What it is:** Custom wind measurement instrument
- **Proposed use:** In-situ wind speed and direction measurement in volcanic plumes
- **Technical approach:**
  - Multiple pressure ports for wind vector determination
  - Wind tunnel validated design
  - Integrated into modular nose cone
  - CFD-optimized sensor placement accounting for fuselage effects
  - Combined with state estimation for inertial wind calculation
- **Commercialization:** Partnership with iMet for XF sensor suite integration

### Pitot-Static Tube (PTH)
- **What it is:** Custom airspeed measurement probe
- **Proposed use:** Aircraft airspeed validation and comparison with MHP
- **Performance validation:** Wind tunnel testing and verification

### Scientific Sensor Payload (unspecified in detail)
- **What it is:** Suite of trace gas, particulate, and meteorological sensors selected from Phase I trade study
- **Proposed use:** Volcanic plume composition and atmospheric characterization
- **Key sensors implied:** Nephelometer (particulates), pressure/humidity instruments, trace gas sensors
- **Data requirements:** Real-time logging with system time and autopilot telemetry synchronization

## Use Cases & Applications

### Primary Mission: Volcanic Plume Observation
- **Turrialba Volcano, Costa Rica** (primary deployment site)
  - In-situ atmospheric profiling of volcanic emissions
  - 15-day deployment window for weather contingency
  - Up to 100 hours flight team deployment time

- **Volcano National Park, Hawaii** (backup volcanic site)
  - Full system validation at alternative volcanic location
  - Demonstrates capabilities across different volcanic environments

### Supporting Test Locations

**Pawnee National Grasslands (PNG), Colorado**
- Phase: Q2-Q4
- Purpose: Aerodynamic validation (empty aircraft), sensor package validation, mission plan execution validation
- Conditions: Sparsely populated grassland; suitable for safe testing
- Duration: 2-day campaigns over 4-week windows (Q2 and Q4)

**San Luis Valley (SLV), Colorado**
- Phase: Q5-Q6
- Purpose: High-altitude and turbulent flight operations validation (14,000 ft ceiling)
- Conditions: Mountainous terrain similar to volcanic regions; simulates volcanic flight environment
- Duration: 2-day campaign over 4-week window
- Validates: Takeoff/landing on difficult terrain, high-altitude performance, turbulence handling, sensor payload in challenging conditions

### Meteorological Applications (Section 4.1)
- Multiple unspecified meteorological applications identified as benefiting from MHP wind measurement capability
- Wind measurement accuracy requirements determined for each application

## Key Results / Deliverables by Quarter

### Q1 Deliverables
- Requirements document (finalized)
- FAA and NASA flight approval paperwork (submitted)
- SuperSwift XT 3D CAD design (finalized)
- Payload sensors (ordered)
- Manufacturing initiated on XT components

### Q2 Deliverables
- Prototype SuperSwift XT with SwiftCore FMS (ready for flight)
- Wind tunnel verification of PTH (completed)
- PNG flight testing results for aerodynamic validation

### Q3 Deliverables
- Integrated sensor package (mechanically and electrically integrated)
- Lab and bench top sensor validation (completed)
- Data analysis software (development started)
- Updated SuperSwift XT design based on PNG results

### Q4 Deliverables
- SwiftTab operator interface with mission planning (finalized)
- PNG flight testing of integrated sensor package and mission planning (completed)
- In-flight sensor data analysis validating functional interfaces and data quality

### Q5 Deliverables
- High-altitude flight testing at SLV (completed)
- High-altitude in-flight sensor data analysis (completed)
- Second SuperSwift XT components (ordered and sent to manufacturing)

### Q6 Deliverables
- Second SuperSwift XT (ready for flight testing)
- End-to-end system flight testing (completed)
- Final verification and validation of flight data and performance
- NASA and Costa Rican flight approval documentation submitted for Turrialba

### Q7 Deliverables
- Turrialba Volcano (or backup site) deployment and flight testing (completed)
- Scientific volcanic plume data collection

### Q8 Deliverables
- Final Report to NASA
- Briefing Chart
- Summary Report
- NTSR (New Technology Summary Report)

## Notable Details

### Flight Certification Strategy
- **Pawnee National Grasslands:** AFSRB (Airworthiness and Flight Safety Review Board) and FRRB (Flight Risk Review Board) approval required; documents started in Phase I; FAA COA (Certificate of Airworthiness) issued after approval; monthly flight reports required
- **San Luis Valley:** Supplemental flight request (uses Pawnee approval as basis); new test plan and FAA COA required
- **Turrialba, Costa Rica:** Dual approval required—NASA AFSRB/FRRB AND Costa Rican authorities; Dr. Diaz brings expertise from previous Turrialba operations
- **Volcano National Park (backup):** Noted as difficult; BST holds distinction of being first company to receive National Park flight permission under new rules (summer 2016 Great Sand Dunes NP survey flights)

### Risk Management
- Phase I risks reviewed and mitigation strategies validated
- New risks identified and assessed
- Mission plan execution risks (terrain impact) identified and validation checks designed
- Software-in-the-loop validation to identify critical autopilot bugs before flight

### Design Optimization
- DFM (Design for Manufacturability) performed late in Phase II to minimize production costs
- CAD model includes all components for verification before manufacturing
- Long lead items identified early to prevent schedule conflicts
- Individual component testing and validation before integration

### Commercialization Focus
- iMet partnership for MHP integration into XF sensor suite (commercial product)
- Design reviews for manufacturability and commercial viability
- Custom mission plan language designed for non-expert scientist users
- Expandable mission plan framework for future custom applications

### Team Expertise
- **Dr. Stachura:** Aircraft design, CAD/Solidworks, flight safety coordination
- **Dr. Dixon:** Aircraft aerodynamic analysis, autopilot sensors and algorithms, UI/software implementation
- **Dr. Diaz:** Volcanology, volcanic flight environment knowledge, Costa Rican approvals expertise, field operations
- **Dr. Wardell:** Sensor integration, data analysis, science mission planning
- **PI:** Overall project management, requirements, design reviews, data logging integration, communications protocol, autopilot firmware

### Data Management and Analysis
- Real-time data logging with system time and autopilot telemetry synchronization
- Lab calibration and validation before flight
- Flight data analysis reports comparing sensors to known atmospheric conditions and ground truth
- Comparison of like sensors (MHP vs. pitot system, nephelometer readings vs. expected values)
- First-of-its-kind volcanic plume dataset collection as project objective

### Subcontractor Roles
- Two subcontractors engaged (names not provided in this excerpt)
- 4-day kickoff meeting at BST with all parties
- Shared requirements document maintained throughout project
- Contributions to design reviews and data analysis

---

**Note:** This work plan represents the detailed execution strategy for a NASA SBIR Phase II project. The document emphasizes a methodical progression from design finalization through component validation, system integration, ground/altitude testing, and culminating