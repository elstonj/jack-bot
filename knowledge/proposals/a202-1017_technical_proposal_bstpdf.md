# Adaptive and Secure Autonomy for UAS: A Modular Approach to Flight Control, Machine Learning Integration, and Multi-Vehicle Coordination

## Document Metadata
- **Type:** NASA SBIR Phase I Technical Proposal
- **Client/Agency:** NASA (Aeronautics Research Mission Directorate)
- **Program/Solicitation:** NASA SBIR Subtopic A2.02: Enabling Aircraft Autonomy; ProSAMS Proposal Number A2.02-1017
- **Date:** Submitted March 10, 2025
- **BST Products/Systems Referenced:** SwiftCore Flight Management System, BST S2 (fixed-wing UAS platform)
- **Key Personnel:** Dr. Jack S. Elston (PI, CEO/co-founder), Dr. Maciej Stachura (Lead Control and Estimation Engineer, CTO), Ben Busby (Lead Software Engineer)

---

## Executive Summary

Black Swift Technologies proposes to develop and validate a modular, layered architecture for the SwiftCore Flight Management System that enables rapid integration of advanced autonomy capabilities into uncrewed aircraft systems. The system uses a publisher-subscriber (pub/sub) messaging framework with embedded containerization and a "safe sandbox" safety layer to allow external experimental controllers (including machine learning modules) to operate without compromising flight safety. This Phase I effort directly addresses NASA's need for rapidly reconfigurable avionics that support cognition, multi-objective decision-making, fault tolerance, and streamlined certification.

---

## Technical Approach

