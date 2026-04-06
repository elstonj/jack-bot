# Data Collection over Costa Rica Volcanoes - Final Report

## Document Metadata
- **Type:** Final Report
- **Client/Agency:** NASA Ames Research Center
- **Program/Solicitation:** Costa Rica Airborne research on foresT Ecosystem Response to volcanic gas emissions (CRATER); Contract Number 80NSSC25CA052
- **Date:** 2025-07-21 (report date); Field campaign conducted May 15-19, 2025
- **BST Products/Systems Referenced:** Black Swift S2 UAS, SwiftCore autopilot, SwiftTab user interface, SwiftStation ground control hardware
- **Key Personnel:** Daniel Prendergast (last editor); William Wade, Isaac Anderson, Tyler Willhite (NASA/partner personnel trained)

## Executive Summary

The CRATER campaign successfully demonstrated the Black Swift S2 fixed-wing UAS for volcanic gas emission monitoring and ecosystem research over Rincón de la Vieja Volcano in Costa Rica. The mission achieved its primary objective of training NASA Ames, University of Costa Rica (UCR), and U.S. Forest Service personnel in autonomous UAS operations, while collecting scientifically valuable datasets on volcanic plume behavior, gas dispersion, and vegetation stress. Despite logistical challenges and weather limitations, the campaign produced high-resolution photogrammetry, trace gas measurements, and validated a novel ground station handoff procedure for terrain-obstructed communications.

## Technical Approach

### Mission Design
- **Primary Focus:** Training local personnel (NASA, UCR, U.S. Forest Service) to independently conduct complex UAS operations in challenging volcanic terrain
- **Secondary Objective:** Collect data on CO₂, SO₂, and other volcanic gases; map vegetation response via photogrammetry and NDVI analysis

### Key Systems & Operations
1. **S2 Aircraft Configuration:**
   - Fixed-wing, electric-powered platform
   - Launched via portable catapult from remote fields and ridge locations
   - Equipped with trace gas sensors (CO₂, SO₂, water vapor), photogrammetric cameras, thermal imaging, and FLEX Fluid Flow Wind Sensor (100 measurements/second)
   - Terrain-following autopilot for safe low-altitude operations

2. **Ground Station Handoff Procedure:**
   - Novel operational innovation developed specifically for CRATER
   - Allows transfer of aircraft control between two geographically separated crews positioned at different locations
   - Maintains visual line-of-sight (VLOS) radio control despite terrain-blocked communication zones
   - Leverages SwiftCore autopilot and SwiftTab interface for seamless real-time transitions
   - Eliminates reliance on Iridium satellite communication for time-critical control (bandwidth and latency limitations)

3. **Mission Planning Software Suite:**
   - Python-based tool originally developed for Makushin Volcano (Alaska) mission
   - Integrates digital elevation models (DEMs) with canopy height data for terrain-following profiles
   - Calculates line-of-sight (LoS) communication viability between aircraft and ground stations
   - Models battery endurance based on distance, airspeed, terrain climb penalties, and loitering time
   - Incorporates regulatory airspace constraints (e.g., Temporary Flight Restrictions)
   - Visualizes handoff orbits where both losing and gaining ground stations maintain contact

### Operational Procedures
- **Pre-Flight Planning:** Daily evening sessions using integrated planning tool; collaborative route adjustments based on weather, terrain, and performance feedback
- **Wind Profiling:** Multirotor scout flights conducted prior to S2 launches to profile vertical wind shear above canopy (50-100 feet altitude)
- **Terrain Validation:** High-resolution photogrammetry flights conducted 1-2 days prior to trace gas missions to generate accurate 3D terrain models and identify vegetation obstacles
- **Flight Patterns:** Raster sampling, curtain profiling, vertically stacked measurements, photogrammetric surveys

## Products & Capabilities Described

### Black Swift S2 UAS
- **Platform Type:** Fixed-wing, electric-powered unmanned aircraft
- **Launch/Recovery:** Portable catapult launch; autonomous landing
- **Operational Advantages vs. Multirotor:**
  - 10x greater spatial coverage per flight compared to E2 multirotor
  - Reduced rotor wash interference on gas sampling measurements
  - More efficient long-range operations over mountainous terrain
  - Can achieve terrain-following flight patterns and wide-area sampling
  - Enables rapid payload swapping for multi-mission flexibility
