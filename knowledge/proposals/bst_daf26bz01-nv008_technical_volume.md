# Runtime Assured Autonomy for a Distributed, Hot-Updateable, MOSA-Compliant Avionics Fabric Across Backpackable, Air-Deployed, and Long-Range VTOL Small Unmanned Aircraft Systems

## Document Metadata
- Type: SBIR Phase I Technical Proposal
- Client/Agency: Department of the Air Force
- Program/Solicitation: DAF26BZ01-NV008 (FY26 Department of the Air Force SBIR); DOD_SBIR_2026_P1_CBZ
- Date: Submitted 2026 (created/modified 2026-05-21)
- BST Products/Systems Referenced: SwiftCore distributed pub-sub avionics; Black Swift S0 (backpackable and air-deployed variants); Black Swift S3 VTOL; WASM validator; NixOS base
- Key Personnel: Jack Elston, PhD (Principal Investigator, Founder and CEO); Maciej Stachura, PhD (Co-Investigator, COO); two senior software engineers; one controls engineer; one verification engineer

## Executive Summary

Black Swift Technologies proposes to develop the first distributed Runtime Assured Autonomy (RTAA) fabric instantiated on production small UAS hardware, combining SwiftCore pub-sub avionics, signed WASM payloads, NixOS reproducible builds, and Copilot 3-generated runtime monitors to safely bound complex autonomous functions while minimizing false alarms. The Phase I effort ($300,000, 6 months) will deliver an ASTM F3269-21-conformant architecture, software-in-the-loop validation against five contingency-driven use cases, and a detailed Phase II plan for cooperative multi-platform flight demonstration across three BST airframes.

## Technical Approach

### Core Architecture (Four-Layer Fabric)

1. **SwiftCore Distributed Pub-Sub Avionics**: Every flight node is an independent compute element on a deterministic network (DDS-compatible, evaluating Zenoh for constrained bandwidth cases), replacing monolithic autopilot architecture. Publishes and subscribes to named topics with specified QoS and reliability modes. Cross-platform topic ontology enables fleetmates to observe each other's situational data for distributed monitoring.

2. **NixOS Reproducible Base Operating System**: Produces bit-for-bit identical, atomically upgradeable, instantly rollbackable system images. All inputs content-addressed; single manifest serves as deployment artifact for certification. Targets >90% reproducibility across hardware.

3. **Signed, Statically Validated WebAssembly (WASM) Payloads**: Loadable autonomy and safety logic sandboxed with capability-bounded execution (WASI Component Model). BST hardware-backed signing chain prevents unauthorized modules. Static validator confirms control flow and memory safety before runtime acceptance.

4. **Formal Runtime Monitors (Copilot 3 Generated)**: Temporal logic specifications (LTL, PTLTL, MTL) compiled to hard real-time C99 monitors with static memory and time bounds. Distributed across pub-sub bus to observe every message every component publishes. Implements ASTM F3269-21 canonical elements: Safety Monitor, RTA Switch, Recovery Control Functions, Input Manager.

### ASTM F3269-21 Instantiation

- Maps ASTM F3269-21 elements onto SwiftCore nodes
- Decomposes Complex Function (autonomy COA generation), Safety Monitor (runtime checks), Recovery Control Functions (safe fallback behaviors), RTA Switch (authority decision), and Input Manager (vetted sensor data) across distributed compute
- Clause 1.5.6 target: <0.5 nuisance trips per 100 flight hours (false alarm rate)

### Use Cases (Objective 2 enumeration)

1. Corrupt COA generation by faulted autonomy
2. Platform hardware fault (sensor degradation, actuator anomaly)
3. Pop-up threat detected and broadcast by fleetmate
4. Unforeseen mission change from ground command or AWACS
5. Jamming-induced sensor inconsistency

## Products & Capabilities Described

### SwiftCore Flight Management System
- **What it is**: Distributed avionics architecture with pub-sub messaging, deterministic network contract, multi-node redundancy
- **RTAA use**: Provides the underlying communication fabric and independent compute nodes for deploying RTAA components; enables cross-platform monitor coordination
- **Specifications**: DDS-compatible today; Zenoh evaluation for contested wireless (64% smaller overhead than DDS per ZettaScale claims); 5-byte per-message overhead target

### Black Swift S0 (Backpackable Variant)
- **What it is**: 2.75 lb folding-wing tactical UAS
- **RTAA use**: Phase II platform for close-in forward ISR; intentionally faulted autonomy testing scenario
- **Specifications**: Backpackable deployment; in operational and pre-operational use

### Black Swift S0 (Air-Deployed Variant)
- **What it is**: Dropped from manned aircraft (NOAA WP-3D Orion via standard A-size sonobuoy tube); Guinness World Record holder for second-longest air-deployed UAS mission
- **RTAA use**: Phase II platform for low-altitude EO/IR sweep; COA replan under pop-up threat scenario
- **Specifications**: Extreme endurance; field-deployed capability; NOAA-qualified

### Black Swift S3 VTOL
- **What it is**: Long-range vertical takeoff and landing platform
- **RTAA use**: Phase II platform for high-altitude relay and long-loiter ISR; mid-mission WASM hot-swap scenario
- **Specifications**: Extreme weather flight qualification ongoing through 2026; capable of RF threat detection and broadcast

### WASM Static Validator
- **What it is**: Tool to accept/reject compiled WebAssembly modules against control flow and memory safety specifications
- **RTAA use**: Gate function in the hot-swap path; ensures only validated modules load
- **Specifications**: Phase I deliverable; capable of rejecting known unsafe instruction sequences; hardware-backed signing key verification