### Core Architecture
The SwiftCore Flight Management System is built on a **fully modular, hierarchical architecture** with independent hardware nodes interconnected via:
- **Publisher-subscriber (pub/sub) messaging** with dynamic service discovery
- **Standardized message types** for inter-layer communication
- **Embedded containerization** (inspired by Wind River's avionics solutions) for isolation and portability

### Five Functional Layers
1. **Multi-vehicle coordination and information gathering** (highest level)
2. **Machine learning and machine vision–based sensing and control**
3. **Standard navigation** (waypoint management, altitude/speed commands, velocity vectors)
4. **Control loop modification** (PID tuning, TECS-like algorithms)
5. **Low-level sensor and actuator interface** (lowest level)

### Key Innovation: "Safe Sandbox"
- Experimental or external ML-based controllers run in isolated containers
- A supervisory controller continuously monitors commands from non-certified modules
- If unsafe conditions are detected (parameters outside certified limits), the certified fallback control system automatically assumes command
- Enables rapid iteration on complex algorithms while maintaining absolute confidence in safety

### Messaging Framework
- Standardized message formats for sensor readings, control commands, and status alerts
- Reference implementation leverages UAVCAN as a model
- High-bandwidth, real-time communication bus enabling independent replacement or enhancement of individual layers

---

## Products & Capabilities Described

### SwiftCore Flight Management System
**What it is:**
- Flight-proven, NDAA-compliant avionics platform
- Deployed in critical NASA and NOAA missions (hurricane observation, volcanic gas sampling)
- Nearly 20 years of operational experience
- Supports multiple aircraft configurations (fixed-wing, VTOL, multirotor)

**Capabilities and Features:**
- Hot-swappable sensors, actuators, autopilots, and flight computers
- Real-time adaptive flight control tuning
- Predictive maintenance algorithms
- Machine vision-based emergency landing system (terrain assessment for autonomous landing zone selection)
- GPS-denied navigation using signals of opportunity (radio, cellular, ADS-B)
- ML-enabled in-flight control loop tuning via injected control inputs (doublets)
- Support for beyond visual line-of-sight (BVLOS) operations

**Use in This Proposal:**
- Serves as the foundation platform being enhanced with modular layers and safe sandbox capability
- Will be adapted to support new messaging protocols and multi-platform configurations
- Flight test platform: BST S2 fixed-wing UAS

### BST S2 Platform
- Fixed-wing uncrewed aircraft already certified under previous NASA SBIR projects
- Successfully deployed in hazardous environments (hurricane observation, volcanic gas sampling)
- Primary flight test vehicle for Phase I demonstration
- Will undergo HWIL testing with ML-enabled control loop tuning

### NDAA-Compliant ML-Enabled Single Board Computer (SBC)
- To be procured as part of Phase I effort
- Features computational acceleration (FPGA-based processing) and dedicated ML support
- Will integrate as parallel "sandbox" controller
- Outputs monitored and overridden by certified SwiftCore system as needed

---

## Use Cases & Applications

### Research and Science Missions
- **Hurricane Observation:** Real-time autonomous navigation through eyewalls and inflow regions; center fix determination, maximum wind speed measurement, inflow characterization
- **Volcanic Gas Sampling:** BVLOS autonomous sampling missions (validated at Makushin Volcano)
- **Atmospheric Monitoring:** Multi-vehicle cooperative atmospheric profiling; severe weather sampling

### Safety-Critical Operations
- **Emergency Landing:** Machine vision-based autonomous identification of safe landing zones during engine-out scenarios
- **GPS-Denied Navigation:** Operation in jamming environments using vision and signals of opportunity
- **Predictive Maintenance:** ML detection of incipient component faults to reduce maintenance downtime

### Commercial and Government Applications
- Remote sensing
- Wildfire response
- Goods delivery
- Disaster management
- Environmental monitoring
- Infrastructure inspection
- Aerial survey

### Advanced Air Mobility (AAM)
- Multi-vehicle coordinated missions with minimal human oversight
- Integration into National Airspace System (NAS) operations

---

## Technical Objectives (Phase I)

### Objective 1: Layered Architecture Definition
- Define and document modular, multi-layer sensing and control architecture
- Develop standardized pub/sub messaging protocol specifications
- Create simulation models (hardware-in-the-loop) demonstrating layer-to-layer interactions

**Deliverables:**
- Detailed architecture documents and flow diagrams
- Standardized messaging protocol specification
- HIL simulation models

### Objective 2: SwiftCore System Adaptation
- Update SwiftCore to support evolved operational requirements based on 20 years of flight experience
- Support multiple aircraft configurations with minimal interface changes
- Adapt control and sensing layer definitions per NASA CAS group requirements

**Deliverables:**
- Updated software interfaces and hardware configurations
- Reconfiguration method documentation for different platforms
- Demonstration flight test reports

### Objective 3: Safe Sandbox Development
- Develop framework allowing external, experimental controllers (ML-based modules) to integrate without compromising safety
- Define safety thresholds and override logic
- Implement supervisory controller continuously monitoring non-certified module commands

**Deliverables:**
- Prototype safe sandbox module
- Safety threshold and override logic documentation
- Simulation and HIL test results demonstrating safe transitions

### Objective 4: ML-Enabled Control Loop Tuning Demonstration
- Demonstrate proof-of-concept for machine learning–enabled, in-flight tuning of control loops
- Use NDAA-compliant flight computer integrated with SwiftCore
- Inject specific control inputs (doublets) to automatically tune PID controllers

**Deliverables:**
- Prototype ML module for control loop tuning
- Flight test data validating tuning performance
- Final report with performance metrics and lessons learned

---

## Work Plan & Schedule

### Task 1: Layered Architecture Definition & Messaging Protocol Specification
- Design review meetings with controls, firmware, and software teams
- UML modeling tools for architecture diagrams
- Prototype message libraries (UAVCAN reference)
- Bench tests with representative sensor/actuator nodes
- **Duration:** Primary focus Months 1-2

### Task 2: SwiftCore System Adaptation and Update
- Review existing implementation; identify updates needed for refined layer definitions
- Modify firmware and software for new messaging interfaces and multi-platform support
- Update control algorithms to interface with new messaging framework
- Version control via git/trac
- Iterative development using software-in-the-loop (SWIL) simulation
- Digital twin environment for flight simulation under various conditions
- **Duration:** Months 2-4

### Task 3: Safe Sandbox Development
- Develop framework for integrating external, experimental control modules
- Define safety thresholds based on system state
- Implement supervisory controller monitoring incoming commands
- Simulation of flight scenarios including edge cases
- Software module acting as intermediary between external controllers and certified autopilot
- Controlled bench tests with injected faulty commands
- **Duration:** Months 2-5

### Task 4: ML-Enabled Control Loop Tuning Demonstration
- Develop proof-of-concept ML module for automatic PID tuning via doublet injection
- Integrate on NDAA-compliant flight computer board
- Collect historical flight data for ML model training
- Supervised learning framework with iterative data collection and validation
- Bench tests with simulated control loop perturbations
- Flight tests on BST S2 platform
- **Duration:** Months 3-6

### Schedule (6-month Phase I)
| Task | Months 1-2 | Months 2-3 | Months 3-4 | Months 4-5 | Months 5-6 |
|------|-----------|-----------|-----------|-----------|-----------|
| Layered Architecture & Messaging | ■■■ | ■ | | | |
| SwiftCore Adaptation | ■ | ■■■ | ■■ | | |
| Safe Sandbox Development | | ■■■ | ■■■ | ■ | |
| ML Control Loop Tuning | | ■ | ■■ | ■■■ | ■■ |

### Resource Allocations (Total 720 hours)
| Task | Dr. Jack Elston | Dr. Maciej Stachura | Ben Busby | Total |
|------|-----------------|-------------------|----------|-------|
| Layered architecture definition | 50 | 40 | 30 | 120 |
| SwiftCore system adaptation | 40 | 40 | 40 | 120 |
| Safe sandbox development | 30 | 40 | 80 | 150 |
| ML control loop tuning demo | 40 | 40 | 80 | 160 |
| Integration, HIL simulation | 30 | 30 | 40 | 100 |
| Final documentation & reporting | 20 | 20 | 30 | 70 |
| **Total** | **210** | **210** | **300** | **720** |

### Key Milestones
- **Month 1:** Detailed architecture definition document and messaging protocol specifications completed
- **Month 2:** Successful bench testing of newly defined messaging protocol between prototype nodes
- **Month 3:** Safe sandbox module prototype completed and validated in controlled bench tests
- **Month 6:** Demonstration HWIL test of ML-enabled control loop tuning on BST S2 platform

---

## Risk Management

### Risk 1: Integration Complexity
**Issue:** New messaging protocols and layered interfaces may introduce latency or interoperability issues
**Mitigation:** Rigorous HIL testing and simulation environments before flight testing

### Risk 2: Legacy System Adaptation
**Issue:** Updating SwiftCore may cause unforeseen compatibility issues with existing components
**Mitigation:** Incremental software updates with iterative testing, version control, and traceability tools

### Risk 3: Experimental Module Safety
**Issue:** External ML-based modules might generate unsafe control commands
**Mitigation:** Robust safe sandbox with predefined safety thresholds and override logic; extensive bench and simulation tests

### Risk 4: ML Algorithm Tuning Accuracy
**Issue:** ML-based tuning may produce suboptimal adjustments affecting flight performance
**Mitigation:** Train using historical flight data; incremental testing in simulation; conservative thresholds for safe operations

---

## Related Prior Work & Background

### Previous NASA SBIR Projects
- **Phase II Predictive Maintenance:** Successfully integrated ML algorithms within SwiftCore to monitor aircraft health parameters in real-time, anticipating failures before occurrence
- **Machine Vision Emergency Landing System:** Implemented deep learning to rapidly assess terrain and autonomously generate "go/no-go" landing maps; validated in simulated engine-out emergencies
- **GPS-Denied Navigation:** Developed vision-augmented navigation using signals of opportunity (radio, cellular, ADS-B); validated in field tests with improved position accuracy in GPS-denied environments

### NOAA Partnership
- **Hurricane Observation Missions:** SwiftCore-equipped BST S0 autonomously navigated hurricane eyewalls and inflow regions with comprehensive real-time data collection
- Validated performance in extreme weather conditions

### Previous Deployments
- VORTEX2 project: First-ever interc