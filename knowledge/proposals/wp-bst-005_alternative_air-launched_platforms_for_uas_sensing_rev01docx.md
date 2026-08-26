# Alternative Air-Launched Platforms for UAS Sensing

## Document Metadata
- **Type:** White paper / capability proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations / Uncrewed Systems Operations Center
- **Program/Solicitation:** SBIR Phase III lineage (NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005); NOAA IDIQ 1305M226D0012; NOAA BAA (open through 30 September 2026)
- **Date:** August 17, 2026
- **BST Products/Systems Referenced:** S0 (S0-AD air-deployed UAS), SwiftCore, SwiftPilot™, SwiftTab™, ground-control station (GCS)
- **Key Personnel:** Cory Dixon (last editor)

## Executive Summary
BST proposes to adapt and flight-demonstrate the mature S0 air-deployed UAS on one NOAA-selected alternative fixed-wing host aircraft (with an optional rotary-wing variant) to preserve hurricane-observation capability beyond the finite WP-3D fleet and reduce risk of transition to NOAA's planned C-130J aircraft. The effort preserves existing S0-AD payload, command/telemetry, procedures, and data outputs while developing host-specific release interfaces, safe-separation evidence, RF installation, crew workflows, and approval packages. Base effort is ~12 months; option adds ~8 months.

## Technical Approach

### Host Integration Framework
BST would organize the integration around seven key control interfaces:
1. **Release architecture** — adapted to host aperture (chute, sleeve, door, ramp, tube, or other mechanism)
2. **Canister and mass properties** — host-specific adapter/installation rather than direct WP-3D transfer
3. **Release envelope** — safe separation analysis using applicable WP-3D evidence, configuration analysis, modeling, ground/surrogate releases, and instrumentation
4. **Command and telemetry** — keeping flight-critical systems separate from host mission dependencies; RF survey, spectrum coordination, filtering, EMC testing
5. **Ground-station installation** — installed rack or portable battery-powered configuration based on host
6. **Crew workflow** — normal and contingency procedures (launch abort, unreleased articles, loss of command link, failure to establish powered flight, host deconfliction)
7. **Data delivery** — verification of existing S0-AD observation data continuity to ground station

### Safe Separation Methodology
- Use WP-3D-derived evidence, configuration analysis, and modeling
- Conduct ground releases, surrogate testing, and instrumented test methods
- Address host aerodynamic environment, parachute-stabilization sequence, wing deployment, transition to powered flight
- Support flight-test decision through approved authority

### Communications Architecture
- SwiftTab operator displays for mission configuration and monitoring
- Existing S0-AD data collection, onboard recording, metadata baseline preserved
- RF interface via existing aircraft antenna (if suitable) or temporary/approved installation
- Spectrum coordination and cybersecurity per Government requirements

### Progressive Test Approach
- Dimensional inspection and mass-property verification
- Bench testing, functional verification, RF and EMC testing
- Installation checkout and release-mechanism testing
- Flight-test readiness review before commencing releases
- Approved number of releases within Government-approved test envelope

## Products & Capabilities Described

### S0 (S0-AD Air-Deployed UAS)
- **What it is:** Purpose-built, low-cost, air-deployed uncrewed aircraft with swiveling-wing architecture; measures three-dimensional winds, pressure, temperature, humidity, and mission-dependent parameters
- **Development heritage:** Initial NOAA contract 2018; operational deployment from NOAA WP-3D since 2023
- **Measurement suite:** 3D wind vectors, pressure, temperature, humidity; configurations support sea-surface and altitude-related measurements
- **Flight control:** SwiftCore flight-management architecture supporting autonomous launch-to-mission behavior and sensor-informed flight control
- **Endurance/Performance:** 71-minute mission demonstrated in Tropical Storm Tammy (October 2023); capable of sustained low-altitude sampling (~100 feet AGL) in hurricane boundary layer
- **Data return:** Long-range command and telemetry; autonomous sampling profiles; integration with NOAA data-routing functions
- **Proposed use:** Deploy from alternative fixed-wing host (C-130-class candidate) to maintain hurricane boundary-layer observation capability beyond WP-3D

### SwiftCore
- Flight-management architecture enabling autonomous launch-to-mission behavior and sensor-informed flight control
- Integrated with NOAA avionics simulation environment during early development

### SwiftTab™
- Operator display and mission-control software
- Provides mission configuration, aircraft state monitoring, mission progress, link health, sensor status
- Retains existing operator-display baseline

