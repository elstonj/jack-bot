# WP-BST-006: Response to OMAO Technical Review

## Document Metadata
- **Type:** White paper / technical response to peer review
- **Client/Agency:** NOAA, Office of Marine and Aviation Operations (OMAO)
- **Program/Solicitation:** WP-BST-006 (uncrewed carrier aircraft for S0 operations)
- **Date:** October 27, 2026
- **BST Products/Systems Referenced:** S0 (air-deployed expendable probe), S2, S3, proposed uncrewed carrier aircraft
- **Key Personnel:** Jack Elston (last editor), Alan Goldstein (OMAO reviewer), RADM Cary (NOAA leadership mentioned)
- **Related Documents:** Original proposal WP-BST-006 (Aug 19, 2026); Goldstein's technical review (Oct 13, 2026)

## Executive Summary

BST responds to OMAO's technical review of its proposal for an uncrewed carrier aircraft to deploy S0 probes in tropical cyclones. The company withdraws three unsupported arguments (P-3 capacity recovery, crew exposure reduction, 2030 transition utility) but stands on the core value proposition: persistence. A four-aircraft carrier rotation would maintain continuous S0 coverage 24/7 in the boundary layer, whereas crewed platforms (P-3, WC-130J) can only relay S0 while on station. BST reframes the $9.9M program as a demonstrator to prove scale, propulsion, release, hazard avoidance, and airspace integration before building an operational fleet.

## Technical Approach

### Demonstrator vs. Operational Aircraft

**Demonstrator (WP-006 Option 1) specifications:**
- Gross weight: 600–800 lb (vs. 1,200–2,000 lb operational)
- Endurance: 12 hours (vs. 22–26 hours full mission or 14–16 hours from forward bases)
- S0 stations: 6 (vs. 10–12 operational)
- Radius: ~400 nm from base for single sortie with 3 hours on station
- Built by BST

**Key design decisions:**
- Not a retrofit of crewed aircraft (rejects Dominator II and similar conversions)
- Purpose-built structure designed for eyewall gusts, icing, and rain ingress
- Twin heavy-fuel and hybrid-electric propulsion tested in real weather
- Self-contained S0 design to minimize weight/drag on wing station
- Wing-pod carriage capability for wider aircraft compatibility

### Program Structure (5 gates with decision points)

1. **Requirements (month 3):** Persistence requirement validation with AOML/HRD/EMC; basing and corridor ranking; National Hurricane Operations Plan revision for small-UAS rule
2. **Airframe (month 8):** Storm load/icing requirements, demonstrator configuration, scaling to operational aircraft, benchmarking against existing platforms, airspace/airworthiness pathway
3. **PDR (month 12):** Configuration, dispenser, autonomy, fleet acquisition and operating cost estimate
4. **Weather readiness:** Progressive envelope expansion and separation/multi-S0 relay testing
5. **Storm demonstration:** Instrumented penetration coordinated with crewed mission; decision on in-house build vs. strategic partner

### Airspace and Airworthiness

- **Operating basis:** NOAA public aircraft under FAA COA, sponsored by UxSOC as NOAA's FAA point of contact
- **No-chase model:** NASA Ikhana (MQ-9) serves as precedent—unescorted flight in Class E/A airspace via Mode S transponder, ADS-B Out, ATC voice relay, onboard detect-and-avoid radar, and Section 919 FAA Reauthorization Act approval pathway
- **Demonstrator constraint:** Operates from coastal fields with direct access to restricted/warning areas over water; restricted-airspace procedures on departure; U.S.-controlled oceanic airspace for initial flights
- **Foreign/Caribbean ops:** Initial concept limited to 300–500 nm of U.S. coast over U.S./international waters; Caribbean operations deferred pending diplomatic clearances and Section 934 ICAO international standards (effective Nov 26, 2026)
- **Coordination:** Task 1 revises National Hurricane Operations Plan rule allowing small UAS at ≤5,000 ft to permit carrier at 10,000 ft releasing multiple S0

## Products & Capabilities Described

### S0 (Air-Deployed Probe)

**What it is:** Small expendable meteorological probe deployed from aircraft to measure hurricane boundary-layer conditions.

