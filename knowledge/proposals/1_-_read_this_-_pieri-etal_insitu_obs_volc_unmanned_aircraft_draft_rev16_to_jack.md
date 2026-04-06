# In Situ Observations and Sampling of Volcanic Emissions with Unmanned Aircraft: A NASA/UCR Case Study at Turrialba Volcano, Costa Rica

## Document Metadata
- **Type:** Academic/Technical White Paper (draft)
- **Client/Agency:** NASA / University of Costa Rica (UCR)
- **Program/Solicitation:** Not explicitly stated as SBIR, but referenced as NASA project
- **Date:** January 19, 2016 (Draft revision 16)
- **BST Products/Systems Referenced:** None explicitly mentioned. Document discusses UAV platforms (Global Hawk, Ikhana, SIERRA, Dragon Eye, Vector Wing 100) but these are NASA/military systems, not BST products.
- **Key Personnel:** David Pieri (JPL, corresponding author), Jorge Andres Diaz (UCR/GASLAB), Geoffrey Bland (NASA Wallops), Matthew Fladeland (NASA Ames), Vincent Realmuto (JPL), Ted Miles (NASA Wallops), Ali Abtahi (Teladaq LLC)

## Executive Summary
This academic paper describes the use of unmanned aerial vehicles (UAVs) and aerostats to conduct in situ observations and sampling of volcanic emissions, particularly SO₂ and ash, at Turrialba Volcano in Costa Rica. The work addresses critical gaps in validation of remote sensing data and transport models used for aviation hazard assessment following volcanic eruptions. The authors present a multi-platform approach using tethered balloons, micro-UAVs (Dragon Eye, Vector Wing 100), and medium-sized UAVs (SIERRA) to measure volcanic plume properties that are difficult or dangerous to access with manned aircraft.

## Technical Approach

### Problem Context
- Current volcanic ash and SO₂ concentration estimates from satellite remote sensing are systematically unvalidated by in situ data
- Lagrangian transport models (PUFF, HYSPLIT) depend critically on accurate boundary conditions (injection altitude, ash concentration distribution, particle size) that are poorly known
- The 2010 Eyjafjallajökull eruption in Iceland demonstrated economic and operational costs of inadequate ash hazard forecasting, forcing shift from "zero tolerance" to risk-based airspace management
- Manned aircraft face crew safety risks and engine damage risks when penetrating high-ash-concentration plumes

### Proposed UAV-Based Solution
The authors propose a three-tiered UAV platform approach:

1. **Aerostats (Tethered Balloons & Kites)**
   - Simple, dependable time-series measurements at fixed locations
   - Meteorological balloons (1m diameter) with SO₂-sonde payloads
   - Extended wind capability using Helikite™/SkyDoc™ hybrids (stable to >73mph)
   - Payloads: electrochemical SO₂ sensors (0-5 and 0-20 ppmv ranges), pressure, temperature, RH, GPS
   - Tested to ~13,000 ft ASL at Turrialba
   - No helium requirement for kites (advantage on remote volcanoes)
   - Cost-effective for atmospheric profiling

2. **Micro-UAVs (µUAVs)**
   - **Dragon Eye (RQ-14):** 2.25 kg, 1.14m wingspan, 500g payload, 8,000 ft ceiling
     - Hand or bungee launchable, fully autonomous with GPS/INS
     - Rugged: absorbs impact on landing, reassemblable
     - Adapted payload: electrochemical SO₂ sensor, optical particle counter (0.5-5µm), vacuum sampling bottle, T/P/RH sensors
     - Video range ~5km
     - Low aircraft cost allows higher deployment risk
   
   - **Vector Wing 100:** 2.1m wingspan, 3.6 kg flight weight, ~1kg payload
     - Tailless flying wing design
     - Operated by UCR/GASLAB in San Jose
     - Equipped with small electrochemical SO₂ sensor

