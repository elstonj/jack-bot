# Expendable Air-sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- **Type:** Final Report (SBIR Phase I Option)
- **Client/Agency:** U.S. Navy Office of Naval Research (ONR)
- **Program/Solicitation:** Navy STTR Topic N25A-T025
- **Contract Number:** N6833525C0270
- **Date:** September 1, 2026
- **Period of Performance:** 02/17/2026 – 09/01/2026
- **BST Products/Systems Referenced:** S0 UAS (unmanned aerial system)
- **Key Personnel:** Jack Elston (CEO, Principal Investigator), Maciej Stachura (Prepared By), Beck Cotter (Last Editor)

## Executive Summary

This Phase I Option period matured the Black Swift S0 UAS as an expendable, air-deployed platform for high-resolution atmospheric and ocean-surface profiling in hazardous maritime weather, including tropical cyclones and polar environments. The Option period addressed four objectives: (O.1) Phase II calibration and validation planning, (O.2) analysis of 2026 NOAA oceanic flight data, (O.3) onboard sea-surface wave-property algorithms, and (O.4) stakeholder engagement and integration planning. Key achievements included two NOAA P-3 validation flights with simultaneous dual-S0 deployment, identification and correction of wind-measurement error sources (reducing worst-case errors by up to 2 m/s), successful air-deployment from DoD aircraft, and development of viable wave-height estimation algorithms suitable for onboard execution.

## Technical Approach

### O.1: Phase II Calibration and Validation Plan
BST defined a four-event over-ocean validation campaign using the Ocean Observatory Initiative Pioneer Mid-Atlantic Bight Array (primary site) off North Carolina, with contingency sites including the Air-Sea Interaction Tower near Martha's Vineyard, Virginia Key NDBC station, Fowey Rock C-MAN station, and the University of Miami SUSTAIN laboratory. Each test event is structured to validate base sensing (3D winds, pressure, temperature, humidity, sea-surface temperature) against independent references (dropsondes, towers, buoys, tail Doppler radar) while progressively validating onboard algorithms (turbulence, wave-height estimation). Tests are staged so base sensing validation accumulates statistical weight across all four events while algorithm validation is sequenced to manage risk.

### O.2: Calibration and Validation Using 2026 NOAA Oceanic Flight Data
Two P-3 validation flights were conducted (26 March and 7 April 2026) using box flight patterns to sample all four wind-relative orientations. Both missions included the first simultaneous deployment of two S0 aircraft, enabling direct platform-to-platform repeatability assessment in identical air masses.

**26 March Mission (W-168, Gulf of America):**
- Altitude: 3,000 ft (914 m) MSL
- Conditions: Clear, calm day
- Leg length: 10 km
- Analysis revealed step-function-like wind responses between legs, localized to wind retrieval rather than thermodynamic sensing

**7 April Mission (East of Cape Canaveral):**
- Altitude: 1,000 m (3,280 ft) MSL
- Conditions: Stratiform rain region
- Leg length: 5 km (allowing both S0s to complete full boxes)
- First S0 validation flight in precipitation; no step-function error observed

Systematic error-source evaluation covered magnetometer calibration, accelerometer bias, magnetometer-to-IMU misalignment, and propagation of pressure/temperature/humidity errors into true airspeed.

### O.3: Wave Height Objective
Developed four sequential estimators for significant wave height (Hs) and mean square slope (MSS) from onboard radar altimeter, with accuracy goals of 3% Hs and 10% MSS. Physical basis: using cross-spectral identity to separate sea-surface elevation from aircraft vertical motion without assuming either sensor is clean.

**Four Candidate Algorithms:**
1. **Method A (Batch Welch cross-spectrum):** Reference offline calculation; validated against independent wave data; state-of-the-art approach
2. **Method B (Spectral Kalman filter):** Sequential design with Fourier coefficients per wavenumber; full covariance maintenance required
3. **Method C (Exponentially-weighted Welch):** Sequential form of Method A using block periodograms with exponential forgetting weights
4. **Method D (EWMA cross-covariance):** Simplest approach using two IIR filters and four exponentially-weighted moving averages; no FFT, no matrix state

Validation used three transects from S0 flights, compared against GFS-wave and ERA5 numerical analyses, and tested altitude independence using step-descent transect.

### O.4: Stakeholder Engagement and Integration Planning
Two air deployments conducted with SOCOM aircraft (17–18 August 2026) using hand-toss release rather than Common Launch Tube. Compared hand-toss deployment against CLT mechanisms to enable initial testing by other users without full CLT integration.

## Products & Capabilities Described

### S0 UAS
**What it is:** Expendable, air-deployed unmanned aerial system designed for atmospheric profiling in hazardous maritime weather

**Sensing Capabilities:**
- 3D wind measurement (via multi-hole pressure probe, IMU, magnetometer)
- Pressure (0.4 hPa accuracy target)
- Air temperature (0.1°C accuracy target, 0.5s response time)
- Relative humidity (2% accuracy target, 0.3s response time)
- Sea-surface temperature (0.3°C accuracy target)
- Radar altimeter for sea-surface wave properties
- Onboard storage at 100 Hz (altitude channel) and 50 Hz (radar)
- Telemetry downlink at ~5 Hz

**Onboard Compute:**
- Enhanced onboard compute running turbulence algorithms
- Sequential wave-height estimator suitable for onboard execution at 50 Hz
- Existing flight computer capable of handling IIR filter-based algorithms (~20 FLOPS per sample)

