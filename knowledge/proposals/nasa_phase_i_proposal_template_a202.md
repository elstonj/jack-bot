# NASA Phase I SBIR Proposal: SwiftCore Flight Management System (Subtopic A2.02)

## Document Metadata
- **Type:** NASA SBIR Phase I Proposal
- **Client/Agency:** NASA (Aeronautics Research Mission Directorate - ARMD)
- **Program/Solicitation:** NASA SBIR Subtopic A2.02: Enabling Aircraft Autonomy
- **Date:** Submitted 2025 (document modified through October 2025)
- **BST Products/Systems Referenced:** SwiftCore Flight Management System (FMS), BST S2 UAS, S0 UAS
- **Key Personnel:** 
  - Dr. Jack Elston (Principal Investigator, CEO/Co-founder)
  - Dr. Maciej Stachura (Lead Control and Estimation Engineer, CTO)
  - Ben Busby (Lead Software Engineer)

---

## Executive Summary

Black Swift Technologies proposes development of the **SwiftCore Flight Management System**, a modular, layered avionics architecture that enables rapid integration of advanced autonomy capabilities into uncrewed aircraft systems (UAS). The innovation addresses critical NASA barriers to autonomous flight by providing a truly modular hardware/software platform with standardized publisher-subscriber (pub/sub) messaging, embedded containerization, and a "safe sandbox" environment for testing experimental controllers. Phase I will define the layered architecture, adapt SwiftCore for multi-platform support, develop the safe sandbox concept, and demonstrate machine learning-enabled control loop tuning on the BST S2 platform.

---

## Technical Approach

### Core Innovation: Modular, Layered Avionics Architecture

**Problem Statement:** Current UAS autopilot systems employ tightly coupled, monolithic designs where sensors, actuators, communications, and control algorithms are deeply integrated. This makes adding or changing components extremely difficult and requires extensive system-wide modifications, lengthy revalidation, and costly flight testing—hindering innovation in rapidly evolving domains like NASA's Convergent Aeronautics Solutions (CAS) program.

**SwiftCore Solution:**
- **Fully modular, hierarchical architecture** with independent, intelligent hardware nodes
- **Publisher-subscribe messaging framework** with service discovery enabling plug-and-play component integration
- **Five defined control layers:**
  1. Multi-vehicle coordination and information gathering
  2. Machine learning (ML) and machine vision–based sensing and control
  3. Standard navigation (waypoint tracking, altitude/speed commands, velocity vectors)
  4. Control loop modification (dynamic PID tuning via TECS-like algorithms)
  5. Low-level sensor acquisition and actuator control

- **Standardized message types** over high-bandwidth, real-time CAN bus enabling individual layer replacement without system-wide modifications
- **Embedded containerization** (inspired by Wind River solutions) allowing experimental modules (e.g., ML-based controllers) to run securely in isolated compute nodes
- **"Safe sandbox" concept** actively monitors experimental controller commands; automatically overrides and reverts to certified flight control if predefined safety thresholds are breached

### Technical Differentiation from State-of-the-Art

| Aspect | Traditional Autopilots | SwiftCore |
|--------|----------------------|-----------|
| Architecture | Monolithic, tightly coupled | Modular, hierarchical, pub/sub messaging |
| Component Integration | System-wide modifications needed | Hot-swappable, minimal integration effort |
| New Algorithm Testing | Requires full system revalidation | Safe sandbox isolation + fallback override |
| Containerization | Not employed | Embedded containers for security/isolation |
| Certification Path | Complex, lengthy system-wide testing | Simplified via independent module validation |
| Multi-Platform Support | Often platform-specific | Configurable for fixed-wing, VTOL, multirotor |

---

## Products & Capabilities Described

### SwiftCore Flight Management System

**What it is:**
- A flight-proven, NDAA-compliant avionics platform built on ~20 years of operational experience
- Modular FMS with pub/sub messaging architecture and embedded containerization
- Integrates sensors, actuators, flight computers, and control algorithms via standardized interfaces