**Performance and history:**
- Approximately 2-hour lifespan per probe
- 2025 season: 17 successful flights totaling ~18 hours against 417 P-3 flight hours
- S0 data entered NOAA's operational hurricane model for first time in 2026
- Preliminary NOAA study showed ~10% better intensity forecasts with S0 data

**Current limitations:**
- Limited to deployment while host aircraft on station
- Historically one S0 per sortie, then two simultaneous (via second telemetry channel added in 2026)
- Data return limited to 430 MHz link capacity

**S0 improvements proposed:**
- **Multi-channel relay:** Upgrade to P-3 and C-130J ground stations enabling three simultaneous S0 instead of current two
- **Self-contained redesign:** Reduces weight/drag for wing-station mounting (applicable to carrier and wing-pod carriage on any aircraft)
- **Satellite command and data link:** Starlink direct-to-cell pilot integration; enables "drop and forget"—S0 released at end of P-3 mission continues reporting 2+ hours after aircraft departs; provides full data set vs. what fits 430 MHz link; supports three sequential 2-hour flights per sortie instead of two
- **Wing-pod carriage:** Self-contained S0 and wing-station release compatible with wider range of crewed and uncrewed aircraft

### Carrier Aircraft (Demonstrator)

**What it is:** Purpose-built, uncrewed aircraft designed to deploy S0 probes autonomously in tropical cyclones while maintaining 24-hour boundary-layer coverage.

**Design approach:**
- Internally designed by BST (not converted from crewed type)
- Twin heavy-fuel and hybrid-electric propulsion (architecture to be proven in real storm conditions)
- Radar plus S0-informed hazard avoidance and automated mesovortex egress
- Sensor-driven autonomy

**Demonstrator goals:**
1. **Storm loads:** Instrumented airframe measures gust loads, rain ingress, icing exposure in real eyewall conditions
2. **Propulsion in water:** Validates heavy-fuel and hybrid-electric architecture for rain/water ingress survival
3. **Release and relay:** Proves wing-station separation and simultaneous multi-S0 relay (size-independent)
4. **Hazard avoidance:** Validates radar + S0 detection of mesovortices and automated egress software
5. **Airspace integration:** Establishes approvals, equipment, and procedures for fleet operations

**Operational concept (demonstrator):**
- Four-aircraft rotation maintains ≥1 S0 in boundary layer continuously (24 hrs/day)
- Uses ~18 S0 per storm-day
- With multi-S0 relay upgrade, raises coverage from 8 hours/day (two sequential S0 per crewed sortie) to 12 hours/day (three per sortie) + 24-hour continuous via carrier
- Addresses final 24–48 hours before landfall, including overnight and between crewed reconnaissance fixes

### S2 and S3

**Mentioned briefly:**
- Referenced as small BST aircraft; relevant experience noted as not about airframe size but about storm environment, S0, release/relay, sensor-driven autonomy, and NOAA operations
- S3 has airspace deconfliction experience with NASA

## Use Cases & Applications

### Primary Mission: Tropical Cyclone Reconnaissance

**Operational scenario:**
- U.S.-threatening hurricanes within 300–500 nm of U.S. coast
- Persistence gap: Current crewed fleet (P-3 TDR, WC-130J) can operate up to two sorties per 24 hours; each sortie covers a few hours on station
- S0 provides continuous boundary-layer wind, pressure, temperature data during critical pre-landfall period (24–48 hours)

**Forecast impact:**
- 2026: S0 data first entered NOAA's operational hurricane model
- Preliminary study: ~10% improvement in intensity forecasts with continuous S0 observations
- Gap identified: overnight observations and data between crewed fixes currently unavailable

### Secondary Applications (Early Deliverables Independent of Carrier)

**Atmospheric river missions:** Air Force Reserve C-130s over Pacific; long-transit S0 releases benefit from satellite-linked "drop and forget" capability

**Multi-S0 coordination:** Multiple simultaneous S0 relay supports expansion of operations on P-3 and C-130J without carrier

## Concessions to OMAO Review

BST withdrew three arguments that did not withstand scrutiny:

1. **"Return P-3 capacity"** – Argument that carrier would free crewed sorties. Fact: S0 drops have not compromised P-3 primary mission; constraint runs opposite direction (S0 timing/location set by P-3 availability).

