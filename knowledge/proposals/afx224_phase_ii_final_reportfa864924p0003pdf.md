# Runway Integrity Validation through Soil Moisture Measurements from a small UAS

## Document Metadata
- **Type:** Phase II Final Report (SBIR)
- **Client/Agency:** U.S. Air Force / AFWERX, AFRL
- **Program/Solicitation:** AFX22.4 Phase II, Open Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions (Topic AFX224-OCSO1)
- **Date:** 11 July 2025
- **Report Number:** F2-16588
- **Contract Number:** FA864924P0003
- **BST Products/Systems Referenced:** E2 Quadcopter, SwiftCore Flight Management System, SwiftTab user interface, L-band Soil Moisture Mapping System (SMMS), LDCR (L-band Lobe Difference Correlation Radiometer)
- **Key Personnel:** Jack Elston, Eryan Dai, Michael Marques, Benjamin Andre, Dan Prendergast
- **Performing Organizations:** Black Swift Technologies LLC, Orbital Micro Systems Inc. (DBA Weather Stream)
- **CAGE:** 6PGF9

---

## Executive Summary

Black Swift Technologies, in partnership with Weather Stream, adapted a NASA-validated L-band soil moisture sensor mounted on the E2 quadcopter UAS to remotely measure soil moisture and calculate soil integrity for rapid assessment of unimproved airfields supporting C-130 aircraft operations. The enhanced system includes improved radiometric accuracy, integrated surface temperature and vegetation sensors, and real-time onboard processing. Field validation across varied soil and terrain types demonstrated strong correlation (r = 0.90) between sensor-derived and ground-measured soil moisture, with newly developed empirical models enabling runway-sized area assessment in under 30 minutes—significantly reducing risk and workload for personnel.

---

## Technical Approach

### Core System Architecture
The Soil Moisture Mapping System (SMMS) operates on three fundamental principles:
1. **L-band soil emissivity** changes significantly with soil moisture content (0.6 to 0.9 emissivity as volumetric soil moisture drops from 40% to 5%)
2. **Soil integrity/load-bearing capacity correlates** with soil moisture and soil type
3. **Passive radiometry** enables non-contact measurement of brightness temperature, which translates to soil moisture via radiative transfer models

### Hardware Components

**L-band Lobe Difference Correlation Radiometer (LDCR RevD):**
- Operates in 1400-1427 MHz Earth Exploration Satellite Service protected band
- Uses Multipath Cross Correlation Radiometry (MXCR) technology with two signal paths and matched load reference
- Achieves 1.2 K radiometric accuracy (sufficient to resolve ~1% volumetric soil moisture changes)
- Two noise diodes provide all-time internal calibration
- New 2x2 L-band patch antenna (FR4 dielectric with air layer) features:
  - Narrower beamwidth (~38°) vs. previous microstrip collinear design (~45°) for improved spatial resolution
  - Wider bandwidth (100 MHz vs. working frequency range of 27 MHz)
  - Better RFI isolation via solid ground plane
  - Enhanced mechanical stability

**RF Receiver & Digital Backend:**
- MXCR-based RF receiver board with enhanced shielding (RF absorber sheets, RF shielding spray)
- ADRV9361-Z7035 FPGA board for down-conversion, ADC, FFT calculation, coherence matrix computation
- Complex coherence matrix calculated and accumulated every 100 milliseconds
- Provides improved RFI detection and mitigation capability

**Thermal Sensor:**
- Melexis MLX90614ESF infrared sensor (non-contact)
- Measures ground surface temperature (required for soil moisture calculation)
- 35° field-of-view (smallest FOV, limits overall system footprint)
- I2C protocol communication

**NDVI Sensor:**
- Apogee Instruments S2-411/412 with upward and downward-facing units
- Measures vegetation health/volume via red and near-infrared spectral comparison
- Adjusts soil moisture calculation for vegetation cover
- 1 Hz measurement rate

**Integration with BST E2 Quadcopter:**
- Group 2 sUAS, 10 kg, 125 cm tip-to-tip
- SMMS mounted on aluminum plate secured under fuselage
- Integrates with SwiftCore Flight Management System (FMS)
- Payload architecture enables sensor command/telemetry through logically separated channels
- SwiftTab Android tablet interface provides operator control and real-time telemetry display

### Software Architecture

**Onboard Processing:**
- Modular architecture with individual threads for each sensor
- Flight software handles initialization, GPS lock detection, system time setting
- Sensor controller coordinates startup, monitors aircraft telemetry, manages data collection
- Each sensor managed by dedicated thread reading from hardware interface
- Limited onboard processing calculates single-point brightness temperature values along flight path
- Real-time telemetry streams ground surface temperature, NDVI, and L-band brightness temperature to operator

**Post-Processing:**
- Soil-vegetation radiative transfer model with vegetation and surface roughness corrections
- Brightness temperature → soil moisture conversion
- Soil moisture + soil type → California Bearing Ratio (CBR) calculation using empirical equations
- New terrain-specific coefficients derived during this program

### Soil Integrity Modeling

**Fundamental Equation:**
```
CBR = a × e^(b×θ_v)  [Equation 3]
```
Where θ_v is volumetric soil moisture, and coefficients a and b are derived for specific soil types and terrain.

**Coefficient Derivation:**
- Mason's original coefficients derived for CL-ML soil types: a=74.67, b=-0.164
- **New coefficients for Agricultural Land (CL-ML):** a=18.56, b=-0.051 (RMSE=2.73)
- **New coefficients for Mountainous Areas (CL-ML):** a=53.00, b=-0.080 (RMSE=4.18)
- Improved RMSE vs. Mason's equations across both terrain types

