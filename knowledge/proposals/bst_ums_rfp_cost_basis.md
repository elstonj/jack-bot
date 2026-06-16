# NOAA UMS RFP — Scenario-Based Cost Estimate: Basis of Estimate & Tier Scoping

## Document Metadata
- Type: Internal cost proposal / budget basis document
- Client/Agency: NOAA AOML (Atlantic Oceanographic and Meteorological Laboratory)
- Program/Solicitation: NOAA UMS (Uncrewed Meteorological Systems) RFP
- Date: June 15, 2026
- BST Products/Systems Referenced: S0, S0-VTOL, S3, SwiftCore
- Key Personnel: Jack Elston (Principal Investigator), Beck Cotter (budget lead); NOAA contacts: Annette Hollingshead, Joe Cione, Jun Zhang, Josh Wadler

## Executive Summary
Black Swift Technologies proposes a tiered 2-year hurricane boundary-layer sampling program using S0-VTOL and S3 uncrewed aircraft to deliver real-time atmospheric profiles to NOAA during hurricane season. The proposal structures costs around a data-buy model with three capability tiers ($1.4M–$2.1M) that scale from coastal landfall operations (Low) through Barbados forward-deployed pre-storm sampling (Medium) to full inner-core air-deployed operations with long-range coverage (High). All pricing centers on a competitive ~$9,000 per delivered profile, with tier differences driven by scope, deployment frequency, and NRE integration costs rather than unit aircraft cost.

## Technical Approach

**Operating Scenario (14-Day African Hurricane Track):**
- Days 1–3: No effort; wave emerges
- Days 4–6: Domestic/Tropical Storm (D/TS) ops from Barbados; S0-VTOL forward-deployed sampling pre-storm ABL (20–3000 m) at T−24–48 h and in-storm ABL (20–1500 m) at T=0; real-time data to NHC/EMC/AOML
- Days 7–14: Traditional Hurricane Hunter ops (Caribbean, W. Atlantic, Gulf, landfall) with two phases:
  - *Coastal/Landfall*: S0-VTOL within ~12 nm of coast, remote ops (unsafe T<12 h)
  - *Inner-core*: Air-deployed S0 from G-IV/G-III at ~40,000 ft, profiling 40k–0 ft (subject to NHOP altitude / WRA constraints)

**Data Pipeline & Integration:**
- Real-time ABL data delivered to NOAA centers (NHC/EMC/AOML)
- SwiftCore ABL data-processing scripts
- Host-aircraft air-launch integration & airworthiness case
- Barbados forward-site setup and operations

**Cost Model Drivers:**
- Data-buy structure: NOAA pays per profile delivered (no standing retainer)
- Per-profile cost (~$9,000): includes S0 airframe fabrication/consumption, field execution, real-time processing/telemetry
- Mob/Demob per deployment ($40–50k per storm response)
- NRE (Year 1 integration + minor Year 2 sustaining): grows with tier scope

## Products & Capabilities Described

### S0-VTOL
- **Type:** Fixed-wing, deep-stall / VTOL recovery capability
- **Endurance:** 90 minutes
- **Ceiling:** 15,000 ft AGL
- **Cruise:** 17 m/s (38 mph); 30 kt (15 m/s) wind resistance
- **Range:** ~170 nm air-deployed glide profile
- **Payload/Weight:** 3.5 lb AUW, integrated meteorological sensor
- **Sensors:** 3-D wind, temperature, RH/dewpoint, pressure, sea-surface temperature
- **Unit Cost:** $18,000 per airframe (draft basis)
- **Heritage:** Guinness record holder for highest wind speed measured by uncrewed aircraft (240 mph, Hurricane Milton, October 2024); purpose-built for hurricane boundary layer; deployed from NOAA WP-3D
- **Proposed Use:** Primary platform for both Barbados D/TS pre/in-storm sampling and coastal/landfall operations; air-deployable variant from G-IV/G-III for inner-core profiling

### S3 (Long-Range VTOL Fixed-Wing)
- **Type:** VTOL fixed-wing
- **Endurance:** 110 minutes (90 minutes nominal)
- **Ceiling:** 20,000 ft MSL
- **Range:** 110 km (60 nm)
- **Payload:** 2.7 kg (6 lb), field-swappable
- **Unit Cost:** TBD (to be confirmed with Jack Elston)
- **Proposed Use:** Extended offshore coverage option in High tier only; not included in Medium or Low tiers

### SwiftCore
- **Proposed Use:** ABL data-processing and real-time telemetry scripts for integration with NOAA's NHC/EMC/AOML systems

## Use Cases & Applications

**Mission:** Real-time tropical cyclone / hurricane boundary-layer characterization across the lifecycle of a system moving from African genesis to U.S. landfall

**Specific Operations:**

1. **Pre-Storm ABL Sampling (Barbados D/TS phase, Days 4–6)**
   - Forward-deployed S0-VTOL sampling 24–48 h before storm arrival
   - Profiles: 20–3000 m altitude
   - Measurements: offshore SST, RH, low-level wind structure
   - Real-time delivery to NOAA forecast centers

2. **In-Storm ABL Sampling (Days 4–6, at T=0)**
   - S0-VTOL coastal/landfall ops within ~12 nm of coast
   - Profiles: 20–1500 m
   - Measurements: low-level wind maxima, surface circulation center
   - Remote operations (unsafe for crews T<12 h before landfall)

