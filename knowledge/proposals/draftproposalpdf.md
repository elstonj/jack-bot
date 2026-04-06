# On-demand Wildfire Susceptibility from Fuel Moisture and Vegetative Index Maps

## Document Metadata
- **Type:** NASA ROSES Proposal (Step 2 Draft)
- **Client/Agency:** NASA Headquarters, Science Mission Directorate, Earth Science
- **Program/Solicitation:** NASA ROSES A.59 Technology Development for Support of Wildland Fire Science, Management, and Disaster Mitigation (NNH23ZDA001N-FIRET)
- **Date:** March 29, 2024
- **BST Products/Systems Referenced:** L-band soil moisture measuring UAS (fixed-wing and multirotor platforms); soil moisture radiometer; onboard data processing systems
- **Key Personnel:** 
  - Jack Elston (PI, BST)
  - Maciej Stachura (Co-I, BST)
  - Eryan Dai (Co-I, Orbital Micro Systems Inc)
  - Ryan Ferrell (Co-I, Pepperwood Foundation)
  - Seung-bum Kim (Co-I, JPL/NASA)
  - Michelle Stern (Co-I/Science PI, USGS Sacramento)

## Executive Summary
Black Swift Technologies proposes to operationalize on-demand fuel moisture mapping for wildfire management by developing a coordinated swarm of up to 8 soil moisture measuring UAS capable of mapping over 3,000 acres in a single day. Building on preliminary work (2021-2023) demonstrating strong correlations between soil moisture and live fuel moisture at Pepperwood Preserve in California, the project will achieve operational status through sensor miniaturization, onboard computing, multi-UAS coordination, and integration with NASA's UAVSAR and NISAR satellite data. The three-year effort (Oct 2024–Sept 2027) targets TRL advancement from 3 to 6 with a total budget of $2,118,190.75.

## Technical Approach

### Primary Technology Developments
1. **L-Band Radiometer Soil Moisture Sensing:** Miniaturized L-band radiometer payload originally developed under NASA SBIR program; will be refined for both fixed-wing and multirotor UAS platforms. Current payload specifications: 1.5 kg for multirotor, 2.2 kg for fixed-wing, <50W power draw.

2. **Onboard Data Processing:** Development of updated digital correlator with FPGA implementation to enable:
   - Real-time coherence matrix calculation
   - Improved gain fluctuation immunity
   - Self-calibration capability
   - Conversion of brightness temperature to soil moisture onboard the aircraft
   - Near real-time live fuel moisture product generation

3. **Multi-UAS Coordination & Autonomy:**
   - Single operator control of up to 8 UAS simultaneously
   - Automated mapping flight planning based on terrain
   - Active terrain tracking and obstacle avoidance using machine learning and AI
   - Sensor-reactive control for dynamic re-tasking during flight
   - Automated pre-flight checks and sensor setup

4. **Data Fusion & Intelligence Tasking:**
   - Integration of NASA P-band UAVSAR (Year 1 testing) and L-band NISAR satellite data
   - Root-zone soil moisture retrieval algorithms adapted from SMAP SAR observations
   - Lookup table-based forward modeling with three axes (dielectric constant/soil moisture, surface roughness, vegetation water content)
   - Automatic tasking of UAS swarm to highest-risk areas identified by satellite/airborne data
   - Cross-platform soil moisture comparison (UAS, UAVSAR, NISAR)

5. **Live Fuel Moisture Conversion:**
   - Empirically derived relationships between soil moisture and LFM established from previous pilot study (strong correlation demonstrated at Pepperwood)
   - Plant-type specific algorithms for onboard conversion
   - Validation against legacy sensors and existing algorithms

### Field Validation Site
**Pepperwood Preserve, Sonoma County, CA:** 3,200-acre nature preserve with exceptional instrumentation (40 active climate/soil stations, 15-minute to hourly data to ≥1m depth), extensive LFM sampling network, and active wildfire management partnership.

## Products & Capabilities Described

### Soil Moisture Measuring UAS Platforms
- **Fixed-wing version:** ~18 m/s flight speed, 8× more area-efficient than multirotor, enables wide coverage in short timeframe
- **Multirotor version:** ~3 m/s flight speed, capable of low-altitude flight (15m AGL) in mountainous terrain, longer sensor integration time improves accuracy through sparse tree canopy
- **Coverage capability:** 3,000+ acres at ≤5m resolution in one operational day with small team

### Data Products Generated
1. **Soil Moisture Maps** at 5m resolution in near real-time
2. **Live Fuel Moisture Maps** derived from soil moisture via empirical plant-type relationships
3. **Integration with satellite data:** NISAR (L-band, 6-day revisit, global) and UAVSAR (20×60 km swath, P-band Year 1 testing)
4. **Formatted outputs for fire management decision support systems**

### Key Specifications
- **Resolution:** Down to 2m achievable with UAS; comparison with UAVSAR (6m) and NISAR (200m base, upscalable)
- **Processing latency:** Current system requires several hours post-processing; proposed system will deliver near real-time products
- **Area coverage:** Single day mapping of ~3,200 acres (Pepperwood area)
- **Technology Readiness:** Entry TRL 3 → Exit TRL 6 over 3-year period

## Use Cases & Applications

### Primary Use Case: Pre-Fire Situational Awareness
- Real-time characterization of soil and live fuel moisture to enable land managers, first responders, and residents to assess wildfire occurrence risk
- **Controlled burn planning:** Data to inform timing and location of prescribed burns (active use case at Pepperwood)
- **Fire response coordination:** Rapid moisture assessment to guide response to ignition sources

