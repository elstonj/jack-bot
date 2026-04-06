# Phase I Kick-Off Briefing: Expendable Air-sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- **Type:** SBIR Phase I Kick-Off Briefing
- **Client/Agency:** Department of the Navy (SBIR/STTR Program)
- **Program/Solicitation:** N25A-T025; Contract No. N6833525C0270
- **Date:** July 22, 2025 (briefing date: July 16, 2025)
- **BST Products/Systems Referenced:** S0 (expendable air-sea profiling UAS)
- **Key Personnel:** 
  - Dr. Jack Elston (PI) – PhD Aerospace Engineering, 15+ years UAS development
  - Dr. Maciej Stachura (Co-I) – PhD Aerospace Engineering, sensor fusion and calibration expert
  - Advisors: Dr. Jun Zhang (NOAA/AOML), Dr. Josh Wadler (Embry-Riddle), Dr. John Park (Old Dominion)

## Executive Summary
Black Swift Technologies proposes to develop and validate the S0 expendable UAS for high-resolution atmospheric and wave measurements in hazardous weather conditions (hurricanes). Phase I will benchmark S0 performance against legacy platforms (AVAPS dropsondes, Coyote systems), characterize sensor error sources, demonstrate unique observables, and assess feasibility for targeted sampling in high-wind environments. Results will support Navy operational integration and expansion to NOAA, NASA, USGS, and FEMA.

## Technical Approach

### Phase I Objectives & Approach

**Objective 1: Data Quality & Cost Benchmarking**
- Compare S0 accuracy, resolution, and cost against AVAPS and Coyote systems
- Analyze 2023–2024 hurricane datasets
- Explore S0 measurement potential through sensor tolerance analysis, thresholds, and relaxation time

**Objective 2: Error Source Identification**
- Perform wind tunnel tests and error analysis
- Assess GNSS/IMU performance and response times
- Characterize dominant error sources in wind, wave sensing, pressure, temperature, humidity, and turbulence

**Objective 3: Unique Observable Demonstration**
- Validate high-rate products and turbulence measurements
- Test radar-based wave sensing in cloud and precipitation conditions

**Objective 4: High-Wind Targeted Sampling Feasibility**
- Review S0 hurricane deployments
- Evaluate control, launch compatibility, and Navy data needs
- Create plan for targeted, automated observation and validation methods

### Work Plan Summary
1. **Benchmark Performance:** Compare S0 against AVAPS dropsondes and other UAS sources using 2023–2024 hurricane datasets
2. **Error Characterization:** Identify and quantify dominant measurement error sources; develop plans for reduction
3. **Sensor & Capability Expansion:** Evaluate radar-based wave sensing alternatives; implement onboard processing for flux and spectral products
4. **Targeted Deployment Feasibility:** Plan automated observation methods and performance validation

## Products & Capabilities Described

### S0 System (Expendable Air-sea Profiling UAS)

**Physical Configuration:**
- Automated, sensor-directed flight in hurricanes
- Minimal operator overhead for crew on P-3 hurricane hunter
- Air-deployed from crewed platforms (P-3, P-8, C-130, KC-135)

**Sensor Suite:**
- **Flush-Air Sensing Nose Cone:** High-rate 3D wind measurements
- **In Situ Atmospheric Probe:** Pressure, temperature, humidity (PTH)
- **Surface Temperature Sensor:** Sea surface temperature (SST)
- **Wave Height Measurement:** Transitioning from laser (clear-air only) to radar-based (all-weather)
- **Long-Range Communications:** Integration with NOAA systems

**Performance Improvements (2024 → 2025):**
| Specification | 2024 | 2025 |
|---|---|---|
| Wind Accuracy | 1–2 m/s | 0.2 m/s |
| Data Rate | ~3 Hz | 10 Hz |
| Data Products | PTH, 3D wind, SST | 2024 + Turbulence |
| Wave Height | Laser (clear-air only) | Radar (all-weather) |
| Endurance | 105 min | 120 min |
| Reliability | 85–90% | >90% |
| Manufacturing Capacity | 19 units (tremendous effort) | 50 units (light effort) |
| Automation | Prototype auto-sampling | Improved sampling + automated onboard P-3 data processing |