### NixOS Reproducibility Manifest (Nix Flake)
- **What it is**: Dependency-isolated build specification with content-addressed inputs; atomic upgrades and instant rollback
- **RTAA use**: Certification anchor—bit-for-bit identical image for evaluation authority
- **Specifications**: Phase I deliverable; >90% reproducibility target; audit report from two independent build hosts

### Copilot 3 Runtime Monitors
- **What it is**: Temporal logic compiler (LTL, PTLTL, MTL) generating hard real-time C99 monitors
- **RTAA use**: Implements safety monitor function of ASTM F3269-21; distributed across pub-sub bus
- **Specifications**: Static memory and time bounds; Phase I generates monitors for ≥3 of 5 use cases; targets <100 ms detection latency at pub-sub layer (95th percentile)

## Use Cases & Applications

### Tactical ISR in Contested Environment
- **Scenario**: Three-platform cooperative ISR with pop-up threat injection
- **Platforms**: S3 relay at high altitude; air-deployed S0 at low altitude; backpackable S0 at forward line of own troops
- **RTAA function**: S3 RF sensor detects SAM activation, broadcasts on fleet bus; air-deployed S0's monitor detects COA/threat envelope conflict; mitigation triggers route replan with geofence/altitude/deconfliction verification

### Mid-Mission Adaptive Threat Classifier
- **Scenario**: Newly observed adversary vehicle silhouette requires threat classifier update mid-mission
- **Platforms**: S3 VTOL
- **RTAA function**: Freshly trained WASM threat classifier uplinked from ground, validated against signing chain, loaded into sandbox, activated only after runtime monitor accepts module

### Hardware Fault Recovery
- **Scenario**: Sensor degradation or actuator anomaly detected
- **Platforms**: Any BST platform
- **RTAA function**: Runtime monitor detects divergence from expected behavior; Recovery Control Function activates safe state (loiter or return to handoff point)

### Intentional Fault Injection (Testing)
- **Scenario**: Autonomy deliberately fed corrupted model recommending unsafe COA
- **Platforms**: Backpackable S0
- **RTAA function**: Network-level temporal logic monitor detects COA divergence from feasible set; mitigation activates return-to-handoff-point

### Ukrainian-Field-Inspired Rapid Adaptation
- **Operational Driver**: Field experience in Ukraine demonstrates platform obsolescence in days without safe field updates
- **BST Answer**: Module load, validation, and activation at flight line before launch; mid-mission hot-swap with formal Simplex guard

## Technical Deliverables (Phase I)

### Task 1: Architecture and Functional Design (Months 1–2)
- RTAA Architecture Specification (SwiftCore instantiation of ASTM F3269-21)
- F3269-21 clause-by-clause conformance matrix
- Open Mission Systems (OMS) alignment table
- Five Use Case Definition Sheets (observable signatures, temporal logic specs, RCF candidates, success criteria)

### Task 2: WASM Validator and Nix Reproducibility Manifest (Months 2–4)
- WASM static validator source code; sample malicious module validator must reject
- Nix flake for SwiftCore RTAA base image (bit-for-bit reproducibility)
- Reproducibility audit report (two independent build hosts)

### Task 3: Desktop Simulation Against Use Cases (Months 3–5)
- SwiftCore software-in-the-loop implementation of ≥3 of 5 use cases
- Copilot 3-generated monitors for each use case
- Deterministic fault injection harness (≥100 simulated flight hours per use case)
- Simulation Results Report: detection latency, detection probability, false alarm rate

**Phase I Success Criteria**:
- False alarm rate: <0.5 nuisance trips per 100 flight hours
- Detection latency: ≤100 ms (95th percentile)
- Detection probability: >95%

### Task 4: Phase II Plan and ACT3 Interoperability (Months 5–6)
- AFRL ACT3 act3-ace reference toolchain interoperability demonstration
- Phase II Technology Development Plan (detailed 40-minute three-platform cooperative flight demonstration, schedule, risk register, transition partnerships)
- Final technical report

### Phase II Quantitative Targets
- Zero false alarms over 10 cumulative hours of monitored cooperative flight
- Detection latency ≤100 ms (pub-sub layer)
- Detection-to-mitigation latency ≤2 seconds end-to-end
- WASM load, validate, and activate cycle ≤500 ms
- Cross-platform mission reproducibility from single Nix manifest
- Technology Readiness Level 6 (flight demo in relevant environment)

## Key Technical Innovation Claims

1. **First distributed Simplex-style Runtime Assured Autonomy on production small UAS hardware**: Combines safety-critical assurance with the agility of Ukrainian drone software
2. **WASM sandboxing with capability bounds (WASI Component Model)**: No prior DoD RTA program has used WASM as loadable autonomy substrate
3. **NixOS reproducible builds in fielded UAS avionics**: No fielded UAS avionics product line uses deterministic, content-addressed build system
4. **Hot-swap mechanism itself certifiable**: Formal guard (Simplex switch) controls module activation
5. **Cross-platform distributed monitoring**: Extends ASTM F3269-21 (single-vehicle focus) to multi-agent scenarios; fleetmate awareness on same pub-sub bus

## Transition Strategy

### Immediate (Department of the Air Force)
- **Collaborative Combat Aircraft (CCA)**: Wrap Shield AI Hivemind (YFQ-44A) and Collins Sidekick (YFQ-42A) on Autonomy Government Reference Architecture
- **AFSOC / Air Combat Command**: Contested-environment small UAS ISR and strike
- **Air Force Special Operations Command**: Engaged through air-deployed S0 program
- **AFRL Aerospace Systems Directorate**: Prior tactical weather drone Phase II relationship

### Broader DoD
- **Navy / NAVAIR / NUWC**: Sonobuoy-launched UAS work
- **USSOCOM / Army Futures Command**: Resilient small UAS in Indo-Pacific contested EM environment
- **OUSD R&E / Replic