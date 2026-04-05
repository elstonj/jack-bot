# Phase I Option Period Kick-Off Briefing: Expendable Air-sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- Type: Kick-off briefing / program review
- Client/Agency: Department of the Navy (DoN), SBIR/STTR Program
- Program/Solicitation: N25A-T025 (Navy STTR); Contract No. N6833525C0270
- Date: March 20, 2026 (kick-off); deliverable due March 23, 2026
- BST Products/Systems Referenced: S0 (expendable UAS)
- Key Personnel: Dr. Jack Elston (PI), Dr. Maciej Stachura (Co-I); Advisors: Dr. Jun Zhang (NOAA/AOML), Dr. Josh Wadler (Embry-Riddle), Dr. John Park (Old Dominion); Meredith Needham (last editor); Joshua Cossuth (Navy POC)

## Executive Summary
This Phase I Option briefing outlines BST's plan to advance the S0 expendable UAS platform for Navy operations in hazardous weather, specifically hurricane monitoring and air-sea profiling. The work focuses on validating S0's superior data quality and cost-effectiveness compared to legacy systems (AVAPS, Coyote dropsondes), identifying sensor error sources, demonstrating unique observables (vertical wind, turbulence, wave state), and assessing feasibility for targeted high-wind deployments. The platform will be integrated with Navy platforms including P8, C-130, and KC-135 aircraft.

## Technical Approach

### Phase I Option Objectives & Approach

**Objective 1: Compare S0 data quality, resolution, and cost with legacy platforms**
- Benchmark against AVAPS and Coyote systems
- Assess accuracy, resolution, and cost-efficiency
- Explore S0 measurement potential through sensor tolerances, thresholds, and relaxation time analysis

**Objective 2: Identify dominant error sources in wind and wave sensing**
- Perform wind tunnel tests and error analysis
- Assess GNSS/IMU performance and response times
- Develop validated error budget

**Objective 3: Demonstrate unique observables**
- Validate high-rate products (vertical velocity, turbulence)
- Test radar-based wave sensing in clouds and precipitation

**Objective 4: Assess feasibility of targeted sampling in high-wind conditions**
- Review S0 hurricane deployments
- Evaluate control, launch compatibility, and Navy data needs

### Phase II Work Plan (Proposed)

**Cal/Val Plan:**
- Wind tunnel testing and field deployments
- Comparative studies with legacy systems
- Algorithm refinement for vertical velocity and turbulence estimation

**Wave Measurement Development:**
- Investigate alternative wave sensing methods (radar-based systems)
- Develop systems capable of >200 mph ground speeds for adequate spatial/temporal coverage

**Operation in Icing:**
- Identify icing issues affecting Magnetic Heading Processor (MHP), wings, propellers
- Design de-ice heaters and explore passive/active de-icing solutions

**Stakeholder Engagement and Integration Planning:**
- Conduct DoN stakeholder interviews
- Define preferred launch platforms, communication systems, data delivery systems

## Products & Capabilities Described

### S0 (Expendable UAS)
**What it is:** Small, expendable unmanned aircraft system designed for atmospheric profiling in extreme weather conditions

**Key Specifications & Performance Claims:**
- Flight duration: 120+ minutes (record demonstrated in Hurricane Melissa)
- Can be deployed from air-launch platforms (P3, C-130, KC-135, P8)
- Ground speeds exceeding 200 mph achievable
- High-rate (3D) wind measurements via flush-air sensing nose cone
- Integrated atmospheric probe: pressure, temperature, humidity
- Surface temperature measurement
- Wave height measurement
- Sensor fusion onboard (GNSS + IMU + barometric pressure)
- Real-time data transmission capability

**Sensor Suite:**
- Flush-air sensing nose cone (high-rate 3D winds)
- In situ atmospheric probe
- GNSS receiver
- Barometric pressure sensor
- IMU
- Radar-based wave sensing (under development)
- Potential de-ice heaters (design phase)

**Data Products:**
- High-resolution atmospheric and wave measurements
- Vertical wind and turbulence estimates
- Wave state characterization (shape, frequency, height)
- Summary metrics (spectra, fluxes)

## Use Cases & Applications

