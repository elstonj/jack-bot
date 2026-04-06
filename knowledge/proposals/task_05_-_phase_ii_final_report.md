# Task 05: Phase II Final Report - Atmospheric Sounding UAS

## Document Metadata
- Type: Phase II Final Report
- Client/Agency: U.S. Air Force
- Program/Solicitation: SBIR (contract FA8730-20-C-0021)
- Date: 16 April 2021
- BST Products/Systems Referenced: S0 (atmospheric sounding UAS)
- Key Personnel: Dr. Jack Elston (PI)

## Executive Summary
This report documents the Phase II validation of Black Swift Technologies' S0 atmospheric sounding UAS platform, demonstrating its capability to conduct autonomous meteorological profiling missions for Air Force operations. The S0 was deployed to the DOE ARM Southern Great Plains facility in Oklahoma (29 March - 3 April 2021) where it completed 11 flights and was directly compared against radiosondes, tower-based instruments, and other UAS platforms (RAAVEN, M600 hexacopter, CoMeT, CopterSonde, Nimbus, nanoTalon). Performance validation confirmed design targets for endurance, climb capability, autoland precision, and wind tolerance while identifying minor sensor calibration issues requiring attention.

## Technical Approach

### Flight Performance Validation
- **Endurance Testing**: 15 missions conducted at SGP test site in Oklahoma measuring power usage and flight time. Results: 70-100 minute typical endurance with 20% power reserve for VTOL landing; cruising-only maximum ~80 minutes (exceeds 60-minute design target).
- **Climb Rate Testing**: Evaluated climb rates from 1-6 m/s (5 m/s omitted)
  - 1 m/s: insufficient to reach 15,000 ft with battery reserve
  - 2-6 m/s: all achieve required 15,000+ ft altitude
  - 6 m/s optimal: reaches 15,000 ft in 13 minutes vs. 20-minute design target at 4 m/s
  - Maximum altitude achievable using 80% battery: varies by climb rate
  
- **Autoland Accuracy**: Precision tested with 10 fixed-wing belly landings (VTOL performance inferred)
  - Mean error: 6.9m overall; 1m (3.3 ft) lateral error
  - Performance well under 10 ft (3.3m) requirement
  - Note: Expected VTOL lateral error similar to measured 1m lateral belly-landing error

- **High Wind Operations**: Successfully demonstrated autonomous operation in winds up to 38 mph
  - 7 of 15 missions in winds exceeding 25 mph
  - 2 missions in winds exceeding 34 mph
  - Exceeds 30 mph design target maximum

- **Operational Efficiency**:
  - Mission prep/setup: <5 minutes per mission for trained operators conducting 5 consecutive missions
  - Real-time telemetry: Full science data downlink throughout entire flight profile with minimal ground equipment
  - Data standardization: Automated generation of Air Force-compliant data files within 5 minutes of landing; validated on 5 different days at maximum altitude

### Sensor Integration & Payload
The S0 was equipped with:
- **Vaisala RSS-421 sensor**: Pressure, temperature, humidity measurement (3D printed housing for solar/precipitation protection)
- **3D sonic anemometer** (tower reference)
- **GPS-based autopilot wind estimation**
- Real-time data logging and telemetry transmission capability

### Flight Patterns Employed
- **Profiling**: Coordinated ascent/descent with radiosonde launches at 1, 2, 3, 4, and 6 m/s rates (3-6 S0 profiles per radiosonde launch)
- **Orbital/Circular**: Varying radius orbits (80-230 m) at constant altitude to evaluate wind sensing and assess impact of aircraft roll angle
- **Star Pattern**: Three racetrack legs offset ~120° to assess directional wind bias
- **Racetrack**: Level flight perpendicular and parallel to wind direction for statistical wind sensing evaluation

## Products & Capabilities Described

### S0 (Atmospheric Sounding UAS)
**What it is**: Autonomous fixed-wing small UAS designed for atmospheric profiling and meteorological data collection to 15,000+ ft altitude with VTOL launch/recovery.