**Proposed Phase I Enhancements:**
1. **Formal layered architecture definition** with detailed documentation and UML diagrams
2. **Standardized messaging protocol specification** (referencing UAVCAN as benchmark)
3. **Safe sandbox framework** for secure testing of experimental external controllers
4. **ML-enabled control loop tuning module** with NDAA-compliant SBC integration
5. **Multi-platform adaptability** (fixed-wing, VTOL, multirotor with minimal reconfiguration)

**Key Specifications/Claims:**
- NDAA-compliant hardware (new ML-enabled SBC to be procured)
- Real-time CAN bus communication
- Supports complex autonomy algorithms: real-time adaptive flight control tuning, predictive maintenance
- Already flight-tested and certified in critical NASA/NOAA missions
- Reduces sensor integration time, minimizes flight test iterations, decreases avionics reconfiguration costs

**Related Previous Work with SwiftCore:**
- **Predictive Maintenance (Phase II NASA SBIR):** ML algorithms monitoring aircraft health parameters in real-time; incipient fault detection reducing maintenance downtime
- **Machine Vision Emergency Landing:** Deep learning terrain assessment generating "go/no-go" landing maps; validated in simulated engine-out scenarios
- **GPS-Denied Navigation (NOAA-funded):** Machine vision + "signals of opportunity" (radio, cellular, ADS-B) providing robust navigation in GPS-denied/jammed environments
- **Hurricane Observation (NOAA partnership):** Autonomous eyewall and inflow region navigation; center fix determination, maximum wind speed measurement, inflow characterization; validated during 2024 hurricane season

### BST S2 UAS Platform

**What it is:**
- Fixed-wing, flight-proven uncrewed aircraft system
- Equipped with SwiftCore Flight Management System
- Certified for multiple NASA and NOAA missions

**Use in Phase I:**
- Primary flight test platform for ML-enabled control loop tuning demonstration
- Hardware-in-the-loop (HIL) and flight validation vehicle

---

## Use Cases & Applications

### NASA-Aligned Applications

1. **Remote Sensing Operations**
   - Rapid integration of new sensors without system-wide reconfiguration
   - Application: Earth science missions, environmental monitoring

2. **Wildfire Response**
   - Advanced autonomy enabling rapid deployment
   - ML-based vision for fire extent/behavior assessment
   - Multi-vehicle coordination

3. **Disaster Management & Rescue**
   - BVLOS operations in hazardous environments
   - Safe sandbox enables testing new autonomy algorithms without mission risk
   - Predictive maintenance reduces downtime in rapid-response scenarios

4. **Volcanic Monitoring** (validated application)
   - BVLOS sampling at extreme altitudes/conditions
   - Previously demonstrated at Makushin Volcano (with NASA)

5. **Hurricane/Severe Weather Observation** (validated application)
   - Autonomous eyewall penetration
   - Real-time data collection in extreme conditions
   - Validated during 2024 hurricane season with multiple successful flights

6. **Goods Delivery & Advanced Air Mobility (AAM)**
   - Modular avionics support for emerging AAM platforms
   - Rapid reconfiguration for varied payload configurations

### Government & Commercial Customers

- **Primary:** NASA, NOAA, USGS, Department of Defense
- **Commercial:** Aerial survey companies, agricultural monitoring, infrastructure inspection
- **OEM/Academic:** UAS manufacturers, research institutions seeking rapid autonomy integration

---

## Phase I Technical Objectives & Deliverables

### Objective 1: Layered Architecture Definition
- **Task:** Define and document modular, multi-layer sensing/control architecture spanning high-level coordination to low-level sensor-actuator interfaces
- **Deliverables:**
  - Detailed architecture documents and flow diagrams
  - Standardized messaging protocol specification (pub/sub + service discovery)
  - Simulation models (hardware-in-the-loop) demonstrating layer-to-layer interactions

### Objective 2: SwiftCore System Adaptation
- **Task:** Update SwiftCore to support evolved NASA requirements; enable multi-platform support (fixed-wing, VTOL, multirotor)
- **Deliverables:**
  - Updated software interfaces and hardware configurations
  - Reconfiguration documentation for different platforms
  - Demonstration flight test reports validating adaptability

