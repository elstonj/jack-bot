# Black Swift S0 Platform Specifications for NOAA

## Document Metadata
- **Type:** Technical specifications/procurement requirements document
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration), Department of Commerce, Office of Marine and Aviation Operations, Aircraft Operations Center (AOC)
- **Program/Solicitation:** NOAA 2026 IDIQ (Indefinite Delivery/Indefinite Quantity); builds on prior SBIR Phase I (1305M218CNRMW0059) and Phase II (1305M219CNRMW0030)
- **Date:** 17 November 2025
- **BST Products/Systems Referenced:** Black Swift S0 (sUAS platform), SwiftCore™ Flight Management System, SwiftTab™ (user interface/flight planning software), SwiftStation™ (ground station), SwiftPilot™, AVAPS™ (Airborne Vertical Atmospheric Profiling System)
- **Key Personnel:** Jack Elston (last editor)

## Executive Summary
This document specifies NOAA's requirements for procurement and operational deployment of the Black Swift S0 small uncrewed aircraft system from 2026–2030 for tropical cyclone (TC) data collection. The S0, previously developed under SBIR Phases I and II, is the only sUAS platform that has achieved NOAA Readiness Level 7/8 and demonstrated reliable deployment from NOAA's WP-3D Hurricane Hunter aircraft. The contract covers platform procurement, ground support equipment, personnel support, non-recurring engineering, training, and integration into operational tropical cyclone forecasting workflows.

## Technical Approach

**Platform Design & Performance:**
- Lightweight airframe with minimum endurance of 100 minutes
- Designed for air-launch from NOAA WP-3D manned aircraft into tropical cyclone conditions
- Robust, durable, mission-reliable design with simple, intuitive user interfaces for scientific operators
- Streaming video capability for outreach
- Designed to operate near the air-sea boundary where detailed atmospheric measurements below 500 m altitude are critically needed but extremely difficult to obtain

**Sensor Suite & Data Collection:**
- Highly accurate in situ atmospheric measurements:
  - Pressure, temperature, humidity, two-dimensional winds (minimum)
  - Future capability: three-dimensional winds, surface temperature, wave height
- Data quality equal to or greater than NRD41 dropsonde technology
- Real-time data transmission to WP-3D in TC conditions
- Data output via AVAPS system for long-range backhaul to National Hurricane Center

**Communication & Range:**
- Minimum communication range of +150 nautical miles (nm) in TC conditions
- Proven communication range exceeding 200 nm
- Accurate, real-time data transmission to WP-3D in high-wind environments

**Flight Management & Autonomy:**
- SwiftCore Flight Management System enables:
  - Pre-canned flight modules (pre-programmed autonomous flight patterns)
  - "Launch-and-forget" autonomous operations
  - Rapid execution of standardized missions with minimal operator input
  - Custom wind estimation algorithms for 3D wind profile capture
  - Automated sampling patterns and mission scripting
- SwiftTab user interface for flight planning and real-time mission monitoring
- Optional manual control handset (not primary mode)

**System Integration:**
- Platform deployment mechanism optimized for tube-launch from WP-3D
- Modular payload bay for rapid sensor suite switching (meteorological sensors, air quality/trace gas detection, lightweight EO/IR cameras)
- Integration with NOAA's Advanced Weather Processing System (AWIPS)
- Tier 1 Validated Earth Observation Data capability

## Products & Capabilities Described

### Black Swift S0 Platform
- **What it is:** A small uncrewed aircraft system specifically designed for air-launch deployment from manned aircraft into tropical cyclone environments
- **Proposed use:** Primary deployment from NOAA WP-3D Hurricane Hunter aircraft to collect critical meteorological measurements in the low-level, high-wind environments near the air-sea boundary during tropical cyclones
- **Specifications:**
  - Minimum 100-minute endurance
  - Minimum +150 nm communication range in TC conditions (demonstrated 200+ nm capability)
  - Lightweight airframe suitable for air-launch
  - Pressure, temperature, humidity, wind measurement capability with upgradeable sensor suite
  - Real-time data transmission capability
  - NOAA Readiness Level 7/8 (only sUAS to achieve this for TC operations)
  - 85% target mission success rate in TC operations
  - Tier 1 Validated Earth Observation Data capability