**Validated Capabilities**:
- Autonomous flight from launch to land (VTOL capable)
- Vertical profiling with operator-selectable climb/descent rates (1-6 m/s)
- Level flight at specified altitudes for extended statistical sampling
- Precision autoland capability (<3.3 m lateral error)
- Real-time telemetry of science data with minimal ground station
- Autonomous data processing and Air Force-compliant file generation
- High-wind autonomous operation (validated to 38 mph)

**Sensor Performance** (challenges identified):
- **Temperature**: Consistent warm bias of ~2 K relative to reference instruments (radiosondes, tower, RAAVEN) across all comparison methods. Likely cause: thermal effects from 3D printed sensor housing and aircraft airflow interference. Minor solar incidence effect (0.1-0.2 K) detected, with aircraft measuring warmer when flying away from sun.
- **Pressure**: Bias of 3-4 hPa low relative to radiosondes and tower; 1-2 hPa low relative to surface comparisons. Potential causes: sensor housing airflow effects or GPS altitude measurement inaccuracy (though latter deemed less likely).
- **Relative Humidity**: Generally within 1-2% sensor uncertainty; some flights showed ~5% dry bias. Variability between two airframes noted (e.g., S0-2 showed 11.34% low bias in one period vs. S0-1 showing good agreement).
- **Wind Speed/Direction**: Good agreement with radiosonde and tower measurements; autopilot-derived wind (U/V components) mean bias ~0 m/s relative to sonic anemometer. S0 captures less variability than sonic anemometer but performs well at 10 Hz temporal resolution.
- **Vertical Velocity**: Reasonable agreement with reference platforms; captures expected variability in atmospheric boundary layer.

**Specifications**:
- Target altitude: 15,000 ft
- Design endurance: 60 minutes
- Actual endurance: 70-100 minutes typical; maximum 80 minutes cruise
- Maximum validated wind: 38 mph
- Lateral autoland error: 1 m (well under 3.3 m requirement)
- Mission setup time: <5 minutes

## Use Cases & Applications

**Primary Mission**: Air Force atmospheric sounding and meteorological profiling
- Autonomous deployment for boundary layer and vertical atmospheric structure characterization
- Time-critical mission execution (rapid setup/turnaround)
- Operations in high-wind environments where larger platforms cannot operate
- Remote deployment to austere locations

**Specific Deployment Context**: DOE ARM Southern Great Plains facility atmospheric research
- Intercomparison with radiosondes (operational standard)
- Validation against tower-based reference instrumentation
- Collaborative operation with multiple UAS platforms

## Key Results

### Meteorological Data Quality Assessment

**Radiosonde Comparison** (9 flights with concurrent launches):
- Temperature: +2 K bias (too warm)
- Pressure: -3 to -4 hPa bias (too low)
- Relative Humidity: ±1-2% variability; some flights ±5% dry bias
- Wind Speed/Direction: Good agreement, within expected atmospheric variability
- Specific Humidity/Water Vapor Mixing Ratio: Good agreement (1-to-1 line)
- Note: One radiosonde exhibited sensor issues affecting humidity comparisons; attributed to radiosonde instrument malfunction, not S0 error

**Tower Instrument Comparison** (60 m AGL level flight segments):
- Temperature: Persistent +1-2 K warm bias
- Relative Humidity: Mostly within 1-2% sensor uncertainty; some flights ~5% dry
- U/V Wind Components: Mean bias ~0 m/s; S0 wind estimate less variable than sonic anemometer (due to autopilot filtering)
- Solar influence on temperature: Minimal effect (0.1-0.2 K), with warmer readings when flying away from sun
- Flight pattern impact: Limited influence on thermodynamic/kinematic measurements