### Secondary Applications
- **Watershed/hydrology studies** (demonstrated in NOAA SPLASH campaign)
- **Year 3 activity:** Data gathering during active controlled burns; integration with NISAR disturbance product for active-fire and post-fire perimeter identification
- **Scalable operational deployment:** System designed for eventual expansion beyond Pepperwood to other wildfire-prone areas in western US

### Wildfire Danger Integration
Soil moisture identified as key predictor of wildfire danger and live fuel moisture threshold-showing strong impact on fire ignition probability, size, and flammability. System addresses critical gap: soil moisture historically unused in fire danger rating systems due to lack of readily available, operationally useful data.

## Key Results (Preliminary/Pilot Study 2021-2023)

### Soil Moisture Validation
- **4 field deployments** at Pepperwood with fixed-wing and multirotor UAS
- **>900 individual mobile TDR measurements** collected across three seasonal campaigns (dry, intermediate, wet conditions)
- Figure 3 shows modeled soil moisture maps with good spatial agreement across May 2022, August 2022, May 2023 flights

### Live Fuel Moisture Correlation
- **Strong empirical correlation** found between soil moisture and LFM across multiple species (chamise as indicator species)
- **Figure 4:** Clear relationship between soil moisture anomaly and LFM field samples for three chaparral species
- **Figure 5:** LFM maps successfully generated from soil moisture anomaly maps for all three seasonal campaigns

### System Refinements from Pilot Study
Iterative improvements required and implemented between deployments:
1. New slope correction algorithm for steep terrain accuracy
2. Updated electronics for expanded temperature envelope (high-temperature stability)
3. New thermal calibration technique with updated hardware
4. Development of new quadrotor version for slower, longer-integration flights over tree cover with constant terrain-relative altitude

### Final Pilot Results
- Figure 9: Final campaign showed very good UAS-based soil moisture map agreement with in situ data even through moderate forest canopy

## Notable Details

### Team Composition & Partnerships
- **Lead:** Black Swift Technologies (commercialization phase; >100 operational flights with USGS, NOAA, universities, commercial partners)
- **Co-Investigators include:**
  - Orbital Micro Systems Inc (firmware support, flight campaign data processing)
  - Pepperwood Foundation (field operations, land management liaison, communications)
  - JPL/NASA (NISAR soil moisture algorithm expertise, cross-platform validation)
  - USGS Sacramento (science PI, validation, previous pilot study lead)

### Budget Highlights (3-year total: $2,118,190.75)
- **Year 1:** $722,693.27 | **Year 2:** $679,170.65 | **Year 3:** $716,326.83
- **Key equipment purchases:** Multiple E2 UAS flight systems (4 in Y1, 2 in Y2, 4 in Y3 = 10 total platforms planned for swarm)
- **UAVSAR flight costs:** $54,000 in Year 1
- **Personnel:** Mix of BST core team (Elston PI, Stachura Co-I), OMS technical staff, Pepperwood field personnel, USGS/JPL expertise (cost-sharing partners)

### Technology Maturation Path
- **TRL Entry:** 3 (Experimental proof of concept)
- **TRL Exit:** 6 (Pilot-scale demonstration)
- **Primary technology type:** TX08 Sensors and Instruments (Radiometers); secondary: TX06.4 Environmental monitoring, TX08.1 Remote Sensing, TX10.X Autonomous Systems
- **Research category:** Earth System Science applications and decision support

### Data & Software Management
- **Code languages:** IDL and Python
- **Repository strategy:** NISAR cloud for operational code; NASA NAS repository and PI's GitLab for analysis code
- **Software release:** Posted at project end with git-flow paradigm, feature/bug tracking, Jenkins automated builds
- **Data archiving:** Validated flight campaign data archived per NASA Earth Science Data & Information Policy; NISAR outputs in NISAR cloud; UAVSAR and UAS outputs at PI institution, publicly available
- **Open Science:** No export-controlled material, no Chinese collaborators, no proprietary restrictions noted

### Competitive/Unique Advantages
1. **Predecessor technology proven:** NASA SBIR-developed L-band radiometer successfully demonstrated at Pepperwood with strong validation results
2. **Exceptional test site:** Pepperwood's dense monitoring network (40 stations) provides gold-standard ground truth unavailable elsewhere
3. **Multi-vantage point integration:** Coordinated use of swarm UAS guided by satellite data represents "next-generation platform" per RFP alignment
4. **Operational partnership:** Active land management use case (controlled burns) embedded in development cycle ensures relevance and feedback-driven iteration
5. **Cross-platform validation:** Unique opportunity to compare P-band UAVSAR (root-zone moisture), L-band NISAR, and UAS data at same location

### Risk Mitigation
Document identifies three main risk areas (partially visible in draft):
1. **Data Quality:** Reduced accuracy possible in difficult environments (steep terrain, heavy tree cover) — mitigated by direct partner feedback and iterative improvement cycle
2. **Technology delivery:** Managed through iterative field work interleaved with development
3. **Operational scalability:** Demonstrated through single-operator multi-UAS coordination development

### Alignment with Program Goals
- Addresses ROSES A.59 "pre-fire" category specifically (soil moisture/hydrology, fuel structure, fuel moisture)
- Classified as "high impact–high risk" research per SMD programmatic assessment: high impact due to critical gap in operationally useful fire-danger data; high risk in ability to deliver accuracy/timeliness needed, but managed through stakeholder engagement
- Directly supports NASA FireSense project objectives

---

## Document Status
This is a **draft Step 2 proposal** submitted March 29, 2024. Document contains complete technical narrative (Sections 1–6), budget details (all 3 years itemized), and management plan, but authorization signatures in Section V are blank (AOR signature and date fields empty). Proposal identifier 23-FIRET23-0032; NASA proposal number TBD at submission.