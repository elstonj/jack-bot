# NASA SBIR Phase II Proposal: SuperSwift XT Volcanic Profiling System

## Document Metadata
- **Type:** NASA SBIR Phase II Proposal (Part 02: Innovation & Phase I Results)
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA 2016 SBIR, Subtopic S3.04
- **Date:** December 2–9, 2016
- **BST Products/Systems Referenced:** SuperSwift XT, SuperSwift airframe, SwiftCore Flight Management System (FMS), SwiftPilot autopilot, SwiftTab operator interface, Multi-hole Probe (MHP)
- **Key Personnel:** Jack Elston (PI), Dr. Wardell (Science Lead), David Pieri (NASA Technical Monitor/JPL volcanologist), Dr. Jorge Andres Diaz (Phase II subcontractor)

## Executive Summary
Black Swift Technologies proposes developing the **SuperSwift XT**, a ruggedized small Unmanned Aircraft System (sUAS) purpose-built to measure volcanic ash and gas emissions at high altitudes and in harsh environments. Building on the proven SuperSwift airframe and SwiftCore FMS, the SuperSwift XT will carry an integrated sensor suite to collect in situ data that improves volcanic ash aviation hazard forecasting, advances volcano monitoring, and validates satellite remote sensing. Phase I established concept of operations, selected sensors, designed the airframe modifications, and completed NASA flight certification documentation.

## Technical Approach

### System Architecture
The SuperSwift XT integrates:
- **Airframe:** Modified SuperSwift with enhanced control surfaces (ailerons +29%, flaps +32%, ruddervators +59%), sealed inlets, improved pitot-static design, custom motor cowling
- **Avionics:** SwiftCore FMS with SwiftPilot autopilot (Linux-based payload computer, CAN bus interface, advanced GPS/GLONASS receiver with raw data logging, ~50cm real-time positional uncertainty)
- **Payload:** Removable modular nose cone with 8 sensors plus optional mass spectrometer

### Propulsion & Performance
- **Single Battery Configuration:** 6-cell 9,000 mAh HV LiPo (4.35V/cell); GTOW 13.7 lb; max flight time 70 min; climb angle 44° at 20 kft; thrust-to-weight >1.0 up to 8 kft density altitude
- **Dual Battery Configuration:** GTOW 15.5 lb; flight time >2 hours at 20 kft; climb angle 37°
- **Altitude Capability:** Sustained flight to 20 kft MSL with high thrust-to-weight for hand-launch and terrain-following
- **Motor Upgrade:** New high-thrust motor selected; thrust-to-weight ratio increased from 0.5 to 1.4 at sea level

### Aerodynamic & Mechanical Hardening
- Increased control surface authority for operations in high turbulence
- All access panel seals with gaskets to exclude ash/particulates
- Custom motor cowl with integrated cooling fins
- Larger pitot-static tube openings to reduce water droplet bridging
- Improved ingress protection on hatches and external component coverings
- Dual battery trays for field modularity

### Flight Planning & Autonomy
- SwiftPilot and SwiftTab to be enhanced in Phase II for **autonomous mission plan generation** based on intuitive parameters
- Plans to implement automatic flight pattern generation for five identified mission scenario types
- Low-altitude terrain-following capability in mountainous regions

## Products & Capabilities Described

### SuperSwift XT Airframe
- **What it is:** Hand-launchable, fixed-wing sUAS derived from the commercially-proven SuperSwift
- **Use in this context:** Primary platform for volcanic plume profiling; designed to operate at up to 20 kft MSL in high winds, turbulence, and corrosive ash environments
- **Key specs:** Max takeoff weight 13.7–15.5 lb (depending on battery config), endurance 70 min–2 hr, range up to 37 km, hand-launchable
- **Competitive advantages:** Higher ceiling and longer endurance than Dragon Eye; larger payload capacity and longer range than Vector Wing airframe; ruggedized for harsh environments

### SwiftCore Flight Management System (FMS)
- **What it is:** Integrated avionics platform consisting of SwiftPilot autopilot and SwiftTab operator interface
- **Use in this context:** Manages flight control, sensor data aggregation, autonomous mission execution, post-processing with accurate timing
- **Key specs:** CAN bus for modularity; Linux payload computer; GPS/GLONASS raw data logging; ~50cm real-time position accuracy; SDK for third-party sensor integration; data storage with autopilot telemetry tagging
- **Phase II enhancements:** Automatic generation of volcanic plume mission profiles; improved flight planning for scientific operations

### Volcanic Plume Sensor Suite (8 Primary Sensors)
1. **Trace Gas Sensor (iMET brand):** SO₂, CO₂, CH₄, H₂S measurements
2. **Nephelometer:** Particle concentration, velocity, sizing
3. **Atmospheric Thermodynamics:** Pressure, temperature, humidity
4. **3D Wind Sensor (BST Custom Multi-Hole Probe):** 
   - Novel design using 3D printing for case and pressure port positioning
   - Five pressure ports connected via flexible tubing to CAN port
   - Lighter weight and lower cost than existing commercial solutions (e.g., Aeroprobe)
   - Phase I wind tunnel validation: outperforms Aeroprobe in angle of attack (α) and sideslip angle (β) measurements across most angles
   - Can be modified for particulate resistance via shape changes
5. **Electro-Optical (EO) Camera:** Downward-looking imagery
6. **Thermal Camera:** Vent and thermal anomaly detection (downward-looking)
7. **Forward Video Camera:** Real-time piloting and documentation
8. **Ash Sampling System:** Physical sample collection

**Optional Payload:** Mass spectrometer in field-swappable nose cone

