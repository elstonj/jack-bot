# Adaptive and Secure Autonomy for UAS: A Modular Approach to Flight Control, Machine Learning Integration, and Multi-Vehicle Coordination

## Document Metadata
- **Type:** Phase I Final Report (NASA SBIR)
- **Client/Agency:** NASA (Aeronautics Research Mission Directorate)
- **Program/Solicitation:** NASA SBIR Subtopic A2.02: Enabling Aircraft Autonomy
- **Contract Number:** 80NSSC25C0155
- **Award Date:** September 29, 2025
- **Report Date:** March 2026
- **BST Products/Systems Referenced:** SwiftCore Flight Management System, S2 fixed-wing UAS
- **Key Personnel:** Dr. Jack Elston (PI, CEO), Dr. Maciej Stachura (CTO), Ben Busby (Lead Software Engineer)

---

## Executive Summary

Black Swift Technologies proposes a modular, layered autonomy architecture built on SwiftCore, a flight-proven NDAA-compliant avionics platform with nearly 20 years of operational heritage in hurricane observation and volcanic sampling. The architecture separates deterministic flight control (STM32-based MCU tier running FreeRTOS at 1 kHz) from experimental autonomy modules (SBC tier running NixOS on Linux), enabling safe integration of machine learning and third-party algorithms through standardized pub/sub messaging and WebAssembly sandboxing. Phase I successfully demonstrated the architecture feasibility via benchtop prototype, validating sub-8ms latency, safe command override mechanisms, and ML-enabled control loop tuning concepts.

---

## Technical Approach

### Core Architecture

**Two-Tier System Design:**
1. **MCU Tier (Embedded Controller):** STM32F4/F1 microcontroller running FreeRTOS providing hard real-time flight control at 1 kHz loop rates
2. **SBC Tier (Single-Board Computer):** NixOS (Linux-based) hosting containerized services and WebAssembly-sandboxed autonomy modules

**Key Technical Elements:**

- **Deterministic Flight Control:** All real-time sensor acquisition, state estimation, control law execution, and actuation remain on the embedded STM32 layer with strict priority-based FreeRTOS task scheduling
- **Hierarchical Messaging:** 
  - Within MCU tier: Direct interrupt-driven and task-based communication between sensor, estimator, control, and actuator functions
  - Between tiers: UART-based binary protocol at 50 Hz with round-trip latency <8 ms
  - Within SBC tier: NNG (nanomsg successor) pub/sub message bus for modular autonomy services
- **Safety Arbitration:** Embedded supervisor service continuously validates all external command suggestions against predefined safety envelopes (attitude, velocity, geofence limits); automatically reverts to certified fallback control if safety thresholds violated or communication lost
- **Experimental Code Isolation:** WebAssembly (WASM) runtime (WAMR or WasmEdge) enforces memory isolation for third-party or rapidly-iterated algorithms; WASM modules cannot access system calls, devices, or bypass safety constraints
- **Service Discovery & Hot-Swapping:** Publisher-subscriber architecture with standardized message types allows sensor, actuator, and control function nodes to be individually replaced without system-wide modifications

### Five Functional Layers (Software Stack)

1. **Layer 5 (Lowest):** Sensor and actuator hardware interfaces (IMU, pressure, GPS, motor/surface actuators)
2. **Layer 4:** Control loop modification (PID tuning, TECS-like energy management)
3. **Layer 3:** Standard navigation (waypoint tracking, altitude/speed commands, velocity vectors)
4. **Layer 2:** ML and machine vision–based sensing and control
5. **Layer 1 (Highest):** Multi-vehicle coordination and information gathering

Each layer has explicitly defined inputs/outputs via standardized message types; layers communicate exclusively through pub/sub abstraction, enabling independent development and testing.

---

## Products & Capabilities Described

### SwiftCore Flight Management System

**What it is:**
- Flight-proven, NDAA-compliant avionics autopilot platform with ~20 years operational heritage
- Dual-core architecture: embedded real-time controller + SBC for advanced autonomy
- Supports multiple aircraft configurations (fixed-wing, VTOL, multirotor) with minimal interface changes

