# A2.02-1017 Phase II Technical Narrative BST

## Document Metadata
- Type: NASA SBIR Phase II Technical Proposal
- Client/Agency: NASA (Aeronautics Research Mission Directorate)
- Program/Solicitation: NASA SBIR Phase II; Topic A2.02 (Autonomy for UAS); Contract 80NSSC25C0155 (Phase I)
- Date: May 2026 (submitted during Phase II proposal assembly)
- BST Products/Systems Referenced: SwiftCore, SwiftCore RTA Kit, SwiftSim, SwiftDeploy, SwiftBus, SwiftPilot, S2 (fixed-wing), S3 (VTOL), E2 (multirotor), S0 (dropsonde)
- Key Personnel: Beck Cotter (last editor)

## Executive Summary

Black Swift Technologies proposes to mature the SwiftCore Flight Management System from a benchtop-validated architecture (TRL 4-5 from Phase I) to a flight-validated, customer-deployable research platform for UAS autonomy and certification (TRL 7). The innovation centers on the Safe Sandbox supervisor—a deterministic runtime-assurance component that safely hosts non-deterministic experimental autonomy code (machine learning, neural networks) on flight-critical aircraft by enforcing hard real-time safety envelopes and automatically recovering to a certified baseline controller when violations occur. Phase II productizes this into reusable components (RTA Kit, SwiftSim simulation, SwiftDeploy deployment chain) that enable rapid validation and certification of autonomy modules for FAA Part 108 BVLOS operations.

## Technical Approach

### Modular Two-Tier Architecture
SwiftCore uses a hierarchical, modular approach separating safety-critical from experimental code:

1. **Tier 1: Embedded Flight Controller** (STM32F4/F1 microcontroller running FreeRTOS)
   - Hard real-time (1000 Hz) sensing, estimation, control, actuation
   - Implements five-layer functional decomposition: System Initialization, Mission Planning, Trajectory Control, Stability Control, Actuator Control
   - Internal CAN bus communication
   - Contains deterministic arbiter (lowest-latency safety enforcement)

2. **Tier 2: NixOS-Based Linux Single-Board Computer**
   - Hosts containerized native autonomy services and WebAssembly-sandboxed experimental modules
   - SwiftBus publish-subscribe message bus (built on NNG library)
   - Supports outer-loop autonomy at 50-200 Hz
   - Software supervisor component of the supervisory chain

3. **Inter-tier Bridge: Bounded-Latency UART Connection**
   - BST custom protocol with measured round-trip latencies <8 milliseconds at 50 Hz state updates
   - Now supports 50-200 Hz outer-loop autonomy

### Safe Sandbox Supervisor Architecture
Two-level supervisory chain enforcing safety without requiring internal controller analysis:

- **Software Supervisor** (Linux SBC): Monitors commands from experimental modules for violations
- **Deterministic Arbiter** (Microcontroller): Final enforcement layer with hard real-time guarantees
- Enforces envelope constraints: attitude, rate, velocity, geofence, message freshness
- Automatic fallback to certified SwiftCore baseline controller on any violation
- Aligned with ASTM F3269 runtime assurance standard

### WebAssembly Sandboxing
- Experimental autonomy modules run as WebAssembly binaries in isolated sandbox
- Memory isolation, bounded CPU/memory resources
- Prevents buffer overflows and unauthorized system access common in native code
- Runtime: WAMR or WasmEdge

## Products & Capabilities Described

### SwiftCore Flight Management System
- **What it is**: Modular, hierarchical flight control stack separating safety-critical baseline from experimental autonomy layers
- **Architecture**: Five functional layers with standardized message interfaces between layers
- **Safety approach**: Runtime assurance via Safe Sandbox supervisor
- **Flight heritage**: NDAA-compliant, operationally proven on S0 (hurricane operations), S2 (environmental sensing, NOAA/NASA missions)
- **Performance specs**: Inter-tier latency <5 ms at 200 Hz (Phase II target), supports 4+ concurrent sandboxed modules

### Safe Sandbox Supervisor (Phase II Innovation)
- **What it is**: ASTM F3269-aligned runtime assurance component; two-level hybrid arbiter (software + deterministic)
- **Proposed enhancements**: Formalized switching predicates, multi-source command arbitration, tamper-evident logging, PVS/SMT-verified switching logic
- **Proof point**: April 2026 EMASS flight test—supervisor recovered E2 multirotor from two envelope violations (roll to +45°, then +73° and yaw 90°) that would have destroyed airframe
- **Target metrics**: Demonstrated 100% override rate on 1000+ adversarial fault test cases; flight validation on 3+ airframes

### SwiftSim (Simulation & Validation)
- **Software-in-the-Loop (SWIL)**: Customer WebAssembly modules run against JSBSim aircraft models
- **Hardware-in-the-Loop (HWIL)**: Real UART bridge with actual timing on bench rig
- **Monte Carlo Faster-Than-Real-Time**: Sweep wind, mass, sensor noise, adversarial inputs across 1000s of trials per night per compute node
- **Deliverable**: Coverage metrics (envelope-trip rate, time-to-trip distributions, parameter-space coverage) for Part 108 safety cases
- **Based on**: JSBSim (dynamics) + AVL (aerodynamics) co-simulation pipeline productized as customer-facing tool

### SwiftDeploy (Atomic Deployment & Configuration)
- **What it is**: End-to-end signed, reproducible deployment chain leveraging NixOS + WebAssembly
- **Features**: 
  - Declarative system definition with atomic upgrades and rollback (<30 second recovery target)
  - Reproducible builds traceable to signed source revision
  - Cryptographic signature chain: trusted host → WebAssembly runtime → autonomy module
  - OTA updates from SwiftStation ground station
