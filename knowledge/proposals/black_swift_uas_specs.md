# Black Swift S0 Platform Specifications for NOAA

## Document Metadata
- **Type:** Specifications document / Contract requirements
- **Client/Agency:** NOAA (National Oceanic and Atmospheric Administration), Department of Commerce, Office of Marine and Aviation Operations, Aircraft Operations Center (AOC)
- **Program/Solicitation:** NOAA 2026-2030 IDIQ (Indefinite Delivery/Indefinite Quantity); references prior SBIR Phase I (1305M218CNRMW0059) and Phase II (1305M219CNRMW0030)
- **Date:** Created October 22, 2025; Modified November 6, 2025
- **BST Products/Systems Referenced:** Black Swift S0 platform, SwiftCore Flight Management System, SwiftPilot autopilot, SwiftTab user interface
- **Key Personnel:** Jack Elston (last editor)

---

## Executive Summary
This specifications document outlines NOAA's requirements for the procurement and operational deployment of Black Swift S0 small uncrewed aircraft systems (sUAS) from 2026-2030 for tropical cyclone (TC) operations. The S0 platform is the only sUAS that has successfully achieved NOAA Readiness Level 7/8 and been operationally deployed from the NOAA WP-3D aircraft to collect critical atmospheric measurements in the low-level, high-wind regions of hurricanes where other platforms cannot safely operate.

---

## Technical Approach

### System Development History
- **SBIR Collaboration (2018-2020):** NOAA and Black Swift collaborated under SBIR Phase I and Phase II to develop a platform compatible with WP-3D deployment
- **Operational Maturity:** Successfully launched and operated S0 platform from WP-3D into multiple hurricanes for over seven years
- **Unique Achievement:** Only sUAS to successfully fly into TC conditions on WP-3D under operational conditions and transmit critical data in real-time

### Technical Integration & Support Requirements
1. **SwiftCore Flight Management System Development:**
   - Development of pre-canned flight modules (pre-programmed autonomous flight patterns for rapid mission execution)
   - Integration with NOAA's TC operations workflows

2. **Software & Hardware Documentation:**
   - Detailed engineering specifications for airframe design
   - Custom PCB (Printed Circuit Board) schematics
   - Mechanical drawings of components and modular payloads (cloud-native CAD with version control)
   - Proprietary communication protocols and control algorithms
   - SwiftTab user interface architecture documentation

3. **Year-Round Testing & Refinement:**
   - Expanded on-aircraft flight hours with NOAA assistance
   - Access to specialized partner ranges and federal wind tunnel facilities
   - High-fidelity data collection to refine autonomous flight performance and sensor integration

4. **Modeling & Data Integration:**
   - Participation in Environmental Modeling Center (EMC) retroactive impact studies using 2023-2026 data
   - Data denial and Observing System Experiment (OSE) analysis
   - Integration into operational forecast models (parallel runs, OSSE assessments)
   - National Hurricane Center (NHC) AWIPS workflow integration

---

## Products & Capabilities Described

### Black Swift S0 Platform

**System Specifications:**
- **Weight/Endurance:** Lightweight, 100+ minute duration
- **Speed:** +55 knots cruise speed
- **Communication Range:** >200 nautical miles minimum in TC conditions
- **Data Transmission:** Real-time, accurate transmission to NOAA WP-3D in TC conditions
- **Video:** Streaming video capability for outreach purposes (noted as pending development confirmation)

**Atmospheric Measurement Capabilities (In Situ):**
- Pressure (highly accurate)
- Temperature (highly accurate)
- Humidity (highly accurate)
- Three-dimensional winds
- Surface temperature
- Wave height
- **Data Quality Standard:** Must equal or exceed existing NRD41 dropsonde technology

**Payload/Support Package:**
- Charger, cables, and protective case for field operations

**Operational Role:**
- Deployed from NOAA WP-3D aircraft into tropical cyclones
- Collects measurements at air-sea boundary (critical region for energy/momentum exchange)
- Captures data in low-level (<500m), high-wind regions where manned platforms cannot safely operate
- Provides Tier 1 Validated Earth Observation Data (can only be collected by UxS)

---

### Associated BST Software Systems

**SwiftCore™ Flight Management System**
- Enables pre-canned flight modules for autonomous mission execution
- Integrated with NOAA operational workflows

**SwiftPilot™ Autopilot**
- Autonomous flight control system

**SwiftTab™ User Interface**
- Intuitive operator interface designed to minimize training and workload

---

## Use Cases & Applications

