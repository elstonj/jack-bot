# AFX22.4 Phase II Final Report: Runway Integrity Validation through Soil Moisture Measurements from a Small UAS

## Document Metadata
- Type: SBIR Phase II Final Report
- Client/Agency: AFWERX, Air Force Research Laboratory (AFRL)
- Program/Solicitation: AFX224-OCSO1 Phase II, Open Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions
- Date: 2025 (completed; document created/modified August 12, 2025)
- Report Number: F2-16588
- BST Products/Systems Referenced: E2 Quadcopter, SwiftCore Flight Management System (FMS), SwiftTab control interface, Soil Moisture Mapping System (SMMS)
- Key Personnel: Jack Elston, Eryan Dai, Michael Marques, Benjamin Andre, Dan Prendergast
- Partner Organization: Weather Stream (Orbital Micro Systems, Inc. DBA Weather Stream)
- CAGE: 6PGF9

## Executive Summary
Black Swift Technologies, partnering with Weather Stream, adapted a NASA-validated L-band soil moisture sensor mounted on the E2 quadcopter UAS to assess unimproved airfield integrity for C-130 aircraft operations. The system integrates improved radiometric accuracy, thermal and vegetation sensors, and real-time processing to measure soil moisture and calculate California Bearing Ratio (CBR) in under 30 minutes—dramatically reducing risk and labor compared to manual ground-based methods using Dynamic Cone Penetrometers.

## Technical Approach

### Core System Architecture
The Soil Moisture Mapping System (SMMS) is built on three principal sensor units mounted on BST's E2 quadcopter:

1. **L-band Lobe Differencing Correlation Radiometer (LDCR)** – Core passive radiometer operating in the 1400-1427 MHz Earth Exploration Satellite Service protected band
   - Measures soil moisture via soil emissivity, which correlates with water content
   - Penetrates 100-150 mm into soil surface
   - Uses Multipath Cross Correlation Radiometry (MXCR) technology with two signal paths for improved calibration stability and RFI immunity
   - Achieves radiometric accuracy of 1.2 K brightness temperature

2. **RF Receiver Board & Digital Backend**
   - Two-path MXCR RF receiver board with improved shielding (RF absorber sheets, shielding spray)
   - ADRV9361-Z7035 FPGA board for down conversion, ADC, FFT calculation, coherence matrix computation, and accumulation
   - Real-time all-time calibration capability via two noise diodes
   - Enhanced RFI detection and mitigation through digital correlator

3. **2x2 Patch Antenna** (redesigned from previous MiCo antenna)
   - FR4 dielectric with air gap layer for improved radiation efficiency and bandwidth
   - 100 MHz bandwidth (accommodates 1400-1427 MHz operating range)
   - Narrower beamwidth (~38° vs. 45°) improves spatial resolution
   - Solid ground plane provides better RFI isolation and mechanical stability

4. **Thermal Sensor**
   - Melexis MLX90614ESF infrared thermal sensor
   - Non-contact ground surface temperature measurement (required for soil moisture calculation)
   - 35° field of view (smallest FOV, thus limits overall system footprint)

5. **NDVI Sensor**
   - Apogee Instruments S2-411/412 (replaces previous Micasense Altum)
   - Downward-looking and upward-looking components to measure vegetation health
   - Enables vegetation correction in soil moisture calculations
   - 1 Hz measurement rate

### Flight Software & Data Processing

**Onboard Processing:**
- Modular architecture with separate threads for each sensor
- Sensor controller coordinates initialization, GPS lock, time synchronization, and data collection
- Real-time telemetry streams brightness temperature, NDVI, and surface temperature to operator
- Data saved to onboard flash for post-flight processing

**Post-Processing:**
- Soil-vegetation radiative transfer model with vegetation and roughness corrections
- Calculates volumetric soil moisture (VSM) from measured brightness temperature
- Two CBR calculation approaches:
  - Mason's equation (established reference using gravimetric soil moisture)
  - New Dai equations derived during this program, tailored to agricultural vs. mountainous terrain

### UAS Integration
- E2 quadcopter platform (Group 2 sUAS, 10 kg, 125 cm tip-to-tip)
- SwiftCore Flight Management System (FMS) provides payload architecture and telemetry
- SMMS mounted on aluminum plate under fuselage with metal standoffs
- SwiftTab Android tablet control interface with dedicated SMMS App for operator control and real-time telemetry display

## Products & Capabilities Described

### BST E2 Quadcopter
- Group 2 small UAS (10 kg, ~125 cm tip-to-tip)
- Integrates Soil Moisture Mapping System payload
- SwiftCore autopilot with modular payload architecture
- Operational over unimproved terrain; previously used for soil moisture mapping with USGS, NOAA, NASA, and Toro

### Soil Moisture Mapping System (SMMS)
- **Primary capability:** Remote measurement of soil moisture (volumetric soil moisture, VSM) via passive L-band radiometry
- **Soil moisture measurement correlation:** r = 0.85-0.90 with in-situ probe data when averaged by cluster
- **Soil integrity (CBR) calculation:** Uses LDCR-derived VSM and soil type classification; moderate correlation with ground truth (r = 0.31-0.81 depending on equation and depth)
- **Spatial coverage:** Can map 800' × 60' area in ~8 minutes; full 3000' × 60' C-130 runway in <30 minutes
- **Soil penetration depth:** 100-150 mm (optimal for top-of-runway assessment)