**2024 Operational Track Record:**
- 19 missions flown, 17 successful
- 4 hurricanes deployed: Ernesto (4 flights), Francine (4 flights), Helene (7 flights), Milton (4 flights)
- Longest flight by air-deployed UAS into storm
- Highest wind measured by UAS
- Maximum range to P-3: 191 miles

## Use Cases & Applications

### Primary (Phase I Focus)
- **Hurricane monitoring and atmospheric profiling** – Real-time boundary-layer observations during extreme weather
- **Navy weather operations** – Support for COAMPS-TC modeling community and tactical mission readiness
- **Air-sea coupling research** – Wave-atmosphere interaction measurement in high-wind conditions

### Transition & Secondary Applications

**DoD Integration:**
- P-3 hurricane reconnaissance (primary target)
- P-8 deployment (in combination with magnetic anomaly detection)
- C-130 deployment (drop site condition assessment)
- KC-135 deployment (magnetic mapping applications)
- Integration with 53rd Weather Reconnaissance Squadron

**Federal Agencies:**
- NOAA: Hurricane monitoring and boundary-layer observations
- NASA: Stratospheric balloon gondola deployment (10s of aircraft per gondola); covers flight costs
- USGS: Environmental monitoring
- FEMA: Disaster response

**Commercial Markets:**
- Energy sector: Offshore platform monitoring
- Insurance industry: Real-time risk assessment
- Wildfire monitoring
- Disaster response

**NASA Stratospheric Balloon Integration:**
- Deploy S0 from high-altitude balloon gondolas
- Enable storm tracking and deployment without crewed aircraft
- Broader application to wildfire and disaster response

## Key Results

### 2024 Hurricane Deployment Summary
- **Total Missions:** 19 flights across 4 hurricanes
- **Success Rate:** 17 of 19 successful (89.5%)
- **Operational Achievements:**
  - Longest flight by air-deployed UAS into storm environment
  - Highest wind speed recorded by any UAS platform
  - Extended range: 191 miles from P-3
  - Demonstrated sustained operations in hurricane-force conditions

### Anticipated Phase I Results
1. **Validated error budget** for wind, turbulence, and wave sensing
2. **Benchmarked S0 performance** against dropsondes (AVAPS) and expendable UAS (Coyote)
3. **Demonstrated feasibility** of collecting unique observables (vertical wind, turbulence, wave state) unavailable via legacy systems
4. **Verified S0 suitability** for targeted deployments in high-wind hurricane environments
5. **Quantitative proof** of S0's superior data quality, resolution, and cost-efficiency vs. legacy platforms

## Notable Details

### Challenges & Risk Mitigation
| Challenge | Mitigation Strategy |
|---|---|
| Accurate altitude estimation without RTK in remote ocean | Dual-sensor fusion (GNSS + barometric pressure) with dynamic correction models |
| Sensor icing in high-moisture/cold air | Passive (hydrophobic coatings) and active (localized heating) de-icing solutions |
| Wave sensing limitations in cloud/precipitation | Evaluate radar-based alternatives to laser altimetry; validate in high-wind test scenarios |
| Data volume vs. downlink bandwidth | Develop onboard summary metrics (spectra, fluxes) and compression algorithms |

### Facilities & Infrastructure
- **Black Swift Technologies Integration Lab** (Boulder, CO): UAS hardware prototyping, sensor integration, real-time processing
- **Precipitation/Icing Test Systems:** Custom chamber for simulating storm sensor exposure
- **NOAA Collaboration:** Access to dropsonde data, evaluation frameworks, atmospheric expertise
- **Embry-Riddle Wind Tunnel:** Available for Phase II testing (not Phase I)

### Transition & Success Planning
- **Target Users:** Navy weather and operations teams; COAMPS-TC modeling community
- **Unique Value:** Actionable atmospheric and wave observables unavailable via dropsondes or manned platforms
- **Integration Path:** Define mechanical, electrical, and software interfaces for sonobuoy launcher platforms
- **Phase II Focus:** Full Navy operational integration and real-time use demonstration with continuous stakeholder feedback

### Delivery Schedule
- Kickoff Briefing: July 22, 2025 ✓
- Base Period Progress Report: October 6, 2025
- Base Period Final Report: January 6, 2026

---

**Classification:** CUI (Controlled Unclassified Information) / SBIR Proprietary  
**Distribution:** DISTRO B (U.S. Government agencies only)  
**POC:** Joshua Cossuth, Arlington, VA (703) 696-0703