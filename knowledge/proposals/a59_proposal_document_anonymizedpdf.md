# ROSES 2023 On-demand Wildfire Susceptibility from Fuel Moisture and Vegetative Index Maps

## Document Metadata
- **Type:** NASA ROSES (Research Opportunities in Earth and Space Science) proposal
- **Client/Agency:** NASA (ESTO FireSense Program)
- **Program/Solicitation:** ROSES 2023, Topic NNH23ZDA001N-FIRET
- **Date:** Submitted 2023 (for projects starting 2024)
- **BST Products/Systems Referenced:** 
  - Soil Moisture Mapping UAS (fixed-wing and multirotor versions)
  - L-band radiometer soil moisture sensor
  - E2 UAS Flight Systems
- **Key Personnel:** 
  - PI (UAS expert, involved with soil moisture project since 2013)
  - Co-I/Science PI (Hydrologist, PhD on soil moisture and LFM at site)
  - Co-I #1 (Research scientist, field sampling expertise)
  - Co-I #2 (Microwave radiometry/radar specialist, algorithm lead for SMAP/NISAR)
  - Co-I #3 (L-band radiometer design and development lead)
  - Co-I #4 (Multi-aircraft UAS design and operations expert)

## Executive Summary
This proposal develops an integrated decision-making system combining UAS-based L-band soil moisture mapping with NASA satellite data (UAVSAR, NISAR) to provide near-real-time, high-resolution live fuel moisture (LFM) and soil moisture maps for wildfire management. The system will enable a single operator to fly up to 8 multirotor UAS simultaneously to cover 3,200 acres daily at 2m resolution, with broader coverage from satellite platforms, optimizing resource deployment for pre-fire situational awareness in California's wildfire-prone regions.

## Technical Approach

The proposal employs a multi-tiered, multi-platform approach:

### Platform Integration:
- **UAS Platform:** Quadrotor-based soil moisture mapping systems (slower flight speed at ~3m/s vs. fixed-wing at 18m/s enables longer integration time and better radiometer measurements through tree canopies; can fly at 15m altitude for 5m or better resolution)
- **Satellite Data:** P-band UAVSAR in Year 1; L-band NISAR satellite (6-day revisit) in Years 2-3
- **Swarm Operations:** Progression from 2 UAS (Year 1) → 4 UAS (Year 2) → 8 UAS (Year 3), all flown by single operator from ground station by Year 3

### Key Technical Objectives:

**Objective 1: Soil Moisture and Live Fuel Moisture Mapping**
- Develop algorithms to convert UAS-derived soil moisture anomaly maps to live fuel moisture (LFM) maps
- Build on prior pilot study (2021-2023) that demonstrated strong correlation between soil moisture and LFM across Chamise and other chaparral species at test site
- Deploy at highly instrumented 3,200-acre nature preserve with 40 active climate/soil stations measuring at 15-minute to hourly intervals to depths of 1m+ or bedrock
- Target: near-real-time, high-resolution maps integrated with current wildfire management systems

**Objective 2: Novel Sensor Platform**
- Miniaturize existing L-band radiometer sensor package for fixed-wing and multirotor UAS
- Develop autonomous flight planning with terrain-aware flight (terrain tracking and avoidance)
- Implement automated pre-flight checks and sensor setup
- Enable 8 UAS operation by single operator through improved autonomy and communications
- System must scale to cover 8 km² in one day at operational cost

**Objective 3: Onboard Soil Moisture Processing**
- Design new FPGA-based digital correlator for L-band radiometer with:
  - Real-time coherence matrix calculation
  - Better immunity to gain fluctuation
  - Self-calibration and real-time calibration capability
- Implement post-processing code onboard for real-time soil moisture calculation
- Enable self-checks on each aircraft (remove non-functioning sensors mid-mission)
- Support re-tasking capability based on live data

**Objective 4: Intelligence Tasking and Data Fusion**
- Use NISAR satellite soil moisture data (global, 6-daily) and UAVSAR (20×60 km coverage) to identify high-risk areas
- Develop algorithms to fuse multi-resolution data (2m UAS, 6m UAVSAR, 200m NISAR)
- Employ L-band forward models ("data cubes") with three axes: dielectric constant, surface roughness, vegetation water content (VWC)
- Implement least-squares soil moisture retrieval algorithm developed for SMAP SAR, extended to P-band (UAVSAR) and L-band (NISAR)
- Direct UAS swarm to priority coverage areas based on satellite data

## Products & Capabilities Described

### Soil Moisture Mapping UAS
- **Fixed-wing version:** Higher altitude operation; 18 m/s flight speed; ~8x more efficient at area coverage
- **Multirotor version (Primary for this project):** 
  - Lower altitude capable (15m AGL for 5m resolution)
  - 3 m/s flight speed
  - Better measurement integration and canopy penetration
  - Instrument package weight: 1.5 kg
  - Power draw: <50W
  - Proven in 100+ operational flights with government agencies, universities, commercial partners

### L-Band Radiometer Sensor
- Originally developed under NASA SBIR program
- Measures L-band brightness temperature
- Integrated with auxiliary sensors for soil type/surface property characterization
- Current version: under improvement with new digital correlator and onboard processing capability
- Demonstrated accuracy: strong agreement with in-situ sensors, even through moderate forest canopy (Figure 9 in document)

### Soil Moisture Data Products
- Resolution: 2m (UAS), 6m (UAVSAR), 200m (NISAR)
- Output formats: HDF, GeoTIFF
- Data volume estimates: 
  - UAS soil moisture maps: 10 GB/year (from 192 flights/year)
  - NISAR soil moisture maps: 6 GB for 6-day interval coverage (from Oct 2025 onward)
  - UAVSAR soil moisture maps: 0.3 GB for 9 flights in Year 1

