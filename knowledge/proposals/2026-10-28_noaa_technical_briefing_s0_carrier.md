# 2026-10-28 NOAA Technical Briefing: S0 Carrier

## Document Metadata
- **Type:** Technical briefing presentation
- **Client/Agency:** NOAA (Office of Marine and Aviation Operations, Unmanned Systems Operations Center, Atlantic Oceanographic & Meteorological Laboratory/Hurricane Research Division)
- **Program/Solicitation:** S0 Carrier development program (proposed)
- **Date:** October 28, 2026
- **BST Products/Systems Referenced:** S0 (Companion), S2, S3, SwiftCore
- **Key Personnel:** Jack Elston (Founder and CEO), Nick (propulsion architect), Maciej (carriage design), Dan (cost estimation), Ed Dumas and Bruce Baker (NOAA ATDD collaborators referenced)

## Executive Summary

Black Swift Technologies proposes developing an autonomous uncrewed S0 carrier aircraft purpose-built to extend NOAA's boundary-layer hurricane observations by enabling continuous S0 deployment independent of crewed aircraft sortie timing. The carrier would augment the WP-3D and C-130J fleet by maintaining persistent sampling throughout tropical cyclone cores, deploying multiple S0 to rainbands, eyewall, and eye locations via a four-aircraft rotation model providing ~24-hour coverage. BST seeks NOAA agreement on mission requirements, demonstrator sizing, and regulatory approval pathways during this technical working session.

## Technical Approach

### Core Concept
- **Mission:** Autonomous launch from coastal runways, transit to storm at ~10,000 ft (700 hPa), execute P-3-style butterfly penetration through eyewall and eye, release S0 at required locations, relay data via satellite to NOAA in real time, hand off to next carrier in rotation (~4-hour ground turn), and repeat
- **Design Philosophy:** Purpose-built from hurricane boundary-layer measurement requirements, not adapted from existing airframes; all design decisions derive from storm environment and NOAA observation needs
- **Operating Model:** Four-aircraft rotation (planned) providing ~400 nm radius continuous coverage with 120–130 kt cruise speed and 12-hour demonstrator endurance; approximately 300 nm radius when one aircraft unavailable
- **Deployment Requirement:** Full-storm access including rainbands, eyewall, eye, and inner-core S0 placements (baseline mission requirement, not optional follow-on)

### Flight Profile
1. Launch from conventional coastal runway under NOAA-coordinated airspace authorization
2. Transit at ~10,000 ft (standard crewed reconnaissance level)
3. Fly P-3-style butterfly pattern: three center crossings 60° apart, joined by repositioning legs
4. Release S0 wherever observing plan requires (not limited by sortie timing)
5. Relay S0 observations over 430 MHz to NOAA via satellite link in real time
6. Hand off to next carrier; land, reload magazines, turn aircraft in ~4 hours
7. Return to storm for continued coverage

**Critical Mission Requirement Update (28 October 2026):** Full-storm "butterfly" mission (penetration legs, adverse winds, release sequences, reserves) not yet validated against initial rotation model; configuration must support required speeds for eyewall and eye access despite flight-level winds >150 kt.

## Products & Capabilities Described

### S0 (Companion System)
- **What it is:** Uncrewed meteorological probe carrying in-situ sensors for tropical cyclone core observations
- **Current operational status:** Operational with NOAA WP-3D since 2023; 37 launches in FY26 with routine dual releases, flights >2 hours, boundary-layer legs 10–15 m above ocean
- **Performance record:** Guinness-recognized wind measurement ~240 mph (240.94 mph, Hurricane Milton, October 8, 2024 at 494.9 m altitude)
- **Data integration:** Selected for integration into NOAA's HAFS (Hurricane Analysis and Forecast System) for 2026 season; supports dual-altitude simultaneous sampling
- **Proposed carrier integration:** Carried wings-deployed on pylons (not in launch tube), direct release via single actuator per station; preliminary carriage goal: <half the tube-based installation mass (~8–10 lb per station baseline)
- **Magazine design:** 6-station initial trade-study baseline; mass estimates 1.2 kg (~2.65 lb) per S0; with pylons/actuators/retention ~25 lb total S0 payload
- **Relay capability:** Multi-channel 430 MHz relay sized to number of simultaneous S0airborne (WP-3D limited to 2 channels; carrier would enable >2 simultaneous)

