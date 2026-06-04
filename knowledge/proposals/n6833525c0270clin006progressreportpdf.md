# Expendable Air-sea Profiling Observations in Hazardous Weather Conditions, via Small Uncrewed Aircraft System

## Document Metadata
- **Type:** SBIR/STTR Progress Report (Phase I Option period)
- **Client/Agency:** Department of the Navy / Office of Naval Research (ONR)
- **Program/Solicitation:** Navy SBIR Topic N25A-T025; Proposal Number N25A-T025-0009
- **Contract Number:** N6833525C0270
- **Date:** June 3, 2026 (covering March 20 – June 3, 2026)
- **BST Products/Systems Referenced:** S0 uncrewed aircraft system (UAS); S0-VTOL (vertical takeoff and landing variant)
- **Key Personnel:** 
  - Principal Investigator: Jack Elston
  - Report Prepared by: Dr. Maciej Stachura
  - Last Editor: Beck Cotter

## Executive Summary

This progress report documents Phase I Option period work (March–June 2026) on refining the Black Swift Technologies S0 uncrewed aircraft system for Navy applications in hazardous maritime weather. Two NOAA P-3 validation flights in March and April 2026 demonstrated repeatable dual-S0 deployments, identified and corrected major wind-measurement calibration errors, and validated S0 performance in precipitation. The team completed or substantially advanced four restructured Option tasks (O1–O4) focused on calibration/validation planning, error analysis using fleet data, de-ice heater design, and stakeholder engagement to reduce Phase II risk.

## Technical Approach

**Objective:** Refine the S0 platform and demonstrate operational utility for Navy-specific applications delivering high-resolution, accurate, and cost-effective atmospheric and ocean-surface observations in hazardous maritime weather.

**Four Phase I Option Tasks (restructured at kickoff March 20, 2026):**

1. **Task O1: Phase II Calibration/Validation Plan** (Milestone: May 20, 2026 – completed)
   - Planned four dedicated over-ocean test events across Base and Option phases
   - Test 1: OOI Pioneer Mid-Atlantic Bight Array validation with 3D winds, pressure, temperature, humidity, sea surface temperature, and initial turbulence algorithm testing
   - Test 2: OOI repeat validation with turbulence algorithm and wave height Kalman filter testing; de-ice heater demonstration
   - Test 3: Arctic environment deployment (if C-130 available) or return to OOI; advanced automated QC validation
   - Test 4: Final validation including DOW aircraft integration (C-130/P-8), AI-based autonomy algorithms, and turn-key Navy system documentation
   - Backup/contingency sites include Virginia Key and Fowey Rock, Florida, and the University of Miami SUSTAIN laboratory

2. **Task O2: Additional Cal/Val Work with NOAA Data and ISARRA** (Milestone: June 20, 2026 for NOAA data; ISARRA results later)
   - Two completed NOAA P-3 validation flights: March 26 and April 7, 2026 (Gulf of America and east of Cape Canaveral, FL)
   - First simultaneous dual-S0 deployment
   - Box-pattern flights at 3,000 ft MSL (March 26) and 1,000 m MSL (April 7)
   - April 7 flight was first precipitation validation, comparing against P-3 tail Doppler radar, dropsondes, and flight-level data
   - Comprehensive error-source evaluation across S0 fleet (S0-70, S0-63, S0-66, S0-72) addressing magnetometer, accelerometer, IMU-magnetometer misalignment, and atmospheric measurement errors

3. **Task O3: S0 Operation in Icing – Design of De-Ice Heaters** (Milestone: July 20, 2026)
   - Design of heated nose cone for multi-hole probe to enable 3D wind measurements in cold/icing conditions
   - Maturation of wing, tail, and propeller coating approach for NASA Glenn icing campaign in Phase II

4. **Task O4: Stakeholder Engagement and Integration Planning** (Milestone: September 20, 2026)
   - Engagement with DoD stakeholders on operational requirements and integration pathways
   - Focus on launch platforms, communication systems, data delivery formats
   - Development of detailed integration plan for hardware, software, and logistics

## Products & Capabilities Described

### S0 Uncrewed Aircraft System
- **Description:** Expendable, air-deployed profiler designed to fit A-size sonobuoy form factor and Common Launch Tube (CLT) standards for integration into Navy platforms (P-8A, CH-53E)
- **Measurement Capabilities:**
  - 3D winds (0.2 m/s accuracy, 0.01 s response time)
  - Pressure (0.4 hPa accuracy, 0.01 s response time)
  - Temperature (0.1°C accuracy, 0.5 s response time)
  - Humidity (2% accuracy, 0.3 s response time)
  - Sea surface temperature (0.3°C accuracy)
  - Vertical wind and turbulence (via onboard algorithms)
  - Wave height (3% accuracy) and mean squared slope (10% accuracy) via radar
  
- **Sampling Rate:** 100 Hz for winds and auxiliary sensors; 5 Hz for Vaisala PTH sensor
- **Enhanced Compute Capability:** Onboard processing for turbulence algorithm, wave height Kalman filter, and AI-based autonomy algorithms
- **Deployment Modes:** Air-deployed from P-3/P-8 aircraft; ground/ship-launched variants (S0-VTOL) under development