### Primary (Navy)
- **Hurricane monitoring and reconnaissance:** 21 S0s launched into storms in 2025; 12 launched into Hurricane Melissa during government shutdown
- **Eyewall sampling:** 500m eyewall circumnavigation data collected during Hurricane Melissa, evaluated by National Hurricane Center (NHC)
- **COAMPS-TC modeling support:** Provide observables for improved ocean-atmosphere coupling in tactical weather prediction
- **Ocean-atmosphere profiling in high-sea-state conditions**

### Planned Integration Platforms
- P3 hurricane hunter (primary current platform; currently has minimal operator overhead)
- P8 Poseidon (magnetic anomaly detection application)
- C-130 Hercules (drop site conditions assessment)
- KC-135 Stratotanker (magnetic mapping)
- 53rd Weather Reconnaissance Squadron operational aircraft

### Secondary (Expansion Markets)
- **NOAA:** Hurricane monitoring, boundary-layer observations
- **NASA:** Stratospheric balloon deployment (10's of S0s per gondola); storm tracking without crewed aircraft
- **USGS/FEMA:** Disaster response and environmental monitoring
- **Commercial energy sector:** Offshore platform monitoring
- **Insurance industry:** Real-time risk assessment
- **Wildfire monitoring and response**

## Key Results & 2025 Achievements

**Operational Track Record:**
- 3rd year of operational S0 deployments into storms
- 21 S0s launched into storms in 2025
- 12 launches into Hurricane Melissa (Dec 2024, during government shutdown)
- Record-setting 120-minute flight duration achieved (Hurricane Melissa)
- First NOAA Corps officer to fly UAS in hurricane conditions

**Data Integration:**
- S0 data ingested into National Hurricane Center operations
- NHC used S0-collected eyewall data for evaluation and comparison to TDR (Total Delta-Height Reduction) measurements
- Real-time data transmission ("HDOBS") operational; "went live"
- Data production integration planned for early June (WCOSS system)
- Real-time display available at hdob.bst.aero

**Program Maturation:**
- Fully integrated into NOAA's Unmanned Aircraft Systems Division (UASD) program
- Proven critical role for S0 operations validated by NOAA/Navy stakeholders

## Notable Details

### Error Mitigation & Risk Management

**Challenges & Proposed Mitigations:**
1. **Altitude estimation without RTK in remote ocean:** Dual-sensor fusion (GNSS + barometric pressure) with dynamic correction models
2. **Sensor icing in high-moisture/cold air:** Passive hydrophobic coatings + active localized heating (heater design underway)
3. **Wave sensing limitations under clouds/precipitation:** Radar-based alternatives to laser altimetry; validation in high-wind scenarios
4. **Data volume vs. downlink bandwidth:** Onboard summary metrics (spectra, fluxes) and compression algorithms

### Facilities & Resources
- **Black Swift Technologies Integration Lab (Boulder, CO):** UAS hardware prototyping, sensor integration, real-time processing
- **Precipitation/icing test chamber:** Custom simulator for storm condition exposure
- **NOAA Collaboration:** Access to dropsonde data, evaluation frameworks, atmospheric expertise
- **Embry-Riddle Wind Tunnel:** Planned for Phase II testing (not used in Phase I)

### Transition & Commercialization Strategy

**Near-term (DoD):**
- Navy weather and operations teams (primary)
- Integration with 53rd Weather Reconnaissance Squadron
- Sonobuoy launcher platform compatibility

**Mid-term (Federal):**
- NOAA (hurricane monitoring)
- NASA (stratospheric balloon deployments)
- USGS and FEMA (disaster response)

**Long-term (Commercial):**
- Energy sector (offshore platform monitoring)
- Insurance (real-time risk assessment)
- Other applications (wildfire, disaster response)

### Competitive Advantages
- Cost-effective vs. dropsondes and manned missions
- Scalable fleet deployment capability
- Unique observables unavailable from legacy systems (vertical wind, turbulence, radar-based wave state)
- Real-time data delivery and integration
- Demonstrated operational success in extreme weather

### Notable Data Points
- **Cost advantage:** Significantly reduced per-flight cost vs. dropsondes or manned missions
- **Performance comparison:** S0 eyewall circumnavigation data comparable/superior to TDR measurements
- **Data resolution:** 500m eyewall sampling resolution demonstrated
- **Operational efficiency:** Minimal operator overhead for crew on P3 hurricane hunter aircraft

---

**Document Classification:** CUI (Controlled Unclassified Information); SBIR Data Rights; Distribution authorized to U.S. Government agencies only