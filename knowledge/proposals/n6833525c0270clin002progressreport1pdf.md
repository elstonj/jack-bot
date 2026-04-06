# Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions via Small Uncrewed Aircraft System

## Document Metadata
- **Type:** SBIR/STTR Progress Report (Phase I, CLIN 002)
- **Client/Agency:** Department of the Navy (DON) / NAVAIR
- **Program/Solicitation:** BAA Topic N25A-T025; SBIR/STTR
- **Contract Number:** N6833525C0270
- **Date:** October 6, 2025 (Report period: July 7 – October 6, 2025)
- **BST Products/Systems Referenced:** S0 (small uncrewed aircraft system), S0-VTOL, Multi-hole pressure probe (MHPP)
- **Key Personnel:** Dr. Jack Elston (Principal Investigator), Meredith Needham (editor)
- **Security Classification:** Unclassified, ITAR Restricted; Distribution Statement B

## Executive Summary
This Phase I progress report documents Black Swift Technologies' work to refine and validate the S0 unmanned aircraft system (UAS) for Navy applications in hazardous weather. The project focuses on delivering high-resolution atmospheric and air-sea observations, particularly for tropical cyclone (TC) operations. Phase I achievements include comparative analysis of existing profiling platforms, comprehensive S0 data validation against multiple sources, and documentation of significant hardware improvements for 2025 operations.

## Technical Approach

### Phase I Objectives
1. **Quantifying enhanced capabilities:** Compare S0 performance to existing platforms (dropsondes, radiosondes, Tail Doppler Radar) and address need for improved expendable in-situ profiling in challenging air-sea environments
2. **Assessing and improving measurement accuracy:** Calibration, validation, error analysis, and extending operations to icing conditions
3. **Producing new observations:** Vertical wind, turbulence, and wave properties; developing onboard algorithms
4. **Adaptive sampling:** Automatically targeting areas of interest using S0's onboard computing and software APIs

### Key Technical Work Completed (Tasks B1 & B2)

**Task B1: Background Review and Comparative Analysis**
- Detailed review of existing atmospheric profiling platforms with emphasis on measurement uncertainties and logistical challenges
- Comparative analysis of NCAR dropsondes, Vaisala radiosondes, Raytheon Coyote, Anduril Altius-600, and Skyfora Streamsonde
- Analysis focused on cost, data accuracy, spatial/temporal coverage, and longevity
- Assessment of S0 advantages over existing systems

**Task B2: S0 Data Analysis and Enhancements**
- Detailed error analysis of S0 measurements (wind, turbulence, height calculations)
- Development of test plan and validation experiments for Phase II
- Evaluation of icing impacts and mitigation strategies
- Validation of sensor performance through multiple comparison datasets

## Products & Capabilities Described

### S0 (Small Uncrewed Aircraft System)
**Overview:**
- 3-pound air-deployable aircraft (compared to ~25 lb Altius-600)
- Expected 2-hour endurance in tropical cyclones (2025), improved from 105 minutes in 2024
- Smallest deployable UAS currently used for hurricane missions
- Recoverable or expendable operation

**Sensor Package:**
- Vaisala RSS421 sensors for pressure, temperature, humidity (same sensors as dropsondes)
- Downward-pointing IR sensors for sea surface temperature (SST) measurement
- Multi-hole pressure probe (MHPP) manufactured by BST for turbulence-quality wind measurements (capable of 100 Hz sampling)
- Radar altimeter (NEW 2025): Activated below 50 m, provides accurate representation of S0 location over large waves or GPS drift
- Dual-GPS system for heading accuracy improvement (from 3° magnetometer to 0.5°, 2025 upgrade)

**2025 Hardware Improvements:**
1. **Data Products:**
   - Improved wind sensing: dual-GPS replacing magnetometer, expected to improve horizontal wind accuracy from 1.5 m/s to 0.3 m/s or better
   - Onboard turbulence calculation with increased processing
   - Radar-guided flights down to 10 m with wave height measurements
   
2. **Avionics:**
   - Updated firmware supporting dual-GPS operation
   - 10 Hz MET data capability
   - Improved communications antenna with increased range
   - Updated power control board for 6S battery configuration

3. **Ground Station/UI:**
   - AirOps interface updated with additional data fields (radar altitude, comms quality)
   - Onboard NetCDF generation
   - Real-time data viewing on P-3 workstations via web browser

4. **System Updates:**
   - Battery upgrade: 108 Wh to 130 Wh (expected >20% endurance improvement)
   - Simplified propulsion system (combined ESC, motor, cooling)
   - ~25% increased power output for downdraft handling
   - Improved wing structure for stiffness and weight reduction
   - >50% reduction in final assembly time
   - Electronics sourcing to meet NDAA requirements

**Communication Range:**
- Clear-air: 210 nmi at 1,500 m altitude
- Tropical Storm Imelda: 160 nmi at 150 m altitude
- Significantly higher than Altius-600 (130 nmi demonstrated in Hurricane Ian)

**Unique Capabilities:**
- Only waterproof 5-hole pressure probe with SWAP suitable for small UAS
- Only sUAS currently deployed in 2025 hurricane season (Erin, Gabrielle, Imelda)
- Capable of measuring turbulent characteristics previously only achievable with crewed aircraft MHPP
- 19 successful hurricane launches in 2024; first successful deployment in Hurricane Tammy (2023)

### Measurement Specifications (Table B2.1 - Phase II Targets)

**Static Pressure:**
- Target Uncertainty: 1 hPa
- Response: 0.01 s
- Frequency: 10 Hz (100 Hz onboard, limited to 10 Hz by comms link)

