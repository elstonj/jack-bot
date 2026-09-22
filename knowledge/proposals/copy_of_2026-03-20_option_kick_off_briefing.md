# 2026-03-20 Option Kick Off Briefing: Expendable Air-sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- Type: SBIR Phase I Option Period Kick-off Briefing
- Client/Agency: Department of the Navy (SYSCOM)
- Program/Solicitation: Navy SBIR/STTR Topic N25A-T025
- Contract Number: N68335-25-C-0270
- Date: March 20, 2026 (Kick-off); Briefing created/modified September 14, 2026
- BST Products/Systems Referenced: S0 (expendable UAS platform)
- Key Personnel: Dr. Jack Elston (PI), Dr. Maciej Stachura (Co-I), Maciej Stachura (last editor)
- POC: Joshua Cossuth, Arlington, VA (703) 696-0703

## Executive Summary
Black Swift Technologies is entering the Phase I Option period of a Navy SBIR/STTR contract to demonstrate the S0 expendable UAS platform's capability for air-sea profiling in hazardous weather conditions. The program aims to validate S0's superior performance, cost-efficiency, and unique observables (vertical wind, turbulence, wave state) compared to legacy systems like AVAPS dropsondes and Coyote UAS, with focus on Navy operational integration and hurricane monitoring.

## Technical Approach

### Phase I Option Objectives & Approach:

**Objective 1: Data Quality & Cost Benchmarking**
- Compare S0 data quality, resolution, and cost against AVAPS and Coyote systems using recent hurricane data
- Assess accuracy, resolution, and cost-efficiency
- Explore S0 measurement potential through sensor tolerances, thresholds, and relaxation times

**Objective 2: Error Source Identification**
- Perform wind tunnel tests and error analysis
- Assess GNSS/IMU performance and response times
- Identify dominant error sources in wind and wave sensing

**Objective 3: Unique Observables Demonstration**
- Validate high-rate products (vertical wind, turbulence)
- Test radar-based wave sensing in clouds
- Demonstrate capabilities unavailable from legacy platforms

**Objective 4: High-Wind Operational Feasibility**
- Review S0 hurricane deployments from 2025 operations
- Evaluate control authority, launch compatibility
- Assess alignment with Navy data needs

### Phase II Work Plan (Proposed):

**Cal/Val Plan (O.1)**
- Calibration and validation activities including wind tunnel testing and field deployments
- Comparative studies against legacy systems
- Refine algorithms for vertical velocity and turbulence estimation

**Wave Measurement Development (O.2)**
- Investigate alternative wave state measurement methods (radar systems preferred over laser altimetry)
- Design systems capable of rapid measurements at ground speeds exceeding 200 mph
- Characterize wave shape, frequency, height under cloud and precipitation

**Icing Operation (O.3)**
- Identify icing issues affecting the S0's micro-helicopter pusher (MHP), wings, propellers
- Explore passive (hydrophobic coatings) and active de-icing solutions (localized heating)

**Stakeholder Engagement & Integration Planning (O.4)**
- Engage Navy (DoW) stakeholders for integration requirements
- Identify preferred launch platforms, communication systems, data delivery systems
- Plan for mechanical, electrical, and software interfaces

## Products & Capabilities Described

### S0 Expendable UAS Platform
**What it is:** Expendable (expendable but recoverable) autonomous aircraft designed for harsh environment sampling, particularly hurricane and hazardous weather operations.

**Key Capabilities:**
- Launches into hurricanes and extreme weather
- Automated, sensor-directed flight in storms with minimal operator overhead
- Long-range communications capability
- High-rate three-dimensional wind measurement
- Surface temperature sensing
- Wave height measurement
- In situ atmospheric probe (pressure, temperature, humidity)
- Flush-air sensing nose cone for accurate measurements
- GNSS/IMU sensor fusion for altitude and navigation
- Real-time data downlink capability

**2025 Performance Summary:**
- 3rd year of storm operations
- 21 launches into storms in 2025
- 12 launches into Hurricane Melissa during government shutdown
- Record 120-minute flight duration during Melissa operations
- Data ingested by National Hurricane Center (NHC)
- Demonstrated 500m eyewall circumnavigation with high-resolution data
- S0 data transitioned to "live" production status on WCOSS (Weather and Climate Operational Supercomputing System) in June 2026

**Comparison to Legacy Systems:**
- Superior to AVAPS dropsondes in terms of reusability, cost, and data resolution
- Provides unique observables (vertical wind, turbulence, wave state) unavailable from traditional systems
- Higher spatial and temporal resolution than expendable UAS like Coyote
- Reduced per-flight cost and risk vs. dropsondes or manned missions