3. **Inner-Core Profiling (High tier only, Days 7–14)**
   - Air-deployed S0 from G-IV/G-III at ~40,000 ft
   - Full 40,000–0 ft profiles around the circulation center
   - Subject to NHOP altitude / WRA deconfliction constraints

4. **Extended Offshore Coverage (High tier only)**
   - S3 long-range operations for extended sampling range

## Cost Structure & Pricing Tiers

### Fully Comprehensive Solution — High Tier ($2,100,000 / 2 years)
- **Data sets:** ~133 profiles @ $9,000 each = $1,200,000
- **Mob/Demob:** 6 deployments @ $50,000 = $300,000
- **NRE:** $550,000 (Year 1) + $50,000 (Year 2 sustaining) = $600,000
- **Deployments:** ~3 storm responses per season (6 over 2 years)
- **Scope:** Both D/TS and coastal/landfall phases + air-deployed inner-core (G-IV/G-III) + S3 long-range offshore
- **Capability:** Full multi-aircraft coordinated operations; highest complexity and risk (inner-core airworthiness/integration, highest airframe attrition)

### Partially Comprehensive Solution — Medium Tier ($1,750,000 / 2 years)
- **Data sets:** ~130 profiles @ $9,000 each = $1,170,000
- **Mob/Demob:** 4 deployments @ $45,000 = $180,000
- **NRE:** $370,000 (Year 1) + $30,000 (Year 2 sustaining) = $400,000
- **Deployments:** ~2 storm responses per season (4 over 2 years)
- **Scope:** Barbados D/TS pre-storm and in-storm ABL sampling AND coastal/landfall S0-VTOL ops
- **Excludes:** Air-deployed inner-core ops; S3 long-range

### Proof of Concept — Low Tier ($1,400,000 / 2 years)
- **Data sets:** ~119 profiles @ $9,000 each = $1,070,000
- **Mob/Demob:** 2 deployments @ $40,000 = $80,000
- **NRE:** $250,000 (Year 1) + $0 (Year 2) = $250,000
- **Deployments:** ~1 storm response per season (2 over 2 years)
- **Scope:** Single operational phase (coastal/landfall S0-VTOL within 12 nm of coast, remote ops only); real-time integration foundation
- **Excludes:** Barbados D/TS forward operations; air-deployed inner-core; S3 long-range

### Cost Building Blocks (Fully Burdened Rates)
- **Fringe:** 29.28% of direct labor
- **Overhead (OH):** 46.67% of (labor + fringe)
- **G&A:** 18.32% of (labor + fringe + OH + ODCs)
- **Fee/Profit:** 7.00% of total cost
- **Loaded Labor Rates:**
  - Principal Investigator: ~$236.61/hr (from $98.56 raw)
  - Engineer/Operator: ~$201.95/hr (from $84.13 raw)

**Key Unit Inputs:**
- S0-VTOL airframe: $18,000
- S3 unit cost: TBD
- Loaded field labor: $200–237/hr
- Per-profile cost (blended): ~$9,000 (dominant sensitivity is airframe attrition rate)

## Key Capability Constraints & Caveats

**Low Tier Limitations:**
- Cannot fund Barbados D/TS forward operations or air-deployed inner-core sampling
- Realistically one storm per season
- No S3 long-range coverage

**Medium Tier Limitations:**
- Cannot fund air-deployed inner-core ops from G-IV/G-III
- No S3 long-range offshore

**High Tier Caveats:**
- Inner-core air-deployed ops carry highest airworthiness/integration risk
- Highest airframe attrition in inner-core subset (per-profile airframe cost share higher than coastal ops)
- 40k-ft G-IV/G-III deployment subject to NHOP altitude / WRA deconfliction constraints

## Notable Details

**Regulatory & Export:**
- S0 and S3 are EAR99, U.S.-built, non-ITAR — keeps Barbados forward operating location clean on export licensing

**Heritage & Performance:**
- S0 holds Guinness record for highest wind speed measured by uncrewed aircraft (240 mph, Hurricane Milton, October 2024)
- Purpose-built for hurricane boundary-layer missions
- Proven deployment from NOAA WP-3D platform

**Cost Model Philosophy:**
- No standing retainer line; "readiness" is embedded in per-profile airframe cost (fabricate inventory pre-season)
- Data-buy structure keeps per-profile price competitive across all tiers
- Tiers differ by *scope* (operational phases) and *volume* (deployments/profiles), not by unit aircraft cost

**Critical Dependencies & Open Items to Confirm:**
1. **Airframe attrition/recovery expectations** — dominant cost sensitivity; distinguish coastal (recoverable) vs. inner-core air-deployed (largely expended) sorties
2. **S3 unit cost** — TBD if priced separately in High tier or folded into blended profile cost
3. **Host-aircraft availability** — P-3/G-IV/G-III assumed NOAA-furnished (flagged as dependency, not BST cost)
4. **Raw labor rates** — field roles beyond PI and engineer need confirmation
5. **Season activity** — profile counts assume typical season; quiet or hyperactive season shifts counts
6. **Pricing granularity** — confirm whether NOAA prefers per-data-set, per-mission, per-storm, or other unit

**NOAA Requirements Met:**
- Caps are not-to-exceed ($1.4M–$2.1M over 2 years)
- Caps and objectives described as "somewhat flexible" by NOAA
- Delivers real-time data to NOAA centers (NHC