# Air-Deployed sUAS and StreamSonde Measurements of Turbulence in the High Wind Tropical Cyclone Surface Layer

## Document Metadata
- **Type:** Research Proposal
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration) - Internal 2023 Request for Proposals from OAR UxS Research Transition Office and OMAO UxS Operations Center
- **Program/Solicitation:** NOAA 2023 UxS (Unmanned Systems) Program
- **Date:** Submitted June 30, 2023 (signed April 2, 2023)
- **Project Period:** May 1, 2023 to April 30, 2025
- **BST Products/Systems Referenced:** S0 (primary sUAS platform)
- **Key Personnel:** 
  - Dr. Joseph J. Cione (Principal Investigator, NOAA/AOML/HRD)
  - Dr. Jun A. Zhang (Co-PI, NOAA/AOML/HRD)
  - Dr. Joshua B. Wadler (Co-PI, Embry-Riddle Aeronautical University)
  - Dr. Frank D. Marks (Division Director, NOAA/AOML/HRD)

## Executive Summary
This proposal seeks to deploy air-launched small unmanned aircraft systems (sUAS) and atmospheric profilers to measure turbulence in the tropical cyclone (TC) boundary layer and surface layer with the goal of improving NOAA's operational hurricane forecasts. Over a two-year period (FY23-FY25), the project will use Black Swift Technologies' S0 platform and Skyfor's StreamSonde atmospheric profiler to collect high-resolution wind, temperature, and humidity data in hurricane conditions, enabling calculation of critical drag and enthalpy exchange coefficients that are poorly understood at high wind speeds. The data will be transitioned to NOAA's National Hurricane Center and Environmental Modeling Center for real-time situational awareness and operational model improvements.

## Technical Approach

### Scientific Objective
Calculate momentum flux (τ), sensible heat flux (Qs), and latent heat flux (Ql) using direct eddy correlation method to determine exchange coefficients (CD, Ch, Cq) in the high-wind surface layer of tropical cyclones. These coefficients are critical for parameterizations in operational forecast models but are currently poorly constrained at wind speeds >30 m/s.

### Field Experiment Structure
Three well-designed modules will be conducted:
1. **Eyewall module** - core storm sampling
2. **Eye-eyewall mixing module** - transition region dynamics
3. **Inflow module** - outer circulation dynamics

Target: >100 flux runs at altitudes 10-200m

### Data Collection Platforms

**Black Swift Technologies S0 Platform:**
- Weight: 3 pounds
- Flight duration: 1-1.5 hours (demonstrated >1.2 hours in clear-air test flights, March 2023)
- Advanced altimeters and turbulence probes
- Wind measurement rate: up to 100 Hz
- Payload: thermodynamic sensors (temperature, humidity), sea surface temperature estimation
- Configuration: Air-deployed from NOAA P-3 Hurricane Hunter aircraft

**Skyfor StreamSonde Atmospheric Profiler:**
- Lightweight design: 14 grams
- Descent rate: 3-5 m/s (allows extended profile duration vs. standard dropsondes)
- Multi-constellation, dual-band GNSS receiver for maximum satellite signal availability
- Sensors: Pressure, temperature, humidity + 3D motion sensors (accelerometer, gyro, magnetometer) for turbulence-quality wind measurements
- Frequency: 400.01–405.99 MHz meteorological band
- Compatibility: Designed to work with existing AVAPS infrastructure on P-3 and other aircraft
- Post-processing: Compatible with ASPEN (Atmospheric Sounding Processing Environment) software
- Status: Successfully tested on NOAA P-3 in March 2023 (cleared basic engineering/safety hurdles, RL6-7 range)

## Products & Capabilities Described

### Black Swift S0 sUAS
**What it is:** Miniature air-deployable unmanned aircraft for boundary layer sampling in extreme weather environments

**Proposed Use:** 
- Primary platform for direct measurement of turbulent quantities (velocity components, temperature, humidity) in TC boundary layer
- Will measure fluxes at multiple altitudes between 10-200m
- Provides high-frequency (100 Hz) wind data enabling direct eddy correlation calculations
- Complements P-3 dropsonde data with continuous flight-level measurements

**Performance Claims/Specifications:**
- Successfully operated in Hurricane Edouard (2014): 9 total sUAS deployed across 3 hurricanes (2014-2018)
- Coyote platform record: 87 m/s wind speed at 641m altitude
- Altius600 (newer generation): Set record for longest duration in hurricane (102 minutes) and highest wind speed observed (215 mph at ~2100 ft)
- Lowest altitude achieved for flux observations: ~100m for 5 minutes
- Demonstrates capability to operate in high-wind eyewall regions where crewed aircraft cannot safely operate

**Readiness Level Goal:** Advance from RL5-6 to RL8 (operational transition) by end of project

### Skyfor StreamSonde
**What it is:** Lightweight atmospheric profiler designed specifically for tropical cyclone applications with enhanced turbulence measurement capability

**Proposed Use:**
- Complementary platform to S0 sUAS
- Deployed via existing dropsonde/AVAPS infrastructure (no new hardware required on aircraft)
- Will validate sUAS measurements
- Provides additional high-resolution vertical profiles with explicit turbulence focus

**Specifications:**
- 14-gram weight enables slow descent (3-5 m/s) for detailed boundary layer sampling
- Dual-band GNSS with multi-constellation support
- Integrated 3D motion sensors for turbulence-quality measurements
- Compatible with ASPEN processing software for seamless integration into existing workflow

