# 2025-07-30 Kick Off Briefing: N25A-T025 Expendable Air-sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- Type: SBIR/STTR Phase I Kick-Off Briefing (presentation)
- Client/Agency: Department of the Navy (SYSCOM)
- Program/Solicitation: Navy SBIR/STTR Topic N25A-T025
- Contract Number: N68335-25-C-0270
- Date: July 22, 2025 (briefing); July 16, 2025 (kick-off meeting)
- BST Products/Systems Referenced: S0 (expendable UAS platform)
- Key Personnel: Dr. Jack Elston (PI), Dr. Maciej Stachura (Co-I)
- POC: Joshua Cossuth, Arlington, VA (703) 696-0703

## Executive Summary
Black Swift Technologies is executing a Navy STTR Phase I contract to validate the S0 expendable UAS platform for air-sea profiling in hazardous weather, specifically comparing performance against legacy systems (AVAPS dropsondes, Coyote systems) using recent hurricane datasets. The project will characterize sensor error sources, demonstrate unique observables (vertical wind, turbulence, wave state), and assess feasibility for targeted high-wind deployments to support Navy operations and COAMPS-TC modeling.

## Technical Approach

**Phase I Objectives:**

1. **Benchmark Performance**: Compare S0 data quality, resolution, and cost-efficiency against AVAPS and Coyote systems using 2023–2024 hurricane data; assess sensor tolerances, thresholds, and relaxation times.

2. **Error Characterization**: Identify dominant error sources in wind, turbulence, pressure, temperature, humidity, and wave sensing through wind tunnel tests and GNSS/IMU performance analysis.

3. **Capability Validation**: Validate high-rate products and test radar-based wave sensing; demonstrate unique observables unavailable from legacy platforms.

4. **Deployment Feasibility**: Review past S0 hurricane deployments; evaluate launch/control compatibility with Navy platforms and integration with automated, sensor-directed flight in high-wind environments.

**Facilities & Testing:**
- Black Swift Technologies Integration Lab (Boulder, CO): UAS prototyping, sensor integration, real-time processing
- Precipitation/icing test chamber: Simulate storm sensor exposure conditions
- Embry-Riddle Wind Tunnel: Planned for Phase II evaluation
- NOAA collaboration: Access to dropsonde data and atmospheric validation frameworks

**Risk Mitigation Strategies:**
- Altitude estimation without RTK: Dual-sensor fusion (GNSS + barometric) with dynamic corrections
- Sensor icing: Passive (hydrophobic coatings) and active (localized heating) de-icing
- Wave sensing in clouds/precipitation: Radar-based alternatives to laser altimetry
- Data volume/downlink: Onboard spectral/flux summaries and compression algorithms

## Products & Capabilities Described

### S0 (Expendable UAS)
- **What it is**: An air-deployable, expendable unmanned aircraft system designed for profiling atmospheric and ocean surface conditions in extreme weather (hurricanes, hazardous ocean conditions).
- **Deployment method**: Launched from P3 hurricane hunter aircraft and other naval platforms (P8, C-130, KC-135)
- **Primary measurements**: Pressure, temperature, humidity (PTH); 3D wind; sea surface temperature (SST); wave height; turbulence
- **2024 Performance**: 19 missions flown (17 successful); longest flight by air-deployed UAS into storm; highest wind measured by UAS (~1-2 m/s accuracy); max range to P3: 191 miles; 85–90% reliability; endurance ~105 min
- **2025 Improvements**:
  - Wind accuracy: 1–2 m/s → **0.2 m/s**
  - Data rate: ~3 Hz → **10 Hz**
  - New data products: Added turbulence, radar-based wave height (all-weather vs. laser/clear-air only)
  - Endurance: 105 min → **120 min**
  - Reliability: 85–90% → **>90%**
  - Manufacturing: 19 units (with tremendous effort) → **50 units** (with "light" effort)
  - Automation: Prototype auto-sampling → **Improved automated sampling and onboard data processing**

**Sensor Suite:**
- **Flush-Air Sensing Nose Cone**: High-rate 3D wind measurement
- **In Situ Atmospheric Probe**: Pressure, temperature, humidity
- **Surface Temperature Sensor**: Sea surface temperature
- **Wave Sensing**: Laser-based (2024) transitioning to **radar-based (2025)** for all-weather capability
- **Long-range Communications**: Maintains link to deployment aircraft
- **Onboard Processing**: Spectral analysis, flux calculations, automated data products

