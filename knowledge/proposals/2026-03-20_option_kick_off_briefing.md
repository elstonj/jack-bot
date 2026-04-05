# Phase I Option Period Kick-Off Briefing: Expendable Air-sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- Type: Program kick-off briefing (SBIR/STTR)
- Client/Agency: Department of the Navy (Naval Surface Warfare Center, Carderock Division)
- Program/Solicitation: N25A-T025; Navy STTR
- Contract Number: N68335-25-C-0270
- Date: March 20, 2026 (kick-off meeting); document created March 10, 2026
- BST Products/Systems Referenced: S0 (expendable UAS)
- Key Personnel: Dr. Jack Elston (PI), Dr. Maciej Stachura (Co-I), Joshua Cossuth (Navy POC)

## Executive Summary
Black Swift Technologies' Phase I Option focuses on demonstrating the S0 expendable UAS as a superior, cost-effective alternative to legacy atmospheric and wave-sensing platforms (dropsondes, manned aircraft) for Navy hazardous weather operations. The effort will validate S0 data quality against established benchmarks, characterize error sources, demonstrate unique observables (vertical wind, turbulence, wave state), and assess operational feasibility for targeted high-wind sampling in Navy contexts.

## Technical Approach

### Phase I Option Objectives & Approach

**Objective 1: Data Quality & Cost Benchmarking**
- Compare S0 data quality, resolution, and cost against AVAPS (Vaisala dropsonde) and Coyote (expendable UAS) systems
- Baseline against recent hurricane deployments and theoretical sensor limits
- Assess accuracy, resolution, and cost-efficiency

**Objective 2: Error Source Identification**
- Perform wind tunnel tests and error analysis
- Assess GNSS/IMU performance and response times
- Quantify dominant error sources in wind and wave sensing

**Objective 3: Unique Observable Validation**
- Validate high-rate products (vertical wind, turbulence)
- Test radar-based wave sensing in cloud/precipitation conditions
- Demonstrate capabilities unavailable from legacy systems

**Objective 4: High-Wind Operational Feasibility**
- Review S0 hurricane deployments from 2025
- Evaluate control authority, launch compatibility, and Navy data requirements
- Assess suitability for targeted sampling in high-wind environments

### Phase II Work Plan (Proposed)

**Cal/Val (Phase II Cal/Val Plan)**
- Wind tunnel testing, field deployments, comparative studies with dropsondes
- Refine algorithms for vertical velocity and turbulence estimation

**Wave Measurement Development**
- Investigate radar-based wave sensing alternatives to laser altimetry
- Design systems capable of measurements at ground speeds exceeding 200 mph
- Characterize wave shape, frequency, and height

**S0 Operation in Icing**
- Identify icing impacts on motor, hot-point probe (MHP), wings, propellers
- Explore passive (hydrophobic coatings) and active (localized heating) de-icing solutions

**Stakeholder Engagement & Integration Planning**
- Engage Navy stakeholders to define launch platform preferences
- Identify communication and data delivery system requirements
- Plan integration with Navy operational workflows

## Products & Capabilities Described

### S0 Expendable UAS
- **What it is**: Expendable (expended in-situ) small UAS designed for deployment into hurricanes and hazardous weather
- **Key capabilities**:
  - Automated, sensor-directed flight in hurricanes with minimal operator overhead
  - Long-range communications for real-time data transmission
  - Flush-air sensing nose cone for high-rate 3D wind measurement
  - In-situ atmospheric probe: pressure, temperature, humidity
  - Surface temperature and wave height measurement
  - Air deployment from P3, C-130, KC-135, P8 platforms

- **2025 Performance Summary**:
  - 21 launches into storms in 2025
  - 12 launches into Hurricane Melissa during government shutdown
  - Record 120-minute flight duration into Melissa
  - Successfully provided 500m eyewall circumnavigation data ingested by National Hurricane Center (NHC)
  - S0 data integrated into NOAA's production WCOSS system (live as of early June 2025)

- **Specifications & Claims**:
  - Superior spatial/temporal resolution compared to dropsondes
  - Cost-effective per-flight alternative to manned missions
  - Scalable fleet capability for tactical or research deployment
  - Real-time data products available via hdob.bst.aero

## Use Cases & Applications

