# Data Collection over Costa Rica Volcanoes – Interim Report

## Document Metadata
- **Type:** Interim Report (field campaign progress report)
- **Client/Agency:** NASA Ames Research Center
- **Program/Solicitation:** CRATER (Costa Rica Airborne research on foresT Ecosystem Response to volcanic gas emissions) mission
- **Contract Number:** 80NSSC25CA052
- **Date:** May 19, 2025
- **BST Products/Systems Referenced:** S2 UAS, SwiftCore autopilot, SwiftPilot autopilot, SwiftTab interface, SwiftStation ground control station
- **Key Personnel:** Jack Elston (last editor); William Wade (trainee); collaboration with Dr. Josh Fisher, Universidad de Costa Rica (UCR), U.S. Forest Service

## Executive Summary
The CRATER campaign is a collaborative NASA Ames–Black Swift Technologies field mission in Costa Rica aimed at quantifying volcanic gas emissions (CO₂, SO₂, H₂S) and their effects on tropical ecosystems around Rincón de la Vieja, Turrialba, and Poás volcanoes. As of May 19, 2025, the team has completed five flights using the S2 fixed-wing UAS, validated a novel ground station handoff procedure for terrain-obstructed operations, and trained personnel from NASA and the U.S. Forest Service in autonomous UAS operations. The campaign has overcome avionics maintenance issues and wind-related aborts to achieve successful photogrammetric mapping and trace gas data collection.

## Technical Approach

### S2 UAS Platform
- Fixed-wing, electric-powered aircraft designed for environmental monitoring in extreme conditions
- Equipped with trace gas sensors (LICOR 850 CO₂/H₂O analyzer), photogrammetric imaging systems, and terrain-following autopilot
- Launched via portable catapult from remote fields and ridge locations
- Battery endurance: 40–70 minutes per cycle depending on flight profile
- Minimum turn radius and climb/descent rate constraints influence feasible flight patterns

### Ground Station Handoff Procedure
A central innovation developed for CRATER to enable aircraft control transfer between two crews at geographically separated locations:
- **Rationale:** Allows missions to proceed across terrain where line-of-sight (LoS) communication is obstructed by ridges or forest canopy, while remaining compliant with VLOS regulations and NASA NPR 7900
- **System Components:** S2 UAS with SwiftPilot autopilot, SwiftStation tripod-mounted ground control station, SwiftTab Android tablet interface, manual handset (2.4 GHz backup)
- **Key Design Decision:** Prioritizes LoS radio control over satellite (Iridium) communication to reduce latency and enable real-time crew response to dynamic airspace situations
- **Standard Operating Procedure:**
  1. **Phase 1 (Mission Setup):** Predefine Handoff Waypoint with safe orbit, load flight plans, confirm batteries and crew communication
  2. **Phase 2 (Transition):** Losing operator sends aircraft to Handoff Waypoint; gaining operator visually confirms; countdown and power handoff (losing station powers down, gaining station boots and establishes link)
  3. **Phase 3 (Post-Handoff):** Aircraft proceeds from Handoff Waypoint to Landing Pattern Holding Point; gaining operator initiates final approach
- **Contingencies:** If gaining station fails to link, manual handset backup available; RF interference protocols; loss-of-LoS abort procedures; repositioning protocols for obstructed handoff points

### Mission Planning Software
- Custom Python-based tool originally developed for Makushin Volcano (Alaska) mission, adapted for Costa Rica conditions
- **Integrated constraints:**
  - Digital elevation models (DEMs) with canopy height buffers (from Dr. Josh Fisher collaborators) for terrain-following safety margins
  - Line-of-sight (LoS) communication geometry checks to determine handoff requirement and optimal orbit locations
  - Battery endurance estimation (accounting for distance, airspeed, terrain climb penalties, loiter times)
  - Regulatory airspace constraints (e.g., Temporary Flight Restrictions, altitude caps)
