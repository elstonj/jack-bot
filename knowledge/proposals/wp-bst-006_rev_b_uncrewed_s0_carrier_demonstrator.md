# WP-BST-006 Rev B: Uncrewed S0 Carrier Demonstrator

## Document Metadata
- **Type:** Capability whitepaper / proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations (OMAO) / Uncrewed Systems Operations Center (UxSOC); NOAA OAR Atlantic Oceanographic and Meteorological Laboratory (AOML)
- **Program/Solicitation:** NOAA IDIQ 1305M226D0012 (OMAO/UxSOC); potentially Phase III SBIR under 15 U.S.C. § 638(r); related to NAVAIR N251-016 and STTR N6833525C0270
- **Date:** October 28, 2026 (Revision B; supersedes August 19, 2026 issue)
- **BST Products/Systems Referenced:** S0 (primary payload), S2, S3, SwiftCore (autonomy), SwiftPilot, SwiftTab (operator displays), series-hybrid propulsion architecture
- **Key Personnel:** Jack Elston (preparer/editor); Dan, Brian, Josh, Maciej referenced in internal review section
- **Document Status:** Internal review checklist included; some sections flagged as provisional pending BOE, schedule confirmation, and partner coordination

## Executive Summary

Black Swift Technologies proposes a purpose-built, uncrewed carrier aircraft to transport, release, and relay S0 micro air vehicles into tropical cyclones, enabling persistent (24-hour) boundary-layer observations through the final days before landfall. A four-aircraft rotation would keep at least one S0 continuously on station, compared to the current ~18 S0 flight hours against 417 WP-3D hours in the 2025 season. The demonstrator (600–800 lb, 12-hour endurance) is deliberately smaller than the eventual operational aircraft and designed to prove release, relay, hazard avoidance, propulsion in rain, and storm survival; measured results determine whether the operational aircraft is built by BST or specified to a strategic partner. The program is gated at five decision points, allowing NOAA to halt with useful outputs (improved S0 systems, satellite data link, wing-pod carriage) at any gate.

## Technical Approach

### Carrier Design Philosophy
- **Observation-driven:** Requirements derived from storm environment and S0 mission, not inherited from existing airframes.
- **Demonstrator-first strategy:** 600–800 lb aircraft proves storm-critical functions (release, relay, hazard avoidance, propulsion in rain) at a size that retires design risk; scaling to 1,200–2,000 lb objective aircraft is low-risk once demonstrator proves concept.
- **Purpose-built vs. adapted:** Rejected alternatives (MQ-9, converted light twins, rugged military UAS, high-altitude platforms) as either oversized, structurally inadequate for eyewall gusts, or misaligned with mission.

### Storm-Hardened Propulsion & Power
- **Series-hybrid electric architecture:** Twin heavy-fuel generator sets in sealed nacelles with heated intakes and inertial separators, driving electric motors via power electronics. Motors are proven in S0 operations through eyewall rain and sea spray.
- **Multi-path redundancy:** Either generator can hold altitude alone; battery bridge covers generator wet-outs; immediate thrust response to downdrafts without engine spool-up.
- **Rationale:** Single-engine aircraft inside an eyewall has no recovery from power loss. Electric propulsion proven in hostile environment.

### Gust Load & Structural Design
- **Design case:** +6 g / −3 g limit loads (derived from WP-3D/Hugo data showing +5.8 / −3.7 g).
- **Gust-load formula:** 20 m/s gust adds ~2.6 g to demonstrator (vs. ~1.2 g WP-3D, ~2.0 g MQ-9A at 10,000 ft).
- **Active mitigation:** Gust-load-limiting autopilot detects and slows to turbulence-penetration speed.
- **Materials/approach:** Uncrewed structure carries gust loads at modest weight cost; CTE 2 includes coupon and wing-section static tests, salt/humidity exposure coupons, and weight build-up validation.

### Storm Penetration & Navigation
- **Crossing max winds:** Radial legs are mostly crosswind in high-wind fields (tangential winds dominate). Aircraft crabs into wind and still makes progress toward eye. Where wind exceeds airspeed, wind-aware guidance plans upstream entry point so drift ends at release point.
- **Dash speed trade:** Every 10% increase in airspeed adds ~10% to gust load. Dash speed and structure set together; intensity requirement and acceptable release-point error above that intensity are Task 1/NOAA decisions.
- **Example penetration table (tangential wind scenarios):**
  - 100 kt tangential wind, 150 kt dash airspeed: 75 kt ground speed toward eye at 60° crab.
  - 170 kt tangential wind, same dash: drifts; requires upstream entry.
- **Contingency:** Routes avoid legs needing headway into strongest winds.

