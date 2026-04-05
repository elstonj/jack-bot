# 2025-12-31 Interim Demonstration Report

## Document Metadata
- **Type:** Interim Progress Report (Phase I, SBIR)
- **Client/Agency:** NASA (Marshall Space Flight Center)
- **Program/Solicitation:** SBIR Subtopic A2.02 - Enabling Aircraft Autonomy
- **Contract Number:** 80NSSC25C0155
- **Date:** December 2025 (Award date: September 29, 2025)
- **BST Products/Systems Referenced:** SwiftCore, S2 (flight test platform), SwiftBus
- **Key Personnel:** Dr. Jack Elston (Principal Investigator)

---

## Executive Summary

Black Swift Technologies reports completion of Phase I interim milestones for the development of a modular, adaptive autonomy architecture built on SwiftCore, an NDAA-compliant flight management system. The project proposes a two-tier system separating deterministic flight control (STM32F4/F1 MCU tier running FreeRTOS) from sandboxed autonomy modules (SBC tier running NixOS/BalenaOS). The team has successfully defined the layered architecture, demonstrated a benchtop prototype integrating SwiftCore with Raspberry Pi Zero 2 W, validated binary protocol bridging, and tested initial supervisor safety logic. The innovation addresses NASA's need for modular, rapidly reconfigurable autonomy platforms that reduce certification burden by isolating experimental code in WebAssembly sandboxes with enforced safety boundaries.

---

## Technical Approach

**Modular Two-Tier Architecture:**
- **MCU Tier (Embedded):** STM32F4/F1 microcontrollers running FreeRTOS at 1kHz loop rates provide hard real-time flight control. Independent hardware nodes communicate over CAN bus using publisher-subscriber messaging, enabling hot-swappable components.
- **SBC Tier (Autonomy):** Linux-based flight computer (NixOS/BalenaOS) hosts containerized services and WebAssembly-sandboxed autonomy modules. State data from embedded controller published over UART (binary protocol, <10ms round-trip latency at 50Hz).

**Key Technical Components:**

1. **FreeRTOS Implementation (MCU):** Preserves existing SwiftCore interrupt-driven architecture for sensor acquisition and control loops while introducing disciplined task scheduling. Migrates from bare-metal to RTOS to support modular communications, health arbitration, and supervisory functions without destabilizing proven flight logic.

2. **UART Interface (MCU ↔ SBC):** Implements BST messaging protocol over DMA-driven serial I/O. Embedded system publishes filtered sensor data, state estimates, and system health at fixed rates (50Hz nominal). SBC sends suggested control/actuator commands; embedded arbiter validates all inputs before admission to control pipeline. Latency budget: <10ms round-trip.

3. **NixOS/BalenaOS (SBC):** Selected for reproducible deployments, atomic updates with rollback, and declarative configuration. Enables consistent fleet management and controlled remote updates with security controls.

4. **NNG Messaging Layer (SBC):** Pub/sub message bus implementing SwiftBus. Chosen over DDS for lightweight, auditable messaging without complex discovery overhead. Supports sensor data, state, control requests, and actuator commands.

5. **WebAssembly Sandboxing:** WASM containers (WAMR or WasmEdge) host experimental autonomy modules with memory isolation and enforceable resource limits. Modules cannot access system calls, devices, or other modules except through exposed interfaces.

6. **Supervisor Service (SBC):** Enforces safety envelopes by validating all autonomy module outputs against predefined attitude, velocity, and geofence limits before forwarding to embedded arbiter. Manages module lifecycle, CPU/memory allocation, and detects stalled/misbehaving components.

**Five-Layer Functional Decomposition:**
1. Multi-vehicle coordination and information gathering (SBC)
2. Machine learning and machine vision sensing/control (SBC, native or WASM)
3. Standard navigation (waypoint tracking, altitude/speed commands) (Hybrid)
4. Control loop modification (PID tuning, TECS algorithms) (MCU with ML suggestions from SBC)
5. Low-level sensor and actuator interface (MCU)

