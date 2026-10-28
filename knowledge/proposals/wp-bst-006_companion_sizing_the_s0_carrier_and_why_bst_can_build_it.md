# WP-BST-006 Companion: Sizing the S0 Carrier and Why BST Can Build It

## Document Metadata
- **Type:** White paper / technical companion document
- **Client/Agency:** NOAA, USAF 53rd Weather Reconnaissance Squadron (WRS)
- **Program/Solicitation:** WP-BST-006 (referenced throughout; appears to be an ongoing proposal or funded project)
- **Date:** October 20–27, 2026
- **BST Products/Systems Referenced:** S0, S3, S2, SwiftCore, Multi-channel 430 MHz relay
- **Key Personnel:** Jack Elston (author/editor), founders cited for VORTEX2 experience, J. Wadler (Embry-Riddle), A. Gasiewski (Weather Stream/CU Boulder)

---

## Executive Summary

This white paper justifies the feasibility and size of an uncrewed S0-carrier aircraft for hurricane reconnaissance. Four carriers in rotation can maintain continuous coverage of the 300 nm zone demanded by the National Hurricane Operations Plan (NHOP) from a coastal base; reaching the ~1,000 nm radius of a typical WC-130J sortie requires a 22–26 hour aircraft or a 14–16 hour platform forward-deployed from existing recon bases. The required payload (~140 lb) and endurance enable a 1,200–2,000 lb aircraft—one-tenth the size of an MQ-9A—and BST's storm environment expertise, S0 operational heritage, and approved hazard-avoidance architecture uniquely position it to succeed where larger penetrator concepts have failed.

---

## Technical Approach

### Fleet Rotation Model
- **Four-aircraft concept:** Each aircraft maintains on-station time sufficient to allow the other three to transit, turn, and refuel (4-hour ground turn includes refuel, magazine reload, inspection).
- **Coverage radius scaling:**
  - 12-hour demonstrator: ~400 nm (all flying), ~300 nm (one down) from coastal base
  - 22–26 hour objective: ~1,000 nm all flying; 14–16 hours sufficient if forward-deployed from existing bases (St. Croix, Barbers Point, Curaçao)
- **Cruise/penetration altitude:** 10,000 ft (≈700 hPa), same as WP-3D and WC-130J
  - Deliberate choice: sits below tropical freezing level (typically >15,000 ft in hurricanes)
  - Dominant hazards are turbulence and rain, not airframe ice

### S0 Magazine Logistics
- On-station times of 3–9 hours require only 4–9 S0 per sortie to maintain continuous airborne presence with 1.75 hour useful life each + one spare
- Demonstrator: 6 stations; objective: 10–12 stations (margin for multi-aircraft release patterns)
- **Continuous-coverage consumption rate:** ~18 S0 per storm-day; ~36 for final 48 hours of landfall; ~90 for average 5-day storm
- Practical ops concept: continuous coverage inside 300 nm of landfall; NHOP-style fix cadence elsewhere

### Environmental Hazards and Mitigation

#### Gust Loads
- Hugo encounter (1989): WP-3D experienced +5.8 g / -3.7 g at 1,500 ft; Milton TDR mission (2024) met 2–3 mesovortex couplets with 5–13 m/s drafts
- **Gust load formula result:** 20 m/s gust at 10,000 ft adds ~2.6 g to demonstrator (vs. ~1.2 g for WP-3D, ~2.0 g for MQ-9A)
- **Mitigation:** Design small airframe for +6/−3 g limit loads at modest weight penalty; autopilot reduces to turbulence-penetration speed on detection; avoidance patterns minimize worst encounters

#### Rain Ingestion
- Eyewall echoes near 50 dBZ ≈ 74 mm/h rain ≈ 3 g/m³ liquid water
- At 10,000 ft: ~0.35% of intake air mass; threat is not flameout but water concentration in intakes, wetting ignition/generators/connectors, pooling in structure
- **No published rain/ingress rating exists for small UAS engines** (gap closed in Task 4)
- **Mitigation:** Series-hybrid architecture with sealed generator nacelles behind inertial separators and heated intakes; electric propulsors (same brushless motor/power electronics S0 flies through eyewall) in wet environment; battery bridge for recovery if generator wets out

