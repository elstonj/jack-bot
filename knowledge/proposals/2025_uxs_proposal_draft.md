# 2025 UxS Proposal Draft

## Document Metadata
- Type: Research proposal
- Client/Agency: NOAA (Office of Oceanic and Atmospheric Research / Office of Marine and Aviation Operations)
- Program/Solicitation: Internal NOAA 2025 Request for Proposals - "Breakthroughs with UxS Technologies" from OAR UxS Research Transition Office and OMAO UxS Operations Center
- Date: Submitted 2024-10-01; Last Modified 2025-03-13
- BST Products/Systems Referenced: Black Swift S0 sUAS
- Key Personnel: 
  - PI: Dr. Joseph J. Cione (NOAA/AOML)
  - Co-PIs: Dr. Jun A. Zhang, Dr. Joshua B. Wadler
  - Senior Researcher: Dr. Guo Lin
  - Division Director: Dr. Ghassan Alaka

## Executive Summary
This proposal aims to advance NOAA's tropical cyclone (TC) forecasting capabilities by transitioning three uncrewed aircraft systems toward operational use: the Black Swift Technologies S0 sUAS for low-altitude boundary layer sampling from the P-3, the Dragoon Coriolis for land-launched long-duration missions, and the StratoSolutions StratoSat-25 HAPS for stratospheric dropsonde deployment. The project focuses on addressing critical data gaps in TC intensity forecasting through improved boundary layer observations, real-time data delivery to operational centers, and enhanced physics parameterizations in NOAA's coupled TC forecast models (HAFS).

## Technical Approach

### Black Swift S0 Advancement
The S0 is a 1.58 kg fixed-wing sUAS with 1.38 m wingspan, 26 m/s cruise speed, ~1.5 hr battery endurance, and 4,600 m maximum altitude. Currently deployed from the NOAA P-3 via parachute in cylindrical container with folded wings. Successfully flown in Hurricanes Tammy (2023: 2 aircraft), Ernesto (2024: 4 aircraft), and Francine (2024: 4 aircraft). The proposal targets RL 8/9 operational transition through:

**Hardware/Payload Improvements:**
- Dual GPS for heading (replacing single GPS) to improve wind velocity accuracy in weak signal conditions
- Data buffering and re-transmission capability during communication loss
- Laser altitude optimization for operation in rain (eyewall/rainband sampling)
- Onboard video camera for real-time environmental observation

**Operational Efficiency Optimizations:**
- Firmware/communications/UI customization for pilot-independent autonomy
- Battery life extension (~1.5 hrs → ~2 hrs potential) through battery tweaks
- Manufacturing improvements for cost reduction and reliability
- External launch via CAD (eliminating need for P-3 depressurization)
- Expanded data fields in AirOPS (laser altitude, radio signal quality, communication timing)
- USB firmware update system (avoiding aircraft removal from deployment tube)
- Automated real-time quality-controlled netCDF file generation (replacing post-processing delays)

**Meteorological Consistency Measures:**
- Wind tunnel testing to characterize wing effects on multi-hole pressure probe measurements
- Increase measurement frequency from 2-3 Hz to at least 10 Hz (limited currently by onboard radio bandwidth)
- Implement laser-altitude-based flight control (replacing GPS/pressure altitude) for accurate low-altitude (<50 m) height assignment

### Dragoon Coriolis Platform
Long-duration hybrid-electric sUAS currently at TRL 6 under separate NOAA Phase II SBIR. Specifications:
- Cruise speed: 63 knots
- Gross weight: 15 kg
- Wingspan: 100 in; Length: 64 in
- Endurance: 15-19 hrs (depending on payload: 5 lbs vs 1 lb)
- Range: 1,100-1,370 statute miles
- Launch: Electric rail; Recovery: Belly landing or single-use
- Sensors: Pressure, temperature, humidity; Iridium satellite link for real-time data
- Autopilot: PX4 Flight Stack
- Cost: <$15k in quantity

Proposal plans two one-week over-water flight operations annually (years 1-3) from Florida, aligned with NOAA weather observation goals and tropical disturbance forecasting. FAA Certificate of Authorization (COA) for beyond-line-of-sight (BLOS) operations from Ft. Myers area expected early 2025. Goal: Low-altitude (<5,000 ft MSL) meteorological data collection around tropical disturbances when P-3 unavailable.

### StratoSolutions StratoSat-25 HAPS
Solar-electric stratospheric fixed-wing aircraft designed to carry micro-dropsonde payloads. Specifications:
- Total takeoff mass: 25 kg
- Wingspan: 12.5 m
- Endurance: Many months (stratospheric loitering capability)
- Payload capacity: 2 kg
- Micro-dropsonde payload: 100 dropsondes potential (using full 2 kg capacity)

**Key Innovation - Micro-Dropsonde Dispensing System:**
- Ultra-lightweight, long-term stratospheric storage capability
- Self-contained dispensing system with <0.5W average power consumption
- Current density: 25 micro-dropsondes per kilogram of payload weight
- Potential future density: >50 micro-dropsondes/kg with enhanced dispensing and improved battery technology
- System includes antenna and UHF receiver for in-flight dropsonde telemetry decoding

**Gust Alleviation Technology (Voltitude):**
Proprietary technology demonstrated to:
- Halve wing bending loads during turbulence
- Double maximum speed of flight envelope
- Enable more frequent launch/recovery and payload restocking

**Regulatory Path:**
- Flight permits through Barbados and Cabo Verde Civil Aviation Authorities
- Launch and recovery from St. Vincent Island, Cabo Verde Verde
- Operations over SAL OCEANIC and PIARCO Flight Information Regions (FIRs)

