# Adaptive and Secure Autonomy for UAS: A Modular Approach to Flight Control, Machine Learning Integration, and Multi-Vehicle Coordination

## Document Metadata
- **Type**: Phase I Final Report
- **Client/Agency**: NASA (Convergent Aeronautics Solutions program; SBIR Subtopic A2.02: Enabling Aircraft Autonomy)
- **Program/Solicitation**: NASA SBIR Phase I; Contract Number 80NSSC25C0155
- **Date**: March 2026 (award 9/29/2025)
- **BST Products/Systems Referenced**: SwiftCore Flight Management System, S2 UAS platform
- **Key Personnel**: Dr. Jack Elston (PI, CEO), Dr. Maciej Stachura (CTO), Ben Busby (Lead Software Engineer)

## Executive Summary
Black Swift Technologies developed and demonstrated a modular, two-tier autonomy architecture for the SwiftCore Flight Management System that safely integrates experimental autonomy modules with flight-critical control. The MCU tier (STM32-based, FreeRTOS) provides deterministic flight control at 1 kHz; the SBC tier (NixOS Linux) hosts containerized services and WebAssembly-sandboxed experimental modules. A benchtop prototype validated the binary protocol bridge, NNG pub/sub messaging, and safety supervisor enforcement with <8 ms round-trip latency at 50 Hz updates.

## Technical Approach

**Two-Tier Architecture:**
- **MCU Tier (STM32F4/F1, FreeRTOS)**: Real-time flight control at 1 kHz loop rate; independent hardware nodes (sensors, actuators, control) communicate via CAN bus using publisher-subscriber messaging; deterministic sensor fusion and state estimation; dedicated supervisory/arbitration task enforces safety envelopes.
- **SBC Tier (NixOS on Linux)**: Hosts native autonomy modules (Nix packages) for trusted/performance-critical functions (cooperative multi-UAS, mission management, planning) and WebAssembly-sandboxed modules for experimental/third-party algorithms (ML-based vision, control tuning, adaptive control).

**Communication Protocol:**
- UART link between MCU and SBC carrying filtered sensor data and state estimates
- Purpose-built binary protocol: <10 ms round-trip latency (measured <8 ms), 50 Hz state updates
- NNG-based pub/sub message bus on SBC enabling flexible inter-module routing
- Service discovery and standardized message types for each functional layer

**Safety Architecture:**
- Embedded arbiter continuously validates externally-supplied control suggestions against predefined attitude, velocity, and geofence limits
- Automatic fallback to certified control modes if experimental modules issue unsafe commands or lose heartbeat
- WebAssembly sandboxing enforces memory isolation and resource limits; modules cannot access system calls, devices, or other modules except through explicitly exposed interfaces
- SBC-level supervisor arbitrates among multiple autonomy sources (priority-based, mode-dependent, blending, or voting policies)

## Products & Capabilities Described

### SwiftCore Flight Management System
- **What it is**: NDAA-compliant, flight-proven avionics platform with ~20 years of operational heritage including hurricane observation and volcanic sampling for NASA/NOAA
- **Proposed use**: Foundation for modular autonomy framework; MCU tier implements deterministic flight control; SBC tier integrates new autonomy capabilities
- **Specifications**: 
  - STM32F4/F1 microcontrollers under FreeRTOS
  - 1 kHz flight control loop rate
  - CAN bus interconnect for sensor/actuator nodes
  - Supports multiple aircraft configurations (fixed-wing, VTOL, multirotor)

### Messaging Architecture
- **NNG pub/sub** for SBC inter-module communication
- Binary protocol for MCU-SBC bridge (design goal: <10 ms latency, achieved <8 ms)
- Standardized message types for sensor data, control commands, status alerts
- Supports 50 Hz state update rates

### Safe Sandbox Environment
- **WebAssembly (WASM)** runtime (WAMR or WasmEdge) for sandboxed experimental modules
- Memory-isolated execution; no direct hardware access or inter-module access except through exposed interfaces
- Safety supervisor validates all commands before submission to flight controller
- Automatic override when thresholds exceeded or heartbeat lost

### ML-Enabled Control Loop Tuning Module (Proof-of-Concept)
- Proof-of-concept WASM module for in-flight PID controller tuning
- Injects calibrated control inputs (doublets) and analyzes system response
- Integrated on NDAA-compliant flight computer
- Benchtop demonstration: ML-enabled altitude control via vertical rate command with safety validation

