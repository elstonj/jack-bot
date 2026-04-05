# Black Swift S0 Platform Specifications for NOAA

## Document Metadata
- **Type:** Specifications document / Requirements specification
- **Client/Agency:** National Oceanic and Atmospheric Administration (NOAA), Department of Commerce, Office of Marine and Aviation Operations (OMAO), Aircraft Operations Center (AOC)
- **Program/Solicitation:** NOAA 2026 IDIQ (Indefinite Delivery/Indefinite Quantity) contract for TC Operations 2026-2030; builds on SBIR Phase I (1305M218CNRMW0059) and Phase II (1305M219CNRMW0030)
- **Date:** Document created/modified December 16, 2025
- **BST Products/Systems Referenced:** Black Swift S0 sUAS platform; SwiftCore Flight Management System; SwiftPilot; SwiftTab; AVAPS (Airborne Vertical Atmospheric Profiling System)
- **Key Personnel:** Beck Cotter (last editor)

## Executive Summary
This specifications document establishes requirements for NOAA's procurement and operational use of Black Swift's S0 Small Uncrewed Aircraft System (sUAS) for tropical cyclone (TC) operations from 2026-2030. The S0 is the only air-launched sUAS platform compatible with NOAA's WP-3D Hurricane Hunter aircraft, capable of collecting critical atmospheric measurements in extreme TC environments near the air-sea boundary where manned aircraft cannot safely operate.

## Technical Approach

### System Overview
The Black Swift S0 is designed for deployment from the NOAA WP-3D aircraft to collect measurements in tropical cyclone conditions. The platform has been operational since at least 2018 under SBIR funding and represents the only sUAS to achieve NOAA Readiness Level 7/8.

### Key Technical Requirements

**Aircraft Performance Specifications:**
- Minimum endurance: 100 minutes
- Lightweight airframe design
- Long-range communication: minimum +150 nautical miles (nm) in TC conditions (currently demonstrated >200 nm)
- Proven communication range enabling regular operational missions during TC taskings
- Robust, durable, mission-reliable design for TC operations
- Simple, intuitive user interfaces for scientific operators
- Streaming video capability for outreach

**Sensor/Payload Capabilities:**
- Minimum in situ atmospheric measurements: pressure, temperature, humidity, 2D winds
- Future capability evolution: 3D winds, surface temperature, wave height
- Modular payload bay for rapid sensor suite switching (air quality monitoring, trace gas detection, EO/IR cameras)
- Data quality equal to or greater than existing NRD41 dropsonde technology
- Accurate, real-time data transmission to WP-3D in TC conditions

**Autonomy & Control:**
- SwiftCore Flight Management System with pre-canned flight modules (pre-programmed autonomous flight patterns)
- Custom wind estimation algorithms for 3D wind profile capture
- Automated sampling patterns and mission scripting enabling "launch-and-forget" operations
- User interface and flight planning software for mission design and real-time telemetry monitoring

**Data Transmission:**
- AVAPS (Airborne Vertical Atmospheric Profiling System) integration
- High-Density Observation Bulletin (HDOB) and IWG formatted data transmission
- Real-time situational awareness data backhaul to WP-3D
- Demonstrated transmission to National Hurricane Center

**Reliability Requirements:**
- 85% mission success rate and reliability target through year-round testing
- Performance validation, safety assurance, and compliance documentation within 5 calendar days of each mission

### Weather Hardening & Integration
- Ruggedized platform optimized for tube-launch deployment mechanism from WP-3D
- Payload integration and tuning for high-fidelity data collection in turbulent TC environments
- Integration and testing of compatibility with WP-3D systems

## Products & Capabilities Described

### Black Swift S0 Platform
- **What it is:** A small uncrewed aircraft system designed for air-launch from manned aircraft in extreme weather environments
- **Proposed use:** Deployment from NOAA WP-3D Hurricane Hunter to collect atmospheric measurements near the air-sea boundary in tropical cyclones
- **Unique capability:** Only sUAS platform compatible with WP-3D; only platform to reach NOAA Readiness Level 7/8; demonstrated reliable deployment with >7 years of operational flights into hurricanes
- **Specifications:** 100+ minute endurance, >150 nm communication range, pressure/temperature/humidity/wind measurements, modular payloads

### SwiftCore Flight Management System
- Pre-canned autonomous flight modules for rapid mission deployment
- Mission scripting for complex meteorological operations
- Integration with NOAA's Advanced Weather Processing System (AWIPS)
- Development of standard operational flight patterns

### Ground Support Equipment (GSE)
- User interface and flight planning software
- Radio modem and communications link (1U rack-mounted unit)
- Chargers, cables, protective cases for TC deployment support
- Operational and maintenance documentation

