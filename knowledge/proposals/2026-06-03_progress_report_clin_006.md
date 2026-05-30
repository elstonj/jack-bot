# 2026-06-03 Progress Report CLIN 006

## Document Metadata
- **Type:** SBIR/STTR Progress Report (Phase I Option Period)
- **Client/Agency:** Department of the Navy
- **Program/Solicitation:** BAA topic N25A-T025; "Expendable Air-sea Profiling Observations in Hazardous Weather Conditions"
- **Date:** June 3, 2026 (covering March 20 – June 3, 2026)
- **Contract Period:** Phase I Option (revised and approved at kickoff March 20, 2026)
- **BST Products/Systems Referenced:** S0 uncrewed aircraft system (UAS); S0-VTOL (vertical take-off and landing variant)
- **Key Personnel:** Jack Elston (Principal Investigator); Joshua Wadler (last editor); co-PI Zhang (University of Miami)

## Executive Summary
This progress report documents Black Swift Technologies' Phase I Option work on refining and validating the S0 expendable UAS platform for Navy maritime weather observations. The S0 is being developed to deliver high-resolution atmospheric and ocean-surface profiling data in hazardous conditions, with focus on calibration/validation, icing capability design, and stakeholder integration planning. The first reporting period (March–June 2026) concentrated on completing the Phase II Cal/Val Plan (Task O1) and conducting additional validation analysis using 2026 NOAA oceanic flight data (Task O2), both substantially complete and on track.

## Technical Approach

### Program Objectives (4 Core Goals)
1. Quantify enhanced observation capabilities by comparing S0 performance to existing platforms for improved expendable in-situ profiling in challenging air-sea environments
2. Assess and improve S0 measurement accuracy through calibration, validation, error analysis, and extension to icing conditions
3. Produce new/unique observations (vertical wind, turbulence, wave properties) and develop onboard algorithms
4. Automatically target areas of interest using onboard computing and software APIs for adaptive sampling

### Option Phase Structure (Revised at Kickoff)
Four tasks replacing original scope to reduce Phase II risk:
- **O1 (Target: May 20, 2026):** Completion of Phase II Calibration and Validation Plan
- **O2 (Target: June 20, 2026):** Additional Cal/Val analysis using 2026 NOAA oceanic flight data and ISARRA results
- **O3 (Target: July 20, 2026):** Design of de-ice heaters for operation in icing conditions
- **O4 (Target: September 20, 2026):** Stakeholder engagement and integration planning

## Products & Capabilities Described

### S0 Uncrewed Aircraft System
**What it is:**
- Expendable, air-deployed profiler platform engineered to fit A-size sonobuoy form factor and Common Launch Tube (CLT) standards
- Equipped with multi-hole probe for 3D wind measurement, Vaisala PTH sensors (pressure, temperature, humidity at 5 Hz), wind sensors (100 Hz), auxiliary static pressure sensor (100 Hz)
- Enhanced onboard compute capability for running algorithms in-flight
- Dual-GPS wind measurement capability
- Pitot heaters for de-icing

**Proposed Use in This Context:**
- Air-deployed from P-8A and CH-53E aircraft (Navy); C-130 and P-3 (Air Force/NOAA); with ground/ship-launch variant (S0-VTOL)
- Autonomous profiling of atmosphere and ocean-surface conditions in hazardous maritime weather
- Collection of meteorological and ocean-state data (3D winds, pressure, temperature, humidity, sea surface temperature, wave properties, turbulence)
- Measurements at 100 Hz sampling rate

**Specifications/Performance Claims:**
- Multi-sensor fusion for wind, pressure, temperature, humidity measurement
- Onboard quality control (QC) algorithms advancing toward turn-key capability
- Turbulence algorithm capability for surface flux validation
- Wave height Kalman filter for sea state estimation
- Data delivery capability moving toward live ingest in operational systems
- 120-minute mission duration demonstrated (2025 NOAA season)

