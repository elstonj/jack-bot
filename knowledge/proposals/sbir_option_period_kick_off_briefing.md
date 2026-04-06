# SBIR Option Period Kick-Off Briefing: Development of a SL UAS with Advanced MAD and Acoustic Sensing Capabilities

## Document Metadata
- **Type:** SBIR Phase I Option Period Kick-Off Briefing (presentation)
- **Client/Agency:** U.S. Navy (Department of the Navy SBIR Program)
- **Program/Solicitation:** Navy SBIR Topic N251-016
- **Contract Number:** N6833525C0492
- **Date:** April 6, 2026 (created/modified); April 21, 2026 (Option Period Kick-Off)
- **BST Products/Systems Referenced:** S0 UAS
- **Key Personnel:** 
  - Dr. Jack Elston (PI) – PhD Aerospace Engineering, 15+ years UAS development
  - Dr. Maciej Stachura (Co-I) – PhD Aerospace Engineering, sensor fusion and calibration expert
  - Beck Cotter (last editor)
- **Collaborators:** Adam Sniff (Cetacean Research Technology – acoustic sensors SME); Dr. Jeffrey Orton (QuSpin Inc. – magnetometer SME)

## Executive Summary
Black Swift Technologies is developing a Sonobuoy-Launched (SL) UAS platform integrating magnetic anomaly detection (MAD) and passive acoustic sensing capabilities for Navy anti-submarine warfare (ASW) operations. Phase I Option will demonstrate sensor integration feasibility, platform compatibility with sonobuoy launch constraints, sensor performance validation, and data fusion algorithms to enhance underwater target detection and classification.

## Technical Approach

**Phase I Base Objectives:**
1. **Sensor Integration Feasibility:** Evaluate noise mitigation strategies to minimize platform-induced interference; ensure hydrophone meets Navy's sensitivity, frequency range, and depth requirements.
2. **Platform Modification:** Modify existing S0 UAS to accommodate sonobuoy launch constraint (SLC) payload volume and weight constraints.
3. **Sensor Performance Validation:** Conduct laboratory simulations and bench testing to characterize magnetometer noise performance and hydrophone acoustic sensitivity.
4. **Data Fusion Algorithm Development:** Design, implement, and test algorithms combining MAD and acoustic sensor outputs for enhanced underwater target detection and classification.

**Work Plan Components:**
- **Requirements Analysis & Preliminary Design:** Validate magnetometer and hydrophone sensors; plan compute module integration; optimize to reduce Size, Weight, and Power (SWAP) while maintaining capability.
- **S0-UAS Design Modifications:** Complete CAD design and updated electronics design for sensor accommodation.
- **Sensor Integration & Testing:** Magnetometer testing for noise spectral density compliance; parallel validation using larger BST UAS platform flying QuSpin magnetometer.
- **UAS Prototype Construction:** Modify S0 UAS to accommodate sensors and Navy mission requirements.

## Products & Capabilities Described

**S0 UAS System:**
- Existing small UAS platform being modified for sonobuoy launch capability
- Currently operational; has been flown with QuSpin magnetometer in test flights
- Airframe and avionics design allows rapid modification and component swapping
- Can trade battery capacity for payload; can modify airframe size/shape
- Designed with all onboard sensor processing and system validation capabilities

## Use Cases & Applications

**Primary:**
- **Navy Anti-Submarine Warfare (ASW):** Tube-launched from P-8A maritime patrol aircraft for MAD and acoustic deployment in-water sensor operations

**Secondary Commercialization Targets:**
- **Federal Agencies:** NOAA (environmental monitoring), DHS (border security, maritime surveillance)
- **Private Sector:** Offshore energy (pipeline and subsea infrastructure monitoring), illegal fishing detection, underwater ecosystem monitoring

## Key Deliverables & Schedule

**Option Period Deliverables:**
- Kickoff Briefing: April 14, 2026 (CLIN 0005) ✓
- Option Period Progress Report: June 29, 2026 (CLIN 0006)
- Option Period Final Report: September 28, 2026 (CLIN 0006)