### Primary Mission: Tropical Cyclone (Hurricane) Operations
- **Mission Profile:** Air-launched from NOAA WP-3D aircraft into active hurricanes
- **Operational Duration:** 2026-2030 hurricane seasons
- **Data Users:** 
  - Operational forecasters (National Hurricane Center)
  - Emergency managers
  - Research scientists
  - Operational modeling centers
  - Stakeholders planning coastal restoration and fisheries management

### Critical Measurement Region
- Air-sea boundary in TC low-level, high-wind environments
- Below 500-meter altitude where severe winds directly affect millions of Americans during landfall
- Region previously inaccessible due to safety constraints and logistical limitations

### Secondary Operations
- Clear air test flights
- Year-round platform performance validation
- Autonomous flight performance refinement

---

## Contract Deliverables & Scope

### 4.1 Aircraft Platforms
- Delivery of multiple Black Swift S0 platforms to NOAA AOC (quantity not specified)
- Full operational package including charger, cables, protective case

### 4.2 Training (Course Development Required)

**Operator & Observer Training:**
- Initial training delivery to designated NOAA personnel
- Draft course due within 90 days of award
- Final course due within 120 days of award
- Training materials for NOAA's future independent training capability

**Instructor Training:**
- Course development to accelerate training capability
- Goal: Full operational capabilities by 2027
- Draft course due within 120 days of award
- Final course due within 150 days of award

### 4.3 Operational Support
- Qualified operator and observer deployment on WP-3D missions during hurricane season
- Personnel must complete all required AOC training
- Maintain flight qualifications for operational availability

### 4.4 Travel Support
- Federal Travel Regulations (FTR)-compliant travel to multiple locations for training and operations
- Government provides accommodations for TC operations and test flights (scope note: document raises question about per-diem, lodging, flights, car rental inclusion)

### 4.5 Documentation & Compliance
- Calibration standards and test results
- Performance validation data (mission-based and post-mission reporting)
- Lessons learned and risk management database (accessible to Government)
- Software/hardware technical documentation

### 4.6 System Modifications & Maintenance
- Engineering and software support for NOAA TC operations integration
- Design modifications permitted for obsolescence, improved production, or performance improvement (subject to approval process)
- Long-term software/hardware documentation maintenance

### 4.7 Data Integration
- AWIPS data integration
- Post-processing and product/visualization development
- Flight planning support
- Forecaster training on data use

---

## Notable Details

### Competitive Advantages & Unique Status
- **Only Platform of Its Kind:** Only sUAS that has successfully achieved NOAA Readiness Level 7/8 and reached operational status
- **Proven Reliability:** 7+ years of successful operational deployments from WP-3D
- **Communication Achievement:** Demonstrated >200 nautical mile communication range in actual TC conditions
- **Data Equivalence:** Provides data quality equal to or exceeding NRD41 dropsonde technology

### NOAA Investment & Risk Mitigation
- NOAA has invested substantially in infrastructure for routine platform deployment
- Document emphasizes that failure to acquire S0 inhibits NOAA's ability to meet research and operational requirements for critical TC measurements

### Intellectual Property Agreement (Section 12)
**Key Provisions:**
- **Technology Readiness Level:** S0 has reached TRL 7-8
- **Government IP Protection:** NOAA requires rights to build/operate equivalent sUAS if Black Swift ceases production, is acquired, or becomes commercially unviable
- **Supply Agreement:** Black Swift commits to supply predetermined number of drones at pre-determined price over 10-year period
- **Right of First Refusal:** Black Swift retains right to continue as producer in acquisition scenario

*(Note: Document contains multiple editorial comments from reviewers questioning specific language, requirements definition, and implementation status. Key open questions flagged by Jack Elston include: streaming video implementation status, necessity of observer role, scope of travel reimbursement, documentation detail level, design modification approval timelines, Lessons Learned database status, IP rights scope, and 10-year pricing terms.)*

---

## Outstanding Contract Development Issues

The document contains flagged reviewer comments indicating the following items are still under internal discussion:
- **Streaming Video Capability:** Noted as unimplemented/not yet invoiced
- **Observer Role:** Flagged as "probably not necessary"
- **Travel Reimbursement Scope:** Unclear if limited to lodging or includes per-diem, flights, car rental
- **Design Modification Approval Process:** Concern that formal approval timeline could interfere with production; suggestion to allow verbal approval from designated government contact
- **Lessons Learned Database:** Status unclear ("is this something currently done?")
- **IP Rights Scope:** Questions about rights to replicate S0
- **10-Year Pricing:** Document suggests potential revision to language for price protection mechanism
- **Technical Documentation Section 6:** Flagged for Jack Elston review regarding appropriate detail level
- **Modeling Section 7 & NHC Integration (Section 8):** Flagged for Jack Elston review