### Icing & Cold Exposure
- **Tropical freezing level:** Typically above 15,000 ft; dominant hazards at 10,000 ft cruise are turbulence and rain.
- **Supercooled liquid water:** Still encountered in climbs, descents, and updrafts; no UAS yet certified for known icing.
- **BST approach:** De-icing heaters (S0 work under Navy STTR N6833525C0270), S3 cold-weather experience (northern Alaska, Greenland salt-spray work), and detection/protection/egress logic as design item rather than assumption.
- **CTE scope:** Includes ice-protection design validation (icing-tunnel testing planned in Option 1).

### Four-Layer Hazard Avoidance Architecture
1. **Planning:** NOAA TDR analyses, coastal NEXRAD, satellite imagery, recon observations define no-go volumes pre-launch; refreshed in flight.
2. **Onboard radar:** Forward-looking X-band Doppler (Garmin GWX 75 class, ~10 lb, ~70 W) flags 45–50 dBZ cores and turbulence ahead.
3. **S0 pickets:** Released S0 fly ahead, report 3-D wind, turbulence, and pressure in real time. (Example: Hugo mesovortex pressure perturbation ~12.5 hPa, measurable by S0, closes radar resolution gap.)
4. **Reactive:** Carrier's own wind and load estimates trigger slowdown, truncated patterns, or egress against approved thresholds.
- **Architectural independence:** Flight-critical C2 independent of relay and science data path; losing relay never costs control.

### Release Mechanism & Carriage
- **Wings-out pylon station:** S0 carried wings-deployed beneath pylon with single release actuator and small hardpoint on S0.
- **Advantage over WP-3D drop tube:** No 8–10 lb of tube, sabot, and release hardware; self-contained S0 and wing-station release enable pod carriage on wider range of crewed/uncrewed aircraft without drop chute.
- **Separation proving:** Progressive—analysis, ground test, captive carry from existing BST aircraft, clear-air drops, then weather.
- **Pre-release health check:** Automated sequence.
- **CTE 3 testing:** Prototype pylon, actuator, hardpoint; ground release tests; captive carry and release of inert S0 from existing BST aircraft.

### S0 Relay & Multi-Simultaneous Operations
- **Current bottleneck:** Two-S0 simultaneous limit on WP-3D set by command-and-telemetry radio channels, not aircraft. BST moved to two simultaneous S0 in 2026 by adding channel.
- **Carrier multi-channel relay:** Sized to number of S0 NOAA wants airborne. Same ground-station upgrade raises WP-3D and C-130J beyond two simultaneous whether or not carrier proceeds.
- **CTE 5 scope:** Bench and ground test of multi-channel 430 MHz relay with four+ live S0 radios alongside flight-critical link and satellite backhaul.

### S0 Direct-to-Cell (D2C) Satellite Data Link
**Phased pilot starting with NOAA request; extends S0 reporting window after host departure.**

**Phase 1 (Base, 6 months):** Prototype + two-unit flight demonstration
- Service: T-Mobile T-Satellite (Starlink Gen1, LTE Band 25); telemetry-rate, capped 15 MB/month on IoT plan; limited to 12 nm offshore without FCC STA.
- Approach: Prototype on carrier board with COTS Band 25 antenna; simple shore endpoint forwarding to NOAA.
- Testing: Clear-air flights over T-Satellite-only area in Colorado (avoids 12 nm limit).
- Gate: Measured link availability, latency, data delivered from two airborne S0.
- Benefit: S0 released at WP-3D mission end can report for another ~2 hours; sortie supports three sequential flights (~12 hrs coverage) instead of two (~8 hrs).

**Phase 2 (Option, offshore WP-3D deployment):** Board respin, flight-grade; requalify for tube launch; route data into NOAA ops path; release beyond 12 nm under STA. Gate: approved STA and Phase 1 results.

**Phase 3 (Option, 2028, Gen2 Starlink Mobile):** Swap to Gen2 module (launches late 2027), retune antenna for 2 GHz, full-rate meteorological + health telemetry. Gate: Gen2 module and service access.

**Design constraints:** Decimated meteorological data + health telemetry only; no video, no BLOS command. Future add-ons scoped separately once throughput measured.

## Products & Capabilities Described

### S0 (Micro Air Vehicle)
- **What it is:** Expendable, released aircraft designed to sample tropical cyclone boundary layer; ~1.2 kg (2.6 lb) mass; ~2-hour endurance; can descend to ~100 ft above ocean on radar altimeter.
- **Operational heritage:** Deployed from WP-3D since October 2023 (Tropical Storm Tammy, 71-minute flight); 37 launches in FY26; dual releases routine; flights past 2 hours; sustained legs 10–15 m above ocean on radar altimeter. Holds uncrewed wind-speed record (240 mph, Hurricane Milton, NCAR-verified). Data entered NOAA operational hurricane model for first time in 2026 season.
- **In this context (carrier):** Primary payload; up to 6 stations on demonstrator, 10–12 on objective aircraft. Pre-release health check performed by carrier; released sequentially by automated logic.
- **Improvements beyond carrier:** D2C satellite link (Phases 1–3); compact S0 radar option (Option 4); wing-pod carriage for non-drop-chute hosts (Option 9).