### S0-VTOL (Vertical Takeoff and Landing variant)
- Proposed for ship- or shore-launched operations
- Mentioned in transition plans for forward-deployed, expeditionary Navy operations
- Reference to CLT and external-tube groundwork in Phase I Final Report

## Key Technical Findings from Phase I Option Period

### NOAA P-3 Validation Flights (March 26 & April 7, 2026)

**March 26, 2026 Flight (3,000 ft MSL, clear conditions):**
- Box pattern with headwind, tailwind, and crosswind legs (10 km leg length)
- Initial identification of two major wind-measurement errors:
  1. Pressure-scaling error on center and right ports (corrected in Fig. 5)
  2. Non-orthogonality of the 3 magnetometer axes (corrected with new calibration technique)
- Post-correction wind-speed agreement became internally consistent (4.2–4.4 m/s across legs)
- Comparison platforms: P-3 flight-level, dropsondes, S0 units

**April 7, 2026 Flight (1,000 m MSL, precipitation conditions):**
- First precipitation validation of S0 system
- Stratiform rain sampling east of Cape Canaveral, FL
- Shorter 5-km legs allowed both S0 units to complete full box patterns
- Comparison platforms: P-3 flight-level, P-3 tail Doppler radar (TDR, 500 m vertical / 2,000 m horizontal resolution), two dropsondes
- Results (Table 2):
  - S0_1: 15.1°C (±0.2), 73.7% RH (±6.0), 7.5 m/s wind (±0.9), 38.9° direction (±8.5), 900.6 mb (±0.2)
  - S0_2: 14.9°C (±0.2), 81.1% RH (±6.4), 8.2 m/s wind (±1.1), 46.6° direction (±8.1), 900.5 mb (±0.3)
  - P-3 Flight Level: 15.5°C (±0.1), 68.1% RH (±5.4), 5.7 m/s wind (±0.8), 23.4° direction (±12.3), 904.0 mb (±0.1)
  - Dropsonde 1: 14.4°C, 74.2% RH, 8.1 m/s, 49.3°, 901.9 mb
  - Dropsonde 2: 13.5°C, 98.4% RH, 8.5 m/s, 54.5°, 901.8 mb
  - P-3 TDR: 4.6 m/s (±0.2), 47.5° (±4.0°)
- Demonstrated robustness under precipitation; step-function behavior in wind measurements eliminated with corrections

### Error Source Evaluation (Fleet Analysis)

**1. Magnetometer Affine Calibration**
- Identified non-orthogonality between magnetometer sensor axes across fleet due to IC placement and PCB flex variations
- Traditional symmetric ellipsoid calibration cannot account for physical axis misalignment
- Implemented affine (9-parameter) calibration model: B_corrected = A · (B_raw − b)
- Results for four aircraft (Table 3):
  - S0-70: 1.68° max deviation, ±0.557 m/s max wind error
  - S0-63: 2.75° max deviation, ±0.911 m/s max wind error
  - S0-66: 4.41° max deviation, ±1.462 m/s max wind error (fleet worst-case)
  - S0-72: 1.79° max deviation, ±0.593 m/s max wind error
  - X–Z axis pair showed largest and most variable non-orthogonality (0.67–4.41°)
- After affine correction, wind-speed agreement improved substantially; errors reduced up to 2 m/s in worst cases

**2. Accelerometer Bias Error**
- Recovered S0 accelerometer bias vector: [+0.087, −0.070, +0.022] m/s² (magnitude 0.114 m/s²)
- Induced roll error of +0.41° and pitch error of +0.51°
- At TAS = 21 m/s (Lakeland FL, inclination 56.6°):
  - Roll bias produces ±0.23 m/s sinusoidal horizontal wind error
  - Pitch bias produces ±0.28 m/s sinusoidal horizontal wind error and +0.187 m/s vertical wind DC offset

**3. Magnetometer–IMU Misalignment**
- S0-70 misalignment errors (Table 5):
  - Roll misalignment (−0.762°): ±0.424 m/s sinusoidal
  - Pitch misalignment (+0.258°): ±0.144 m/s sinusoidal + 0.095 m/s vertical wind DC offset
  - Yaw misalignment (−0.551°): 0.202 m/s constant heading offset

**4. TAS Errors from Atmospheric Measurement**
- Temperature error (+0.3°C): +0.013 m/s wind error
- Static pressure error (+1 hPa): −0.013 m/s wind error
- Relative humidity error (+4%): +0.007 m/s wind error
- Root-sum-square of all three: 0.018 m/s (negligible vs. calibration-driven terms)

**Summary Error Contribution (Figure 7):**
- Magnetometer non-orthogonality (affine correction): fleet mean ±0.6 m/s, worst-case ±1.5 m/s
- Accelerometer bias: ±0.4 m/s (roll) + ±0.4 m/s (pitch horizontal) + +0.19 m/s (pitch vertical DC)
- Magnetometer–IMU misalignment: ±0.4 m/s (roll) + ±0.2 m/s (pitch) + 0.2 m/s (yaw)
- Atmospheric measurement errors: <0.02 m/s (negligible)

**Relative Humidity Compensation Issue (minor):**
- Identified sensor compensation error in data pipeline; corrected in