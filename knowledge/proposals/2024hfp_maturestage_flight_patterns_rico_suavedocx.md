# 2024HFP_MatureStage_Flight_Patterns_RICO_SUAVE

## Document Metadata
- Type: Experiment overview / flight operations planning document
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration)
- Program/Solicitation: Hurricane Field Program (HFP); APHEX (Atlantic Hurricane and Severe Weather Field Program); specifically Mature Stage operations
- Date: Created/Modified March 5, 2025
- BST Products/Systems Referenced: S0 (sUAS), Altius 600 (sUAS platform)
- Key Personnel: Jack Elston (last editor); PIs: Joseph Cione, Josh Wadler (ERAU), Jun Zhang, Mikal Montgomery. Co-Investigators from NOAA, NCAR, University of Miami, MSSU, UAH

## Executive Summary
RICO SUAVE (Research In Coordination with Operations Small Uncrewed Air Vehicle Experiment) is a NOAA hurricane research program that deploys small uncrewed aircraft systems (sUAS) from P-3 reconnaissance aircraft to collect high-resolution, three-dimensional wind field and thermodynamic measurements in mature tropical cyclones. The document outlines six specialized flight patterns designed to fill spatial and temporal gaps in existing hurricane observational networks and improve understanding of mature hurricane structure and intensity change.

## Technical Approach

### Overall Concept
- **Platform Integration**: sUAS deployed from NOAA P-3 aircraft during eyewall penetrations and near-core operations
- **Operational Constraints**: sUAS must maintain command-and-control range ≤125 nautical miles from P-3; communications range limit of 20 nm for video/real-time control modules
- **Deployment Altitude**: Standard deployment at 10,000 feet radar altitude; post-deployment altitudes determined by safety separation requirements
- **Coordination**: Flight operations follow 2024 National Hurricane Operations Plan (NHOP) deconfliction protocols for multi-aircraft operations (P-3, AF C-130s, saildrones)

### sUAS Platforms Specified
1. **Altius 600**: Long-duration platform (~240 minutes total flight time); capable of Catapult-Assisted Deployment (CAD) for AXBT launches; supports extended missions with multiple altitude stages
2. **S0**: Short-duration platform (~60 minutes remaining flight time post-launch/stabilization); suitable for rapid descent profiling

### Measurement Approach
- **Expendable Sondes**: Dropsondes (SST-capable), StreamSonde (new lightweight atmospheric profiler with slower descent rate), AXBTs (Airborne eXpendable BathyThermograph)
  - Up to 50 StreamSondes deployable per mission
  - ~10-15 AXBTs per sUAS flight
  - Dropsonde deployment maximized with P-3 location, sUAS "under flight"
- **Complementary P-3 Instruments**: Tail Doppler Radar (TDR), flight-level measurements, Stepped Frequency Microwave Radiometer (SFMR), Cloud Radar Lidar (CRL)

## Products & Capabilities Described

### S0 (sUAS)
- **Specifications**: ~60 minutes flight time remaining after launch, stabilization, and transit to target location
- **Capabilities**: Autonomous spiral descent/ascent patterns, altitude maintenance, heading adjustment to track local wind direction
- **Use in RICO SUAVE**: Deployed for short-duration, focused sampling missions in extreme conditions (hurricane-force winds, eyewall penetration); emphasis on rapid vertical profiling

### Altius 600 (sUAS)
- **Specifications**: ~240 minutes total flight time; capable of CAD AXBT deployment
- **Capabilities**: Multi-stage stepped descent/ascent patterns, extended loiter, circumnavigation of cyclone core, autonomous center-finding algorithms
- **Use in RICO SUAVE**: Primary platform for extended missions requiring sustained sampling across multiple altitude levels or extended core region coverage

### StreamSonde
- **What it is**: New lightweight atmospheric profiler
- **Key Difference**: Slower descent rate than traditional dropwindsonde
- **Use in RICO SUAVE**: Deployed up to 50 units per mission; preferred for sampling inflow layer thermodynamics and kinematic structure over extended areas

## Use Cases & Applications

### Pattern #1: sUAS Eyewall Circumnavigation
- **Target**: Maximize azimuthal coverage of mature tropical cyclone core
- **Mission**: Sample maximum wind speed at various altitudes within eyewall; locate and track Radius of Maximum Wind (RMW)
- **sUAS Approach**:
  - Deployed in hurricane eye near circulation center
  - Descends in counterclockwise spiral to 5,000 ft
  - Continues spiral outward until eyewall penetration
  - Adjusts heading to maintain local wind direction at tail (wind-relative navigation)
  - Performs stepped descent through 7 altitude levels: 5000, 3000, 1000, 500, 250, 150, 100 ft
  - Finds RMW at each altitude using S-pattern maneuvers
  - Total mission duration: 210-220 min for Altius 600; 60 min for S0

### Pattern #2: sUAS Inflow Layer Sampling
- **Target**: Document thermodynamic and kinematic structure of TC inflow layer and air mass properties in downdraft-cooled regions
- **Mission**: Sample downdraft-cooled air between rainbands; track air parcel trajectories
- **Deployment Location**: Downshear-left quadrant, at ~1.5× RMW radius (typically 1,000-1,500 m inflow layer depth)
- **Option 1 - Trajectory Following**: sUAS follows local tailwinds at constant altitude through inflow region; P-3 deploys sondes every 30° azimuth along same path
- **Option 2 - Stepped Descent**: Complex multi-phase profile (3500, 2500, 1500, 500 ft descent; then ascent through 1000, 2000, 3000 ft entering eyewall; continued ascent to 5000, 6500 ft if using Altius 600; then outward spiral and re-descent through 4500, 2500, 500, 250 ft)
  - Outward spiral: ~15 minutes at 30-45° angle from RMW
  - Option 2 estimated duration: ~120 minutes
