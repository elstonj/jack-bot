# 2025-07-16 Kick Off Briefing: Navy STTR Phase I – Expendable Air-sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- **Type:** SBIR/STTR Phase I Kick-Off Briefing (presentation)
- **Client/Agency:** Department of the Navy (SBIR/STTR Program)
- **Program/Solicitation:** N25A-T025; Navy STTR Topic
- **Contract Number:** N68335-25-C-0270
- **Date:** Kick-off July 16, 2025; Briefing presented July 22, 2025
- **BST Products/Systems Referenced:** S0 (expendable air-sea profiling UAS)
- **Key Personnel:** 
  - Dr. Jack Elston (PI) – PhD Aerospace Engineering; 15+ years UAS development
  - Dr. Maciej Stachura (Co-I) – PhD Aerospace Engineering; sensor fusion and UAS calibration expert
  - Beck Cotter (document editor)
  - Advisors: Dr. Jun Zhang (NOAA/AOML), Dr. Josh Wadler (Embry-Riddle), Dr. John Park (Old Dominion)
- **Navy POC:** Joshua Cossuth, Arlington, VA. (703) 696-0703

## Executive Summary
Black Swift Technologies is conducting a Navy STTR Phase I effort to develop and validate the S0 expendable air-sea profiling UAS for hazardous weather observation, particularly hurricane monitoring. The program will benchmark S0 performance against legacy systems (AVAPS dropsondes, Coyote UAS), characterize measurement errors, expand sensor capabilities (especially radar-based wave sensing), and demonstrate feasibility for targeted, automated deployments in high-wind environments.

## Technical Approach

### Phase I Objectives & Work Plan

**Objective 1: Performance Benchmarking**
- Compare S0 data quality, resolution, and cost against AVAPS dropsondes and other platforms
- Analyze recent (2023–2024) hurricane datasets
- Assess sensor tolerances, thresholds, and relaxation time to understand measurement potential

**Objective 2: Error Characterization**
- Identify dominant error sources in wind, turbulence, pressure, temperature, humidity, and wave sensing
- Conduct wind tunnel tests and GNSS/IMU performance analysis
- Assess sensor response times

**Objective 3: Demonstrate Unique Observables**
- Validate high-rate products
- Test radar-based wave sensing in cloud and precipitation conditions
- Develop onboard processing for flux and spectral products

**Objective 4: Feasibility Assessment**
- Review S0 hurricane deployment history
- Evaluate control, launch compatibility, and Navy data needs for high-wind operations
- Create plan for targeted, automated observation with performance validation methods

### Key Technical Improvements (2024 → 2025)
| Metric | 2024 | 2025 |
|--------|------|------|
| Wind Accuracy | 1–2 m/s | 0.2 m/s |
| Data Rate | ~3 Hz | 10 Hz |
| Wave Height Sensing | Laser (clear air only) | Radar (all weather) |
| Endurance | 105 min | 120 min |
| Reliability | 85–90% | >90% |
| Manufacturing Capacity | 19 units (with effort) | 50 units (light effort) |
| Data Products | PTH, 3D wind, SST | 2024 + Turbulence |

### Risk Mitigation Strategies
- **Altitude estimation without RTK:** Dual-sensor fusion (GNSS + barometric pressure) with dynamic correction models
- **Sensor icing:** Passive (hydrophobic coatings) and active (localized heating) de-icing solutions
- **Wave sensing in clouds/precipitation:** Radar-based alternatives to laser altimetry; validation in high-wind tests
- **Data volume vs. downlink bandwidth:** Onboard summary metrics (spectra, fluxes) and compression algorithms

## Products & Capabilities Described

### S0 System
**What it is:** Expendable air-sea profiling UAS designed for deployment from crewed aircraft (P3 Orion, C-130, KC-135, P8) into hurricanes and hazardous weather environments.

**Key Capabilities:**
- Flush-air sensing nose cone for aerodynamic wind measurement
- High-rate three-dimensional wind sensing
- Pressure, temperature, and humidity measurements via in-situ atmospheric probe
- Surface temperature sensing
- Wave height measurement (2024: laser; 2025: radar for all-weather capability)
- Long-range communications (191 miles demonstrated range to P3)
- Automated, sensor-directed flight in hurricanes with minimal operator overhead
- Onboard processing for real-time flux and spectral calculations
- Multi-hour endurance (120 min demonstrated in 2025)

