# A Ruggedized UAS for Scientiﬁc Data Gathering in Harsh Environments

## Document Metadata
- Type: NASA CCRPP (Commercialization/Collaborative Research & Development) Proposal
- Client/Agency: NASA Ames, NOAA (two groups), USGS
- Program/Solicitation: NASA CCRPP; References NASA SBIR Phase II-e (Contract NNX17CP13C)
- Date: 2022 (Proposal Number 2022-1-1118)
- BST Products/Systems Referenced: S2, S2-VTOL, S0, SwiftCore Flight Management System (FMS), SwiftPilot autopilot, SwiftTab user interface, SwiftFlow Probe, E2 multirotor, S1 surveying sUAS
- Key Personnel: Dr. Jack S. Elston (Principal Investigator), Dr. Maciej Stachura (Lead Engineer), Josh Fromm (Mechanical Engineering Lead)

## Executive Summary
This CCRPP proposal describes Black Swift Technologies' plan to mature and commercialize advanced small UAS platforms (S2 and S0) with enhanced autonomous flight capabilities for scientific data gathering in extreme environments. Building on successful Phase II-e SBIR work that demonstrated volcanic observation missions, the proposal outlines development of intelligent wind-aware flight planning, advanced mission planning for terrain/communications constraints, improved scientific data interfaces, and cost-reduced manufacturing for the S2-VTOL to meet urgent operational needs from NASA, NOAA, and USGS for volcano monitoring, hurricane sampling, and soil moisture mapping.

## Technical Approach

### Core Technologies & Systems
**S2 Aircraft (Fixed-Wing):**
- Category 1 UAS with gross takeoff weight <55 lbs including payload
- Payload capacity: up to 5 lbs
- Endurance: minimum 1 hour
- Designed for 15 km diameter observation circles
- Operates BVLOS; approved for beyond-visual-line-of-sight missions
- Recently demonstrated 20-mile range over terrain

**S2-VTOL (Vertical Takeoff & Landing variant):**
- New prototype developed in Phase II-e
- Enables launch/landing from small or obstacle-dense areas
- Greatly expands operational envelope
- Primary focus for manufacturability improvements (target: 30% cost reduction)
- Target price point: ~$40,000

**S0 Aircraft (Smaller, Disposable/Expendable):**
- Smaller than S2, designed for air-deployment from manned aircraft
- Used for hurricane observations
- Unrecoverable/expendable technology for severe storm environments
- Capable of multi-hour duration
- Requires 150+ nautical mile command & control range

### Avionics & Flight Management
- **SwiftCore FMS:** Connects up to 128 unique sensors; logs diverse data types to onboard storage
- **SwiftPilot autopilot:** Autonomous flight capability
- **SwiftTab user interface:** Ground control station interface for mission planning and real-time data visualization
- Iridium communications integration as backup to primary data link

### Key Technical Development Tasks (CCRPP Work)

**1. Intelligent Flight in Strong Winds**
- Feasible flight path algorithms that calculate navigable routes in extreme winds
- Uses a priori mesoscale models + in-situ wind measurements
- Onboard execution for real-time adaptation
- Machine-learning based flight-time prediction incorporating:
  - 3D wind estimates
  - Measured power consumption
  - Real-time battery reserve calculations
  - Safe return-to-base margin
- Direct application to S0 hurricane missions and S2-VTOL volcanic surveys

**2. User Interface Improvements for Scientific Data**
- Generic sensor data visualization interface on SwiftTab
- Real-time plotting of payload data (time series and geographic mapping)
- Support for ~20 different payloads BST has developed
- Enable operator/scientist adjustment of flight paths to maximize scientific return

**3. Advanced Mission Planning**
- Terrain-aware flight planning using digital elevation maps
- Communication coverage prediction (radio line-of-sight models)
- Integration of terrain knowledge with aircraft performance models
- Safe terrain avoidance while enabling close-range monitoring
- Lost-communication contingency planning that avoids terrain

**4. Manufacturing & Cost Reduction**
- Improved manufacturability processes for S2-VTOL
- Design simplifications to reduce build time
- Target: 30% cost reduction; achieve $40,000 price point

## Products & Capabilities Described

### S2 (Primary Scientific Platform)
- **What it is:** Ruggedized fixed-wing sUAS (<55 lbs) designed for harsh environments
- **Use in proposal:** Primary platform for volcano monitoring, soil moisture mapping, and weather observation; foundation for VTOL variant
- **Specifications:**
  - 1+ hour endurance
  - 15 km diameter survey capability
  - 5 lb payload capacity
  - BVLOS approved; demonstrated 20-mile range
  - Operates in extreme winds, downdrafts (tested to >40 kts headwinds, 2000 fpm downdrafts)
  - Temperature rated to -40°C
  - Proven photogrammetry and trace gas measurement
  - Modular field-swappable payload nose cones

### S2-VTOL
- **What it is:** VTOL variant of S2 in prototype form (started Phase II-e)
- **Advantages:** Vertical takeoff/landing capability for deployment from small/obstacle-dense areas
- **Use in proposal:**
  - Primary system for NASA Ames volcanic observation
  - Expanded operational envelope for diverse missions
  - Focus for cost reduction efforts
  - Target commercial price: $40,000

### S0 (Smaller/Expendable UAS)
- **What it is:** Smaller disposable/expendable UAS for air-deployment
- **Use in proposal:**
  - NOAA hurricane sampling missions
  - Deployed from NOAA WP-3D manned aircraft
  - Intended for operations in tropical cyclones/severe storms
  - Unrecoverable technology concept
- **Specifications:**
  - Multi-hour duration target
  - 150+ nautical mile C2 range requirement
  - Continuous meteorological/oceanographic data collection
  - Wind-navigation techniques being developed for enhanced success