**How used in this project:**
- Updated from monolithic design to modular, layered architecture
- Integrated with Raspberry Pi Zero 2 W (SBC) running NixOS for benchtop Phase I prototype
- Demonstrated as flight test platform for S2 fixed-wing UAS
- Adapted messaging interfaces to support experimental autonomy modules

**Specifications/Performance Claims:**
- MCU tier: STM32F4/F1 running FreeRTOS, 1 kHz loop rate (deterministic real-time)
- SBC tier: Raspberry Pi Zero 2 W (prototyping), NixOS OS
- Message protocol: Binary UART between tiers, measured latency 50 Hz updates, round-trip <8 ms
- NNG pub/sub within SBC: sub-10 ms latency claimed for state-to-control pathways
- Supervisor service: Continuous validation at 50 Hz+ rates
- WASM sandbox: Memory-isolated, no direct hardware access

### Binary Protocol Bridge

**Purpose:** Real-time communication between MCU tier and SBC tier

**Specifications:**
- Measured round-trip latency: <8 ms at 50 Hz state update rate
- Payload: Filtered sensor state, state estimates, RC takeover status, communications health
- Inbound: Suggested navigation commands, actuator commands, control parameter updates
- All inbound suggestions time-validated, bounded, and checked for consistency by embedded arbiter

### NNG Pub/Sub Messaging System

**Purpose:** Internal autonomy module coordination on SBC

**Features:**
- Lightweight C implementation
- Multiple communication patterns supported
- Suitable for embedded/multi-process systems without ROS 2 or DDS overhead
- Enables modular autonomy components to interact without tight coupling

### NixOS Operating System (SBC)

**Why selected:**
- Declarative configuration model
- Reproducible builds
- Atomic upgrade/rollback capabilities
- Valuable for safety-critical experimentation, fleet deployment, traceability

**Capabilities:**
- Supports fleet-wide over-the-air updates
- Container-based component deployment

### WebAssembly (WASM) Sandboxing

**Runtime options:** WAMR (WebAssembly Micro Runtime) or WasmEdge

**Security guarantees:**
- Memory isolation: WASM modules cannot access memory outside sandbox
- No system call access
- Cannot bypass safety constraints or access hardware devices
- Explicit interface exposure for pub/sub communication only
- Resource limits enforced (CPU, memory)

### S2 Flight Test Platform

**What it is:** BST's fixed-wing UAS platform, previously developed and certified under prior NASA SBIR projects

**How used:** Phase I benchtop prototype validation; planned for Phase II flight testing of modular autonomy architecture

---

## Use Cases & Applications

### NASA Applications

1. **Advanced Air Mobility (AAM):** Modular autonomy architecture provides framework for developing and testing AAM flight systems; enables third-party evaluation of autonomous components
2. **Sense-and-Avoid (SAA) / Detect-and-Avoid (DAA):** Capable of hosting perception algorithms in isolation
3. **Terrain and Obstacle Avoidance:** Vision-based modules can execute as sandboxed WASM components
4. **Beyond Visual Line of Sight (BVLOS) Operations:** Multi-vehicle coordination layer supports coordinated BVLOS missions
5. **Computer Vision Applications:** ML and vision layer hosts perception and learning-based estimation
6. **Advanced Flight Control:** ML-enabled control loop tuning for optimal performance across flight regimes

### Non-NASA / Commercial Applications

- **Aerial Survey Companies:** Rapid integration of custom sensing algorithms without full system revalidation
- **Agricultural Monitoring:** Precision agriculture applications with advanced autonomy
- **Infrastructure Inspection:** Long-duration operations with adaptive flight control
- **Environmental Monitoring / Emergency Response:** Resilient autonomy for dynamic field conditions
- **UAS Original Equipment Manufacturers (OEMs):** Modular autonomy framework as underlying backbone for fleet management systems
- **Academic Research Institutions:** Plug-and-play research autonomy module integration

### Commercialization Model