### SwiftCore (Autonomy/Guidance)
- **What it is:** Onboard autonomy estimating 3-D wind and flying S0 autonomously to maximum wind and storm center.
- **Storm-guided autonomy heritage:** BST founders published guidance for UAS penetration of severe storms (2010–2011), including wind fields stronger than aircraft airspeed; evaluated in hardware-in-the-loop simulation. Flew UAS component of VORTEX2 (2009–2010). SwiftCore guidance developed against high-fidelity simulated hurricane wind and rain fields with NCAR support.
- **Carrier application:** SwiftCore ported to carrier; implements storm patterns, wind-aware guidance with upstream-entry planning, gust-load and icing limiting, contingency/egress logic, four-layer hazard-avoidance architecture.
- **CTE 4 scope:** Replay real TDR, NEXRAD, S0 storm data through hardware-in-the-loop environment with COTS X-band radar model; measure warning time against achievable response (slowdown, turn, egress).

### SwiftTab (Operator Displays)
- **What it is:** Operator display interface.
- **Carrier application:** Ground-station mission planning and real-time monitoring.

### S2 (Existing Small UAS)
- **What it is:** Existing small aircraft that has carried and released NASA Langley CICADA micro air vehicles.
- **Relevant heritage:** First fully autonomous CICADA drop December 17, 2021, after NASA ORR. NASA airworthiness review cleared S2 to carry CICADA to 10,000 ft through cloud; drops repeated 2022.
- **Carrier validation:** Demonstrator will use S2 for captive-carry and release tests of inert S0 (CTE 3).

### S3 (Existing Small UAS)
- **What it is:** Small aircraft with cold-weather, de-ice, salt-spray operational heritage (northern Alaska, Greenland).
- **Relevant heritage:** Environmental qualification under Navy STTR N6833525C0270 (with Embry-Riddle and University of Miami/HRD) covers S0 de-icing heaters, real-time turbulence sensing, adaptive sampling.
- **Carrier application:** Ice-protection and cold-weather design inheritance.

### Hybrid-Electric Propulsion System
- **Components:** Twin heavy-fuel generator sets (sealed nacelles, inertial separators, heated intakes); electric motors and power electronics (same class proven in S0); battery bridge.
- **Specifications:** Either generator holds altitude alone; battery covers wet-out; immediate responsive thrust.
- **Validation:** CTE 1 bench water-spray and ingestion test; one-generator-out and battery-bridge test.

### Forward-Looking X-Band Doppler Weather Radar
- **Type:** Garmin GWX 75 class.
- **Specs:** ~10 lb, ~70 W, flags 45–50 dBZ cores and turbulence ahead.
- **Integration:** Onboard (layer 2 of hazard avoidance); also modeled in hardware-in-the-loop simulation (CTE 4).

### 430 MHz Command & Data Link
- **Heritage:** Tested to 400 km; WP-3D safe-separation tested; AVAPS interference mitigation; operationally proven release mechanics, link budget, RF coexistence, approval path.
- **Demonstrator upgrade:** Multi-channel relay (Task 5, CTE 5) sized to number of simultaneous S0; supports four+ S0 radios alongside flight-critical link and satellite backhaul.

### Storm-Field Hardware-in-the-Loop Simulation Environment
- **What it is:** High-fidelity simulated hurricane wind and rain fields (developed with NCAR support).
- **Use:** Guidance algorithm validation, autonomy testing, hazard-avoidance architecture verification.
- **Carrier tasks:** Tasks 5, CTE 4 implement demonstrator in this environment.

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Boundary-Layer Observation
- **Operational concept:** Four-aircraft rotation keeps at least one S0 on station continuously 24 hours a day through final days before landfall.
- **Current gap:** S0 can be released/relayed only while crewed host (WP-3D) on station. 2025 data: ~18 S0 flight hours vs. 417 WP-3D hours; coverage peaks ~8 hours/day with two sequential S0 per sortie.
- **Proposed benefit:** Continuous observations, including overnight and between crewed fixes. Preliminary NOAA study found ~10% improvement in intensity forecasts from S0 data.

### Operating Area & Basing
- **Initial concept:** U.S.-threatening storms within 300–500 nm of U.S. coast (mostly over U.S. and international waters).
- **Deployment:** Launch from coastal runway with adjoining restricted/warning airspace over water; no overflight of towns.
- **Range:** 12-hour demonstrator holds continuous coverage ~400 nm (all four flying) to ~300 nm (one down), covering NHOP 3-hourly-fix zone. Objective aircraft: ~1,000 nm reach (matching WC-130J sortie average).
- **Caribbean operations:** Require diplomatic clearances; BST to pursue with OMAO later.

