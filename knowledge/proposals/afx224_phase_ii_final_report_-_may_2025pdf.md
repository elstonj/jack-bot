# AFX22.4 Phase II Final Report - Runway Integrity Validation through Soil Moisture Measurements from a Small UAS

## Document Metadata
- **Type:** SBIR Phase II Final Report
- **Client/Agency:** U.S. Department of the Air Force (DAF) / AFWERX, Air Force Research Laboratory (AFRL)
- **Program/Solicitation:** SBIR Topic AFX224-OCSO1 Phase II; Open Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions
- **Date:** May 2025
- **Report Number:** F2-16588
- **Contract Number:** FA864924P0003
- **CAGE Code:** 6PGF9
- **BST Products/Systems Referenced:** E2 Quadcopter, L-band Soil Moisture Mapping System (SMMS), L-band Lobe Difference Correlation Radiometer (LDCR), SwiftCore Flight Management System, SwiftTab control interface
- **Partner Organization:** Orbital Micro Systems, Inc. (DBA Weather Stream)
- **Key Personnel:** Jack Elston, Eryan Dai, Michael Marques, Benjamin Andre, Dan Prendergast

## Executive Summary
Black Swift Technologies, in partnership with Weather Stream, developed and validated a UAS-mounted L-band radiometer system to remotely measure soil moisture and calculate soil integrity (California Bearing Ratio) for rapid assessment of unimproved airfields supporting C-130 aircraft operations. The enhanced system integrates improved radiometric accuracy, an integrated thermal sensor, NDVI sensor, and real-time data processing. Field validation demonstrated strong correlation (r = 0.90) between sensor-derived and ground-measured soil moisture, with newly derived CBR equations tailored to agricultural and mountainous terrains. The system can evaluate a runway-sized area (800' × 60') in under 30 minutes—significantly faster than manual methods.

## Technical Approach

### Core Technology Foundation
The system is built on two established principles:
1. **Soil moisture correlation:** Volumetric soil moisture (VSM) is strongly correlated with L-band soil emissivity (changes from ~0.6 to ~0.9 as VSM drops from 40% to 5%)
2. **Soil integrity correlation:** Soil load-bearing capacity (CBR) correlates with soil moisture and soil type

### Key Technical Modifications (Phase II)

**L-band Radiometer (LDCR) Improvements:**
- Modified PCB design with enhanced RF shielding and component isolation
- Implemented Multipath Cross Correlation Radiometry (MXCR) technology for improved calibration stability and RFI mitigation
- Radiometric measurement accuracy: 1.2 K (corresponding to ~1% VSM)
- Two-path RF receiver board with dual noise diodes for all-time calibration
- New 2x2 L-band patch antenna design (FR4 substrate with air gap):
  - Narrower beamwidth (~38° vs. 45° previous design) improves spatial resolution
  - Wider bandwidth (100 MHz vs. 27 MHz operating range) accommodates integration shifts
  - Better RFI isolation via solid ground plane
  - Operates in protected 1400-1427 MHz Earth Exploration Satellite Service band

**Digital Processing:**
- FPGA-based digital backend (ADRV9361-Z7035) performs:
  - Down conversion, analog-to-digital conversion (ADC)
  - Fast Fourier Transform (FFT) calculation
  - Coherence matrix calculation and accumulation (100 ms intervals)
- Real-time onboard telemetry to operator
- Post-flight rapid soil moisture and CBR calculation via radiative transfer model

**Sensor Integration:**
- **Thermal Sensor:** Melexis MLX90614ESF IR thermal sensor (non-contact ground surface temperature, I2C protocol, 35° FOV)
- **NDVI Sensor:** Apogee Instruments S2-411/412 (upward and downward-looking to measure vegetation health via red/near-IR spectra, 1 Hz sample rate)
- Validated sensor replacements (from Micasense Altum) for reduced size, weight, power, and cost

**UAS Platform Adaptation:**
- Integrated into BST E2 Quadcopter (Group 2 sUAS, 10 kg, ~125 cm tip-to-tip)
- Components mounted on aluminum plate under fuselage using metal standoffs
- Custom NDVI/thermal sensor housing with serial port interface
- SwiftCore Flight Management System enables payload control and telemetry transmission via secure, logically separated software channels
- SwiftTab Android tablet control interface with real-time sensor telemetry display

### Soil Integrity Calculation Models

**Exponential CBR-Moisture Relationship:**
Three equations used to calculate California Bearing Ratio from volumetric soil moisture:

1. **Mason's Original Equation (Eq. 1):**
   - CBR = a·e^(b·θ_g)
   - Parameters fixed by soil USCS type (CL=1.39, ML=1.18, CL-ML=1.34, SM=1.50 bulk density)
   - RMSE: 4.25 (agricultural), 10.68 (mountain)

2. **New Agricultural Land Equation (Eq. 3):**
   - CBR = a·e^(b·θ_v)
   - CL-ML soil group: a=18.56, b=-0.051
   - RMSE: 2.73
   - Direct VSM input (no gravimetric conversion needed)

3. **New Mountainous Terrain Equation (Eq. 3):**
   - CL-ML soil group: a=53.00, b=-0.080
   - RMSE: 4.18
   - Accounts for thin, rocky soil layers vs. deep agricultural soils

**Soil Classification:**
- USDA and USCS soil frameworks used
- Sand/clay percentages mapped to USCS classifications via USDA texture triangle
- SF (Sod Farm) represents agricultural terrain; PNG (Pawnee National Grasslands) represents mountainous terrain

## Products & Capabilities Described

