# 1132024 Technical Grant Document for Orphaned Wells Methane Detection

## Document Metadata
- **Type:** Grant proposal / Technical application
- **Client/Agency:** U.S. Department of Energy - Fossil Energy and Carbon Management (DOE FECM)
- **Program/Solicitation:** Not explicitly stated; appears to be DOE grant application related to orphaned oil and gas wells
- **Date:** November 5, 2024 (draft for internal review)
- **BST Products/Systems Referenced:** 
  - Black Swift S2 (Fixed-wing UAS)
  - Quanta3 methane sensor payload
  - FluxMapper™ software (data analysis)
- **Key Personnel:** 
  - Dr. Saeed Salehi (PI, petroleum engineer)
  - Dr. Ken Mischwaner (atmospheric scientist)
  - Dr. Maciej Stachura (aerospace engineer)
  - Dr. Jack Elston (aerospace engineer, drone expertise)
  - Dr. Sebastien Biraud (methane expert, advisor)
  - Beck Cotter (last editor)
  - Review by: Ken, Stefan, Jack

---

## Executive Summary

This proposal aims to advance methane detection and quantification technologies from TRL-5 to TRL-6 for monitoring emissions from orphaned and abandoned oil and gas wells across the U.S. (estimated 310,000-800,000 wells). The project integrates Black Swift Technologies' S2 fixed-wing drone with Quanta3 methane sensors, LI-COR eddy covariance tower systems, novel FluxMapper™ software for geospatial emission tracking, and remote connectivity systems (HOO-nah device from Hyde Park West Telecommunications) to enable continuous, real-time monitoring of methane emissions from orphaned wells, with a focus on detecting emissions as low as 0.2-0.4 kg/hour over a 3-year study period.

---

## Technical Approach

### Overall Strategy
The proposal employs a multi-method, comparative approach to methane detection:

1. **Drone-Based Aerial Surveys** (Aim 1): Black Swift S2 UAS with Quanta3 methane sensor performing eddy covariance analysis during ~50 flights over 3 years at identified orphaned well sites in Colorado
2. **Tower-Based Continuous Monitoring** (Aim 2): LI-COR eddy covariance system deployed for 6-month periods at 3 sites (2 months per site) in Year 2
3. **Software Enhancement** (Aim 3): FluxMapper™ geospatial flux analysis software to convert eddy covariance measurements into spatially-georeferenced emission maps with 0.2 kg/hour sensitivity
4. **Remote Connectivity** (Aim 4): HOO-nah device and Hyde Park West Telecommunications systems for real-time data transmission from remote well sites

### Key Technical Details

**Eddy Covariance Methodology:**
- Combines high-frequency methane concentration data (2 Hz or 10 Hz) with simultaneous wind speed/direction measurements
- Calculates methane flux by tracking atmospheric eddies and covariance of CH₄ concentration with vertical wind velocity
- Enables both plume inversion analysis (near-field, <100 m) and far-field Gaussian plume integration over hours

**Black Swift S2 System Specifications:**
- Flight endurance: up to 90 minutes
- Wingspan: 3 meters
- Payload capacity: 2 kg
- Operational capability: extreme environments, high winds, low temperatures
- Quanta3 sensor sensitivity: 2 ppb (parts per billion)
- Quanta3 sampling frequency: 2 Hz
- Quantification range: detects leaks down to 0.4 kg/hour with eddy covariance analysis

**LI-COR Methane System Specifications:**
- Instrument: LI-7700 open-path laser analyzer
- Operating principle: Wavelength Modulation Spectroscopy (WMS) at near-infrared frequencies
- Precision: 5-10 ppb at 1 Hz sampling for ambient ~2 ppm
- Linearity: ±1% for 0-25 ppm range
- Power draw: <30 W (operates on solar/battery systems)
- Detection without FluxMapper™: 2 kg/hour
- Detection with FluxMapper™: 0.2 kg/hour
- Data storage: 4 GB internal (22-44 days depending on sampling frequency; ~40 MB/day at 0.5 Hz)
- Tower height: 3-5 m for initial deployment; 7 m with 7900-300 tripod mast for FluxMapper™ studies

**FluxMapper™ Software (TRL-5, advancing to TRL-6):**
- Operating principle: Traces 10 Hz eddy covariance measurements backward along wind trajectory to geographic source
- Technology: Time-frequency decomposition + adaptive source detection + knowledge-guided AI + geospatial layers
- Output: Geospatified flux maps at decameter resolution, sub-hourly intervals, in units of kg/hour
- Spatial coverage: 4 km² per deployment
- Sensitivity enhancement: Reduces detection threshold from 2 kg/hour to 0.2 kg/hour
- Emission capture improvement: 95% vs. 60-80% with classical eddy covariance
- Key benefit: Disaggregates flux tower data into individual pixel time-series, enabling multi-well simultaneous monitoring

**Validation/Supplementary Instruments:**
- **Xplorobot**: Ground-based TDLAS laser device for episodic methane quantification
  - Sensitivity: 0.5 ppm
  - Detection range: 50 meters
  - Includes integrated anemometer
  - Used for independent validation at each drone and tower site
  
**Remote Connectivity System (HOO-nah Device):**
- Portable, proprietary system from Hyde Park West Telecommunications
- Connectivity modes: Dynamic switching between cellular, satellite (Starlink, Hughes 9502), optical fiber
- Features: Encrypted transmission, proprietary low-bandwidth video teleconferencing
- Power: Low-power design with solar/battery options
- Data handling: Ethernet and USB interfaces; compatible with LI-COR equipment
- Patents: 7 patents (2 US, 1 pending; 1 EPO covering Germany, Ireland, UK, Switzerland, Liechtenstein; 4 Australia)

