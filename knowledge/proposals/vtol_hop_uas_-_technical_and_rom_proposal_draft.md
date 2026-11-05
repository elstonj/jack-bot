# VTOL Hop UAS - Technical and ROM Proposal

## Document Metadata
- **Type:** Technical proposal and rough order of magnitude (ROM) cost estimate
- **Client/Agency:** [Customer name and office] – TBD
- **Program/Solicitation:** Appears to be NOAA-related (reference to 2026 IDIQ in file path)
- **Date:** 4 November 2026
- **BST Products/Systems Referenced:** SwiftCore FMS, S0-VTOL, S3, S2, 430 MHz Microhard P400 command and data link
- **Key Personnel:** Jack Elston (last editor)
- **Status:** Draft for internal review; all values are planning estimates

---

## Executive Summary

Black Swift Technologies proposes a purpose-built hybrid lift-plus-cruise VTOL UAS carrying a 10–15 lb payload in a 1 ft³ bay, capable of ~100 mi transit legs with vertical takeoff and landing from land or ship. The concept meets threshold requirements (200–250 mi range at 80+ kt) using four electric lift rotors and a 7–8 kW combustion cruise engine with onboard generator; objective performance (400–500 mi, 120 kt) is achievable with increased fuel load. Development timeline is 9–10 months to first flight and 12–15 months to land-based threshold demonstration at an estimated cost of $1.8M–$2.8M for design and two prototypes.

---

## Technical Approach

### Configuration
- **Airframe:** Twin-boom lift-plus-cruise VTOL with 13–15 ft wingspan, 8–9 ft length
- **Lift system:** Four ~28 inch electric lift rotors on the booms, powered by a high-discharge lift battery (~1 kWh); rotors stop and lock in line with booms during cruise
- **Cruise propulsion:** Rear-mounted pusher engine, 7–8 kW (10 hp) class combustion; engine-driven ~0.5 kW generator recharges lift battery and powers payload/avionics during cruise
- **Payload bay:** ~10 × 10 × 17 in (1 ft³) internal bay using S2-derived field-swappable power, data, and mechanical interface
- **Airframe materials:** Composite construction with non-conductive skins in selected areas; shaped surfaces and shielded engine bay for low-observable design
- **Tail:** V or inverted-V configuration

### Rationale for Configuration
- **Tailsitter configuration rejected:** Higher risk for gusty and moving-deck recovery
- **Tiltrotor configuration rejected:** Higher mechanical complexity, cost, and schedule risk for first article

### Weight Estimate (Table 4)
| Element | Threshold (lb) | Objective Range (lb) |
|---------|---|---|
| Payload | 15.0 | 15.0 |
| Fuel (incl. 20% reserve) | 10.0 | 20.0 |
| Structure | 17.5 | 20.0 |
| Cruise engine, generator, exhaust, tank | 9.0 | 9.5 |
| Lift motors, rotors, controllers | 7.5 | 8.0 |
| Lift battery | 8.5 | 8.5 |
| Avionics, datalink, wiring | 3.5 | 3.5 |
| **Maximum Takeoff Weight** | **71.0** | **84.5** |

- Aircraft classified as small Group 3 UAS at these weights
- Weight budget carries 10% growth margin in structure and fuel

### Mission Profile
1. Vertical takeoff from land site or ship deck; transition to wing-borne flight
2. Cruise ~100 mi at 85–95 kt, up to 5,000 ft; dash capability to 120 kt; generator recharges lift battery in-flight
3. Transition and vertical landing at remote site, or brief touch with rotors powered
4. Payload operation on ground; engine running or shut down (TBD)
5. Vertical takeoff; return or continue to next site
6. Vertical recovery at origin or on ship deck

**BST Interpretation of Range Requirement:** 200–250 mi threshold = ~100 mi outbound + one site landing + ~100 mi return + 20% fuel reserve

### Performance Envelope (Strawman Specification, Table 3)

