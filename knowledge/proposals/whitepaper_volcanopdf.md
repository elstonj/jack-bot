# Volcano Monitoring with Unmanned Aircraft Systems (UAS)

## Document Metadata
- Type: White paper / capability brief
- Client/Agency: NASA (primary focus); implied audience includes aviation authorities, researchers
- Program/Solicitation: Not explicitly stated; context suggests NASA science missions and airspace safety initiatives
- Date: Created 2022-12-20; modified 2020-10-25
- BST Products/Systems Referenced: S2 UAS, SwiftCore (SwiftPilot, SwiftStation, SwiftTab), Multi-Hole Probe (MHP)
- Key Personnel: Jack Elston (CEO), Maciej Stachura (CTO)

## Executive Summary
This white paper presents the Black Swift S2 unmanned aircraft system as a purpose-built solution for collecting critical in situ data from volcanic plumes to improve aviation safety, advance volcano research, and validate atmospheric dispersion models. The S2 addresses a critical data gap in volcanic ash characterization—information that currently relies on limited ground sensors, dropsondes, and satellite observations—by enabling routine autonomous flights through harsh volcanic environments to measure gas composition, particle size distribution, and atmospheric properties.

## Technical Approach

**Core Problem Addressed:**
- Volcanic ash plumes present aviation hazards (e.g., 2010 Eyjafjallajökull eruption canceled 95,000 flights, $1.7B economic loss)
- Aircraft regulations limit ash ingestion to 0.2–4 mg/m³; airspace above this threshold is a no-fly zone
- Accurate ashfall advisories require high-quality in situ data that ground sensors and satellites cannot adequately provide
- Volcanic Ash Transport and Dispersion (VATD) models lack proper validation due to the hazardous nature of volcanic environments

**BST Solution:**
The S2 is a fixed-wing UAS engineered from inception for high-altitude flight through strong winds and damaging airborne particulates. Key design features:
- **Payload-centric design**: Large nose cone volume (20.3 cm diameter, 63.2 cm length) allows easy field integration and swapping of sensor suites
- **Autonomous operations**: Fully autonomous takeoff and landing (laser-guided belly landing), terrain-following flight
- **Rugged construction**: Designed for extreme environments, operating ceiling 4,500 m (15,000 ft)
- **Sensor-reactive flight patterns**: Real-time data feeds enable adaptive flight paths to follow plume dynamics
- **Rapid response**: Assembly and pre-flight checkout in <30 minutes

## Products & Capabilities Described

### Black Swift S2 UAS
**What it is:** A hand-launched or rail-launched fixed-wing unmanned aircraft system designed for atmospheric research in harsh environments.

**Specifications:**
- **Weight**: 5.2 kg nominal (6.6 kg max)
- **Wingspan**: 3.0 m (10 ft)
- **Payload capacity**: 2.3 kg (5 lbs) max with rail launch; 1.4 kg (3 lbs) hand launch
- **Flight ceiling**: 4,500 m (15,000 ft)
- **Flight speed**: 12 m/s stall (24 kts), 18 m/s cruise (35 kts)
- **Endurance**: 110 min max; 90 min nominal
- **Range**: 110 km (60 nm) max; 92 km (50 nm) nominal
- **Max wind endurance**: 15 m/s (30 kts)
- **Power available for payload**: 50 W total
- **Position accuracy**: <4 meters (geotagged)

**Proposed Use in Volcano Context:**
Autonomous flights into and around volcanic plumes to collect comprehensive scientific datasets. The aircraft carries multiple interchangeable sensor payloads for measuring:
- Trace gases: SO₂, CO₂, H₂S, CH₄
- Atmospheric parameters: pressure, temperature, humidity, 3D wind vectors
- Particulate matter: size distribution and concentration
- Remote sensing: high-resolution RGB and thermal (FLIR) imagery

**Payload Options Detailed:**

1. **Multi-Gas Sensor**: Measures SO₂, H₂S, CO₂ day/night
2. **Nephelometer**: Assesses volcanic particle size and distribution
3. **Particle Counter**: Six-channel real-time data at ground station (size bins: 0.3, 0.5, 1.0, 2.5, 5.0, 10.0 µm); user-selectable ranges
4. **Multi-Stage Filter Sampler**: On-demand air sampling with real-time sensor data to select timing/location; samples tagged with all payload and avionics data
5. **Pressure, Temperature, Humidity (PT&H) Sensor**: Critical for sensor corrections
6. **3D Wind Sensor (Multi-Hole Probe/MHP)**: Developed by BST; measures wind velocity aloft; critical for understanding plume movement and turbulence; addresses air speed as largest source of error in airborne flux measurements
7. **High-Resolution Color Camera (EO)**: Generates orthomosaics; can be rendered into 3D for change detection, volume calculations, hazard maps
8. **FLIR Thermal Camera**: Monitors volcanic unrest; can be combined with EO for visual overlays, feature analysis, hazard mapping; automated change detection for lava volume/inflation calculations
9. **Forward-Looking Real-Time Video**: Navigation, hazard avoidance, outreach

### SwiftCore Avionics
**What it is:** An integrated flight management system designed and manufactured entirely by BST in the USA (key differentiator vs. competitors using open-source avionics).

**Components:**

1. **SwiftPilot** (Autopilot)
   - "One of the smallest and most powerful autopilots commercially available"
   - Multiple dedicated CPUs with floating-point units (FPU) for autonomous functionality
   - Modularized CAN-bus hardware architecture supporting unlimited connectivity options (UART, I2C, SPI, CAN, Ethernet, USB, GPIO)
   - Enables fully autonomous flight from launch to landing
   - Advanced landing algorithm for robust, precise autonomous belly landings using laser landing system