### Radiometric Accuracy Improvements
- Brightness temperature measurement accuracy: 1.2 K (allows meaningful discernment of ~1% VSM)
- MXCR technology provides all-time calibration and RFI immunity
- New patch antenna design improves spatial resolution and interference rejection vs. previous MiCo antenna

## Use Cases & Applications

### Primary Use Case: Unimproved Runway Assessment for C-130 Operations
- DoD requirement: Ability to land C-130 and similar tactical aircraft on austere, unimproved airfields globally
- Previous method: Manual dynamic cone penetrometer (DCP) measurements—labor-intensive, time-consuming, exposes personnel to risk, yields only sparse point measurements
- SMMS advantage: Rapid, comprehensive, high-resolution soil integrity mapping of entire runway without personnel exposure

### Operational Impact
- Applicability to 160+ air operation facilities and 9,000+ worldwide air operation personnel
- 7.3 million annual aircraft operations potentially affected
- Reduces risk, operational costs, and enhances sustainability through informed decision-making

### Secondary/Future Applications (Mentioned)
- Trafficability assessments for heavy vehicle mobility
- Stability/saturation monitoring of earthen dams
- Civil engineering projects
- Potential Army applications

### Commercial Applications
- Golf course irrigation optimization (existing partnership with Toro)
- Environmental monitoring (existing partnerships with NASA, USGS, NOAA for soil moisture mapping)

## Key Results

### Soil Moisture Measurement Performance
- **Correlation with ground truth (in-situ VSM):**
  - All locations: r = 0.85
  - Averaged by cluster: r = 0.90
- **Sensor consistency:** Strong correlation between flight 1 and flight 2 brightness temperature, NDVI, and temperature maps at validation site

### California Bearing Ratio (CBR) Derivation
- **Mason's equation (baseline):** CBR = a × exp(b × GSM) with published coefficients
- **New Dai equations (terrain-specific):**
  - Agricultural land (CL-ML soil): a = 18.56, b = -0.051, RMSE = 2.73
  - Mountainous terrain (CL-ML soil): a = 53.00, b = -0.080, RMSE = 4.18
  - Improvements over Mason's equation in RMSE and correlation (r)

### CBR Correlation with Ground Truth
**At Sod Farm and Pawnee National Grasslands (calibration sites):**
- LDCR VSM → CBR (150 mm depth): r = 0.38, RMSE = 4.54 (Dai equations)
- LDCR VSM → CBR (310 mm depth): r = 0.81, RMSE = 2.91 (Dai equations)
- In-situ VSM → CBR (310 mm): r = 0.78, RMSE = 3.31 (Dai equations)

**At Elk Park Ranch Airfield (validation site, CL soil type):**
- Flight 1 LDCR → CBR (150 mm): r = 0.50, RMSE = 7.4
- Flight 1 LDCR → CBR (310 mm): r = 0.31, RMSE = 5.4
- Flight 2 LDCR → CBR (150 mm): r = 0.52, RMSE = 7.7
- Flight 2 LDCR → CBR (310 mm): r = 0.29, RMSE = 5.7
- Average in-situ CBR (310 mm): 14.25; Average SMMS CBR (Dai): 16.18; Average SMMS CBR (Mason): 14.40

### Operational Performance
- **Survey speed:** 800' × 60' area mapped in 8 minutes 7 seconds average
- **C-130 runway assessment:** 3000' × 60' runway (minimum for C-130) would require 27 minutes 54 seconds
- **Comparison to manual DCP:** Manual methods take hours; SMMS reduces assessment time by 85%+

### Sensor Validation (NDVI & Thermal)
- **Apogee NDVI vs. Micasense Altum:** Excellent correlation with small bias
- **Melexis thermal vs. Micasense thermal:** Good correlation; some bias within stated Micasense accuracy of ±5°C

## Notable Details

### Ground Truth Data Collection
- Field campaigns at Sunny Slope Sod Farm (Longmont, CO) and Pawnee National Grasslands (CO)
- Validation at Elk Park Ranch Airfield (CO), representative private grass runway
- In-situ measurements: FieldScout TDR 350 probe for VSM; KSE Model K100 Dynamic Cone Penetrometer for CBR
- Soil classification: USDA soil texture triangle mapped to USCS classifications
- Extensive soil characterization: sand/clay percentage, bulk density, depth profiles

### Terrain-Specific Modeling
- Significant difference in CBR behavior between agricultural and mountainous soil:
  - Sod Farm (agricultural): CBR < 15 (consistent with CL-ML practical range)
  - Pawnee National Grasslands & Elk Park Ranch (mountainous): CBR > 15 (due to rocky, thin soil layers, coarser composition)
- Result: Two separate empirical equations required for CL-ML soil type depending on terrain

### Limitations & Future Work
- **CBR calculation moderate correlation:** Sensor-derived CBR shows moderate (not high) correlation with ground truth due to soil variability within classifications and contributing geophysical factors beyond moisture
- **Recommended future enhancement:** P-band sensor development for deeper soil penetration (current L-band penetrates 100-150 mm; full 12-inch assessment benefits from deeper data)
- **Broader data collection need:** Thorough data collection campaign for wider range of soil types and conditions to develop tailored coefficients

### Dual-Use Applicability
- System originally developed for NASA SMAP satellite calibration; used by USGS (wildfire soil monitoring), NOAA (precipitation/hydrology studies), and commercially (Toro irrigation)
- Defense application (C-130 runway assessment) extends to Army vehicle mobility, civil engineering
- Successfully transitioned from commercial/science mission to tactical military operations
- Supports Air Force Strategic Capabilities: Air Superiority, ISR, Command and Control
- Addresses Space Force strategic gap: