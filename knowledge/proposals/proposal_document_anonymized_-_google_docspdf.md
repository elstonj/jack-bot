# ROSES 2023 On-demand Wildfire Susceptibility from Fuel Moisture and Vegetative Index Maps

## Document Metadata
- **Type:** NASA ROSES 2023 research proposal
- **Client/Agency:** NASA (Earth Science Technology Office - FireSense program)
- **Program/Solicitation:** ROSES 2023 Fire and Earth Science Technology (FIRET) - Topic NNH23ZDA001N-FIRET
- **Date:** Submitted May 2024 (cover page date)
- **BST Products/Systems Referenced:** Soil Moisture Mapping UAS (fixed-wing and multirotor versions with L-band radiometer)
- **Key Personnel:** 
  - PI (UAS expert, soil moisture project lead since 2013)
  - Co-I/Science PI (Hydrologist, PhD on soil moisture and live fuel moisture at test site)
  - Co-I #1 (Research scientist, field sampling expertise)
  - Co-I #2 (Microwave radiometry and radar specialist, SMAP SAR and NISAR algorithm lead)
  - Co-I #3 (L-band radiometer design expert, leads instrument development)
  - Co-I #4 (Multi-aircraft UAS design expert, flight operations, FAA COA authority)

## Executive Summary

This proposal presents a multi-year effort to operationalize near real-time soil moisture and live fuel moisture mapping for wildfire management. The system integrates a swarm of up to 8 multirotor UAS equipped with L-band radiometers (capable of mapping 3,200 acres at 2m resolution in one day) with satellite data from NASA's UAVSAR (P-band) and NISAR satellite (L-band) to provide tiered coverage from high-resolution tactical data to wide-area strategic guidance. Key innovations include onboard soil moisture computation, autonomous multi-UAS coordination by a single pilot, and intelligent tasking of the UAS swarm based on satellite moisture anomalies.

## Technical Approach

### Core Strategy
The proposal employs a hierarchical sensing architecture:
1. **Wide-area guidance:** NISAR satellite (6-day global revisit) and UAVSAR airborne radar (20×60 km footprints) provide regional soil moisture maps at 200m and 6m resolution
2. **Intelligent tasking:** Satellite data is analyzed to identify high-risk areas (moisture anomalies, gaps) where the UAS swarm should concentrate coverage
3. **High-resolution tactical data:** Multirotor UAS equipped with L-band radiometer fly at ~15m altitude to achieve 2m resolution soil moisture maps; data is processed onboard and converted to live fuel moisture (LFM) via plant-type specific algorithms
4. **Data fusion:** All three platforms' data are fused to create enhanced products at decision-making scale

### Technical Innovations

**Objective 1: Soil Moisture and Live Fuel Moisture Mapping**
- Use L-band brightness temperature measured by UAS radiometer to compute soil moisture at 2m spatial resolution
- Develop robust relationships between soil moisture anomalies and live fuel moisture for key plant species (e.g., Chamise chaparral)
- Generate near real-time, plant-type-specific LFM maps as input to fire danger assessment
- Validation against 40 ground stations (15-minute to hourly measurements to 1m depth or bedrock) and field-collected TDR measurements (900+ samples across three seasonal campaigns) and LFM samples

**Objective 2: Novel Sensor Platform**
- Operate 8 multirotor UAS simultaneously from a single ground control station (one operator)
- Justification for multirotor: 
  - **Height constraint:** Radiometer antenna requires ~15m AGL to achieve 5m spatial resolution in mountainous terrain; fixed-wing cannot safely maintain such low altitude
  - **Integration time:** Slower speed (3 m/s vs. 18 m/s) allows longer radiometer integration, improving accuracy and enabling measurement through sparse canopy
  - **Trade-off solution:** Use 8 multirotors to match fixed-wing efficiency (8× the area covered per aircraft)
