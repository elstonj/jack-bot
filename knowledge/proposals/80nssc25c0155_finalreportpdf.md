# Adaptive and Secure Autonomy for UAS: A Modular Approach to Flight Control, Machine Learning Integration, and Multi-Vehicle Coordination

## Document Metadata
- Type: NASA SBIR Phase I Final Report
- Client/Agency: NASA
- Program/Solicitation: SBIR Subtopic A2.02 – Enabling Aircraft Autonomy; Contract 80NSSC25C0155
- Date: March 2026 (Award date: September 29, 2025)
- BST Products/Systems Referenced: SwiftCore Flight Management System, S2 aircraft platform
- Key Personnel: Dr. Jack Elston (PI/CEO), Dr. Maciej Stachura (CTO), Ben Busby (Lead Software Engineer)

## Executive Summary
Black Swift Technologies has successfully completed Phase I of a NASA SBIR contract to develop a modular, layered autonomy architecture for the SwiftCore Flight Management System. The project demonstrates a novel approach that cleanly separates deterministic flight-critical control (on an STM32-based MCU tier) from experimental autonomy modules (on a Linux/NixOS-based SBC tier), enabling rapid technology integration while maintaining safety through WebAssembly sandboxing and supervisory override mechanisms. Phase I work validated the architecture's feasibility through benchtop demonstrations showing <8ms round-trip latency, successful message routing, and safe integration of ML-based experimental controllers.

## Technical Approach

### Core Architecture
SwiftCore employs a two-tier modular architecture:

**MCU Tier (Safety-Critical):**
- STM32F4/F1 microcontrollers running FreeRTOS
- Delivers hard real-time flight control at 1kHz loop rates
- Independent hardware nodes for sensors, actuators, and control functions
- CAN bus with publisher-subscriber messaging framework
- Allows individual hot-swapping of components without system-wide modifications
- Deterministic sensor acquisition, state estimation, control law execution, and actuation

**SBC Tier (Non-Real-Time Autonomy):**
- NixOS on Linux-based flight computer (validated on Raspberry Pi Zero 2 W)
- Containerized autonomy services
- WebAssembly-sandboxed experimental modules
- NNG (nanomsg next generation) pub/sub message bus for module communication
- Service discovery and module lifecycle management

**Inter-Tier Communication:**
- Purpose-built binary protocol over UART
- Measured round-trip latency: <8ms at 50Hz state updates
- Enables real-time supervisory and adaptive control functions

### Five Functional Layers
1. Multi-vehicle coordination and information gathering
2. Machine learning and machine vision-based sensing and control
3. Standard navigation (waypoint tracking, altitude/speed commands, velocity vectors)
4. Control loop modification (PID tuning, TECS-like algorithms)
5. Low-level sensor and actuator interface

### Safety Model
- Dedicated embedded supervisory and arbitration task continuously evaluates system health
- Supervisor monitors all commands from external/experimental modules against predefined safety thresholds (attitude, velocity, geofence limits)
- Automatic fallback to certified control modes if experimental modules exceed boundaries or fail heartbeat
- SBC-level supervisor operates within bounds enforced by embedded arbiter (advisory only, no ultimate authority)
- Layered safety architecture mirrors aerospace standards (e.g., NASA autonomy layering principles)

## Products & Capabilities Described

### SwiftCore Flight Management System
- **What it is:** Flight-proven, NDAA-compliant avionics platform with ~20 years of operational heritage
- **Heritage:** Used in hurricane observation and volcanic sampling missions for NASA and NOAA
- **Proposed use:** Foundational platform for modular autonomy framework; MCU tier provides certified flight control
- **Key specifications:**
  - STM32-based MCU tier with FreeRTOS scheduler
  - Directly interfaces with diverse sensor suite: dynamic/static pressure, temperature/humidity, current/voltage monitors, IMU (angular rates, accelerations, magnetic field), GPS position/velocity, RC emergency takeover receiver
  - 1kHz control loop rates (deterministic execution)
  - 50Hz state publication to SBC tier
  - CAN bus interconnect with pub/sub messaging
  - Supports multiple aircraft configurations: fixed-wing, VTOL, multirotor

### NixOS Operating System
- **What it is:** Declarative Linux distribution selected for SBC tier
- **Rationale:** Reproducible builds, atomic upgrades/rollbacks, fleet-wide over-the-air update capability, certification traceability
- **Use:** Base OS for autonomy services and experimental module execution

### NNG (nanomsg next generation)
- **What it is:** Lightweight C-based pub/sub messaging library
- **Use:** SwiftBus—local publish-subscribe environment on SBC for message routing between autonomy modules
- **Advantages:** Low overhead, multiple communication patterns, suitable for embedded/multi-process systems without ROS 2 or DDS overhead

### WebAssembly (WASM) Sandbox
- **What it is:** Memory-isolated execution environment for untrusted autonomy code
- **Runtimes tested:** WAMR (WebAssembly Micro Runtime), WasmEdge
- **Use:** Host experimental, third-party, or rapidly-iterated autonomy logic without compromising flight-critical systems
- **Benefits:** Language-agnostic development, enforceable resource limits, strong memory isolation; modules cannot access system calls, devices, or other modules except through explicitly exposed interfaces

## Use Cases & Applications

### NASA Applications
- Advanced Air Mobility (AAM) development and testing
- Sense-and-avoid (SAA) and detect-and-avoid (DAA) algorithm evaluation
- Terrain and obstacle avoidance systems
- Beyond visual line-of-sight (BVLOS) operations
- Computer vision applications
- Advanced flight control system development
- Rapid evaluation framework for third-party autonomous components
- Wildfire response, disaster management missions