- **Payload Capacity:** Trace gas sensors, photogrammetric cameras, thermal imaging, wind sensors
- **Endurance:** Single battery cycle sufficient for comprehensive sampling missions (specific duration not stated)

### SwiftCore Autopilot & SwiftTab Interface
- **Capability:** Autonomous flight management, terrain-following navigation, in-flight mission editing
- **Training Requirement:** Formal certification program for operators
- **Features:** Ground station handoff capability, real-time telemetry monitoring, mission logging

### Mission Planning Software
- **Core Function:** Terrain-following flight path optimization in complex environments
- **Integration Capability:** DEM data, canopy height, communication geometry, battery models, airspace constraints
- **Visualization Tools:** Altitude profiles, handoff orbits, gas measurement footprints, real-time flight tracking

### Data Products Generated
- **Photogrammetry:** High-resolution orthomosaics (6 cm/pixel), digital elevation models (meters MSL), 200+ hectare coverage per mission
- **Vegetation Analysis:** Normalized Difference Vegetation Index (NDVI) maps identifying stress zones from volcanic emissions
- **Thermal Imagery:** Canopy and terrain surface temperature data
- **Trace Gas Data:** CO₂, SO₂, and water vapor concentration measurements with precise geospatial alignment
- **Wind Data:** 100 Hz sampling rate velocity profiles

## Use Cases & Applications

### Primary Mission: Volcanic Ecosystem Research
- **Target Volcanoes:** Rincón de la Vieja, Turrialba, and Poás (Costa Rica)
- **Scientific Objective:** Quantify long-term exposure effects of persistent volcanic gas emissions on tropical forests
- **Focus Areas:** Plant health, soil chemistry, atmospheric dynamics alterations
- **Specific Measurements:**
  - Spatial and temporal variability of CO₂, SO₂, and H₂S emissions
  - Vegetation stress mapping via NDVI
  - Plume dispersion patterns and atmospheric transport

### Secondary Applications Demonstrated
1. **High-Resolution Terrain Mapping:** 6 cm/pixel orthomosaics for flight planning and hazard assessment
2. **Low-Altitude Environmental Sampling:** Safe operations 50-200+ feet above terrain in densely forested areas
3. **Multi-Operator Complex Missions:** Ground station handoff enabling operations beyond direct radio range
4. **Real-Time Data-Driven Flight Planning:** Rapid incorporation of same-day photogrammetry into subsequent gas sampling missions

## Key Results (Mission Outcomes)

### Training Achievements (Primary Objective - **FULLY MET**)
- **Formal Certification:** William Wade, Isaac Anderson, and Tyler Willhite certified in SwiftCore flight management and SwiftTab interface operation
- **Competency Domains Achieved:**
  - Independent mission planning and flight plan development
  - Aircraft system pre-checks and launcher operations
  - SwiftTab operations (loading, in-flight editing, autonomous execution)
  - Ground station handoff procedures
  - Emergency procedures and abort criteria
  - Payload calibration and sensor operations
  - Visual observation and logging protocols
  - Battery management
  - Post-flight data processing

### Flight Operations Summary
| Date | Flight ID | Type | Status | Key Outcomes |
|------|-----------|------|--------|--------------|
| May 15 | RF1 | Photogrammetry | Aborted Mid-Flight | Severe wind shear above canopy; successful launch but weather-forced abort |
| May 16 | RF2 | Photogrammetry | Completed | 200-hectare terrain mapping; generated 3D models for flight planning |
| May 17 | RF3 | Raster Sampling | Completed | Western basin baseline CO₂/SO₂ data downstream of Vent A |
| May 17 | RF4 | Vertically Stacked Sampling | Partially Successful | Flight logic spiral issue corrected; partial data salvage via waypoint skipping |
| May 19 | RF5 | Ground Station Handoff & Mapping | Completed | **First successful operational handoff**; detailed basin mapping of opposite basin |
| May 19 | RF6 | Vertically Stacked Sampling | Completed | Improved sampling patterns; refined flight logic; minor landing incident |
| May 19 | RF7 | Curtain Sampling | Cancelled | Not executed due to flap servo damage from landing incident |

