# Coyote UAS Observations in Hurricane Edouard (2014)

## Document Metadata
- **Type:** Peer-reviewed research article / scientific publication
- **Journal:** Earth and Space Science
- **Published:** September 30, 2016
- **DOI:** 10.1002/2016EA000187
- **Authors:** J. J. Cione, E. A. Kalina, E. W. Uhlhorn, A. M. Farber, B. Damiano
- **Affiliations:** NOAA Hurricane Research Division, NOAA Earth System Research Laboratory, AIR-Worldwide, Raytheon Missile Systems, NOAA Aircraft Operations Center
- **BST Connection:** This document appears in BST's NOAA SBIR Phase I project files (2018) as a reference publication
- **Key Personnel Named:** Joe Cione (NOAA), Andrew Osbrink, Chris Troudt, Eric Redweik (Raytheon engineers)

## Executive Summary
This paper presents the first successful deployment of a Coyote UAS from a manned aircraft (NOAA WP-3D Orion) into a tropical cyclone. Two Coyote missions into Hurricane Edouard (2014) collected boundary-layer meteorological data at altitudes of 900–1500 m (eye/eyewall) and ~760 m (inflow layer). Data comparisons with NOAA WP-3D aircraft and GPS dropsonde measurements validate the Coyote's measurement accuracy and demonstrate its capability to capture fine-scale atmospheric variability in hurricane environments.

## Technical Approach

### Coyote UAS Platform
- **Manufacturer:** Raytheon Missile Systems
- **Dimensions:** Length 0.79 m, wingspan 1.47 m, mass 6 kg
- **Payload capacity:** Up to 1.8 kg
- **Maximum cruising airspeed:** ~36 m/s (~71 knots)
- **Endurance:** Up to 68 minutes (record achieved in this campaign)
- **Deployment method:** Wings folded, vehicle placed in canister, released from WP-3D sonobuoy chute at ~3 km altitude; parachute-stabilized descent; automatic wing deployment and flight initiation after 15 seconds

### Control & Communication
- Remote flight control from WP-3D via dual data links:
  1. Iridium satellite connection (proved unreliable in eyewall)
  2. 900-MHz data stream (required WP-3D to remain 6–11 km from Coyote for continuous data)
- Real-time data transmission capability
- GPS/INS autopilot with 50-Hz extended Kalman filter for velocity and attitude calculations

### Meteorological Sensors
- **Temperature:** Shibaura PB5, range -80 to +60°C, ±0.3°C tolerance, 2 Hz sampling, <2 s response time
- **Humidity:** E+E HC103M2, 0–100% RH, ±5% tolerance, 1 Hz sampling, <5 s response time
- **Pressure:** Honeywell SCCP15ASMTP, 5–1070 mb, ±0.5 mb tolerance, 3 Hz sampling, <1 s response time
- **Wind measurement:** Computed from vector subtraction of true air velocity (from pitot/static pressure sensors) from GPS-derived ground velocity
- **Spatial resolution:** ~20 m horizontal distance per temperature measurement; ~40 m per humidity measurement (at 40 m/s ground speed)

### Wind Calculation Method
- Equivalent airspeed (EAS) derived from dynamic pressure (pitot-static difference)
- True airspeed (TAS) corrected for local air density
- Wind speed and direction obtained by subtracting TAS vector from GPS ground velocity
- Autopilot Kalman filter details proprietary (acknowledged limitation in paper)

## Products & Capabilities Described

### Coyote UAS
**What it is:** A small, expendable unmanned aircraft system designed for atmospheric sampling, manufactured by Raytheon Missile Systems.

**Proposed use in this context:** 
- Deploy from manned hurricane research aircraft to collect low-altitude boundary-layer measurements in tropical cyclones
- Measure horizontal wind, temperature, moisture, and pressure in regions too hazardous for manned aircraft (below 1 km altitude)
- Provide fine-scale spatial resolution of atmospheric variability

**Specifications & Performance Claims:**
- Successfully deployed from NOAA WP-3D at 3 km altitude
- Operated safely in major hurricane (105 kt winds, Hurricane Edouard)
- Measured wind speeds to within ~1 m/s of WP-3D flight-level measurements (at 3 km altitude)
- Temperature accuracy: mean difference 0.4°C vs. dropsonde analysis (eyewall); 0.0°C vs. analysis (inflow layer)
- Dew point temperature accuracy: mean difference 0.7°C (eyewall); 1.3°C (inflow layer)
- Captured wind speed variability (σ = 3.4 m/s) that coarse dropsonde arrays could not resolve (σ = 2.2 m/s)
- Peak measured wind speed: 51.5 m/s in eyewall
- Longest platform endurance record achieved: 68 minutes

## Use Cases & Applications

### Mission 1: Eye & Eyewall Penetration (September 16, 2014)
- **Duration:** 27 minutes (1433–1500 UTC)
- **Flight profile:** Counterclockwise semicircle from NW of eye to southern eyewall
- **Altitude range:** 900–1500 m
- **Storm intensity:** 105 kt (major hurricane)
- **Target regions:** Eye, transition zone (10–20 km radius), western eyewall
- **Key result:** First UAS-deployed-from-aircraft mission into a hurricane; measured low-altitude wind profile structure comparable to WP-3D data at 3 km altitude