---

## Products & Capabilities Described

### E2 Quadcopter
- **What it is:** Black Swift Technologies' Group 2 small unmanned aircraft system
- **Modifications for this program:** Aluminum plate mounting structure, housing for thermal/NDVI sensors, serial port integration with SwiftCore payload interface
- **Specifications:** 10 kg weight, 125 cm tip-to-tip, operates via SwiftCore FMS
- **Capability demonstrated:** Successfully mapped 800' × 60' runway area in ~8 minutes

### L-band Soil Moisture Mapping System (SMMS)
- **What it is:** Integrated suite of passive microwave radiometer + thermal + vegetation sensors for soil characterization
- **Use in this program:** Primary sensor for unimproved airfield assessment; adapted from prior NASA-validated and commercial versions
- **Key performance:** 
  - Strong soil moisture correlation: r=0.90 when in-situ measurements averaged per cluster
  - Effective penetration depth: 100-150 mm
  - Real-time map generation capability
  - Can survey full C-130 runway (typically ~3000' × 100') in under 30 minutes

### SwiftCore Flight Management System
- **What it is:** Core flight control system for all BST aircraft
- **Use in this program:** Primary autopilot; provides payload architecture for SMMS command/telemetry
- **Capability:** Logically separated command/telemetry channels ensure safety/integrity of essential flight functions

### SwiftTab User Interface
- **What it is:** Android tablet-based control and telemetry application
- **Use in this program:** Operator control of SMMS modes (On/Off/Calibrating) and real-time sensor telemetry display

---

## Use Cases & Applications

### Primary Use Case: C-130 Austere Airfield Assessment
- **Mission:** Evaluate unimproved/austere landing zones globally to support C-130 cargo aircraft operations
- **Current method:** Labor-intensive manual dynamic cone penetrometer measurements by personnel on ground (places Airmen at risk)
- **BST solution benefits:** 
  - Non-contact remote measurement
  - Comprehensive area coverage vs. point measurements
  - Sub-30-minute assessment of runway-sized area
  - Reduced personnel risk
  - Real-time decision support for forward air controllers

### Strategic Air Force Capabilities Supported
- Air Superiority
- Intelligence, Surveillance, and Reconnaissance (ISR)
- Command and Control

### Strategic Space Force Capability
- Addresses "Soil Moisture" as one of 12 Category A observation gaps identified by Joint Requirements Oversight Council for Meteorology (JROC-M, 2014)

### Additional Military Applications (Identified)
- Trafficability assessments
- Monitoring stability/saturation of earthen dams
- Extends capability across 160+ air operation facilities, 9,000+ AO personnel, 7.3M annual aircraft operations

### Dual-Use Commercial Applications
- Golf course irrigation optimization (prior partnership with Toro)
- Wildfire-prone area soil moisture mapping (prior USGS California collaboration)
- Hydrometeorology research (prior NOAA SPLASH project partnership)

---

## Key Results

### Sensor Performance
1. **Soil Moisture Accuracy:**
   - LDCR-measured VSM vs. in-situ: r=0.85 across all locations
   - When averaged per cluster: r=0.90
   - In-situ spatial variability: ±10-15% VSM within single cluster at some locations

2. **Thermal & NDVI Sensor Validation:**
   - Apogee NDVI vs. Micasense NDVI: strong correlation with minimal bias
   - Melexis thermal vs. Micasense thermal: measurable but acceptable bias (Micasense stated accuracy ±5°C)
   - Thermal sensor replaced Micasense; NDVI replaced Micasense for size/weight/power/cost reduction

3. **Coefficient Development:**
   - Mason equation (original): CBR = 74.67 × e^(-0.164×θ_g), RMSE across all data = 4.25 (agricultural), 10.68 (mountain)
   - New Dai equation agricultural: RMSE improved to 2.73
   - New Dai equation mountainous: RMSE improved to 4.18
   - **Critical finding:** Different terrain types (agricultural vs. mountainous) require separate coefficients; mountainous areas show higher CBR for same moisture due to coarser, rockier soil

### Field Validation Data

**Test Sites:**
- Sunny Slope Sod Farm (SF) in Longmont, Colorado
- Pawnee National Grasslands (PNG), Colorado
- Elk Park Ranch Airfield, Colorado (final validation, mock C-130 landing site)

**Data Collection Method:**
- Lawnmower flight patterns over box-shaped footprints
- 3×3 grids of in-situ soil moisture (0.5m spacing)
- Dynamic Cone Penetrometer (DCP) measurements for CBR at each point
- USDA/USCS soil classification at each location

**Soil Types Tested:**
- CL (Clay), ML (Silt), SM (Sandy loam), CL-ML (mixed clay-silt)
- Agricultural lands and mountainous terrain
- Sand percentage: 6.9%-63.8%, Clay percentage: 10.2%-31%
- Bulk density: 1.23-1.56 g/cm³

### Final Validation at Elk Park Ranch

**Flight Performance:**
- Two validation flights (Flight 1: 10:57:26, Flight 2: 11:28:43)
- Successfully generated maps of brightness temperature, NDVI, surface temperature, and VSM
- High correlation between flight 1 and flight 2 measurements (consistent sensor performance)

**CBR Calculation Results:**
- Using newly derived mountain coefficients (Dai Eq. 3)
- Comparison metrics between airborne and in-situ CBR:
  - **CBR at 150mm depth:** r = 0.38, RMSE = 4.54 (using Dai equations on LDCR VSM)
  - **CBR at 310mm depth:** r = 0.81, RMSE = 2.91 (using Dai equations on LDCR VSM)
  - Improved vs. Mason