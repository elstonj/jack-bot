# Coyote UAS Observations in Hurricane Edouard (2014)

## Document Metadata
- **Type**: Research article / peer-reviewed publication
- **Client/Agency**: NOAA (National Oceanic and Atmospheric Administration) - Hurricane Research Division
- **Program/Solicitation**: Disaster Relief Appropriations Act of 2013
- **Date**: Published September 30, 2016 (research conducted September 16-17, 2014)
- **BST Products/Systems Referenced**: Coyote UAS (manufactured by Raytheon Missile Systems; note: document indicates Raytheon as manufacturer, but this appears to be a reference document for BST's proposal context)
- **Key Personnel**: J.J. Cione, E.A. Kalina, E.W. Uhlhorn (NOAA); A.M. Farber (AIR-Worldwide); B. Damiano (NOAA Aircraft Operations Center); Jack Elston (last editor on BST copy)

## Executive Summary
This peer-reviewed publication documents the first successful deployment of an unmanned aircraft system (Coyote UAS) into a major hurricane from an airborne manned aircraft. Two Coyote missions were conducted in Hurricane Edouard on September 16-17, 2014, collecting low-altitude boundary layer measurements (wind, temperature, moisture) from the eye, eyewall, and inflow layer. Coyote measurements compared favorably with concurrent observations from NOAA's WP-3D aircraft and GPS dropsondes, validating UAS data accuracy in extreme tropical cyclone conditions.

## Technical Approach

### Coyote UAS Platform Specifications
- **Dimensions**: 0.79 m length, 1.47 m wingspan, 6 kg mass
- **Payload Capacity**: Up to 1.8 kg
- **Maximum Cruising Airspeed**: ~36 m/s (~40 m/s ground speed during missions)
- **Endurance**: 68 minutes (platform record achieved in second mission)
- **Deployment Method**: Folded wings, placed in canister, released from WP-3D sonobuoy chute at ~3 km altitude; parachute slows descent; Coyote wings deploy ~15 seconds after release
- **Flight Control**: Remote commands issued from WP-3D
- **Data Transmission**: Iridium satellite connection (unreliable) and 900-MHz data stream (required WP-3D within 8-11 km range for first mission, ~6 km for second)

### Meteorological Sensor Suite
**Sensors and Specifications (per Table 2):**
- **Pressure**: Honeywell SCCP15ASMTP (5-1070 mb range, ±0.5 mb tolerance, <1.0 s response, 3 Hz sampling)
- **Temperature**: SHIBAURA PB5 (-80 to 60°C range, ±0.3°C tolerance, <2.0 s response, 2 Hz sampling)
- **Humidity**: E+E HC103M2 (0-100% range, ±5% tolerance, <5.0 s response at 25°C, 1 Hz sampling)

### Wind Measurement Methodology
- Ground velocity: Computed via 50-Hz GPS/INS extended Kalman filter (IMU, air data, GPS inputs)
- Equivalent airspeed (EAS): Calculated from pitot-static pressure differential: EAS = √(2Q/ρ₀), where Q is dynamic pressure and ρ₀ = 1.225 kg/m³
- True airspeed (TAS): Computed from IAS × √(ρ₀/ρ), where ρ is local air density
- Wind speed/direction: Vector subtraction of true air velocity from ground velocity; reported at 1 Hz
- Note: Kalman filter details are proprietary; future improvements planned for customized tuning

### Comparison Methodology
- **Dropsonde Data Analysis**: Weighted Gaussian interpolation to Coyote flight track using scaled distances in radius, azimuth, altitude, and time
  - Eyewall scaling: sᵣ = 5 km, sλ = 45°, sz = 100 m, st = 1 hour
  - Inflow layer scaling: sᵣ = 10 km, sλ = 10°, sz = 100 m, st = 1 hour
- **WP-3D Comparison**: 1-second flight-level wind measurements at ~3 km altitude

## Products & Capabilities Described

### Coyote UAS
**What it is**: Small air-deployed unmanned aircraft system capable of sustained low-altitude atmospheric sampling in extreme weather conditions

**Proposed/Demonstrated Uses**:
- Tropical cyclone boundary layer observation (primary application demonstrated)
- Measurement of heat, moisture, and momentum exchanges in hurricane environments
- Low-altitude sampling (900-1500 m in eye/eyewall; ~760 m in inflow layer) previously dangerous or impossible for manned aircraft
- Extended endurance missions (up to 68 minutes documented)

**Specifications/Performance Claims**:
- Wind accuracy: ±1-2 m/s (validated against WP-3D and dropsonde data)
- Temperature accuracy: ±0.4-0.0°C mean difference (16-17 September respectively)
- Dew point accuracy: ±0.7-1.3°C mean difference
- Fine-scale variability detection: 3.5× higher wind variability detection than dropsonde analyses (σ = 3.4 m/s vs. 2.2 m/s)
- Capable of sampling rainband structure and small-scale features

**Payload Capabilities**:
- Temperature, humidity, pressure sensors with 1-2 Hz sampling rates
- Wind speed/direction computation from GPS/INS/air data integration
- Future capability: downward-looking infrared for sea surface temperature measurement
- Modular payload design allowing sensor suite customization

## Use Cases & Applications

### Demonstrated Missions (Hurricane Edouard, 2014)

**Mission 1: Eye/Eyewall Survey (September 16, 1433-1500 UTC)**
- Duration: 27 minutes
- Altitude: 900-1500 m (descending then climbing)
- Area: Eye, transition zone, and western eyewall
- Hurricane State: Major hurricane (105 kt / 54 m/s)
- Key Findings:
  - Light winds (2-8 m/s) in eye region
  - Rapid wind increase in eye-eyewall transition (8-32 m/s over 10 km radial distance)
  - Peak wind: 51.5 m/s in eyewall (Coyote platform record)
  - Temperature: 75% of data within ±1°C of dropsonde analysis
  - Dew point: 67% of data within ±1°C of analysis

**Mission 2: Inflow Layer Survey (September 17, 1508-1616 UTC)**
- Duration: 68 minutes (platform endurance record)
- Altitude: ~760 m, varying 250-460 m
- Area: Northwestern quadrant, 275-150 km radius (clear air and rainband)
- Hurricane State: Weakening hurricane (80 kt / ~41 m/s)
- Key Findings:
  - Total wind speed agreement: 0.5 m/s mean difference vs. dropsonde analysis
  - Radial wind agreement: 0.8 m/s mean difference
  - Temperature: 93% of data within ±1°C, 59% within ±0.5°C
  - Detected outer rainband structure with increased wind speeds (18-25 m/s pre-rainband increase)
  - Captured fine-scale moisture gradients and variability

### Identified Research Applications
- **Hurricane Intensity Forecasting**: Potential to validate/improve NOAA's coupled Hurricane Weather Research and Forecasting (HWRF) operational modeling
- **Boundary Layer Science**: Addresses critical data gaps in tropical cyclone boundary layer thermodynamics and kinematics previously inaccessible to manned aircraft
- **Air-Sea Interaction Studies**: Measurement of heat, moisture, and momentum exchanges controlling TC intensity
- **Observing System Optimization**: Planned Observing System Experiments (OSEs) and Observing System Simulation Experiments (OSSEs) to optimize observing strategies
- **Future "UASonde" Concept**: Hybrid platform combining Coyote UAS targeting capabilities with GPS dropsonde and Airborne Vertical Atmospheric Profiling System (AVAPS) technologies for next-generation operational applications

## Key Results

### Wind Measurement Validation

**16 September Eye/Eyewall Mission**:
- Mean wind speed difference (Coyote vs. WP-3D inbound): 1.2 m/s
- Mean wind speed difference (Coyote vs. WP-3D outbound): 0.8 m/s
- Peak winds: Coyote 51.5 m/s; WP-3D adjusted to flight level 55.6-59.5 m/s
- Agreement in radial wind profiles: Excellent (within ~1 m/s average)
- Individual dropsonde validation (7.8 km from center): 6.4 m/s measured; Coyote measured ~5 m/s in same radial zone

**17 September Inflow Layer Mission**:
- Mean total wind speed difference: 0.5 m/s
- Mean radial wind component difference: 0.8 m/s
- Individual dropsonde agreements: Within ~2 m/s
- Wind variability detection: Coyote σ = 3.4 m/s vs. dropsonde analysis σ = 2.2 m/s (3.5× higher variability capture)

### Temperature and Moisture Validation

**16 September Eye/Eyewall**:
- Air temperature agreement: 75% within ±1°C, 46% within ±0.5°C; mean difference 0.4°C
- Dew point temperature: 67% within ±1°C, 40% within ±0.5°C; mean difference 0.7°C
- Individual dropsonde validation: Both platforms recorded ~21°C at same altitude

**17 September Inflow Layer**:
- Air temperature agreement: 93% within ±1°C, 59% within ±0.5°C; mean difference 0.0°C
- Dew point temperature: Mean difference 1.3°C; attributed to possible Coyote "moist bias" or dropsonde "dry bias"
- Individual dropsondes showing sharp radial gradients: Differences reduced to 0.3-0.4°C when accounting for spatial variability

### Scientific Findings

1. **First Air-Deployed UAS in Hurricane**: Coyote deployments from WP-3D represent first successful air-launched UAS missions into tropical cyclone
2. **Boundary Layer Structure**: Documented 2-3°C warming trends with altitude descent (1500-900 m)
3. **Rainband Detection**: Coyote captured outer rainband structure and increased wind speeds (18-25 m/s) not resolved by discrete dropsonde measurements
4. **Moisture Gradients**: Detected sharp radial gradients in moisture; identified feature locations to within ~1 km
5. **Data Quality Confirmation**: All measured parameters (wind, temperature, moisture) compare favorably with independent observations, validating UAS sensor accuracy in hurricane environments

## Notable Details

### Historical Context
- **First Occurrence**: First successful air-deployed UAS launch into mature hurricane (prior UAS TC deployments were land-based only)
- **Prior UAS Hurricane Flights**: Only three prior missions documented:
  - 2005 Tropical Storm Ophelia (~760 m altitude)
  - 2005 Typhoon Longwang (3000 m altitude)
  - 2007 Hurricane Noel (~90 m altitude)
- **Innovation**: First comparison of UAS data with concurrent measurements from other platforms (WP-3D, dropsondes)

### Operational Partnerships & Support
- **NOAA/Aircraft Operations Center**: WP-3D platform provider and operational support
- **Raytheon Missile Systems**: Coyote manufacturer; engineers Andrew Osbrink, Chris Troudt, Eric Redweik involved
- **ItriCorp**: Payload integration support (Jim Etro