#### Icing
- Below freezing level: confined to climb, descent, occasional updrafts; induction icing possible above-freezing temps in saturated air
- **Mitigation:** Fuel injection, heated intakes; S0 de-ice heater design under Navy STTR; S3 cold-weather heritage

#### Storm Winds vs. Airspeed
- Major-hurricane winds at 700 hPa exceed 150 kt
- **Mitigation:** Carrier patterns keep aircraft outside radius of maximum wind; S0 released upwind so they drift into core (current operational practice)

### Propulsion Architecture
- **Demonstrator:** Twin heavy-fuel piston; hybrid assist under trade
- **Objective aircraft:** Twin heavy-fuel generator sets (series-hybrid), electric propulsors, battery bridge
  - Generator sets in sealed nacelles with inertial separators and heated intakes
  - Electric propulsors operate in wet environment (flight-proven motor/electronics class from S0)
  - Either generator able to hold altitude alone; battery sized for bridging only, not full egress

---

## Products & Capabilities Described

### S0 (Atmospheric Probe Aircraft)
- **Operational status:** In use from WP-3D since 2023; holds uncrewed wind-speed record (240 mph in Hurricane Milton, NCAR-verified)
- **Data assimilation:** Being assimilated into NOAA operational hurricane model for first time in 2026
- **FY26 activity:** 37 S0 launches; dual-release now routine; flights sustained >2 hours; boundary-layer operations 10–15 m above ocean on radar altimeter
- **Environmental proven:** Flies through eyewall rain and sea spray; carries S0-class brushless motors and power electronics proven in harsh conditions
- **Autonomous capabilities:** SwiftCore estimates 3-D wind onboard; autonomous flight to maximum wind and storm center from own measurements; holds 10–15 m altitude on radar altimeter
- **Proposed role as carrier:** Forward pickets ahead of and below carrier; real-time 3-D wind, turbulence, pressure relay through carrier link; closes radar resolution gap for mesovortex detection (Hugo mesovortex: 12.5 hPa pressure perturbation and sharp wind shifts, exactly what S0 measures)

### S3 (Implied: Larger/Extended Platform)
- **Heritage:** Cold-weather, de-ice, salt-spray qualification work
- **Applications:** Northern Alaska, Greenland flight heritage; CJFC Arctic sprint; NCAS Greenland interest
- **Relevance:** Direct icing and corrosion experience transferable to carrier design

### S2
- **Heritage:** Flight history in northern Alaska and Greenland

### SwiftCore
- **Capability:** Onboard 3-D wind estimation; autonomous max-wind and center-finding patterns; storm-guided autonomy beyond autopilots
- **Founders:** Flew UAS component of VORTEX2 (2009–2010), intercepting supercells with mobile Doppler radar in the loop

### Situational-Awareness Weather Radar
- **Baseline (demonstrator):** Garmin GWX 75 / GWX 8000
  - Certified X-band Doppler with turbulence detection
  - 10–13 lb, 10–14 in antenna, 40 W transmit
  - Flags reflectivity cores 45–50 dBZ and Doppler turbulence tens of miles ahead
  - 7–8° beam resolves features ~1.3 km at 10 km (adequate for convective cores, marginal for 1 km mesovortex)
  - Requires ~12 in nose radome (sets minimum fuselage diameter for demonstrator)
- **Objective option (Task 6):** Fused weather/detect-and-avoid/radiometer suite built with Weather Stream
  - FMCW cloud/rain radar with custom Doppler processing and radiometry
  - Custom module in ~6-month development for S0 version

### Multi-Channel 430 MHz Relay
- Previously tested to 400 km
- Supports simultaneous relay of multiple S0 (vs. WP-3D limited to two channels)
- Starlink direct-to-cell pilot as secondary path (Task 5)

---

## Demonstrator vs. Objective Aircraft

