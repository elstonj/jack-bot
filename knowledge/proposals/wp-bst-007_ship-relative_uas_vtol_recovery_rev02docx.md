# Autonomous Ship-Relative UAS VTOL Recovery for Persistent Maritime Observation

## Document Metadata
- **Type:** White paper / capability proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations (OMAO) / Uncrewed Systems Operations Center
- **Program/Solicitation:** NOAA IDIQ vehicle (1305M226D0012); potential SBIR Phase III sole-source (NAVAIR N251-016, STTR N6833525C0270, AF192-005); NOAA BAA (open through 30 September 2026)
- **Date:** May 21, 2026
- **BST Products/Systems Referenced:** S0-VTOL, S3, SwiftCore (Flight Management System), SwiftPilot (autopilot), SwiftStation (ground station), SwiftTab (operator interface), Swift Safe-To-Land (machine vision)
- **Key Personnel:** Brian Grubel (last editor)

## Executive Summary

Black Swift Technologies proposes a ship-relative autonomous recovery system for NOAA's S0-VTOL aircraft, combining differential-GPS approach with cooperative visual or infrared terminal guidance to enable routine, repeatable VTOL recovery from moving vessels. The solution reduces operator workload during the most challenging phase of shipboard flight and provides a reusable integration package applicable across NOAA vessels. The approach builds on BST's existing S0 integration with NOAA, SwiftCore autonomy capabilities, S2 Arctic operations experience, and MIZOPEX full-system-readiness lessons.

## Technical Approach

**Core Architecture:**
- **Ship-relative navigation frame** established between aircraft and vessel using differential GPS for outer approach
- **Cooperative terminal guidance** via visible or infrared deck target for precise terminal-phase relative-pose estimation
- **Layered navigation architecture** combining GPS, cooperative target data, and onboard motion sensors to avoid single-point dependency
- **Motion compensation** with explicit vessel-heading and velocity matching before descent
- **Superstructure obstacle avoidance** using mapped keep-out zones relative to vessel attitude
- **Safety gates** evaluating navigation integrity, target confidence, aircraft state, deck-zone availability, approach geometry, and environmental limits before progressing through each phase

**Flight Phases:**
1. Vertical launch from vessel
2. Transition to efficient fixed-wing flight
3. Execute approved observation mission
4. Return to ship-relative holding point
5. Capture approved approach corridor
6. Match vessel motion and heading
7. Transition to hover over deck target
8. Terminal descent and touchdown with explicit hold, wave-off, go-around, abort, and manual-takeover paths available

**Ground Station Integration:**
- SwiftStation manages aircraft data link and ship-reference interface
- SwiftTab provides mission configuration, operator monitoring, status annunciation, and manual-control access
- Ship master and mission owner retain authority over operating area, payload, deck zone, approach corridor, weather limits, and recovery operations

## Products & Capabilities Described

### S0-VTOL
- **What it is:** Compact vertical-takeoff-and-landing aircraft, existing operational platform
- **Proposed use:** Base platform for autonomous ship-relative recovery demonstrations; four systems to be delivered to NOAA configured for cooperative-target recovery
- **Specifications:** Foundation for near-term development; S0 has prior integration experience with NOAA P-3 and measurement validation against environmental instruments
- **Configuration:** Equipped with differential-GPS receivers and ship-reference interfaces for autonomous recovery

### S3
- **What it is:** Next-generation VTOL platform with extended capability
- **Proposed use:** Growth path for longer-range and higher-payload maritime missions (Option 4)
- **Specifications:** 
  - Up to 110 minutes flight time
  - 2.7 kg (6 lb) payload capacity
  - 20,000 ft MSL ceiling
  - 110 km range
  - 30-knot wind resistance
  - IP42 ingress protection
- **Approach:** Same autonomous recovery architecture transferred and validated on S3 over estimated 3–6 months; two S3 development systems to be delivered

### SwiftCore Flight Management System
- **Components:** SwiftPilot autopilot, SwiftStation ground station, SwiftTab operator interface, aircraft and payload interfaces, mission management, autonomous flight-control functions
- **Demonstrated capability:** Autonomous mission execution from launch through recovery; advanced landing algorithm; laser-based landing system for precise autonomous belly landings
- **Use in this context:** Underlying autonomy and operator architecture; fuses navigation and terminal-sensor information for approach-to-touchdown phase; manages hold, wave-off, go-around, and abort behavior

### Swift Safe-To-Land (Machine Vision)
- **What it is:** Compact, low-power onboard system using semantic segmentation to process high-resolution imagery for hazard detection
- **Developed under:** NASA SBIR award
- **Capabilities:** Pixel-level classification of people, vehicles, structures, terrain, and hazards; identifies and selects safer emergency landing areas
- **Relevance:** Establishes foundations for onboard perception, scene segmentation, obstacle identification, and integration of machine-vision outputs with autonomous flight decisions applicable to ship-relative navigation and moving-deck touchdown; targetless ship recognition is a separable growth option

## Use Cases & Applications

**Primary Mission Profile:**
- NOAA vessels equipped with S0-VTOL as organic "mobile weather tower" and sensor platform
- Persistent maritime observation including atmospheric profiling, orbiting operations, and return to vessel
- Repeatable cycle operations across multiple NOAA missions and vessels