### S0 Carrier (Proposed Demonstrator)
- **What it is:** Purpose-built autonomous uncrewed aircraft for S0 deployment throughout tropical cyclone cores
- **Gross weight class:** 600–800 lb initial study case; final sizing TBD after full-storm speed, structure, and power requirements confirmed
- **Endurance:** Initial rotation model: ~12 hours; objective study case: 22–26 hours for ~1,000 nm reach or 14–16 hours with forward basing
- **Cruise speed:** 120–130 kt (reduction from earlier 150 kt estimate); gust loads increase with airspeed, constraining penetration speed options
- **Propulsion (series-hybrid proposed):**
  - Twin heavy-fuel generators in sealed nacelles with inertial separators and heated intakes (rain/spray protection)
  - Electric motors drive propellers (S0 rain/sea-spray heritage demonstrates brushless motor viability)
  - Battery-bridge energy reserve to manage generator wet-outs, induction icing, or fuel-system upsets
  - Either generator sized to hold altitude; rapid electrical thrust response for downdraft recovery
  - Full fault-tolerance (bus segmentation, contactors, wiring protection) remains design work

- **Payload/Magazine:** Wings-deployed S0 carriage with pylons, retention, single actuator per station; multi-channel relay (430 MHz, count TBD); situational-awareness radar; in-situ meteorology; total mission payload 20–30 lb estimated
- **Structure:** Designed for eyewall gust loads; +6/−3 g total load-factor target; gust-load-limiting autopilot; automatic slowdown to turbulence-penetration speed
  - Preliminary gust comparison: 20 m/s gust at 10,000 ft induces ~2.6 g on carrier (vs. ~1.2 g on WP-3D, ~2.0 g on MQ-9A)
  - Full environmental envelope (winds, gusts, rain, hail, icing, lightning) to derive from WP-3D record before airframe frozen
- **Landing gear:** Included (conventional-runway concept with autonomous operations)
- **Ice protection (capability gap to close):**
  - Tropical-cyclone rainbands contain supercooled liquid water above freezing level (~15,000–16,000 ft typical)
  - Operating level ~10,000 ft generally below freezing level, but freezing level varies; climbs, descents, updrafts expose to icing
  - Induction icing can occur above freezing in saturated air
  - Candidate approaches: UBIQ D•ICE (electrothermal wing/propeller), heated propellers (Meteomatics tested at −5 °C; limitations at −10 °C noted)
  - BST relevant experience: S0 de-icing heaters (Navy STTR N6833525C0270), S3 cold-weather/de-ice work, S2 Arctic flight heritage (Alaska, Greenland)
  - Qualification scope/cost: TBD; working estimate $55,000–$60,000 per icing-tunnel test day (requires current quotation)

### S2
- **Reference use:** Previously flown with NASA CICADA micro air vehicle payload; dropped CICADA successfully at Beaver Dam Airpark, VA (December 17, 2021) following NASA operational readiness review; continued successful drops 2022; NASA airworthiness cleared for cloud and higher-altitude operations
- **Cold-weather heritage:** Referenced for Arctic operations precedent

### S3
- **Reference use:** Cold-weather and de-ice development work referenced as BST institutional capability

### SwiftCore
- **Capability:** Estimates three-dimensional wind onboard; supports S0 maximum-wind and storm-center sampling; provides starting point for carrier guidance development

## Use Cases & Applications

### Tropical Cyclone Reconnaissance
- **Primary mission:** Boundary-layer observation augmentation during tropical cyclone events
- **Sampling improvements:** 
  - Continuous S0 presence (24-hour illustrative rotation) vs. current limited S0 availability tied to WP-3D sortie windows
  - Coverage during crewed-aircraft downtime or when crewed assets tasked to radar/dropsonde/fix missions
  - Release locations determined by observing plan (not sortie geometry)
  - Dual/multiple simultaneous S0 (>2 concurrent launches via multi-channel relay, vs. current WP-3D 2-channel limit)
- **Sampling locations:** Rainbands, eyewall, eye, and inner core
- **Observing requirements:** Real-time boundary-layer winds, turbulence, pressure, dual-altitude capability
- **Integration:** Data flows to NOAA/AOC, NHC, AOML/HRD, EMC; operational model integration with HAFS

