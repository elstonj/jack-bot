# FY25 D2P2 Technical Volume: Advanced Air-Deployed UAS for Hurricane Sampling

## Document Metadata
- **Type:** Direct-to-Phase II (D2P2) SBIR Proposal Technical Volume
- **Client/Agency:** U.S. Air Force (Department of the Air Force)
- **Program/Solicitation:** AFX255-DPCSO1 Direct-to-Phase-II Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions
- **Proposal Number:** F2D-16162
- **Topic Number:** AFX255-DPCSO1
- **Date:** Submitted FY25 (document modified 2025-03-06)
- **BST Products/Systems Referenced:** S0 UAS, SwiftCore Flight Management System, ADONIS (autonomous swarming platform)
- **Key Personnel:** 
  - Dr. Jack Elston (Founder, CEO, Principal Investigator)
  - Dr. Joshua Wadler (Co-PI, Embry-Riddle Aeronautical University)
  - Dr. Jun A. Zhang (Scientist, University of Miami)
  - Major Ian Park (End-User Point of Contact, 53rd Weather Reconnaissance Squadron)
  - Major Christopher Dyke (Alternate TPOC, 53rd Weather Reconnaissance Squadron)
  - Major Grant Talkington (Chief, AF Reserve Weather Operations, Customer)

## Executive Summary

Black Swift Technologies proposes to adapt its proven S0 UAS platform—successfully operated under NOAA SBIR contracts with over 20 operational hours in hurricanes—for integration with U.S. Air Force C-130 aircraft. The adapted system will provide high-resolution, continuous atmospheric boundary layer measurements (3D wind, temperature, humidity, pressure at 10-meter altitude) to enhance hurricane forecasting and operational situational awareness. The project includes aircraft certification, redesigned remote tube-based deployment mechanisms, cybersecurity compliance, and demonstration of at least 10 sorties with operational C-130 platforms, with deliverables including 20 prototype units and comprehensive test/evaluation reports over 24 months.

## Technical Approach

**Core System Adaptation:**
- Modify the S0 UAS (currently at TRL 8-9) from NOAA P-3 deployment configuration to C-130 compatibility
- Replace manual launch procedures with remote, tube-based activation system suitable for C-130 back-door deployment
- Enhance communications systems and implement USAF cybersecurity protocols and RF coordination standards
- Integrate S0 with C-130's onboard systems and AVAPS ground station
- Implement secure firmware upgrades and revised launch protocols per DAF requirements

**Technical Specifications:**
- Aircraft weight: ~3 pounds
- Flight endurance: Target 2 hours (improved from current 1.5 hours)
- Sampling rate: Up to 10 Hz (initial specification); 4 Hz for operational deployment
- Communication range: >150 nautical miles
- Autonomous flight range: 90 miles
- Data measurement accuracy targets: ±0.5 m/s (wind), ±0.1°C (temperature), ±2% (humidity), ±1 hPa (pressure)
- Deployment success rate target: ≥95%
- Operational tempo: One sortie every 6 hours

**Integration Modifications:**
- Redesign protective case to interface with C-130 attachment mechanisms and survive propulsive ejection
- Upgrade firmware and radio systems for remote activation while contained in tube
- Enhance onboard guidance algorithms for autonomous storm navigation (target: <5% deviation from desired flight path)
- Implement robust, long-range, secure data transmission protocols per USAF standards
- Streamline manufacturing using 3D printing and composite wing production for scalability

**Testing & Validation Approach:**
- Bench testing and simulation of cybersecurity, sensor calibration, and deployment mechanisms
- Local prototype flight trials with 10 units
- C-130 integration flight tests with minimum 10 sorties
- Real-world storm condition validation during operational hurricane missions
- Field validation with 53rd Weather Reconnaissance Squadron operators

## Products & Capabilities Described

### S0 UAS
**What it is:** Ultra-lightweight (3 lb), air-deployed unmanned aircraft system designed for high-resolution atmospheric sensing in extreme weather environments.

