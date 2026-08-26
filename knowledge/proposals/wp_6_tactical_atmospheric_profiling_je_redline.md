# WP_6_Tactical_Atmospheric_Profiling_JE_redline

## Document Metadata
- Type: Capability proposal / White paper (draft with editorial notes)
- Client/Agency: U.S. Army Combat Capabilities Development Command (DEVCOM) — new customer
- Program/Solicitation: SBIR Phase III sole-source or S2MARTS/other OTA; also noted: PEO Aviation / PM UAS CSO "Launcher Approach Call for Solutions" (W58RGZ-26-S-C001, technical presentations due 13 Aug 2026)
- Date: 5 August 2026 (prepared); document modified 7 August 2026
- BST Products/Systems Referenced: S0 air-deployed, S0-VTOL, SwiftCore ground station
- Key Personnel: Jack Elston (last editor), Daniel Pendergast (point of contact), KrateoSky Inc. (coordination partner mentioned)

## Executive Summary
Black Swift Technologies proposes to extend proven U.S. Air Force tactical weather capabilities (S0 air-deployed platform) into Army precision airdrop, long-range fires, and launched-effects missions. The effort would integrate Army fire-control message formatting, conduct two field experiments demonstrating met profile improvements to airdrop and ballistic accuracy, and deliver six aircraft systems with transition analysis over 12 months using expiring FY26 O&M and FY25–26 RDT&E balances.

## Technical Approach

**Core Problem:** Precision airdrop accuracy, long-range fires ballistic solutions, and launched-effects employment rely on coarse gridded forecasts or radiosondes that cannot be deployed at point and time of need.

**BST Solution:**
- Deploy S0 air-deployed platforms to profile atmospheric conditions (winds, pressure, temperature, humidity) in actual drop or engagement corridors
- Field S0-VTOL from forward positions to rapidly generate full meteorological messages (MET-CM equivalent) within minutes
- Achieve 0.38 m/s wind-velocity resolution—accuracy class claimed to meaningfully reduce ballistic and airdrop solution error budgets
- Integrate met data into Army fire-control systems (MET-CM, MET-B, JPADS mission-planner formats) via SwiftCore ground station

**Key Integration Tasks:**
- Message formatting for Army fire-control interoperability (MET-CM/MET-B and JPADS mission-planner ingest)
- Interface development with AFATDS/AMDWS authority chain and PM-FSS (Natick)

## Products & Capabilities Described

### S0 Air-Deployed
- **What it is:** Autonomous atmospheric profiling platform launched from aircraft
- **Proposed use:** Release in actual drop/engagement corridor; profiles winds, pressure, temperature, humidity from release altitude to surface
- **Heritage:** Operational with U.S. Air Force for tactical weather support
- **Performance:** 0.38 m/s wind-velocity resolution

### S0-VTOL
- **What it is:** Man-portable, single-operator vertical-launch variant
- **Proposed use:** Deploy from firing positions to generate full met messages autonomously
- **Specifications:** 
  - Climb to 15,000 ft AGL
  - 90-minute endurance (note: draft contains editorial note questioning whether 15,000 ft climb is feasible within usable endurance window and flags airspace deconfliction/counter-UAS signature concerns in live-fire corridors)
  - Time to met message delivery: <20 minutes to 15,000 ft (Air Force Phase II data, hand-launched variant)
- **Key feature:** Launch-and-forget autonomy, minimal training burden

### SwiftCore Ground Station
- **What it is:** Ground control and data ingest system
- **Proposed use:** Message formatting for Army fire-control interoperability

## Use Cases & Applications

1. **Precision Airdrop (JPADS):** In-corridor atmospheric profiling to improve Joint Precision Airdrop System (JPADS) accuracy vs. baseline coarse forecast methods

2. **Long-Range Fires:** Deployment of fresh met profiles to reduce ballistic solution error; comparison of met message freshness vs. solution error

3. **Launched-Effects:** Referenced as primary responsive use case; S0 air-deployed heritage and April 2026 single-operator multi-vehicle validation cited as directly responsive to PEO Aviation / PM UAS CSO launcher approach requirements

## Field Experiments Proposed

- **Experiment 1 (Precision Airdrop):** JPADS accuracy measurement with and without in-corridor S0 profiles
- **Experiment 2 (Fires):** Met message freshness vs. ballistic solution error analysis

## Budget & Scope (Rough Order of Magnitude)

| Element | Amount |
|---------|--------|
| Aircraft systems & spares (6 aircraft, mixed variants) | $610,000 |
| Fire-control / JPADS message formatting & integration | $290,000 |
| Two field experiments (range costs, personnel, analysis) | $340,000 |
| Transition & requirements-alignment report | $160,000 |
| **Total** | **$1,400,000** |

**Funding Sources:** FY26 O&M and FY25–26 RDT&E expiring balances (deadline: 30 September 2026)

**Period of Performance:** 12 months (integration, two field experiments, transition report)

**Deliverables:** Six aircraft systems (mixed air-deployed and VTOL) with spares for government experimentation and residual use

## Notable Details

- **Air Force Heritage:** U.S. Air Force operational employment under AF192-005 materially de-risks technical evaluation; Air Force 557th Weather Wing is named consumer; approximately half of all USAF weather activity supports Army operations
- **April 2026 Validation:** Single-operator multi-vehicle validation recently completed, supporting credibility for Army employment
- **Supply Chain:** All-U.S. supply chain; platforms transportable on commercial aviation
- **Data Standards:** Already writes BUFR, GRIB, and netCDF to Air Force standards under AF192-005 (noted as shortening distance to Army integration but editorial note flags $290K message formatting budget as under-scoped)
- **DEVCOM Entry Point:** New customer relationship; DEVCOM doors described as strongest through Launched Effects pathway (PEO Aviation / PM UAS CSO) rather than other mentioned DEVCOM divisions

## Editorial Notes (from Redline Draft)
The document includes substantive editorial comments questioning:
- Feasibility of S0-VTOL climbing to 15,000 ft within 90-minute endurance constraint and use-case timing
- Airspace deconfliction and counter-UAS signature risk in live-fire corridors for VTOL operations
- Under-scoping of $290K message formatting budget for MET-CM (Army artillery met format) and JPADS mission-planner ingest integration; recommends re-scoping given complexity of AFATDS/AMDWS chain and PM-FSS coordination