### S0-VTOL
- Vertical take-off and landing variant for ship-launched and ground-based deployments
- Support for Navy expeditionary, distributed, and forward-deployed operations
- Vertical-wind comparison testing planned against NCAR FastEddy model (ISARRA)

## Use Cases & Applications

### Naval/Maritime Operations
- Hazardous weather observation for Navy operations
- Air-sea profiling in challenging maritime conditions
- Drop-zone wind measurement ahead of C-130 operations
- Ship- or shore-launched operations (S0-VTOL)

### Hurricane/Storm Reconnaissance
- Deployment from NOAA P-3 during hurricane season (established operational heritage)
- Eyewall-circumnavigation data collection and validation against tail Doppler radar (TDR)
- Stratiform rain sampling (April 7, 2026 mission demonstrated capability)
- Validation flights in precipitation conditions

### Oceanographic Research
- Validation over Ocean Observatory Initiative (OOI) Pioneer Mid-Atlantic Bight Array
- Momentum flux, latent heat flux, sensible heat flux estimation
- Surface turbulent transfer coefficient validation (COARE 3.0 algorithm comparison)
- Floating buoy and portable tower validation

### Arctic Operations
- Potential C-130 drop deployment in Arctic environment (Test 3 goal)
- Cold-weather sensor and de-ice heater testing

### Clear-Air/Atmospheric Research
- Clear-air testing prior to hurricane season
- Vertical wind and turbulence profiling (with onboard algorithms)
- Comparison against NCAR dropsondes
- Wind tower validation (land-based testing of S0 upgrades)

## Key Results (Reporting Period: March 20 – June 3, 2026)

### Task O1: Phase II Cal/Val Plan – SUBSTANTIALLY COMPLETE
**Planned Test Events (4 total, over Base and Option phases):**

**Test 1: Over-Ocean Validation (Virginia Key & Foway Rock, FL)**
- Location: Near University of Miami (co-PI Zhang)
- Validation targets: 3D winds, pressure, temperature, humidity, sea surface temperature (SST) against floating buoy and portable towers
- Novel capability: First test of turbulence algorithm on enhanced S0 compute
- Data collection: ≥4 hours meteorological/ocean data at 100 Hz
- Wave height Kalman filter tuning with sonobuoy truth data
- Deliverables: S0 base sensing datasheet with 4-hour comparison data; turbulence algorithm confirmation; radar sea-surface data with sonobuoy truth
- Special feature: Wave tank for S0 radar testing (noted in report)

**Test 2: Ocean Observatory Initiative (OOI) Pioneer Array, North Carolina Coast**
- Array: Approximately 37 miles × 37 miles box, ~34 miles offshore, water depths 25–300 m
- Validation targets: Base S0 sensing; turbulence algorithm against OOI Bulk Meteorology Package (momentum, latent, sensible heat flux)
- Onboard wave height Kalman filter testing vs. buoy data
- Pitot heater demonstration (no icing expected during test)
- Deliverables: Updated S0 base sensing accuracy datasheet; turbulence comparison data; wave height Kalman filter confirmation; onboard QC demonstration
- Integration point: Collaboration with WHOI (Edson et al. 2022; Barr et al. 2025)

**Test 3: Arctic or OOI Pioneer Array (Backup)**
- Primary goal: Arctic deployment via Air Force C-130 (if logistics/certification permit)
- Backup: Return to OOI Pioneer Array
- Objectives: Additional base sensing validation; turbulence/wave height validation; integration of cold-weather enhancements
- Deliverables: Increased statistical significance of error bounds; advanced automated QC version demonstration

**Test 4: Final Flight Validation – Aircraft Drop Integration & Ship/Ground Launch Concepts**
- Deployment concepts: DOW aircraft (Air Force C-130 or Navy P-8) drop over ocean array; ship-launched and ground-based S0-VTOL demonstrations
- Testing: AI-based autonomy algorithms in-flight; improved turbulence/wave height algorithms (Task O.7)
- Deliverables: Final validation data; turn-key Navy system lessons-learned document; evidence of base sensing, advanced algorithms, autonomy, and Navy integration features