2. **SwiftStation** (Ground Station)
   - Tripod-mounted, portable, customizable
   - Incorporates 900 MHz and GPS antenna
   - Expandable functionality via custom modules
   - Multiple radio options available

3. **SwiftTab** (User Interface)
   - Runs on Android tablets and smartphones
   - Intuitive gesture-based controls
   - Flight plans can be modified and uploaded mid-flight
   - Easy map and geo-referenced data import
   - Minimal training required

**Design Philosophy:** BST controls all critical components (electronics design, software, mechanical assembly, QC), ensuring quality and robustness unlike competitors relying on open-source or low-quality avionics.

### Multi-Hole Probe (MHP)
A tightly integrated probe and wind velocity measurement device designed by BST specifically for the S2. Provides 3D wind measurements critical to enhanced scientific missions and understanding plume dynamics.

## Use Cases & Applications

### Primary: Volcanic Monitoring
1. **Costa Rica (Turrialba Volcano)**: Flights conducted with S2 equipped with CO₂ sensors and atmospheric probes (pressure, temperature, humidity, 3D wind)
2. **Hawaii (Lower Puna Eruption, Fissure 8 location)**: Comprehensive study measuring:
   - Trace gas concentration (SO₂, CH₄, H₂S, CO₂)
   - Particulate size and distribution
   - Three-dimensional winds
   - Atmospheric thermodynamic values
   - RGB orthomosaic and thermal map
   - Atmospheric samples for lab analysis
   - 3D model of fissure and surrounding flow

**Results from Hawaii deployment:**
- Valuable background-level trace gas data in and around affected areas
- Surface temperature measurements, 3D maps, and orthomosaics constructed from camera data
- Comprehensive dataset supporting volcano research and aviation hazard response

### Secondary Applications Mentioned
- Arctic research: Snow/ice aerial measurements in extreme cold (-20°C), altitudes to 14,000 ft, Greenland water vapor studies
- Wildfire monitoring: Nighttime plume measurements, CO₂/CO/aerosol sampling, multispectral high-resolution mapping
- Soil moisture mapping: Up to 600 acres per flight using L-band radiometer
- CO₂ monitoring in volcanic regions: Ecosystem response studies in tropical environments
- Satellite instrument calibration: Landsat-8 OLI and S-NPP VIIRS validation with NASA Goddard
- Snow Water Equivalent (SWE) measurement: P-band reflective signals in mountainous environments
- Coastline monitoring: Thermal and hyperspectral payloads

## Key Results

**Hawaii (Lower Puna Eruption) Dataset:**
- Multi-parameter volcanic plume characterization
- Real-time sensor data enabling targeted sample collection
- High-resolution thermal and orthomosaic imagery
- 3D surface models for volume/change calculations
- Lab-analyzed atmospheric samples

**Operational Track Record:**
- S2 has been deployed multiple times for NASA missions
- Successfully completed NASA Airworthiness Flight Safety Review Board (AFSRB) and Flight Readiness Review Board (FRRB) six different times in two years prior to document creation
- Demonstrated ability to meet or exceed expectations of demanding clients
- Proven operations in wildland fire observation, hurricane monitoring, and mapping at altitudes exceeding 14,260 ft

**Technical Validation:**
- Demonstrated accurate measurement of volcanic gas plumes above volcanoes in close proximity to ground
- Safer and more repeatable than surface methods
- Novel sub-2.5 kg payload capability for sampling diverse atmospheric parameters simultaneously

## Notable Details

### Strategic Advantages
1. **NASA Partnership**: Demonstrated six successful AFSRB/FRRB completions, positioning BST as "a leading NASA partner for UAS development and flight testing"
2. **Vertical Integration**: Unlike competitors, BST designs and manufactures SwiftCore entirely in-house, controlling quality of critical components
3. **Consulting Services**: BST couples product sales with engineering consulting to government entities (NASA, NOAA, universities) and commercial customers
4. **Rugged Design Philosophy**: Aircraft explicitly engineered for harsh environments based on founder expertise in complex research missions (tornadic supercell intercepts, VORTEX2 campaign)

### Key Problem Solved
The paper emphasizes a critical scientific gap: Volcanic Ash Transport and Dispersion (VATD) models lack validation data because volcanic environments are too hazardous for traditional measurement methods. Nine Volcanic Ash Advisory Centers (VAAC) worldwide rely on these unvalidated models. The S2 provides the first practical means to collect in situ validation data through routine autonomous operations.

### Data Model Impact
Document notes that atmospheric models (weather, dispersion) drive:
- Volcanic ash aviation hazard warnings
- Pollution alerts
- Toxic release notifications
- Dust storm forecasts
- Wildfire smoke hazards

Improved in situ data collection from the S2 directly improves model accuracy and safety system reliability.

### Personnel Credentials
- **Jack Elston (CEO)**: Ph.D. from University of Colorado Boulder; doctoral work on meshed network UAS and control algorithms for tornadic supercell sampling
- **Maciej Stachura (CTO)**: M.S. and Ph.D. in aerospace engineering (CU Boulder); experience with 300+ flight experiments including first-ever tornadic supercell intercept

### Company Context
- Based in Boulder, CO
- Founded 2011
- All UAS products built on proprietary SwiftCore flight management system
- Business model includes both product sales and engineering services to government and commercial sectors