### Payload Integration
- **Removable modular payload system** enables rapid sensor suite changes without specialized tools
- **Mechanical, electrical, and data interface** designed and validated in Phase I
- **Nose cone redesign:** CFD validated for unobstructed airflow to atmospheric sensors
- **Weight/CG margins:** Verified through integration planning; all sensors fit within airframe constraints
- **Data architecture:** Consistent format with autopilot telemetry tagging for scientific post-processing

## Use Cases & Applications

### Primary Mission: Volcanic Plume Profiling
**Five Concept of Operations (CONOPS) mission profiles identified in Phase I:**

1. **Volumetric Sampling:** 
   - Max altitude: 19,300 ft MSL
   - Flight time: 75 min
   - Range: 10.4 km
   - Climb slope: 14°
   - Purpose: Comprehensive 3D plume characterization

2. **Cylindrical Profiling:**
   - Max altitude: 19,800 ft MSL
   - Flight time: 34 min
   - Range: 7.6 km
   - Climb slope: 14°
   - Purpose: Vertical cross-section plume measurements

3. **Long Distance Gradient:**
   - Max altitude: 19,300 ft MSL
   - Flight time: 74 min
   - Range: 37.3 km
   - Climb slope: 14°
   - Purpose: Downwind plume tracking and dispersion monitoring

4. **Vent Contouring:**
   - Max altitude: 17,850 ft MSL
   - Flight time: 14 min
   - Range: 7.4 km
   - Climb slope: 31°
   - Purpose: High-resolution near-source measurements

5. **Terrain Mapping:**
   - Max altitude: 14,500 ft MSL
   - Flight time: 90 min
   - Range: 5.0 km
   - Climb slope: 31°
   - Purpose: Thermal and visual documentation of volcanic activity

### Test Volcanoes Referenced
- **Turrialba, Costa Rica** (height 10,958 ft)
- **Popocatépetl, Mexico** (height 17,802 ft)

### Broader Applications
- Model validation and calibration (VATD models, atmospheric dispersion models)
- Rapid-response data collection post-eruption (particle size distribution, vertical ash concentration, SO₂ flux)
- Coordination with NASA ASTER satellite for SO₂ validation
- Volcano observatory support and remote sensing validation
- Wildfire smoke, dust storm, and toxic release monitoring
- Improvement of Volcanic Ash Aviation Centers (VAAC) advisory accuracy

## Key Results (Phase I Findings)

### Completed Phase I Tasks

**1. Concept of Operations & Sensor Selection**
- Five mission profiles defined through collaboration with PI, Science Lead Dr. Wardell, and NASA Technical Monitor David Pieri
- Eight primary sensors selected and ranked by scientific value and integration feasibility
- Sensor CAD models generated for mechanical integration and CG verification
- Option for mass spectrometer payload identified and reserved

**2. SuperSwift XT Airframe Design**
- Performance modeling completed for single and dual battery configurations
- Control surface authority increased by 29–59% to handle turbulence
- Propulsion system redesigned (new motor, HV LiPo battery) to achieve thrust-to-weight ratio of 1.4 at sea level (vs. 0.5 baseline)
- Environmental hardening designed: sealed inlets, gasket seals, motor cowl, larger pitot-static tube
- Dual battery trays designed for field modularity
- All design changes documented and ready for manufacturing

**3. Sensor Integration & Wind Tunnel Validation**
- **Custom Multi-Hole Probe (MHP):** Designed, 3D-printed prototype built, wind tunnel tested
  - Outperforms commercial Aeroprobe sensor in angle of attack and sideslip angle measurements
  - Validation demonstrates feasibility of low-cost, lightweight custom wind sensor
- **Payload Nose Cone:** CFD analysis completed to validate airflow to atmospheric sensors
- **Electrical & Data Plan:** Developed framework for consistent sensor data logging with autopilot telemetry
- All mechanical mounts and electrical interfaces designed within weight/CG margins

**4. Flight Certification & Test Site Preparation**
- Three Phase II test sites identified:
  - **Pawnee National Grasslands, Colorado:** Near BST, low-risk initial testing site; NASA documentation ready for submission Week 1 of Phase II; BST has prior FAA and NASA approval for this site
  - **Mountainous Colorado Site:** Allows testing all CONOPS scenarios; tall peaks (14,000 ft+) for elevation change validation
  - **Volcanic Site:** Full system validation with real-world deployment (Turrialba or Popocatépetl planned)
- All Airworthiness Flight Safety Review Board (AFSRB) and Flight Readiness Review Board (FRRB) documentation prepared for Pawnee site

## Notable Details

### Phase I Innovation & Scientific Significance
- **In situ data gap:** Volcanic Ash Transport and Dispersion (VATD) models lack validation data; current satellite data (ASTER, MODIS, AIRS, OMI) suffer from infrequent coverage, cloud masking, and unvalidated ash thickness/density estimates
- **Aviation safety imperative:** Nine Volcanic Ash Advisory Centers provide worldwide coverage; aircraft ash encounters are hazardous; 33,000 new passenger/freighter aircraft expected over 20 years
- **Unique capability:** Purpose-built sUAS can operate in regions too hazardous for manned aircraft; lower operational costs than large UAS; can be deployed nomadically without runways; simultaneous multi-aircraft deployment feasible for improved temporal/spatial coverage

### Market/State-of-Art Comparison
- **Existing sUAS limitations:** Small fixed-wing platforms not purpose-designed for harsh environments; frequent field failures; overly restrictive flight envelopes; autopilots not optimized for scientific missions
- **VTOL systems limitations:** Insufficient endurance/range for large-scale atmospheric characterization
- **SuperSwift XT advantages:**
  - Field-swappable payload system enables rapid sensor changes and data contamination avoidance
  - SwiftCore FMS designed for scientific payload integration (tight sensor-autopilot coupling improves data accuracy)
  - Ruggedized design for