### AVAPS Integration
- System for generating HDOB and IWG formatted data
- Situational awareness data transmission to WP-3D
- Long-range backhaul of science data
- Real-time data delivery to National Hurricane Center

## Use Cases & Applications

### Primary Use Case: Tropical Cyclone Operations
- **Mission Profile:** Launch from NOAA WP-3D Hurricane Hunter aircraft into active tropical cyclones during hurricane season (June 1 - November 30)
- **Data Collection Zone:** Near air-sea boundary where energy and momentum exchange occurs; altitudes below 500m where severe winds directly impact lives and property
- **Operational Context:** Provides critical measurements from dangerous low-level, high-wind TC environments inaccessible to manned aircraft or other platforms
- **Data Use:** Real-time transmission to forecasters for situational awareness and assimilation into operational TC forecast models; support for National Hurricane Center operations

### Secondary Applications (Mentioned as Future Capability)
- Air quality monitoring
- Trace gas detection (e.g., methane)
- EO/IR imaging for surface analysis

### Integration with Operational Systems
- Advanced Weather Processing System (AWIPS) integration at National Hurricane Center
- Environmental Modeling Center (EMC) retroactive impact studies and Observing System Experiments (OSE)
- Operational weather model assimilation (parallel runs, data denial experiments)
- Forecaster workflow integration at Atlantic Oceanographic & Meteorological Laboratory (AOML) and Hurricane Research Division (HRD)

## Key Results/Achievements

### Historical Performance
- 7+ years of successful operational deployment from WP-3D into active hurricanes
- Demonstrated communication range exceeding 200 nautical miles
- Proven Tier 1 Validated Earth Observation Data capability
- Only sUAS to achieve NOAA Readiness Level 7/8 for TC operations
- Successfully collecting and transmitting High-Density Observation Bulletin data to National Hurricane Center
- Platform is the only one pursued by NOAA for TC operations to reach operational reliability standards

### Regulatory/Compliance Status
- Compliant with Federal Regulations and NOAA policies
- SBIR Phase I (2018) and Phase II (2019-2020) successfully completed
- Ready for transition to SBIR Phase III
- Candidate for operationalization by 2027

## Notable Details

### Performance Targets for IDIQ Period
- Achieve "routinely operational" status (TRL9) within 6 months of award
- Maintain 85% mission success rate in TC environment
- Complete finalized end-to-end product (TRL8) with all system documentation, operational/maintenance training, and NOAA acceptance within 6 months

### Required Deliverables
1. **Aircraft:** Deployable Black Swift S0 platforms for 2026-2030 operations
2. **Personnel:** Qualified operators and observers deployable on short notice for hurricane season missions
3. **Engineering Support:** Non-recurring engineering (NRE) for payload integration, weather hardening, and algorithm development; software updates for NOAA TC operational workflow integration
4. **Training:** Operator/Observer and Instructor certification courses
5. **Pre-Canned Flight Modules:** Standardized autonomous mission patterns integrated into SwiftCore
6. **Documentation:** Technical documentation for operational use, integration, long-term sustainment (without disclosing proprietary source code)
7. **Data Services:** AVAPS system for real-time HDOB/IWG data formatting and transmission
8. **Modeling Support:** Participation in EMC retroactive impact studies using 2023-2026 drone data
9. **NHC Integration:** Support for AWIPS integration, data formatting, product visualization, flight planning, forecaster training

### Intellectual Property & Sustainment Framework
- **NOAA Rights:** Government Purpose Rights (GPR) per FAR 52.227-14 Alternate IV and SBIR Data Rights (FAR 52.227-20) for use, reproduction, and modification internally and through approved vendors for sustainment
- **BST Retains:** Full ownership of proprietary software (SwiftCore, SwiftPilot, SwiftTab), source code, algorithms, communication protocols, avionics designs, production processes
- **Data Escrow:** BST maintains escrow of design baselines, production documentation, and key interface specifications accessible to NOAA only if BST ceases operations or cannot fulfill IDIQ
- **Right of First Refusal:** BST offers NOAA first refusal for future production, upgrades, and sustainment services
- **Annual Reviews:** NOAA and BST to meet annually to align production forecasts, configuration changes, and sustainment plans

### Operational Integration Requirements
- Provide personnel support to all UASD (Uncrewed Aircraft Systems Division) planning meetings
- Conduct pre-planning, execution, and post-operation debriefings
- Maintain mission documentation and lessons learned accessible to Government
- Provide risk management program documentation
- Travel support for operational missions and clear-air test flights
- Collaboration with Atlantic Oceanographic & Meteorological Laboratory, Hurricane Research Division, and Cooperative Institute for Research in the Atmosphere

### Competitive Context
Specification emphasizes that S0 is "the only platform" among all sUAS pursued by NOAA to achieve operational readiness for TC missions, distinguishing it from other attempted systems that did not reach comparable capability or reliability levels.