### Live Fuel Moisture (LFM) Maps
- Derived from soil moisture anomaly maps using species-specific relationships
- Validated against field samples of Chamise and other species
- Prior testing showed high correlation (Figures 4-5)
- Can be generated in near-real-time onboard UAS
- Formats compatible with wildfire management systems

## Use Cases & Applications

### Primary Use Case: Pre-Fire Wildfire Management
- **Situational Awareness:** Rapid characterization of fuel moisture conditions before ignition
- **Controlled Burn Planning:** Provide real-time data to support scheduled controlled burns at test site; inform decisions on fuel loads, timing, and extent
- **Response Readiness:** Enable rapid data collection in response to ignition sources
- **Landscape Management:** Support coordination between state/local agencies and land managers on best practices to decrease fire risk

### Test Site
- 3,200-acre (8 km²) nature preserve in California's fire-prone region
- Existing infrastructure: 40 monitoring stations, extensive vegetation/soil/climate measurements
- Active fuel management: mechanical thinning, prescribed burns
- Ideal for validation: co-located ground truth data

### Geographic Scope
- Focus: California northern coastal mountains and western US fire-prone landscapes
- Extended application potential: broader wildland/fire management community
- Operates within scope of NASA FireSense project goals

### Secondary Applications (Year 3)
- Fire perimeter detection using NISAR disturbance product and L-band data during controlled burns
- Post-fire monitoring capability demonstration

## Key Results (Prior Pilot Study, 2021-2023)

The proposal builds on successful preliminary work at the proposed site:

### Data Collection
- Four deployments with fixed-wing and multirotor UAS
- Over 900 mobile Time Domain Reflectometry (TDR) soil moisture measurements across three seasonal campaigns
- LFM field samples from tree and chaparral species coincident with flights
- Comparison against 40 in-situ monitoring stations

### Demonstrated Capabilities
- Soil moisture mapping accuracy through moderate forest canopy
- Strong correlation between soil moisture and LFM (Figure 4):
  - Tested across Chamise (primary indicator species for fire danger) and other chaparral species
  - Linear relationships enabling conversion to LFM maps (Figure 5)
- Successful refinement of hardware/software across iterations:
  - Implemented slope correction algorithm for steep terrain
  - Expanded temperature envelope for high-heat operation
  - Developed new thermal calibration technique
  - Created quadrotor UAS version for low-altitude, slow-speed operations
  
### Final Campaign Results (Figure 9)
- Very good correlation between UAS and in-situ data
- Demonstrated mapping capability even through moderate forest canopy
- Single flight validation showed reliable soil moisture retrieval

## Work Plan and Schedule

### Year 1 (Oct 2024 - Sept 2025)
**Risk Retirement Focus**

**Task Y1-1:** Kickoff and Planning (project management, sub-contracts)

**Task Y1-2:** Live Fuel Moisture Mapping (develop tools to process/deliver soil moisture and LFM maps; integrate with wildfire management systems)

**Task Y1-3:** Flight Campaign #1 (2-week deployment; high-resolution L-band UAS mapping of entire 3,200-acre site; field measurements; three UAVSAR flights)

**Task Y1-4:** Onsite Soil Moisture Calculation (implement edge computing for field processing without connectivity)

**Task Y1-5:** Flight Campaign #2 (two UAS flown simultaneously by two pilots; in-situ data collection)

**Task Y1-6:** Multi-UAS Integration (UI, communications, planning software development for 8-UAS operation; simulation demonstration)

**Task Y1-7:** Flight Campaign #3 (two UAS flown by one operator from single ground station; three UAVSAR flights)

**Milestones:** Fuse UAS/UAVSAR P-band data; LFM mapping operational; onsite soil moisture calculation demonstrated; 2-UAS single-operator flight proved

### Year 2 (Oct 2025 - Sept 2026)
**Expansion and Satellite Integration Focus**

**Task Y2-1:** NISAR Data (process NISAR soil moisture data for past campaigns; validate against in-situ/UAS/UAVSAR)

**Task Y2-2:** Flight Campaign #4 (four UAS by two pilots; double coverage area; in-situ data)

**Task Y2-3:** Terrain Planning and Following (automated flight planning; sensor-feedback autonomous terrain avoidance)

**Task Y2-4:** Flight Campaign #5 (four UAS by two pilots with autonomous terrain avoidance)

**Task Y2-5:** Onboard Brightness Calculation (implement real-time L-band brightness temperature processing onboard)

**Task Y2-6:** Flight Campaign #6 (four UAS by one operator; test onboard L-band processing; in-situ data)

**Milestones:** NISAR soil moisture data integrated into decision-making; 4-UAS single-operator flight achieved; real-time brightness temperature onboard

### Year 3 (Oct 2026 - Sept 2027)
**Operational Demonstration Focus**

**Task Y3-1:** UAS Directed by NISAR (develop tools to classify priority coverage areas)

**Task Y3-2:** Flight Campaign #7 (eight UAS by two pilots with NISAR-based prioritization; in-situ data)

**Task Y3-3:** Real-time Soil Moisture Mapping (implement onboard soil moisture product calculation; enable science-directed flight)

**Task Y3-4:** Flight Campaign #8 (eight UAS by one pilot; integrate with wildfire management partners; provide data to burn boss; inform prescribed burn planning)

**Task Y3-5:** Live Fuel Moisture Data Product (continued validation, calibration, delivery optimization)

**Task Y3-6:** Flight Campaign #9 (repeat Campaign #8 with improvements based on burn boss feedback)

**Task Y3-7:** Final Report

**Final Deliverables:** Full 8-UAS single-operator system operational; maps generated within 30 minutes of