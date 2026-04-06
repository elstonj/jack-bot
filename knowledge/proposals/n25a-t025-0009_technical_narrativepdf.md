# Navy STTR 25.A-T025: Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- **Type:** Navy STTR Phase I Proposal - Technical Narrative
- **Client/Agency:** Office of Naval Research (ONR)
- **Program/Solicitation:** Navy STTR 25.A (N25A-T025-0009)
- **Date:** Submitted February 4, 2025 (last modified May 7, 2025)
- **BST Products/Systems Referenced:** S0 UAS (unmanned aircraft system)
- **Key Personnel:** 
  - Jack Elston (PI, CEO/Co-founder, BST)
  - Maciej Stachura (CTO, BST)
  - Joshua Wadler (Embry-Riddle Aeronautical University)
  - Jun Zhang (University of Miami)
  - John Park (Old Dominion University)

## Executive Summary
Black Swift Technologies proposes to adapt and enhance the S0 UAS for Navy-specific atmospheric profiling in hazardous weather environments (tropical cyclones, polar lows). The S0 offers superior cost-effectiveness and data density compared to traditional radiosondes and dropsondes, with demonstrated capability in extreme conditions. Phase I will focus on quantifying performance advantages, improving measurement accuracy, developing new observation capabilities (turbulence, wave measurements), and establishing integration pathways with Navy operational systems.

## Technical Approach

### S0 UAS Platform Overview
- **Design:** Purpose-built small UAS optimized for atmospheric profiling in extreme environments
- **Configurations:** Two variants available:
  - Disposable air-deployed version (expendable)
  - Reusable VTOL (vertical takeoff/landing) version for land/ship launch
- **Key Technical Specifications:**
  - Weight: 2.6 pounds
  - Ascent rate: 4 m/s
  - Descent rate: 6 m/s
  - Flight duration: 90+ minutes typical; up to 120 minutes projected with battery improvements
  - Current cost: $15K for 120 minutes of data (disposable version)
  
### Operational Capability Demonstrated (2024)
- 19 S0 units deployed operationally from NOAA WP-3D (P-3)
- Successfully operated in Category 5 hurricanes (Ernesto, Francine, Helene, Milton)
- Measured extreme conditions simultaneously: vertical velocities up to 30 m/s and horizontal winds up to 209 knots
- Collected data across four major tropical cyclones

### Sensors & Measurements
The S0 measures:
- 3D wind data (u, v, w components) via multi-hole probe at 100 Hz onboard processing
- Temperature and humidity
- Pressure
- Sea surface temperature
- Wave height (via laser altimeter; radar alternative under investigation)
- Vertical velocity and turbulence (derived from high-rate wind data)

### Comparative Advantages Over Existing Systems

**vs. NCAR Dropsondes (AVAPS):**
- Cost: $1,000 per 5 minutes of data → S0: $15K for 120 minutes (cost per observation 2-3x better for disposable; 50-100x better for reusable)
- Duration: Dropsondes provide single profile; S0 provides extended multi-profile missions
- Accessibility: S0 can be deployed from diverse platforms; dropsondes require specialized aircraft (P-3, WC-130J)
- Continuous data collection: S0 enables temporal tracking of storm evolution vs. episodic dropsonde deployments

**vs. Radiosondes:**
- Temporal resolution: Radiosondes 2x daily at fixed locations; S0 enables targeted, continuous sampling
- Spatial coverage: S0 can reach previously inaccessible areas (hurricane eyewalls, ice edges)
- Low-altitude capability: S0 excels at air-sea interface measurements; radiosondes create observational gaps critical for understanding boundary layer processes
- Reusability: S0 reduces cost accumulation over intensive campaigns

### Flight Patterns & Sampling Strategy
- **Stepped descent patterns:** 10 minutes per altitude level to measure boundary layer turbulence features
- **Spiral patterns:** For full atmospheric profiling
- **Autonomous/manual control:** Flight paths can be pre-programmed or dynamically controlled by operators to target specific regions of interest
- **Programmable sampling:** Enables high spatial and temporal resolution in critical observation areas