**Performance Specifications Demonstrated:**
- Dual simultaneous deployment capability
- Deployment ceiling: 19,341 ft hand-toss release; climbed to 19,718 ft
- Station-keeping capability: ±0.64 m standard deviation altitude maintenance over 109 s
- Stratiform rain tolerance demonstrated
- No unrecoverable attitude excursions during DoD deployments

## Use Cases & Applications

1. **Tropical Cyclone Reconnaissance:** High-resolution atmospheric boundary layer profiling in hurricane-force winds; validated in Tropical Storm Lala environment with 19 dropsonde comparisons

2. **Polar Environment Operations:** Arctic deployment planned from Air Force C-130 aircraft; demonstrated higher employment ceiling than existing NOAA P-3 heritage

3. **Marine Atmospheric Boundary Layer Characterization:** Wind-wave alignment and surface roughness examination co-located with momentum flux measurements

4. **Expendable Platform Concept:** Air-deployed from DoD aircraft of opportunity, allowing flexible mission tasking without dedicated carrier aircraft infrastructure

5. **Ocean Array Validation:** Co-located with Pioneer Array bulk meteorology measurements for flux computation validation and surface-based reference comparisons

## Key Results

### O.1: Phase II Calibration and Validation Plan
- Four-event validation campaign defined with primary Pioneer Array site and three contingency options
- Measurement accuracy targets, response times, and validation methods specified for all core measurements
- Campaign structure designed to accumulate statistical weight on base sensing while staging algorithm validations
- Redundancy built in: failure in any single event delays but does not invalidate campaign

### O.2: Calibration and Validation Using 2026 NOAA Oceanic Flight Data

**Platform Intercomparison Results:**

*26 March Flight (3,000 ft, clear conditions):*
- Identified step-function wind errors between box legs
- Root cause: multi-hole probe pressure scaling error and magnetometer axis non-orthogonality
- Mean wind speeds comparable to P-3 and dropsondes (within expected uncertainty)

*7 April Flight (1,000 m, stratiform rain):*
- Both S0s completed full box patterns
- Paired S0 temperature agreement: 0.12–0.28°C
- Paired S0 wind speed agreement: 0.7–1.5 m/s
- S0 wind matching dropsondes at altitude: 8.1–8.5 m/s observed vs dropsonde 8.1–8.5 m/s
- P-3 flight-level wind matching on tailwind leg
- Robust precipitation performance; no step-function error after corrections

**Error Budget (root-sum-square wind error at 21 m/s true airspeed, Lakeland FL):**

1. **Magnetometer affine calibration dominates:** 1.03 m/s fleet mean, 1.58 m/s fleet worst-case
   - Axis non-orthogonality: X–Y deviation 0.06–1.79°, X–Z deviation 0.67–4.41°, Y–Z deviation 1.05–1.62°
   - Heading-dependent sinusoidal error; averages to zero around complete orbit but contaminates individual legs

2. **Magnetometer–IMU misalignment:** 0.50 m/s
   - Roll misalignment: –0.762° (±0.424 m/s sinusoidal)
   - Yaw misalignment: –0.551° (0.202 m/s constant bias)
   - Pitch misalignment: constant 0.095 m/s vertical wind bias

3. **Accelerometer bias:** 0.41 m/s
   - Bias vector: [+0.087, –0.070, +0.022] m/s²
   - Roll/pitch offsets: +0.41°/+0.51° producing ±0.23/±0.28 m/s horizontal wind errors
   - Vertical wind bias: +0.187 m/s (constant, non-averageable)

4. **Atmospheric measurement errors (pressure/temperature/humidity):** 0.018 m/s (negligible)
   - Temperature error propagation: 0.013 m/s per +0.3°C
   - Pressure error: –0.013 m/s per +1 hPa
   - Humidity error: 0.007 m/s per +4% RH

**Tropical Storm Lala Comparison (19 dropsondes):**
- Close agreement in temperature lapse rate
- Wind speed matching dropsondes at altitude
- Validates performance in cyclone conditions

### O.3: Wave Height

**Reference Estimator Validation (Method A - Batch Welch):**

*Against Independent Data:*
- Altitude independence confirmed across step-descent transect
- GFS-wave agreement bias: 0.13 ± 0.11 m
- Zero-crossing wave-count agreement: good

*Across Three Flights:*
- S00087 transects (269 m peak wavelength):
  - 10 km window: 10.0% observed scatter (10 km track length)
  - 20 km window: 9.9% observed scatter
  
- S00076 transects (338 m peak wavelength):
  - 10 km window: 15.5% observed scatter
  - 20 km window: 13.3% observed scatter

**Sequential Estimator Performance:**

*Method D (EWMA cross-covariance) selected as optimal:*
- Simplest implementation: exponentially-weighted moving average of two band-passed cross-products
- Most accurate of four methods: reproduces reference Hs within 0.04 m across three test transects
- Constant memory, no Fourier transform required
- Suitable for onboard execution (~20 FLOPS per sample)
- Reports from first sample; no spin-up distance
- State: 4 scalars + 2 IIR filter sections

*Method B (Spectral Kalman filter) findings:*
- Viable but computationally expensive: O(M²) ≈ 0.9 Mflop per sample
- Required three critical implementations:
  1. Mode spacing condition: Δk = 1/L_eff pins mode count at M = 475 for 20 km window (state dimension 950)
  2. Time-update formulation: standard exponentially-weighted recursive least squares instead