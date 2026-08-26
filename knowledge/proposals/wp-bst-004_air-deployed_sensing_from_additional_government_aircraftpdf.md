# Alternative Air-Launched Platforms for UAS Sensing

## Document Metadata
- **Type:** White paper / capability proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations / Uncrewed Systems Operations Center
- **Program/Solicitation:** Potential SBIR Phase III (NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005); NOAA IDIQ 1305M226D0012; NOAA Broad Agency Announcement (open through 30 Sept 2026)
- **Date:** August 17, 2026
- **BST Products/Systems Referenced:** S0 (air-deployed UAS), SwiftCore, SwiftTab, SwiftPilot
- **Key Personnel:** Cory Dixon (last editor)

## Executive Summary

Black Swift Technologies proposes to integrate and flight-demonstrate the mature S0 air-deployed environmental observation system on one NOAA-selected alternative fixed-wing host aircraft (e.g., C-130-class) to preserve and extend NOAA's hurricane-observation capability beyond the aging WP-3D platform. The effort would adapt the proven S0 system—which has demonstrated tropical-cyclone boundary-layer sampling since 2023—to new host-aircraft configurations while maintaining existing observation missions, payloads, and data outputs. A separable option would extend integration to a rotary-wing platform.

## Technical Approach

**Core Integration Framework:**
- Preserve existing S0-AD observation mission, payload, command/telemetry, ground control, procedures, and data outputs
- Develop host-specific release interface, safe-separation evidence, RF installation, crew workflow, and approval packages
- Organize integration around critical interfaces: release architecture, canister/mass properties, release envelope, safe separation, command & telemetry, ground-station installation, crew workflow, data delivery, and contingency behavior

**Fixed-Wing Host (Base Effort):**
1. **Task 1 - Mission & Host Selection:** Define priority NOAA mission, users, candidate fixed-wing aircraft, integration authorities, launch concept, and success criteria. NOAA selects host based on mission relevance, release feasibility, engineering-data availability, RF compatibility, approval authority, and schedule.
2. **Task 2 - Integration Architecture:** Develop release, mechanical, electrical, RF, control, data, crew, and safety architecture specific to selected host. Define canister/adapter config, command-telemetry path, control station installation, antenna interface, launch/abort sequence, and safe-separation evidence plan.
3. **Task 3 - System Integration:** Fabricate host-interface hardware; configure S0, encapsulation, GCS, communications, antenna, embedded systems, and instrumentation. Complete dimensional inspection, mass-property verification, bench/functional testing, RF/EMC testing, and installation checkout.
4. **Task 4 - Safe-Separation & Flight-Test Readiness:** Develop safe-separation evidence using host aircraft engineering data, analysis, modeling, ground/surrogate releases, and instrumentation. Finalize normal/emergency procedures, training, flight cards, and operating limits. Conduct flight-test readiness review.
5. **Task 5 - Flight Demonstration:** Execute Government-approved releases and S0 flights from selected fixed-wing host within approved test envelope. Demonstrate installation, checkout, mission loading, release, safe separation, powered-flight transition, command/telemetry, observation collection, data delivery, and crew procedures.
6. **Task 6 - Transition Package:** Deliver configuration records, interface-control information, procedures, training materials, test evidence, data products, operating limitations, and recommendations for future host-aircraft planning.

**Rotary-Wing Option (Option 1):**
- Select Government rotary-wing host; establish mission, release concept, interfaces, and approval path
- Address rotor wash/recirculation, aircraft speed/attitude, separation from fuselage/empennage/rotor system
- Configure host-specific release interface, S0, GCS, communications, embedded systems, procedures, and instrumentation
- Progress through analysis, ground/representative testing, flight-test readiness, and representative demonstration within approved test envelope

## Products & Capabilities Described

### S0 (Air-Deployed UAS)
- **What it is:** Purpose-built, low-cost uncrewed aircraft designed for air deployment from WP-3D drop tube; features swiveling-wing architecture with integrated atmospheric sensor suite
- **Key specifications:**
  - Measures three-dimensional winds, pressure, temperature, humidity
  - Autonomous launch-to-mission behavior via SwiftCore flight-management architecture
  - Sensor-informed flight control
  - Endurance and transition reliability optimized for air-drop deployment
  - Recoverable via parachute descent to ocean surface
- **Demonstrated performance:** Successfully deployed from NOAA WP-3D into Tropical Storm Tammy (October 2023); completed 71-minute mission at ~100 feet above ocean in subsequent hurricane operations
- **Proposed use:** Extension to C-130-class or rotary-wing hosts while preserving existing measurement configuration and data outputs

### SwiftCore
- Flight-management architecture enabling autonomous launch-to-mission behavior and sensor-informed flight control