- **Outputs:** Optimized flight lines, feasibility predictions, LoS visualization, handoff orbit planning, battery usage forecasts
- **Daily use:** Collaborative, real-time mission planning with evening sessions adjusting routes based on weather, observed performance, and ground surveys

### Flight Pattern Strategies
Evaluated and implemented multiple sampling approaches depending on site and scientific objectives:
- **Radial patterns:** Outward spokes from vent source; challenges include maintaining consistent distance over terrain and turn radius violations at low altitude
- **Vertically stacked lines:** Upwind or downwind from vents to observe plume evolution; decision between constant MSL (better repeatability) vs. terrain-following (better plume sampling altitude consistency)
- **Grid-style photogrammetry:** Full-coverage parallel legs for broad spatial mapping; useful for diffuse emissions or unknown vent locations; battery and LoS planning critical
- **Downwind transects:** Plume transport assessment
- **Curtain-style (stepped transect):** Descending flight legs for broad dispersion mapping
- **Hybrid approach employed:** Photogrammetry for baseline mapping, terrain-following stacks for vertical sampling, downwind transects for plume transport

## Products & Capabilities Described

### Black Swift S2 UAS
- **What it is:** Fixed-wing, electric-powered, catapult-launched uncrewed aircraft with terrain-following autopilot
- **Proposed use in CRATER:** Airborne platform for simultaneous photogrammetric imaging and in situ trace gas sampling around active volcanic emission zones
- **Specifications/performance claims:**
  - Battery endurance: 40–70 minutes per cycle
  - Collection altitudes: 54–64 meters MSL (typical)
  - Mission distances: 46–56 km per flight
  - Flight durations: 40–49 minutes
  - Takeoff trajectory: Shallow climb, 150+ m lateral separation from obstacles, 60+ m altitude gain before horizontal plane of nearest pole
  - Repeatable takeoff pattern under varying wind conditions
  - Capable of autonomous mission execution and manual override via handset
  - Minimum turn radius constrains sharp-turn patterns; glide ratio affects descent planning

### SwiftCore / SwiftPilot Autopilot
- **What it is:** Onboard autopilot system governing aircraft autonomy and control surface response
- **Use in CRATER:** Executes pre-programmed flight plans, terrain-following profiles, holding patterns, and landing sequences; responds to SwiftTab waypoint updates in-flight
- **Performance:** Post-flight analysis tools show nominal control surface response curves, no signal lag or dropout; capable of managing dynamic atmospheric disturbances

### SwiftTab Interface
- **What it is:** Android tablet-based ground control station user interface
- **Use in CRATER:** Mission loading, in-flight telemetry monitoring, waypoint confirmation, command issuance, data capture timing control
- **Capabilities:** Real-time telemetry display, inflight mission editing, sensor operation commands, autonomous landing abort capability

### SwiftStation Ground Control Hardware
- **What it is:** Tripod-mounted ground station with integrated radios and power
- **Use in CRATER:** Portable control node for LoS command-and-control; supports dual-station operations for handoff procedures
- **Deployment:** Positioned at Power Plant Field (primary launch/recovery), Route 918 Field (takeoff-only), and Santa Maria Ranger Station (ridge-top for handoff operations)

### LICOR 850 CO₂/H₂O Analyzer
- **What it is:** Trace gas sensor payload
- **Use in CRATER:** In-flight measurement of carbon dioxide and water vapor concentrations
- **Performance:** Smooth, consistent sensor output during flight; no signal dropout, thermal drift, or delayed response during attitude changes; baseline preflight/postflight readings align with expected ambient values; captures coherent CO₂ gradients downwind of known emission points; localized concentration peaks consistent with wind-driven plume advection

## Use Cases & Applications

### Primary Mission: CRATER (Costa Rica)
**Application:** Quantifying tropical ecosystem response to persistent volcanic gas emissions

