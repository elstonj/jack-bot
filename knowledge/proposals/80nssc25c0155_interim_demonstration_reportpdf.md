# Adaptive and Secure Autonomy for UAS: A Modular Approach to Flight Control, Machine Learning Integration, and Multi-Vehicle Coordination

## Document Metadata
- **Type:** Phase I Interim Demonstration Report (SBIR)
- **Client/Agency:** NASA (Subtopic A2.02: Enabling Aircraft Autonomy)
- **Program/Solicitation:** NASA SBIR, Contract 80NSSC25C0155
- **Date:** December 2025 (awarded 9/29/2025)
- **BST Products/Systems Referenced:** SwiftCore Flight Management System (FMS), BST S2 aircraft platform
- **Key Personnel:** Dr. Jack Elston (Principal Investigator)

---

## Executive Summary

Black Swift Technologies has completed Phase I work on a modular, two-tier autonomy architecture for the SwiftCore Flight Management System. The system separates deterministic, real-time flight control on an STM32-based microcontroller (MCU) tier from experimental autonomy capabilities running on a Linux-based single-board computer (SBC) tier. The architecture implements standardized pub/sub messaging, WebAssembly sandboxing for experimental modules, and a supervisory safety system that automatically overrides unsafe commands, enabling rapid integration of machine learning and advanced autonomy without compromising certified flight safety.

---

## Technical Approach

### Architecture Overview

**Two-Tier Design:**
1. **MCU Tier (Real-Time Flight Control):**
   - STM32F4/F1 microcontrollers running FreeRTOS
   - 1 kHz control loop execution
   - Hard real-time sensor acquisition, state estimation, and control
   - CAN bus interconnecting independent hardware nodes (sensors, actuators, control functions)
   - Publisher-subscriber messaging on CAN bus
   - Embedded health arbiter that evaluates all external commands before admitting to control pipeline

2. **SBC Tier (Higher-Level Autonomy):**
   - Linux-based flight computer (e.g., Raspberry Pi Zero 2 W running BalenaOS or NixOS)
   - Non-real-time autonomy services and modules
   - Containerized native executables for trusted/performance-critical logic
   - WebAssembly (WASM) sandboxed modules for experimental algorithms
   - NNG-based pub/sub message bus (SwiftBus)
   - Supervisory module managing module lifecycle, resource limits, and arbitration

### Five Functional Layers (Hierarchical Control)

1. **Multi-vehicle Coordination & Information Gathering** (SBC)—cooperative behaviors, coordinated sensing, mission-level decision-making
2. **Machine Learning & Machine Vision-Based Sensing & Control** (SBC, native or WASM)—perception, learning-based estimation, anomaly detection, adaptive control
3. **Standard Navigation** (Bridge between MCU and SBC)—waypoint management, altitude/speed commands, velocity vectors, trajectory following
4. **Control Loop Modification** (MCU)—PID tuning, TECS-like energy management, ML-enabled in-flight parameter adjustment
5. **Low-Level Sensor & Actuator Interface** (MCU)—direct hardware access to sensors and actuators

### Communication Between Tiers

- **UART Serial Link:** Connects MCU to SBC with binary protocol (BST messaging format)
- **Measured Performance:** <8 ms round-trip latency, 50 Hz state update rate, measured performance <10 ms
- **Protocol:** Lightweight, purpose-built binary format supporting state telemetry, autonomy command requests, safety override signals
- **Safety Monitoring:** All SBC suggestions validated by embedded arbiter before execution

### Key Technical Components

**FreeRTOS RTOS (MCU):**
- Replaces bare-metal architecture with structured, auditable task scheduling
- Preserves ISR-driven sensor acquisition and 1 kHz control timing
- Enables cleaner separation of concerns for new communication and supervisory functions
- Future foundation for CAN-based distributed firmware updates

**NixOS (SBC):**
- Declarative configuration model
- Reproducible builds
- Atomic upgrade and rollback capabilities
- Valuable for safety-critical experimentation and certification traceability

