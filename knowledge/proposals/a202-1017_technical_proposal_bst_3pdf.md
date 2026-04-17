# Adaptive and Secure Autonomy for UAS: A Modular Approach to Flight Control, Machine Learning Integration, and Multi-Vehicle Coordination

## Document Metadata
- **Type:** NASA SBIR Phase I Technical Proposal
- **Client/Agency:** NASA (Aeronautics Research Mission Directorate - ARMD)
- **Program/Solicitation:** NASA SBIR Subtopic A2.02: Enabling Aircraft Autonomy; ProSAMS Proposal Number A2.02-1017
- **Date:** 2026 (submitted; document created/modified 2026-04-16)
- **BST Products/Systems Referenced:** SwiftCore Flight Management System, BST S2 UAS, NDAA-compliant flight computers
- **Key Personnel:** 
  - Dr. Jack S. Elston (Principal Investigator, CEO/co-founder of BST)
  - Dr. Maciej Stachura (Lead Control and Estimation Engineer, CTO of BST)
  - Ben Busby (Lead Software Engineer)

---

## Executive Summary

Black Swift Technologies proposes to develop and validate a modular, layered architecture for the SwiftCore Flight Management System that enables rapid integration of advanced autonomy capabilities into uncrewed aircraft systems (UAS). The innovation centers on a fully modular hardware and software architecture using publisher-subscriber (pub/sub) messaging and service discovery, combined with a "safe sandbox" environment for testing experimental ML-based controllers without compromising flight safety. This addresses NASA's critical barriers to aircraft autonomy including cognition, multi-objective decision-making, resilient communications, fault tolerance, and rapid validation/certification.

---

## Technical Approach

### Core Innovation: SwiftCore Flight Management System

**Modular, Layered Architecture:**
- Hierarchical system with five functional layers:
  1. Multi-vehicle coordination and information gathering
  2. Machine learning and machine vision–based sensing and control
  3. Standard navigation (waypoint management, altitude/speed commands, velocity vectors)
  4. Control loop modification (dynamic PID tuning via TECS-like algorithms)
  5. Low-level sensor acquisition and actuator control

**Key Technical Features:**
- Independent, intelligent hardware nodes interconnected via open, message-based pub/sub communication framework with service discovery
- Standardized message types and inter-layer communication interfaces
- Hot-swappable components (actuators, sensors, autopilots, flight computers)
- Embedded containerization (inspired by Wind River solutions) for security, isolation, and portability
- Real-time, high-bandwidth communication bus for standardized inter-layer messaging

**Safe Sandbox Environment:**
- Supervisory controller continuously monitors commands from experimental (non-certified) modules
- Automatic override mechanism reverts to certified, flight-proven control system if unsafe conditions detected
- Predefined safety thresholds based on system state
- Enables rapid iteration on complex algorithms while maintaining absolute confidence in safety and mission integrity

**State-of-the-Art Comparison:**
- Departs from conventional monolithic, tightly-coupled UAS avionics architectures
- Enables modular integration vs. conventional systems requiring extensive system-wide modifications and lengthy revalidation
- Eliminates need for complete system re-certification when components change through containerization and standardized interfaces
- Dramatically streamlines development, test, and validation processes

### Flight-Proven Foundation
- Nearly 20 years of operational experience with SwiftCore-based systems
- Completed 9 NASA Airworthiness Flight Safety Review Boards (AFSRB) and Flight Readiness Review Boards (FRRB)
- First company to successfully complete NASA's new Unmanned Commercial Aviation Services (UCAS) review
- NDAA-compliant systems with proven performance in critical missions

---

## Products & Capabilities Described

### SwiftCore Flight Management System
**What it is:**
- Flight-proven, NDAA-compliant avionics platform specifically engineered for advanced autonomy development, testing, and integration
- Modular architecture replacing conventional monolithic designs
- Enables rapid technology infusion, robust fault tolerance, and simplified certification

