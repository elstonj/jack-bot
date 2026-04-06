# Quarter 6 Report: Soil Moisture Mapping sUAS Phase II

## Document Metadata
- **Type:** Phase II Interim Report / Quarterly Progress Report
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR Phase II; Contract Number NNX14CG09C
- **Date:** October 2015
- **BST Products/Systems Referenced:** BST Tempest (sUAS platform), SwiftPilot Pro autopilot, SuperSwift prototype (under development), LDCR (L-band radiometer), MiCo antenna, NDVI sensors
- **Key Personnel:** Maciej Stachura (report editor)

## Executive Summary
This Phase II quarterly report documents the first flight deployment of BST's Soil Moisture Mapping (SMM) system in Canton, Oklahoma, where five successful mapping missions were flown over three flights. The report details critical findings from the Tempest sUAS platform deployment, analysis of radiometer performance and soil moisture data, assessment of aircraft control systems, and progress on the SuperSwift prototype development as a next-generation platform for commercial soil moisture monitoring.

## Technical Approach

### Deployment & Testing
- **Location:** Canton, OK test site with in situ soil moisture sensors
- **Aircraft:** BST Tempest (N738SW) with COA #2014-CSA-200-COA
- **Sensor Integration:** L-band Dicke Radiometer (LDCR) with MiCo antennas, NDVI sensors (thermal, red, near-infrared upward/downward-facing), laser altimeter (disabled due to interference), GPS, IMU
- **Flights:** 3 total flights (Sep 8-9, 2015) with 5 mapping missions, 1 hour total operational time
- **Altitude:** 25-55m AGL; laser altimeter disabled, minimum altitude limited to 30m for safety

### Radiometer Calibration & Data Processing
**Four-State Calibration System:**
- State 0: Vout = V0 + gain0*(Tref2 - Tref1)
- State 1: Vout = V0 + gain1*(Tu - Tref1)
- State 2: Vout = V0 + gain2*(Tref2 - Td)
- State 3: Vout = V0 + gain3*(Tu - Td)

**Processing Pipeline:**
1. Linear interpolation of navigation data to radiometric time grid (~1ms intervals)
2. Dropped 5 samples during calibration state transitions
3. Averaged LDCR output voltage with 80-sample uniform window per calibration state
4. Antenna temperature calibration using pre-flight water calibration data
5. Brightness temperature mapping using antenna gain models (η = 95.58% radiation efficiency)
6. Pixel size calculation = flying altitude; down-looking brightness temperature computed per pixel with geographic coordinates

**Calibration Parameters** (estimated via simulated annealing from 1,180 calibration cycles):
- Applied second-order polynomial temperature model to identify V0 and gains G0-G3
- χ² goodness-of-fit values near degrees of freedom (1,174 DOF), indicating good model fit
- Known ~3dB gain differences between states due to RF losses in internal quadrature hybrid and coaxial cables

### Control System Performance

**Altitude Tracking (without laser altimeter):**
- Average error: -0.36m to +0.16m across mapping runs
- Standard deviation: 0.54m to 1.14m (best: 0.54m)
- Maximum error: 1.88m to 5.15m
- Assessment: "Sufficient for soil moisture mapping"

**Waypoint/Path Tracking:**
- Average error: 0.12m to 0.52m
- Standard deviation: 0.74m to 1.28m (best: 0.74m on final runs)
- Maximum error: 2.35m to 5.59m
- Wind speeds: 3.8-4.9 m/s (21% of cruise speed)
- Assessment: Standard deviation better than unaided GPS accuracy; acceptable for soil moisture system

## Products & Capabilities Described

### BST Tempest (Existing sUAS Platform)
- **Configuration:** Electric-powered sUAS with bungee launcher
- **Nominal flight time:** ~1 hour with SMM payload (15.8 lbs total)
- **Limitations:** 
  - ESC overheating with SMM payload (limited to ~20 min operational flights)
  - Cramped fuselage limits payload access and creates EMI issues
  - Bungee launcher susceptible to grass/vegetation snagging at wing tip
  - Difficult handling at SMM payload weight (requires two-person launch, expert pilot for landing)
  - Laser altimeter generates L-band interference with radiometer
  - Saturation issues with red/NIR NDVI sensors

### SuperSwift (Next-Generation sUAS - Prototype Phase)
- **Design advantages over Tempest:**
  - **Nominal flight time:** 90 minutes (vs. 1 hour Tempest) → coverage expansion from 494 to 741 acres
  - **Weight:** 2 lbs lighter than Tempest (estimated)
  - **Wing area:** Larger, enabling better handling at lower speeds
  - **Hand-launchable:** Fully autonomous operation, no bungee launcher needed
  - **Improved thermal management:** ESC mounted externally with heat sink (design borrowed from BST Apollo platform)
  - **RF-clean design:** Motor, ESC, battery positioned in aft fuselage away from L-band antenna in nose
  - **Payload access:** Removable nose cone with dedicated payload scaffolding
  - **Data logging:** New FPGA-based logger with 60 MS/sec rate (vs. 1 KS/sec current) for noise analysis
  - **Calibrated NDVI sensors:** Recently purchased Decagon sensors to address saturation issues

**Construction Details:**
- **Wings:** Foam core fiberglass with embedded servos/wiring; prototype weight 1,556g (65g under estimate); manufacturing moving to hollow core via outer-mold method with master plug/female mold tooling
- **Tail surfaces:** V-tail design (110° angle); prototype uses EPP foam with basswood skin; production version planned as hollow fiberglass with potential for embedded RF antennas
- **Fuselage:** Laser-cut balsa plywood bulkheads with hand-shaped foam blocks; production moving to composite outer-mold manufacturing with integrated laser-cut bulkheads as internal structure
- **Control surfaces:** Aileron/flaps on wings; ruddervator (combined rudder/elevator) on v-tail surfaces
- **Manufacturing partner:** North Wind Composites selected for plug/mold/parts production