**NNG Pub/Sub Messaging (SBC):**
- Modern successor to nanomsg
- Lightweight C implementation
- Multiple communication patterns
- Avoids ROS 2/DDS overhead for embedded systems

**WebAssembly Sandboxing:**
- WASM runtime (WAMR or WasmEdge) executes experimental autonomy modules
- Strong memory isolation prevents unauthorized hardware access
- Language-agnostic development
- Enforceable resource limits (CPU, memory)
- Modules cannot access system calls, devices, or bypass interfaces

---

## Products & Capabilities Described

### SwiftCore Flight Management System

**What It Is:**
- Flight-proven, NDAA-compliant avionics platform
- ~20 years operational heritage (hurricane observation, volcanic sampling missions for NASA/NOAA)
- Core autopilot for fixed-wing UAS
- Previously developed under NASA SBIR programs

**Proposed Use in This Project:**
- Enhanced with modular autonomy architecture
- Serves as baseline flight control system (MCU tier)
- Interfaces with SBC for advanced autonomy
- Supports ML-enabled control loop tuning
- Foundation for multi-platform support (fixed-wing, VTOL, multirotor)

**Specifications/Claims:**
- STM32F4/F1 microcontroller base
- FreeRTOS real-time scheduler
- CAN bus for sensor/actuator node interconnection
- UART interface to SBC (1-3 Mbps recommended)
- Sensor suite: dynamic/static pressure, temperature, humidity, current/voltage, IMU, GPS, RC receiver
- Deterministic 1 kHz control loop rate
- Independent CAN-connected nodes for sensors, actuators, control functions

### Autonomy Architecture Components

**Embedded Health Arbiter/Supervisor:**
- Evaluates system health: sensor validity, estimator consistency, control loop timing, RC override status, communication health
- Validates all SBC-suggested commands against predefined boundaries (attitude, velocity, geofence limits)
- Automatically rejects unsafe commands or triggers fallback to certified control
- Retains final authority regardless of SBC behavior

**SBC Supervisory Module:**
- Launches and monitors native and WASM autonomy modules
- Enforces CPU and memory resource limits
- Detects stalled or misbehaving modules
- Arbitrates among multiple control input sources (priority-based selection, voting, blending, mode-dependent switching)
- Rate-limits and validates commands before forwarding to MCU tier

**ML Tuning Module (Proof of Concept):**
- Injects calibrated control inputs (doublets) to identify system response
- Analyzes aircraft behavior to recommend PID gain adjustments
- Runs as WASM module or native service on SBC
- Validated by embedded supervisor before applying parameter changes

---

## Use Cases & Applications

### Operational Context
- **Primary Platform:** BST S2 aircraft (flight-proven, certified under previous NASA SBIR)
- **Target Missions:** 
  - Rapid autonomy development and integration
  - Multi-vehicle coordination (fleet operations)
  - Advanced sensing (ML-based vision for landing zone assessment)
  - Adaptive flight control
  - Rapidly evolving operational scenarios: wildfire response, disaster management, BVLOS operations

### Target Customers
- NASA, NOAA, USGS
- Department of Defense
- Commercial operators (aerial survey, infrastructure inspection, agricultural monitoring)

### Key Application Areas Addressed
- Enabling aircraft autonomy (NASA CAS objectives)
- Safe integration of experimental algorithms without full system requalification
- Advanced Air Mobility and autonomous UAS integration into National Airspace System
- Fleet-wide over-the-air updates via BalenaOS

---

## Key Results (Phase I Completion Status)

### Objective 1: Layered Architecture Definition
**Status:** ✓ **Completed**
- Documented five-layer hierarchical autonomy architecture
- Developed binary messaging protocol specification (BST protocol)
- Defined standardized message types for state telemetry, command requests, safety overrides
- Created layer diagrams and software message definitions for three primary functions:
  - System Initialization
  - Mission Planning and Mid-Mission Plan Revision
  - Mission Execution