### Operationalization Context
- **Current operational baseline:** S0 launched from WP-3D during 7–10 hour crewed sorties; limited to 2 simultaneous S0 by radio channels; >18 S0 flight hours in 2025, 417 hours total Hurricane Hunter fleet
- **Proposed operational model:** Carrier fleet (4 aircraft in rotation) maintains persistent S0 presence; crewed aircraft freed from S0 launch duty to focus on radar, dropsonde, and storm-fix missions; NHOP 2026 supports requests for up to eight 3-hourly fixes within 300 nm of coast (separate from carrier base radius)

## Key Results (Technical Capabilities & Heritage)

### S0 Operational Maturity
- **37 launches in FY26** with routine dual releases, flights >2 hours, 10–15 m altitude legs above ocean
- **Wind record:** 240.94 mph, Hurricane Milton, October 8, 2024 (Guinness World Records)
- **Integration milestones:** WP-3D safe-separation testing completed, 430 MHz link tested to 400 km, AVAPS interference mitigation in place, NOAA data routing established
- **August 18, 2026 Hurricane Lala results:** 132-minute flight, sustained flight at 10 m, simultaneous dual-altitude sampling (public NOAA data available)

### Design Evolution
- Addressed prior review feedback (Alan Goldstein, OMAO): reframed case around persistence and observation continuity rather than P-3 capacity comparison
- Emphasizes full-storm access (eye, eyewall, rainbands) from initial baseline, not optional follow-on

### Propulsion Risk Reduction
- Series-hybrid architecture selected (not direct-drive combustion) to enable rapid electrical thrust response in downdrafts and survivability via dual generators + battery bridge
- Protected generator architecture (sealed nacelles, inertial separators, heated intakes) designed for rain/spray tolerance demonstrated by S0 electric-drive heritage

### Guidance/Autonomy Approach
- Sensor-driven guidance lineage: founders' VORTEX2 mobile radar + UAS integration, SwiftCore wind estimation, distributed S0 observations
- Proposed multi-layered hazard detection: planning data (NOAA TDR/NEXRAD/satellite/recon), onboard X-band radar (convective hazards ahead), released S0 pickets (local wind/turbulence/pressure around planned deployment points), reactive wind/load estimates for route/speed adjustment and egress
- Task 5 develops and tests guidance logic in simulation; progressive flight-envelope validation follows
- Mesovortex detection capability discussed (based on S0 ability to measure sharp pressure/wind shifts, e.g., ~12.5 hPa local perturbation in Hurricane Hugo); avoidance performance TBD

### Communications & Data Relay
- Multi-channel 430 MHz relay sized to required simultaneous S0 count (removes 2-channel WP-3D limit)
- Flight-critical control kept separate from mission payload and science data (losing relay does not lose carrier control)
- Satellite link returns carrier state and priority observations to NOAA
- **Starlink direct-to-cell (D2C) feasibility pilot** proposed as gated low-cost phase (~$47K Phase 0 concept, ~$680K over three phases ROM) to enable independent S0 reporting; benefits NOAA operations even if carrier delayed; Phase 0 to establish module availability, coverage, antenna/power needs, latency, provider terms before operational commitment

### UAS-from-UAS Precedent
- BST S2/NASA CICADA: First drop December 17, 2021 (Beaver Dam Airpark, VA) after NASA operational readiness review; autonomous launch-to-landing, tablet-commanded release; continued successful drops 2022
- Larger examples: ALTIUS-600 from MQ-1C (2020), MQ-9A (December 2023); Eaglet from Gray Eagle ER (2022)
- **Regulatory note:** 14 CFR 91.15 permits dropping objects when reasonable precautions avoid injury/damage, but does not itself approve BVLOS operations, multiple UAS, release envelope, or specific airspace access; civil vs. public-aircraft status, NHOP coordination, and release approvals require specific Phase authorization; military-range precedents do not establish standing civil approval

## Notable Details

### Carrier Sizing & Configuration Decisions (Open Trades)
- **Magazine:** 6-station baseline (TBD); S0 mass 1.2 kg or 3 lb per unit (to be confirmed with Maciej)
- **Propulsion architecture:** Series-hybrid confirmed direction; generator-out performance requirement, battery-bridge duration, and protected-intake design TBD
- **Carriage concept:** Wings-deployed on pylon with single release actuator; target installed mass materially below tube-based (~8–10 lb) reference; specific hardpoint location and outer-mold-line drag TBD in Task 3
- **Separation qualification:** Progressive approach (analysis → ground → clear-air drops → weather) must ultimately support eye, eyewall, rainband deployment including local airflow and carrier maneuvers at release
- **Speed requirements:** Cruise, dash, and turbulence-penetration speeds remain unresolved; full-storm access (reaching all deployment locations despite flight-level winds >150 kt) drives power and structural sizing
- **Operating radius:** 4-aircraft rotation model ~400 nm from base (12-hour demonstrator at 120–130 kt, 4-hour turnaround, reserves); assumes adequate magazines, reliable handoffs, sustained S0 supply; continuous 24-hour coverage is planning model, not yet demonstrated
- **Gross weight:** 600–800 lb initial study case; final sizing TBD after propulsion, structure, and power trades confirmed

