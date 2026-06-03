# Runtime Assured Autonomy for a Distributed, Hot-Updateable, MOSA-Compliant Avionics Fabric Across Backpackable, Air-Deployed, and Long-Range VTOL Small Unmanned Aircraft Systems

## Document Metadata
- Type: SBIR Phase I Technical Proposal (Volume 2)
- Client/Agency: U.S. Air Force Research Laboratory (AFRL)
- Program/Solicitation: DSIP Topic DAF26BZ01-NV008; Runtime Assured Autonomy; Proposal No. F26BZ-NV008-0063
- Date: 2026-06-02
- BST Products/Systems Referenced: Black Swift S0 (backpackable and air-deployed variants), Black Swift S3 VTOL, SwiftCore distributed pub-sub avionics fabric
- Key Personnel: Jack Elston, PhD (Principal Investigator); Beck Cotter (last editor)

## Executive Summary

Black Swift Technologies proposes to develop the first distributed, production-ready Runtime Assured Autonomy (RTAA) fabric instantiated on small UAS hardware, combining formal runtime monitors (via NASA Copilot 3), signed WebAssembly (WASM) payloads with capability-bounded sandboxing, and NixOS reproducible builds. The architecture implements ASTM F3269-21 standards across a distributed pub-sub avionics bus, enabling safe mid-mission software updates, multi-platform cooperative autonomy with fault detection/mitigation, and zero false-alarm performance under contested conditions. Phase I will deliver architecture specification, WASM validator, simulation validation against five contingency use cases, and Phase II flight demonstration plan across three BST platforms.

## Technical Approach

**Core Innovation**: First instantiation of distributed Simplex-style Runtime Assured Autonomy on production small UAS hardware, composed of four mutually reinforcing layers:

1. **SwiftCore Distributed Pub-Sub Avionics Fabric** (Layer 4 - Foundation)
   - Every flight node is an independent compute element on a deterministic network (DDS-compatible, with Zenoh evaluation planned for Phase II)
   - Single observable surface for fault determination via published topics
   - Cross-platform fleet awareness: fleetmate situational data published on shared bus
   - Replaces monolithic centralized autopilot architecture

2. **NixOS Reproducible Base Operating System** (Layer 3 - Infrastructure)
   - Bit-for-bit identical, atomically upgradeable, instantly rollbackable system images
   - Content-addressed manifest eliminates supply chain ambiguity
   - Addresses DO-178C/DO-330 tool qualification burden via deterministic builds
   - Demonstrated reproducibility across independent build hosts

3. **Signed and Statically Validated WebAssembly (WASM) Payloads** (Layer 2 - Loadable Autonomy)
   - Loadable autonomy and sensing modules compiled to portable WASM format
   - Hardware-backed signing chain for authenticity verification
   - WASI Component Model capability-bounded sandboxing (deny-by-default, no ambient authority)
   - Static validator rejects unsafe instruction sequences pre-deployment
   - Enables mid-mission hot-swap of threat classifiers and autonomy modules under Simplex guard

4. **Formal Runtime Monitors (ASTM F3269-21 Architecture)** (Layer 1 - Safety Guard)
   - Copilot 3-generated monitors from temporal logic specifications (LTL, PTLTL, MTL)
   - Distributed across pub-sub bus: monitors see every message every component publishes
   - Implements the five canonical F3269-21 functional blocks:
     - Complex Function (loadable autonomy)
     - Safety Monitor (detects unsafe outputs)
     - RTA Switch (enforces authority reversion)
     - Recovery Control Functions (verified baseline behaviors: loiter, return-to-base, geofence revert)
     - Input Manager (vets exogenous inputs)
   - Cross-platform monitors detect fleetmate-observable faults

## Products & Capabilities Described

### Black Swift S0 (Backpackable Variant)
- 2.75 lb folding wing tactical asset
- Operator-deployed from forward line of own troops
- Close-in ISR or strike spotting role in Phase II demonstration
- Hosts loadable autonomy and sensing modules via WASM sandbox

### Black Swift S0 (Air-Deployed Variant)
- Guinness record holder for second-longest air-deployed UAS mission
- Deployed via standard A-size sonobuoy tube from NOAA WP-3D Orion
- Low-altitude EO/IR sweep role in Phase II
- Detects pop-up threats and executes dynamic COA replanning

### Black Swift S3 VTOL
- Long-range VTOL with extreme weather flight qualification (ongoing through 2026)
- High-altitude relay and long-loiter ISR role in Phase II
- RF sensor detects pop-up SAM threats
- Target platform for mid-mission WASM threat classifier hot-swap demonstration
- All three platforms designed and manufactured in the United States with no PX4/ArduPilot/DJI lineage

### SwiftCore Distributed Pub-Sub Avionics Fabric
- DDS-compatible interface (supports RTI Connext DDS Cert at DO-178C Level A standard)
- Zenoh evaluation planned for Phase II (reported 64% smaller wire overhead than DDS)
- Deterministic temporal contracts on each topic (QoS, reliability mode, deadline)
- Single unified bus across three platforms enables cross-platform fleet awareness
- Fault containment superior to monolithic centralized flight stacks

## Use Cases & Applications

**Five Enumerated Contingency-Driven Use Cases (Phase I Task 1):**

1. **Corrupt Course of Action (COA) Generation** - Faulted autonomy producing unsafe trajectory recommendations (e.g., airspace deconfliction violations)
2. **Platform Hardware Fault** - Sensor degradation, actuator anomaly, or avionics failure detected via RTAA monitor
3. **Pop-Up Threat Detection and Broadcast** - Fleetmate RF or optical sensor detects emerging threat and broadcasts on fleet pub-sub bus; other platforms' monitors detect COA/threat envelope conflict
4. **Unforeseen Mission Change** - Ground command or AWACS broadcasts new mission parameters; platform autonomy lacks trained model for new conditions
5. **Jamming-Induced Sensor Inconsistency** - Multi-sensor fusion fails under adversarial jamming; redundant observations diverge