### Black Swift E2 Quadcopter (Soil Integrity Configuration)
- **Function:** Carries integrated soil moisture mapping payload
- **Specifications:** Group 2 sUAS, 10 kg, ~125 cm tip-to-tip
- **Flight Control:** SwiftCore FMS with secure payload architecture
- **Demonstrated Performance:** Maps 800' × 60' runway area in ~8 minutes; full C-130 runway (estimated <30 minutes)

### L-band Soil Moisture Mapping System (SMMS)
- **Components:** LDCR radiometer, RF processing board, thermal sensor, NDVI sensor, digital processor
- **Measurement Parameters:** 
  - L-band brightness temperature (1400-1427 MHz)
  - Ground surface temperature
  - NDVI (vegetation index)
  - Volumetric soil moisture (VSM)
  - California Bearing Ratio (CBR) / soil integrity
- **Spatial Resolution:** Approximately 35° FOV (limited by thermal sensor)
- **Processing:** Real-time onboard calculation; full post-processing in <30 minutes
- **Accuracy:** Soil moisture correlation r=0.90; radiometric accuracy 1.2 K

### SwiftCore Flight Management System
- Payload architecture enabling sensor control and telemetry transmission
- Secure software channels separating payload from flight-critical autopilot functions
- Integration with SwiftTab control interface

### SwiftTab User Interface
- Android tablet-based control station
- Real-time telemetry display of:
  - Ground surface temperature
  - NDVI values
  - L-band brightness temperature
  - Sensor mode control (On/Off/Calibrating)

## Use Cases & Applications

### Primary Use Case: C-130 Airfield Assessment
- **Mission:** Rapid soil integrity evaluation of unimproved/austere landing zones
- **Benefit:** Replaces labor-intensive manual dynamic cone penetrometer measurements; removes personnel from airfield
- **Operational Impact:** 
  - Evaluates full C-130 runway in <30 minutes (vs. hours for manual methods)
  - Provides spatial mapping (not just point measurements)
  - Reduces risk and workload for Air and Space Force personnel
- **Scale:** Potentially impacts 160+ air operations facilities, 9,000+ worldwide AO personnel, 7.3 million annual aircraft operations

### Secondary Use Cases
- **Commercial:** Golf course soil moisture mapping (partnership with Toro for smart irrigation optimization)
- **Environmental/Scientific:** 
  - Wildfire-prone area monitoring (USGS partnership in California)
  - NOAA SPLASH project (precipitation and hydrometeorology studies)
  - NASA SMAP satellite calibration platform
- **Army Applications:** Trafficability assessments, earthen dam stability/saturation monitoring

### Strategic Alignment
- **Air Force Strategic Capabilities:** Air Superiority, Intelligence/Surveillance/Reconnaissance (ISR), Command and Control
- **Space Force Technology Strategy:** Addresses Category A observation gap (soil moisture) identified by JROC-M 2014 study; supports global persistent awareness and informed mission planning

## Key Results

### Sensor Validation
- **NDVI Sensor Replacement:** Apogee NDVI sensor shows strong visual and statistical correlation with Micasense Altum (very small bias, similar contours)
- **Thermal Sensor Replacement:** Melexis IR thermal sensor validated as adequate replacement; some bias noted but within stated Micasense accuracy (±5°C)

### Soil Moisture Measurement Accuracy
- **LDCR vs. In-Situ VSM:** Correlation coefficient r=0.85 (all points), r=0.90 (cluster averages)
- **Testing Locations:** Sunny Slope Sod Farm (SF) and Pawnee National Grasslands (PNG)
- **Soil Types Tested:** Sandy loam (SM), clay loam (CL), silt loam (ML), silty clay loam
- **In-Situ Variability:** VSM can vary 10-15% within one measurement cluster

### CBR/Soil Integrity Results

**Calibration Data Collection:**
- Ground truth: KSE K100 Dynamic Cone Penetrometer (DCP), FieldScout TDR 350 moisture probe
- Measurement Protocol: 9-point 3×3 grid per location (~0.5 m spacing), single DCP test per cluster
- CBR measured to 1 meter depth

**New Coefficient Performance:**
- Agricultural land equation (CL-ML): RMSE=2.73 (vs. Mason's 4.25)
- Mountainous terrain equation (CL-ML): RMSE=4.18 (vs. Mason's 10.68)
- Significant improvement in RMSE for both terrain types

**Verification Flight at Elk Park Ranch:**
- Demonstrated real-world runway assessment scenario
- Two sequential flights collected TB (brightness temperature), NDVI, TP (ground surface temperature) maps
- CBR maps generated from both flights using Eq. 1 and newly derived Eq. 3
- Moderate correlation between airborne and in-situ CBR measurements
- Particularly strong correlation when using terrain-specific coefficients

### System Performance
- **Flight Speed:** Maps 800' × 60' area in ~8 minutes
- **Projected Full Runway:** <30 minutes for C-130-length runway
- **Data Processing:** Rapid post-processing enables near-real-time CBR maps
- **Real-Time Telemetry:** Operators receive brightness temperature, ground temperature, and NDVI during flight

## Notable Details

### Technical Innovations
1. **Improved RFI Mitigation:** 
   - RF absorber sheets and shielding spray applied to receiver/digital backend cases
   - MXCR architecture and FFT-based RFI detection enable better immunity to interference
   - Critical for UAS-mounted operation near aircraft RF sources

2. **Antenna Design Advancement:** 
   - 2×2 patch antenna provides narrower beamwidth (38°) than previous collinear design (45°)
   - Improves spatial resolution at same flight altitude
   - FR4 construction with air gap optimizes radiation efficiency and bandwidth

3. **Terrain-Specific Modeling:** 
   - Recognition that agricultural soil (deep, well-maintained) exhibits different CBR response to moisture than mountainous soil (thin, rocky)
   - Derivation of separate equations significantly