| Attribute | Demonstrator (WP-006 Option 1) | Objective Aircraft |
|-----------|--------------------------------|-------------------|
| **Mission** | Near-landfall coverage from coastal base; envelope expansion | Full recon-radius coverage, multi-week rotation |
| **Design endurance** | 12 h | 22–26 h (14–16 h with forward basing) |
| **Continuous-coverage radius (4 aircraft)** | ~400 nm all flying; ~300 nm with one down | ~1,000 nm all flying |
| **Cruise/penetration airspeed** | 120–130 kt | 150 kt cruise, penetration set by gust trade |
| **S0 stations** | 6 | 10–12 |
| **Useful payload** | ~80 lb (stations, relay, in-situ met, 10 lb situational-awareness radar) | ~140 lb + growth-sensing allowance |
| **Gross weight** | 600–800 lb | 1,200–2,000 lb |
| **Wingspan (wing loading 25–35 psf)** | ~18–22 ft | ~30–36 ft |
| **Propulsion** | Twin heavy-fuel piston, hybrid assist under trade | Twin heavy-fuel generator sets, series-hybrid electric propulsors, battery bridge |
| **Build approach** | BST-led, clean-sheet or adapted airframe | BST avionics/autonomy/dispenser/sensing; airframe partner; KrateoSky production |

**Design envelope bounds (WP-006 Table 1):** 550–1,000 lb baseline; 1,100–1,900 lb growth

**Sizing assumptions:**
- Lift-to-drag: 12–18 clean; 30% lower in storm
- Fuel consumption: 0.45–0.55 lb/hp-h
- Empty-weight fraction: 0.50–0.60 (cost driver; every point of storm hardening >0.55 pushes 24-hour aircraft toward upper weight range)

**For scale:** MQ-9A grosses ~10,500 lb; carrier needs ~1/10 that size because payload is a 3 lb aircraft magazine.

---

## Use Cases & Applications

### Primary Mission: Hurricane Reconnaissance
- **Near-landfall threat assessment** (demonstrator from coastal base)
- **NHOP-compliant 3-hourly fixes** inside 300 nm of coast (demonstrator capability)
- **Full reconnaissance radius coverage** (~1,000 nm, objective aircraft)
- **Multi-week storm tracking** (5-day average Atlantic storms; record storms >20 days)
- **Data assimilation into NOAA operational hurricane models**

### Operational Context
- **Crewed fleet rotation model (existing standard):**
  - NOAA WP-3D: 7–10 h sorties at ~10,000 ft; two P-3s every 12 h (up to two TDR missions/24 h)
  - USAF WC-130J: ~11 h sorties, 3,500 statute miles; up to 5 sorties/day from 3 bases; 3-hourly fixes <300 nm coast, 6-hourly <500 nm
- **2024–2025 activity:** 1,609 reconnaissance hours (both fleets, 2024); NOAA 63 flights, 417 hours into six hurricanes (2025)
- **High-impact storms:** Hurricane Lee (2023) lasted 13.5 days, drew 30 recon flights and 69 center fixes

### Distributed S0 Sampling Patterns
- Carrier enables boundary-layer observation network at 10–15 m altitude
- Real-time wind, turbulence, pressure data for rapid mesovortex detection and avoidance
- Multi-S0 simultaneous releases (requires policy revision from current single-sUAS-per-area rule)

### Secondary Heritage Applications (S3, S2)
- Arctic operations (cold-weather, de-ice capability)
- Volcano monitoring (implied by cold/corrosion work)
- Salt-spray/maritime environments

---

## Automated Hazard Avoidance Architecture

BST's four-layer approach to mesovortex and extreme-turbulence detection (no autonomous detect-and-avoid for convective hazards is fielded on any UAS):

### Layer 1: Planning
- NOAA TDR analyses, coastal NEXRAD near landfall, satellite imagery, recon observations define no-go volumes pre-launch
- Refreshed in flight via satellite link

### Layer 2: Onboard Situational-Awareness Radar
- X-band Doppler weather radar (Garmin GWX 75 baseline)
- Flags reflectivity cores 45–50 dBZ and Doppler turbulence tens of miles ahead
- ~10 lb with 10–12 in antenna, ~70 W draw; fits both demonstrator and objective aircraft
- Resolution: 7–8° beam, ~1.3 km features at 10 km (adequate for convective cores, marginal for 1 km mesovortex)

### Layer 3: S0 as Forward Pickets
- S0 released ahead of and below carrier report real-time 3-D wind, turbulence, pressure through carrier relay
- **Closes radar resolution gap** (e.g., Hugo mesovortex: 12.5 hPa pressure perturbation, sharp wind shifts)
- **Only distributed system already in storm can provide this capability**
- Multi-channel 430 MHz relay supports simultaneous S0 communications

### Layer 4: Reactive Layer
- Carrier's own wind estimation (SwiftCore) and load monitoring trigger:
  - Speed reduction on gust detection
  - Pattern truncation
  - Egress against approved thresholds (WP-006 Section 3.3)