### Mission 2: Inflow Layer Sampling (September 17, 2014)
- **Duration:** 68 minutes (1508–1616 UTC)
- **Flight profile:** Outbound sampling from ~280 km to ~150 km from storm center
- **Altitude:** ~760 m (near-surface inflow layer)
- **Storm intensity:** 80 kt (weakened from previous day)
- **Target region:** NW quadrant; clear air, rainbands, and inflow environment
- **Key result:** Documented fine-scale structure of outer rainband boundary layer that conventional dropsonde arrays missed; measured wind speed increase from 18 to 25 m/s in pre-rainband environment; provided complete kinematic and thermodynamic characterization of rainband structure

## Key Results

### 16 September 2014 (Eye/Eyewall Mission)

**Wind Speed Comparison:**
- Coyote mean difference vs. WP-3D: +1.2 m/s (inbound leg), +0.8 m/s (outbound leg)
- Both platforms showed consistent radial wind profile structure
- Light winds (2–8 m/s) in eye; rapid increase to 32 m/s at eye-eyewall boundary; peak winds ~51.5 m/s in eyewall
- WP-3D peak winds (55.6–59.5 m/s after adjustment to Coyote altitude) vs. Coyote peak (51.5 m/s)—difference likely due to limited eyewall data transmission from Coyote

**Temperature:**
- Mean difference: +0.4°C (Coyote warmer)
- 75% of data within ±1°C; 46% within ±0.5°C
- Both platforms captured 2–3°C warming trend with descent, consistent reversal with ascent in eyewall

**Dew Point Temperature:**
- Mean difference: +0.7°C
- 67% of data within ±1°C; 40% within ±0.5°C
- Largest discrepancies in transition zone (10–20 km) with steep moisture gradients

### 17 September 2014 (Inflow Layer Mission)

**Total Wind Speed:**
- Mean difference: -0.5 m/s (Coyote slightly slower)
- Individual dropsonde comparisons: agreement within ~2 m/s
- Coyote wind variability (σ = 3.4 m/s) 3.5× larger than dropsonde analysis (σ = 2.2 m/s), indicating superior detection of fine-scale variability

**Radial Wind Component:**
- Mean difference: -0.8 m/s
- Good agreement with dropsonde analysis

**Temperature:**
- Mean difference: 0.0°C
- 93% of data within ±1°C; 59% within ±0.5°C
- Mean temperature both platforms: 20.9°C
- Three individual dropsonde measurements validated both analysis and Coyote data

**Dew Point Temperature:**
- Mean difference: +1.3°C (Coyote moist bias)
- Discrepancy concentrated between 260–195 km radius
- Sharp radial moisture gradients may explain some differences (e.g., 0.3°C vs. 3.3°C difference at different radial locations from same dropsonde)
- Possible causes: sensor wet bias, dropsonde dry bias, analysis artifacts, or combination
- Recommended further testing to resolve

### Fine-Scale Feature Capture

The Coyote identified an outer rainband structure (225–190 km radius) with:
- Pre-rainband wind speed increase: 18 → 25 m/s
- Complete thermodynamic and kinematic characterization
- Feature not resolved by dropsonde analysis or other platforms—unique capability demonstrated

## Notable Details

### Significance of Milestone
- **First air-deployed UAS into a tropical cyclone:** All previous UAS hurricane missions (Ophelia 2005, Typhoon Longwang 2005, Hurricane Noel 2007) were land-based deployments without manned aircraft delivery
- **First accuracy validation:** Previous UAS hurricane flights lacked comparison with independent measurement platforms; this study provides rigorous validation against NOAA WP-3D and GPS dropsonde measurements

### Data Gaps Addressed
- Opens pathway to routinely sample TC boundary layer below 1 km altitude, which has been inaccessible to manned aircraft due to hazard severity
- Complements point measurements (dropsondes, ocean buoys) with continuous spatial sampling
- Captures mesoscale variability that sparse dropsonde networks cannot resolve

### Sensor Limitations Identified
- Laboratory sensor specifications may not hold under extreme hurricane conditions (high winds, turbulence, sea spray, heavy rain)—acknowledged and addressed through extensive inter-platform comparisons
- Communication reliability: Iridium satellite connection proved unreliable in eyewall; 900-MHz line-of-sight link required proximity maintenance

### Operational Lessons Learned
- First mission (eyewall): Limited data recovery due to communication issues and WP-3D range constraints; shortened flight to 27 min
- Second mission: Adjusted operational procedures (maintained 6 km WP-3D proximity), enabling full 68-min flight with >93% data recovery

### Future Development Goals
- Chamber testing of InterMet sensors to resolve wet/dry bias in dew point measurements
- New downward-looking infrared sensor for sea surface temperature measurements (planned 2016)
- Integration of GPS dropsonde and Airborne Vertical Atmospheric Profiling System technologies into next-generation hybrid "UASonde" platform
- Validation of NOAA coupled Hurricane Weather Research and Forecasting (HWRF) model simulations using Coyote data
- Observing System Experiments (OSE) to assess impact on hurricane intensity forecasts

### Funding
- Disaster Relief Appropriations Act of 2013 supported Coyote purchase, testing, and operations
- Raytheon Missile Systems provided engineering support and expertise

### Data Availability
- Data archived at NOAA AOML HRD website: http://www.aoml.noaa.gov/hrd/data_sub/

---

## Relevance to Black Swift Technologies

This publication is referenced in BST's 2018 NOAA SBIR Phase I proposal files, likely because:
1. **Precedent for airborne-deployed UAS in hurricanes:** Demonstrates feasibility and scientific value of deploying small UAS from manned aircraft into extreme weather environments
2.