### Flight Profile
1. Launch from coastal base.
2. Transit at ~10,000 ft (700 hPa, same as WP-3D/WC-130J).
3. Penetrate storm (eyewall, eye) and release S0 per observing plan.
4. Relay S0 data over 430 MHz; return carrier state + priority observations to NOAA over satellite.
5. Hand off to next carrier; land, reload, turn in ~4 hours.

### S0 Consumption
- **On-station time requirement:** With four aircraft rotating: (aircraft flying) × S ≥ 2 × transit + S + ground turn.
- **Magazine sizing:** On-station times 3–9 hours need only 4–9 S0 per sortie.
- **Storm consumption:** ~18 S0/storm-day; ~36 for final 48 hours before landfall.

### Secondary Applications (Stand-Alone Value)
- **Multi-S0 relay upgrade (Option 8):** Upgrade WP-3D and C-130J ground station + radios to fly >2 simultaneous S0; delivers value whether or not carrier proceeds.
- **S0 satellite link (Options 6–7):** D2C enables S0 to report for ~2 extra hours after host departs; supports three sequential flights (~12 hrs/day) instead of two.
- **Wing-pod carriage (Option 9):** Self-contained S0 in pods on non-drop-chute hosts (crewed and uncrewed); expands deployment platforms.
- **Compact S0 radar (Option 4):** Near-field Doppler rain radar on S0; research objective to assess storm-relative wind recovery from repeated microwave observations of moisture/hydrometeor structure, constrained by S0 in-situ, without full Tail Doppler Radar.

## Key Technical Results & Heritage

### S0 Operational Record (to date)
- **First deployment:** October 2023, Tropical Storm Tammy, WP-3D drop, 71-minute flight, descended to ~100 ft.
- **FY26 launches:** 37 total, dual releases routine, flights >2 hours, sustained low-altitude legs (10–15 m radar altimeter).
- **Wind record:** 240 mph, Hurricane Milton (NCAR-verified).
- **Data assimilation:** Entered NOAA operational hurricane model for first time in 2026 season.
- **2025 hurricane season:** 63 flights into six hurricanes, 417 crewed WP-3D hours vs. ~18 S0 hours (showing persistence gap).

### Prior Uncrewed Operations in Severe Weather
- **VORTEX2 (2009–2010):** BST flew UAS component, placing aircraft around supercells with mobile Doppler radar in loop.
- **S2/CICADA air-launch:** First fully autonomous drop December 17, 2021 (post-NASA ORR); NASA airworthiness cleared S2 to 10,000 ft through cloud; drops repeated 2022.
- **Airspace/approvals heritage:** FAA BVLOS for S2 (2018, NOAA ATDD); WP-3D integration (AOC, UxSOC); Navy VACAPES (SASCWATCH); NASA coordination (S3); 777 S0 integration.
- **Environmental qualification:** Navy STTR N6833525C0270 covers S0 de-icing, turbulence sensing, adaptive sampling; S3 cold/de-ice/salt-spray; S2 Greenland/Alaska ops.

### Storm Environment Knowledge
- **Load data:** WP-3D in Hurricane Hugo (1989): +5.8 / −3.7 g (informs demonstrator +6 / −3 g design).
- **Gust modeling:** 20 m/s gust adds ~2.6 g to 600–800 lb aircraft, ~1.2 g to WP-3D, ~2.0 g to MQ-9A.
- **Wind field simulation:** High-fidelity hurricane + rain fields with NCAR for guidance and autonomy testing.
- **Pressure signature example:** Hugo mesovortex ~12.5 hPa perturbation (measurable by S0, fills radar gap).

## Proposed Scope, Schedule, & Decision Gates

### Base Program (12 months, $2.39M as revised)
**Analytical and risk-reduction foundation:**

1. **Task 1:** Mission and observation requirements baseline (AOML/HRD, OMAO, EMC, 53rd WRS, CARCAH).
   - Persistence requirement (continuous boundary-layer coverage final 48 hrs before landfall).
   - Release patterns, spatial density, simultaneity.
   - Storm intensity carrier must cross; acceptable release-point error above intensity.
   - Data products, latency, success criteria.
   - Coastal base and corridor ranking.
   - NHOP small-UAS rule revision.

2. **Task 2:** Demonstrator conceptual design and configuration trade.
   - Configuration, mass properties, aerodynamics/performance.
   - Series-hybrid propulsion and electrical architecture.
   - Station arrangement, dash-speed and gust-load trade, basing.
   - Scaling plan to objective aircraft.
   - Benchmarking vs. existing platforms (Dominator, CCAs, UCAVs).
   - Structures/propulsion/scale-up partner assessment (time and cost).