### Task O2: Additional Cal/Val Analysis – SUBSTANTIALLY COMPLETE / ON TRACK
**2026 NOAA Oceanic Flight Data Analysis:**

**March 26, 2026 Flight (Gulf of America, W-168)**
- Altitude: 3,000 feet (914 m)
- Conditions: Clear, calm day
- Flight pattern: P-3 box pattern (10 km legs) before S0 deployment; P-3 then rose to deploy two S0s simultaneously (new capability in 2026)
- S0 deployed dropsondes: 2 dropsondes launched during S0 box sampling
- Measurements analyzed: Wind speed, wind direction, relative humidity, air temperature (broken down by wind-relative orientation: headwind, tailwind, crosswind legs)
- Key finding: "Step function" response in wind speed/direction at leg turns; relative humidity and temperature show no such jumps
- Accuracy observation: S0 mean values comparable to P-3 and dropsondes (with exception of air temperature)
- Data normalization: Measurements scaled per leg due to different true air speed and sampling frequency between platforms

**April 7, 2026 Flight (Stratiform Rain East of Cape Canaveral, FL)**
- Altitude: 1,000 m (3,280 ft) – first validation flight in precipitation
- Box pattern: 5 km legs (shortened to enable complete box patterns); headwind and tailwind legs only (rain persistence concern)
- Comparison data: P-3 tail Doppler radar winds (500 m vertical resolution) – **not yet available as of report writing**
- Key findings:
  - No step-function behavior in wind speed/direction (unlike March 26)
  - S0 wind speed/direction matched dropsondes and P-3 flight-level winds during tailwind leg
  - P-3 headwind leg winds were outlier
  - Relative humidity showed substantial spread (60–100%); two successive dropsondes exemplified this variability
  - Air temperature: Dropsondes showed ~1–2°C lower; P-3 reported higher values (~1 hour earlier, creating verification challenge)
  - **Conclusion: Demonstrated S0 measurement repeatability and accuracy in rainy conditions**

**Data Quality Issues Identified & Managed:**
- Relative-humidity sensor compensation error identified and corrected in real-time data pipeline; previously delivered data recompensated
- TDR radar coverage limited in eastern region useful for S0 comparison (weaker returns in clear air vs. precipitation); NOAA coordinated recovery and reprocessing of additional TDR files
- Data assembly challenge: Mixed data rates (Vaisala PTH 5 Hz; winds/auxiliary static pressure 100 Hz) against WMO format expecting single time base – resolved with full-rate delivery and per-sensor timing

**Planned Continuation (Next Reporting Period):**
- ISARRA flight week results (vertical-wind comparisons against NCAR FastEddy model for air-deployed S0 and S0-VTOL)
- Additional comparison data from new Eastern Colorado tower
- Dual-GPS wind product analysis from 2026 CAT flights
- S0 frequency-sensitivity study
- Over-land repeatability work

### Task O3: S0 Operation in Icing – INITIATED
**Scope:** Design of de-ice heaters for multi-hole probe to enable 3D wind data reporting in cold conditions.
**Status:** Early scoping during this period; detailed mechanical design work planned for next reporting period.
**Planned Next Steps:** 
- Complete mechanical design of heated nose cone
- Integrate standalone heater and sensor assembly with autopilot on/off control and commercial process controller
- Bench-level function testing with heater power draw measurement on 24 V switched line
- Wing, tail, propeller coating approach maturation toward Phase II NASA Glenn icing campaign

### Task O4: Stakeholder Engagement and Integration Planning – INITIATED
**Scope:** DoD stakeholder requirements identification; launch platform, communication system, data delivery format preferences; Navy operator engagement; detailed integration plan development.
**Status:** Early engagements begun this period.
**Planned Next Steps:**
- Convert engagements to structured requirements interviews