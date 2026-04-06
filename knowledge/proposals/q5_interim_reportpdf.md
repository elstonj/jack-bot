# A Ruggedized UAS for Scientific Data Gathering in Harsh Environments – Phase II-E Interim Report

## Document Metadata
- **Type:** NASA SBIR Phase II-E Interim Report
- **Client/Agency:** NASA (Jet Propulsion Laboratory)
- **Program/Solicitation:** NASA SBIR; Contract Number NNX17CP13C
- **Date:** December 2020
- **BST Products/Systems Referenced:** S2 XT (fixed-wing UAS), VTOL S2 XT (proposed variant), SwiftCore Flight Management System, SwiftPilot autopilot, SwiftTab user interface, multi-hole probe (MHP) sensor
- **Key Personnel:** Jack Elston (PI), Maciej Stachura (Lead Engineer)

## Executive Summary
Black Swift Technologies proposed to extend the S2 XT volcanic sampling UAS by adding vertical takeoff and landing (VTOL) capability while maintaining high-wind operability, addressing a critical gap in volcanic monitoring platforms. This Phase II-E work focused on developing a hybrid VTOL/fixed-wing control system capable of landing in winds >30 mph (where comparable commercial systems fail), integrating real-time data visualization, and conducting a flight campaign to Makushin Volcano in Alaska to validate operational performance.

## Technical Approach
The project pursued four concurrent technical objectives:

1. **VTOL S2 XT Airframe Design:** Added four rotors to the existing fixed-wing S2 XT platform while maintaining the ability to operate in volcanic ash and precipitation. Key design constraints included:
   - Maintaining approximately 1 hour endurance
   - Minimizing weight by eliminating catapult launch and belly-landing systems
   - Ensuring compatibility with existing payload systems
   - Designing for field deployment (airline-transportable carrying case)
   - Implementing water/dust-proof electrical connectors using CAN protocol for rotor control

2. **High-Wind VTOL Algorithm:** Developed a hybrid control system that combined rotor thrust with fixed-wing aerodynamic surfaces (ailerons, elevator) during landing. This unique approach:
   - Maintains sufficient vertical descent rate to keep airflow over control surfaces effective
   - Uses the low-cost multi-hole probe instrument to keep aircraft pointed into wind
   - Provides control authority during high-wind conditions (target: >30 mph)
   - Represents significant competitive advantage over existing VTOL fixed-wing aircraft (typically limited to <15 mph)

3. **Real-Time Data Visualization:** Development of open-source, modular ground-based software for displaying sensor telemetry in real-time, enabling scientists to redirect aircraft during missions based on measurements. Integration leveraged existing SwiftTab tablet interface and telemetry systems.

4. **Scientific Flight Campaign:** Validation flight campaign planned for Makushin Volcano, Alaska (backup: Hawaii), with operational goals of demonstrating launch/recovery from a 20' × 20' area in winds up to 30 mph.

## Products & Capabilities Described

### S2 XT (Original Fixed-Wing Platform)
- **What it is:** Ruggedized fixed-wing UAS designed for harsh environment scientific sampling, specifically volcanic plume observation
- **Specifications:** ~1 hour endurance, capable of carrying scientific payloads including mass spectrometers and atmospheric sensors
- **Design features:** Belly-landing capability, catapult launch, wings with automatic electrical connectors, robust construction for operation in volcanic ash and precipitation
- **Proven deployments:** ELEVATE campaign (Costa Rica), Phase II operations in Colorado

### VTOL S2 XT (Proposed Variant)
- **What it is:** Modified S2 XT with four VTOL rotors enabling vertical takeoff/landing without requiring launch infrastructure
- **Key design elements:**
  - Four rotors (sizing and placement to be validated through prototype testing)
  - 50% larger battery than original S2 to support hover power requirements
  - Hybrid control during landing combining rotor and fixed-wing surfaces
  - Multi-hole probe sensor for wind-relative heading measurement
  - Modular payload bay for scientific instruments
  - Maintained volcanic plume operability (ash/precipitation tolerance)
- **Performance targets:** 1-hour endurance, landing capability in >30 mph winds with volcanic sampling payload
- **Advantage over alternatives:** No comparable VTOL fixed-wing aircraft on market capable of operating in these wind conditions with comparable payloads

### SwiftCore Flight Management System
- **Function:** Aircraft autopilot and control system managing VTOL transitions, hybrid landing algorithms, and sensor integration
- **VTOL-specific upgrades:** New autonomous transition algorithms and control laws for high-wind operations
- **Protocol:** CAN bus for rotor control and sensor integration

### SwiftPilot Autopilot
- **Role:** Low-level flight control implementing hybrid VTOL/fixed-wing landing algorithm
- **Updates:** Implementation of new high-wind landing control laws

### SwiftTab User Interface
- **Function:** Tablet-based mission planning and real-time vehicle command/control
- **VTOL-specific updates:** New command/control capabilities for VTOL operations, integration of real-time sensor data display

### Multi-Hole Probe (MHP) Sensor
- **What it is:** Low-cost atmospheric probe measuring wind speed/direction
- **Application in VTOL:** Provides wind-relative aircraft heading to orient aircraft into wind during landing, enabling hybrid control algorithm
- **Commercial applications noted:** Also applicable to NOAA's Coyote UAS for hurricane wind measurements (noted as higher accuracy than Piccolo autopilot)