### SwiftCore™ Flight Management System
- **What it is:** Autonomous flight management and mission planning software
- **Capabilities:** Pre-canned flight modules, automated sampling patterns, mission scripting, wind estimation algorithms, autonomous navigation
- **Use in contract:** Enables rapid deployment of standardized TC measurement missions with minimal operator intervention

### SwiftTab™ User Interface & Flight Planning Software
- **What it is:** Ground-based software for flight planning and mission monitoring
- **Capabilities:** Design and upload flight plans (including advanced sampling patterns and high-level mission scripting), monitor missions in real-time, receive live telemetry
- **Use:** Primary interface for operators during TC missions

### SwiftStation™ Ground Station Equipment
- **What it is:** Portable ground control and communications unit
- **Capabilities:** Maintains control and data link with sUAS; contains radio modem and communications link
- **Form factor:** Compact, highly portable, tripod-mountable
- **Use:** Central hub for sUAS command and telemetry during operations

### AVAPS™ (Airborne Vertical Atmospheric Profiling System)
- **What it is:** Data transmission and formatting system
- **Use:** Enables Black Swift S0 to generate formatted data transmission to NOAA WP-3D for long-range backhaul of science data to National Hurricane Center

### SwiftPilot™
- **Referenced as:** Proprietary software (source code retained by BST)
- **Details:** Minimal information provided; noted as proprietary IP retained by Black Swift

## Use Cases & Applications

**Primary Mission:** Tropical Cyclone (Hurricane) Operations
- Deploy from NOAA WP-3D manned aircraft during hurricane season (June 1 – November 30)
- Collect measurements near air-sea boundary where energy and momentum exchange with sea occurs
- Provide critical data in areas where manned aircraft cannot safely collect detailed observations below 500 m altitude
- Data supports:
  - Real-time forecaster situational awareness
  - Assimilation into operational TC forecast models
  - Validation of forecast accuracy through retroactive impact studies (data denial, Observing System Experiments)
  - Emergency manager and decision-maker response planning

**Secondary Applications (Future Capability):**
- Air quality monitoring missions
- Trace gas detection missions
- Lightweight EO/IR imaging missions
- Clear air and test flights

**Geographic/Environmental Context:**
- Tropical cyclone conditions with severe winds and turbulent environments
- Low-altitude, high-wind regions (below 500 m)
- Over-water operations at sea-air boundary

## Key Results (if applicable)
This is a forward-looking specifications/requirements document rather than a results report. However, it documents historical achievements:
- **Operational History:** Successfully flying into TC conditions since 2018; "over seven years" of successful operational deployments from WP-3D into multiple hurricanes
- **Development Milestones:** Completed SBIR Phase I and Phase II; achieved NOAA Readiness Level 7/8 (only sUAS to reach this level for TC operations)
- **Data Achievement:** High-Density Observation Bulletin capability enabling real-time data transmission to National Hurricane Center
- **Performance Validation:** Communication range exceeding 200 nm in operational TC environment; data quality meeting or exceeding dropsonde standards

## Notable Details

**Competitive Position:**
- Black Swift S0 is explicitly stated as "the only platform compatible with the WP-3D" and "the only platform that has reached a NOAA Readiness level of 7/8"
- Only sUAS to demonstrate reliable deployment from WP-3D, reliable flight duration/range, Tier 1 Earth Observation Data capability, and communication range exceeding 150 nm in TC conditions
- All other NOAA-pursued sUAS for TC operations have not reached operational readiness