### SwiftPilot™
- Referenced as existing capability (no additional details in document)

### Ground Control Station (GCS)
- Can be installed rack unit or portable battery-powered configuration
- Ingests host-aircraft information for time- and position-referenced data products
- RF and antenna characterization, cable-loss accounting
- AVAPS interference mitigation
- Data-routing functions to NOAA mission team

## Use Cases & Applications

### Primary Mission
**Tropical-cyclone boundary-layer sampling:**
- Collect sustained, high-frequency observations from hurricane boundary layer (too hazardous for crewed aircraft to sample continuously at very low altitude)
- Measure kinematics, thermodynamics, wind, pressure, temperature, humidity, turbulence, heat/moisture/momentum transfer
- Complement satellite, radar, buoy, vessel, shore-station, and crewed-aircraft observations with targeted in situ measurements

### Deployment Context (WP-3D heritage)
- October 2023: Tropical Storm Tammy deployment — 71-minute mission at ~100 feet AGL; accessed region unsafe for crewed host
- Subsequent hurricane operations in stronger storms demonstrated sustained low-altitude sampling and long-range data return
- NOAA Atlantic Oceanographic and Meteorological Laboratory operational lead

### Future Host Context
- C-130J aircraft planned to enter NOAA fleet in 2030 to replace long-serving WP-3D Orions
- Same host-integration approach may support other NOAA-selected missions using existing S0-AD measurement configuration
- Weather-reconnaissance operations on C-130-class platform

## Key Results

### Prior Performance (WP-3D Integration, 2018–2026)
**October 2023 Tropical Storm Tammy Mission:**
- 71-minute autonomous flight duration
- Low-altitude sampling (~100 feet AGL)
- Successful data collection and return from hurricane boundary layer
- Wind and rain-field mapping demonstrated

**Safe-Separation Testing (2022):**
- High- and low-dynamic-pressure test points from NOAA WP-3D
- High-speed camera documentation (belly and wing views)
- Provided release-modeling, instrumentation, test-planning, and flight-clearance experience

**System Maturity:**
- Operational airborne system with established ground station, UHF command-and-telemetry chain, antenna characterization, interference mitigation, operator displays, crew procedures, and NOAA data-routing functions
- Purpose-built design overcame tight constraints: size, weight, release packaging, endurance, transition reliability
- Simulation validation using high-fidelity hurricane fields and atmospheric-system expertise from NCAR

## Notable Details

### Competitive/Strategic Position
- Preserves NOAA's proven S0-AD capability while de-risking transition to C-130J
- Reduces technical and schedule risk of moving beyond WP-3D dependence
- Establishes documented integration foundation for future host-aircraft decisions
- Direct alignment with NOAA's announced fleet transition plan (2030 C-130J entry)

### SBIR/Data Rights Lineage
- BST holds SBIR data rights on S0 program enabling Phase III sole-source award under 15 U.S.C. § 638(r)
- Associated SBIR/STTR contracts: NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005
- Existing NOAA IDIQ vehicle: 1305M226D0012
- Alternative pathway: NOAA BAA (open through 30 September 2026)

### Scope Boundaries
- Base effort delivers one alternative fixed-wing demonstration only; does not include fleet-wide certification, full release-envelope qualification, recurring production, or operational sustainment
- Option (Task 7) adds rotary-wing host integration and demonstration
- ROM estimate reflects bounded scope assumptions; detailed pricing requires formal RFP/task-order request

### Government-Furnished Resources Required
- Aircraft, crew, maintenance, installation access, committed test windows
- Available drawings and geometry data (release envelope, aerodynamics, pressure boundary, antenna, RF, power, mission-system interfaces)
- Spectrum, cybersecurity, environmental, airworthiness, safe-separation, and flight approvals
- Approved test airspace or range access
- Timely technical, host-selection, test, and program decisions

### Schedule and Funding Pathway
- Base period: ~12 months from authorization, assumes host selection by Month 2
- Option 1: ~8 months post-exercise
- Obligation path: FY26 ORF funds (deadline mid-September 2026); performance runs into FY27
- Complies with bona fide needs rule as non-severable deliverable of season-readiness capability

### Intellectual Property
- Deliverables incorporate BST pre-existing proprietary systems: airframes, SwiftCore, SwiftPilot™, SwiftTab™, GCS software, fleet-management software, simulation assets, operator-interface software, alert-management logic, fleet-orchestration methods, atmospheric wind-estimation methods, autonomy functions
- Data rights and IP assertions to be defined in resulting agreement