**Current capabilities:**
- Captures 3D wind vectors, temperature, humidity, pressure, sea surface temperature
- Operates at critical 10-meter boundary layer altitude
- TRL 8-9 with proven operational reliability
- Tube-deployed design compatible with aircraft deployment
- Modular architecture for rapid payload reconfiguration

**NOAA Performance History (2024):**
- 19 operational flights across 4 hurricanes
- 20.5 total flight hours
- Maximum single flight: 105 minutes
- Maximum winds encountered: 209 knots
- Maximum communication range: 191 miles to P-3 aircraft
- Successfully deployed in Category 4 and 5 hurricanes

**Proposed USAF C-130 Application:**
- Enables higher sortie frequency than NOAA P-3 operations (10 USAF C-130 platforms vs. 2 NOAA P-3s with 12-hour intervals)
- Will provide continuous boundary layer measurements for real-time hurricane intensity and track forecasting
- Cost per observation: ~$10,000 for 120 minutes of 4-10 Hz data vs. $1,000 for 5 minutes from dropsonde
- Provides vertical wind and turbulence measurements not available from dropsondes
- Directly ingestible into operational weather models including Global Telecommunications System (GTS)

**Competitive advantages:**
- Proven in extreme conditions with world record performance claims
- Selected over Anduril for NOAA contract
- Low cost relative to traditional platforms
- High-frequency data collection
- Lightweight, robust design
- Mature technology with extensive flight history

### SwiftCore Flight Management System
**What it is:** Low-cost, highly capable autopilot system with unique networking technologies for cooperative control.

**Application in proposal:**
- Core avionics platform for S0 UAS
- Recently obtained AFWERX flight permission, providing validation of robustness and compliance
- Establishes regulatory precedents that streamline S0 certification for DAF integration
- Supports autonomous guidance algorithms for storm feature navigation

### ADONIS Project
**What it is:** Autonomous swarming technology leveraging tube-deployed S0 design for networked operations.

**Relevance:**
- Demonstrates modular capability to reconfigure S0 for ISR and EW applications
- Currently under development in AFWERX Phase II effort
- Proof-of-concept for expanding S0 beyond weather reconnaissance

## Use Cases & Applications

### Primary Use Case: Hurricane Reconnaissance
- Enhanced meteorological data collection for tropical cyclone intensity and track forecasting
- Support for National Hurricane Operations Plan (NHOP)
- Real-time atmospheric boundary layer measurements (10-meter altitude) essential for model initialization
- Integration with National Center for Atmospheric Research (NCAR) and National Hurricane Center operations
- Supports "Readiness to Deploy and Fight" operational imperative

### Secondary/Future Applications:
- **ISR (Intelligence, Surveillance, Reconnaissance):** Lightweight EO/IR cameras with machine learning integration
- **EW (Electronic Warfare):** Specialized radio packages for USAF platforms
- **Maritime Operations:** Highly sensitive magnetometer for undersea platform detection (Navy interest)
- **Non-Defense Commercial:** Offshore energy operations, maritime insurance risk assessment, weather forecasting services, emergency management agencies

## Key Results (Phase I-Type Feasibility Study Results)

**NOAA SBIR Program Achievement:**
- Successfully demonstrated S0 UAS concept from theoretical development through operational deployment
- Addressed major technical challenges: reliable P-3 deployment mechanism, long-range communications despite size constraints, extended flight endurance, accurate wind measurements, survivability in extreme weather (heavy rain, sea spray, high winds)
- Completed through Phase I and Phase II SBIR contracts with subsequent R&D follow-on funding

**2024 Operational Season Performance:**
- 4 hurricanes sampled
- 19 S0 flights completed
- 20.5 total flight hours accumulated
- Maximum single flight endurance: 105 minutes
- Maximum sustained winds: 209 knots
- Communication range achieved: 191 nautical miles to P-3
- Data validation: Over 20 hours of high-resolution atmospheric data collected and validated against traditional methods (dropsondes, Doppler radar)
- Accuracy demonstrated: Data compared favorably against established measurement platforms