**Sites:** Three volcanic regions with distinct characteristics
- **Rincón de la Vieja Volcano (primary focus):**
  - **Vents A (Las Pailas sector):** High CO₂/SO₂ emissions, visible thermal anomalies, persistent degassing near boardwalk; stunted canopy and altered pigmentation from chronic exposure
  - **Vents B (Santa Maria Ranger Station area):** Lower-temperature degassing in dense forest; subtler CO₂, detectable only via instruments; opportunity to study gas diffusion through canopy
  - **Vents C (Power Plant Field terminus):** Mixed hot/cold geothermal features; margin of forested/cleared land; convenient for calibration and spatial comparisons
- **Turrialba Volcano:** Secondary target, accessibility dependent
- **Poás Volcano:** Secondary target, accessibility dependent

**Scientific Objectives:**
- Characterize volcanic plume structure and evolution
- Understand downwind gas transport and dispersion
- Detect localized CO₂ anomalies across varying terrain and land-cover types
- Quantify spatial and temporal variability of emissions (CO₂, SO₂, H₂S)
- Assess ecosystem impacts on plant health, soil chemistry, and atmospheric dynamics
- Validate stationary ground-based instruments

**Operational Requirements Addressed:**
- Remote launch/recovery from challenging terrain (portable catapult capability)
- Operations over complex topography with terrain-following capability
- Navigation and communication in LoS-obstructed regions (ground station handoff)
- Precise photogrammetric data collection for terrain and canopy modeling
- Integration of multiple payload types (imaging + trace gas sensors)
- Compliance with Costa Rican aviation regulations and NASA NPR 7900 safety standards

## Key Results (as of May 19, 2025)

### Flight Summary
**Completed Missions:**
- **May 13:** Preflight check caught avionics issue; field maintenance performed (CAN bus connector re-soldering, solder joint reinforcement, obstruction removal). Aircraft returned to operational status. Battery B2-0060 (NASA designation "Battery 2") removed from rotation after incidental short circuit during diagnostics; placed in liposac for storage.
- **May 15:** Launch successful but high wind speeds near/above airspeed thresholds forced mid-mission abort before data collection. Post-flight analysis confirmed control surfaces responding nominally; irregular flight behavior attributed to environmental turbulence (gust fronts, rotor-like flows over ridge) rather than residual avionics faults.
- **May 16:** Flight #3 – Full photogrammetry mission executed successfully; 3D terrain models generated for flight planning.
- **May 17:** 
  - Flight #5 (Vertically stacked trace gas) – Partially successful; discrepancies in data density and navigation timing identified; execution logic refinement underway.
  - Wide-area trace gas survey over western volcanic basin (Vents A transect); baseline CO₂/SO₂ dispersion data collected.
- **May 18:** Weather prevented flights; used downtime for data processing, imagery analysis, and ground station handoff procedure validation.

### Flight Performance Data
Completed flights logged the following characteristics:

| Flight ID | Collection Box | Takeoff Site | Landing Site | Route Length (km) | Collection Altitude (m MSL) | Duration (min) | Total Lost LoS (min) | Max Consecutive Lost LoS (min) | Battery Used (%) |
|-----------|---|---|---|---|---|---|---|---|---|
| A | #1 SE Short | Power Plant | Power Plant | 56.1 | 59.2 | 49.2 | 2.5 | 1.0 | 50.9 |
| B | #1 SE Short | Rt 918 Field | Power Plant | 52.1 | 59.2 | 45.7 | 0.0 | 0.0 | 46.9 |
| C | #2 SE Full | Power Plant | Power Plant | 53.7 | 63.4 | 47.1 | 1.3 | 0.4 | 49.0 |
| D | #2 SE Full | Rt 918 Field | Power Plant | 49.6 | 63.4 | 43.5 | 0.0 | 0.0 | 44.9 |
| E | #3 South Long West | Power Plant | Power Plant | 46.4 | 54.2 | 40.7 | 0.1 | 