3. **Task 3:** Dispenser architecture and release concept.
   - Wings-out pylon station, single release actuator, S0 hardpoint, sequencing, pre-release health check.
   - Per-station installed mass, external-carriage drag, separation in gusts.
   - Wing-pod interface for non-drop-chute hosts.

4. **Task 4:** Storm-penetration environmental and structural requirements.
   - Gust and maneuver loads, turbulence, water ingestion/hail, SLW/icing, lightning, salt.
   - Derived from WP-3D record and NOAA storm data.
   - Flow to structure, propulsion, ice protection, systems.
   - Identify cost drivers.

5. **Task 5:** Autonomy, communications, and data architecture with storm-field simulation.
   - SwiftCore storm patterns, wind-aware guidance, upstream-entry planning.
   - Gust-load and icing limiting, contingency/egress logic.
   - Four-layer hazard-avoidance architecture.
   - Multi-channel S0 relay (Task 1 sized).
   - Satellite backhaul, C2/mission-data architectural separation.
   - Hardware-in-the-loop implementation.

6. **Task 6:** Next-generation remote sensing and 3-D wind retrieval (with Weather Stream, Inc.).
   - Trade: reduced-aperture Doppler, SFMR-class radiometry, microwave sounding, compact S0 radar, sounding-derived winds.
   - Payload envelopes, phased sensor-development sequence.
   - Coordination with C-130J radar study.

7. **Task 7 (New):** Airspace and airworthiness pathway (with UxSOC).
   - Operating basis (COA, Policy 1107, custody during test).
   - ATC integration equipment list.
   - Section 919 and Ikhana-style approval approach.
   - Warning-area procedures for demonstrator.
   - Airworthiness package structure and review schedule.
   - Approval plan for NOAA review at Gate 2.

8. **Task 8 (New):** Critical Technology Element risk-reduction testing.
   - **CTE 1 (Propulsion in rain/failure):** Bench water-spray and ingestion test of heavy-fuel generator in sealed nacelle; electric propulsor wet-side; one-generator-out and battery-bridge test.
   - **CTE 2 (Structure/hardening/weight):** Coupon and wing-section static tests to +6 / −3 g design case; salt/humidity coupons; validated weight build-up.
   - **CTE 3 (Carriage/release):** Prototype pylon, actuator, S0 hardpoint; ground release tests; captive carry/release of inert S0 from existing BST aircraft.
   - **CTE 4 (Weather sensing/hazard avoidance):** Replay real TDR, NEXRAD, S0 data through HiL environment with COTS X-band model; measure warning time vs. response (slowdown, turn, egress).
   - **CTE 5 (Multi-S0 relay/comms integration):** Bench and ground test multi-channel 430 MHz relay with 4+ live S0 radios, flight-critical link, satellite backhaul.

9. **Task 9 (New):** S0 satellite link, D2C Phase 1.
   - Prototype board + two-unit flight demonstration (Section 3.5 detail).
   - Clear-air flights over T-Satellite area in Colorado.
   - Gate: measured link availability, latency, data from two airborne S0.

10. **Task 10:** Preliminary design review and program plan.
    - PDR covering configuration, dispenser, environment, autonomy, hazard avoidance, sensing growth, CTE results.
    - Program plan, risk register, fleet acquisition/operating cost estimate.
    - Build-in-house or partner recommendation for objective aircraft.

**Base deliverables (due ARO + specified months):**
- Requirements baseline; basing/corridor ranking; verification cross-reference (ARO + 3 mo).
- D2C Phase 1 flight demo report (ARO + 6 mo).
- Conceptual design, configuration trade, scaling plan (ARO + 8 mo).
- Airspace/airworthiness approval plan (ARO + 8 mo).
- Dispenser architecture, ICD, separation test approach (ARO + 8 mo).
- Storm-penetration environmental/structural requirement set (ARO + 8 mo).
- CTE 1–5 test reports (ARO + 11 mo).
- Autonomy, C2, data architecture, simulation results (ARO + 10 mo).
- Next-generation sensing trade and payload envelopes (ARO + 11 mo).
- PDR package, program plan, risk register, fleet cost estimate, build-or-partner recommendation (ARO + 12 mo).

### Option Tasking

**Option 1 (Task 11): Demonstrator detail design, build, clear-air flight test (22 months, $3.50M)**
- CDR, fabrication, integration, structural/environmental qualification, ground/taxi, envelope expansion.
- Icing-tunnel time for ice-protection design.
- Deliverables: aircraft, ground segment, test evidence, weather-test approval package.

**Option 1a (Task 12): Second demonstrator airframe (alongside Option 1, $1.00M)**
- Recurring-cost second aircraft enabling two-ship demo and sustained envelope expansion.