**Phase II Demonstration Scenario**: Contested area cooperative ISR with three platforms:
- **Phase A (Nominal)**: Three platforms execute pre-planned ISR COA; baseline monitoring establishes false-alarm baseline
- **Phase B (Pop-Up Threat)**: Red-team SAM activates; S3 RF sensor detects; air-deployed S0 autonomy detects COA conflict; RTAA mitigation activates safe loiter + dynamic replanning; detection-to-mitigation budget ≤ 2 seconds
- **Phase C (Intentional Fault + Hot Swap)**: Backpackable S0 fed corrupted threat model (violates airspace deconfliction); RTAA detects and triggers return-to-base. In parallel, freshly trained WASM threat classifier uplinked to S3 mid-mission, validated via signing chain, loaded into sandbox, brought online only after monitor acceptance

**Operational Context**: Addresses Ukrainian field experience demonstrating autonomous platforms become obsolete in days without capability to push model and behavior updates at consumer software cadence. BST approach provides same agility as field-hardened Ukrainian systems (Saker Scout, Skynode, Swarmer) but under formal real-time safety assurances.

## Key Results (Anticipated - Phase I Plan)

This is a proposal, not a completed study, but deliverables planned include:

**Phase I (6 months)**:
- **Task 1** (M1-M2): ASTM F3269-21 clause-by-clause conformance matrix; Open Mission Systems (OMS) interface alignment table; five use case definition sheets with observable signatures, temporal logic specifications, recovery control functions, success/false-alarm criteria
- **Task 2** (M2-M4): WASM static validator (rejects unsafe instruction sequences); hardware-backed signing chain; Nix flake producing bit-for-bit reproducible SwiftCore RTAA base image across independent build hosts
- **Task 3** (M3-M5): Desktop simulation against three of five use cases; 100+ simulated flight hours per use case; measured detection latency, detection probability, false alarm rate. **Target: <0.5 nuisance trips per 100 flight hours** (per ASTM F3269 §1.5.6)
- **Task 4** (M5-M6): ACT3 act3-ace interoperability demonstration (wire-level or runtime); Phase II Technology Development Plan with milestone schedule, risk register, transition partner identification, TRL target (TRL 6)

**Phase II (Projected)**:
- Zero false alarms over 10 cumulative flight hours of cooperative flight
- Detection latency ≤ 100 ms (95th percentile) at pub-sub layer
- Detection-to-mitigation latency ≤ 2 seconds end-to-end
- WASM load/validate/activate cycle ≤ 500 ms
- Full mission reproducibility from single Nix content-addressed manifest across three airframes
- ASTM F3269-21 conformance evidence package (every clause)
- Technology Readiness Level 6 (flight demonstration in relevant environment)

## Notable Details

**Competitive Advantages & Positioning**:
- **Vertical Integration**: BST designed three full avionics product lines under controlled integration with no Chinese or non-allied component dependencies and no PX4/ArduPilot/DJI lineage
- **Principal Investigator Pedigree**: Jack Elston designed his first autopilot in 2003; led design of three avionics systems through flight qualification
- **SBIR Track Record**: Eight prior SBIR contracts (USAF, NASA, NOAA, AFWERX) including current Phase II on tactical weather drones, soil integrity assessment for C-130 expedient airfields, avionics health monitoring
- **Technology Maturity**: All three demonstration platforms (S0 backpackable, S0 air-deployed, S3 VTOL) already in operational or pre-operational use; not a prototype

**Standards and Compliance**:
- **ASTM F3269-21**: Primary certification anchor; BST treats the 2020 Schierman/Barron JGCD paper as touchstone and traces all architectural decisions to defensible deltas against its framing
- **Open Mission Systems (OMS)**: Phase I deliverable includes alignment table mapping SwiftCore pub-sub topics to OMS message classes
- **Autonomy Government Reference Architecture (A-GRA)**: RTAA fabric designed as complementary assurance wrapper around any A-GRA conformant autonomy stack (demonstrates explicit interoperability with Shield AI Hivemind on YFQ-44A and Collins Sidekick on YFQ-42A)
- **AFRL ACT3 Interoperability**: Objective 5 mandates either runtime interoperability or wire-level compatibility with act3-ace reference toolchain; conformance evidence released in ACT3-compatible format
- **DO-178C/DO-330**: NixOS reproducible builds materially reduce tool qualification burden by providing certification authority a single content-addressed manifest that is the deployed binary

**Prior Art Landscape & BST Delta**:
The proposal extensively cites foundational work:
- **Simplex & Descendants**: Lua Sha (CMU, 1990s) established architectural pattern; Phan (Stony Brook) extended to RL; Mehmood et al. (2024) introduced Black Box Simplex; Ghori et al. (2022) presented distributed version for multirotor with formal definition
- **AFRL Aerospace Systems Directorate**: Schierman/Barron (2016) Runtime Assurance Framework Development (AFRL-RQ-WP-TR-2016-0001); 2020 JGCD paper defining four RTA levels
- **NASA Runtime Assurance**: Armstrong GCAS/EVAA (Skoog legacy); Copilot 3 temporal logic monitor compiler (Perez, NASA TM 2020-220587)
- **DARPA Lineage**: HACMS (seL4 microkernel retrofit), CASE (AADL tooling), Assured Autonomy (learning-enabled CPS assurance