2. **"Crew exposure reduction"** – Argument that uncrewed operations reduce risk. Fact: UAS crews change shifts on ground without landing aircraft; binding limit is aircraft on station, not crew hours.

3. **"Bridge 2030 P-3 to C-130J transition"** – Argument that carrier would support transition. Fact: Schedule does not support 2030 ops (demonstrator not flight-ready until 2030 season with 2027 start); RADM Cary accepted that 5+ year effort is appropriate for this problem.

## Key Technical Arguments in Response to Specific Concerns

| Concern | BST Response | Change |
|---------|--------------|--------|
| $9.9M is too cheap relative to military MALE programs | MALE programs cost hundreds of millions for 10,000 lb aircraft with weapons/secure datalinks. Carrier is 600–2,000 lb with 3 lb S0 payload; $9.9M covers design, one prototype, storm demo—not certified fleet. Fleet cost estimated at PDR gate. | State fleet acquisition cost as separate, later estimate (Task 7) |
| S3/S2 are small; carrier is mostly new design | Agreed. Relevant experience is storm environment, S0, release/relay, sensor autonomy, NOAA ops—where every prior uncrewed hurricane effort stalled. | Recast as demonstrator proving larger design and informing build-or-partner decision |
| Weight figures (900–1,900) misinterpreted as range | Corrected: 550–1,000 lb baseline, 1,100–1,900 lb growth variant (gross weights). 12-hour demonstrator ~400 nm radius single sortie; 22–26 hour operational or 14–16 from forward bases reaches ~1,000 nm. | Clarify weights in proposal; add range specifics |
| Dominator II fits better than MQ-9 comparison | Fair benchmark: twin diesel, 20+ hrs endurance. But converted DA42 crewed light twin not designed for eyewall gusts; costs ~$10M/unit. | Use Dominator as benchmark for objective aircraft, not demonstrator |
| Takeoff/landing over populated areas | Agreed—basing constraint. Candidate fields: coastal sites with adjoining restricted/warning areas over water. | Basing and departure corridors become Task 1 deliverable |
| Airspace, ATC, certification left to NOAA | Fair criticism. Part 108 won't solve it (SUAS below 400 ft, <1,320 lb, prohibits transponders). NAS flight at 10,000 ft needs transponder, ADS-B, ATC voice relay, Part 108 exception or alternative basis. | BST owns airspace/airworthiness pathway as funded task with UxSOC; models on NASA Ikhana and Section 919 FAA Reauthorization Act for federal UAS |
| Foreign airspace and ADIZ limits (Caribbean) | Agreed. Initial ops cover U.S.-threatening storms within 300–500 nm U.S. coast, mostly U.S./international waters. Caribbean ops depend on diplomatic clearances pursued with OMAO. | Narrow concept to near-landfall U.S. coverage first; defer Caribbean |
| Two-S0 telemetry limit is bottleneck, not P-3 | Correct. BST moved to two simultaneous in 2026; can extend further. Crewed aircraft carry more but only use while on station. | Add multi-S0 telemetry upgrade for P-3/C-130J as near-term deliverable; base carrier case on persistence, not magazine size |
| Sleeve/tube restrictor could replace self-contained S0 redesign | Self-contained S0 needed for wing-station external mounting to save weight/drag (every lb/inch costs endurance). Same work lets S0 fly in wing pods on other aircraft. | Keep self-contained S0 as wing-station and wing-pod item; clarify rationale |

## Notable Details

### Airspace Integration Strategy

BST explicitly adopts **NASA's Ikhana model** for unescorted operation in controlled airspace:
- **Equipment:** Mode S transponder, ADS-B Out, ATC voice relay (line-of-sight and satellite), detect-and-avoid radar onboard
- **Approval basis:** Section 919 of FAA Reauthorization Act of 2024 directs FAA/DoD to determine federal non-small UAS requirements for NAS operation outside restricted airspace without escort
- **Precedent:** Ikhana (MQ-9) already flying unescorted in Class E/A airspace near 10,000 ft
- **Constraints for demonstrator:** Depart from coastal field with direct restricted/warning-area access over water; accept escort or restricted-area procedures on departure; fly tests in U.S.-controlled oceanic airspace until approval path complete

### International Standards and Diplomatic Path