**Option 2 (Task 13): Dispenser development and separation qualification (12 months, $0.75M)**
- Qualify station hardware and sequencing software; instrumented separation across release envelope.
- Multi-S0 sequenced release/relay from demonstrator.

**Option 3 (Task 14): Instrumented tropical cyclone demonstration (12 months, $1.15M)**
- Progressive envelope expansion: convection → rainbands → Government-approved eyewall penetration.
- Stop criteria at each step.
- One instrumented mission releases multiple S0 into boundary layer, coordinated with NOAA crewed mission (synchronized TDR, SFMR, dropsonde, S0 reference).

**Option 4 (Task 15): S0 compact radar (12 months, $0.20M)**
- Compact near-field Doppler rain radar on S0; ground validation to clear-air flight test.

**Option 5 (Task 16): Advanced remote-sensing risk reduction (12 months, $2.80M)**
- Breadboard, lab, ground, retrieval-algorithm work on highest-value Task 6 concept; not fieldable yet.

**Option 6 (Task 17): D2C Phase 2 (9 months, $0.11M)**
- Board respin to flight-grade; offshore and WP-3D deployment beyond 12 nm under STA.

**Option 7 (Task 18): D2C Phase 3 (9 months, $0.09M)**
- Gen2 Starlink Mobile integration and storm release from WP-3D.

**Option 8 (Task 19): Multi-S0 telemetry upgrade for WP-3D and C-130J (9 months, $0.25M)**
- Ground-station and radio upgrade to fly >2 simultaneous S0 from crewed fleet.
- AOC installation support, flight checkout.

**Option 9 (Task 20): Wing-pod S0 carriage (12 months, $0.30M)**
- Package Task 3 station as pod for crewed and uncrewed hosts without drop chute.
- Separation analysis, ground test, captive-carry test.

### Decision Gates (5 gated decision points)

| Gate | Timing | Evidence | Question NOAA Decides |
|------|--------|----------|----------------------|
| 1. Requirements | Base month 3 | Persistence requirement; basing/corridor ranking; NHOP rule path; first CTE test plans | Is continuous boundary-layer coverage worth uncrewed fleet, and can it be based and coordinated? |
| 2. Configuration/Approval Basis | Base month 8 | Storm load/icing requirements; demonstrator config and scaling plan; airspace/airworthiness plan; early CTE results; D2C Phase 1 flight data | Is configuration right, under which approval basis will it fly? |
| 3. PDR | Base month 12 | Full CTE results; dispenser/hazard-avoidance architecture; fleet cost estimate | Build and clear-air test demonstrator? |
| 4. Weather Readiness | Option 1 end | Prototype, clear-air envelope, separation/multi-S0 relay tests | Approve progressive weather envelope expansion? |
| 5. Storm Demonstration | Option 3 end | Instrumented penetration with S0 release | Build operational aircraft in-house or with strategic partner? |

### Master Phasing Plan (2027–2031)
- **Base award:** Early 2027.
- **Baseline path:** First instrumented storm penetration in 2030 season (Option 3 following Options 1–2).
- **Accelerated path (2029 target):** Option 1 long-lead propulsion/structure released at Gate 2; second demonstrator funded at Option 1 start; targeted partner support on structures/propulsion. Aims for rainband steps and late-2029 penetration (2030 backup). Requires earlier funding, additional staff, firm supplier commits; retains all design/safety/readiness decisions. (Note: BST is 12–14 person company; people, not technology, pace work.)
- **Near-term S0 improvements:** Fly from 2027 on own schedule; Options 8, 9, D2C Phases 1–3 deliver value whether or not carrier proceeds.

### Cost Summary (ROM)
| Scope | Duration | ROM |
|-------|----------|-----|
| Base analytical (Tasks 1–6, 10) | 12 months | $1.50M |
| Base airspace/airworthiness (Task 7) | 12 months | $0.20M |
| Base CTE risk reduction (Task 8) | Months 3–11 | $0.60M |
| Base D2C Phase 1 (Task 9) | 6 months | $0.09M |
| **Base total** | 12 months | **$2.39M** |
| Option 1 demonstrator | 22 months | $3.50M |
| Option 1a second demonstrator | Alongside Opt 1 | $1.00M |
| Option 2 dispenser | 12 months | $0.75M |
| Option 3 storm demo | 12 months | $1.15M |
| Option 4 S0 compact radar | 12 months | $0.20M |
| Option 5 advanced sensing | 12 months | $2.80M |
| Option 6 D2C Phase 2 | 9 months | $0.11M |
| Option 7 D2C Phase 3 | 9 months | $0.09M |
| Option 8 multi-S0 telemetry | 9 months | $0.25M |
| Option 9 wing-pod carriage | 12 months | $0.30M |
| **All options total** | — | **$12.54M** |
| **Carrier path (Base + Options 1–3)** | — | **$7.8M** |
| **Near-term S0 improvements** | — | **$0.74M** |