---

## Products & Capabilities Described

### SwiftCore Flight Management System
- **What it is:** NDAA-compliant, flight-proven avionics platform with ~20 years of operational heritage (hurricane observation, volcanic sampling for NASA/NOAA).
- **How used in this context:** Core embedded flight control layer running on STM32F4/F1 microcontroller. Provides real-time sensing, estimation, control, and actuation with deterministic 1kHz loop rates. Interfaces with SBC via UART for state publication and command arbitration.
- **Specifications:** 
  - Real-time execution on FreeRTOS
  - CAN bus interconnect for sensor/actuator nodes
  - Hard real-time interrupt handling with ISRs managing high-rate IMU, pressure, temperature, electrical, GPS sensors
  - Actuator interfaces for aerodynamic control surfaces and propulsion
  - Embedded health arbiter with RC emergency takeover receiver
  - Message latency <10ms round-trip (50Hz update rate)

### S2 (Flight Test Platform)
- **What it is:** BST's fixed-wing UAS platform, previously developed and certified under NASA SBIR projects.
- **How used:** Primary flight test vehicle for demonstrating ML-enabled control loop tuning and validating architecture feasibility in actual flight conditions.

### SwiftBus
- **What it is:** NNG-based pub/sub messaging environment on SBC.
- **How used:** Central message routing between autonomy modules, enabling topic-based subscription without tight coupling.

---

## Use Cases & Applications

1. **ML-Enabled In-Flight Control Loop Tuning:**
   - WASM or native ML module analyzes aircraft response to injected doublet control inputs
   - Recommends optimal PID gain adjustments
   - Supervisor validates recommendations against safe limits before application
   - Enables aircraft to maintain optimal performance under varying flight conditions

2. **Multi-Vehicle Coordination:**
   - SBC-hosted coordination logic aggregates fleet-wide information
   - Proposes cooperative behaviors (formation flight, coordinated sensing, task allocation)
   - Transmitted as navigation/control suggestions through supervisor to embedded arbiter

3. **Rapid Autonomy Development & Integration:**
   - Experimental autonomy modules (computer vision, adaptive estimators, anomaly detection) deployed as WASM sandboxes without full system revalidation
   - Safe fallback to certified SwiftCore control if experimental modules fail or exceed safety thresholds
   - Individual modules independently validated without system-wide certification burden

4. **Mission Applications (Proposed):**
   - Wildfire response
   - Disaster management
   - BVLOS operations
   - Beyond Visual Line-of-Sight (BVLOS) National Airspace System integration

---

## Key Results (Phase I Interim)

### Completed Milestones:

**Objective 1: Layered Architecture Definition** ✓ COMPLETE
- Defined two-tier hierarchical architecture with five functional layers
- Developed binary messaging protocol specification with standardized message types
- Designed pub/sub framework for layer-to-layer communication
- Specified safety supervisor logic and override protocols
- Documented message definitions for system initialization, mission planning, mission execution functions

**Objective 2: SwiftCore System Adaptation** ✓ COMPLETE
- Successfully migrated from bare-metal to FreeRTOS-based execution model
- Implemented UART bidirectional bridge with BST protocol framing, DMA I/O, <10ms latency
- Integrated NixOS/BalenaOS SBC infrastructure
- Deployed NNG-based pub/sub messaging layer
- Implemented WebAssembly container support with resource isolation
- Preserved proven interrupt-driven sensor acquisition and validated control algorithms

**Objective 3: Safe Sandbox Development** ✓ PARTIALLY COMPLETE (Benchtop Validation)
- Developed supervisor safety framework with predefined attitude, velocity, geofence thresholds
- Implemented command validation logic in embedded arbiter
- Successfully tested override mechanisms in benchtop integration
- Confirmed fallback to certified control when experimental module outputs exceed limits
- HIL testing environment prepared; flight validation planned for Phase II