- **Heritage**: Already demonstrated on S0 hurricane sondes (2024-2025 seasons, NOAA P-3) and S2 UAS
- **Target specs**: 30-second atomic rollback, support for Rust/C/C++/ML frameworks (PyTorch, TensorFlow via WASI-NN)

### SwiftCore RTA Kit (Phase II Deliverable)
- Reusable, license-bounded SDK component for third-party integration
- Includes: Formal RTA specification, PVS/SMT-verified switching logic, comprehensive adversarial test suite
- Supports regulatory compliance documentation for Part 108

## Use Cases & Applications

### Demonstrated/Near-Term Missions
1. **Hurricane Operations** (NOAA partnership)
   - S0 dropsonde deployed 23+ times in 2025 hurricane season
   - Survival test: Hurricane Milton Category 5 with 200+ knot horizontal winds
   - Autonomous sounding in extreme atmospheric conditions

2. **BVLOS Fixed-Wing Missions**
   - Alaska BVLOS without ground observers (pioneered with NASA Ames)
   - Terrain-relative navigation and GPS-denied operations
   - 25 km volcanic-gas sampling at Makushin Volcano (7,000 ft AGL, SO₂/CO₂ payloads)

3. **Severe Weather Interception**
   - VORTEX2: First uncrewed aircraft interception of tornadic supercell (72 missions, 100+ mph, zero losses)

4. **Wildfire Monitoring**
   - August 2025: 24-hour airspace-persistence demo (Sunny Slope Sod Farm, Colorado)
   - Two S2 aircraft with NOAA NightFOX IR payload, Remote-ID detector, TAK integration

### Phase II Target Demonstrations
1. **ML-Based PID Auto-Tuning** (Layer 4, S2 fixed-wing): Neural network replaces manual tuning
2. **Terrain-Following Trajectory Control** (Layer 3, S3 VTOL): Maintain constant AGL altitude over varying terrain
3. **Vision-Based Emergency Landing Site Classification** (Layer 2, E2 multirotor): ML classifier for safe landing zones (leverages BST's prior NASA-funded ML emergency landing work)

### Commercial Partner Use Cases
- **EMASS (Embedded A.I. Systems)**: Integrating ECS-DoT ultra-low-power Edge AI SoC into multirotor power management via SwiftCore payload pathway (active partnership, April 2026 flight validation completed)
- **ADONIS**: Reference customer using SwiftCore as avionics backbone for specialized fixed-wing UAS (Phase I reference, Phase II case study)
- **Genesis/Brookhaven National Lab**: DOE inter-agency partner using SwiftCore for atmospheric-science UAS (DE-FOA-0003612, May 2026 submission)

## Key Results (from Phase I, forming Phase II baseline)

### Phase I Achievements (Sept 2025 – March 2026)
- All four technical objectives reached 100% completion
- Exited at TRL 4-5, ready for in-flight maturation
- **Risk retired**: Hosting non-deterministic autonomy on flight-critical UAS without compromising safety

### Phase I Validation Demonstrations
1. **Terrain-Following Controller Test**: Replaced altitude function in Trajectory Control Layer with two implementations:
   - Proportional AGL terrain-following controller (baseline)
   - Neural network terrain-following controller (trained to emulate proportional)
   - Both exercised in Gazebo HWIL simulation
   - Both maintained within supervisor's vertical-rate envelope (+3 m/s climb, -1.5 m/s descent)
   - Neural network: 10,000 synthetic training examples, 150 epochs to convergence, MSE = 0.038

2. **Phase I Artifacts Produced**:
   - Five-layer autopilot functional decomposition with explicit interface message definitions
   - JSBSim/AVL co-simulation pipeline with closed-loop digital twin
   - Flight-proven UART payload-control protocol (tested on real BST customer aircraft in commercial program)

### April 2026 EMASS Flight Test (Headline Proof Point – Phase II Validation)
**Event**: Safe Sandbox supervisor prevented loss of E2 multirotor during EMASS AI controller testing

**Test Setup**:
- E2 hovering at 9 m AGL under SwiftCore control
- Control handed to EMASS AI-based controller via UART payload pathway
- Structured progression: hover → square pattern → vertical → hover-orbit → descent

**First Envelope Violation (t = 752.56 s, Flight 4)**:
- EMASS controller commanded roll +45°, pitch +16° within 1 second
- Supervisor roll envelope (30°) tripped immediately
- Arbiter rejected further EMASS inputs, reverted to SwiftCore
- Aircraft returned to stable hover, zero altitude loss, zero test-box excursion

**Second Envelope Violation (t = 777.48 s, Flight 4)**:
- EMASS controller saturated all four rotors to 1900 μs PWM
- Aircraft excursion: roll 73°, pitch 43°, yaw 90°, altitude 10→18 m AGL, lateral velocity 5.5 m/s, 7 m northward drift
- Supervisor forced recovery state
- Aircraft recovered safely, operator commanded landing at t = 805.9 s
- No airframe or payload damage

**Significance**:
- Real-world flight (not simulation or paper safety case)
- Non-deterministic controller produced commands that would have destroyed airframe
- Deterministic supervisor arrested divergence in time
- Occurred on production BST customer aircraft executing real commercial program
- Only known flight-validated demonstration of deterministic-fallback architecture hosting third-party AI control on small UAS (as of May 2026)
- High-fidelity dataset (143 Hz actuators, 71 Hz state, 70 Hz pressure, full ground track) with reproducible analysis pipeline—exact artifact type needed for Part 108 safety case

## Technical Objectives (Phase II)

### Objective 1: Safe Sandbox Supervisor Maturation & Formalization (RTA Kit)
- **Output**: Fully specified ASTM F3269-aligned RTA component
- **Acceptance criteria**:
  - Released RTA