## Technical Layers Defined
1. **Layer 1**: Multi-vehicle coordination and information gathering
2. **Layer 2**: Machine learning and machine vision-based sensing and control
3. **Layer 3**: Standard navigation (waypoint tracking, altitude/speed commands, velocity vectors)
4. **Layer 4**: Control loop modification (dynamic PID tuning, TECS-like algorithms)
5. **Layer 5**: Low-level sensor acquisition and actuator control

Each layer uses standardized pub/sub messaging and service discovery; independently replaceable through defined interfaces.

## Use Cases & Applications

### NASA Applications
- **Advanced Air Mobility (AAM)**: Third-party development and safety evaluation of autonomous components
- **Sense-and-Avoid (SAA)** and **Detect-and-Avoid (DAA)** systems
- **Terrain and obstacle avoidance**
- **Beyond Visual Line-of-Sight (BVLOS)** operations
- **Computer vision** applications
- **Advanced flight control systems**
- **Rapid integration** of autonomy for NASA CAS SWIFT project and related programs

### Non-NASA / Commercial Applications
- Aerial survey companies
- Agricultural monitoring firms
- Infrastructure inspection services
- UAS original equipment manufacturers (OEMs) seeking advanced autonomous functionalities
- Academic research institutions

## Key Results (Phase I Accomplishments)

**Architecture Definition:**
- Two-tier architecture separating deterministic flight control from sandboxed autonomy implemented and validated
- Standardized binary messaging protocol developed; <8 ms measured round-trip latency confirmed
- 50 Hz state updates supported

**Benchtop Demonstration:**
- Integrated SwiftCore autopilot with Raspberry Pi Zero 2 W running NixOS
- Validated UART-based MCU-SBC communication
- Validated NNG pub/sub message routing between autonomy modules
- Confirmed supervisory safety enforcement: experimental control inputs successfully monitored and rejected when exceeding predefined safety thresholds
- Demonstrated system can safely incorporate non-deterministic autonomy algorithms without compromising flight-critical control

**Proof-of-Concept Demonstrations:**
- ML-enabled altitude control: WebAssembly module provided vertical rate command based on above-ground-level altitude with supervisor validation before application
- Task scheduling and labor allocation: 720 total hours across three key personnel (Dr. Elston: 210 hrs, Dr. Stachura: 210 hrs, Ben Busby: 300 hrs)

## Notable Details

**Operational Heritage:**
- SwiftCore has been flight-proven on nearly two decades of missions including hurricane observation (atmospheric sampling for NOAA) and volcanic gas sampling (NASA missions)
- Dr. Elston involved in development of four different UAS; authored >100 FAA Certificates of Authorization; conducted hundreds of flight experiments including Arctic deployments
- Dr. Stachura led >300 flight experiments (multi-aircraft cooperation, VORTEX2 tornado intercept); maintained 140+ FAA COAs; completed NASA Airworthiness Flight Safety Review Board process for UAS National Airspace System operations

**Compliance & Safety:**
- NDAA-compliant (U.S. domestic supply chain requirement met)
- Safety architecture mirrors established aerospace patterns (deterministic embedded control + advisory higher-level guidance)
- Embedded arbiter retains final authority over all control decisions
- Certified fallback modes automatic under all failure conditions

**Fleet Deployment Capability:**
- NixOS atomic upgrades and rollback support fleet-wide over-the-air updates
- Reproducible builds and declarative configuration enable traceability and certification

**Commercialization Strategy:**
- Subscription-based model: continuous updates, maintenance support, centralized flight log database
- Target partnerships with avionics distributors and OEMs
- Market research conducted identifying potential customers: AFIT, Navy/Marine UAS, Army Corps Engineers, DOE national labs, MIT Lincoln Lab, Johns Hopkins APL, universities (CU Boulder, Colorado State, University of Alaska Fairbanks, Kansas State, UND), Air Force Academy

**Phase II Pathway:**
- Extended hardware-in-the-loop and flight demonstrations planned
- Further maturation toward full validation framework
- Transition to NASA CAS and other federal/commercial stakeholders
- Continued customer discovery with prioritized organizations aligned with rapid autonomy integration missions

**Risk Mitigations Addressed:**
- Integration complexity: HIL testing and simulation validation before flight
- Legacy system adaptation: incremental updates with version control and traceability
- Experimental module safety: robust sandbox with predefined thresholds and fallback verification
- ML algorithm accuracy: historical flight data training, conservative tuning thresholds, simulation-first validation