**Sensor/Mission Payloads Referenced:**
- Atmospheric measurements (profiling, radiometry)
- Imaging and electro-optical observations
- Fisheries surveys
- Hydrographic data collection
- Sea-surface observations
- Protected-species monitoring

**Operating Domains:**
- Open ocean and near-shore operations
- Vessel-relative approach and recovery in deck motion, relative wind, and wake turbulence
- Operations in degraded visibility and navigation conditions (with optional coastline-matching extension)

## Key Results / Past Performance

**S0 Integration History:**
- Air-deployed S0 integration with NOAA P-3 aircraft established procedures for deployment, RF integration, ground-station operation, operator displays, and environmental-data delivery
- S0 measurements validated against towers, sondes, tail Doppler radar, and modeled fields

**SwiftCore Autonomy:**
- Demonstrated autonomous mission execution from launch through recovery
- Advanced landing algorithm and laser-based landing system proven for precise autonomous belly landings

**Swift Safe-To-Land:**
- Onboard machine-vision system operational for hazard detection and landing-area assessment
- Establishes practical experience in onboard compute, perception integration, and obstacle identification

**S2 Environmental Operations:**
- NASA MIZOPEX operations in Alaska and Greenland exposed systems to cold, wind, moisture, remote logistics, EMI concerns, and demanding airspace coordination
- MIZOPEX lessons including full-system testing before deployment, moisture and EMI control, onboard recording, spares, and explicit lost-communications behavior inform this proposal

## Notable Details

**Operational Authority & Safety:**
- Ship master retains authority over deck availability and recovery continuation
- Explicit safety gates govern progression from hold through approach, descent, and touchdown
- Manual takeover available under approved procedures
- Defined behavioral response for failed gates (hold, wave-off) and guidance loss during descent (go-around)

**Vessel Integration Advantages:**
- **Reusable integration package** reduces one-off engineering across multiple NOAA vessels
- **No permanent ship modification** required; cooperative target is portable and removable
- **Scalable design** reduces training demands and operator burden across fleet

**Options for Capability Growth (separable):**
1. **Targetless Ship Recognition and Recovery** — Develop deck and ship recognition without cooperative target; fuse relative pose with base solution
2. **Coastline Map Matching and Ship Reacquisition** — Near-shore image matching for degraded-GPS scenarios; featureless open-ocean visual navigation excluded
3. **Non-GPS Deck Ranging** — Integrate deck-mounted time-of-flight ranging with aircraft receiver to provide independent relative-distance measurement
4. **S3 Transfer and Demonstration** — Validate architecture on higher-payload platform; deliver two S3 systems to NOAA

**Intellectual Property & Procurement Path:**
- BST retains ownership of preexisting S0, S3 airframes, SwiftCore/SwiftPilot/SwiftTab/SwiftStation software, payload interfaces, autonomy algorithms, system models, and manufacturing know-how
- Eligible for SBIR Phase III sole-source award under 15 U.S.C. § 638(r) using existing lineage (NAVAIR N251-016, STTR N6833525C0270, AF192-005)
- Alternative: NOAA Standing BAA open through 30 September 2026
- Award by mid-September allows FY26 ORF obligation before lapse; delivery into FY27 compliant with non-severable bona-fide-needs rule

**Budget Context:**
- NOAA FY2027 budget request includes $75 million for autonomous research vessel fleet initiation and $60 million for Class C vessel acquisition (Executive Order 14269 support)
- OMAO funded at approximately request level in House-reported FY2027 bill (H.R. 8845); uncrewed-aircraft complement remains unspecified, creating opportunity for documented organic aerial layer

**Rough Order of Magnitude (ROM):**
- Specific dollar values not disclosed in this white paper (noted as non-binding ROM for planning); detailed pricing deferred to formal RFP or task-order proposal
- Estimates exclude Government vessel operating costs and major permanent ship modifications
- **Base effort:** ~18 months from authorization
- **Option 4 (S3):** ~18 months after exercise

**Period of Performance:**
- Base: Approximately 18 months after receipt of order (ARO)
- Phases: Vessel baseline → Architecture/safety review → Surrogate preparation → S0-VTOL testing → Vessel readiness → At-sea demonstration
- May adjust for hardware, weather, range access, reviews, and vessel availability

**Government-Furnished Resources:**
- Vessel and deck access
- Available geometry, navigation, motion, and interface data
- Ship master and crew coordination
- Test windows, ports, and normal ship services
- Range or airspace access
- Payload and science-user participation
- Timely spectrum, safety, airworthiness, cybersecurity, environmental, and operational decisions

**Demonstration Scope (Base Effort):**
- One Government-vessel at-sea event demonstrating S0-VTOL ship-relative approach and recovery within approved envelope
- Deliverables include: embarkation preparation, crew training, test data and video, after-action reporting, operating and emergency procedures, safety and airworthiness support, configuration records, and fleet/S3 transition recommendations

---

**Document Substance Assessment:** This is a comprehensive, technically detailed capability proposal with well-structured tasking, clear operational concepts, realistic past-performance foundations, and explicit pathways for both immediate (S0) and growth (S3, optional capabilities) implementation. It directly addresses a specific NOAA capability gap (autonomous VTOL recovery from moving vessels) and provides detailed scope, technical approach, risk mitigation, and contractual/IP considerations suitable for formal procurement action.