**Technical Challenges & Mitigations:**
- *Altitude estimation without RTK:* Dual-sensor fusion (GNSS + barometric pressure) with dynamic correction models
- *Sensor icing:* Passive (hydrophobic coatings) and active (localized heating) solutions
- *Wave sensing in cloud/precipitation:* Radar-based alternatives to laser altimetry
- *Data volume vs. bandwidth:* Onboard summary metrics (spectra, fluxes) and compression algorithms

## Use Cases & Applications

### Primary Use Cases (Phase I):
- **Hurricane monitoring and eyewall characterization:** Demonstrated with Hurricane Melissa (2025); provides real-time observations to NHC
- **Boundary-layer atmospheric profiling:** High-resolution wind, temperature, humidity, pressure measurements
- **Wave state observation:** Characterizing air-sea interaction and wave dynamics in hazardous conditions
- **Tactical weather support:** Minimal operator overhead for deployment from crewed platforms (P-3 hurricane hunters, etc.)

### Anticipated Customers & Markets:

**DoD (Primary):**
- Navy weather and operations teams
- Integration with 53rd Weather Reconnaissance Squadron
- Proposed integration with C-130, KC-135, P-8 platforms
- COAMPS-TC (Coupled Ocean/Atmosphere Mesoscale Prediction System for Tropical Cyclones) modeling community

**Federal Agencies:**
- NOAA: Hurricane monitoring, boundary-layer observations
- NASA: Atmospheric research, flight opportunities via stratospheric balloons
- USGS: Environmental monitoring
- FEMA: Disaster response

**Private Sector:**
- Energy sector: Offshore platform monitoring
- Insurance industry: Real-time risk assessment
- Wildfire monitoring and response
- Disaster response operations

### Stratospheric Balloon Applications (Future):
- Deploy 10+ UAS per balloon gondola
- Track storms without crewed aircraft
- Wildfire monitoring
- Disaster response
- Magnetic mapping (with KC-135)
- Magnetic anomaly detection (with P-8)

## Key Results (from 2025 Operations)

### Performance Metrics:
- **Flight Endurance:** Record 120-minute mission during Hurricane Melissa
- **Operational Success Rate:** 21 successful storm deployments in 2025
- **Data Quality:** Hurricane Melissa eyewall data compared favorably to manned WP-3D observations
- **Data Integration:** Real-time data products transitioned to operational status on NOAA WCOSS system
- **NHC Integration:** 500m-resolution eyewall circumnavigation data ingested for operational evaluation

### Organizational Achievements:
- S0 program fully integrated with NOAA UASD (Unmanned Aircraft Systems Division)
- First NOAA Corps officer qualified to fly UAS in hurricane conditions
- Demonstrated critical operational role justifying continued fleet operations

## Notable Details

### Personnel Qualifications:
- **Dr. Jack Elston (PI):** PhD Aerospace Engineering; 15+ years UAS development; led NOAA, NASA, and DoD-funded UAS deployments into hurricanes and extreme environments
- **Dr. Maciej Stachura (Co-I):** PhD Aerospace Engineering; expert in sensor fusion and UAS calibration; architect of S0 onboard sensor processing and system validation

### Academic/Research Collaborators:
- Dr. Jun Zhang (NOAA/AOML): Boundary layer physics
- Dr. Josh Wadler (Embry-Riddle): UAS validation
- Dr. John Park (Old Dominion): Wave-atmosphere coupling

### Facilities & Equipment:
- Black Swift Technologies Integration Lab (Boulder, CO): UAS hardware prototyping, sensor integration, real-time processing
- Precipitation/icing test systems: Custom chamber for storm condition simulation
- Embry-Riddle Wind Tunnel: Planned for Phase II testing
- NOAA Collaboration: Access to dropsonde data, evaluation frameworks, atmospheric expertise

### Integration Timeline & Platforms:
- Phase II focus: Full Navy operational integration and real-time use demonstration
- Proposed launch platforms: C-130, KC-135, P-8 (via 53rd Weather Reconnaissance Squadron)
- Data products will provide actionable atmospheric and wave observables unavailable via legacy systems
- Continuous stakeholder feedback loop planned for adoption and relevance

### Risk Mitigation Emphasis:
Document explicitly addresses 2026-2027 challenges with clear mitigation strategies for altitude estimation in remote ocean environments, sensor icing, wave sensing limitations, and data downlink constraints—indicating maturity in understanding operational deployment challenges.