**Objective 4: ML-Enabled Control Loop Tuning Demonstration** ✓ BENCHTOP PROTOTYPE COMPLETE
- Developed proof-of-concept ML module for PID tuning via doublet injection
- Implemented control loop response analysis algorithm in WASM
- Demonstrated supervisor validation of recommended PID adjustments
- ML module successfully integrated with benchtop SwiftCore/SBC prototype
- Flight test data collection preparation underway for Phase II

### Benchtop Integration Results:
- Raspberry Pi Zero 2 W successfully integrated with SwiftCore autopilot
- UART bridge validated with measured round-trip communication latency <8ms
- NNG pub/sub message routing confirmed functional
- Safety supervisor correctly rejected out-of-bounds experimental commands
- System demonstrated graceful fallback to certified control
- Simulation environment (hardware-in-the-loop) validated layer interactions

### Technical Specifications Validated:
- 50Hz state update rate maintained with <10ms latency
- FreeRTOS task prioritization ensures 1kHz flight control loop execution
- WASM module memory isolation prevents cross-module interference
- DMA-driven serial I/O eliminates control-loop blocking on UART operations

---

## Notable Details

### Innovation & Competitive Advantages:
- **Modular Autonomy without Certification Burden:** WebAssembly sandboxing with enforced safety boundaries allows third-party experimental modules to execute without requiring full system revalidation. Supervisor-enforced safety envelopes enable rapid technology integration.
- **Flight-Proven Foundation:** SwiftCore's ~20 years of operational heritage (hurricane observation, volcanic sampling) provides proven baseline for safety-critical operations.
- **NDAA Compliance:** System meets Department of Defense National Defense Authorization Act requirements, critical for government operations.
- **Safety-First Layering:** Mirrors aerospace best practices (NASA autonomy layering principles) with dual supervisors (SBC + embedded) ensuring experimental code cannot bypass certified control.

### Subcontractor/Partnership Status:
- No subcontractors mentioned; all work conducted internally at BST Boulder facility.

### Risk Mitigation Status:
1. **Integration Complexity:** Addressed through rigorous HIL testing and simulation validation. Benchtop prototype confirms feasibility.
2. **Legacy System Adaptation:** Minimized through incremental refactoring approach; FreeRTOS conversion preserves existing interrupt drivers and validated control algorithms.
3. **Experimental Module Safety:** Supervisor override logic tested and validated. Safety thresholds established and enforced.
4. **ML Algorithm Accuracy:** Historical flight data available for training. Conservative thresholds established. Simulation validation completed; flight testing scheduled for Phase II.

### Certification & Compliance:
- Project designed to align with NASA CAS (Convergent Aeronautics Solutions) objectives
- Modular approach reduces certification overhead compared to monolithic systems
- SBIR intellectual property protection: 20-year government use period from award date (9/29/2025), with disclosure restrictions through 2045 unless permitted

### Next Steps (Phase II):
- Flight test validation of ML-enabled control loop tuning on BST S2
- Expanded hardware platform support (fixed-wing, VTOL, multirotor configurations)
- Multi-vehicle coordination demonstrations
- Enhanced computer vision and perception module integration
- Hardened security controls for remote update mechanisms
- Commercial path development for government and commercial markets

### Facility & Resources:
- BST development facility: Boulder, CO (simulation hardware, autopilot bench test rigs, computing infrastructure)
- Hardware: Raspberry Pi Zero 2 W for SBC tier, STM32F4/F1 for MCU tier, CAN bus interconnect
- Software: FreeRTOS, NixOS/BalenaOS, NNG, WAMR/WasmEdge, BST SDK

---

## Significance to NASA

The proposed architecture directly addresses NASA SBIR Subtopic A2.02 barriers:
- **Cognition & Multi-Objective Decision-Making:** ML and autonomy modules can execute at SBC tier with supervisor-enforced objectives.
- **Fault Tolerance:** Dual-layer supervision (SBC + embedded arbiter) with automatic fallback to certified control.
- **Resilient Communications:** UART bridge with bounded latency; CAN bus redundancy at node level.
- **Streamlined Validation & Certification:** Modular validation reduces certification burden; WASM