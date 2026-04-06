# AI/ML-Based Anomaly and Fault Detection System for UAS

## Document Metadata
- **Type:** Phase II SBIR Proposal - Technical Volume
- **Client/Agency:** U.S. Air Force Research Laboratory (AFRL); Air Force via AFWERX
- **Program/Solicitation:** AF 20.3 - CSO1 (Artificial Intelligence/Machine Learning); SBIR Topic AF 20.3
- **Proposal Number:** F2-14757
- **Date:** Submitted 2020 (created/modified June 2021)
- **BST Products/Systems Referenced:** SwiftCore (FMS), S2 (fixed-wing UAS), S0 (fixed-wing UAS), E2 (multirotor), Piccolo (third-party), Dronecode (third-party)
- **Key Personnel:** Dr. Jack Elston (Principal Investigator, CEO/Founder), Dr. Maciej Stachura (CTO, Machine Learning Lead)

## Executive Summary
Black Swift Technologies proposes developing an AI/ML-based anomaly and fault detection system for Unmanned Aircraft Systems (UAS) to improve reliability, operational readiness, and safety. The system will utilize unsupervised machine learning algorithms (specifically Generative Adversarial Networks for time-series analysis) to analyze flight telemetry data and predict maintenance issues before they cause failures. BST will deliver a cloud-based web portal for both commercial and defense customers, initially integrated with Air Force Research Laboratory's Piccolo-equipped Group 2 UAS and expandable to other flight management systems.

## Technical Approach

### Core Technology
- **Algorithm Type:** Unsupervised machine learning using Generative Adversarial Networks (GANs) for time-series anomaly detection
- **ML Library:** Orion (unsupervised time-series anomaly detection library)
- **Method:** Two-step training process:
  1. Build expected outputs using GANs (e.g., communications RSSI, propulsion power)
  2. Apply sliding-window analysis comparing predicted vs. measured values; flag deviations exceeding threshold (in terms of standard deviations)

### Subsystems Monitored
- Communications (RSSI tracking)
- Propulsion efficiency and loss detection
- Control system degradation
- Actuator/servo performance
- Vibration and thermal signatures (via potential added sensors)

### Data Sources
- Historical flight logs from AFRL-supplied Piccolo data
- BST internal SwiftCore database (hundreds of UAS flights)
- Dronecode-derived system logs from federal/state partners
- Manual maintenance logs and failure reports from operators
- Proposed addition: embedded acoustic and thermal sensors

### Integration Approach
- Web-based portal for log upload and analysis
- Separate cloud instances for DoD and commercial customers (no cross-customer data sharing)
- Open API for customer-developed analysis tools
- Real-time onboard versions of algorithms for flight management systems (embedded in autopilot)
- Tight integration with SwiftCore FMS for enhanced early warning

## Products & Capabilities Described

### 1. **AI Predictive Maintenance Web Portal**
- **What it is:** Cloud-based SaaS platform for analyzing UAS flight logs to detect anomalies and predict maintenance needs
- **How used in this context:** Serves both USAF/DoD and commercial operators; separates defense and commercial instances for security
- **Specifications/Performance Claims:**
  - Processes logs automatically; parses Piccolo, SwiftCore, and Dronecode flight data
  - Detects anomalies with focus on minimizing false positives/negatives
  - Performance envelope detection: predict reduction in flight time to within 5% accuracy
  - Propulsion anomaly detection: 100% accuracy on degraded performance scenarios
  - Pricing: $10/month per aircraft (SaaS model)
  - Commercial TAM: ~$36M annually (362,101 registered commercial UAS × $10/month)
  - Total TAM (all UAS): ~$104M annually

### 2. **SwiftCore Flight Management System**
- **What it is:** BST-developed autopilot and flight management system
- **Used in this context:** Tight integration with predictive maintenance algorithms; benefits from onboard edge AI capability
- **Advantages:** Full control over hardware/firmware; no supply chain vulnerabilities from hostile nations

### 3. **S2 Fixed-Wing UAS**
- **What it is:** Medium-altitude fixed-wing unmanned aircraft
- **Used in this context:** Certification and flight test platform for real-time propulsion anomaly detection; performance envelope validation
- **Specifications:** Will carry onboard neural network for anomaly detection; flight-tested with degraded propulsion scenarios

### 4. **S0 Fixed-Wing UAS**
- **What it is:** Small, low-cost fixed-wing UAS
- **Used in this context:** User training and operational demonstration platform for AFRL

### 5. **E2 Multirotor**
- **What it is:** Multi-rotor UAS platform
- **Used in this context:** Supporting commercial applications; example: Alerion wind turbine inspection system uses E2 with SwiftCore and onboard edge AI

## Use Cases & Applications

### Defense/Military
1. **AFRL Group 2 UAS Operations:** Maintain readiness of Piccolo-equipped fixed-wing systems; support Skyborg Vanguard program
2. **Travis AFB Security:** Dronecode-based "drone in a box" multirotor ISR systems for base security; enable remote operations with confidence
3. **Performance Envelope Tracking:** Real-time decision-making on mission capability based on detected degradations
4. **Field Readiness:** Preventative maintenance to keep mission-critical systems operational when deployed

### Commercial/Civilian
1. **Routine NAS Operations:** Increase safety and operational confidence for UAS flying in National Airspace System
2. **Data Collection Missions:** Support NASA, NOAA, USGS operations with predictive maintenance; minimize payload loss (sensors can exceed $100K)
3. **Wind Turbine Inspection (Alerion partnership):** Automated maintenance monitoring for autonomous inspection UAS
4. **Commercial ISR/Mapping:** Enable BVLOS operations with greater confidence in system reliability

