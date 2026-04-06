# Improving NOAA Forecasts by Advancing the Capabilities of UAS to Sample Tropical Cyclones from the Ocean Surface to the Stratosphere

## Document Metadata
- **Type**: Research proposal (submitted)
- **Client/Agency**: NOAA/OMAO (Office of Oceanic and Atmospheric Research, Office of Marine and Aviation Operations)
- **Program/Solicitation**: 2025 Breakthroughs with Uncrewed Systems Technology RFP; Targeted RFP priorities: Vertical meteorological profiling, Medium/Large UAS applications, Payload optimization
- **Date**: Submitted October 17, 2024 (digitally signed)
- **BST Products/Systems Referenced**: Black Swift Technologies S0 (sUAS)
- **Key Personnel**: 
  - Dr. Joseph J. Cione (Principal Investigator, NOAA/AOML/Hurricane Research Division)
  - Dr. Jun A. Zhang (Co-PI, University of Miami/CIMAS & NOAA/AOML)
  - Dr. Joshua B. Wadler (Co-PI, Embry-Riddle Aeronautical University)
  - Dr. Ghassan Alaka (Division Director, NOAA/AOML/Hurricane Research Division)

## Executive Summary
This three-year proposal ($1,895,208 total, 87% to universities) aims to advance NOAA's uncrewed systems capabilities for tropical cyclone (TC) forecasting by operationalizing three distinct UAS platforms: Black Swift Technologies' S0 small UAS for low-altitude boundary layer sampling; Dragoon's Coriolis hybrid-electric long-duration aircraft for land-based deployments; and StratoSolutions' StratoSat-25 solar-powered HAPS for stratospheric dropsonde deployment. Real-time data will be delivered to NOAA's National Hurricane Center and Environmental Modeling Center to improve TC track and intensity forecasts.

## Technical Approach

### Black Swift S0 sUAS (Section 2.1)
- **Current status**: Readiness Level 7; successfully deployed in Hurricanes Tammy (2023), Ernesto, Francine, Helene, Milton (2024)
- **Deployment method**: Launched from P-3 aircraft via A-sized sonobuoy chute in folding container with parachute; aircraft unfolds after deployment
- **Capabilities**: Samples low-altitude boundary layer where energy/momentum exchange occurs; currently non-recoverable over water; data transmitted via two-way radio
- **Hardware improvements** (Section 2.1a):
  - Moving baseline RTK GPS for heading (replacing magnetometer) to improve accuracy in high-interference environments
  - Data buffering and re-transmission capability during lost communications windows
  - Laser altitude sensor optimization for operation in heavy precipitation (eyewall and rainbands)
  - Onboard video capability for real-time situational awareness
- **Operational efficiency improvements** (Section 2.1b):
  - Firmware, communications, and user interface customization for autonomy (reduce pilot dependency)
  - Extended battery endurance: current ~1.5 hours → potential +30 min through battery enhancements
  - External launch via CAD (Carriage Ejector Device) instead of A-sized sonobuoy chute (reduces cabin depressurization requirements)
  - Enhanced airOPS display fields: laser altitude, radio signal quality, time since last communication
  - USB firmware update capability in tube without parachute reset
  - Real-time quality-control netCDF file generation (currently post-processed, can take days)
- **Meteorological instrument enhancements** (Section 2.1c):
  - Wind tunnel testing of multi-hole pressure probe to characterize wing effects on wind measurements
  - Increased reporting frequency from 2-3 Hz to ≥10 Hz for turbulence-scale process analysis
  - Laser-based altitude control instead of GPS altitude (maintains consistent height above sea surface)

### Dragoon Coriolis Aircraft (Section 2.2)
- **Current status**: Readiness Level 6; undergoing initial flight testing under NOAA Phase II SBIR
- **Target status**: Readiness Level 8
- **Specifications**:
  - Long-duration (15-19 hour endurance at varying payload weights)
  - Cruise speed: 63 knots
  - Gross weight: 15 kg
  - Wingspan: 100 inches; Length: 64 inches
  - Payload capacity: 1-5 lbs
  - Hybrid electric powerplant; recoverable via belly landing or single-use recovery
  - Autopilot: PX4 Flight Stack
  - Iridium satellite link for real-time data transmission
- **Instrumentation**: Pressure, temperature, humidity sensors
- **Deployment approach**: Land-based launch from Florida (eventually Ft. Myers airstrip with FAA Certificate of Authorization pending for Q1 2025); planned for use when P-3 unavailable or out of range
- **Mission plan**: Two one-week flight operations in Florida annually (FY25-FY27), aligned with NOAA weather observation goals

### StratoSolutions StratoSat-25 HAPS (Section 2.3)
- **Current status**: Readiness Level 3; feasibility studies completed
- **Target status**: Readiness Level 6
- **Platform characteristics**:
  - Solar electric stratospheric HAPS (High Altitude Pseudo-Satellite)
  - Fixed-wing, high aspect-ratio design (~12.5 m wingspan)
  - Gross weight: 25 kg
  - Persistent loiter capability over target areas
  - Photovoltaic cells on wings generate power; excess charges high-energy-density batteries for night cruising
- **Micro-dropsonde capability**:
  - Compact micro-dropsondes designed for stratospheric storage in self-contained dispensing system
  - Current system: 400g dispenser carrying 10 dropsondes = 25 micro-dropsondes per kilogram payload weight
  - Enhanced dispenser with improved battery technology: target >50 micro-dropsondes per kilogram
  - Goal: 100 dropsondes per mission using full 2 kg payload capacity
  - Dispenser includes UHF antenna/receiver for decoding dropsonde transmissions during descent
  - Low power consumption: <0.5W average, including dropsonde warming/charging/preparation