## Use Cases & Applications

**Primary (Phase I focus):**
- Hurricane reconnaissance and profiling (2024 missions: Hurricanes Ernesto, Francine, Helene, Milton)
- Boundary-layer atmospheric sampling in extreme ocean conditions
- Targeted, automated deployments in high-wind environments (>50 kt)
- Support for COAMPS-TC (Navy Coupled Ocean/Atmosphere Mesoscale Prediction System for Tropical Cyclones) modeling
- Navy weather and operations mission readiness

**Anticipated Secondary Markets (Phase II/Commercialization):**
- NOAA hurricane monitoring and boundary-layer research
- NASA boundary-layer and atmospheric science
- USGS and FEMA disaster response and environmental monitoring
- Commercial offshore platform monitoring (energy sector)
- Insurance risk assessment (real-time ocean-atmosphere hazard data)
- Wildfire monitoring and response
- Stratospheric balloon deployments (NASA partnerships) for storm tracking, disaster response

**Platform Integration Pathways:**
- 53rd Weather Reconnaissance Squadron (primary Navy integration)
- C-130: Drop site condition assessment
- P8: Magnetic anomaly detection ops
- KC-135: Magnetic mapping operations
- Stratospheric balloons: Multi-vehicle deployments from NASA high-altitude gondolas

## Deliverables & Timeline

**Phase I Deliverables:**
- Kickoff Briefing: July 22, 2025 ✓
- Base Period Progress Report: October 6, 2025
- Base Period Final Report: January 6, 2026

**Anticipated Phase I Results:**
1. Quantitative benchmarking of S0 vs. dropsondes and expendable UAS across wind, turbulence, and wave sensing
2. Validated error budget for all primary measurement types
3. Demonstrated feasibility of unique observables (vertical wind, turbulence, wave state, sea surface temperature) in operationally relevant conditions
4. Verified S0 suitability for targeted, automated deployments in high-wind (hurricane-force) environments
5. Preliminary integration plan for Navy sonobuoy launcher platforms

## Key Personnel

- **Dr. Jack Elston (Principal Investigator)**: PhD Aerospace Engineering; 15+ years UAS development; led NOAA, NASA, and DoD-funded UAS deployments into hurricanes and extreme environments
- **Dr. Maciej Stachura (Co-Investigator)**: PhD Aerospace Engineering; expert in sensor fusion and UAS calibration; architect of S0 onboard sensor processing and system validation
- **Advisors/Collaborators**: 
  - Dr. Jun Zhang (NOAA/AOML): Boundary-layer physics expertise
  - Dr. Josh Wadler (Embry-Riddle): UAS validation
  - Dr. John Park (Old Dominion): Wave-atmosphere coupling

## Notable Details

- **2024 Operational Track Record**: 19 hurricane missions across four storms (Ernesto, Francine, Helene, Milton) with 17 successful deployments establishes mature platform readiness
- **Dramatic Performance Improvements**: Wind accuracy improvement by 10× (1–2 m/s → 0.2 m/s) and data rate increase (3 Hz → 10 Hz) between 2024–2025 versions signal rapid capability maturation
- **Manufacturing Scalability**: Manufacturing capacity increased from 19 units (2024, with extreme effort) to 50 units (2025, light effort) indicates readiness for operational fleet deployment
- **Unique Sensor Capabilities**: Radar-based wave sensing (all-weather) and high-rate turbulence products are not available from legacy dropsonde systems (AVAPS, Coyote), addressing a critical Navy operational gap
- **Automation & Data Processing**: Shift from manual data post-processing to automated, onboard data products with P3 integration directly supports operational Navy weather workflows
- **Transition Strategy**: Multi-platform integration pathway (P3, P8, C-130, KC-135, stratospheric balloons) and diverse customer targets (Navy, NOAA, NASA, USGS, FEMA, commercial) suggest phase II focus on operational deployment and commercialization
- **COAMPS-TC Integration**: Direct support for Navy tropical cyclone forecasting and modeling community enhances relevance to core DoD weather operations
- **Risk-Aware Design**: Documented mitigation strategies for challenging ocean environment issues (RTK denial, icing, precipitation, bandwidth constraints) demonstrate systems engineering maturity

---

**Classification**: Controlled Unclassified Information (CUI), SBIZ; DISTRO B. Distribution authorized to U.S. Government agencies only.