- Enable single-pilot operation through:
  - Automated mapping flight plans with terrain-based route planning
  - Active terrain tracking and collision avoidance
  - Automated pre-flight checks and sensor configuration
  - FAA and NASA certification for multi-UAS operations

**Objective 3: Onboard Soil Moisture Computation**
- Upgrade L-band digital correlator using FPGA for real-time coherence matrix calculation with improved gain stability and self-calibration
- Implement post-processing algorithms onboard each UAS to compute brightness temperature and soil moisture in real-time
- Benefits:
  - Reduces processing latency from several hours to near real-time
  - Enables per-aircraft health checks (detect/isolate non-functioning sensors mid-flight)
  - Allows adaptive re-tasking (lower altitude for higher resolution in high-risk areas identified in real-time)
  - Reduces data management overhead for multi-aircraft operations

**Objective 4: Intelligence Tasking and Data Fusion**
- Use NISAR (6-day revisit after 2025) and P-band UAVSAR (Year 1 testing) to generate root-zone soil moisture maps
- Implement L-band retrieval algorithm developed for SMAP SAR, extended to P-band
- Algorithm approach: Minimize difference between modeled and observed dual-pol radar backscattering (σ0) using 3-axis lookup tables (data cubes: dielectric constant, surface roughness, vegetation water content)
- Classification of satellite data identifies high-risk areas → intelligent tasking of UAS swarm to prioritize coverage
- Cross-platform validation: compare UAS, UAVSAR, and NISAR soil moisture estimates to confirm consistency before operationalizing intelligent tasking

## Products & Capabilities Described

### Soil Moisture Mapping UAS (Primary System)

**Fixed-Wing Version:**
- Mass: 2.2 kg (sensor package only)
- Power draw: <50W
- Altitude: 100+ m (fixed-wing requirement)
- Flight speed: 18 m/s
- Flight time: Longer than multirotor
- Use case: Wide-area coverage (used in pilot study; found insufficient for this application due to altitude/terrain constraints)

**Multirotor Version (Primary for this project):**
- Mass: 1.5 kg (sensor package)
- Power draw: <50W
- Altitude: ~15m above ground (variable terrain)
- Flight speed: 3 m/s
- Spatial resolution: 2m (due to low altitude and long integration time)
- Sensor: L-band radiometer with auxiliary thermal/NDVI sensors
- Data output: Brightness temperature, soil moisture, converted to live fuel moisture maps
- Operational capability: 8 aircraft flown simultaneously by one pilot (end of Year 3)

**Radiometer Specifications:**
- Frequency: L-band (1.4 GHz)
- Measurement: Brightness temperature via two-channel design (VV and HH polarization inferred)
- Processing: Digital correlator with FPGA (new design proposed)
- Calibration: Real-time and self-calibration capability
- Auxiliary inputs: Soil type, surface properties (roughness), plant water content

**Flight Performance (Target):**
- Coverage area: 3,200 acres (8 km²) in one day with one operator
- Resolution: 2m soil moisture maps
- Temporal latency: Maps generated within 30 minutes of landing (end of Year 3)

### Satellite Data Integration

**UAVSAR (Year 1)**
- Frequency: P-band (< L-band, penetrates deeper)
- Resolution: 6m soil moisture retrievals
- Function: Test utility of root-zone soil moisture for fire prediction; inform algorithm extension
- Campaign: Three flights planned in Year 1

**NISAR Satellite (Years 2-3)**
- Frequency: L-band
- Revisit: 6 days (ascending + descending combined)
- Resolution: 200m soil moisture maps (global coverage)
- Function: Identify wide-area moisture anomalies and gaps to task UAS swarm
- Disturbance product: Planned use in Year 3 to identify fire perimeters during controlled burns
- Status: Upcoming mission (NASA NISAR scheduled for deployment)

## Use Cases & Applications