### Payload Suites (Modular)

**Volcanic Gas Monitoring:**
- LICOR CO2/H2O analyzer
- CityTech electrochemical SO2 and H2S sensors
- Upward-looking DOAS spectrometer
- Spectrometer with collimating optics
- Pressure, temperature, humidity sensors
- Real-time streaming capability

**Photogrammetry/EO-IR:**
- 24 MP RGB camera (primary)
- FLIR Vue Pro R thermal camera (downward-facing)
- Extra battery for extended flight time
- Produces 3D models, orthomosaics, thermal overlays

**Soil Moisture Mapping:**
- Lobe Differencing Correlation L-band Radiometer (LDCR) (provided by customer)
- Surface imaging sensors (RGB)
- BST SwiftFlow Probe (wind/thermodynamic data)

**Communications:**
- Iridium backup package integrated with ground station and aircraft

### SwiftCore FMS & SwiftPilot
- Multi-sensor architecture (up to 128 sensors)
- Diverse data logging
- Autonomous flight capability
- Modular design enabling rapid payload customization

### SwiftFlow Probe
- Multi-hole turbulence probe for 3D wind measurement
- Provides atmospheric data
- Lower cost and weight vs. competing systems
- Improved measurement accuracy

## Use Cases & Applications

### 1. Volcanic Observation & Trace Gas Monitoring
**NASA Ames Earth Science Division Primary Mission:**
- Volcanic flux monitoring using trace gas sensors
- CO2, SO2, H2S measurements over volcanic vents
- Photogrammetry mapping of calderas
- Mission: Makushin Volcano, Alaska (Phase II-e deployment)
  - 4 missions completed September 2021
  - 20-mile BVLOS flights with 7,000 ft altitude gain
  - Encountered >40 kt headwinds, 2000 fpm downdrafts
  - Only successful visual observations of volcano that year
- Planned Costa Rica deployment March 2022 with S2-VTOL
- Applications: volcanic ash detection, aviation safety hazard monitoring, plume dispersion analysis

### 2. Hurricane & Tropical Cyclone Sampling
**NOAA Primary Mission:**
- In situ meteorological and oceanographic data collection in boundary layer
- Air-deployed from NOAA WP-3D
- Missions into severe turbulent tropical cyclones
- Requirements: 150+ nautical mile C2 range, multi-hour duration, expendable concept
- Wind-navigation algorithms critical for reaching sampling areas when direct flight impossible
- Data supports hurricane evolution forecasting

### 3. Soil Moisture Mapping in Complex Terrain
**NOAA SPLASH (Study of Precipitation, Lower Atmosphere, Surface for Hydrometeorology):**
- Deployment: East River Basin, Colorado (north of Crested Butte)
- Coverage: ~10 km² mountainous terrain
- Mission duration: 7 week-long flight campaigns (May-August snow melt through late summer)
- Payload: LDCR radiometer + RGB imaging + wind probe
- Data recipients: National Weather Service Colorado River Basin Forecast Center (CRBFC), Grand Junction WFO
- Terrain-aware flight planning critical for low-altitude radiometer performance
- In-situ soil moisture sensor co-location for retrieval validation

### 4. Wildfire Monitoring & Support
- Identified as secondary NASA market opportunity
- Operate in environments with volcanic ash-like particulates and severe turbulence
- One prior mission with NCAR using NOAA support; additional missions planned

### 5. Weather Observation & Model Validation
- 3D in-situ atmospheric measurements (temperature, pressure, humidity, winds)
- Validation of small-scale dynamic phenomena in weather models
- Tornado/supercell thunderstorm development studies
- Applicable to S2 and S0 platforms
- Reduced operational overhead vs. manned aircraft

### 6. Remote Sensing in Difficult Areas
- Emergency rapid deployment to hazardous/remote locations
- Low planning overhead
- BVLOS capability for areas 20+ miles from launch site
- Future wildfire emergency response

## Key Results (Phase II-e Validation)

### Makushin Volcano Mission (September 2021)
**Flight 1 (Sept 10):**
- Photogrammetry payload
- 6,500 ft altitude reached
- Strong downdrafts during ingress caused higher power usage
- Aircraft returned conservatively with 3.2x required battery reserve
- Validated 15-mile wireless communication range
- Validated BVLOS safety procedures
- All 3 onboard sensors (video, RGB, thermal) functional

**Flight 2 (Sept 11):**
- Photogrammetry payload
- Encountered >40 kt headwind + strong downdraft unable to climb through
- Aircraft autonomously detected dangerous conditions and returned
- 25% lower power consumption than Flight 1
- Validated autonomous safety response

**Flight 3 (Sept 12):**
- Photogrammetry payload
- Elevated ingress path to avoid downdrafts
- Completed primary goal: full 1 km² thermal/visible map of summit
- Produced 3D model and orthomosaic with thermal overlay showing hot spots/vents
- Imaged active hydrothermal area (Upper Makushin Valley) in single swath
- Validated sustained performance in strong winds

**Flight 4 (Sept 12):**
- Trace gas payload (first flight with gas sensors)
- Equipment: LICOR CO2/H2O, CityTech SO2/H2S, DOAS spectrometer
- Encountered significant downdraft (up to 2000 fpm descent at full throttle)
- Aircraft autonomously returned due to insufficient thrust; maintained >1000 ft AGL
- Validated gas calibration procedures and real-time data streaming
- All gas sensors within specification post-flight

### Key Findings:
- S2 demonstrated only visual observations of Makushin during entire 2021 calendar year
- Flight planning (months of preparation) and in-flight wind observations critical to mission success
- Automation needed for routine operations
- Significant power consumption variability in downdraft areas (Figure 5: double predicted power in downdraft sections)
- Aircraft autonomously responds to dangerous wind/downdraft conditions