### Risk Mitigation
- Prevent loss of expensive aircraft and payloads
- Reduce injury/loss-of-life risk from mid-air failures over populated areas
- Enable extended BVLOS operations with greater confidence
- Minimize downtime through predictive scheduling

## Phase I Feasibility Study Results

### Key Findings
- **Current USAF Practice:** Uses combination of manual maintenance logs and various software systems; significant manual labor; lacks lifetime monitoring
- **Supervised + Unsupervised ML Best Approach:** Combination of both techniques most effective for drawing conclusions from manual logs, flight data, and maintenance software
- **Novel Sensor Opportunities:** Phase I identified potential embedded sensors (acoustic, thermal) that could augment existing telemetry for enhanced anomaly detection
- **Data Availability:** AFRL has large, well-annotated Piccolo flight datasets with detailed maintenance/failure reports suitable for algorithm training

### End-User Engagement
- **AFRL Contact:** Dr. Dave Grymin (AFRL UAS expert); provided access to significant Piccolo flight data and maintenance records
- **Travis AFB Contact:** Kenny Perkins (Chief, Plans and Programs, 60th SFS); confirmed interest from security operations perspective
- **Federal Partners:** NASA, NOAA, NREL already using early web portal version for flight tracking on BST S2 aircraft
- **Commercial Partner:** Alerion (European firm) using current web portal and expressing strong interest in Phase II enhancements

### New Requirements from AFRL
- Onboard decision-making capability reacting to AI preventative maintenance inputs
- Performance envelope identification and detection (real-time environmental/system constraints)
- Integration with S2 platform for basic capability demonstration
- Certification of BST platforms for DoD use

## Phase II Technical Objectives and Key Results

### Task 1: Gather and Process Historical Flight Data (0-4 months)
- Ingest AFRL Piccolo logs and annotations into BST web portal
- Parse logs automatically; populate cloud database with AFRL data
- Run baseline (non-ML) version of processing; establish performance metric
- Provide AFRL logins for ongoing log uploads

### Task 2: Develop, Train, and Validate Anomaly Detection Algorithms (0-8 months)
- **Communications Subsystem:** Demonstrate improved failure/degraded performance detection vs. baseline on RSSI data
- **Propulsion System:** Expand algorithms to detect efficiency loss and complete loss of propulsion
- **Control Degradation:** Monitor actuator and control loop performance
- **Deliverable:** Open API for AFRL to develop custom analysis tools

### Task 3: BST S2 Flight Certification and Envelope Testing (8-12 months)
- Obtain USAF approval for S2 use in Air Force research
- Conduct 5 test flights with onboard anomaly detection for propulsion subsystem
- Test degraded propulsion scenarios; achieve:
  - 100% accuracy detecting anomaly
  - Predict impact/reduction in flight time to within 5% accuracy
- Generate certification documentation

### Task 4: Transition to AFRL Usage (12+ months)
- Deliver working anomaly detection web portal to AFRL
- Enable upload of Piccolo flight logs with automatic anomaly/maintenance scanning
- Training and operational support

### Milestone Schedule and Deliverables
| Task | Delivery | Amount |
|------|----------|--------|
| Refined Work Plan | +1 month | $50,000 |
| System Demo with AFRL Data | +4 months | $100,000 |
| GAN Implementation Demo | +8 months | $150,000 |
| S2 Certification & Envelope Framework | +12 months | $150,000 |
| Final Report | +13 months | $100,000 |
| AF User Training | +13 months | $50,000 |
| Test Support (UAS Integration) | +13 months | $50,000 |
| Test Support (S0 UAS) | +14 months | $50,000 |
| Additional Reporting | +15 months | $47,674 |

### Key Deliverables
1. **Cloud-based software solution** meeting Air Force operational requirements:
   - Cloud instance replicable on AF designated servers
   - Unique database architecture for parsing aircraft logs into labeled ML-ready data
   - Secure login ensuring data isolation
   - Web-based intuitive user interface
   - Customized ML-based preventative maintenance tools
   - Open API for AFRL custom analysis
2. **S2 UAS Certification** documentation for AFRL research use
3. **Software documentation and user manuals** for all interactions
4. **Commercialization status update** (available at +15 months)

## Commercialization Plan

### Business Model
- **SaaS Subscription:** $10/month per aircraft
- **Market Targets:** Both DoD and commercial operators
- **Revenue Goals:**
  - Year 1: 3% market share = $1M annual revenues
  - Year 5: 35% market share = $12.5M annual revenues
- **Market Size:** 872,694 total UAS registered with FAA (362,101 commercial); TAM ~$104M annually (all) / ~$36M (commercial only)

### Go-to-Market Strategy
- Direct sales to UAS operators
- Partnerships with UAS manufacturers
- Marketing via social media, trade publications, email campaigns
- Integration with aircraft sales (offered free initially to BST aircraft purchasers)
- Accelerator support: Capital Factory (Austin, TX) membership for mentoring and fundraising

### Competitive Advantages
1. **Multi-manufacturer autopilot support:** Only system supporting Piccolo, SwiftCore, Dronecode, and planned DJI support
2. **Intrinsic autopilot expertise:** Deep understanding of flight management fundamentals enables better third-party system diagnostics
3. **Vertical integration:** BST designs all components of its aircraft; no supply chain vulnerabilities
4. **Existing early adopters:** NASA, NOAA, NREL already using baseline portal
5. **IP Protection:** Source code protected via copyright/trade secrets; potential future patents from Phase III

### Intellectual Property
- Source code protected by copyright and trade secrets (not visible to users)
- Patents to be evaluated if Phase III proceeds
- SBIR data rights available for Phase III commercialization

## Notable Details

### Key Personnel
- **Dr. Jack Elston (PI, CEO/Founder):** 15+ years UAS experience; Ph.D. (CU Boulder, 2011) focused