### Primary (Phase I Focus)
- **Navy Hazardous Weather Operations**: Integration with Naval Surface Warfare Center operations; support for COAMPS-TC (Coupled Atmosphere-Ocean Prediction System for Tropical Cyclones) modeling
- **Hurricane Monitoring & Eyewall Sampling**: Demonstrated in Hurricane Melissa (2025); targeted high-wind profiling
- **Ocean-Atmosphere Boundary Layer Observations**: High-resolution wind, turbulence, and wave state characterization

### Secondary (Anticipated Commercialization)
- **DoD Integration**: Initial focus on Navy operations; potential expansion to Air Force (53rd Weather Reconnaissance Squadron integration with C-130, KC-135, P8)
- **NOAA Operations**: Expansion from hurricane research into routine boundary-layer and wave monitoring
- **NASA Missions**: Stratospheric balloon gondola deployment for storm tracking and other applications (wildfire, disaster response)
- **Federal Agencies**: USGS and FEMA for disaster response and environmental monitoring
- **Private Sector**: Offshore platform monitoring, real-time insurance risk assessment, energy sector applications

### Proposed Platform Integration
- **Launch platforms**: P3, P8, C-130, KC-135, sonobuoy launchers
- **Magnetic anomaly detection** (P8)
- **Drop site condition assessment** (C-130)
- **Magnetic mapping** (KC-135)

## Anticipated Results

By end of Phase I Option, BST anticipates:
1. **Validated error budget** for wind, turbulence, and wave sensing
2. **Quantitative performance benchmarks** against dropsondes and legacy expendable UAS
3. **Demonstrated feasibility** of collecting unique observables (vertical wind, turbulence, wave state) in operational conditions
4. **Verified operational suitability** for targeted deployments in high-wind Navy environments
5. **Defined integration pathway** for mechanical, electrical, and software interfaces with Navy launch platforms

## Notable Details

### Collaborative Resources
- **NOAA/AOML Partnership**: Access to dropsonde data, validation frameworks, atmospheric expertise; advisors include Dr. Jun Zhang
- **Academic Advisors**: Dr. Josh Wadler (Embry-Riddle), Dr. John Park (Old Dominion)—domain expertise in boundary layer physics, UAS validation, wave-atmosphere coupling
- **Wind Tunnel Access**: Embry-Riddle facility available for Phase II testing (not used in Phase I)
- **BST Integration Lab** (Boulder, CO): UAS prototyping, sensor integration, real-time processing; precipitation/icing test chambers

### Key Achievements & Momentum
- Third year of S0 hurricane deployments
- **First NOAA Corps officer** to pilot UAS into hurricane conditions (2025)
- S0 data now flowing to **National Hurricane Center** in real-time (confirmed for production WCOSS by early June 2025)
- Competitive advantage: Only expendable UAS system demonstrated in operational hurricane environment with production data integration

### Identified Technical Challenges & Mitigations
| Challenge | Mitigation |
|-----------|-----------|
| Altitude estimation without RTK in remote ocean | Dual-sensor fusion (GNSS + barometric) with dynamic correction |
| Sensor icing in high-moisture/cold air | Passive (hydrophobic) and active (localized heating) de-icing |
| Wave sensing under clouds/precipitation | Radar-based alternatives to laser altimetry; high-wind validation |
| Data volume vs. downlink bandwidth | Onboard summary metrics (spectra, fluxes) and compression algorithms |

### Deliverables Schedule
- Kick-off Briefing: March 23, 2026
- Base Period Progress Report: TBD
- Base Period Final Report: TBD
- Phase II Cal/Val Plan execution: 6-month option period timeline

### Personnel Qualifications
- **Dr. Jack Elston (PI)**: PhD Aerospace Engineering, 15+ years UAS development, led NOAA/NASA/DoD hurricane and extreme-environment deployments
- **Dr. Maciej Stachura (Co-I)**: PhD Aerospace Engineering, sensor fusion expert, architect of S0 onboard sensor processing and system validation

### Data Products & Integration
- Real-time atmospheric profiles (wind, temperature, humidity, pressure)
- Wave height and state characterization
- Surface temperature measurements
- High-rate vertical wind and turbulence products
- Dashboard: hdob.bst.aero (real-time data portal)
- Integration target: Navy COAMPS-TC modeling community