- Gust-load-limiting autopilot reduces to turbulence-penetration speed

### BST's Qualifications for Sensor-Driven Guidance
- SwiftCore: real-time 3-D wind estimation, autonomous max-wind and storm-center finding from own measurements
- VORTEX2 lineage: UAS placed around supercells with mobile radar data in the loop
- NASA Swift Safe-to-Land program: coupled onboard sensing to autonomous flight decisions
- Same radar class addresses NOAA's open question on **detect-and-avoid for over-water BVLOS**

---

## Key Results & Validated Findings

### S0 Operational Record (2023–2026)
- **Wind-speed record:** 240 mph in Hurricane Milton (NCAR-verified)
- **FY26 launches:** 37 S0 launches from WP-3D
- **Dual-release operations:** Now routine
- **Extended flight time:** Flights sustained >2 hours
- **Boundary-layer operations:** 10–15 m above ocean on radar altimeter
- **Data assimilation:** Being integrated into NOAA operational hurricane model for first time in 2026 (first operational integration of uncrewed core observation)

### Historical Recon Data (Baseline for Carrier Sizing)
- **2024:** Both fleets (WP-3D + WC-130J) flew 1,609 reconnaissance hours
- **2025:** NOAA 63 flights, 417 hours into six hurricanes
- **Storm duration:** Average Atlantic storm ~5 days; Hurricane Lee (2023) lasted 13.5 days (30 flights, 69 center fixes)

### Environmental Encounter Documentation
- **Hugo (1989):** WP-3D experienced +5.8 g / -3.7 g at 1,500 ft; updrafts to 21 m/s
- **Milton TDR (2024):** 2–3 mesovortex couplets with 5–13 m/s drafts
- **Eyewall rain rates:** 50 dBZ echoes ≈ 74 mm/h (3 g/m³ liquid water)
- **Tropical freezing level:** Typically >15,000 ft in hurricanes (so 10,000 ft penetration stays below ice)

---

## Notable Details

### Why BST Succeeds Where Large Penetrator Concepts Failed

**Historical failures/stalls:**
- NOAA's ALTIUS air-launched program: dropped over cost
- Aerosonde and Coyote: proved access but not routine operations
- Larger/faster concepts: raise gust loads, reduce on-station time in data-rich zones, cannot support S0 distributed patterns