- **Science Goal**: Retrieve parcel trajectories, model validation of inflow properties

### Pattern #3: sUAS Inflow-Layer Turbulence Module
- **Target**: Turbulence characteristics at hurricane-force wind speeds (V10 > 65 kt) in inflow layer
- **Mission**: Retrieve vertical profile of eddy viscosity (Km) at extreme winds
- **Deployment**: During P-3 inbound radial leg in hurricane-force conditions (V10 ≈ 35-55 m/s)
- **sUAS Approach**: Stepped descent from 3,500 ft through 7 altitude levels (3000, 2250, 1500, 900, 600, 300, 150 ft); ~8 min per level; 2-3 min descent between levels
- **P-3 Coordination**: P-3 flies "zig-zag" pattern (~15 nm legs deviating from inbound track) to maintain pace with sUAS; deploys dropsonde at start of each sUAS flight leg (7 dropsondes total)
- **Duration**: 1-1.5 hours total

### Pattern #4: sUAS Center Fix / Eye Loiter / Eye-Eyewall Sampling
- **Target**: Hurricane eye structure, near-surface conditions, eye-eyewall interface
- **Mission**: Multiple center fixes at different altitudes; eye pressure/SST variability; low-altitude loiter
- **Option 1 - Center Fix Series**:
  - Descend in tight counterclockwise spiral from 10 kft to 5,000 ft
  - Navigate to NOAA-estimated center location; continually adjust heading to find minimum wind speed (center indicator)
  - Repeat pattern at 4000, 3000, 2000, 1000 ft
  - Optional: Radial excursion to eyewall edge at 1,000 ft, brief 2-min eyewall penetration, return to center, conduct 3rd center fix
- **Option 2 - Spiral Profile with Level Flight**:
  - Spiral ascent centered on estimated center with 2-orbit level flight every 3,000 ft up to 15 kft (pending AOC-ORM approval)
  - Reverse process: Descend from 12,000 ft in 3,000 ft increments to 1,000 ft
  - Conduct 2nd center fix; loiter/orbit at 1,000 ft matching estimated hurricane heading and forward speed
  - Continue loiter until 30 minutes battery time remains
  - **Advanced Navigation**: Document suggests employment of FD/ARWO methodology: maintaining wind 90° off track; programming "desired track parameter" 90° offset; employing GSHTL (ground speed higher turn left) / GSLTR algorithms
- **Battery Life**: Up to 3.5 hours for extended loiter operations

### Pattern #5: Video Capture Module
- **Target**: Hurricane boundary layer eye and eye-eyewall interface (visual documentation)
- **Mission**: Record high-quality video of ocean surface, eye structure, cloud features
- **Constraint**: P-3 must remain within 20 nm of sUAS for communication
- **sUAS Approach**:
  - Launch in eye; descend to 1,000 ft in eye to observe ocean structure
  - Transit toward eyewall and sample region
  - Flight pattern adaptive: modified to find high-wind, minimal-cloud regions for optimal camera visibility
  - Pattern may be further modified to record unique features or nearby platforms (e.g., other observational systems)
- **Duration**: Up to 3.5 hours battery life possible

### Pattern #6: Saildrone Overflight Module
- **Target**: Ocean surface measurements from saildrone platform in tropical storm-force winds or higher (V10 > 34 kt)
- **Mission**: Coordinated sUAS-P-3 overflight of actively-transmitting saildrone; dual sampling from above and below
- **Deployment**: sUAS released ≥20 nm upwind of saildrone in TS-force conditions; descends to 5 kft then to 1,000 ft for overflight
- **P-3 Coordination**: Executes Figure-4 flight pattern; deploys expendables ~5 nm either side of saildrone and directly overhead; coordinates timing so P-3 overflight occurs simultaneous with sUAS overflight
- **Extended Operations**: If battery permits, sUAS circumnavigates TC and conducts 2nd saildrone overflight; P-3 repeats deployment pattern
- **Duration**: Minimum 30+ minutes; highly dependent on TC/saildrone characteristics

## Key Results
This document does not contain experimental results; it is a pre-mission planning document outlining proposed flight operations for the 2024 Hurricane Field Program.

## Notable Details

### Science Objectives (APHEX-aligned)
- Fill spatial and temporal gaps in existing airborne/surface measurements in mature hurricanes
- Improve three-dimensional wind field representation in eyewall region
- Increase spatial density of boundary layer thermodynamic sampling
- Achieve more accurate ocean surface wind velocity measurements
- Better understand internal processes contributing to mature hurricane structure and intensity change

### Operational Innovations
- **Extended Range**: sUAS no longer requires P-3 "babysitting" due to improved range/endurance; P-3 can pursue independent sampling objectives while maintaining command-and-control
- **Deconfliction**: Established inter-agency protocols (2024 NHOP) enable safe multi-platform operations (P-3, AF C-130, sUAS) within same airspace
- **Autonomous Navigation**: Advanced center-finding algorithms incorporating wind-relative tracking and ground-speed methods rather than simple pressure/wind-speed minimization
- **Flexible Expendable Deployment**: No pre-set sonde count; deployment driven by mission-specific conditions and P-3 pattern flown; prioritizes SST-capable dropsondes and new StreamSonde technology

### Instrumentation Integration
- **Validation Strategy**: All sUAS modules designed to collect coincident measurements with P-3 flight-level, TDR, dropsonde, SF