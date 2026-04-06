# Canton Report: Soil Moisture Mapping sUAS Preliminary Deployment Report

## Document Metadata
- **Type:** Technical Report (Flight Test Report)
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR Phase II, Contract Number NNX14CG09C
- **Date:** October 2015
- **BST Products/Systems Referenced:** Tempest sUAS, SwiftPilot Pro autopilot, SuperSwift (proposed successor), LDCR (L-band Dicke Radiometer), NDVI sensors, SwiftCore data logger
- **Key Personnel:** Maciej Stachura (report editor/contact)
- **Location/Test Site:** Canton, Oklahoma

## Executive Summary
This report documents the preliminary results from a flight deployment of Black Swift Technologies' Tempest sUAS equipped with soil moisture mapping (SMM) payload at Canton, Oklahoma in September 2015. The deployment consisted of 3 flights totaling 5 mapping runs, demonstrating the integration of radiometer, NDVI, thermal, GPS, IMU, and laser altimetry systems. While the system successfully gathered brightness temperature maps and validated autopilot performance, several operational and thermal management issues were identified that informed the design transition toward the commercial SuperSwift platform.

## Technical Approach

### System Architecture
The SMM Tempest integrated multiple sensor systems:
- **L-band Dicke Radiometer (LDCR):** Primary soil moisture sensing instrument with up-looking and down-looking channels
- **NDVI System:** Red and near-infrared sensors (up and down facing) for vegetation correction
- **Thermal Sensors:** Up and down facing thermal imaging
- **Navigation:** GPS, IMU, laser altimeter (disabled during deployment)
- **Autopilot:** SwiftPilot Pro for autonomous waypoint navigation
- **Data Logging:** On-board logging with planned FPGA upgrade to 60 Ms/sec

### Mission Execution
- **Aircraft:** BST Tempest (N738SW), Certificate of Authorization #2014-CSA-200-COA
- **Payload Weight:** 15.8 lbs
- **Flight Duration:** 18–22 minutes per flight (limited by ESC thermal issues)
- **Mapping Altitude:** 25–55 m AGL; nominal 30 m for 30 m waypoint spacing
- **Coverage:** 5 mapping runs with 15 m spacing (Flight 1) and 30 m spacing (Flights 2–3)

### EMI Mitigation Strategy
Prior to deployment, significant L-band radiometer noise (1000 mV on 3300 mV range) was traced to the motor/ESC/battery system. Two filtering approaches failed (quarter-wavelength stub filter and Lorch bandpass filter). Successful solution involved comprehensive electromagnetic shielding:
- ESC, motor cables, propulsion battery, avionics battery, power distribution board wrapped in copper foil
- All copper elements connected to common ground
- Ventilation holes added to ESC wrap to prevent overheating
- Ground tests confirmed noise elimination; flight data validated the fix

### Radiometer Data Processing
Brightness temperature maps generated from two mapping runs using:
1. Interpolation of navigation data to radiometric time grid
2. Dropping 5 samples during calibration state transitions
3. Uniform window averaging (80 samples) per calibration state
4. Four calibration states solved simultaneously:
   - State 0: Vout = V0 + gain0*(Tref2 - Tref1)
   - State 1: Vout = V0 + gain1*(Tu - Tref1)
   - State 2: Vout = V0 + gain2*(Tref2 - Td)
   - State 3: Vout = V0 + gain3*(Tu - Td)
5. LDCR gain calibration performed over water with known atmospheric/water brightness temperatures
6. Pixel size calculation based on altitude, incident angle, and antenna pattern (pixel size = flying altitude)

### Autopilot Control Assessment
**Altitude Control (Longitudinal):**
- No tuning performed across all mapping runs (used consistent gains throughout)
- Standard deviation of 0.78 cm across all 5 mapping missions
- Maximum error: 5.15 m
- Performance sufficient for soil moisture measurement despite disabled laser altimeter

**Waypoint Tracking (Lateral):**
- Progressive tuning between Flight 1 and Flight 2 improved performance
- Final achieved: 0.74 m standard deviation, 2.35 m maximum error
- Wind speeds during deployment: 3.8–4.9 m/s (8.5–11.0 mph)
- Tracking accuracy better than uncorrected GPS accuracy despite wind at ~21% of cruise speed

## Products & Capabilities Described

### Tempest sUAS
- **Role:** Experimental platform for SMM payload
- **Performance:** Nominal 1-hour flight time; achieved ~22 minutes with SMM payload due to thermal constraints
- **Constraints:** Narrow fuselage diameter limited payload access; bungee launcher susceptible to grass snagging; poor ventilation for ESC/motor cooling
- **Weight at Deployment:** 15.8 lbs total
- **Launch Requirements:** Two-person bungee launch at this weight; required expert pilot for landing

### L-band Dicke Radiometer (LDCR)
- **Configuration:** MiCo dual-polarized antenna with 1.4–1.5 GHz passband
- **Channels:** Up-looking (atmospheric), down-looking (soil/surface)
- **Calibration:** Four-state calibration using reference loads and sky view
- **Performance:** Successfully mitigated motor noise through shielding; data quality validated
- **Results:** 
  - Flight 2015-09-08 (dry conditions): Mean brightness temperature 316.9 K (range 294.7–338.8 K)
  - Flight 2015-09-09 (morning, damper soil): Mean brightness temperature 297.3 K (range 267.7–323.4 K)
  - Trend validation: Lower brightness temperature correlated with damp soil from overnight dew

### NDVI Sensor Package
- **Configuration:** Red and near-infrared sensors (up/down facing)
- **Issue:** Both upward and downward sensors saturated under cloud cover despite lower light levels
- **Workaround:** Satellite data used for NDVI calculation in this deployment
- **Resolution:** New calibrated sensors procured from Decagon for SuperSwift to address saturation

