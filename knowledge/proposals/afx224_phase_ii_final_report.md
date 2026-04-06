# AFX22.4 Phase II Final Report

## Document Metadata
- **Type**: SBIR Phase II Final Report
- **Client/Agency**: AFWERX, Air Force Research Laboratory (AFRL)
- **Program/Solicitation**: SBIR Topic AFX224-OCSO1 Phase II; Open Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions
- **Date**: Report completed 2025 (document modified August 19, 2025)
- **Report Number**: F2-16588
- **BST Products/Systems Referenced**: E2 Quadcopter, SwiftCore Flight Management System, SwiftTab user interface, L-band Soil Moisture Mapping System (SMMS)
- **Key Personnel**: Jack Elston, Eryan Dai, Michael Marques, Benjamin Andre, Dan Prendergast
- **Partner Organization**: Weather Stream (Orbital Micro Systems, Inc.)
- **CAGE Code**: 6PGF9

## Executive Summary

Black Swift Technologies, in partnership with Weather Stream, successfully adapted a UAS-mounted L-band soil moisture sensor to rapidly assess soil integrity for C-130 aircraft operations on unimproved airfields. The system integrates an L-band radiometer with thermal and vegetation sensors on BST's E2 quadcopter, enabling remote measurement of soil moisture and calculation of California Bearing Ratio (CBR) in under 30 minutes for a C-130-sized runway. Field validation demonstrated strong correlation between sensor-derived soil moisture and ground measurements (r = 0.90), with new empirical models developed for converting soil moisture to CBR tailored to agricultural and mountainous terrains.

## Technical Approach

### Core System Architecture
The Soil Moisture Mapping System (SMMS) comprises three principal sensor units plus digital processing:

1. **L-band Lobe Differencing Correlation Radiometer (LDCR)**
   - Operates in protected 1400-1427 MHz band
   - Uses Multipath Cross Correlation Radiometry (MXCR) technology with two-path RF receiver board
   - Includes two noise diodes for all-time calibration
   - Measures brightness temperature with 1.2 K accuracy (1% volumetric soil moisture equivalent)
   - Penetrates 100-150 mm into soil surface
   - New 2x2 patch antenna (FR4 dielectric) replaces previous microstrip collinear design
   - Narrower beamwidth (~38° vs 45°) improves spatial resolution
   - Improved RF shielding reduces interference from UAS and instrument itself

2. **Digital Back End**
   - ADRV9361-Z7035 FPGA board for down conversion, ADC, FFT, coherence matrix calculation
   - Complex coherence matrix accumulated every 100 milliseconds
   - Enables RFI detection and mitigation
   - Supports modular software architecture with separate sensor threads

3. **Thermal Sensor**
   - Melexis MLX90614ESF infrared sensor
   - Measures ground surface temperature via emitted IR radiation
   - 35° field of view (smallest of three primary sensors, limiting overall footprint)
   - I2C communication protocol

4. **NDVI Sensor**
   - Apogee Instruments S2-411/412
   - One downward-looking, one upward-looking unit
   - Measures vegetation health and volume via red and near-infrared spectra comparison
   - Adjusts soil moisture calculation for vegetation effects
   - 1 Hz reporting rate

### Flight Software Architecture
Modular design with:
- Main flight software handling system initialization and component coordination
- Sensor controller monitoring aircraft telemetry, GPS lock, system time, and sensor startup
- Sensor-specific threads for each sensor with independent sampling rates
- Onboard data logging to flash storage
- Real-time telemetry transmission to operator (ground surface temperature, NDVI, brightness temperature)
- Limited onboard processing for periodic single-point brightness temperature calculation

### Post-Processing for Soil Integrity Calculation
1. Soil moisture calculated using soil-vegetation radiative transfer model with vegetation and surface roughness corrections
2. Two approaches for CBR calculation:
   - Mason's empirical equation (established baseline)
   - New Dai coefficients developed during this program, differentiated by terrain type

### UAS Integration
- BST E2 Quadcopter (Group 2, 10 kg, ~125 cm tip-to-tip)
- SwiftCore Flight Management System (FMS) as core flight control
- Payload architecture enables sensor control and telemetry transmission
- SMMS mounted on aluminum plate under fuselage with metal standoffs
- NDVI and thermal sensors housed with serial port for E2 payload interface
- SwiftTab control interface (Android tablet) provides operator control via "App Data" channels

## Products & Capabilities Described

### E2 Quadcopter
- **What it is**: Group 2 small unmanned aircraft system, primary airframe for SMMS payload
- **Specifications**: 10 kg weight, ~125 cm tip-to-tip, operates with SwiftCore FMS
- **Use in this context**: Modified to carry integrated SMMS for runway soil integrity assessment
- **Performance claim**: Can survey 800' x 60' area in ~8 minutes; full C-130 runway (3000' x 60') in under 30 minutes

### SwiftCore Flight Management System
- **What it is**: Core flight control system for all BST aircraft
- **Capabilities**: Modular payload architecture with logically separated command/telemetry channels from essential flight functions; safety and integrity of flight functions maintained
- **Use**: Manages SMMS sensor control, telemetry transmission, and payload integration

### SwiftTab User Interface
- **What it is**: Android tablet-based operator control application
- **Use**: Allows operator to set SMMS modes (On, Off, Calibrating) via Channel 0; displays real-time sensor telemetry via Channel 1

### L-band Soil Moisture Mapping System (SMMS)
- **What it is**: Integrated remote sensing payload for measuring soil moisture and deriving soil integrity
- **Specifications**:
  - Brightness temperature accuracy: ±1.2 K
  - Soil moisture penetration depth: 100-150 mm
  - NDVI sensor accuracy: validated against Micasense Altum with strong correlation
  - Thermal sensor accuracy: stated ±5°C (some bias noted vs. Micasense)
- **How it was proposed to be used**: Mounted on E2 to rapidly assess unimproved airfields for C-130 operations
- **Key enhancements from Phase II**:
  - Improved radiometric accuracy through enhanced PCB shielding and isolation
  - New 2x2 patch antenna with narrower beamwidth and better RFI isolation
  - Integration of Apogee NDVI and Melexis thermal sensors (replacing Micasense Altum)
  - Real-time data processing and telemetry onboard
  - Modular flight software enabling both onboard and post-flight processing
  - Soil-specific CBR empirical models

## Use Cases & Applications

### Primary Use Case: C-130 Runway Assessment
- **Mission**: Rapid soil integrity evaluation of unimproved/austere airfields
- **Operational scenario**: Forward air controllers require soil condition data before C-130 landing operations
- **Impact scope**: Potentially spans 160+ air operation facilities, 9,000 worldwide AO personnel, 7.3 million annual aircraft operations
- **Specific requirement**: Minimum runway length for C-130 peacetime ops: 3000' x 60'
- **Current manual process**: Labor-intensive, time-consuming cone penetrometer measurements; places personnel in harm's way

### Validation Sites
1. **Sod Farm (SF), Longmont, Colorado**
   - Agricultural land with varied terrain and vegetation
   - Soil types: CL, SM, ML classifications
   - Soil bulk density: 1.23-1.56 g/cm³
   
2. **Pawnee National Grasslands (PNG), Colorado**
   - Mountainous terrain
   - Soil types: ML, CL, SM
   - Higher measured CBR values (>15 in places) due to rocky, coarse soil layers
   
3. **Elk Park Ranch Airfield, Colorado**
   - Privately owned grass runway representative of potential C-130 landing site
   - Final validation/demonstration location
   - Soil type: CL (loam) at surface, with GC (clay gravel) component
   - Runway dimensions: 800' x 60' test area

### Secondary/Dual-Use Applications
- Commercial soil moisture mapping for golf course irrigation optimization (partnership with Toro)
- Army vehicle trafficability assessments
- Earthen dam stability/saturation monitoring
- Wildfire-prone area soil moisture monitoring (USGS California Water Science Center)
- Hydrometeorology research (NOAA SPLASH project)
- NASA satellite calibration platform (SMAP mission)

## Key Results

### Sensor Validation (Field Testing Phase)

**Soil Moisture Measurement Correlation:**
- LDCR-measured volumetric soil moisture (VSM) vs. in-situ measurements at all locations: **r = 0.85**
- When averaged by cluster: **r = 0.90**
- In-situ VSM variability within clusters: up to 10-15% at some locations

**Thermal Sensor Validation (Melexis vs. Micasense Altum):**
- Correlation coefficient: Not explicitly stated, but described as showing "similarity of contours"
- Noted bias within stated ±5°C Micasense accuracy
- NDVI Sensor Validation (Apogee vs. Micasense Altum):
- Strong correlation with "very small bias"

### California Bearing Ratio (CBR) Calculation

**Original Mason Equations (Baseline):**
- Exponential relationship: CBR = a × exp(b × GSM)
- Mason parameters for CL-ML: a = 74.67, b = -0.164
- RMSE (agricultural): 4.25; (mountain): 10.68

**New Dai Equations (Derived Phase II):**
Separate coefficients for terrain types in Eq. 3: CBR = a × exp(b × VSM)

- **Agricultural land (CL-ML soil)**:
  - a = 18.56, b = -0.051
  - RMSE: 2.73 (improvement of 36% vs. Mason)
  
- **Mountainous areas (CL-ML soil)**:
  - a = 53.00, b = -0.080
  - RMSE: 4.18 (improvement of 61% vs. Mason)

**Correlation Performance (Training Data - SF and PNG):**

| Metric | LDCR VSM + Mason | LDCR VSM + Dai | In-situ VSM + Mason | In-situ VSM + Dai |
|--------|------------------|----------------|---------------------|------------------|
| CBR (150mm) | r = -0.02, RMSE = 8.59 | r = 0.38, RMSE = 4.54 | r = 0.43, RMSE = 5.10 | r = 0.51, RMSE = 4.72 |
| CBR (310mm) | r = 0.57, RMSE = 5.69 | r = 0.81, RMSE = 2.91 | r = 0.73, RMSE = 4.59 | r = 0.78, RMSE = 3.31 |

### Final Validation (Elk Park Ranch Airfield)

**Measured vs. Calculated CBR (7 ground collection points, 310mm depth):**
- **In-situ measured average CBR**: 14.25
- **SMMS-calculated CBR (Dai coefficients)**: 16.18
- **SMMS-calculated CBR (Mason coefficients)**: 14.40

**Correlation with In-Situ Measurements:**

| Flight | Equation | CBR (150mm) | CBR (310mm) |
|--------|----------|-------------|------------|
| Flight 1 | Mason | r = 0.56, RMSE = 6.7 | r = 0.37, RMSE = 6.1 |
| Flight 1 | Dai | r = 0.50, RMSE = 7.4 | r = 0.31,