**Relative Humidity:**
- Target Uncertainty: 4%
- Response: 0.3–10 s
- Frequency: 10 Hz

**Air Temperature:**
- Target Uncertainty: 0.3°C
- Response: 0.5 s
- Frequency: 10 Hz

**3D Winds:**
- Target Uncertainty: 0.3 m/s
- Frequency: 10 Hz (100 Hz onboard)

**Sea Surface Temperature:**
- Target Uncertainty: 0.3°C

**Wave Height:**
- Significant wave height: <1 m (best case 0.2 m)
- Mean Squared Slope: 10% accuracy

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Reconnaissance
- **Air-sea profiling observations in hazardous weather conditions**
- **Target:** Inner-core and boundary layer measurements where dropsondes and radar have limitations

### Specific Advantages Over Existing Platforms

**vs. Dropsondes:**
- **Spatial Coverage:** Better coverage in inner-core region (r<100 km); larger horizontal area vs. single vertical profile
- **Observation Volume:** 
  - 2024 S0: ~6,300 obs per flight vs. 333 obs per dropsonde
  - 2025 S0: ~25,200 obs per flight (3x improvement)
  - Under 500m: 283× equivalent dropsondes
  - Under 100m: 1,391× equivalent dropsondes
- **Sustained Measurement:** Can sample strongest wind region for longer periods; provides 1-minute sustained wind estimates vs. instantaneous dropsonde winds
- **Cost Efficiency:** S0 at $15K yields significantly better return than dropsondes at $1K each when accounting for measurement yield and time

**vs. Tail Doppler Radar (TDR):**
- Provides thermodynamic observations in lowest 2 km not achievable from TDR
- ~100 times more observations than dropsondes
- Flexible flight patterns; not constrained by aircraft flight track
- Able to target specific regions substantially away from flight track

**vs. Altius-600:**
- Lighter weight (3 lb vs. 25 lb)
- Better communication range demonstrated
- Superior endurance in 2025 configuration

### Turbulence and Exchange Coefficient Measurements
- **Unique capability:** Calculating drag coefficient (CD), heat transfer coefficient (CH), moisture transfer coefficient (CE)
- **Methodology:** Deloach et al. (2025) demonstrated feasibility using S0 MHPP data at ~10 m altitude
- **Value:** These exchange coefficients are critical for hurricane intensity prediction but have high uncertainty (>100% for hurricane-force winds)
- **Application data shown:** Momentum flux, sensible heat flux, latent heat flux calculations from 8 flight-path legs
- **Onboard processing planned:** Algorithms to calculate CD, momentum flux, turbulent kinetic energy at higher frequencies during Phase II

### Boundary Layer Turbulence Structure
- Example from Tropical Storm Imelda (Sept 29, 2025): Detected 4x increase in wind standard deviation between 100 m and 50 m altitude—impossible for dropsondes to capture
- Enables study of turbulent-scale processes and vertical wind variation near surface

## Key Results

### Comparative Performance Demonstrations

**2024 Hurricane Season Deployments:**
- 19 launches across Hurricanes Ernesto, Francine, Helene, and Milton
- 2025 season (as of Oct 1): 3 deployments in Erin, Gabrielle, Imelda
- Longest 2024 mission: 105 minutes
- Longest 2025 mission: 111 minutes (Tropical Storm Imelda, with battery capacity remaining)

### Data Validation Results

**SGP Tower Comparison (2021):**
- 10 S0 flights over 3 days at ARM Southern Great Plains site
- Compared against 60 m tower with sonic anemometer, temperature, humidity
- Validated "self-QC" wind estimation technique using GPS speed over ground
- Demonstrated good agreement on bulk wind estimates

**Dropsonde Comparison (2023):**
- Clear-air tests with simultaneous dropsonde deployments
- Wind speed and direction profiles aligned well with dropsonde data
- Demonstrated ability to capture detailed temporal structure that dropsondes miss

**Clear Air Test Flights (2024):**
- Comparison with 8 Streamsondes and 1 Vaisala dropsonde
- Two flights on 2024-03-20 and 2024-03-21
- Temperature agreement generally good with minor deviations (±0.9°C in lower atmosphere)
- Humidity agreement strong across altitude ranges
- Wind means aligned well; identified issues with tight spiral patterns producing outliers

**Tail Doppler Radar Comparison (2024):**
- S0 wind measurements at 500 m altitude compared with NOAA P-3 TDR
- Wind speeds in Hurricane Ernesto and Milton showed good alignment
- Confirms reliability of S0 wind measurements

### Turbulence Measurements (Deloach et al. 2025 Data)
- Successfully calculated momentum flux, sensible heat flux, latent heat flux from near-surface measurements
- Drag coefficient (CDN) calculations from 8 flight legs
- Exchange coefficients for sensible heat (CHN) and latent heat (CEN) derived
- Data shows expected variability with wind speed

### Field Coverage Comparison (2024 Data)
- Figure analysis from Hurricane Helene shows:
  - Dropsonde: Limited to areas near flight track, single vertical profiles
  - S0: Much larger horizontal area coverage with continuous sampling capability
  - Data density: 2 S0 flights ~ 2× total observations of entire dropsonde suite

## Notable Details

### Competitive Position
- **Only air-deployed sUAS in operational use for 2025 hurricane season** (as of report date)
- Previous generation platforms (Aerosonde, Raytheon Coyote) no longer manufactured
- Competing platform: Anduril Altius-600 (not deployed in 2025 as of report)
- Only MHPP currently sampling turbulence in tropical cyclones
- Only waterproof 5-hole probe with SWAP for small UAS integration

### Technical Innovation
- Radar altimeter implementation unique to S0 among hurricane-