**Proposed Use in This Context:**
- Serve as the foundation for modular autonomy architecture supporting machine learning integration
- Enable multi-vehicle coordination and advanced sensing/control layers
- Support ML-based control loop tuning and emergency landing systems
- Facilitate rapid integration of experimental controllers through safe sandbox approach

**Key Specifications/Performance Claims:**
- Supports multiple aircraft configurations (fixed-wing, VTOL, multirotor) with minimal interface changes
- Proven in hazardous environments (hurricanes, volcanic gas sampling, severe weather)
- Hardware-in-the-loop (HIL) testing and simulation capabilities
- Real-time machine learning algorithm execution
- Proven fault detection and predictive maintenance capabilities

### ML-Enabled Single Board Computer (SBC)
**What it is:**
- New NDAA-compliant ML-enabled compute node to be integrated
- American-made to meet federal regulations and NDAA standards
- Provides computational acceleration (FPGA-based processing) and dedicated ML support

**How it's Used:**
- Installed as parallel "sandbox" controller within avionics rack
- Interfaced with SwiftCore via standardized pub/sub messaging over CAN bus
- Executes advanced machine learning algorithms for vision-based obstacle avoidance, predictive maintenance, and control loop adaptation
- Outputs monitored and overridden by certified SwiftCore system to ensure safety

---

## Use Cases & Applications

### Previous/Demonstrated Applications
1. **Predictive Maintenance (NASA Phase II SBIR):** ML techniques integrated within SwiftCore to monitor aircraft health parameters in real-time, anticipate failures, and generate timely maintenance alerts

2. **Emergency Landing Systems:** Deep learning-based terrain assessment for autonomous identification of safe landing zones during simulated engine-out emergencies; categorizes terrain features (trees, water, buildings, roads) to generate "go/no-go" landing maps

3. **GPS-Denied Navigation (NOAA-funded):** Machine vision combined with "signals of opportunity" (radio signals, cellular, ADS-B broadcasts) for robust, vision-augmented navigation in GPS-denied/jammed environments

4. **Hurricane Observation (NOAA/2024):** Autonomous navigation of hurricane eyewalls and inflow regions using three observational models (center fix determination, maximum wind speed measurement, inflow characterization); validated during 2024 hurricane season with multiple successful flights

5. **Volcanic Gas Sampling (BVLOS):** Demonstrated autonomous operations in hazardous environments (Makushin Volcano); shows capability for beyond visual line-of-sight missions in dynamic environments

6. **Icing Detection:** ML methods to detect ice accumulation on aircraft wings during flight

7. **Severe Weather Sampling:** Multi-aircraft cooperative operations, including VORTEX2 project (first-ever intercept of tornadic supercell thunderstorm by uncrewed aircraft); vertically stacked formation flight through gust fronts

### Proposed Phase I Demonstrations
- ML-enabled in-flight control loop tuning on BST S2 platform using calibrated control inputs (doublets) and real-time response analysis
- Bench and HIL tests validating safe sandbox override mechanisms
- Simulation-based validation of layer-to-layer interactions

### Target Mission Areas
- Remote sensing
- Wildfire response
- Goods delivery
- Disaster management
- Environmental monitoring
- Beyond visual line-of-sight (BVLOS) operations
- Multi-vehicle coordinated missions
- Advanced Air Mobility (AAM) applications

---

## Technical Objectives & Work Plan

### Phase I Technical Objectives

**Objective 1: Layered Architecture Definition**
- Define and document modular, multi-layer sensing and control architecture spanning from high-level multi-vehicle coordination through low-level sensor/actuator interfaces
- Develop standardized pub/sub messaging protocol specification
- Create hardware-in-the-loop simulation models demonstrating layer-to-layer interactions
- Deliverables: Architecture documents, flow diagrams, messaging protocol specifications, simulation models

**Objective 2: SwiftCore System Adaptation**
- Update and refine existing SwiftCore FMS based on 20 years of flight experience and new NASA CAS requirements
- Modify firmware and software to support new messaging interfaces and multi-platform support (fixed-wing, VTOL, multirotor)
- Enable rapid adaptation with minimal interface changes
- Deliverables: Updated software interfaces, hardware configurations, documentation of reconfiguration methods, demonstration flight test reports

