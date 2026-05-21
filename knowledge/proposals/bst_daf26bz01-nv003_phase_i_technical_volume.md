# S3-EW: A Modular Payload Vehicle for Agile Electronic Warfare Swarms with VTOL Ground Launch from Confined Terrain

## Document Metadata
- **Type**: SBIR Phase I Technical Volume (Proposal)
- **Client/Agency**: U.S. Department of the Air Force (DAF)
- **Program/Solicitation**: DAF26BZ01-NV003; DSIP Proposal #[TBD]
- **Date**: May 21, 2026 (created/modified)
- **BST Products/Systems Referenced**: S3 (production platform), S3-EW (proposed EW variant), S2, S0, S0-VTOL, SwiftCore FMS (SwiftPilot, SwiftTab, SwiftStation), DS-GPS, AeroPod (implied via modular payload)
- **Key Personnel**: 
  - Dr. Jack Elston (PI, CEO) — ≥30% LoE
  - Dr. Maciej Stachura (Co-Investigator, CTO) — ≥25% LoE
  - Mechanical/Structural Lead [TBD]
  - RF/Payload Engineer [TBD]
  - SkyMesa Systems lead engineer (subcontractor POC: Arthur Shune, unverified)

## Executive Summary

Black Swift Technologies proposes the S3-EW, an electronic-warfare variant of the production BST Swift S3 multi-mission VTOL fixed-wing UAS, to satisfy DAF Topic NV003 requirements for a low-cost, ground-launched small UAS (Group 3 and below) capable of rapid payload reconfiguration and cooperative swarm operations (3–10 vehicles). The baseline S3 already meets or exceeds all published KPPs (≥5 lb payload, ≥45 min endurance, ≥100 km range, ≤5 min deployment) with a 4 m wingspan that enables antenna baselines one order of magnitude larger than quadcopter competitors, a 20,000 ft ceiling for RF horizon extension, native VTOL launch/recovery from austere terrain, and 110 min maximum endurance. Phase I will retire feasibility risks through system architecture definition, antenna integration feasibility, SIGINT payload trade-space, and swarm CONOPS simulation, culminating in a Phase II flight demonstration and transition plan.

## Technical Approach

**Platform Foundation**: The S3-EW is built on the production S3 airframe, a composite VTOL fixed-wing aircraft with:
- Wingspan: ~4 m
- Payload capacity: 2.7 kg (6 lb) demonstrated
- Maximum endurance: 110 min (90 min nominal)
- Service ceiling: 20,000 ft MSL
- Maximum range: 110 km (60 nm)
- Wind tolerance: 30 kt (15 m/s)
- IP42 ingress protection
- Field deployable from transport case in <5 minutes

**Seven Phase I Tasks**:

1. **Task 1 — System Architecture & Modular Payload Interface**: Define block diagram, operating concept, requirements traceability to NV003 KPPs, and Interface Control Document (ICD) Rev. A specifying power (28 V regulated, 12 V auxiliary, 5 V signaling), high-speed data (10 GbE for SDR, 1 GbE for C2, CAN-FD for status), time distribution (PPS + IRIG-B), mechanical mount, and RF feed pass-through.

2. **Task 2 — Quick-Assembly/VTOL Field Deployment**: Define hardened transport case, tool-free assembly sequence (wing-fuselage captive fasteners, rotor-arm latching, payload tray insertion, antenna connection, battery hot-swap), 300-second deployment time budget with margin, and two-person operator workflow at SOF/USAF technician skill level. Leverages S3's existing rapid-deployment pedigree from civilian field campaigns.

3. **Task 3 — Antenna Feasibility Study** (core technical task): Trade conformal antenna integration approaches (printed dipole arrays, tapered-slot elements, FSS-loaded flexible polyimide films, fragmented apertures, additive-manufactured structural antennas) exploiting the ~4 m wingspan. Baseline design: multi-element conformal array distributed along wing leading edge (up to 4 positions per wing, ~4 m maximum baseline). Support frequency coverage HF/VHF/UHF/L/S/C bands. At 300 MHz (lower UHF), 4 m baseline ~4 wavelengths for sub-degree DF; at 1 GHz, ~13 wavelengths for high DF accuracy. Objective configuration: wing-tip pods, fuselage spiral/sinuous elements for hemispherical coverage, EA antenna for Phase II. Deliverables: antenna trade matrix, baseline/objective configurations, simulated radiation patterns at 100/300/900/1500/2450 MHz via method-of-moments/FDTD, DF accuracy bounds using Cramér–Rao lower bound (CRLB) framework, composite-layup impact assessment (carbon-fiber proximity, embedded ground planes, radome cutouts), anechoic-chamber calibration plan.

4. **Task 4 — SIGINT/EW Payload SWaP-C Trade**: Baseline SIGINT payload definition: wideband dual-channel coherent SDR (30 MHz to 6 GHz minimum, growth to ≥18 GHz), low-noise RF front end with multi-octave preselection, multi-channel coherent reference oscillator, edge compute module for real-time energy detection/classification/cued I/Q recording, SSD storage. Vendors evaluated include Sidekiq Z3u-class form factors (basis for USSOCOM Modular Payload MP/MPx SIGINT/EW units). Mass closure straightforward; thermal constraint more demanding (25 W avg / 40 W peak requires conduction path to wing/fuselage). Time/frequency reference: chip-scale atomic clock (CSAC, SA.45s-class) for inter-aircraft TDOA/FDOA coherence, GNSS-disciplined when available, holdover-capable otherwise. CSAC expected to reduce localization error 20–30% at SNRs of interest. Candidate EA payload reserved for Phase II growth. SWaP-C budget (shown below) closes within S3 MTOW envelope with ≥10% mass margin at Phase I CDR.