**Competitive advantages unique to BST:**
1. **Only operational uncrewed core observation system** (S0 in WP-3D since 2023; 37 launches FY26; 240 mph Milton record)
2. **Inside knowledge of prior air-launched effort** (BST contracted to outfit another vendor's vehicles with atmospheric payload in earlier NOAA program; saw first-hand where calibration, magnetics, interference, wind estimation stall programs)
3. **Storm-guided autonomy** (VORTEX2 UAS component: intercept supercells with mobile Doppler in the loop; NCAR hurricane-field hardware-in-the-loop simulation; autonomous max-wind and center-finding routines)
4. **Environmental qualification already funded** (Navy STTR N6833525C0270: S0 de-ice heaters, turbulence sensing, autonomous adaptive sampling, electric S0 variant with ~12 h endurance, longer-range platform Phase II)
5. **S3/S2 cold-weather heritage** (de-ice, salt-spray, northern Alaska/Greenland flight history; CJFC Arctic sprint; NCAS Greenland interest)
6. **Integration and approval path in hand** (WP-3D safe-separation testing, 430 MHz link tested to 400 km, AVAPS interference mitigation, NOAA data routing, NASA Langley 777 S0 integration, September 2026 USSOCOM S0-AD contract H9223626P9056)
7. **Contract vehicles exist** (NOAA IDIQ 1305M226D0012; S0 SBIR data-rights lineage: NAVAIR N251-016, STTR N6833525C0270, AF192-005 support Phase III without new competition)

### Policy Context
- **Current NHOP constraint:** Only one sUAS active per reconnaissance area, ≤5,000 ft MSL with 2,000 ft separation from crewed aircraft
  - Multi-S0 carrier concept requires policy revision
  - WP-006 Task 1 should carry this as requirement for NOAA and 53rd WRS

- **Legislative headwind:** Hurricane Hunter Aircraft Recapitalization Act cleared Senate Commerce July 2026; press coverage indicates requirement for crewed aircraft
  - Strategy: Pitch carrier as added observing capacity for crewed fleet, not replacement

### Strategic Partners (Pre-Existing BST Relationships)

| Partner | Role | Existing Tie |
|---------|------|--------------|
| Weather Stream / CU Boulder (A. Gasiewski) | Microwave sounding, SFMR-class radiometry, compact FMCW cloud/rain radar | WP-006 Task 6 partner; FMCW module development for S0 |
| NCAR | Storm simulation, data validation | Hurricane-field HIL support; Milton record verification |
| Embry-Riddle (J. Wadler) | Wind tunnel, boundary-layer science | Navy STTR subcontract; 777 wind tunnel plan |
| University of Miami / NOAA HRD (J. Zhang) | Requirements, data assimilation, TDR comparison | Navy STTR co-investigator |
| NASA Langley | High-altitude release, airworthiness review | 777 S0 integration; LaRC S0-AD purchase |
| KrateoSky | Production scale-up, capital, manufacturing | Strategic investor; Denton, TX facility |
| Airframe/Propulsion Partner (TBD) | Objective-aircraft structure, heavy-fuel or hybrid power | To be selected in WP-006 Task 2 |

### Risk Retirement Mapping (WP-006 Tasks)

Each risk identified has stopped larger programs; BST has specific mitigation and existing funded work:

| Risk | Industry Status | BST Approach | Retired In |
|------|-----------------|-------------|-----------|
| Rain ingestion | Group 3–5 UAS engines not eyewall-rated | Series-hybrid sealed generator nacelles behind inertial separators; electric propulsors (S0-proven class) in wet; battery bridge egress | Task 4, bench water-spray test, Option 1 |
| Gust loads on small airframe | 25–30 psf wing sees ~2× gust load factor vs. WP-3D | Uncrewed structure designed +6/−3 g limit loads; gust-load-limiting autopilot; 3-D wind from S0 algorithm | Task 4, Task 5 HIL |
| Mesovortex/extreme turbulence | No autonomous convective detect-and-avoid fielded on any UAS | Onboard X-band radar, S0 pickets, NOAA feeds, rule-based egress | Task 5; Option 3 progressive envelope |
| Flight-level winds >airspeed | Major-hurricane winds at 700 hPa exceed 150 kt | Patterns outside radius of max wind; upwind S0 release; airspeed set by trade, not P-3 match | Task 1, Task 2 |
| Icing in climb/descent/updrafts | Few UAS fly known icing; tunnel time ~$55k–$60k/day | S0 de-ice under Navy STTR; S3 cold-weather work; detection vendors engaged | Task 4; icing tunnel test Option 1 |
| Lightning, salt, humidity | Cumulative corrosion/connector failure rarely tested on UAS | S0 salt/sea-spray heritage at 10–15 m; S3 salt-spray qualification | Task 4 |
| Relaying many simultaneous S0 | WP-3D limited to two 430 MHz channels | Multi-channel 430 MHz relay on carrier; Starlink direct-to-cell pilot | Task 5 |
| Over-water BVLOS approval | New aircraft class for NOAA; no precedent airworthiness basis | UxSOC and AOC approval history; Navy VACAPES airspace experience from SASCWATCH | Task 7 |

### Icing Qualification Gap
- **No published rain/ingress rating exists for small UAS engines** → Task 4 closes gap
- **No UAS yet certified for known icing** (MQ-9B completed simulated-ice tests April 2026 only)
- NASA Glenn tunnel time: ~$55k–$60k per day (high cost driver for test program)

### Radar and Detect-and-Avoid Options Evaluated

| Candidate | Offering | Size/Power | Fit |
|-----------|----------|-----------|-----|
| Garmin GWX 75 / GWX 8000 | Certified X-band Doppler weather radar, turbulence detection | 10–13 lb, 10–14 in antenna, 40 W transmit | Demonstrator baseline; COTS, flight-proven |
| Weather Stream / CU Boulder | Compact FMCW cloud/rain radar, custom Doppler, radiometry | Prototype ~6 months for S0 | Fused radar/radiometer on objective; S0 compact radar (WP-006 Option 4) |
| Honeywell IntuVue RDR-84K | K-band detect-and-avoid and terrain radar | ~1.4 kg | BVLOS DA; no weather mode stated |
| Echodyne EchoFlight | K-band electronically scanned DA radar | ~0.8 kg, <40 W | BVLOS DA; no weather mode |
| ProSensing; NCAR EOL | Research airborne Doppler design and processing | To be scoped | Custom weather radar if COTS turbulence detection insufficient |

**Recommendation:** Fly demonstrator with COTS X-band unit + S0 pickets; use WP-006 Task 6 to decide if objective carries fused weather/DA/radiometer suite with Weather Stream.

### Crewed Reconnaissance Baseline (Operational Context)

**NOAA WP-3D:**
- Typical sortie: 7–10 hours (Milton TDR: 6.9 h, Lakeland to Mobile)
- Max endurance: ~8.5 hours below 18,000 ft
- Penetration altitude: ~10,000 ft (typically 8,000–10,000 ft; no lower than ~5,000 ft)
- Tasking: Two P-3s fly every 12 h; up to two TDR missions per 24 h
- Multi-aircraft philosophy: continuous coverage from rotation, not single long flight

**USAF WC-130J (10 aircraft):**
- Typical sortie: ~11 hours, 3,500 statute miles
- Max endurance: ~18 hours
- Penetration: ~10,000 ft; invests at or below 1,500 ft
- Tasking: Up to 5 sorties/day from 3 bases; 3-hourly fixes <300 nm coast, 6-hourly <500 nm
- Forward bases routinely used: St. Croix, Barbers Point, Curaçao
- Average sortie: 4–6 eye passes on 105 nm legs, ~1,000 nm transit each way

### Funding and Contract Authority
- **NOAA IDIQ 1305M226D0012** (existing BST vehicle)
- **S0 SBIR data-rights lineage:** NAVAIR N251-016, STTR N6833525C0270, AF192-005
- **Navy STTR N6833525C0270** (co-investigators: Embry-Riddle, University of Miami/HRD; covers S0 de-ice, turbulence sensing, adaptive sampling, electric S0 variant Phase II, longer-range platform)
- **September 2026 USSOCOM S0-AD contract H9223626P9056** (approval/integration precedent)

### WP-006 Structure (Implied from References)
- **Task 1:** Policy requirement (multi-S0 per area); operational concept
- **Task 2:** Objective-aircraft configuration (airframe/propulsion partner selection)
- **Task 3:** (Not explicitly named; likely flight testing or detailed design)
- **Task 4:** Environmental requirements derivation before configuration freeze; rain-ingress testing; icing tunnel tests
- **Task 5:** Hardware-in-the-loop simulation; hazard-avoidance testing; multi-S0 relay
- **Task 6:** Weather/detect-and-avoid radar selection and integration (Weather Stream decision point)
- **Task 7:** Over-water BVLOS airworthiness basis and approval path

---

## Summary of BST's Unique Positioning

This white paper establishes that:

1. **Sizing is physics-constrained, not arbitrary:** 12-hour demonstrator meets NHOP 300 nm requirement; 22–26 hour objective meets full WC-130J radius; neither requires large airframe (payload is only ~140 lb)

2. **Environmental challenges are solvable with existing BST heritage:** S0's eyewall flight record, storm-guided autonomy (VORTEX2), Navy-funded de-ice work, and S3/S2 cold/corrosion experience address every environmental risk identified

3. **Approval path is clear:** S0 integration with WP-3D, 430 MHz relay tested to 400 km, NASA Langley 777 integration, USSOCOM S0-AD contract, UxSOC/AOC history, Navy VACAPES airspace experience provide precedent and integration points

4. **Policy is moving in BST's favor:** Hurricane Hunter Recapitalization Act creates crewed recapitalization pathway; positioning carrier as added capacity (not replacement) avoids legislative headwind

5. **Partnership ecosystem is pre-positioned:** Weather Stream, NCAR, Embry-Riddle, University of Miami/HRD, NASA Langley, KrateoSky all actively engaged in funded or proposed work

6. **Competitive moat is deep:** Only S0 in operational hurricane use; only vendor with inside knowledge of prior air-launched program's failures; only team with storm-guided autonomy and distributed sensing proven in supercells and hurricanes

The document does not report new test results, but rather synthesizes existing S0 operational data, crewed-recon baselines, environmental encounter records, and BST capabilities to make the case for feasibility and BST's unique fit.