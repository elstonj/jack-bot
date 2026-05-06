# NASA ARMD Aeronautics Flight Accelerator RFI Response: Adaptive and Secure Autonomy

## Document Metadata
- **Type:** RFI Response (Request for Information)
- **Client/Agency:** NASA ARMD (Aeronautics Research Mission Directorate)
- **Program/Solicitation:** NASA Aeronautics Flight Accelerator (AFA); Notice ID 80AFRC26SS013
- **Date:** 2026 (submitted in response to RFI)
- **BST Products/Systems Referenced:** SwiftCore, SwiftPilot, SwiftStation, SwiftTab, S2 fixed-wing, S2 VTOL, S0 air-deployable, E2 multirotor
- **Key Personnel:** Dr. Jack Elston (CEO, Technical POC), Beck Cotter (Administrative POC), Dr. Stachura (Safety leadership), Dr. Jinu Idicula (NASA Phase I technical monitor, CAS)

## Executive Summary

Black Swift Technologies proposes to mature the **SwiftCore Adaptive and Secure Autonomy framework**—a modular, two-tier avionics architecture that cleanly separates deterministic flight-critical control from sandboxed experimental autonomy—from Phase I prototype status (TRL 4–5) to flight-relevant maturity (TRL 7) through three flight-test spirals ending in FY28. The architecture solves the core obstacle to integrating advanced autonomy into airspace-class aircraft: providing a flight-test-ready platform where non-deterministic algorithms can be safely exercised while the certified SwiftPilot controller retains final command authority at all times.

## Technical Approach

### SwiftCore Architecture (Five-Layer Hierarchical Design)

**Core Innovation:**
- **Two-tier design** with strict separation of concerns:
  - **Microcontroller tier (STM32 under FreeRTOS):** Runs deterministic SwiftPilot flight controller with final command authority
  - **SBC tier (NixOS-based single-board computer):** Hosts experimental autonomy modules in WebAssembly sandboxes
  
**Operational Flow:**
- Experimental modules (classical control, ML models, computer vision, third-party autonomy stacks) execute in **WebAssembly sandboxes** with strong memory and capability isolation
- Modules publish *suggested* commands through standardized **NNG-based pub/sub message bus (SwiftBus)**
- **Dual-supervisor system** (one on SBC, one on microcontroller) continuously validates every suggestion against pre-defined:
  - Attitude, rate, velocity, and geofence envelopes
  - Freshness/staleness checks
  - Heartbeat validation
- Invalid, stale, or failed suggestions are **silently discarded**; certified controller continues flying
- End-to-end latency targets: <5 ms round-trip (microcontroller ↔ SBC) at 200 Hz

**Five Functional Layers:**
1. Multi-Aircraft/Swarm Interface and Mission Management
2. Trajectory Control
3. Stability Control
4. Actuator Control
5. Sensor & Payload Acquisition

### Phase I Heritage (Completed March 2026, Contract 80NSSC25C0155)

- Architecture definition and formal specification
- Ported SwiftCore microcontroller firmware to FreeRTOS
- Implemented NNG pub/sub message bus on Raspberry Pi Zero 2 W running NixOS
- Demonstrated sandboxed WebAssembly autonomy module exercising in-flight control authority through supervisor
- Validated end-to-end behavior in hardware-in-the-loop (HIL) simulation using JSBSim aircraft model
- Achieved <8 ms round-trip latency at 50 Hz on benchtop

### Proposed Three-Spiral Maturation Path

**Spiral 1 (FY26 Q4–FY27 Q2): HIL + Bench**
- Full-stack integration on BST S2 platform
- Hardware-in-the-loop validation in BST's JSBSim digital-twin environment
- Port SBC from Raspberry Pi Zero 2 W to NDAA-compliant production-grade SBC (no architectural changes)
- Demonstrate timing improvements to <5 ms at 200 Hz
- Validate atomic rollback mechanisms

**Spiral 2 (FY27): Fixed-Wing Flight at AFRC**
- Fixed-wing flight operations at Armstrong Flight Research Center under existing S2 Airworthiness Statement (AWS)
- Leverage AFRC range access and airworthiness culture
- Demonstrate supervisor envelope enforcement in dynamic flight conditions
- Gather flight-relevant performance data and seeded-fault data

**Spiral 3 (FY28): Multi-Airframe, Multi-Module Flight**
- Extend AWS to S0 air-deployable and E2 multirotor platforms
- Demonstrate four concurrent sandboxed autonomy modules of different provenance in single flight:
  - BST-native module
  - University research module
  - AAM partner module
  - ML/vision third-party module
- Demonstrate atomic, signed, over-the-air module deployment with <30 second rollback on fault
- Host AAM National Campaign partner's autonomy workload in sandbox for direct subscale validation

### Technology Integration Challenges & Mitigation

**Timing Challenge:** End-to-end latency across UART bridge under realistic SBC load
- Mitigation: DMA-driven serial I/O, latest-sample semantics, aggressive freshness arbitration

**WebAssembly Toolchain Maturity:** Known compiler-bug history
- Mitigation: Architecture explicitly contains WASM-induced faults inside supervisor's safety envelope; in flight, WASM defect produces only bad suggestion, never unsafe actuator command

**FAA Certification Path Uncertainty:** Current FAA guidance does not address modular architectures directly
- Mitigation: NASA partnership is primary mechanism for shaping certification path; deterministic-fallback design directly addresses DO-178C non-deterministic-AI concerns

## Products & Capabilities Described

