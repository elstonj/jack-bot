# BLACK SWIFT S0 PLATFORM SPECIFICATIONS FOR NOAA

## Document Metadata
- **Type:** Specifications document / Contract requirements
- **Client/Agency:** National Oceanic and Atmospheric Administration (NOAA), Office of Marine and Aviation Operations, Aircraft Operations Center (AOC)
- **Program/Solicitation:** NOAA 2026 IDIQ (Indefinite Delivery/Indefinite Quantity) contract; references prior SBIR Phase I (1305M218CNRMW0059) and Phase II (1305M219CNRMW0030)
- **Date:** December 16, 2025 (document modified date)
- **BST Products/Systems Referenced:** Black Swift S0 (sUAS platform), SwiftCore Flight Management System, SwiftPilot, SwiftTab, AVAPS (Airborne Vertical Atmospheric Profiling System)
- **Key Personnel:** Beck Cotter (last editor)

## Executive Summary
This specification document outlines NOAA's requirements for Black Swift Technologies to supply S0 Small Uncrewed Aircraft Systems (sUAS) platforms and operational support for tropical cyclone (TC) monitoring operations from 2026-2030. The S0 is the only sUAS platform that has achieved NOAA Readiness Level 7/8 and demonstrated reliable deployment from NOAA's WP-3D Hurricane Hunter aircraft for collecting critical low-altitude atmospheric measurements in TC environments.

## Technical Approach

**System Integration & Operations:**
- Air-launched deployment from NOAA WP-3D aircraft
- Real-time data transmission to WP-3D and National Hurricane Center
- Autonomous flight operations using SwiftCore Flight Management System
- Pre-programmed mission modules for standardized, rapid deployment

**Technology Development Areas:**
- Payload integration with modular sensor bay for rapid switching
- Weather hardening and ruggedization for TC deployment
- Custom 3D wind estimation algorithms
- Automated sampling patterns and mission scripting for "launch-and-forget" autonomous operations
- Integration with Advanced Weather Processing System (AWIPS) and forecaster workflows

## Products & Capabilities Described

### Black Swift S0 (sUAS Platform)
**What it is:**
- Small uncrewed aircraft system designed for tropical cyclone data collection
- Deployable from WP-3D Hurricane Hunter aircraft
- Only sUAS platform certified to NOAA Readiness Level 7/8
- Successfully operational for over 7 years in TC environments

**Specifications:**
- Lightweight airframe with minimum 100-minute endurance
- Long-range communication: minimum 150+ nautical miles (proven >200 nm in operations)
- Streaming video capability for outreach
- Accurate real-time transmission of data to WP-3D

**Sensors & Measurements:**
- Current: Pressure, temperature, humidity, 2D winds
- Future capability: 3D winds, surface temperature, wave height
- Data quality must equal or exceed NRD41 dropsonde technology currently in use
- Classified as Tier 1 Validated Earth Observation Data requirement

**Proposed Use:**
- Air-launched near air-sea boundary in TC low-level, high-wind environments
- Real-time data transmission to improve forecaster situational awareness
- Data assimilation into operational TC forecast models
- Collection of High-Density Observation Bulletins (HDOB) for National Hurricane Center

### SwiftCore Flight Management System
- User interface and flight planning software
- Design and upload of flight plans with advanced sampling patterns
- Mission scripting for autonomous operations
- Real-time telemetry monitoring

### SwiftPilot & SwiftTab
- Proprietary software systems (source code retained by BST)
- User-facing operational software

### AVAPS (Airborne Vertical Atmospheric Profiling System)
- Data generation system for HDOB and IWG formatted transmissions
- Long-range backhaul of science data and situational awareness

### Ground Support Equipment
- Radio modem and communications link (1U rack-mounted unit)
- User interface and flight planning software
- Standard support equipment: chargers, cables, protective cases

## Use Cases & Applications