- Subscription-based: Continuous updates, maintenance support, centralized flight log database
- Recurring revenue streams for maintenance and feature updates
- Strategic partnerships with avionics distributors and OEMs to expand market reach

---

## Key Results (Phase I Accomplishments)

### Architecture Definition (Task 1)

**Deliverables:**
- Detailed layered architecture documentation with five functional layers (Layers 1–5)
- Standardized binary messaging protocol specification for inter-tier communication
- NNG pub/sub message definitions for intra-SBC module communication
- Comprehensive sequence diagrams for system initialization, mission planning, and mid-mission plan revision
- Interface definition documents specifying message formats for sensor readings, control commands, status alerts

**Key Findings:**
- Two-tier separation (MCU + SBC) successfully isolates deterministic control from experimental autonomy
- Publisher-subscriber abstraction enables modular, loosely coupled components
- Standardized message types allow components to be hot-swapped without system-wide modification

### SwiftCore System Adaptation (Task 2)

**Deliverables:**
- FreeRTOS-based task scheduling on STM32 (minimally invasive refactor of existing flight-proven control logic)
- Updated software interfaces to support modular autonomy inputs
- Multi-platform support readiness (fixed-wing, VTOL, multirotor configurations)

**Key Findings:**
- Migration to FreeRTOS maintains determinism while improving modularity and maintainability
- Existing validated control behaviors preserved; RTOS layer adds organization without reinvention
- Embedded arbiter effectively arbitrates between native controller and external suggestions

### Safe Sandbox Development (Task 3)

**Deliverables:**
- Benchtop prototype safe sandbox module integrating Raspberry Pi Zero 2 W with SwiftCore autopilot
- Safety threshold definition and override logic documentation
- Supervisor service implementation for continuous command validation

**Key Findings:**
- UART-based communication between MCU and SBC validated as reliable
- NNG-based pub/sub message routing successfully distributes autonomy module commands
- Supervisory safety enforcement confirmed: experimental control inputs successfully monitored and rejected when exceeding predefined safety thresholds
- Safe transition between external and fallback controllers validated in benchtop tests
- Round-trip latency: <8 ms, supporting real-time supervisory and adaptive control functions

### ML-Enabled Control Loop Tuning Demonstration (Task 4)

**Deliverables:**
- Prototype ML module for control loop tuning
- WebAssembly-sandboxed experimental terrain-following altitude controller
- Benchtop HWIL (hardware-in-the-loop) demonstration of ML-enabled adaptive control

**Key Findings:**
- ML module successfully executes in WebAssembly sandbox without direct control authority
- Altitude control example: ML module provides vertical rate command based on current above-ground-level altitude; supervisor validates commands against safe altitude thresholds before application
- Sandboxing mechanism prevents non-deterministic ML algorithms from compromising flight-critical control

### Overall Phase I Outcome

- **Status:** Phase I successfully demonstrated architecture feasibility and function
- **Hardware Validated:** Benchtop integration of Raspberry Pi Zero 2 W (SBC) with SwiftCore autopilot (MCU tier)
- **Safety Confirmed:** Supervisory override mechanism proven effective; fallback to certified control verified
- **Modular Autonomy Proven:** Experimental modules can execute in isolation without jeopardizing flight safety
- **Latency Performance:** Measured round-trip communication latency <8 ms supports real-time control functions

---

## Notable Details

### Operational Heritage of SwiftCore
- ~20 years of flight operations
- Hurricane observation missions for NASA
- Volcanic sampling missions for NASA and NOAA
- Multiple FAA Certificates of Authorization (COAs) under Dr. Stachura's leadership (140+)
- Flight-tested on fixed-wing and multirotor platforms

### NDAA Compliance
- SwiftCore is NDAA-compliant, meeting defense sector requirements
- Supports uncrewed operations in contested environments

### Key Personnel Experience

**Dr. Jack Elston (PI, CEO):**
- Technical lead on all avionics work at BST
- Creator of SwiftCore autopilot
- Direct involvement in development of four different UAS