**RAAVEN UAS Comparison** (2 April, Marshall mesonet site):
- Wind Measurements: Very good agreement; S0 showed more variability but good correspondence at 10 Hz resolution
- Temperature: S0 measured ~2 K warmer (consistent with other comparisons)
- Relative Humidity: S0 measured 1-2% higher (within 2% Vaisala repeatability specification)
- Pressure: S0 measured slightly lower (consistent with radiosonde/tower comparisons)
- Temperature Sensitivity: RAAVEN captured greater temperature differences during profiling maneuvers, suggesting S0 sensor housing limits sensitivity to atmospheric temperature changes

**Surface-Based Instrument Intercomparison** (3 periods with elevated wind speeds):
- Pressure: Biases ranged -0.25 to -2.13 hPa; beyond sensor uncertainty
- Temperature: S0 biases +0.45 to +1.70 °C; outside expected sensor uncertainty
- Relative Humidity: S0-1 accurate (1.39-1.69% low); S0-2 highly variable (11.34% low to 2.5% high)

**Identified Root Cause**: 
The consistent +2 K temperature warm bias and -3 to -4 hPa pressure low bias across all comparison methods (radiosondes, tower, RAAVEN, surface instruments) are most likely attributable to the 3D printed sensor housing design and aircraft airflow interference around the Vaisala RSS-421 sensor, rather than GPS altitude measurement error (which would not explain the simultaneous occurrence of both temperature high and pressure low biases given the opposite temperature/pressure gradients with altitude).

### Mission Capability Validation
- **Endurance**: Exceeded design target (60 min target vs. 70-100 min actual; 80 min pure cruise)
- **Climb Performance**: Met all altitude targets; 6 m/s climb rate offers efficiency advantage
- **Autoland Precision**: Demonstrated <1 m lateral error; exceeds 3.3 m requirement
- **Wind Tolerance**: Validated to 38 mph; exceeds 30 mph design maximum
- **Operational Readiness**: <5 minute setup time validated across 5 consecutive missions
- **Data Processing**: Automated Air Force-compliant file generation within 5 minutes post-landing

## Notable Details

### Test Site Infrastructure & Collaboration
- **Primary Site**: DOE Atmospheric Radiation Measurement (ARM) Southern Great Plains (SGP) facility, Lamont, Oklahoma
- **Reference Instruments at SGP**:
  - 60 m instrumented tower with 3D sonic anemometer, temperature, humidity sensors
  - Radiosonde launching capability (augmented from 4 to 9 daily launches for this evaluation)
  - Surface Energy Balance System (SEBS/ECOR) measurements
  - DOE ARM comprehensive sensor suite
  
- **Secondary Site**: Marshall (OK) mesonet
  - Comparison with University of Colorado RAAVEN
  - Comparison with University of Oklahoma CopterSonde
  - Comparison with Oklahoma State University Nimbus and nanoTalon platforms

- **Collaborative Platforms**:
  - University of Nebraska-Lincoln M600 hexacopter (iMet XQ sensors)
  - UNL Combined Mesonet and Tracker (CoMeT)
  - Multiple reference instruments (8 iMet XQ-2's evaluated)

### Sensor Housing Challenge
The 3D printed protective housing for the Vaisala RSS-421 sensor—designed to shield from solar irradiance, precipitation, and damage—appears to be the primary source of measurement biases. Future iterations should prioritize redesign to minimize thermal effects and pressure measurement interference while maintaining protection.

### Temporal Variability Methodology
The evaluation protocol deliberately employed multiple S0 profiles (3-6 per radiosonde launch) at various ascent/descent rates (1, 2, 3, 4, 6 m/s) to distinguish sensor lag effects from atmospheric temporal heterogeneity—a sophisticated approach accounting for atmospheric boundary layer variability that radiosondes cannot capture.

### Data Deliverables to Customer
Sampling flights conducted on 5 different days to maximum altitude; ground system automatically generated Air Force-standard data files within 5 minutes of landing. Files stored with link provided to Air Force customer for analysis.

### Document Status
This appears to be a comprehensive technical