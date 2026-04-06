# AFX22.4 Phase II Technical Volume - Runway Integrity Validation through Soil Moisture Measurements from a small UAS

## Document Metadata
- **Type:** SBIR Phase II Technical Volume (Proposal)
- **Client/Agency:** U.S. Air Force (AFWERX)
- **Program/Solicitation:** AFX224-OCSO1 Phase II, Open Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions
- **Contract Number:** F2-16588
- **Date:** 2023 (Phase II submission)
- **CAGE Code:** 6PGF9
- **BST Products/Systems Referenced:** S2 (fixed-wing UAS), E2 (multirotor UAS), L-band radiometer (LDCR architecture), soil moisture mapping system
- **Key Personnel:** 
  - Dr. Jack Elston (Founder, CEO, Principal Investigator)
  - Dr. Maciej Stachura (Founder, CTO, Lead Engineer)
  - Michael A. Hurowitz (Orbital Micro Systems, LDCR Sensor Lead)
  - Eryan Dai (Remote Sensing Scientist)

## Executive Summary
Black Swift Technologies proposes to adapt its existing commercial UAS-based L-band radiometer soil moisture mapping system to measure soil integrity (cone index) for evaluating unimproved landing zones for C-130 cargo aircraft operations. The system will provide forward air controllers with rapid, high-resolution soil integrity maps covering 3,000' x 60' runway areas in ~10 minutes, replacing time-consuming manual cone penetrometer measurements that require ground personnel in potentially contested areas.

## Technical Approach

### Core Technology Foundation
- **Existing System:** UAS-based L-band radiometer developed through NASA SBIR partnership with Orbital Micro Systems (OMS) and Center for Environmental Technology (CET) at University of Colorado
- **Measurement Principle:** L-band radiometer operates at 1400-1427 MHz (Earth Exploration Satellite Service protected band) using proprietary Lobe Differencing Correlation Radiometer (LDCR) architecture
- **LDCR Architecture:** Compares signals from two reference signals and two antennas (one looking up, one looking down) for stable calibration and accurate brightness temperature measurement (1.2K accuracy required)
- **Soil Penetration:** Measures volumetric soil moisture within 10cm of surface; can be extended to lower frequency bands for deeper penetration if needed
- **Pixel Resolution:** Approximately equal to aircraft flight altitude; can be enhanced further with post-processing

### Phase II Modifications
1. **L-band Radiometer Improvements:**
   - Modifications to PCB design with enhanced electromagnetic interference (EMI) shielding and isolation hardware
   - Implementation of proprietary digital radiometer detection technique for enhanced interference detection/mitigation
   - Improved calibration stability and measurement accuracy
   - Rapid real-time processing software for data visualization on UAS or ground station

2. **UAS Platform Modifications (E2 multirotor base):**
   - Integration of thermal sensors for surface temperature measurement
   - Addition of NDVI (Normalized Difference Vegetation Index) sensors
   - New data logger hardware for sensor integration
   - 3D CAD design and wiring interfaces for updated radiometer, datalogger, and auxiliary sensors

3. **Soil Integrity Algorithm Development:**
   - Algorithm to compute cone index from L-band soil moisture measurement and soil type
   - Real-time computation code for rapid post-mission data processing
   - Validation against ground-truth cone penetrometer measurements

## Products & Capabilities Described

### L-Band Radiometer (LDCR)
- **Current Status:** TRL 8 (fully mature for soil moisture mapping)
- **Specifications:** 1400-1427 MHz, 1.2K brightness temperature accuracy, ~15m resolution at typical flight altitudes
- **Capability:** Measures volumetric soil moisture within 10cm of surface
- **Previous Sales:** Sold to University of Virginia and CIRES at University of Colorado Boulder; $700K combined revenue from sales and services (USGS, NOAA, Turfscout data services)
- **Phase II Target:** Upgrade to TRL 7 for soil integrity measurement capability

### E2 Multirotor UAS
- **Role:** Primary platform for modified soil integrity mapping system
- **Characteristics:** Fully American-made, FAA/NASA/NOAA approved for non-defense commercial operations
- **Payloads:** Designed to carry updated L-band radiometer plus thermal and NDVI sensors
- **Versatility:** Can operate on both fixed-wing (S2) and multirotor (E2) depending on mission requirements

### Soil Moisture Mapping System (Commercial Predecessor)
- **Status:** Currently available commercial product
- **Applications:** NASA soil calibration/validation (SMAP satellite), USGS wildfire-prone area mapping (California), NOAA SPLASH project (precipitation/atmosphere/hydrometeorology), Toro smart irrigation systems (golf courses)
- **Coverage Rate:** Up to 600 acres per flight
- **Market Traction:** $700K in combined revenue from two systems sold and data services provided

## Use Cases & Applications

### Primary Use Case: C-130 Runway Operations
- **Mission:** Rapidly assess unimproved landing zones for C-130 cargo aircraft operations
- **Coverage:** 3,000' x 60' runway area in approximately 10 minutes
- **Benefit:** Full runway mapping vs. point measurements from manual cone penetrometer
- **Impact Scope:** 160+ air operation facilities, 9,000 worldwide AO personnel, 7.3 million annual aircraft operations
- **Customer:** Air Mobility Command (AMC), Air Force Life Cycle Management Center (AFLCMC)
- **Transition Path:** Air Force Civil Engineer Center's Airfield Pavement Evaluation team at Tyndall AFB, FL

### Secondary Defense Applications
- **Army Ground Mobility:** Assess soil conditions for heavy vehicle trafficking
- **Trafficability Assessments:** Evaluate terrain for vehicle movement
- **Dam Monitoring:** Monitor stability/saturation of earthen dams

