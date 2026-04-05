# B2: S0 Measurement Evaluation

## Document Metadata
- Type: Phase I Deliverable / Technical Task Plan
- Client/Agency: U.S. Navy
- Program/Solicitation: Navy STTR, Hazardous Weather Topic
- Date: Created 2025-07-22; Modified 2026-01-02
- BST Products/Systems Referenced: S0, S0-VTOL, MHPP (Multi-Hole Pitot Probe)
- Key Personnel: Daniel Prendergast (last editor), Josh Fromm, Maciej Stachura, James Elston

## Executive Summary
This document outlines Task B.2 of a Navy STTR Phase I program focused on S0 data analysis and enhancements. It presents a comprehensive plan for validating S0 meteorological measurements, conducting error analysis, and developing de-icing strategies. The document includes a detailed data validation plan with target uncertainties for key atmospheric parameters and summarizes extensive comparison studies validating S0 measurements against tower data, dropsondes, radiosondes, and tail Doppler radar.

## Technical Approach

### Integration & Platform Compatibility
- Evaluate integration with Navy launch platforms: sonobuoy launch systems, P-8A Poseidon external pod mounts, MH-60 helicopter mounts
- Verify compatibility with launch tubes on P-8 and MH-60 (noted as de-scoped but compatibility verification ongoing)
- Conduct mechanical tests and simulations to validate platform compatibility

### Error Analysis
- Detailed error analysis of S0 data identifying sources of uncertainty in:
  - Wind measurements
  - Turbulence estimation
  - Height calculations
- Testing planned at multiple data frequencies (100 Hz, 50 Hz, 25 Hz, 10 Hz) to determine at what frequency turbulent fields level off

### De-icing Strategy
- Heat MHP (Multi-Hole Pitot Probe) tips using PTC (Positive Temperature Coefficient) heating with thermostat control
- Evaluate Ice-X or similar de-icing compounds on wings and propellers
- Develop and execute test plan, potentially through NASA wind tunnel testing
- Note: Propeller de-icing identified as critical ("show stopper") issue requiring solution

## Products & Capabilities Described

### S0 (Small UAS)
- **Specifications:**
  - Equipped with MHPP (5-hole probe) for wind measurement at 3.5 Hz and higher frequencies
  - Carries pressure, temperature, humidity, and sea surface temperature (SST) sensors
  - Can fly at constant radius to capture turbulent fluctuations
  - Operating altitude: can fly near 10 m to 500+ m
  - Flight endurance supports extended orbits for atmospheric profiling
  
- **Current Capabilities:**
  - High-frequency wind measurements (100 Hz capable)
  - Calculation of drag coefficient (CD), heat transfer coefficients (CH, CE), momentum flux, turbulent kinetic energy (TKE)
  - Vertical and horizontal wind profiling
  - Thermodynamic profiling (temperature, humidity, pressure)
  - SST measurement via MLX90614ESF infrared sensor
  - Self-quality control technique for wind validation using GPS speed-over-ground

- **Unique Advantage:**
  - Only instrument currently on aircraft capable of taking high-quality measurements to calculate exchange coefficients (CD, CH, CE) critical for tropical cyclone (TC) intensity forecasting

### S0-VTOL
- Same avionics and sensors as S0
- Successfully flown with identical sensor suite in clear air testing (ISARRA 2024)

## Data Validation Plan

### Target Uncertainties & Validation Methods

| Parameter | Current/Desired Value | Validation Methods |
|-----------|----------------------|-------------------|
| **Pressure** | 1 hPa uncertainty | Dropsondes, tower data, wind tunnel |
| **Relative Humidity** | 4% uncertainty; 0.3-10s response | Dropsondes, tower data, wind tunnel, humidity chamber |
| **Temperature** | 0.3°C uncertainty; 0.5s response | Dropsondes, tower data, instrumented wind tunnel |
| **3D Winds** | 0.2 m/s uncertainty | Tower data, wind tunnel with moving aircraft, dropsonde (2D only) |
| **SST** | 0.3°C uncertainty | Sonobuoys, fixed platforms |
| **Significant Wave Height** | ±0.2m (good) to ±2m (acceptable) | SASCWATCH comparison, dominated by longer wavelengths |
| **Mean Squared Slope** | 10% accuracy target | SASCWATCH comparison |

### Derived Quantities (Onboard Algorithm Development)
Plans to develop real-time onboard algorithms for:
- **Drag Coefficient (CD)** - critical for storm intensity prediction
- **Momentum Flux**
- **Turbulent Kinetic Energy (TKE)**
- **Heat Transfer Coefficients (CH, CE)** - high uncertainty in high winds (>100% currently)
- **Sensible Heat Flux**
- **Latent Heat Flux**
- **Enthalpy Flux**

### Key Methodological Considerations
- Response time mismatch: Temperature and humidity sensors have different response rates than MHPP wind measurements; careful co-location in space and time required for covariance calculations
- Frequency response testing: Will evaluate calculations at 100 Hz, 50 Hz, 25 Hz, and 10 Hz to determine minimum sampling frequency
- Note: Vaisala RS41-NG radiosondes used as reference standard; Vaisala RH considered "gold standard"

## Use Cases & Applications

### Tropical Cyclone (TC) Research
- Primary application for high-frequency measurements of exchange coefficients
- Deloach et al. (2025) demonstrated TC sampling capability in back-and-forth flight legs near 10 m altitude
- Exchange coefficients (CD, CH, CE) directly support TC intensity forecasting
- Historical deployment: Hurricane reconnaissance (Ernesto, Edouard, Milton - 2024)

### Atmospheric Boundary Layer Studies
- Clear air profiling missions
- Turbulence characterization
- Vertical structure measurement up to 500+ m altitude
- Ocean surface interaction studies