### Data Validation & Accuracy
- **Wind measurement validation** (SGP tower comparison, March-April 2021):
  - Mean differences within 0.50 m/s for all three wind components
  - Accurately captured turbulence magnitude and variance patterns
  - Successfully measured increasing vertical wind variance in dynamic conditions
  
- **Sensor improvements implemented:**
  - New shroud limiting solar influence on temperature/humidity measurements
  - Bias corrections from prior validation campaigns
  - Peer-reviewed manuscript on S0 validation currently under review

### Phase I Work Plan (Base & Option Tasks)

**Task B.1: Background Review & Comparative Analysis**
- Comprehensive review of existing platforms (NCAR dropsondes, radiosondes, Raytheon Coyote, Anduril Altius-600)
- Comparative analysis on cost, accuracy, coverage, and longevity
- Highlight S0 strengths and identify improvement areas
- **Lead:** ERAU, UM, BST

**Task B.2: S0 Data Analysis & Enhancements**
- Integration planning with Navy launch platforms (sonobuoy systems, P-8A Poseidon external pods, CH-53E helicopters)
- Simulation and mechanical testing for platform compatibility
- Detailed error analysis of wind, turbulence, and altitude measurements
- Icing mitigation strategies evaluation
- **Lead:** BST, ERAU, UM, ODU

**Task B.3: Turbulence & Wave Height Measurements**
- Develop onboard algorithms for high-rate turbulence computation (100 Hz wind data)
- Evaluate wave measurement requirements/accuracy specifications
- Investigate radar-based wave sensing (replacing laser altimeter limitations in heavy precipitation)
- **Lead:** BST, ERAU, UM

**Task B.4: Automatic Sampling Strategy**
- Two-level autonomy approach:
  - **Open-loop:** Pre-programmed rules derived from TC forecasting model utilities
  - **Closed-loop:** Machine learning surrogate models trained on hurricane forecast data for adaptive, real-time sampling
  - AI incorporates dimensionality reduction for UAS computational constraints
- **Lead:** ODU, BST

**Option Tasks (O.1-O.4):**
- **O.1:** Calibration/validation plan including wind tunnel tests, field deployments, tower/dropsonde comparisons
- **O.2:** Wave measurement system development for radar-based altitude sensing at 200+ mph ground speeds
- **O.3:** S0 icing operations (multi-hole probe, wings, propellers; design updates for all-weather capability)
- **O.4:** DoD stakeholder engagement and detailed Navy integration plan (hardware, software, logistics)

### Project Schedule
12-month Phase I with sequential/parallel base and option task execution (Gantt chart provided)

## Products & Capabilities Described

### S0 UAS System
**What it is:** A small unmanned aircraft system specifically designed for atmospheric profiling in hazardous environments

**Current capabilities demonstrated:**
- Operates in Category 5 hurricanes and extreme weather
- Autonomous navigation with operator control capability
- Long-duration low-altitude hovering and profiling
- Proven reliability through 2024 NOAA operations (19 deployments)

**Proposed enhancements (Phase I):**
- Navy-specific launch/recovery integration (sonobuoy, pod-mounted)
- Improved wind/turbulence measurement accuracy
- Onboard turbulence algorithms (100 Hz data compression)
- Radar-based wave measurement
- Icing mitigation (heating elements, coatings, sensor protection)
- Automated adaptive sampling via AI/ML

**Performance specifications:**
- Disposable variant cost: $15,000 (vs. $1,000 dropsondes for 5 min data)
- Data duration: 90-120 minutes of continuous profiling
- Measurement accuracy: Wind components within ±0.50 m/s (validated against tower)
- Operational wind envelope: Sustained to 209 knots with simultaneous vertical velocities to 30 m/s
- Sensor sample rates: 100 Hz for wind data (multi-hole probe)