## Use Cases & Applications

### Volcanic Monitoring (Primary Focus)
- **Makushin Volcano, Alaska:** Primary flight campaign target; one of Alaska's most active volcanoes
- **Turrialba Volcano, Costa Rica:** Previous operations during Phase II and ELEVATE campaign
- **Measurement objectives:** Volcanic plume characterization, ash sampling, gas chemistry
- **Key advantage:** VTOL enables access to remote/difficult volcanic sites without requiring prepared landing areas

### NASA Missions Identified as Potential Customers
- **Tropospheric Chemistry Program (TCP):** Atmospheric chemistry measurements
- **CALIPSO/CATS missions:** Cloud-aerosol observations
- **MALIBU project (GSFC):** Landsat calibration at difficult mountain sites
- **SoOp (JPL):** Snow water equivalent measurements in Colorado mountains
- **Earth Ventures Program:** Airborne field campaigns

### Non-NASA Government Applications
- **USGS Volcano Monitoring:** Primary matching-fund partner; providing Alaska operations funding
- **NOAA:**
  - **NightFOX project:** Wildfire measurements for FIREX mission and fire weather forecasting (CO₂, aerosol, plume measurements)
  - **Coyote UAS hurricane operations:** Potential wind measurement improvements via MHP sensor integration
- **DOE:** Potential atmospheric monitoring applications
- **National Weather Service:** Air quality and hazard monitoring

### Commercial/Scientific Applications
- **Wildfire Monitoring:** Sampling of particulates and severe turbulence environments
- **Atmospheric Dispersion Modeling:** Data collection for model validation (volcanic ash, pollution, dust storms, smoke)
- **Multi-hole Probe Sensor:** Commercial market for standalone atmospheric measurement
- **Sensor Integration:** Platform enabling rapid sensor swaps for different mission types

## Key Results (Interim Report Status)

### Completed Milestones (as of December 2020)
- VTOL S2 prototype constructed and test-flown; motor/propeller selection and hover control algorithms validated
- Production VTOL S2 design underway; new wings designed, molds constructed, first-article parts produced
- Autonomous transition control algorithm framework completed; supporting logic and communications implemented
- Makushin payload sensors selected, CAD-modeled, and integrated into payload bay
- Makushin payload firmware completed and bench-tested
- AFSRB (Airworthiness and Flight Safety Review Board) completed; virtual site visit in progress
- Certificate of Authorization (COA) submission site access granted; COA constructed
- BVLOS (Beyond Visual Line of Sight) waiver under construction
- Alaska operations site land owner permission secured; data connectivity arrangements with local provider initiated
- Comprehensive permissions contact list compiled
- ADS-B receiver purchased; firmware developed for SwiftCore integration; ground display software created
- Iridium modem procurement completed; PCB designed for aircraft and ground station integration

### Project Status
- **Physical completion:** 85%
- **Amount expended:** $153,410
- **Schedule:** No-cost extension obtained through September 30, 2021 (originally constrained by COVID-19 quarantine preventing Dutch Harbor operations in 2020; extension allows deployment readiness by June 2021)

## Notable Details

### Matching Funds & Partnerships
- **USGS:** Primary non-NASA partner providing matching funds for Alaska Makushin campaign ($X amount unspecified)
- **Creare:** Matching funds for VTOL SwiftCore algorithm development; their aircraft designed for NOAA ship-based operations (complements high-wind capability)
- **JPL:** Technical monitor and customer; ELEVATE campaign partnership

### Competitive/Commercial Positioning
- **Market gap addressed:** No existing VTOL fixed-wing aircraft can land in >30 mph winds with volcanic sampling payloads
- **Commercialization goal:** Phase II-E designed to produce "commercially ready platform" with finalized manufacturing processes and QC documentation
- **Target markets:** Government agencies (NASA, USGS, NOAA, DOE), commercial atmospheric science, sensor manufacturers
- **Prior commercial success:** S2 XT successfully deployed; MHP sensor in use for multiple campaigns

### Operational Uniqueness
- **Launch infrastructure elimination:** VTOL removes dependency on catapult launchers and prepared landing areas, enabling operations at remote/difficult sites
- **Data-directed missions:** Real-time sensor display enables scientists to adaptively direct aircraft to maximize scientific return
- **Hybrid algorithm innovation:** Combination of rotor and fixed-wing control surfaces for high-wind operation represents novel technical approach

### Technical Risks & Mitigation
- **COVID-19 impact:** Quarantine restrictions prevented 2020 Alaska deployment; mitigated through no-cost extension
- **Backup plan:** If Makushin permitting delayed, flight campaign planned for Hawaii (existing flight permissions from Phase II)

### Specific Technical Constraints
- **Endurance target:** Maintained at ~1 hour despite 50% battery size increase (weight optimization critical)
- **Payload compatibility:** New VTOL system designed to carry same volcanic sampling instruments as Phase II fixed-wing variant
- **Field operability:** Aircraft and supporting equipment must remain airline-transportable (carried case constraint maintained)
- **Environmental tolerance:** VTOL system must operate in volcanic ash and precipitation (unlike most VTOL aircraft)