- **ICAO Annex 6 Part IV** (certificated RPAS): Effective November 26, 2026
- **Section 934, FAA Reauthorization Act:** Directs FAA–ICAO coordination on UAS approval over high seas in U.S.-controlled oceanic regions
- **Legal question:** Whether NOAA can operate under state-aircraft "due regard" provisions beyond 12 nm requires legal opinion
- **Deferred:** Caribbean operations, Mexico/Cuba/Bahamas proximity flights pending resolution

### Operational Partnership with 53rd WRS and CARCAH

- **Current National Hurricane Operations Plan:** Allows one small UAS per reconnaissance area at ≤5,000 ft
- **Required revision:** Permit carrier at 10,000 ft releasing multiple S0; coordinated with 53rd Weather Reconnaissance Squadron and CARCAH (Civilian Air Route Clearance Authority for Hurricanes)
- **Task 1 deliverable:** Recon coordination rule revision

### S0 Release Approval History

BST cites existing airspace/operations experience:
- S0 release approvals and procedures on P-3 with AOC (Air Operations Certificate) and UxSOC
- Navy VACAPES airspace coordination for SASCWATCH flights
- Airspace deconfliction with NASA on S3
- NASA Langley 777 S0 integration currently underway

### Cost Framing

- **$9.9M ROM (Rough Order of Magnitude):** Design, one prototype, one storm demonstration
- **Includes:** Demonstrator build, clear-air test, airspace/airworthiness pathway work with UxSOC
- **Does not include:** Certified fleet acquisition (estimated separately at PDR gate, Task 7)
- **Positioning:** "Lowest-cost serious attempt OMAO has seen"

### Comparative Benchmarks (Rejected or Benchmarked)

- **MQ-9 Reaper:** Export-controlled, priced per unit above program total
- **Dominator II (Aeronautics DA42 conversion):** Twin diesel, ~20 hrs endurance, ~$10M/unit; used as objective aircraft benchmark, not demonstrator model
- **Military CCAs/UCAVs:** Jet aircraft, export-controlled, per-unit cost above program total; unlikely affordable in numbers; Task 2 surveys alongside piston and hybrid options

### Forecast Value and NOAA Model Integration

- **2025 season:** 17 successful S0 flights, ~18 total flight hours (vs. 417 P-3 flight hours in same season)
- **2026 milestone:** S0 data entered NOAA's operational hurricane model for first time
- **Preliminary impact:** ~10% improvement in intensity forecasts with continuous S0 observations
- **Critical gap:** 24–48 hours before landfall, including overnight and between crewed reconnaissance fixes, lacks boundary-layer observations

### Questions for NOAA Decision (Posed by BST)

1. Does HRD/EMC value continuous boundary-layer coverage in final 48 hrs enough to set as Gate 1 requirement?
2. Global Hawk program COA, escort, basing costs in time/money; which would carry over to 10,000 ft aircraft?
3. Which coastal fields has OMAO considered for uncrewed ops with adjoining restricted/warning airspace?
4. Which demonstrator risks matter most: loads, propulsion in rain, release, hazard avoidance, or airspace?
5. Would OMAO support satellite-linked, drop-and-forget S0 trial from P-3 in 2027 season?
6. Appetite to start near-term S0 items (multiple simultaneous, satellite link, wing pods) ahead of carrier decision?

## Document Quality and Significance

**Strengths:** Detailed technical response point-by-point to peer review; clear articulation of demonstrator rationale and scaling principles; integration of regulatory pathways (Section 919, 934 FAA Reauthorization; ICAO Annex 6 Part IV); gating structure for phased decision points; explicit acknowledgment of concessions and reframing around core value proposition (persistence).

**Significance:** Represents major refinement of proposal based on NOAA expert feedback; demonstrates BST's willingness to withdraw unsupported arguments and rebuild case on verifiable persistence benefit; shows deep understanding of NOAA operations, airspace regulatory landscape, and tropical cyclone forecasting needs; establishes roadmap for demonstrator as proof-of-concept that de-risks operational fleet decision.

**Context note:** Document dated Oct 27, 2026, is response to Oct 13, 2026 review; indicates active, iterative proposal development cycle with NOAA stakeholder engagement circa mid-2026.