**NOAA Investment & Institutional Commitment:**
- NOAA has invested substantially in infrastructure for routine WP-3D operations (control hardware, operator training, integration with forecasting workflows)
- SBIR Phase I and II developed design improvements, sensor integration, and WP-3D compatibility features
- Critical to NOAA mission: data collection capability unavailable through other means

**Operational Requirements (2026–2030):**
1. **Platform Procurement:** Delivery of S0 aircraft and GSE for 5-year period
2. **Operational Support:** Personnel (operators/observers) available for 6-month hurricane season deployment on WP-3D
3. **Personnel Training:** Development and delivery of Operator/Observer and Instructor training courses
4. **Non-Recurring Engineering:** 
   - Payload integration and modular payload bay design
   - Weather hardening and tube-launch optimization
   - Algorithm development (3D wind estimation, automated sampling patterns)
   - Real-time situational visualization tools
5. **System Integration:** NHC operational workflow integration with AWIPS, forecaster training
6. **Testing & Validation:** 85% mission success rate requirement; year-round testing with access to specialized partner ranges and federal wind tunnel facilities
7. **Operational Timeline:** Within 6 months of contract award, must achieve TRL8 (demonstration in operational TC environment) and TRL9 (routinely operational, 85% success rate, full system documentation, training complete)

**Intellectual Property Framework:**
- NOAA receives Government Purpose Rights (FAR 52.227-14 Alternate IV, SBIR Data Rights per FAR 52.227-20)
- NOAA can use, reproduce, modify internally; support sustainment through approved vendors
- NOAA **cannot** reproduce/manufacture additional S0 aircraft or derivative systems without BST written consent
- Black Swift retains proprietary ownership of:
  - SwiftCore™, SwiftPilot™, SwiftTab™ (source code)
  - Algorithms, communication protocols, avionics designs, production processes
- Data escrow mechanism established: if BST ceases operations, NOAA gains access to configuration baselines and production documentation under Government Purpose Rights (sustainment/re-competition only)
- BST offers right of first refusal for future production, upgrades, and sustainment

**Collaborative Framework:**
- Annual review meetings planned to align production forecasts, configuration changes, sustainment plans
- Shared goal: sustain tropical cyclone sUAS operations long-term
- Balances competitive fairness with IP protection

**Data Reporting Requirements:**
Black Swift must provide performance data within 5 calendar days of each mission covering:
- **Mission & Payload Data:** Scientific payload data, geospatial data
- **Aircraft Performance Data:** Full flight path, trajectory, speeds, endurance, climb/descent rates
- **System Health & Reliability:** Performance metrics
- **Test & Compliance Data:** Test criteria verification, data management assurance, weather/environment conditions
- Maintain Lessons Learned and Risk Management Program database accessible to NOAA

**Training Development:**
- Operator and Observer course defining safety and operational standards
- Instructor training course to support NOAA's goal of full S0 operational capability by 2027
- All courses subject to Program Office approval and task order modifications

**Equipment Delivery:**
- SwiftTab user interface software (flight planning, monitoring, telemetry)
- SwiftStation ground station (radio modem, communications link, portable deployment)
- Control handset (optional; S0 designed for autonomous operation)
- Standard deployment support: chargers, cables, protective cases
- AVAPS-enabled data transmission system
- Spares as approved by Government

**NHC Integration Focus:**
Close collaboration required with:
- Atlantic Oceanographic & Meteorological Laboratory (AOML)
- Hurricane Research Division (HRD)
- Cooperative Institute for Research in the Atmosphere (CIRA)
- Environmental Modeling Center (EMC) for retroactive impact studies and operational model assimilation

---

## Document Quality Note
This is a detailed, substantive procurement specification document with clear technical requirements, historical context, and operational framework. While containing footnotes indicating minor internal questions about success rate definition and timeline feasibility, the document is comprehensive and suitable for contract execution. The specifications are specific, measurable, and grounded in demonstrated operational history.