### Non-NASA and Commercial Applications
- Aerial survey companies
- Agricultural monitoring firms
- Infrastructure inspection services
- UAS OEM integration partners
- Academic research institutions
- Commercial operators in environmental monitoring, emergency response, infrastructure inspection, precision agriculture
- Defense and Department of State applications

## Key Results

### Phase I Technical Accomplishments

**Task 1 – Layered Architecture Definition:**
- Implemented two-tier architecture separating deterministic flight control (MCU) from sandboxed autonomy (SBC)
- Developed standardized binary messaging protocol with <10ms round-trip latency
- Designed 5 explicit functional layers with documented interfaces
- Created detailed UML diagrams and flow diagrams of layered architecture
- Developed message type specifications for pub/sub communications and service discovery

**Task 2 – SwiftCore System Adaptation:**
- Updated firmware and software to support new messaging interfaces
- Added configuration options for multi-platform support (fixed-wing, VTOL, multirotor)
- Modified control algorithms to interface with new messaging framework
- Used software-in-the-loop (SWIL) simulation to validate changes
- Validated performance under various flight conditions using digital twin environment

**Task 3 – Safe Sandbox Development:**
- Developed "safe sandbox" framework allowing external experimental control modules without compromising safety
- Defined safety thresholds and override protocols based on system state
- Implemented supervisory controller continuously monitoring incoming commands
- Benchtop validation: injected "faulty" commands confirmed correct override behavior
- System validates all commands against predefined attitude, velocity, and geofence limits

**Task 4 – ML-Enabled Control Loop Tuning Demonstration:**
- Developed proof-of-concept ML module for automatic control loop tuning
- Implemented altitude control demonstration using WebAssembly module
- ML module provides vertical rate command based on above-ground-level altitude
- Supervisor validates conformance with safe altitude threshold before application
- Demonstrated feasibility of in-flight tuning in simulation environment

### Benchtop Demonstration Results
- Successfully integrated SwiftCore autopilot with Raspberry Pi Zero 2 W running NixOS
- End-to-end operation of modular autonomy framework validated
- Reliable UART-based communication between MCU and SBC layers achieved
- NNG-based pub/sub message routing between autonomy modules confirmed operational
- Supervisory safety enforcement validated: experimental control inputs successfully monitored and rejected when exceeding predefined safety thresholds
- Confirmed system can safely incorporate non-deterministic autonomy algorithms without compromising flight-critical control
- Measured latency performance: 50Hz state updates with <8ms round-trip latency (meeting <10ms requirement)

## Notable Details

### Operational Heritage
- SwiftCore has nearly 20 years of flight experience
- Used in hurricane observation missions
- Deployed in volcanic sampling missions for NASA and NOAA
- Hundreds of flight experiments conducted including Arctic deployments
- Over 100 COA (Certificate of Authorization) applications authored by BST personnel

### Technical Team Expertise
- Dr. Elston: 4 different UAS systems developed, all avionics work technical lead
- Dr. Stachura: 300+ flight experiments, 140+ FAA COAs maintained, completed NASA AFSRB and Flight Readiness Review processes, doctoral work in cooperative multi-UAS control
- Ben Busby: Lead developer of Android tablet flight control, web-based tools, flight log parsing, live video streaming

### Project Management & Delivery
- 6-month Phase I period (award date 9/29/2025, report date 3/27/2026)
- Total project labor: 720 hours across three key personnel
- Four key milestones: (1) Month 1 - architecture & messaging specs, (2) Month 2 - messaging protocol bench tests, (3) Month 3 - safe sandbox prototype validation, (4) Month 6 - HWIL ML-enabled control loop tuning demo

### Commercialization Strategy
- TABA (Technical Business Analysis) provider conducted market research covering UAS autonomy, drone software, and mission applications
- Identified potential customers: NASA, NOAA, USGS, DoD, aerial survey, infrastructure inspection, agricultural monitoring companies
- Targeted partnerships: avionics distributors, OEMs, federal agencies (AFIT, Navy/Marine, US Army Corps of Engineers, DOE labs, MIT Lincoln Lab, Johns Hopkins APL, academic institutions)
- Proposed subscription model: continuous updates, maintenance support, centralized flight log database, fleet-wide over-the-air updates
- Industry engagement: participation in events like XPONENTIAL planned

### NASA Alignment
- Directly addresses NASA SBIR Subtopic A2.02 barriers: cognition, multi-objective decision-making, fault tolerance, resilient communications, streamlined validation/certification
- Substantially reduces certification burden through modular safety boundaries; individual modules can be validated independently
- Supports NASA CAS (Convergent Aeronautics Solutions) objectives for modular, reconfigurable autonomy solutions
- Enables Advanced Air Mobility (AAM) development and integration into National Airspace System

### Risk Mitigation
- Integration complexity: Rigorous HIL testing and simulation before flight
- Legacy system compatibility: Incremental software updates with version control and traceability
- Experimental module safety: Robust safe sandbox with predefined thresholds; bench and simulation verification
- ML algorithm accuracy: Historical flight data training, incremental simulation testing, conservative safety thresholds

### Future Development Path
- Phase II planned: expanded hardware-in-the-loop and flight demonstrations, full system validation
- Extended applications: multi-UAS swarm coordination, vision-based landing zone assessment, adaptive control tuning
- Commercial market: position SwiftCore as critical enabling technology for Advanced Air Mobility and autonomous UAS integration