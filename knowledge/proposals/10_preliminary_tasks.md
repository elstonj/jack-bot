# A Ruggedized UAS for Scientific Data Gathering in Harsh Environments: Phase I Final Report

## Document Metadata
- Type: SBIR Phase I Final Report
- Client/Agency: NASA
- Program/Solicitation: 2016 NASA SBIR
- Date: September 10, 2016
- BST Products/Systems Referenced: SuperSwift XT, DragonEye (reference platform), Vector Wing 100 & 500 (reference platforms)
- Key Personnel: Jack Elston (PI), Dr. Dixon, Dr. Stachura, Prof. Argrow (CU), Dr. David Pieri (JPL), Dr. Lois Wardell (Arapahoe SciTech), Dr. Jorge Diaz (volcano sampling expert)

## Executive Summary
This Phase I SBIR report documents Black Swift Technologies' development of the SuperSwift XT UAS system for scientific monitoring of volcanic plumes and ash emissions. The Phase I effort focused on establishing mission requirements, sensor selection, and airframe specifications for high-altitude volcano sampling operations, with planned Phase II implementation of payload integration and flight testing in Colorado and eventual deployment to active volcanoes like Popocateptl (Mexico) and Turrialba (Costa Rica).

## Technical Approach

### Mission Development
BST established a Concept of Operations (CONOPS) based on five primary volcanic sampling mission types:
1. **Volumetric plume profiling** - Grid sampling at multiple altitudes over 30 km radius
2. **Cylindrical profiling** - Continuous vertical profile via helical climb pattern
3. **Long-distance gradient sampling** - 30 km out-and-back transects downwind
4. **Vent contouring** - Terrain-following flight at 50 ft AGL around vents
5. **Terrain mapping** - High-resolution photogrammetry (8 km² per flight at 3.7 cm/pixel)

The CONOPS was driven by past missions to Turrialba volcano (Costa Rica) using DragonEye and Vector Wing platforms, with recommendations from expert volcanologists including Dr. Pieri (JPL) and Dr. Diaz.

### Airframe Requirements Development
SuperSwift XT functional requirements derived from mission profiles:
- Hand-launchable with 1 lb payload to 12,000 ft MSL
- Rail/bungee launchable with 5 lb payload to 12,000 ft MSL
- Ceiling: ≥20,000 ft MSL with 200 ft/min climb capability
- Maximum climb angle: >31° at 18,000 ft with 3 lb payload
- Flight range: >50 nm (80 km) at 20,000 ft
- Endurance: >100 minutes at cruise altitude 8-20,000 ft
- Enhanced roll/pitch authority vs. original SuperSwift
- Operational wind limit: 30 kts (with 40 kts gust capability via airframe upgrade)

### Atmospheric Operational Envelope
- Ambient temperatures: Standard conditions at altitude (icing possible at high altitude)
- Particulate concentrations: Design baseline 500 μg/m³ (maximum 2,000 μg/m³); potential testing up to 4,000 μg/m³
- Maximum wind: 30 kts operational (15.4 m/s), 40 kts gust capability
- Launch altitude: Up to 11,800 ft (Popocateptl worst-case scenario)
- Target altitudes: Up to 19,800 ft MSL

## Products & Capabilities Described

### SuperSwift XT
- **Description**: Ruggedized fixed-wing UAS for harsh environment operations, evolved from original SuperSwift platform
- **Proposed Use**: High-altitude volcano monitoring platform carrying multiple scientific payloads
- **Specifications**:
  - Maximum payload capacity: 5 lbs (rail launch) to 1 lb (hand launch)
  - Flight ceiling: ≥20 kft MSL
  - Endurance: >100 minutes
  - Range: >50 nm
  - Launch methods: Hand launch, rail launch, bungee launch, belly landing on unimproved terrain
  - Payload interfaces: Mechanical and electrical integration planned for Phase II

### Sensor Payload Suite (Selected for Phase II Integration)

**Meteorological:**
- iMet-XF: PTH (pressure, temperature, humidity) measurements
  - Weight: 52g
  - Accuracy: ±2.5 hPa, ±0.7°C, ±5% RH
  - Power: 0.1 W
  
- BST 5-hole probe: 3D wind velocity measurement
  - Weight: 50g
  - Accuracy: ±0.5 m/s, ±0.5° direction
  - Power: 0.5 W

**Trace Gas:**
- iMet-MiniGAS: Multi-gas sensor package
  - Weight: 1,200g (with battery)
  - Measures: CO₂, SO₂, H₂S (PTH integrated)
  - Performance:
    - CO₂: 0-2000 ppm, 20 ppm resolution, <10s response
    - SO₂: 0-200 ppm, 0.5 ppm accuracy, <20s response
    - H₂S: 0-200 ppm, 0.25 ppm accuracy, <35s response
  - Power: ~3.0 W
  - Note: Long response time requires 2-4 minute loitering periods for accurate sampling

**Particulates:**
- MSE Inc. Mini PCS Nephelometer
  - Weight: 250g
  - Forward-looking inlet for particle size-frequency distribution
  - Resolvable sizes: 1-100 μm
  - Power: 20 W

**Imaging:**
- MapIR Survey2 (EO/multispectral): 47g, 1.0 W
- Forward FPV camera (COTS): 200g, 0.9 W
- FLIR VUE thermal imager: 113g, 2.2 W

**Total Payload Mass**: ~2.4 kg (~5.3 lbs) with all sensors