### Primary Application: Wildfire Pre-Fire Preparedness
- **Controlled burn planning:** Provide soil moisture and LFM data to land managers 2-3 days before planned controlled burns to optimize fuel reduction (burns more effective at certain moisture ranges)
- **Ignition response:** Rapid assessment of fuel moisture in areas of reported ignition to determine suppression resource requirements
- **Fire danger rating:** Integrate soil moisture and LFM into existing fire danger models (currently under-utilized due to lack of on-demand data)
- **Pre-positioning resources:** Decision support for placement of fire crews and equipment based on high-risk areas identified by satellite data

### Test Site
- **Location:** 3,200-acre nature preserve with extensive instrumentation
- **Existing infrastructure:** 40 active climate and soil stations (15-minute to hourly measurements), tree moisture sensors, established fuel management program (mechanical thinning, prescribed burns)
- **Validation assets:** 900+ field TDR soil moisture measurements, live fuel moisture samples from multiple species (Chamise, oak, etc.)
- **Management partners:** NGO focused on fire resilience; coordination with state/local agencies
- **Terrain:** Mountainous, chaparral/mixed forest with variable canopy

### Geographic Applicability
- **Focus area:** California's northern coastal mountains and western US fire-prone regions
- **Terrain challenges:** Steep slopes requiring terrain-aware flight planning
- **Vegetation:** Chaparral, mixed oak-conifer forests with variable canopy density
- **Scalability:** System designed to expand from test site to regional/multi-regional deployment

## Key Results (Pilot Study, 2021-2023)

The proposal builds on a successful pilot study involving four field deployments:

**Soil Moisture Mapping Accuracy:**
- Strong agreement between UAS-derived soil moisture maps and in-situ station data (Figure 9 shows excellent correlation)
- Successful measurement through sparse tree canopy (multirotor advantage)
- Seasonal validation across three campaigns (dry, intermediate, wet conditions) with 900+ TDR validation points

**Soil Moisture to Live Fuel Moisture Relationship:**
- High correlation demonstrated between soil moisture anomaly and measured LFM for three chaparral species (Figure 4)
- Conversion algorithm developed enabling LFM map generation from soil moisture retrievals (Figure 5 shows LFM maps for three dates)
- Relationship validated against field-collected samples from key indicator species (Chamise)

**System Improvements Implemented During Pilot:**
- Slope correction algorithm for steep terrain accuracy
- Thermal hardware redesign for hot climate stability (expanded temperature envelope)
- Thermal calibration technique refinement
- Quadrotor platform development (not previously in UAS family)

**Operational Validation:**
- 100+ operational flights completed (outside this project) for government agencies, universities, and commercial partners
- Performance demonstrated in watershed studies and other Earth science applications

## Work Plan & Timeline

### Year 1 (Oct 2024 – Sep 2025): Risk Retirement & Core Capability
**Tasks:**
- Y1-1: Kickoff, planning, and subcontract setup
- Y1-2: Develop live fuel moisture processing tools; improve based on partner feedback
- **Y1-3: Flight Campaign #1** – High-resolution mapping of entire site over 2 weeks; three UAVSAR P-band flights; extensive field sampling (soil moisture, leaf moisture, tree moisture)
- Y1-4: Implement onboard soil moisture computation using edge computing (enable processing in field without connectivity)
- **Y1-5: Flight Campaign #2** – Two UAS flown simultaneously by two pilots; field sampling continued
- Y1-6: Multi-UAS integration development (UI, communications, planning software); simulation demonstration of 8-UAS command and control
- **Y1-7: Flight Campaign #3** – Two UAS operated by one pilot from single ground station; three UAVSAR flights

**TRL Targets:**
- Live fuel moisture mapping: TRL 5→6 (advance prototype demonstrated in pilot to flight-proven in relevant environment)
- L-band radiometer with onboard processing: TRL 4→7 (operational flights by Year 3)
- Multi-UAS autonomy: TRL 4→7 (operational flights by Year 3)
- P-band UAVSAR soil moisture: TRL 5→6 (demonstrated in proven environment)

###