**Notes:**
- Planning estimates pending detailed BOE.
- D2C airframes (6 total, two per phase) Government-furnished from NOAA's existing S0 order at $18,630 each (Ordering Period 2 price).
- Fleet acquisition cost for operational aircraft delivered separately at PDR (Task 10).
- Assumes NOAA provides WP-3D operating/load/storm data; reference observations; range/warning-area access; timely reviews at each gate.

## Airspace, Airworthiness & Operations

### Regulatory Framework
- **Operating basis:** NOAA public aircraft under FAA COA sponsored by UxSOC, per NAO 216-104A and NOAA UAS Operations Policy 1107.
- **Why not Part 108:** Proposed rule covers operations at or below 400 ft AGL and prohibits ADS-B Out; carrier operates 10,000 ft in NAS under ATC.

### Flight Profile & ATC Integration
- **10,000 ft cruise:** Same as crewed WP-3D/WC-130J; operates in Class E/A airspace.
- **Equipment:** Mode S transponder, ADS-B Out, ATC voice relay (line-of-sight + satellite), published lost-link procedures, onboard detect-and-avoid radar.
- **No chase aircraft:** Unescorted authorization pursued via Section 919 and Ikhana-style approval (federal non-small UAS flying without crewed escort).
- **Heritage:** NASA Ikhana flew unescorted near 10,000 ft on equivalent equipment.

### Demonstrator Flight Authorization Path
- **Coastal field with direct water access:** Departs from restricted/warning-area corridor; accepts escort or restricted-area procedures on departure.
- **Oceanic airspace testing:** U.S.-controlled oceanic airspace; over-water warning-area operations follow BST's SASCWATCH/Navy VACAPES model.
- **Section 934 (FAA Act of 2024):** FAA/ICAO coordination on high-seas UAS approval; ICAO Annex 6 Part IV standards apply from November 26, 2026.
- **Diplomatic/legal questions:** Whether NOAA can operate state-aircraft due regard beyond 12 nm needs legal opinion.

### NOAA Airworthiness Pathway (Policy 1107)
1. CONOPS → UxSOC UAS Division.
2. Evaluation by designated Platform Evaluator.
3. Airworthiness Designation with limits.
4. Flight authorization from UxSOC Director.
5. BST builds package from day one: load substantiation, hazard analysis, flight manual (lost-link, emergency procedures), configuration control, flight test plan.
6. NOAA reviewers at PDR, CDR, flight readiness, weather gates.
7. Policy 1107 permits NOAA to accept airworthiness work from NASA (precedent available).

### NHOP and Reconnaissance Coordination
- **Current rule:** One small UAS per reconnaissance area, ≤5,000 ft MSL.
- **Carrier need:** 10,000 ft with multiple S0 releases requires rule revisit with 53rd WRS and CARCAH (Task 1).

### Dropping UAS from UAS
- **Precedent:** 14 CFR 91.15 allows dropping objects with reasonable precautions; NOAA certifies airworthiness.
- **Examples:** NASA Langley S2/CICADA flights; DoD Altius-600 and Eaglet air-launches from Gray Eagle/MQ-9A on military ranges.

### Title & Custody During Test
- Task 7 to determine who holds title during Phases 1–2 (decides whether Policy 1107 or BST COA governs).

## Notable Details & Strategic Context

### Why BST Leads Airspace Work
- Airspace, not airframe, is the hardest part. BST owns COA, Section 919, NOAA airworthiness as funded task with UxSOC rather than leaving to NOAA alone.

### Operational Necessity: Persistence, Not Capacity
- Crewed aircraft can carry many S0 but only use while on station. Four-carrier rotation keeps S0 on-station 24/7, multiplying value of ~10% intensity-forecast improvement.
- Current inefficiency: 417 WP-3D hours vs. 18 S0 hours in 2025 season; gap is persistence, not magazine size.

### Why Purpose-Built Over Adapted Platforms
- **MQ-9 class:** Single-engine, weather-limited (icing/precipitation), structurally for benign ISR, ~10× oversized.
- **Light twins (e.g., Dominator II):** Useful for objective aircraft (20+ hrs) but light-aircraft structure not eyewall-gust-hardened; 2× objective gross weight and $10M/unit.
- **Military UAS/CCAs/UCAVs:** Rugged but jet-class, no ice protection typically, export-controlled, priced above program total.
- **High-altitude platforms (Global Hawk):** Valuable for other work but overflight loses boundary-layer release/relay.
- **Design principle:** Faster/larger penetrator raises gust loads proportionally to airspeed², spends less time where data is, costs more to lose → less likely to be sent into eyewall.