3. **Medium-Sized UAV**
   - **SIERRA (Sensor Integrated Environmental Remote Research Aircraft):** NASA Ames platform
     - Moderate endurance and payload capabilities
     - Lower operating costs than NASA Global Hawk/Ikhana
     - Can carry miniaturized mass spectrometers
     - Battery/fuel-cell powered options reduce ash ingestion sensitivity
     - Suitable for <12 kt altitude operations near active volcanoes
     - Can extend range into ash-dense/gas-dense plume cores

### Coordination with Remote Sensing
- Synchronized in situ measurements with ASTER satellite overpasses for validation
- Combined approach: orbital remote sensing + sub-orbital UAV observations
- Ground truth measurements validate radiative transfer models used for SO₂ and ash concentration retrieval

## Products & Capabilities Described

### Instrumentation & Payloads
1. **SO₂ Measurement Systems**
   - Electrochemical SO₂ sensors (0-5 ppmv, 0-20 ppmv ranges)
   - Miniaturized SO₂ sonde developed by JPL/Pieri/Abtahi
   - Measurements in range of 2-20 ppmv within 3km of Turrialba vent

2. **Aerosol Sampling & Characterization**
   - Optical particle counters (0.5-5µm and broader 0.1-960µm ranges)
   - Evacuated vacuum sampling bottles with automatic actuators
   - Aerosol impactors
   - Ash concentration measurements (µg/m³)

3. **Atmospheric Profiling**
   - Temperature, pressure, relative humidity sensors
   - GPS location tracking
   - Wind velocity measurements
   - 3D aerosol/gas distribution mapping

4. **Remote Sensing Analysis**
   - ASTER thermal infrared bands (8.125-11.65 µm) for SO₂ detection
   - Principal component decorrelation stretch for plume visualization
   - Radiative transfer modeling for concentration retrieval
   - AVHRR, GOES, MODIS, AIRS data exploitation

### NASA Platforms Referenced (Not BST)
- **NASA Global Hawk:** 44 ft length, 116 ft wingspan, 26,750 lb MTOW, 60,000 ft ceiling
- **NASA Ikhana:** 36 ft length, 66 ft wingspan, 10,500 lb MTOW, 25,000 ft ceiling (civilian Predator variant)
- **SIERRA:** Medium-sized platform with proven Arctic operations (CASIE 2009)

## Use Cases & Applications

### Primary Application: Volcanic Emissions Monitoring
**Turrialba Volcano Case Study (3,340m ASL, Costa Rica)**
- Basaltic-to-dacitic stratovolcano
- Continuously erupts SO₂, steam, CO₂ from south-westernmost vent
- Low-altitude (<12 kft) SO₂ emitter with light ash emissions
- History of 5+ major explosive eruptions in past 3500 years
- Recent activity: increased seismic activity, fumarolic activity since 1998
- Recent observations: increased helium output indicating new magma, elevated SO₂/CO₂ concentrations

### Science Objectives at Turrialba
1. Determine primary injection altitude and concentration distributions—critical boundary condition for transport models
2. Understand how remote sensing instrument response relates to plume physical/chemical properties
3. Establish ash/gas concentration thresholds for instruments
4. Scale local in situ measurements to plume-wide properties
5. Quantify ash/gas present outside satellite instrument response envelope
6. Measure SO₂ loss as function of downwind distance
7. Validate orbital data (ASTER) with coordinated sub-orbital measurements

### Broader Applications Beyond Turrialba
- **Aviation Hazard Assessment:** Validation of volcanic ash concentration estimates used to forecast aircraft hazards
- **Ash Cloud Trajectory Prediction:** Improved boundary condition data for VATD models (PUFF, HYSPLIT)
- **Eruption Column Characterization:** Rapid response to explosive eruptions to constrain source parameters
- **Atmospheric Chemistry:** Support WRF-Chem and similar models including atmospheric chemistry
- **Remote Volcanic Areas:** Enhanced capability for monitoring inaccessible volcanoes (Aleutians, Kamchatka, etc.)
- **Pre-eruption Monitoring:** Detection of volcanic restlessness through steady-state emission changes