### Naval Operations Context
- Hazardous weather characterization and prediction support
- Maritime atmospheric measurements
- Integration with Navy platforms (P-8A Poseidon, MH-60 helicopters)

## Key Results from Validation Studies

### 1. SGP Comparison (2021 - Lamont, Oklahoma)
- **Deployment:** 29 March - 3 April 2021 at DOE ARM Southern Great Plains facility
- **Method:** 10 S0 flights compared against 60 m instrumented tower with 3D sonic anemometer, temperature, and humidity sensors
- **Findings:**
  - Time series of U and V winds showed good agreement with tower data
  - Developed novel "self-QC" technique using GPS speed-over-ground for wind validation (independent of 5-hole probe)
  - Power spectral density (PSD) of 3-axis tower winds provided target structure for UAS wind estimates
  - Technique useful for checking bulk wind bias; cannot capture higher frequency turbulent structure

### 2. Dropsonde Comparison (2023)
- **Method:** S0 flights conducted in clear air with dropsondes deployed before/after
- **Findings:**
  - Wind speed and direction of dropsondes at S0 altitude showed good agreement
  - S0 PSD shows good frequency response for u, v, w winds, though u and v deviate slightly from expected -5/3 power law fit
  - Dropsondes show significant missing structure compared to S0 measurements, indicating superior temporal resolution of S0
  - Confirms S0's ability to capture atmospheric structure that point measurements miss

### 3. Deloach et al. (2025) - Exchange Coefficient Calculations
- **Methodology:** Calculated from 8 flight path legs near 10 m altitude using 3.5 Hz measurements in low-wind conditions
- **Results:**
  - Successfully computed momentum flux, sensible heat flux, and latent heat flux
  - Derived exchange coefficients: CD, CH, CE
  - Drag coefficient (CDN) values and momentum velocity (u*) calculated across wind speed range
  - Heat and moisture transfer coefficients quantified, showing relationship to wind speed
  - BST MHPP confirmed as only active airborne instrument capable of these high-quality measurements
  - Current uncertainty in CD, CH, CE exceeds 100% in high winds; S0 measurements support improved characterization

### 4. Clear Air Test Flights (2024)
**2024-03-20 Flight:**
- 8 streamsondes and 1 dropsonde within 5 km and 20 minutes of S0 (other data excluded)
- S0 flight time: ~50 min at 830 hPa, 22 min at 950 hPa, final minutes at 985 hPa; other altitudes descended rapidly at 3.5 m/s
- **Humidity:** Good agreement across all instruments; dropsonde showed slight deviation 900-950 hPa
- **Temperature:** Dropsonde read colder than streamsondes; S0 agreed better with streamsondes but sometimes warmer (~0.9°C in lower atmosphere, possibly due to 1-hour time difference)
- **Winds:** Mean u and v components agreed well across platforms; S0 missed some structure 900-930 hPa during rapid descent; wind histograms at 1740 m and 605 m MSL showed mean agreement, though tight spiral flight pattern produced some outliers
- **Note:** S0 mostly flew tight spirals during this test, introducing issues with wind estimation requiring further analysis

**2024-03-21 Flight:**
- Only one nearby Vaisala sonde (15 km away)
- S0 flew 30+ minutes after radiosonde
- Humidity mismatch at lower values (uncertain which instrument correct)
- Temperature offset observed; unclear if due to instrument difference or atmospheric warming during time gap
- Wind "turn issue" persisted but improved with more straight legs; wind direction tracking better during straight segments

### 5. Tail Doppler Radar (TDR) Comparison (2024)
- **Comparison Altitude:** 500 m (TDR vertical resolution limit)
- **Test Cases:** Hurricane Ernesto and Hurricane Edouard
- **Findings:** S0 wind speed measurements aligned well with TDR observations for both storms, validating S0 wind measurement reliability in tropical cyclone environment

### 6. ISARRA (2024)
- **Platform:** S0-VTOL with same avionics and sensors as S0
- **Location:** 1000' elevation near downtown Tulsa
- **Comparison:** Vertical wind data vs. NCAR Fast Eddy model
- **Result:** Very good vertical wind agreement with Fast Eddy, validating S0 measurement capability
- **Credit:** James Pinto (NCAR)

## Notable Details

### Partnerships & Collaborators
- **Academic:** Embry-Riddle Aeronautical University (ERAU), University of Michigan (UM), Old Dominion University (ODU)
- **Government/Research:** NOAA (Joe Cione, Jun Zhang), NCAR, DOE ARM facility, NCAR EOL Calibration Laboratory
- **Project Links:** 
  - SASCWATCH (ONR-funded MURI investigating CD variations in tropical cyclones)
  - Deloach et al. (2025) ongoing work on exchange coefficients
  - FastEddy model validation (James Pinto, NCAR)

### Technical References & Data Sources
- Vaisala RS41-NG radiosonde: 130 ms measurement delay; considered reference standard for humidity (RH) and pressure-temperature data
- SST sensor: Melexis MLX90614ESF infrared thermometer
- Wave height validation: SASCWATCH project baseline
- Wind tunnel testing: Potential access through John's contact (NASA); ERAU wind tunnel; NCAR EOL calibration chamber

### Outstanding Questions & Development Items
1. **Icing Mitigation:** Propeller de-icing identified as critical unsolved problem; heating solution confirmed adequate for MHP tips; wing treatment (Ice-X compound) requires testing
2. **Frequency Response:** Determining minimum sampling frequency for CD/CH/CE calculations remains open question; test matrix planned (100/50/25/10 Hz)
3. **Response Time Compensation:** Temperature/humidity sensors slower than MHPP; need methodology to ensure proper space-time co-location for covar