---

## Products & Capabilities Described

### Black Swift S2 UAS
**What it is:** Fixed-wing unmanned aircraft system designed for long-range environmental monitoring in extreme conditions

**Proposed use in this project:**
- Platform for carrying Quanta3 methane sensor
- Performing ~50 episodic flights over 3 years across orphaned well sites in Colorado
- Each flight complemented by ground-based Xplorobot measurements for validation
- Initial screening of methane-emitting orphaned wells to identify sites for intensive tower-based monitoring

**Performance specifications:**
- Flight endurance: 90 minutes
- Wingspan: 3 meters
- Payload: 2 kg
- Operational range: Capable of flying in extreme weather (high winds, low temperatures)
- Quanta3 sensitivity: 2 ppb
- Methane quantification with eddy covariance: 0.4 kg/hour
- TRL advancement goal: TRL-5 → TRL-6

**Key advantages noted:**
- Covers larger areas than tower systems
- Provides spatial distribution of emissions
- Eliminates human exposure risk
- Automated data collection with high data density
- Reduced operational costs compared to continuous tower monitoring
- Adapts well to high wind speeds (including hurricane-force conditions)

**Limitations identified:**
- Requires access for takeoff/landing within 1 km of source
- Sensitive to cloud cover
- Wind speed dependency: optimal 2-6 m/s; unreliable <2 m/s due to plume variability
- May require re-visiting sites if emissions not detected or are episodic
- Deployment affected by meteorological conditions (insolation, wind direction steadiness)

### Quanta3 Methane Sensor
**What it is:** Custom-built, integrated methane detector for the S2 UAS platform

**Specifications:**
- Sensitivity: 2 ppb (parts per billion)
- Sampling frequency: 2 Hz
- Operating range: Stable across wide range of temperatures
- Integration: Designed for eddy covariance analysis (wind sensing + CH₄ concentration)

**Design features:**
- Provides high-resolution, real-time methane concentration data
- Maintains precision across varying environmental conditions

### FluxMapper™ Software
**What it is:** Advanced data analysis software for converting eddy covariance measurements into geospatially-referenced emission maps

**Proposed use:**
- Post-processing of both drone-based and tower-based eddy covariance data
- Converting flux tower measurements from flux density (kg/hour/m²) to discrete source emissions (kg/hour)
- Creating time-series emission maps at decameter resolution
- Monitoring multiple wells simultaneously across 4 km² areas
- Enhancing detection sensitivity for low-emitting orphaned wells

**Performance claims:**
- TRL-5 → TRL-6 advancement through this project
- Detection sensitivity: 0.2 kg/hour (vs. 2 kg/hour for classical eddy covariance)
- Emission capture: 95% (vs. 60-80% for classical methods)
- Geospatial resolution: Decameter-scale pinpointing
- Temporal resolution: Sub-hourly intervals
- Statistical power increase: 10-fold through pixel disaggregation

**Validation basis:**
- Cross-validation with controlled methane release experiments
- Comparison with independent eddy covariance measurements
- Large eddy simulation confirmation of landscape-level accuracy

### LI-COR Methane System Components
**LI-7700 Open-Path Methane Analyzer:**
- Laser technology: Single-mode tunable near-infrared
- Detection method: Wavelength Modulation Spectroscopy (WMS)
- Compensation: Temperature and pressure algorithms maintain stability
- Precision: 5-10 ppb (1 Hz sampling)
- Range: 0-25 ppm linear response (±1%)
- Temperature stability: Self-cleaning mirrors, regulated optics

**Tower Configuration:**
- Sonic anemometer: Gill WindMaster (10 Hz wind vector measurement)
- Supporting analyzers: LI-7500DS (CO₂, H₂O open-path)
- Data system: SmartFlux acquisition
- Connectivity: Sierra Wireless AirLink RV50X (cellular) or Hughes 9502 (satellite)
- Time synchronization: GPS clocks with Precision Time Protocol (sub-microsecond accuracy)

**Use in project:**
- Deployed for 6-month periods at 3 sites in Year 2 (2 months per site)
- Additional 3-month deployments in Years 2-3 at sites selected based on positive drone results
- Bi-weekly orientation adjustments based on wind patterns and real-time data
- Complementary episodic Xplorobot measurements every two weeks

**Advantages:**
- High accuracy and long-term measurement stability
- Low power (<30 W) enables solar/battery operation
- Minimal on-site labor requirements
- Can be repositioned every 2 weeks based on wind climatology

**Limitations:**
- Site access for tower placement
- Dependency on favorable wind conditions (optimal 2-6 m/s downwind at 10-100 m)
- Static deployment limits plume sampling if wind directions shift
- Measurements provide flux density (kg/m²/hour); requires FluxMapper™ for discrete source quantification

### HOO-nah Connectivity Device
**What it is:** Portable telecommunications integration platform by Hyde Park West Telecommunications

**Specifications:**
- Connectivity: Cellular (multiple carriers), satellite (Starlink, Hughes 9502), optical fiber
- Data interfaces: Ethernet, USB
- Networking: Dynamic carrier switching based on signal strength
- Coverage: 25+ mile catchment from towers (tested with external antennas)
- Power: Low-power design; solar/vehicle-powered options
- Encryption: Full transmission encryption
- Video capability: Proprietary low-bandwidth teleconferencing platform
- Applicability: Tested in moving vehicles (ambulances, trucks), stationary installations

**Proposed use:**
- Interface with LI-COR methane system for real-time data transmission
- Enable continuous monitoring and episodic data upload from