## Key Results (from Turrialba Case Study, as of February 2013)

### Aerostat Operations
- **SO₂-Sonde Deployments:** Multiple successful launches to ~13,000 ft ASL (6.5 kft AGL)
- **Measured Concentrations:** 2-20 ppmv within ~3 km of vent
- **Peak Altitude Concentrations:** Maximum 5 ppmv recorded at ~3,300m ASL on 01 February 2012
- **Estimated Actual Maximum:** 6-7 ppmv (sensor saturation)
- **Comparison with ASTER:** Excellent agreement with ASTER estimate of 6 ppmv from 21 January 2012 overpass
- **Coordinated Measurements:** Successful cloud-free coordinated tethersonde/ASTER acquisitions on 07 Jan 2013, 16 Jan 2013, 08 Feb 2013 (data reduction ongoing)

### ASTER Remote Sensing Analysis (21 January 2012)
- **SO₂ Plume Detection:** Principal component decorrelation stretch clearly visualized plume extending westward
- **Concentration Retrieval:** Radiative transfer modeling yielded maximum ~6 ppmv—consistent with later in situ measurement
- **Plume Altitude:** Visual identification of plume position and extent
- **Characteristic Conditions:** Results representative of Turrialba emissions during this period (corroborated by Campion et al., 2012)

### Dragon Eye Testing (Fall 2012)
- **Platform Acquisition:** NASA Ames acquired 75 Dragon Eye aircraft as USMC surplus in fall 2012
- **Deployment:** ~10 aircraft allocated for March 2013 Turrialba testing
- **Initial Testing:** Demonstrated as "rugged, dependable, and flexible platform for volcanological research within lower troposphere"
- **Payload Integration:** Successfully adapted for SO₂ measurement and aerosol sampling
- **Risk Tolerance:** Low aircraft cost enables higher deployment risk for plume penetration

### Vector Wing 100 Operations
- Operational testing underway since 2011 by UCR/GASLAB
- Equipped with small electrochemical SO₂ sensor
- Status as of Feb 2013: details limited but operational (document cut off mid-description)

## Notable Details

### Regulatory & Operational Context
- **Airspace Clearance Challenges:** UAV flight approval significantly more difficult in high-traffic areas (US, Europe); Costa Rica offers case-by-case clearance via Director General of Civil Aviation (DGAC) and monitoring by Costa Rican Air Surveillance Service
- **Technology Export Sensitivity:** Potential restrictions on UAV export for international operations (dual-use technology concerns)
- **Manned Aircraft Precedent:** EUFAR campaign during Eyjafjallajökull 2010 deployed 70 research flights on 12+ aircraft over 250 flight hours; confirmed UAVs necessary for dense plume penetration that endangers manned aircraft

### Partnership & Collaboration
- **International:** NASA (JPL, Wallops, Ames), University of Costa Rica (GASLAB/CICANUM), Teladaq LLC
- **Coordination:** Sub-orbital campaigns synchronized with NASA Terra/ASTER orbital overpasses
- **Lessons from Eyjafjallajökull 2010:** European research community identified urgent need for instrumented UAVs through EUFAR experience

### Site Selection Rationale
Turrialba chosen as "natural laboratory" because:
- Low-altitude steady-state emissions (<12 kft) provide relatively benign test environment
- Good technical infrastructure and physical volcano access
- Conditions suitable for platform/instrument proving before attempting high-altitude explosive eruption scenarios (>30 kft)
- Persistent volcanic activity enables extended testing campaign
- Costa Rican regulatory environment favorable for UAV testing

### Technology Miniaturization Strategy
- Leveraging spacecraft-grade miniaturization technology for small-UAV instrument development
- Compact instruments already feasible or in development: optical particle counters, aerosol impactors, aerosol optical absorption analyzers, UV