**Readiness Level Goal:** Advance from RL6-7 (post-March 2023 testing) to RL8-9 by end of project

## Use Cases & Applications

### Primary Mission: Hurricane Intensity Prediction
The fundamental use case is improving NOAA's operational hurricane intensity forecasts through better understanding of the tropical cyclone planetary boundary layer (PBL).

### Specific TC Sampling Modules

**1. Eyewall Module**
- Direct sampling of the most intense, most dangerous part of the hurricane
- Measurement of eyewall turbulence properties
- Data currently unavailable due to safety constraints on crewed operations

**2. Eye-Eyewall Mixing Module**
- Measure mixing dynamics at the boundary between eye and eyewall
- Understand entrainment and energy exchange

**3. Inflow Module**
- Sample inflowing air in outer rainbands
- Characterize boundary layer properties at greater distances from storm center

### Historical Precedent
- **Hurricane Maria (2017):** 6 sUAS flights collected 256.5 minutes total of data, primarily below 1 km altitude
- **Hurricane Michael (2018):** 1 sUAS mission; lowest altitude achieved ~100m for sustained observations
- **Hurricane Ian (2022):** Altius600 set duration record (102 minutes) and wind speed record (215 mph)

### Critical Data Gap Being Addressed
Prior to 2017, ~100 times more data existed on wind speed than temperature/humidity in TC boundary layer. Even turbulence measurements are extremely rare. Previous direct flux observations limited to ~30 m/s; this project targets hurricane-force winds (>60 m/s).

## Key Results (None Yet - This is a Proposal)

**Project is in proposal stage; no results yet. However, it builds on:**

### Historical Validation Data (from prior sUAS missions):
- Figure 4a shows momentum flux (|τ|) vs. mean wind speed from 2017-2018 sUAS flights compared to P-3 observations
  - sUAS data extends to higher wind speeds than P-3
  - Comparison shows reasonable agreement with established relationships
- Figure 4b shows non-dimensional momentum flux vs. height
  - sUAS data tracks similarly to P-3 observations
  - Shows expected decrease with height in boundary layer

## Notable Details

### Operational Transition Integration
The proposal explicitly designs for transition from research to operations:

**Real-Time Data Delivery:**
- sUAS data will be transmitted to NOAA's National Hurricane Center (NHC) in real-time via Advanced Weather Interactive Processing System-2 (AWIPS-II)
- Data will feed to National Centers for Environmental Prediction's Environmental Modeling Center (EMC) for data assimilation
- Situational awareness tool (AirOPS) on P-3 will display sUAS data in flight

**Related Operational Efforts (No-Cost Collaboration):**
- Dr. Sippel (AOML) is conducting parallel OMAO-funded project testing sUAS data impact on Hurricane Weather Research and Forecast (HWRF) model
- Work will be extended to HAFS (new NOAA operational model)
- Data assimilation system development will ensure sUAS data can be ingested in optimal manner

### Budget & Resources
- **Total 2-Year Project Budget:** $965,830 (federal funding)
  - FY23: $489,305 (includes $172,250 for hardware, $75,000 technical support)
  - FY24: $476,525 (includes $150,000 for sUAS hardware, $22,250 for StreamSondes)
- **In-Kind Support:** $796,699 (primarily P-3 flight hours)
  - Estimated ~100 hours of P-3 time over 2-year period for missions and calibration

### Technology Maturation Status
- **S0 sUAS:** Currently RL5-6; goal is RL8 by project completion
- **StreamSonde:** Achieved RL6-7 after March 2023 field testing; goal is RL8-9
- Pre-season payload calibration and integration work already completed (March 2023)

### Partnerships & Contracting
- Black Swift Technologies: Contracted to deliver 10 S0 platforms in FY23 and 10 more in FY24
- Skyfor: Contracted to deliver 50 StreamSondes in FY23 and 50 in FY24
- University of Miami/CIMAS: Administrative support and post-doctoral associate
- Embry-Riddle Aeronautical University: Technical analysis support

### Data Management & Dissemination
- All data stored at NOAA/AOML
- Quality-controlled data released to public within 1 year of collection
- Code development managed in public repository
- Results published in peer-reviewed journals and conference presentations

### Key Problem Being Solved
**The Critical Data Void:** Exchange coefficients (CD, Ch, Cq) for momentum, sensible heat, and latent heat are:
- Poorly constrained at high wind speeds (>30 m/s)
- Derived mostly from indirect methods with >50% errors
- Critical for accurate TC intensity forecasts
- Previously limited to observation windows >100 km from storm center

**Why sUAS + StreamSonde Solves It:**
- Can safely sample high-wind eyewall regions (10-200m altitude)
- Provide direct eddy-correlation flux measurements
- Enable calculation of exchange coefficients in hurricane-force winds (first time attempted)
- Can collect >100 flux runs for robust statistical characterization

### Historical Context of sUAS in Hurricanes
- 2005: First-ever UAS flight into tropical cyclone (Tropical Storm Ophelia) - collected real-time wind data for NHC forecasts
- 2007: Hurricane Noel missions established duration (17.5h) and minimum altitude (82m) records
- 2014-2018: Coyote platform missions in Hurricanes Edouard, Maria, Michael
- 2022: Altius600 set new records in Hurricane Ian

---

**Document Assessment:** Comprehensive, well-structured research proposal with clear objectives, detailed technical approach, strong historical validation, explicit operational transition plan, and realistic budget. The proposal effectively documents Black Swift Technologies' S0 platform as the primary measurement platform and emphasizes its role in advancing hurricane forecasting capabilities at NOAA.