### Regulatory & Approval Pathway (Complex, Phased)

**NOAA Airworthiness Authority:**
- Policy 1107 applicability depends on NOAA operational/safety responsibility and ownership (not title alone)
- Proposed path: CONOPS → NOAA UASD → designated Platform Evaluator → airworthiness evaluation/designation with limits → flight authorization
- NOAA may consider NASA airworthiness work as supporting evidence; S2 clearance does not automatically transfer to new carrier
- BST experience: NOAA ATDD S2 support for FAA BVLOS submission (2018, with Ed Dumas/Bruce Baker), S0 WP-3D integration approval

**Build Approval Package from Day One:**
- Loads, hazard analysis, flight manual, lost-link/emergency procedures, configuration control, flight-test plan
- Proposed review gates: PDR, CDR, before first flight, before each weather/storm-access envelope expansion
- Propose NOAA reviewers join PDR and envelope gates so required evidence is clear before testing

**Qualification Sequence (Staged):**
1. Clear-air envelope expansion
2. Convection and weather expansion
3. Full-storm demonstration (eyewall crossings, eye access, required S0 releases)
- Each gate has stop criteria; final capability is full-storm access (not optional follow-on)

**FAA/Airspace Approvals:**
- NHOP 2026 sUAS provisions: 5,000 ft MSL ceiling, 2,000 ft separation from crewed aircraft, CARCAH coordination
- Current text contains no one-sUAS-per-reconnaissance-area cap; unclear how provisions apply to simultaneous carrier + multiple S0 operations
- Spectrum, interference, aircraft approvals require work beyond current NHOP
- Civil vs. public-aircraft status, release authorization, and contingency procedures (e.g., lost-link behavior) require specific airspace/approval coordination for each test phase
- BST's prior VACAPES experience is relevant planning background, not automatic authorization for new operations

### Transition & Operations Model (Four-Phase)

| Phase | Lead | Scope | Notes |
|-------|------|-------|-------|
| 1 | BST | Build, ground test, clear-air, S0 separation, relay checkout | BST integration & validation |
| 2 | BST + NOAA | NOAA review, coastal base delivery, operator/maintenance training | Joint qualification |
| 3 | NOAA | NOAA operators fly; BST field engineering; data to AOML/HRD, EMC | Operational testing |
| 4 | NOAA + BST | Full-storm S0 deployment with coordinated crewed mission; handover | Storm demonstration |

**Proposed End State:** NOAA owns aircraft and ground segment; BST supports sustainment and upgrades

**Ownership Milestones (TBD):**
- Title transfer, custody transfer, and operational-responsibility milestones are separate decisions; contractually bind rather than assume coincidence
- Operating base (Lakeland or forward site TBD) and responsible NOAA office (AOML/HRD, OMAO, EMC) to be confirmed
- Manuals, spares, training, ground equipment, sustainment acceptance criteria to be defined

### Program Pricing & Options (Non-Binding ROMs)

| Element | Duration | ROM | Notes |
|---------|----------|-----|-------|
| **Base** | 12 mo | $1.50M | Requirements, design trades, environment, autonomy, sensing, PDR |
| **Option 1** | 20 mo | $3.50M | Carrier prototype, qualification, clear-air test |
| **Option 1a** | TBD | BOE pending | Second complete carrier, recurring cost only |
| **Option 2** | 12 mo | $0.75M | Dispenser & separation qualification |
| **Option 3** | 12 mo | $1.15M | Instrumented full-storm S0 deployment demonstration |
| **Option 4** | 12 mo | $0.20M | S0 compact radar |
| **Option 5** | 12 mo | $2.80M | Advanced sensing risk reduction |

**Totals:** All 6 priced elements = $9.90M; Base + Options 1–3 = $6.90M
**Exclusions:** Second-carrier BOE, multi-S0 radio, wing pods, approval execution, D2C Phase 0 (~$47K separate)
**Caveats:** Non-binding ROMs; exclude new second carrier; assume government-arranged range/airspace access, approval without new certification basis, commercial partner participation