### Thermal Sensor Package
- **Configuration:** Up and down facing thermal sensors
- **Performance:** Down-facing sensor correlated well with air temperature; no field validation performed
- **Status:** Scheduled for controlled environment validation

### SwiftPilot Pro Autopilot
- **Capabilities:** Autonomous waypoint navigation, altitude control, terrain-following logic
- **Performance Validated:** 
  - Altitude tracking: ±0.78 cm standard deviation without laser altimeter feedback
  - Lateral waypoint tracking: ±0.74 m standard deviation in 3.8–4.9 m/s winds
- **Tuning:** Lateral control gains optimized during first two flights

### SuperSwift (Proposed Commercial System)
Planned successor to Tempest with following improvements:
- **Flight Endurance:** 90-minute nominal (vs. 1-hour Tempest), enabling 741-acre coverage (vs. 494 acres)
- **Payload Access:** Removable nose cone with dedicated payload scaffolding (direct access to LDCR, SD cards, switches)
- **Thermal Management:** ESC-to-heat-sink design with thermal paste, integrated into airflow (adapted from Apollo platform)
- **Airframe Design:** 2 lbs lighter; larger wing area for easier handling at lower speeds
- **RF Cleanliness:** Motor, ESC, and battery relocated to aft fuselage section (away from L-band antenna in nose); coordinated RF shielding design with CET during build
- **Operational Mode:** Full autonomous capability (reduced operator error risk)
- **Launch Method:** Hand-launchable at SMM payload weight
- **Data Logging:** FPGA-based logger at 60 Ms/sec (vs. current 1 Ks/sec) for enhanced noise characterization

## Use Cases & Applications

### Soil Moisture Mapping
- **Application:** Remote sensing of soil moisture via L-band brightness temperature
- **Validation Approach:** Comparison of flight-derived brightness maps with in situ ground sensors
- **Coverage:** Single flight mapping runs over ~494 acres (Tempest) to ~741 acres (SuperSwift)
- **Altitude Flexibility:** Demonstrated 25–55 m AGL operation; nominal 30 m for mapping with 30 m waypoint spacing
- **Comparison Reference:** SMAP satellite (36 km × 36 km resolution) used as sanity check; flight data provides ~meter-scale resolution

### Agricultural/Environmental Monitoring
- **Partnership Reference:** Ongoing collaboration with Colorado State University on agricultural applications
- **Use Case Demonstrated:** Capability to detect soil moisture variations from overnight dew (morning mapping flights showed measurable brightness temperature differences)

## Key Results

### Radiometer Performance
- **Brightness Temperature Maps:** Successfully generated from 2015-09-08 Flight #2 and 2015-09-09 Flight #1
- **Dry Soil Conditions:** Mean 316.9 K, range 294.7–338.8 K
- **Damp Soil Conditions (morning dew):** Mean 297.3 K, range 267.7–323.4 K
- **Validation Status:** Expected brightness temperature correlation confirmed; full soil moisture map generation and in situ comparison ongoing

### Autopilot Performance Validation
- **Altitude Tracking:** Average error 0.16 m to -0.36 m; standard deviation 0.54–1.14 m across flights
- **Waypoint Tracking:** Average error 0.12–0.52 m; standard deviation 0.74–1.28 m; maximum error 5.59 m
- **Wind Performance:** Maintained tracking accuracy with wind at 21% of cruise speed

### Flight Operations Summary
| Flight | Date | Duration | Mapping Runs | Altitude | Objectives Met | Notes |
|--------|------|----------|--------------|----------|----------------|-------|
| Flight 1 | 09/08/2015 | 18 min | 1 | 55 m AGL | 3/3 (checkout, autopilot, mapping) | High noise (50 mV); tuning flight; 15 m spacing test |
| Flight 2 | 09/08/2015 | 21 min | 2 | 35 m AGL | 2/2 (mapping) | Clean data; 30 m spacing; lateral control tuning |
| Flight 3 | 09/09/2015 | 22 min | 2 | 25 m AGL | 2/2 (morning mapping) | Clean data; damp soil variation observed |

### Thermal/Operational Issues Identified
1. **ESC Overheating:** Limited flight time to ~20 minutes; ESC reached 1-hour predicted endurance only after flight due to thermal constraints
2. **Laser Altimeter Interference:** L-band noise from proximity to radiometer antenna cables; disabled for all flights; minimum safe altitude raised to 30 m
3. **NDVI Saturation:** Red and NIR sensors saturated except for downward red channel in low-light morning flight
4. **Handling Difficulties:** 15.8 lbs payload weight required two-person bungee launch and expert pilot for landing
5. **Payload Access:** Narrow Tempest fuselage limited maintenance and sensor access

## Notable Details

### EMI Mitigation Lessons
- Motor noise in L-band was **radiated**, not conducted—filter-based approaches failed; mechanical shielding was necessary solution
- Noise appeared in specific calibration states (states 2 and 3), indicating down-facing channel as common link
- Comprehensive copper foil wrapping with grounded connections eliminated noise across all flight data

### Sensor Integration Challenges
- **Laser Altimeter Constraint:** Physical proximity limitations in Tempest airframe prevented relocation; disabled as safety measure
- **NDVI Sensor Limitations:** Saturation issues drove procurement decision for Decagon calibrated sensors for SuperSwift
- **High-Rate Logging Gap:** Current 1 Ks/sec logging insufficient to characterize transient noise (first flight); FPGA upgrade to 60 Ms/sec planned

### SMAP Satellite Comparison