### SwiftCore Avionics Framework
- **What it is:** Modular two-tier flight management system separating deterministic control from experimental autonomy
- **Specifications:**
  - Inter-tier message latency: <5 ms round-trip at 200 Hz (FY28 target; Phase I: <8 ms at 50 Hz)
  - Safety envelope override response: <50 ms in flight (Phase I: <100 ms on bench)
  - Concurrent sandboxed modules: ≥4 per airframe (Phase I: 1 demonstrated)
  - Platform reconfiguration time: <4 hours across FW/VTOL/multirotor
  - Atomic OS rollback on autonomy fault: <30 seconds field rollback
  - Supported languages in sandbox: Rust, C/C++ via WASM; Simulink, Python, MATLAB via WASI-NN
  - Current TRL: 4–5 (Phase I benchtop); Target: TRL 7 (flight relevant) by end FY28

### SwiftPilot Flight Controller
- TRL 9 production hardware in operational use across NASA, NOAA, USGS, USAF
- Deterministic autopilot resident on STM32 microcontroller under FreeRTOS
- Retains final command authority throughout SwiftCore architecture
- FAA-certified under prior Certificates of Authorization and AFRC Airworthiness Statement

### SwiftStation & SwiftTab
- Ground station software and Android UI
- TRL 9 production systems
- Integrate with SwiftCore supervisory logic

### WebAssembly Sandbox Runtime
- Capability-isolated execution using WAMR/WasmEdge
- Allows third-party modules in any compiled language
- Modules delivered as signed, versioned, atomic artifacts
- Constraints enforced without requiring deep embedded-systems expertise from module developers

### NNG Pub/Sub Message Bus (SwiftBus)
- Lightweight C-native messaging
- Standardized interface for all layers and modules
- Deterministic semantics for real-time control

### NixOS-Based SBC Autonomy Host
- Reproducible Linux base
- Atomic rollback capability
- BST SDK message protocol
- DMA serial I/O for low-latency UART bridge to microcontroller

## Airframes & Platforms

### S2 Fixed-Wing
- 10 ft wingspan, 14,000 ft ceiling
- 30 mph max wind tolerance
- 2 hr endurance
- 5 lb modular nose-cone payload capacity
- FAA-certified under prior COAs and AFRC AWS
- Production aircraft, already TRL 9

### S2 VTOL
- 13 ft wingspan
- 1.5 hr endurance
- Shares identical SwiftCore avionics with fixed-wing variant

### S0 Air-Deployable
- 1.2 kg airframe
- 105 min endurance
- Launched from carrier aircraft (NOAA WP-3D, USAF WC-130J, NASA B-200 King Air, Gulfstream III)
- Recovers by parachute
- Validated through NOAA WP-3D hurricane reconnaissance
- Demonstrated survival in 200+ knot horizontal winds during Hurricane Milton's Category 5 phase

### E2 Multirotor
- Used in April 2026 Nanoveu ECS-DOT (X-DOT) AI control payload flight demonstration
- Carries E2-class payloads

## Use Cases & Applications

### NASA Applications
- **Convergent Aeronautics Solutions (CAS):** Autonomy V&V, research validation
- **Airspace Operations and Safety Program (AOSP):** Safety-critical autonomy validation, deterministic-fallback architecture research
- **Advanced Air Mobility (AAM) National Campaign:** Hosting third-party AAM autonomy workloads for subscale validation; direct path to certification
- **System-Wide Safety (SWS):** Seeded-fault flight data for safety research
- **Earth Science (SMD):** FireSense campaigns, hurricane reconnaissance, volcano monitoring integration

### NOAA Applications
- Hurricane and atmospheric reconnaissance
- Building on BST's ongoing S0 deployments and 268-mission WP-3D heritage
- Hurricanes Ernesto, Helene, Milton, Tammy, Francine operations

### USGS Applications
- Volcano Disaster Assistance Program (VDAP) BVLOS monitoring
- Makushin/Aleutian Islands volcano sampling campaigns
- SO₂ and CO₂ plume characterization at 25 km BVLOS, 7,000 ft AGL

### Department of Defense
- Counter-UAS operations
- GPS-denied ISR (Intelligence, Surveillance, Reconnaissance)
- Replicator-class autonomous-mass missions
- AFWERX and Air Force CUAS engagements
- NDAA-compliant alternative to foreign-origin flight controllers

### Commercial Operators
- **Advanced Air Mobility (AAM):** Wisk, Joby, Archer, Supernal, Reliable Robotics class certification and autonomy V&V
- **Beyond-Visual-Line-of-Sight (BVLOS) operations:** Precision agriculture, infrastructure inspection, mining
- **Small UAS OEMs:** Seeking NDAA-compliant U.S. flight management system alternative to monolithic open-source autopilots (PX4, ArduPilot)

### Field Heritage
- All seven continents operational deployment
- 2,500+ legal flight hours
- 150+ FAA-approved operations
- Mission classes:
  - **Hurricane reconnaissance:** S0 deployments in Hurricane Milton Category 5 (200+ knot winds); Hurricanes Ernesto, Helene, Milton, Tammy, Francine
  - **Volcanic plume sampling:** USGS VDAP at Makushin; water-vapor and SO₂/CO₂ payloads
  - **Arctic atmospheric profiling:** Greenland operations to 14,000 ft at sub-zero ambient
  - **Soil-moisture mapping:** Costa Rican rainforest canopy operations
  - **Severe-weather penetration:** VORTEX2 tornado interception (first UAS to intercept tornadic supercell); 72 missions at 100+ mph with zero airframe losses
  - **Persistent observation:** August 2025 NASA-NSSC 24-hour wildfire airspace persistence with dual S2 carrying NOAA NightFOX IR payload, Remote-ID detector, and TAK integration

## Key