### SwiftTab
- Operator-display software providing mission configuration and operator monitoring (aircraft state, mission progress, link health, sensor status)

### Ground Control System (GCS)
- Command-and-telemetry control station
- Data collection, onboard recording, metadata, and ground-station outputs
- Can be installed rack unit or portable battery-powered configuration
- Interfaces with host-aircraft systems for time- and position-referenced S0 data products

## Use Cases & Applications

**Primary Mission:**
- Tropical-cyclone boundary-layer sampling where crewed aircraft cannot safely operate at sustained low altitude
- Targeted in situ measurements of wind, pressure, temperature, humidity, turbulence, and heat/moisture/momentum transfer in hurricane environments

**Supporting Role:**
- Complement to satellites, radar, buoys, vessels, shore stations, and crewed aircraft for broader observing enterprise
- Fill gaps in satellite/radar/buoy coverage where required access, altitude coverage, timing, or spatial resolution is inadequate

**Future Missions:**
- Extension to other NOAA-selected missions where existing S0-AD measurement configuration is suitable (not specified in document)

## Key Results / Historical Performance

**S0 Development & Operational Heritage (since 2018):**
- **2018:** NOAA awarded BST initial development contract
- **2022:** Safe-separation testing from NOAA WP-3D conducted at high- and low-dynamic-pressure test points using aircraft-mounted high-speed cameras; generated release-modeling and flight-clearance evidence
- **October 2023:** First operational deployment into Tropical Storm Tammy
  - 71-minute flight mission
  - Descended to ~100 feet above ocean
  - Reported observations from region unsafe for crewed host
- **Subsequent operations:** Expanded flight heritage in stronger storms; demonstrated sustained low-altitude sampling and long-range data return

**Matured Supporting Systems:**
- Ground station, UHF command-and-telemetry chain, antenna/cable-loss characterization
- AVAPS interference mitigation
- SwiftTab operator displays
- Crew normal and emergency procedures
- NOAA data-routing functions
- Host-aircraft information ingestion capability

## Notable Details

### C-130-Class Aircraft as Leading Candidate
- Aligns with NOAA's announced 2030 transition from WP-3D Orions to two C-130J aircraft
- Relevant to weather-reconnaissance operations
- May offer existing apertures, dropsonde-related infrastructure, cabin space, and antenna options reducing integration burden
- NOAA identified UAS launch-and-control capability as part of future C-130J capability requirements

### Integration Risk Reduction Strategy
- Reuses WP-3D release, communications, ground-control, procedure, and safe-separation experience
- Does **not** include fleet-wide certification, full release-envelope qualification, recurring production, or operational sustainment
- Delivers decision-quality transition package for future host-aircraft planning
- Remains valuable even if rotary-wing option not exercised

### Government Responsibilities
- Host selection based on mission need, access, integration authority, and schedule
- Aircraft, crew, maintenance, installation access, and committed test windows
- Engineering data (drawings, geometry, release-envelope, aerodynamic, pressure-boundary, antenna, RF, power, mission-system information)
- Spectrum, cybersecurity, environmental, airworthiness, and flight approvals
- Test airspace/range access
- Timely technical and program decisions

### Intellectual Property & Award Path
- BST deliverables incorporate pre-existing proprietary systems: SwiftCore, SwiftPilot, SwiftTab, GCS software, fleet-management software, simulation assets, autonomy functions, and manufacturing know-how
- BST holds SBIR data rights lineage enabling potential Phase III sole-source award under 15 U.S.C. § 638(r)
- Can leverage existing NOAA IDIQ vehicle (1305M226D0012) or NOAA Broad Agency Announcement (open through 30 Sept 2026)
- Mid-September award permits FY26 ORF fund obligation before lapse

### Scope & Schedule
- **Base effort:** 12 months ARO (Approval to Receive); assumes host selection by Month 2
- **Option 1:** 8 months after option exercise
- **Potential delays:** Delayed host selection, aircraft-access gaps, release-system complexity, spectrum coordination, safe-separation review, weather, range access, or flight approval delays

### Budget
- **Base effort ROM:** $0.70M (12 months; one fixed-wing host; four S0-AD articles; one host-interface kit; one GCS set; up to three approved releases)
- **Option 1 ROM:** $0.50M (8 months; one rotary-wing host; four S0-AD articles or equivalents; one interface kit; up to two approved releases)
- **Maximum potential value:** $1.20M (Base + Option 1)

### Hardware Deliverables
- **Base:** 3 flight/test S0-AD articles plus 1 attrition/spare; 1 installed/test fixed-wing release interface kit plus critical spares; 1 operational GCS set with radio, antenna-interface, cases, charging, and support equipment (Government title proposed)
- **Option 1:** 1 rotary-wing interface kit; 3 flight-ready S0-AD articles or equivalent replacements (Government title proposed for new articles)