**Objective 3: Safe Sandbox Development**
- Develop framework allowing external, experimental controllers (e.g., ML-based modules) to be integrated without compromising flight safety
- Define safety thresholds and override protocols based on system state
- Implement supervisory controller continuously monitoring experimental module commands
- Deliverables: Prototype safe sandbox module, documentation of safety thresholds/override logic, simulation and HIL test results

**Objective 4: ML-Enabled Control Loop Tuning Demonstration**
- Demonstrate proof-of-concept for machine learning–enabled, in-flight tuning of control loops
- Inject specific control inputs (e.g., doublets) to automatically tune PID controllers
- Ensure optimal performance under varying conditions
- Deliverables: Prototype ML module, flight test data, final report with performance metrics and lessons learned

### Work Plan Tasks

**Task 1: Layered Architecture Definition & Messaging Protocol Specification (Month 1)**
- Conduct design review meetings with controls, firmware, and software teams
- Use UML modeling tools for detailed architecture diagrams
- Develop prototype message libraries (leveraging UAVCAN as reference)
- Validate messaging interoperability using bench tests with representative nodes
- Milestone: Completion of detailed architecture definition document and messaging protocol specifications

**Task 2: SwiftCore System Adaptation and Update (Months 1-4)**
- Review existing SwiftCore implementation and identify needed updates
- Modify firmware and software for new messaging interfaces and multi-platform support
- Update control algorithms to interface with messaging framework
- Methods: Version control (git/trac), software-in-the-loop (SWIL) simulation, internal digital twin environment
- Milestone: Successful bench testing of newly defined messaging protocol between prototype nodes

**Task 3: Safe Sandbox Development (Months 2-5)**
- Develop "safe sandbox" framework for experimental external control modules
- Define safety thresholds and override protocols
- Implement supervisory controller with continuous monitoring
- Methods: Simulation of flight scenarios with edge cases, development of intermediary software module, controlled bench tests with injected faulty commands
- Milestone: Safe sandbox module prototype completed and validated in controlled bench tests

**Task 4: ML-Enabled Control Loop Tuning Demonstration (Months 3-6)**
- Develop proof-of-concept ML module for automatic control loop tuning via calibrated control inputs
- Integrate ML module on NDAA-compliant flight computer board within SwiftCore
- Demonstrate in simulation and on BST S2 platform
- Methods: Collect historical flight data for training, supervised learning framework, iterative validation, bench tests with simulated perturbations, flight tests
- Milestone: Demonstration HWIL test of ML-enabled control loop tuning on BST S2 platform

**Task 5: Integration, HIL Simulation**
- Comprehensive system integration testing
- Hardware-in-the-loop validation across all layers

**Task 6: Final Documentation, Reporting**
- Deliverables and customer portal access

### Resource Allocation
| Task | Dr. Jack Elston (PI) | Dr. Maciej Stachura | Ben Busby | Total Hours |
|------|---------------------|-------------------|-----------|------------|
| 1. Layered architecture | 50 | 40 | 30 | 120 |
| 2. SwiftCore adaptation | 40 | 40 | 40 | 120 |
| 3. Safe sandbox development | 30 | 40 | 80 | 150 |
| 4. ML control loop tuning | 40 | 40 | 80 | 160 |
| 5. Integration, HIL sim | 30 | 30 | 40 | 100 |
| 6. Documentation, reporting | 20 | 20 | 30 | 70 |
| **Total** | **210** | **210** | **300** | **720** |

### Risk Mitigation Strategy

| Risk | Mitigation |
|------|-----------|
| Integration Complexity: New messaging protocols may introduce latency/interoperability issues | Rigorous HIL testing and simulation environments before flight testing |
| Legacy System Adaptation: Updates may cause compatibility issues | Incremental software updates, iterative testing, extensive version control and traceability |
| Experimental Module Safety: ML modules might generate unsafe commands | Robust safe sandbox with predefined thresholds; extensive bench and simulation testing of fallback mechanism |
| ML Algorithm Accuracy