### Reference Platforms Analyzed

**DragonEye:**
- Payload: 1.1 lb hand-launchable
- Ceiling: 12,000 ft
- Cruise: 35 kts
- Endurance: 60 min
- Current volcano payload: SO₂ sensors (5/20/50 ppmv), thermal camera (Indigo TIR), color/low-light cameras, temperature/pressure/humidity sensors
- Future payloads: Nephelometer (IDI Corp), OEM CO₂ sensor, experimental CO₂ sensor

**Vector Wing 100:**
- Payload: 2 lbs (rail launch)
- Ceiling: 15,000 ft
- Cruise: 35 kts
- Endurance: 30 min
- Past deployments: Turrialba sampling with CO₂ sensors

**Vector Wing 500:**
- Payload: 9.9 lbs (rail launch)
- Ceiling: 14,800 ft
- Cruise: 35 kts
- Endurance: 30 min
- Notable: Successfully flew miniaturized mass spectrometer (Inficon MS-XRP3 + KNF diaphragm pump + Creare turbo molecular drag pump)

## Use Cases & Applications

### Primary Mission: Volcanic Plume Monitoring
**Volcanoes Targeted for Phase II Testing & Deployment:**
- Turrialba Volcano, Costa Rica (10,958 ft elevation)
- Popocateptl, Mexico (17,802 ft elevation) - primary worst-case planning reference

**Mission Scenarios:**
1. **Volumetric Profiling** (example: Popocateptl)
   - 4 parallel 6 km sampling lines spaced 1 km apart
   - 3 altitude levels, 500 ft spacing
   - Total flight distance: 27 km per altitude level
   - Maximum altitude: 19,300 ft MSL
   - Time of flight: 75 minutes
   - Maximum range from launch: 10.4 km

2. **Cylindrical Profiling (Plume Column)**
   - Helical climb pattern directly above volcano
   - Climb/descent rate: 200 ft/min (1 m/s)
   - Maximum height: 2,000 ft above volcano summit
   - Helix diameter: 1 km (adjustable)
   - Time of flight: 34 minutes
   - Maximum altitude: 19,800 ft MSL

3. **Long-Distance Gradient**
   - Downwind transect at ~1,500 ft above summit
   - 30 km out-and-back sampling pattern
   - Maximum altitude: 19,300 ft MSL
   - Time of flight: 74 minutes
   - Maximum range: 37.3 km

4. **Vent Contouring**
   - Terrain-following flight 50 ft AGL over vents
   - Climb slope: up to 31° (steepest portions of Popocateptl)
   - Requires laser altimeter for AGL measurement
   - Time of flight: 14 minutes

5. **Terrain Mapping**
   - High-resolution photogrammetry capability
   - Area coverage: up to 8 km² per flight
   - Ground resolution: 3.7 cm/pixel
   - Flight time: ~90 minutes
   - Total path length: ~62 km

### Secondary Applications
- Validation of volcanic ash transport and dispersion (VATD) models
- Validation of satellite data (OMI, TOMS volcanic SO₂ measurements)
- Aviation hazard characterization (ash concentrations for aircraft safety)
- Atmospheric input data for volcanic hazard forecasting
- Support for remote sensing validation (DOAS, FTIR measurements)

### Operational Timeline (Example Two-Flight Campaign)
- T-24 hrs: Mission planning and flight pattern development
- T-2 hrs: Transport equipment to launch site (man-portable)
- T-45 min: Site identification and preparation
- T-30 min: Aircraft assembly and payload calibration
- T-0: Launch
- T+85-90 min: Mission execution
- T+100 min: Landing, post-flight inspection, data download
- T+2 hrs: Second payload installation
- T+4 hrs: Second flight completion and data download
- T+4.5 hrs: Equipment pack-out and team egress

## Key Results (Phase I Findings)

### Mission Requirements Finalized
- Five sampling scenarios defined and validated with expert volcanologists (Pieri, Wardell)
- Mission profiles confirmed as covering all current and planned volcano monitoring missions
- Sensor compatibility verified with mission profiles (loitering strategies developed to accommodate sensor response times)
- Airframe requirements updated to accommodate refined mission and sensor specifications

### Sensor Selection Completed
Two candidate payload configurations developed and refined based on:
- Weight/size constraints (optimized for SuperSwift XT)
- Scientific capability (measurements of CO₂, SO₂, H₂S, particulates, PTH, wind)
- COTS availability (avoiding prototypes not yet commercialized)
- Integration feasibility (no extensive hand-held device modifications)

**Final Payload Selected:**
- iMet-miniGAS (trace gas + PTH)
- BST 5-hole probe (3D winds)
- MSE Mini PCS Nephelometer (particulates)
- MapIR Survey2 + FLIR VUE (imaging)
- Total mass: 2.4 kg (well within SuperSwift capacity)

### Airframe Capability Gaps Identified
Compared to reference platforms (DragonEye, Vector Wing 100/500), SuperSwift XT must achieve:
- Higher altitude ceiling (20 kft vs. 12-15 kft of predecessors)
- Greater endurance (>100 min vs. 30-60 min)
- Better climb performance (31° slope capability)
- Multi-launch method flexibility (hand, rail, bungee)
- Enhanced control authority for turbulent volcanic environments

### Atmospheric Operational Envelope Defined
- Operating limits: 30 kts steady wind, 40 kts gust capability
- Particulate environment: 500 μg/m³ baseline, 2