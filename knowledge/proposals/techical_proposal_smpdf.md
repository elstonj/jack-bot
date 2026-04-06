# A Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- **Type:** Phase II-E SBIR Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR 2016, Topic 04-8 0777 (Volcano monitoring)
- **Date:** 2016 (proposal for Phase II-E extension)
- **BST Products/Systems Referenced:** S2 XT, SwiftCore Flight Management System, SwiftPilot, SwiftTab UI, MultiScat (Multihole Probe/MHP)
- **Key Personnel:** Jack Elston (PI), Dr. Wardell (Science Lead), David Pieri (NASA Technical Monitor)

## Executive Summary
Black Swift Technologies proposes Phase II-E development of a Vertical Takeoff and Landing (VTOL) variant of the S2 XT unmanned aircraft system for volcanic sampling and atmospheric measurements in harsh environments. Building on successful Phase II completion of the S2 XT platform and payload integration, this extension aims to add VTOL capability with high-wind operation (up to 30 mph) and real-time data visualization, enabling deployment at volcanic sites worldwide with reduced ground infrastructure requirements.

## Technical Approach

### Core Development Objectives
1. **VTOL S2 XT Airframe Modification**
   - Add four rotors to existing S2 XT fixed-wing platform
   - Maintain 1-hour flight endurance target
   - Minimize added weight while preserving volcanic ash/precipitation durability
   - Remove catapult launch and belly-landing systems to reduce mass
   - Design for 20' x 20' takeoff/landing footprint

2. **High-Wind VTOL Landing Algorithm**
   - Hybrid control approach combining rotor thrust with fixed-wing aerodynamic surfaces
   - Utilize 3D multihole probe sensor (developed in Phase I/II) to keep aircraft pointed into wind
   - Maintain vertical descent rate sufficient to generate control authority from ailerons/elevator
   - Target capability for winds >30 mph (compared to typical VTOL aircraft limitation of 15 mph)
   - Implement on SwiftPilot autopilot with updates to SwiftTab tablet interface

3. **In-Flight Data Visualization**
   - Real-time telemetry display of multiple sensor channels for operator
   - Modular software architecture to support future sensor integration
   - Open-source ground-based visualization software for customer modification
   - Critical for scientist-directed sampling strategies

4. **3D Navigation with Terrain Awareness**
   - Dubin's curves-based path planning in 3D (Phase II achievement)
   - Automatic vertical spacing/segment insertion for terrain avoidance in mountainous environments
   - Five mission profile types for volcanic work: volumetric sampling, lava flow mapping, fissure measurement, ocean entry, background sampling
   - Intuitive UI parameter-based flight plan generation
   - XML scripting capability for non-expert UAS operators

## Products & Capabilities Described

### S2 XT Aircraft
- **What it is:** Ruggedized fixed-wing UAS designed for harsh environments (high altitude, volcanic ash, extreme temperatures)
- **Specifications:**
  - Operating temperature range: -40°C to +85°C
  - Altitude capable of high-altitude volcano operations
  - Pneumatic catapult launch and belly landing capability (removed in VTOL variant)
  - Sealed payload bay with rapid tool-free nose-cone swapping
  - Enhanced ingress protection vs. standard S2
- **Phase II accomplishments:**
  - Motor cowling with ferrous ash particle protection
  - Sealed nose cone with rapid payload access
  - Modular payload computer with geo-tagging and time synchronization
  - Successful deployments in Costa Rica, Greenland, Arizona, Hawaii
- **Phase II-E modifications:**
  - Four rotor addition for VTOL
  - 50% larger battery system
  - Redesigned carrying case (airline check-bag compatible)
  - Updated manufacturing and QC processes

### SwiftCore Flight Management System
- Autopilot platform supporting both fixed-wing and VTOL operation
- CAN protocol integration for rotor control via wing-mounted connectors
- Gazebo simulation environment for algorithm validation
- Water/dust-proof electrical connectors for field operations

### Multihole Probe (MHP)
- **Measurement capability:** 3D wind velocity, temperature, humidity
- **Specifications:**
  - Wind velocity range: up to 114 m/s
  - Temperature range: -40°C to +85°C
  - 3D-printed construction, custom sensor board
  - Low-cost, lightweight package
- **Application:** Real-time 3D wind sensing for high-wind VTOL control, keeping aircraft pointed into wind during descent
- **Phase II validation:** Bench-tested and compared with meteorological tower data (July 2018)

### Volcano Payload Integration
Comprehensive sensor suite integrated into custom S2 XT nose cone with geo-tagged, time-synced data logging:

| Sensor | Measurement | Range/Specs |
|--------|-------------|------------|
| BST 5-Hole Probe | Wind, temp, humidity | 0-114 m/s, -40 to +85°C |
| City Tech T3ST/F (×3) | SO₂ | 0-20, 0-200, 0-500 ppm |
| City Tech T3H | H₂S | 0-100 ppm |
| Particles Plus 8306 | Particle count | 0.3-25 µm |
| Sensair K30FR | CO₂ | 0-10,000 ppm |
| Sampling cassettes | In situ samples | 0.45 & 5 µm filters |
| MAPIR 14MP | Visible imagery | Geotagged, 3D terrain |
| FLIR Vue Pro R | Thermal IR | 640×480, up to 30 Hz |
| Airborne Innovations | Video | Real-time forward view |

**Payload computer features:**
- Single-board computer for sensor integration and data fusion
- Modular architecture for adding new sensors
- Payload independent field operation capability

## Use Cases & Applications

### Volcano Monitoring Missions
1. **Lava Flow Thermal Mapping**
   - High-resolution thermal IR with 3D visual overlay
   - Subsurface flow detection via lava tube identification
   - Pahoehoe breakout characterization and distribution tracking
   - Volume change calculation via before/after imagery
   - Phase II testing: 2014-2016 lava flow operations