## Technical Sensors & Components

**Magnetometer:**
- QuSpin QTFM Gen-2 magnetometer (identified sensor)
- Must meet Navy sensitivity, frequency range, and depth requirements
- Primary challenge: maintaining noise requirements within small UAS
- Mitigation: BST has conducted test flights with QuSpin sensor on similar UAS; rapid modification capability

**Hydrophone (Acoustic Sensor):**
- Supplier: Cetacean Research Technology (Adam Sniff, P.E., acoustic SME)
- Must meet Navy sensitivity and frequency range requirements
- Testing and validation facilities available through Cetacean Research
- Challenge: fitting into tube-launched UAS constraints

**Compute Module:**
- Required for real-time data fusion and processing
- Must be integrated while respecting sonobuoy launch payload constraints

## Key Challenges & Risk Mitigation

| Challenge | Mitigation |
|-----------|-----------|
| Maintaining magnetometer noise requirements in small UAS | Test flight history with QuSpin sensor; ability to rapidly modify all S0 components |
| Fitting sensors and compute into tube-launched platform | S0 design flexibility; can trade batteries for payload; modify airframe size/shape |
| Achieving $10K price point | Sensor/compute optimization; production efficiency improvements planned for Phase II |

## Facilities & Resources

- **Black Swift Technologies Integration Lab:** UAS hardware prototyping, sensor integration, real-time processing tools
- **Magnetic Sensing:** Access to QuSpin sensors; proven flight history with QuSpin on BST UAS
- **Hydrophone Testing:** Cetacean Research facilities for testing and validation
- **Computing:** Onboard processing capabilities inherited from S0 architecture

## Transition & Commercialization Planning

**Navy Integration Path:**
- Target users: Groups conducting ASW activities within Navy
- Collaboration with NAVAIR program managers and P-8A community stakeholders
- Phase II focus: Full Navy operational integration and real-time demonstration
- Continuous stakeholder feedback loop for adoption alignment

**Benefits Claimed:**
- Aligns with Navy goals for cost-effective autonomous ASW systems
- Scalable production with future swarm capabilities for larger area coverage
- Operational demonstration across diverse environments (referenced: 19 flights across Hurricanes Ernesto, Francine, Helene, Milton)

**Production Scaling Vision:** 3 → 19 → 50 → 150 units (leveraging airframe/avionics similarity with existing platforms)

**Additional Transition Opportunities:**
- **Continued NOAA Collaboration:** Multi-use case approach allows cost reduction and reliability improvements
- **Stratospheric Balloons:** NASA flight opportunities; long-loiter high-altitude operations; applications in wildfire monitoring and disaster response; development of stratospheric launch from alternative high-altitude platforms

## Personnel Qualifications

**Dr. Jack Elston (Principal Investigator)**
- PhD Aerospace Engineering
- 15+ years UAS development experience
- Led NOAA, NASA, and DoD-funded UAS deployments into hurricanes and extreme environments

**Dr. Maciej Stachura (Co-Investigator)**
- PhD Aerospace Engineering
- Expert in sensor fusion and UAS calibration
- Architect of S0 onboard sensor processing and system validation

**External Collaborators:**
- Adam Sniff (Cetacean Research Technology) – Acoustic sensor SME
- Dr. Jeffrey Orton (QuSpin Inc., Senior Engineer) – Magnetometer SME for QTFM Gen-2 integration and testing

## Notable Details

- Document is **export-controlled** under Arms Export Control Act; distribution restricted to U.S. Government agencies
- Data Rights: DFARS SBIR Data Rights restrictions apply
- Classification Level: CUI (Controlled Unclassified Information); DISTRO B distribution
- Navy POC: Angel R. Ruiz-Reyes, (301) 757-7955
- BST has **existing flight experience** with magnetometer payloads in operational environments (hurricane deployments documented)
- Budget constraint identified: $10K price point requirement for operational viability
- **Phase II planning** explicitly includes full Navy integration and real-time operational demonstration
- Multi-use case approach enables cost recovery across NOAA, DHS, and private sector applications