## Use Cases & Applications

### Primary Mission: Tropical Cyclone & Hazardous Weather Monitoring
- **Air-sea interaction studies:** Measuring boundary layer thermodynamics, drag coefficients, momentum/enthalpy fluxes at air-sea interface
- **Storm intensity forecasting:** Providing high-resolution boundary layer data to improve TC intensity/track prediction
- **Marine atmospheric boundary layer (MABL) characterization:** Profiling wind, temperature, humidity, pressure in hurricane eyewalls and extreme wind regions previously inaccessible to crewed aircraft

### Secondary/Emerging Applications
- **Polar low research:** Profiling over Arctic/polar ice edges
- **Wave state characterization:** Sea surface conditions and wave energy during extreme weather
- **Turbulence measurement:** Fine-scale eddy structure in hurricane boundary layers
- **Military operational readiness:** Navy maritime operations supporting decision-making during severe weather events
- **Climate/environmental research:** Air-sea coupling in high-wind conditions; drag coefficient parameterization

### 2024 Operational Deployments (Demonstrated)
- Tropical Storm/Hurricane Ernesto: Stepped descent profiles measuring boundary layer turbulence
- Hurricane Francine: (deployed)
- Hurricane Helene: (deployed)
- Hurricane Milton: (deployed; extreme conditions: 209 kts wind + 30 m/s vertical velocity simultaneously)

## Key Results (from 2024 NOAA Partnership)

### Operational Achievements
- **19 S0 units** successfully launched from NOAA P-3 in 2024 hurricane season
- **Multi-storm coverage:** Operated in four major tropical cyclones (Ernesto, Francine, Helene, Milton)
- **Extended duration:** Battery life exceeded 90 minutes on multiple occasions; 120 minutes projected
- **Extreme wind survival:** Demonstrated sustained operation in simultaneous high vertical (30 m/s) and horizontal (209 kts) winds

### Data Validation Results
- **Wind measurement accuracy:** Mean differences ±0.50 m/s across all three components vs. instrumented tower (ARM SGP facility)
- **Turbulence capture:** S0 successfully measured similar histograms and variance patterns as calibrated tower instrument
- **Dynamic response:** Accurately captured increasing variance in vertical wind during transitional conditions

### Scientific Value Demonstrated
- New observations unavailable from radiosondes: vertical wind velocities, fine-scale turbulence (100 Hz resolution)
- Wave height and sea surface temperature co-located with atmospheric profiling
- Boundary layer profiling from near-surface to 2+ km altitude
- Potential for improved drag coefficient parameterization and TC intensity forecasting

## Notable Details

### Competitive Positioning
- **Unique hybrid design:** Both disposable (air-deployed) and reusable (VTOL) variants in single platform
- **Cost advantage:** 50-100x cheaper per observation than reusable systems; 2x cheaper than dropsondes
- **Proven in extreme conditions:** Demonstrated operational reliability in conditions exceeding design envelopes of competing systems
- **Compared competitors:** Raytheon Coyote, Anduril Altius-600 (mentioned as comparative platforms to be analyzed)

### Partnership & Infrastructure
- **NOAA collaboration:** Ongoing operational partnership; 2024 deployments from NOAA WP-3D; data access to advanced testing facilities
- **University consortium:**
  - **Embry-Riddle:** Wind tunnel facilities for sensor calibration/validation
  - **University of Miami:** MABL and TC dynamics expertise; air-sea interaction research
  - **Old Dominion University:** AI/ML path planning and adaptive sampling algorithms
- **ONR MURI collaboration:** SASCWATCH project (Dr. David Richter, Notre Dame) studying air-sea coupling at high winds

### Commercialization & Market Strategy
- **Target markets:** DoD (Navy priority), NOAA, NASA, USGS, private sector (energy, insurance, climate research)
- **Global UAS market:** Projected $58.4 billion by 2026
- **Revenue projections:**
  - Year 1 (Phase II): $1 million
  - Years 