### Commercial Applications
- **Construction Industry:** Soil integrity assessment for project planning
- **Mining:** Understanding soil saturation and integrity around mining operations (Caterpillar interest noted)
- **Railways:** Soil integrity measurements around rail infrastructure (Network Rail UK contacted)
- **Agriculture:** Precision irrigation and drainage management

## Key Results & Previous Validation

### Development History
- Over 15 years of L-band sensor design and evolution
- 8 years of flight testing across multiple field campaigns
- 18 successful SBIR projects (3 transitioned to Phase III)

### Proven Applications
- Wildfire monitoring: NOAA nighttime fire observation experiments (NightFOX)
- Volcano monitoring: NASA-featured routine hazard monitoring
- Tornado/hurricane tracking: First-ever intercept of tornadic thunderstorm (VORTEX2 project)
- High-altitude research: Greenland atmospheric studies at near -20°C, 14,000 ft

### Soil Moisture System Commercial Traction
- 2 systems sold to research institutions
- Ongoing contracts: NOAA (3 field campaigns, mountain valley soil moisture during snowmelt), USGS (wildfire mitigation research)
- Service revenue: $700K from predecessors
- Estimated Year 1 market potential: $3.8M in services (identified pilot customers)

## Phase II Technical Objectives & Deliverables

| Objective | Key Deliverables | Timeline |
|-----------|------------------|----------|
| 1. Modify L-band Radiometer | PCB redesign, RFI mitigation, lab testing, flight validation | Months 2-6 |
| 2. UAS Modifications | Thermal/NDVI sensor integration, mechanical housing updates, prototype build | Months 4-8 |
| 3. Soil Integrity Algorithm | Cone index computation code, real-time processing capability | Months 6-12 |
| 4. Local Field Testing | 4+ test flights across moisture levels (5-40% VWC), 3 soil types, 3 vegetation covers | Months 12-14 |
| 5. Model Refinement | Accuracy validation vs. cone penetrometer, algorithm refinement | Months 14-17 |
| 6. Tyndall AFB Validation Campaign | Flight testing at operational air base, quantitative system assessment | Months 17-18 |
| 7. Final Reporting | Comprehensive results and recommendations | Month 21 |

### Milestone Payments (Total: $1,049,725)
- Kickoff & AF Requirements: $100,000
- Sensing System Modifications: $200,000
- UAS Modifications: $200,000
- Algorithm Development: $200,000
- Local Field Testing: $100,000
- Model Refinement: $200,000
- Tyndall AFB Testing: $150,000
- Additional Reporting: $99,725

## Notable Details

### Technical Risks & Mitigation
1. **RF Interference:** Radiometers operating in predefined bands are susceptible to both inadvertent interference and jamming. Mitigation: Implement proprietary digital radiometer detection technique for enhanced interference detection/mitigation; potential shift to lower frequency bands.
2. **Soil Penetration Depth:** L-band penetration (10cm) may be insufficient for C-130 landing weight assessments. Mitigation: Lower frequency operation capability can improve soil penetration depth.

### Competitive Advantages
- **Unique Technology:** LDCR architecture has received patent office action finding all claims unique in sensor design and retrieval algorithm
- **U.S.-Based Production:** All systems fully American-made, enabling direct government sales
- **Proven Track Record:** 15+ years sensor development, 8 years flight testing, multiple government partnerships (NASA, NOAA, USGS)
- **Dual-Use Technology:** Strong commercial market potential (mining, construction, railways, agriculture) ensures sustainability beyond DoD funding
- **Speed & Coverage:** 10-minute full runway mapping vs. time-consuming point measurements from manual methods

### Market Potential
- **Global UAS Market:** $20.71B (2018) → $52.30B (2025), CAGR 14.15%
- **Military UAS Procurement:** Significant growth driver; U.S. military projected $18B drone spending over next decade
- **sUAS Specific Market:** Projected $43.1B by 2024
- **Identified Commercial Customers:** RES Group, Caterpillar, Network Rail UK, Toro (golf courses)
- **Estimated Pilot Market Revenue:** $3.8M first year from identified customers alone

### Key Personnel & Expertise
- **Dr. Jack Elston:** 15+ years UAS experience; VORTEX2 tornado intercept; 300+ flight experiments; expertise in avionics, autopilot systems, cooperative UAS control
- **Dr. Maciej Stachura:** 300+ flight experiments; NASA AFSRB/FRB process leadership; Phase I/II NASA SBIR soil moisture PI
- **Michael A. Hurowitz (OMS):** Electronics, RF, semiconductor/optical device development, SBIR/STTR expertise; NOAA-CU CET member
- **Eryan Dai:** Developed core LDCR calibration and soil moisture retrieval algorithms during PhD at CU Boulder

### Commercial Viability
- **Non-Defense Revenue (last 12 months):** ~$750,000
- **Profitability:** Company profitable since 2016, bootstrapped from founders only
- **Equity Strategy:** Planning capital raise; multiple investor expressions of interest (One Colorado Fund, Regolith Ventures)
- **Acceleration Support:** Capital Factory member (Austin, TX); access to startup mentors and government procurement experts
- **Phase III Strategy:** AFWERX TACFI/STRATFI programs targeting $350K-$15M matching SBIR dollars; potential for air-deployable variant from C-130

### Government Stakeholder Engagement
- **AFRL Contacts:** Paul Fleitz (DR-IV, ALOBO Team Lead), Kyle Egbert (Capt, Pavements Instructor), Collin Gwaltney (1st Lt), Jason Foley (DR-IV, RXEB)
- **Test Locations:** BST's local Longmont, CO facility + Tyndall AFB
- **Customer Requirements Integration:** Team working with AFRL and Civil Engineer School at Air Force Institute of Technology

### Manufacturing & Support
- All BST UAS fully American-made
- Can customize training/reporting interfaces per customer type (DoD, non-defense government