| Parameter | Value |
|-----------|-------|
| **Flight Performance** | |
| Best-range cruise speed | 85–95 kt |
| Dash speed | 120 kt |
| Range | 250 mi threshold (20% reserve); 400–500 mi objective |
| Endurance | ~3 h threshold; 5–6 h objective |
| Operating altitude | 5,000 ft MSL with hot-day VTOL margin |
| VTOL cycles per sortie | 2 minimum by design; additional with in-flight recharge |
| VTOL wind limit | 25 kt sustained (goal) |
| **Payload & Power** | |
| Payload capacity | 10–15 lb internal, 1 ft³, field-swappable |
| Payload power | 200–500 W continuous (pending payload breakdown) |
| **Propulsion** | |
| Cruise engine | 7–8 kW combustion; JP-5/JP-8 heavy-fuel variant for shipboard |
| Lift rotors | 4 × ~28 in; 8–9 kW peak electrical |
| Lift battery | ~1 kWh |
| Generator | ~0.5 kW onboard (sized with growth path) |
| **Navigation & Control** | |
| Flight management | SwiftCore FMS (STM32/FreeRTOS flight tier, Linux mission tier) |
| Navigation | GNSS/INS, RTK precision landing, relative navigation for moving-deck recovery |
| Comm/datalink | 430 MHz Microhard P400 line-of-sight; SATCOM for beyond-horizon legs |
| **Airframe** | |
| Wingspan | 13–15 ft (4.0–4.5 m) |
| Length | 8–9 ft |
| Configuration | Composite twin-boom, V/inverted-V tail, pusher engine |

---

## Products & Capabilities Described

### SwiftCore Flight Management System
- **What it is:** BST-developed flight control and autonomy platform running STM32/FreeRTOS for flight tier and Linux for mission tier
- **Heritage:** Flown on all BST aircraft; VTOL-to-wing transition control demonstrated on S0-VTOL and S3
- **Proposed use:** Primary flight control, automated transition, autonomous mission execution, precision landing capability
- **Specifications:** Capable of RTK precision landing and relative navigation for moving-deck operations

### S2 Field-Swappable Payload Interface
- **What it is:** Common power, data, and mechanical interface standard developed for S2 platform
- **Proposed use:** Define VTOL Hop UAS payload bay (~10 × 10 × 17 in) with commonality to S2 interface for field payload swaps
- **Benefit:** Enables rapid payload reconfiguration without airframe modifications

### 430 MHz Microhard P400 Command and Data Link
- **What it is:** Long-range line-of-sight command and data link
- **Heritage:** Tested to 400 km air-to-air on BST aircraft
- **Proposed use:** Primary C2 and telemetry link for near-range operations
- **Limitation noted:** Line-of-sight radio horizon at 5,000 ft is ~90–95 mi; legs exceeding ~100 mi require supplementation
- **Mitigation:** SATCOM link planned for beyond-horizon segments; optional airborne relay

### S0-VTOL and S3 VTOL Fixed-Wing Aircraft
- **Heritage:** S0-VTOL operated by NOAA and USAF; S3 long-range VTOL fixed-wing platform
- **Proposed use:** Inform lift system sizing, transition envelope definition, and VTOL operations procedures
- **Relevant capability:** Severe-environment operations (S0 demonstrated in tropical cyclones including 240 mph wind measurement in Hurricane Milton 2024)

### Avionics & Navigation Subsystems
- **GNSS/INS:** Inertial navigation for standoff periods when GNSS denied
- **RTK precise positioning:** For field landing site accuracy
- **Relative navigation capability:** For moving-deck (ship) recovery using deck-motion reference

---

## Use Cases & Applications

### Primary Mission Profile
- **Maritime/shipboard operations:** Vertical launch and recovery from ship decks; moving-deck VTOL recovery capability required
- **Remote site surveys:** ~100 mi transit legs to reach remote observation sites; intermediate landing and re-launch cycles
- **Multi-hop missions:** Design supports minimum 2 VTOL cycles per sortie; additional cycles with in-flight battery recharge
- **Payload delivery or remote observation:** Ground time at remote sites with engine on/off configurable

### Environmental/Severe-Weather Operations
- **Tropical cyclone operations:** BST heritage in hurricane sampling (S0 verified 240 mph wind measurement in Hurricane Milton 2024)
- **Cold-weather operations:** BST heritage in Arctic and Greenland operations (S2)
- **Wind envelope:** 25 kt sustained wind limit (goal); design envelope for gusty maritime conditions

### Airspace & Range Requirements
- **Restricted/warning-area flight:** Test plan built around restricted or warning-area airspace; NASA airspace deconfliction and Navy VACAPES coordination experience from S3
- **Over-water operations:** Experience on S3 and prior platforms

---

## Key Technical Risks and Mitigations