### Sensors & Instrumentation
- **LDCR (L-band Dicke Radiometer):** 1.4-1.5 GHz, dual-polarization (H/V), four-state calibration; antenna radiation efficiency 95.58%
- **MiCo Antenna:** Dual-polarization pair; simulated gain models provided for V and H polarization
- **Thermal sensors:** Up/down-facing; down-facing correlated well with air temperature
- **NDVI sensors:** Up/down-facing red and near-infrared; saturation issues on Tempest (red/NIR saturated in all flights except early-morning down-facing red)
- **Auxiliary sensors:** GPS, IMU, laser altimeter (functional but disabled due to interference)

## Use Cases & Applications

### Soil Moisture Mapping
- **Primary application:** Precision agriculture and environmental monitoring
- **Methodology:** Airborne L-band radiometry for non-invasive soil moisture estimation
- **Coverage:** 741 acres per 90-minute flight (SuperSwift target)
- **Validation approach:** In-situ ground sensors + SMAP satellite comparison (SMAP limited to 36km × 36km resolution, used as sanity check only)

### Canton Deployment Results
- **5 mapping missions** across different altitudes and times (including early morning to capture dew/moisture variation)
- **Brightness temperature ranges:**
  - 09/08 Flight 2 (dry soil): Mean 316.9K, range 294.7-338.8K
  - 09/09 Flight 1 (damp soil with morning dew): Mean 297.3K, range 267.7-323.4K
- **Preliminary finding:** Lower brightness temperatures observed in damp soil, consistent with physics (demonstrates sensor sensitivity)
- **Detailed soil moisture mapping:** Ongoing (in situ network data collection still in progress at report writing)

## Key Results (for reports)

### Radiometer Data Analysis
1. **Brightness Temperature Mapping:** Successfully generated calibrated brightness temperature maps from radiometric data with validation against water body and atmospheric references
2. **Calibration Validation:** χ² goodness-of-fit confirms second-order polynomial temperature model adequately captures LDCR behavior across four calibration states
3. **Antenna Efficiency:** 95.58% radiation efficiency determined via HFSS simulation (±~1% accuracy)
4. **Surface Brightness References:** Water brightness temperatures (H: 64.4K, V: 132.2K), atmospheric (2.73K); elevation angle dependence noted as needed for future refinement
5. **Noise Characterization:** First flight (09/08 #1) exhibited ~50mV noise (~120K equivalent) from unknown environmental source; subsequent flights clean (~5mV); new high-rate FPGA logger will aid diagnosis

### Flight Control Assessment
1. **Altitude hold:** 0.54-1.14m standard deviation without laser altimeter; acceptable for sensor measurement (altitude used for pixel size calculation)
2. **Lateral tracking:** 0.74m standard deviation on final missions; control loop tuning improved performance across deployment
3. **Wind robustness:** Maintained tracking accuracy in 3.8-4.9 m/s winds without cross-wind control tuning
4. **System integration:** Autopilot, terrain-following, data logging, and sensor interfaces all functioned nominally

### EMI Mitigation Success
- **Problem:** Motor/ESC/battery generated ~1000mV L-band noise in pre-deployment Boulder tests
- **Root cause:** Motor radiated noise in L-band (not electrical coupling)
- **Solution:** Comprehensive shielding of ESC, motor cables, batteries, wiring with copper foil grounded to common return
- **Validation:** Ground tests and flight data confirmed noise elimination; second flight manual motor-off segments showed no additional noise
- **Production improvement:** SuperSwift design with aft-fuselage power systems + composite shielding planned for "RF-clean" aircraft

### ESC Thermal Management Issue
- **Problem:** SMM Tempest ESC overheated with payload, limiting flights to ~20 min despite 1-hour nominal battery
- **Root cause:** Lack of airflow in cramped fuselage with large ESC and fan
- **Predicted capability:** Battery post-flight recharge data suggests 62-minute flight possible
- **SuperSwift solution:** External ESC heat sink (mounted on fuselage exterior per Apollo design) maintains thermal control while keeping aircraft sealed against dirt/moisture
- **Impact:** Enables 90-minute SuperSwift flights for expanded coverage

### Launch/Recovery Constraints
- **Grass snagging risk:** Tempest bungee launcher susceptible to wing-tip contact with tall vegetation (witnessed crash with Colorado State University Tempest)
- **Payload weight handling:** Required two-person bungee pull and expert pilot for landing at 15.8 lbs total weight
- **SuperSwift solution:** Hand-launchable design eliminates bungee dependency; larger wings improve slow-speed handling; autonomous operation eliminates pilot skill dependency

## Notable Details

### Partnership & Collaboration
- **USC SoilSCAPE:** Collaborated on in situ sensor network at Canton test site; experiencing network issues at report time, manual data collection ongoing
- **SMAP satellite:** Used for validation sanity checks; SMAP radar inoperative, limited to 36km × 36km radiometer-only coverage
- **North Wind Composites:** Selected manufacturing partner for SuperSwift production tooling (plugs, molds, composite parts)
- **Decagon:** Supplier of calibrated NDVI sensors for SuperSwift to address Tempest saturation issues
- **Colorado State University:** Collaborative flights demonstrating Tempest operational challenges at SMM payload weight
- **UASUSA:** Tempest manufacturer; committed to providing ventilation scoops/vents (trade-off