### Risk Management & Qualification Evidence

| Risk | Mitigation Approach | Evidence Gate |
|------|-------------------|---------------|
| Rain in engine | Sealed generator, wet-side electric drive | Task 4, bench spray test, Option 1 |
| Gusts / track control | Wind margins, storm-rated structure, load limiting | Tasks 2, 4–5; Options 1–3 |
| Mesovortices | Local sensing, path adjustment, egress | Task 5, Option 3 |
| Icing | Detection & protection, icing tunnel | Task 4, Option 1 |
| Multiple S0 relay | Multi-channel relay, D2C feasibility pilot | Task 5, relay qualification |
| UAS-from-UAS approval | CICADA precedent, proposed airspace task | Task 1, Task 7, mission approval |
| NOAA airworthiness | Package from day one, NOAA review gates | Task 7, Options 1–3 |

**Critical Caveat:** Assigning a risk to a task does not establish that it has been retired; measurable completion evidence and stop criteria must be agreed with NOAA before each gate

### Key Open Requirements for NOAA Decision

BST proposes immediate requirements session with AOML/HRD, OMAO, EMC to close Task 1 baseline:

1. **Magazine & simultaneity:** How many S0 airborne at once; station spacing (sizes magazine and relay channel count)
2. **Operating range:** Size for coastal-storm missions or WC-130J-equivalent reach; which bases (coastal radius ≠ mission radius from operating base)
3. **Speed envelope:** Required cruise, dash, penetration speeds for deployment throughout storm; critical for propulsion/structure sizing
4. **Operational procedures & approvals:** Carrier + multiple S0 coordination procedures under NHOP 2026; release approvals; lost-link contingencies; FAA/airspace path
5. **Airworthiness authority:** Which NOAA office holds authority; reviewer participation at PDR
6. **Operating model:** Preferred base, ownership, operational-control, custody arrangements

### Strategic Partnerships & Investor Disclosure
- **KrateoSky:** Strategic investor (identified in presenter decision notes; confirmation required before public mention)

### Internal References & Sources
- Companion white papers (cited but not included): WP-BST-006 and related design documents
- Storm data: Hurricane Milton (October 2024), Hurricane Hugo (historical), Hurricane Lala (August 2026)
- External references: NOAA 2025 Hurricane Hunter summary, NHOP 2026, NCAR Milton verification, Meteomatics SOPHIA report, UBIQ D•ICE, Guinness World Records, GA-ASI MQ-9B FIKC tests (April 2026)

### Presenter Notes & Internal Decisions to Confirm
Document contains extensive presenter guidance, including:
- Confirm NASA Langley clearance for S2/CICADA media before external use
- Confirm HAFS operational assimilation status
- Confirm Hurricane Lala unpublished data restrictions before adding wind results
- Jack + Maciej to choose demonstrator mission and size framing
- Dan to complete second-carrier BOE after scope finalized
- Define measurable stop criteria for each qualification gate
- Secure requirements-session date with named NOAA decision owners

---

## Summary Assessment

This is a detailed technical briefing (presentation format) proposing a purpose-built autonomous carrier aircraft for enhanced tropical cyclone boundary-layer observations. The concept is grounded in BST's operational S0 heritage and addresses genuine capability gaps (continuous S0 presence, multiple simultaneous deployment, eye/eyewall access). However, the design remains largely conceptual:

**Maturity Level:**
- **Mature:** S0 operational status, propulsion architecture direction, approval pathway framework, risk taxonomy
- **Early concept:** Carrier sizing, full-storm speed/power/structure reconciliation, ice-protection integration, multi-S0 relay relay and guidance autonomy
- **Unvalidated:** 4-aircraft 24-hour rotation model, gust-load predictions at carrier scale, mesovortex detection/avoidance performance, full regulatory approval path

**Critical Path Items:**
1. NOAA requirements closure (speed, magazine, deployment locations, approval authority)
2. Speed/structure/power trade resolution for full-storm access (eyewall/eye in winds >150 kt)
3. Carrier prototype design and clear-air qualification
4. Phased storm-access envelope expansion with measurable gates

The proposal reflects rigorous engineering discipline (environmental requirements-driven design, staged qualification, risk mapping) and clear acknowledgment of open technical and regulatory questions. Success depends heavily on NOAA commitment to the requirements closure process and acceptance of an extended development/qualification timeline.