### High-Risk Items (Table 6)

| Risk ID | Risk | Likelihood | Consequence | Mitigation |
|---------|------|------------|-------------|-----------|
| K-1 | Combustion propulsion integration (vibration, cooling, EFI, generator) is new to BST | Medium | **High** | Engine/generator test stand in Phase 1; small-engine integration subcontractor; vibration-isolated avionics |
| K-2 | Parked lift rotors and booms limit cruise L/D and 120 kt dash | **High** | Medium | Rotor lock aligned with booms; faired boom-motor nacelles; CFD in Phase 0; 120 kt treated as dash (not cruise) |
| K-5 | Moving-deck VTOL recovery in wind and sea state | Medium | **High** | RTK relative navigation; deck-motion-tolerant gear; land-based moving-platform tests before ship trials |
| K-6 | RCS value cannot be guaranteed before measurement; engine and lift motors are dominant returns | **High** | Medium | Low-observable design practice; RCS measurement at outdoor/compact range in Phase 4 |
| K-7 | Line-of-sight radio horizon at 5,000 ft is ~90–95 mi; 100 mi legs exceed it | **High** | Medium | SATCOM link for beyond-horizon segments; optional airborne relay |
| K-11 | Program requires ~5 dedicated FTE from 12–14 person company | Medium | **High** | Phased hiring tied to award; subcontract non-core work |

### Medium-Risk Items
- K-3: Weight growth mitigation via budget tracking and 10% margin in structure/fuel
- K-4: Heavy-fuel requirement (ship vs. land variants); gasoline for land ops, heavy-fuel as option
- K-8: Payload power/thermal loads undefined; generator sized at 0.5 kW with growth path
- K-9: Hot-day VTOL performance at 5,000 ft; lift system sized with 30% thrust margin
- K-10: Group 3 weight class affects test approvals; approvals planning in Phase 1

---

## Schedule

| Phase | Duration (Months ARO) | Content | Exit Criterion |
|-------|---|---|---|
| 0 - Requirements & Sizing | 0–2 | Requirements lock, payload power breakdown, configuration trade, engine selection, CFD | Concept Design Review |
| 1 - Preliminary Design & Risk Reduction | 2–6 | Engine/generator test stand, lift thrust testing, structural sizing, payload bay mockup, test approvals initiated | Preliminary Design Review |
| 2 - Detailed Design & Fabrication | 6–10 | Tooling, two prototype air vehicles, avionics integration, ground and tethered hover tests | Critical Design Review; first hover |
| 3 - Flight Test (Land) | 10–15 | Hover, transition, envelope expansion, range & multi-landing demo, precision landing | **Threshold Demonstration** |
| 4 - Ship & Signature (Option) | 15–20 | Moving-deck trials, heavy-fuel variant, RCS measurement, objective range | Ship Demonstration |

- **First flight:** 9–10 months after award
- **Land-based threshold demonstration:** 12–15 months after award

---

## Rough Order of Magnitude (ROM)

### Base Effort (Phases 0–3): Design, Two Prototypes, Land Demonstration

| Scope | Content | Duration | ROM |
|-------|---------|----------|-----|
| Labor | ~5 dedicated FTE | 15 months | $1.20M–$1.60M |
| Materials & Hardware | Tooling, engines, lift system, avionics, datalinks, two air vehicles | Phases 1–3 | $0.35M–$0.60M |
| Subcontracts & Test | Engine integration, CFD/wind tunnel, test range, travel | Phases 0–3 | $0.25M–$0.60M |
| **Base Total** | **Design, two prototypes, land demonstration** | **15 months** | **$1.8M–$2.8M** |

### Option (Phase 4): Ship Trials, RCS Characterization, Objective Range
- **ROM:** $0.5M–$1.0M, 4–6 additional months

### Recurring Unit Cost (Air Vehicle Only)
- **Low-rate production:** $90k–$150k per aircraft
- *Excludes payload and ground segment*

### Assumptions for ROM
- Government-provided range access
- Ship access for Phase 4
- Payload simulators or interface definitions provided

---

## Assumptions and Open Items