2. **Fissure Sampling and Mapping**
   - Low-altitude mapping (70 m AGL)
   - Slow spiral ascent (0.5 m/s vertical rate) from 40-120 m AGL
   - Real-time gas sampling with onboard collection

3. **Plume Characterization and Ocean Entry**
   - Volumetric sampling across multiple altitudes (40, 80, 120 m AGL, 25 m spacing)
   - Sulfate-forming process characterization
   - Vog (volcanic smog) assessment
   - Near vs. distal, dawn/dusk vs. mid-day comparisons
   - Land-cover variation analysis

4. **Background/Baseline Sampling**
   - Diurnal multi-flight campaigns (early morning, midday, late)
   - Lava vs. vegetation comparison flights
   - Spiral patterns (40-120 m AGL, 0.5 m/s descent)

### Phase II Demonstrated Deployments
- **Turrialba Volcano, Costa Rica (January 2018):** CO₂ sampling during eruptive activity; validated ash tolerance
- **Southern Arizona (August 2018):** Landsat calibration in extreme heat; thermal design validation
- **Northern Greenland (2018):** Arctic atmospheric sampling; confirmed -40°C operation
- **NOAA Coastal Operations:** Two S2 XT systems with multihole probe for all-weather coastal monitoring
- **NASA Langley:** Flight training and asset acquisition
- **NASA JPL (SoOp):** Snow water equivalent measurement with P-band radiometer in mountain environments

### Phase II-E Planned Mission
**Makushin Volcano, Alaska (or backup: Hawaii):**
- VTOL demonstration in operational volcanic monitoring environment
- Real-time data visualization for scientist-directed sampling
- Demonstration of 20' × 20' launch/landing footprint
- Wind testing up to 30 mph (stretch goal: higher)
- Potential applications expansion to MALIBU project (Landsat calibration), SoOp (snow monitoring), NOAA ATD (atmospheric science)

## Key Results (Phase II Completion Status)

### Phase II Completed Milestones
1. **CONOPS Development & Automatic Mission Planning**
   - Five mission profile types formalized for volcanic work
   - 3D Dubin's curve-based navigation implemented
   - Automatic spiral/vertical spacing for terrain avoidance validated
   - Tested at Turrialba: improved vertical tracking and terrain clearance vs. legacy 2D navigation
   - XML mission scripting for non-expert operator input

2. **S2 XT Design & Validation**
   - Aircraft construction completed and flight-proven
   - Motor cowling protection validated against ferrous ash particles
   - Sealed payload integration with rapid field-swappable nose cone
   - Successful deployments across diverse environments (volcanic, arctic, desert, coastal)

3. **Sensor Payload Integration**
   - 12-sensor suite integrated and geo-tagged
   - Bench-tested trace gas calibration (CO₂ and SO₂ measurements validated)
   - Thermal camera and visible imagery systems operational
   - Modular payload architecture demonstrated

4. **Multihole Probe Development & Testing**
   - 3D-printed sensor design completed
   - Wind data validation performed vs. meteorological tower (July 2018)
   - Identified as key enabler for VTOL high-wind control

5. **Hawaii Flight Campaign (Scheduled August 31-November 2019)**
   - Flight permission obtained from JPL Safety and NASA Armstrong
   - Four mission types planned:
     - Lava flow thermal mapping (38 km, 120 m AGL, 35 min)
     - Fissure gas sampling (41 km, 70 m AGL, 38 min)
     - Ocean entry volumetric (70 km, 40-120 m AGL, 65 min)
     - Background diurnal sampling (multiple spirals)
   - Objectives: thermal IR/3D mapping, gas emission characterization, particulate sampling, ash/gas sample collection

### Commercial Traction
- Multiple S2 XT units sold to NASA centers and NOAA
- JPL ELEVATE campaign deployment (Costa Rica)
- Multihole probe used across multiple atmospheric campaigns
- Strong customer base for VTOL expansion (MALIBU, SoOp, NOAA ATD)

## Notable Details

### Technical Innovations
- **First-of-a-kind VTOL fixed-wing capability for high winds:** Hybrid rotor/fixed-wing landing approach with real-time 3D wind sensing and wind-pointing control exceeds typical VTOL aircraft wind limitations (15 mph → 30+ mph)
- **3D terrain-aware navigation:** Dubin's curves with automatic vertical spacing prevents terrain collision in mountainous volcanic environments
- **Rapid mission planning:** Intuitive UI-based volumetric sampling generation and XML scripting enables scientist-directed operations without UAS expertise
- **Modular sensor architecture:** Payload computer design allows future sensor integration without firmware rewrites

### Strategic Partnerships & Matching Funds
- **Creare:** Matching funds for VTOL SwiftCore avionics development; future NOAA aircraft design benefits
- **USGS:** Matching funds for Makushin Volcano Alaska flight campaign and sensor package modifications
- **NASA JPL:** ELEVATE campaign sponsorship (Costa Rica deployment); snow water equivalent monitoring partnership
- **NOAA ATD:** Two S2 XT systems purchased; atmospheric science operations
- **NASA Langley:** Aircraft acquisition and flight training use

### Market Positioning
- Addresses gap between satellite data (infrequent, cloud-masked, coarse resolution) and ground systems (limited coverage, stationary)
- Lower cost and repair risk than manned aircraft or large UAS
- Multi-aircraft deployment feasible for temporal/spatial coverage
- Specific design for harsh environments (volcanic ash, extreme temperatures, high altitude, precipitation) vs. off-the-shelf platforms
- VTOL variant eliminates pneumatic launcher requirement, expanding operational