**S3-EW SWaP-C Budget Summary:**
| Subsystem | Mass | Power (Avg/Peak) | Notes |
|-----------|------|-----------------|-------|
| Airframe + propulsion | ~5.8 kg | per battery | Baseline S3; carbon/composite hosts conformal antennas |
| Energy / battery | ~2.2 kg | — | 90-min nominal endurance; smart BMS; hot-spare |
| SwiftCore avionics | ~0.6 kg | 15 W / 25 W | SwiftPilot, IMU/GPS, datalink modem; no change |
| SIGINT payload | ~1.4 kg | 25 W / 40 W | RF front end + SDR + edge processor; vendor trade |
| Antenna array + RF cable | ~0.4 kg | passive | Wing-embedded conformal; Task 3 output |
| Comms / inter-aircraft link | ~0.2 kg | 5 W / 10 W | MANET-style mesh; growth to encrypted Type-1 Phase II/III |
| **Margin** | **~0.7 kg** | — | **≥10% mass margin at CDR** |
| **Total** | **≤11.3 kg MTOW** | **45 W avg / 75 W peak** | **Closes within S3 envelope** |

5. **Task 5 — Swarm CONOPS & Cooperative Geolocation Feasibility**: Define 3–10-aircraft swarm CONOPS with single ground-station cue, leveraging SwiftCore cooperative-control heritage (VORTEX2 tornado interception, CRATER NASA multi-aircraft volcanic mission at Poás, four-aircraft Hurricane Ernesto 2024 deployments). Inter-aircraft data link: low-probability-of-intercept MANET 1.3–2.4 GHz band (growth to encrypted Type-1). Swarm time-sync and SwiftCore mission orchestration with dynamic baseline reconfiguration as aircraft attrit. Simulate cooperative DF, TDOA, and FDOA geolocation accuracy using published CRLB (Ho/Chan family for constrained TDOA/FDOA, UAV-swarm-specific A-optimality derivations). Parameterize: aircraft count (1, 2, 3, 5, 7, 10), standoff range (5, 10, 20, 50 km), inter-aircraft separation (1, 5, 10, 25 km), SDR sampling characteristics, sub-microsecond time-sync error (CSAC-disciplined). **Preliminary analysis**: three S3-EW aircraft separated 5–10 km with CSAC-disciplined SDRs achieve TDOA/FDOA geolocation accuracy 100–300 m at 20–30 km standoff against narrowband cooperative emitters (consistent with published Group 2 SIGINT performance). Define autonomous sensor-based-control behaviors: line-of-bearing intersection, fly-to-maximize-geometry maneuvers, emitter-tracking patterns (direct descent from Stachura's PhD cooperative communication-relay control law).

6. **Task 6 — Subcontractor Integration (SkyMesa Systems)**: SkyMesa (RF software subcontractor) contributes software-defined RF geolocation, emitter-tracking algorithms, and adaptive signal processing for detection under strict time/resource constraints. Integration model: receiver I/Q data in → bounded cues out with confidence and audit trail, operator-in-the-loop workflow. SkyMesa hardware-agnostic, software-first complement to BST full-stack hardware. Define BST/SkyMesa interface (SDR I/Q stream format, metadata wrapper with UAS pose/time/frequency plan, geolocation-cue output consumed by SwiftCore). Phase II software-in-the-loop testing and Phase II/III teaming-agreement scope. **Note**: SkyMesa due-diligence open items (legal entity, UEI/CAGE, POC Arthur Shune verification, prior contracts) flagged in Author's Notes; fixed-scope teaming agreement signed at Phase I kickoff; if any item fails, BST retains back-up to bring geolocation in-house using DS-GPS heritage staff.

7. **Task 7 — Risk Management & Phase II Planning**: Monthly risk register, Phase I risk closure via mitigations (shown below), Phase II Statement of Work, flight-test plan, and cost volume.

**Phase I Risk Register** (simplified):
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Antenna pattern degradation from composite wing (carbon-fiber proximity) | Medium | High | Subtask 3.6 EM-simulates as-built layup; Cu-mesh ground planes, radome cutouts validated pre-tooling |
| SWaP budget overrun (SIGINT mass/thermal) | Medium | High | ≥10% mass margin at CDR; thermal conduction path designed with margin (Task 4.3) |
| Sensor-based control law convergence (cooperative geolocation maneuvers) | Low | Medium | Reuse VORTEX2/CRATER heritage; SIL before flight test (Task 5) |
| SkyMesa scope creep / due diligence gaps | Medium | Medium | Fixed-scope teaming agreement; ICD frozen at Task 6 closeout; open items tracked |
| Spectrum coordination / FCC STA delays (Phase II RF emissions) | Medium | Medium | Phase I includes spectrum plan; Phase II demos receive-only initially, EA reserved later |
| Anechoic chamber partner availability | Low | Medium | Two partners identified; outdoor far-field range fallback |
| GPS-denied operation (contested environment) | Medium | Low | NOAA DS-GPS SDR signal-of-opportunity heritage; CSAC holdover |
| Key personnel availability (Mech/Struct, RF/Payload) | Medium | Medium | Roles identified; hire-or-subcontract tracked; BST bench depth adequate |

## Products & Capabilities Described

### S3-EW (Electronic Warfare Variant of S