### Key Assumptions
1. **Threshold mission definition:** One ~100 mi outbound leg + one site landing + one ~100 mi return leg + 20% fuel reserve
2. **VTOL cycles:** Two minimum per sortie at threshold; additional cycles supported by in-flight lift-battery recharge
3. **Operating altitude:** 5,000 ft MSL; standard day plus hot-day VTOL margin
4. **Payload:** 15 lb at 1 ft³; power 200–500 W (pending payload breakdown)
5. **Airspace:** Land-based testing in restricted or warning-area airspace
6. **Export controls:** Range above 300 km falls under EAR 9A012 controls (S2 classified under this regulation)

### Open Items for Customer
1. Confirm whether ~100 mi is one leg of out-and-back or the length of each hop
2. Number of landings/touches per sortie, ground time per site, engine state on ground
3. **Payload breakdown:** Power, thermal, field of view, aperture; whether payloads are delivered or retained
4. **Ship requirements:** Ship class, deck size, sea state for recovery; mandatory heavy fuel requirement?
5. **RCS specification:** Quantitative RCS goal and frequency band, or acceptance of low-observable design practice?
6. Quantity and fielding date

---

## Relevant BST Heritage and Capabilities

| Capability | Heritage | Application to VTOL Hop UAS |
|-----------|----------|---------------------------|
| **SwiftCore FMS** | All BST aircraft; VTOL transition flown on S0-VTOL, S3 | Flight control, transition, autonomy, precision landing |
| **VTOL fixed-wing aircraft** | S0-VTOL (NOAA, USAF); S3 long-range VTOL | Lift system sizing, transition envelope, VTOL operations |
| **Field-swappable payload interface** | S2 common power/data/mechanical interface | Payload bay and payload integration |
| **Long-range command and data link** | 430 MHz Microhard P400, tested to 400 km air-to-air | Line-of-sight C2 and telemetry |
| **Severe-environment operations** | S0 tropical cyclones (240 mph in Hurricane Milton 2024); S2 Arctic/Greenland; S3 cold-weather | Ruggedization, maritime, wind envelope |
| **Airspace coordination** | NASA deconfliction (S3); Navy VACAPES warning-area ops | Test range and over-water operations |

### Key Differentiators from Current BST Portfolio
- Current BST platforms: payloads up to 2.7 kg (6 lb, S3); all-electric
- VTOL Hop UAS introduces: **combustion cruise propulsion** and **payload class 2–3× larger** than current platforms

---

## Notable Details

### Design Philosophy
- **Hybrid propulsion strategy:** Electric lift (high power density for VTOL), combustion cruise (fuel density for range) with in-flight battery recharge to enable multiple VTOL cycles per sortie
- **Low-observable design approach:** Composite airframe, non-conductive skins, shaped surfaces, shielded engine bay; engine and lift motors identified as dominant RCS contributors
- **Ship-friendly variant:** Heavy-fuel (JP-5/JP-8) combustion engine option for maritime deployments

### Payload Flexibility
- **Standardized interface:** Derives from S2 to enable rapid field-swappable payload configurations
- **Power growth path:** Generator sized at 0.5 kW with growth capability for future higher-power payloads
- **On-ground flexibility:** Payload operation with engine running or shutdown configurable based on mission

### Airspace & Regulatory Posture
- **Group 3 classification:** 55–150 lb category impacts test approvals and range access; mitigated via restricted/warning-area planning
- **Export control awareness:** BST recognizes EAR 9A012 applicability to systems with range >300 km
- **Approvals strategy:** Test plan coordination with NASA and Navy precedent; approvals timeline starts Phase 1

### Staffing & Execution
- **Resource-constrained execution:** ~5 dedicated FTE from a 12–14 person company; mitigated via phased hiring and strategic subcontracting of non-core work (engine integration, CFD/wind tunnel)

### Future Ship Trials Option
- Phase 4 option addresses objective-range mission (400–500 mi, 120 kt) via:
  - Ship-deck VTOL recovery with moving-platform techniques
  - Heavy-fuel propulsion variant for naval logistics
  - RCS characterization at outdoor/compact range
  - Objective-range demonstration over multiple hops

---

## Document Quality Notes

- **Status:** Draft for internal review; all values are planning estimates (non-binding)
- **Completeness:** Well-structured with clear requirements baseline, technical trade rationale, comprehensive risk register, and realistic schedule
- **Payload definition gaps:** Critical open items around payload specifications (power, thermal, delivery vs. retention) that will drive final design in Phase 0
- **Customer coordination required:** Many design decisions (fuel type, RCS goals, ship class, mission hopping pattern) carry significant cost and schedule implications and require early customer definition