**Performance Metrics:**
- 50 Hz state update rate
- Round-trip latency <8 ms (measured)
- Protocol supports high-rate sensor updates with low overhead

### Objective 2: SwiftCore System Adaptation
**Status:** ✓ **Completed in Phase I (partial)**

**Achievements:**
- Migrated from bare-metal to FreeRTOS-based execution
- Implemented deterministic task scheduling for sensing, estimation, control, actuation
- Established supervisory arbitration task for system health evaluation
- Developed UART interface for bidirectional MCU-SBC communication
- Documented firmware update architecture for CAN-connected nodes
- Planned support for multi-platform configurations (fixed-wing, VTOL, multirotor)

**Technical Refinements:**
- FreeRTOS task priorities: Sensor Processing (high), Estimator (high), Control (high), Actuator Output (high), System Health/Arbiter (medium), Communications (low)
- DMA-based UART with non-blocking design
- State data copied to preallocated buffers; control loop execution unaffected by UART throughput
- CAN bootloader strategy planned for distributed firmware updates with cryptographic signing

### Objective 3: Safe Sandbox Development
**Status:** ✓ **Completed (benchtop prototype)**

**Achievements:**
- Integrated SwiftCore autopilot with Raspberry Pi Zero 2 W running BalenaOS
- Validated UART-based communication between MCU bridge task and SBC protocol bridge service
- Implemented NNG-based pub/sub message bus on SBC
- Integrated initial supervisor logic
- **Demonstrated safe override:** Commands violating predefined safety thresholds rejected before reaching flight controller

**Testing Validation:**
- Benchtop tests with injected "faulty" commands
- Confirmed supervisor correctly overrides unsafe inputs
- Tested fallback mechanism

### Objective 4: ML-Enabled Control Loop Tuning Demonstration
**Status:** ✓ **Prototype Demonstrated**

**Achievement:**
- Developed proof-of-concept WebAssembly module for in-flight control loop tuning
- Module analyzes aircraft response to injected doublet commands
- Recommends PID gain adjustments
- SBC supervisor validates recommendations before application
- Training and validation using historical flight data

**Operational Model:**
1. ML module injects doublet control input
2. Observes aircraft response
3. Analyzes system identification (e.g., Ziegler-Nichols method, frequency response)
4. Recommends PID gain updates
5. Embedded supervisor validates against safety limits
6. Approved adjustments applied if within certified envelope

---

## Notable Details

### Modular Design Advantages
- **Rapid Algorithm Integration:** Third-party autonomy modules execute in WASM sandboxes; individual modules validated independently without full system requalification
- **Hot-Swappable Components:** CAN-bus-connected nodes can be independently replaced
- **Fleet Updates:** BalenaOS supports fleet-wide over-the-air updates
- **Certification Path:** Clean separation between certified control laws and experimental modules reduces validation burden

### Safety Architecture
- **Dual-Supervisor Model:** 
  - Embedded arbiter (MCU tier) retains final authority
  - SBC supervisor manages module lifecycle and arbitrates among suggestions
  - Layered safety prevents unsafe experimental behavior from propagating downward
- **Fallback Mechanisms:** RC/handheld emergency override, automatic revert to certified control on link loss or unsafe command
- **Watchdog & Heartbeat Monitoring:** FreeRTOS-based framework for detecting stalled or missing updates

### NDAA Compliance
- SwiftCore platform verified as NDAA-compliant (no Chinese components/design)
- Supports U.S. government and defense operations

### Innovation vs. Prior Art
- **Monolithic Systems Problem:** Conventional UAS tightly couple sensors, actuators, and algorithms, requiring extensive modifications for new capabilities
- **SwiftCore Solution:** Publisher-subscriber architecture with independent node interconnection allows capability additions with minimal system-wide revalidation

### Future Directions (Phase II Planning)
- Full flight validation of modular architecture
- Advanced ML integration (vision-based landing zone assessment, cooperative multi-UAS coordination)
- Extended control law adaptation
- Distributed firmware update mechanism across CAN network
- Security hardening (cryptographic signing, session