**2024 Operational Performance:**
- 19 missions flown across Hurricanes Ernesto (4), Francine (4), Helene (7), and Milton (4)
- 17 successful flights (89.5% success rate)
- Longest flight by air-deployed UAS into a storm
- Highest wind measured by UAS
- Max range to P3: 191 miles

**Performance Benchmarking Focus:**
- Data quality and resolution vs. AVAPS dropsondes
- Cost-efficiency analysis
- Wind/turbulence measurement accuracy
- Wave state characterization

## Use Cases & Applications

### Primary (Phase I Focus)
- **Hurricane monitoring:** Real-time atmospheric profiling and boundary-layer observations in extreme wind conditions
- **Navy operations:** Integration with 53rd Weather Reconnaissance Squadron and COAMPS-TC modeling community
- **Targeted deployment:** Automated sampling in high-wind environments with minimal crew overhead

### Anticipated Expansion (Phase II / Commercialization)
- **DoD:** Navy operations integration (primary); Air Force applications (C-130, KC-135, P8)
- **Federal agencies:** 
  - NOAA: Hurricane monitoring, boundary-layer research
  - NASA: Stratospheric balloon gondola deployments (10s of aircraft per gondola), storm tracking
  - USGS/FEMA: Disaster response and environmental monitoring
- **Private sector:**
  - Energy: Offshore platform monitoring
  - Insurance: Real-time risk assessment
  - Wildfire and disaster response operations

### Stratospheric Balloon Integration
- NASA-funded flight opportunities covering operational costs
- Multiple S0 units per gondola for wide-area monitoring
- Capability to track storms and deploy without crewed aircraft
- Applications in wildfire and disaster response

## Deliverables & Schedule

| Deliverable | Due Date |
|-------------|----------|
| Kickoff Briefing | July 22, 2025 |
| Base Period Progress Report | October 6, 2025 |
| Base Period Final Report | January 6, 2026 |

## Anticipated Phase I Results

1. **Validated error budget** for wind, turbulence, and wave sensing
2. **Benchmarked S0 performance** against AVAPS dropsondes and expendable UAS
3. **Demonstrated feasibility** of collecting unique observables (vertical wind, turbulence, wave state) unavailable via legacy systems
4. **Verified S0 suitability** for targeted deployments in high-wind environments
5. Quantitative demonstration of superior data quality, resolution, and cost-effectiveness vs. legacy platforms

## Facilities & Resources

- **Black Swift Technologies Integration Lab (Boulder, CO):** UAS hardware prototyping, sensor integration, real-time processing tools
- **Precipitation/icing test systems:** Custom chamber for simulating sensor exposure under storm conditions
- **Embry-Riddle Wind Tunnel:** Capabilities to be evaluated for Phase II testing
- **NOAA Collaboration:** Access to dropsonde data, evaluation frameworks, atmospheric expertise

## Notable Details

### Competitive Advantages
- Demonstrated operational history: 19 missions in 2024 across four major hurricanes
- Significant performance improvements (wind accuracy: 1–2 m/s → 0.2 m/s; data rate: 3 Hz → 10 Hz)
- Radar-based all-weather wave sensing (vs. laser-only competitors)
- Scalable manufacturing (50 units achievable with minimal effort in 2025)
- Onboard automation reducing operator burden on crewed platforms

### Integration Pathways
- **Near-term:** 53rd Weather Reconnaissance Squadron (Navy P3)
- **Medium-term:** Integration with C-130, KC-135, P8 across DoD
- **Advanced:** Stratospheric balloon gondola deployments via NASA

### Data Products
- Pressure, temperature, humidity (PTH)
- Three-dimensional winds (0.2 m/s accuracy)
- Turbulence metrics
- Sea surface temperature
- Wave height (radar-based, all-weather)
- High-rate onboard-calculated fluxes and spectral products
- Automated data processing on host aircraft

### Unique Value Proposition
S0 delivers "actionable atmospheric and wave observables unavailable via legacy systems" with reduced per-flight cost and risk compared to dropsondes or manned missions, scalable to fleet-level tactical or research deployments.