### Scientific Data Quality
- **Preliminary Assessment:** "One of the most detailed and scientifically rich datasets available to date"
- **Dataset Composition:**
  - High-density wind data (100 Hz sampling)
  - Accurate gas concentration measurements (CO₂, SO₂)
  - Robust terrain and vegetation mapping (6 cm resolution)
- **Validation:** Direct comparison with 2022 E2 multirotor data demonstrates clear operational and scientific advantages of fixed-wing platform
- **Vegetation Stress Mapping:** NDVI products identified areas significantly impacted by volcanic emissions

### Operational Achievements
1. **Ground Station Handoff Procedure:** Successfully designed, tested, and executed in operational environment
   - Enabled seamless transfer of aircraft control between ridge-based crews
   - Maintained VLOS radio control throughout terrain-obstructed sections
   - Avoided latency and uncertainty of satellite-only command links
   
2. **Terrain-Following Photogrammetry Integration:** Daily same-day imagery used to refine subsequent flight plans with high confidence margins

3. **Wind Profiling Protocol:** Multirotor scout flights prevented dangerous wind shear encounters and optimized launch timing

4. **Field Maintenance & Repairs:** Two minor incidents managed with on-hand spare components
   - Avionics CAN bus connector (re-soldered, plastic obstruction removed)
   - Flap servo gear damage (identified but unable to repair in field due to resource constraints)

## Notable Details

### Training Innovation
- **Departure from Standard BST Training:** Field-based integration into active scientific mission rather than classroom/simulator-focused approach
- **Benefits Realized:**
  - Real-world exposure to site scouting, terrain assessment, and adaptive planning
  - Hands-on experience with operational constraints vs. scientific objectives trade-offs
  - Development of mission-specific checklists and procedures
  - Ground station handoff expertise (atypical for standard BST training)
  
- **Challenges Introduced:**
  - Remote NASA safety oversight created procedural delays
  - Limited repair resources and spare parts availability
  - Conflict between aggressive scientific goals and conservative operational margins

### Comparison to Multirotor Operations
- **Coverage Efficiency:** One S2 flight = coverage of 10 E2 multirotor flights
- **Sensor Interference:** S2 eliminated rotor wash effects that compromised gas sample integrity in multirotor operations
- **Operational Pattern:** E2 flights clustered in small loitering circles; S2 flights covered broad transects with coherent spatial coverage

### Technology Transfer & Sustainability
- **Knowledge Retention:** Training designed to embed mission-critical knowledge in NASA/UCR/USFS personnel for future deployments
- **Tool Sustainability:** Integrated mission planning software (Python-based) adapted for multiple volcanic environments
- **Procedural Documentation:** Detailed checklists, handoff protocols, and maintenance logs documented for institutional reuse

### Regulatory Compliance
- **Airworthiness:** Full compliance with NASA NPR 7900
- **Research Permits:** SINAC (Costa Rica wildlife authority) research permit guidelines followed
- **VLOS Operations:** All missions conducted within visual line-of-sight regulations; ground station handoff procedure maintains VLOS compliance despite terrain obstacles
- **Safety Documentation:** Detailed maintenance logs, incident reports, and photographic documentation submitted to NASA flight safety reviewers

### Community Engagement
- NASA outreach materials distributed to local communities around Rincón de la Vieja
- Interactive presentations featuring real-time flight data and imagery
- Local youth exposure to STEM careers and advanced technology

### Lessons & Future Recommendations

**Operational Improvements:**
1. Designate on-site authority empowered to make real-time safety and operational decisions (current remote consultation model created significant delays)
2. Transport high-quality calibration gases from NASA facilities (locally sourced gases failed to meet scientific standards)
3. Implement flight simulator availability for continuous operator proficiency training
4. Consider nighttime operations for improved atmospheric stability and reduced daytime turbulence (detailed white paper included in appendix)
5. Deploy