**Technology Maturation:**
- Transition from conceptual platform to fully functional autonomous aircraft
- Iterative design process refined both hardware and software
- Autonomous guidance algorithms evolved for precise storm feature navigation
- Communication system enhancements proved long-distance capability despite compact form factor

**2025 Production Trajectory:**
- 50 S0 units planned for delivery to NOAA for 2025 hurricane season (up from 19 flights in 2024)
- Production growth trajectory: 3 initial test units → 8 (year 2) → 16 (year 3) → nearly 50 (2025)
- Commercial adoption: One commercial partner integrating swarming technology; two university customers
- NOAA transition plan: Making S0 a regular component of annual hurricane sensor purchases

**End-User Validation:**
- 53rd Weather Reconnaissance Squadron commitment to adopt S0 UAS
- Positive feedback from senior squadron operators regarding enhanced storm forecasting and situational awareness
- System Program Office interest in federally-funded Phase III transition
- Signed Memorandum of Understanding (MOU) with DAF stakeholders

## Notable Details

### Commercial Market Traction
- Non-Defense commercial solution sales: $378,000 in past 12 months
- Purchase orders executed: $1,148,000 from academic/research customers
  - University of Miami (NOAA-funded): $1,112,000
  - University of Notre Dame: $36,000
- Target unit pricing: $10,000 per system (competitive in market)
- Market opportunity: Global weather forecasting and environmental monitoring valued in billions of dollars

### Operational Imperatives Addressed
1. **Readiness to Deploy and Fight:** Enhanced weather intelligence for tactical decision-making
2. **Multi-Mission Versatility:** Platform extensible to ISR, EW, and maritime detection applications
3. **Cost Efficiency:** Cost-per-observation advantage of 2.5x vs. dropsondes; enables expanded storm sampling without proportional cost increase
4. **Operational Tempo Enhancement:** Higher sortie rate capability from C-130 fleet (10 platforms) vs. NOAA P-3s (2 platforms), enabling more frequent sampling of rapidly evolving storm features

### Regulatory and Certification Pathway
- SwiftCore avionics system already obtained AFWERX flight permission
- Establishes regulatory precedents that significantly streamline S0 certification for DAF
- Phase II includes: aviation safety certification, cybersecurity compliance, RF coordination, DoD safety compliance
- Target certification achievement: Month 12 of Phase II

### Competitive Differentiation
- Selected over Anduril for NOAA contract (explicit competitive win cited)
- Proven world record performance in extreme conditions (2024)
- Superior data resolution and sampling frequency vs. legacy systems
- Modular design enabling rapid payload reconfiguration
- Low cost with high performance combination

### DAF Stakeholder Commitments
- **53rd Weather Reconnaissance Squadron** (End-Users): Committed to system adoption; Major Ian Park designated as TPOC
- **AF Reserve Weather Operations:** Major Grant Talkington (Chief) committed as customer for Phase III transition
- **System Program Office:** Program Manager expressed strong interest in Phase III federal funding
- Signed MOU with DAF representatives

### Intellectual Property Strategy
- Primary protection via trade secrets (design processes, sensor integration, algorithms)
- No broad patent portfolio currently pursued
- Phase II results to be evaluated for selective patent protection if warranted
- Maintains temporal competitive advantage while preserving innovation flexibility

### Financing & Investment
- History: Bootstrapped from founder funding since 2016
- Current SBIR funding + planned equity capital raise
- Multiple investors (venture capital, angel investors) expressed strong initial interest
- Term sheets signed contingent on Phase II award
- Planned raise to support manufacturing scale-up, USAF integration, and non-Defense market expansion

### Phase II Deliverables & Milestones
- **20 prototype S0 UAS units** (10 per year)
- **2 complete C-130 integration kits**
- **Minimum 10 operational sorties** collecting ≥10 hours of data at 4-10 Hz
- **Hardware adaptation designs** (6 months)
- **Cybersecurity/RF compliance designs** (8