### BST's Competitive Position
- **Uncrewed hurricane operations heritage:** Only NOAA-deployed UAS into hurricane core; VORTEX2, CICADA air-launch, S0 operational data in forecast model.
- **Storm autonomy expertise:** Founders' 2010–2011 publications on penetration of super-cell wind fields; hardware-in-the-loop NCAR environment.
- **Risk-retirement early:** Five CTEs bench/rig/HiL tested in Base before PDR; hardware evidence before build decision.
- **Airspace pathway owned:** UxSOC partnership removes regulatory uncertainty.
- **Strategic investor:** KrateoSky backing (advanced manufacturing, production capital for objective aircraft scale-up).

### Data Rights & IP
- Deliverables may incorporate BST pre-existing: S2, S3, SwiftCore, SwiftPilot, SwiftTab, ground-station and simulation software (hurricane-field environment), autonomy functions, wind-estimation methods, manufacturing know-how.
- Data rights to be defined in resulting agreement.
- Partner sensor concepts, airframe partner designs, third-party hardware retain their own terms.

### Near-Term S0 Improvements (Stand-Alone Value)
Even if carrier not pursued:
- **Multi-S0 relay upgrade (Option 8, $0.25M):** WP-3D and C-130J fly >2 simultaneous S0.
- **S0 satellite link (Options 6–7, $0.20M):** D2C enables S0 to report for ~2 extra hours; sortie supports 3 sequential flights (~12 hrs/day) vs. 2 (~8 hrs).
- **Wing-pod carriage (Option 9, $0.30M):** Self-contained S0 compatible with non-drop-chute platforms.
- **Total:** ~$0.74M for near-term improvements; carrier path (Base + Options 1–3) $7.8M.

### NOAA Roles & Assumptions
- **Provide:** Mission ownership (AOML/HRD, OMAO, EMC); WP-3D operating/load/storm data; reference observations (TDR, SFMR, dropsonde, model datasets); range/warning-area access; spectrum, cybersecurity, airworthiness coordination; timely gate reviews.
- **Partner:** T-Mobile (D2C service, test SIMs, airtime under CRADA); pursue STA for D2C Phase 2.
- **Coordinate:** C-130J radar study team (Task 6 sensing work).

### Related Prior Contracts
- NAVAIR N251-016 (S0 SBIR).
- STTR N6833525C0270 (Navy; with Embry-Riddle, University of Miami/HRD; S0 de-icing, turbulence, adaptive sampling).
- AF192-005 (Air Force).
- NOAA CRADA with T-Mobile (D2C feasibility, 2026).

---

## Internal Review Notes (Document Control)

Document flagged several items for resolution before final release:
- Detailed BOE needed for new Base scope (CTEs, airspace task, second airframe, multi-S0 telemetry, wing-pod).
- Total cost moved from $9.9M to $12.54M; consider leading with $7.8M carrier path and presenting sensing options separately.
- Option 1 extended 20→22 months (10-month build vs. ~7 months); confirm with Josh/Maciej; validate $3.50M hold.
- Standardize S0 mass across all documents (3 lb vs. 1.2 kg/2.6 lb).
- Dash speed set as Task 2 trade; confirm storm intensity requirement and acceptable release-point error with NOAA.
- Confirm CICADA/S2 drop heritage clearance with NASA Langley (Mark Motter).
- Confirm S3 can carry/release inert S0 for CTE 3 testing.
- Verify Colorado T-Satellite test site and T-Mobile airborne Band 25 approval for D2C Phase 1.
- Confirm NOAA standing BAA successor (prior BAA closed Sept 30, 2026).
- Title custody during test phases drives Policy 1107 vs. BST COA governance; resolve in Task 7.
- Validate Brian's Master Phasing Plan chart against original (chart rebuild from review notes).
- No airframe partner named; keep any discussions in "objective aircraft partner" role, not demonstrator supply.
- Hurricane Lala figures pending NOAA coordination call approval.

---

## Summary

This proposal offers NOAA a gated path to persistent tropical cyclone boundary-layer observation via a purpose-built, 12-hour demonstrator uncrewed carrier (600–800 lb) rotating with three sister aircraft. The demonstrator proves storm-critical technologies (hybrid propulsion in rain, eyewall-gust-hardened structure, S0 release/relay, wind-aware penetration autonomy) at low-risk scale before commitment to a 1,200–2,000 lb operational aircraft. Five critical technology elements are hardware-tested in the Base phase; airspace and airworthiness pathways are BST-owned funded work, not assumed. Near-term S0 improvements (multi-channel relay, satellite data link, wing-pod carriage) deliver value immediately whether or not the carrier proceeds. The program is structured for early decision gates and stops, ensuring NOAA retains control and usable results at each milestone.