- **Aeroelastic innovations**:
  - Voltitude's proprietary "gust alleviation" technology demonstrated to reduce wing bending loads by ~50% during turbulence and double maximum flight speed envelope
  - Enables more frequent launch/recovery and dropsonde restocking
- **Operations base**: St. Vincent Island, Cabo Verde (existing facility from previous stratospheric balloon operations)
- **Airspace**: FAA approval sought for flights above FL600 in SAL OCEANIC and PIARCO Flight Information Regions; flight permits expected from Barbados and Cabo Verde CAAs

## Products & Capabilities Described

### Black Swift S0
- **What it is**: 1.58 kg (~3 lb) small uncrewed aircraft system designed for atmospheric measurement
- **Specifications**:
  - Cruise speed: 26 m/s
  - Wingspan: 1.38 m
  - Maximum altitude: ~4600 m
  - Battery life: ~1.5 hours (upgradeable to ~2 hours)
  - Can fly at GPS or pressure altitudes
  - Deployable via parachute from P-3 aircraft
- **Use in this context**: Primary platform for routine boundary layer turbulence sampling in tropical cyclones; advancement toward Readiness Level 9 (full operational status) through hardware, payload, and efficiency improvements
- **Performance claims**: Only current in-situ mechanism for turbulence-quality measurements throughout TC planetary boundary layer down to ocean surface; successfully deployed multiple times in 2023-2024 hurricane season

### Dragoon Coriolis
- **What it is**: Hybrid-electric, long-duration, low-cost medium UAS designed for scalable multi-aircraft operations
- **Use in this context**: Land-based platform to sample TCs when P-3 unavailable or out of range; complements BST S0 capability; supports low-altitude meteorological data collection
- **Performance specifications**: 15-19 hour endurance, 63-knot cruise speed, satellite telemetry link

### StratoSolutions StratoSat-25
- **What it is**: Solar-powered fixed-wing stratospheric platform capable of persistent loiter and micro-dropsonde deployment
- **Use in this context**: Addresses upper-level sampling gap (outflow layer, 14-16 km altitude) critical for TC intensity change indicators; complements low-altitude S0 and mid-altitude Coriolis
- **Performance claims**: Can deploy 25-100 micro-dropsondes per mission; persistent operation capability; improved wing load management via gust alleviation technology

## Use Cases & Applications

1. **Tropical Cyclone Boundary Layer Sampling** (Primary use case)
   - Measure wind, temperature, humidity, and turbulence within planetary boundary layer (PBL) where momentum/enthalpy exchange with ocean occurs
   - Currently sampled only by P-3 at ~3000m altitude or GPS dropsondes; S0 fills gap at surface to 1000m altitude
   - Focus on air-sea interaction processes controlling intensity change
   - Applications: Hurricane Tammy (2023), Hurricanes Ernesto, Francine, Helene, Milton (2024)

2. **Upper-Level Outflow Layer Characterization**
   - Stratospheric HAPS deployed micro-dropsondes to sample 14-16 km altitude region
   - Identified as indicator of TC intensity change and related to diurnal cycle
   - Supports track forecast improvement (literature shows 500 mb wind vector sensitivity)
   - Previously done via NASA Global Hawk or NOAA G-IV; stratospheric HAPS provides low-cost alternative

3. **Real-Time Forecast Support**
   - Data delivered to NOAA National Hurricane Center for situational awareness and AWIPS2 visualization
   - Data assimilation into Environmental Modeling Center's operational TC forecast models (HAFS, UFS)
   - Support to emergency management and operational forecasters

4. **Model Physics Validation and Improvement**
   - Turbulence observations used to validate/improve boundary layer parameterizations in HAFS
   - Exchange coefficient calculations (momentum, enthalpy) from multi-hole probe measurements
   - Vertical eddy diffusivity calculations to improve surface layer parameterizations

## Key Results (For Reports)

Not a report with results; this is a proposal for future work. However, the document cites successful past deployments:
- **S0 deployment history**: Successfully launched in Hurricanes Tammy (2023) and Ernesto, Francine, Helene, Milton (2024); missions advanced readiness to Level 7
- **Reference to prior impacts**: Crewed aircraft sUAS (Coyote) data from Hurricanes Maria (2017) and Michael (2018) showed measurable forecast improvements through model assimilation
- **Existing model improvements**: Boundary layer physics upgrades in HAFS based on crewed aircraft data led to substantial intensity forecast improvements (citations: Hazelton et al. 2024; Gopalakrishnan et al. 2021)

## Notable Details

### Budget and Resource Allocation
- **Total 3-year budget**: $1,895,208
  - FY25: $526,425
  - FY26: $736,473
  - FY27: $632,310
- **In-kind NOAA support**: $1,425,000 total (P-3 flight hours: $1,350,000; labor/overhead: $75,000)
- **University allocation**: 87% of total budget ($1,654,207) goes to universities (UM/CIMAS and Embry-Riddle)
- **Key procurements**:
  - BST S0 engineering/technical support: $329,000 over 3 years
  - Dragoon Coriolis spare parts and operations: $108,806
  - StratoSolutions StratoSat-25 engineering/demo: $356,720
  - Skyfora Streamsondes (75 units annually): $100,125 total
  - NHC support (CIRA facilitator): $100,000 (first 2 years)

### Operational Transition Infrastructure
- **Real-time data flow**: NOAA's Cooperative Institute for Research in the Atmosphere (CIRA) manages dataflow to National Hurricane Center