### Objective 3: Safe Sandbox Development
- **Task:** Create "safe sandbox" environment for experimental external controllers (e.g., ML modules) with automatic override if safety thresholds breached
- **Deliverables:**
  - Prototype safe sandbox module
  - Safety threshold and override logic documentation
  - Simulation and HIL test results demonstrating safe fallback transitions

### Objective 4: ML-Enabled Control Loop Tuning Demonstration
- **Task:** Develop proof-of-concept ML module for in-flight PID tuning via calibrated control inputs (doublets); integrate NDAA-compliant flight computer
- **Deliverables:**
  - Prototype ML tuning module
  - Flight test data validating in-flight tuning performance
  - Final report with performance metrics and lessons learned

---

## Work Plan & Schedule

### Task Structure (6-Month Phase I)

| Task | Description | Duration | Key Milestones |
|------|-------------|----------|-----------------|
| 1 | Layered Architecture & Messaging | Months 1-2 | M1: Architecture definition doc & protocol spec complete |
| 2 | SwiftCore System Adaptation | Months 1-4 | Incremental updates via version control |
| 3 | Safe Sandbox Development | Months 2-5 | M3: Prototype completed & bench-tested |
| 4 | ML-Enabled Control Loop Tuning | Months 3-6 | M4: HWIL demo on BST S2 |
| 5 | Integration, HIL Simulation | Throughout | Continuous validation |
| 6 | Final Documentation & Reporting | Month 6 | Delivery to NASA portal |

### Resource Allocation (720 total hours)

| Team Member | Hours | Role |
|------------|-------|------|
| Dr. Jack Elston (PI) | 210 | Electronic design, firmware, project management |
| Dr. Maciej Stachura | 210 | Control & estimation, algorithm development |
| Ben Busby | 300 | Software development, integration |

### Location & Facilities
- **Development facility:** Boulder, Colorado (state-of-the-art BST facility)
- **Resources:** UAS integration laboratory, HIL test rigs, precision instruments, high-performance computers
- **Flight assets:** BST S2 fleet (maintained under strict quality control)
- **New Equipment:** NDAA-compliant ML-enabled single-board computer (SBC) for Phase I

---

## Risk Mitigation

| Risk | Mitigation Strategy |
|------|-------------------|
| **Integration Complexity** – New messaging protocols may introduce latency/interoperability issues | Rigorous HIL testing and simulation validation before flight testing |
| **Legacy System Adaptation** – Updating SwiftCore may cause compatibility issues | Incremental software updates with iterative testing, version control, traceability |
| **Experimental Module Safety** – ML modules might generate unsafe commands | Robust safe sandbox with predefined thresholds & override logic; extensive bench/sim testing |
| **ML Algorithm Tuning Accuracy** – Initial tuning may be suboptimal | Historical flight data for training; incremental simulation testing; conservative operational thresholds |
| **Market Acceptance** – Resistance to closed-source system | Emphasis on standardized messaging, open interfaces, rigorous certification; 20 years operational credibility |
| **Regulatory/Certification** – FAA/international rules may delay deployment | Continued collaboration with regulators; compliance with DO-178C and safety standards |
| **Integration with Third-Party Components** – Compatibility challenges | Open communication interface + safe sandbox isolation for non-certified modules |
| **Cybersecurity** – Critical UAS vulnerability | NDAA-compliant hardware, robust CAN bus encryption, access controls, continuous monitoring |

---

## Key Results & Validated Achievements (Prior Related Work)

### Previous NASA/NOAA Projects Demonstrating SwiftCore Maturity

1. **Predictive Maintenance (Phase II SBIR)**
   - ML algorithms successfully identified incipient component faults in real-time
   - Result: Substantially reduced maintenance downtime; enhanced reliability

2. **Machine Vision Emergency Landing**
   - Deep learning terrain categorization (trees, water, buildings, roads)
   - Result: Autonomous identification of safe landing zones during simulated engine-out; validated system capability for critical BVLOS missions