**Project Objectives for StratoSat-25:**
- Advance readiness level to RL 7-8
- Integrate enhanced micro-dropsonde housing (target >25 micro-dropsondes/kg)
- Establish flight approval basis and secure flight permit
- Demonstrate targeted dropsonde deployment capability
- Potential for 100+ dropsondes per mission

### Complementary System - Skyfora Streamsondes
75 atmospheric profiling systems procured for validation of sUAS and other UxS measurements. Advantages over Vaisala dropsondes:
- Advanced CONOPS possibilities
- Potentially improved per-unit pricing
- Additional observational capabilities including sea surface temperature estimates

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Forecasting
1. **Boundary Layer Data Gap:** Sample planetary boundary layer (PBL), surface layer, and turbulence in TC eye and rainbands—region identified as critical for intensity and intensity-change forecasting but currently undersampled (P-3 operational altitude ~3,000 m / 700 mb too high for safety)

2. **Upper-Level Data Gap:** Provide stratospheric dropsonde profiles to characterize TC outflow layer (~14-16 km altitude), which is an indicator of intensity change and diurnal cycle dynamics

3. **Landfall and Post-Landfall Operations:** sUAS over land will provide boundary layer wind and flux profiles after TC landfall for improved situational awareness and hazard impact assessment

4. **Extended Storm Access:** Dragoon Coriolis enables sampling when:
   - Reconnaissance aircraft (P-3, G-IV) unavailable
   - Storm beyond operational range of crewed aircraft
   - Need for sustained observation periods

### Secondary Applications: Model Physics Improvements
- Calculate exchange coefficients (momentum and enthalpy) in high-wind surface layer of TCs for first time using direct turbulent measurements
- Compute vertical eddy diffusivities of momentum, heat, and moisture
- Calibrate and improve PBL scheme in HAFS
- Evaluate model performance: turbulent kinetic energy (TKE), boundary layer height, vertical velocity distribution, eyewall slope, warm core strength/height, vortex tilt

### Real-Time Operational Support
- Situational awareness for National Hurricane Center (NHC) forecasters
- Data assimilation into NOAA operational TC forecast models (HAFS)
- Integration into next-generation forecast systems (UFS)
- Visualization in Advanced Weather Interactive Processing System-2 (AWIPS2)
- Prototype 2-D surface wind analysis system development (CIRA)
- AirOPS crew situational awareness tool updates

## Products & Capabilities Described

### Black Swift S0
**What it is:** Ultra-lightweight (~3 lbs / 1.58 kg) fixed-wing sUAS with 1.38 m wingspan, optimized for aircraft-deployed sampling into hazardous low-altitude TC environments

**Current capabilities:**
- Cruise speed: 26 m/s
- Endurance: ~1.5 hours
- Altitude range: Surface to 4,600 m (with GPS and pressure altitude capability)
- Deployment: Parachute-descent launch from P-3 via A-sized sonobuoy chute
- Recovery: Non-recoverable over water; data transmitted real-time via two-way radio to P-3
- Sensors: Multi-hole pressure probe (wind), downward-pointing laser (altitude/sea surface characteristics), thermodynamic sensors
- Data reporting: Currently 2-3 Hz (bandwidth-limited by radio)
- Communications: Two-way radio link to P-3

**Historical deployment success:**
- Hurricane Tammy (2023): 2 aircraft
- Hurricane Ernesto (2024): 4 aircraft
- Hurricane Francine (2024): 4 aircraft
- Current readiness: RL 6/7; target RL 8/9 by project completion

**Proposed enhancements for operational transition:**
- Dual GPS heading (improved accuracy)
- Data buffering/re-transmission during communication loss
- Rain-optimized laser (eyewall sampling)
- Onboard video
- 10+ Hz data reporting
- Laser-altitude-based flight control
- Extended endurance (~2 hrs)
- External CAD launch (P-3 depressurization not required)
- Automated real-time quality-controlled data file generation
- Expanded AirOPS display fields
- USB firmware update capability

**Proposed use in this project:** Primary low-altitude boundary layer sampling platform deployed from P-3 for TC PBL and surface-layer turbulence observations; 5-day field deployments annually (Sep-Nov) for 3 years

---

### Dragoon Coriolis
**What it is:** Long-duration hybrid-electric land-launched sUAS for extended low-altitude atmospheric profiling missions

**Specifications:**
- Cruise speed: 63 knots TAS
- Total takeoff weight: 15 kg
- Wingspan: 100 in (2.54 m); Length: 64 in (1.63 m)
- Endurance: 15-19 hours (depending on payload weight)
- Range: 1,100-1,370 statute miles
- Sensors: Pressure, temperature, humidity; Iridium satellite link for real-time data
- Launch: Electric rail (no runway required)
- Recovery: Belly landing (recoverable) or single-use
- Autopilot: PX4 Flight Stack
- Cost: <$15k per unit in quantity
- Current status: TRL 6 (Phase II SBIR ongoing)

**Proposed capabilities in this project:**
- Integration of Skyfora Streamsonde sensors for improved accuracy/reliability
- Low-altitude (<5,000 ft MSL) meteorological data collection around tropical disturbances
- Operations from land base when P-3 unavailable or storm out of range
- Long endurance enables sustained observation during storm evolution

**Regulatory status:**
- FAA Certificate of Authorization (COA) for BLOS operations expected early 2025
- Launch site: Small airstrip near Ft. Myers, Florida
- Flight region: Offshore warning area with large area coverage for storm intercept

**Proposed deployment:** Two one-week over-water field operations annually (years 1-3), August-November, aligned with NOAA weather observation goals

---

### StratoSolutions StratoSat-25 HAPS
**What it is:** Solar-electric stratospheric fixed-wing aircraft designed for persistent high-altitude