**Primary Use Case: Tropical Cyclone Operations**
- Monitor energy and momentum exchange at air-sea boundary
- Collect measurements in TC low-level, high-wind environments where manned platforms cannot safely operate
- Support forecaster decision-making and emergency manager situational awareness
- Impact on lives and property protection for millions of Americans

**Operational Context:**
- Deployment season: June 1 – November 30 (hurricane season)
- Mission types: Hurricane intercepts, clear air test flights
- Stakeholders: NOAA forecasters, researchers, emergency managers, operational modeling centers

**Secondary Applications (Mentioned as Future Capability):**
- Air quality monitoring
- Trace gas detection
- Lightweight EO/IR camera payloads

## Key Results

**Historical Performance (7+ years operational):**
- Successfully deployed from WP-3D into multiple hurricanes
- Demonstrated reliable deployment, flight duration, and range
- Proven communication range >200 nautical miles in TC conditions
- Regular transmission of HDOB data to National Hurricane Center
- Only sUAS to reach NOAA Readiness Level 7/8

**Contract Performance Requirements:**
- 85% mission success rate and reliability through 2026-2030
- Must achieve TRL9 (operational) status within 6 months of contract award
- Data denial/Observing System Experiments (OSE) with 2023-2026 data showing positive modeling impact

## Notable Details

### Partnership & Infrastructure Investment
- NOAA has invested in infrastructure required for routine platform deployment on WP-3D
- 2018-2020 SBIR Phase I and Phase II development and testing
- Current effort transitions to SBIR Phase III
- Failure to acquire this capability inhibits NOAA's ability to meet critical research and operational requirements

### Intellectual Property & Continuity Framework
- **Government Purpose Rights:** NOAA receives rights to use, reproduce, and modify delivered data internally and support operational sustainment through approved vendors
- **Proprietary Protection:** BST retains full ownership of source code, algorithms, communication protocols, avionics designs, and production processes
- **Data Escrow:** BST maintains escrow of design baselines, production documentation, and interface specifications; accessible to NOAA only if BST ceases operations
- **Right of First Refusal:** BST continues to offer NOAA first refusal for future production, upgrades, and sustainment services
- **Annual Reviews:** Parties agree to meet annually to review production forecasts, configuration changes, and sustainment plans

### Training & Sustainment Requirements
- Operator and Observer training courses to meet safety standards
- Instructor training course for NOAA personnel
- All training must be approved by NOAA
- Personnel must maintain qualifications throughout hurricane season

### Non-Recurring Engineering Tasks
1. Payload integration and tuning for thermodynamic/kinematic measurements
2. Modular payload bay design for rapid sensor switching
3. Weather hardening and deployment mechanism optimization
4. 3D wind estimation algorithm development
5. Automated sampling patterns and mission scripting in SwiftCore

### Data Reporting Requirements
Upon completion of each mission (within 5 calendar days):
- **Mission & Payload Data:** Scientific payload and geospatial data
- **Aircraft Performance Data:** Flight path, trajectory, speeds, endurance, climb/descent rates
- **System Health & Reliability:** Performance metrics
- **Test & Compliance Data:** Test criteria verification, data management assurance, weather/environment conditions
- **Lessons Learned & Risk Management:** Ongoing documentation maintained and accessible to government

### Integration Partnerships
- Environmental Modeling Center (EMC) for retroactive impact studies and operational model integration
- Atlantic Oceanographic & Meteorological Laboratory (AOML), Hurricane Research Division (HRD)
- Cooperative Institute for Research in the Atmosphere (CIRA)
- National Hurricane Center (NHC) for AWIPS workflow integration and forecaster training

### Unique Competitive Position
The S0 is identified as "the only platform compatible with the WP-3D and meets NOAA Readiness Level 7/8" and "the only one that has reached a NOAA Readiness level of 7/8, demonstrated reliable deployment from the WP-3D, reliable flight duration and range, transmission of High-Density Observation Bulletin transfer to the National Hurricane Center, and a proven communication range over 200 nautical miles."