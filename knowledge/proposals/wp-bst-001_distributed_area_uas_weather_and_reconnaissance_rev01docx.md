# Distributed Extreme Weather Reconnaissance and Sensing

## Document Metadata
- **Type:** White paper / Capability proposal
- **Client/Agency:** NOAA Office of Marine and Aviation Operations / Uncrewed Systems Operations Center
- **Program/Solicitation:** NOAA IDIQ (1305M226D0012); potential SBIR Phase III pathway (NAVAIR N251-016, STTR N6833525C0270, Air Force AF192-005); NOAA Standing BAA (open through 30 September 2026)
- **Date:** August 17, 2026
- **BST Products/Systems Referenced:** S0-VTOL, S0, S1, S2, SwiftCore™, SwiftPilot™, SwiftTab™, SwiftStation™
- **Key Personnel:** Cory Dixon (last editor)

---

## Executive Summary

Black Swift Technologies proposes a deployable, distributed S0-VTOL fleet for rapid multi-aircraft incident-area reconnaissance and weather profiling to support NOAA emergency response. The base effort integrates lightweight EO/IR payload on S0-VTOL aircraft, develops centralized dynamic area-search autonomy for one operator controlling multiple aircraft, establishes ground-control capability, pursues FAA authorization, and demonstrates the system across five delivered aircraft. This approach leverages BST's existing NOAA S0 operating heritage and provides a reusable local aerial capability that complements crewed assets while shortening collection timelines and reducing dependence on limited manned aircraft.

---

## Technical Approach

### Overall Architecture
- **Multi-aircraft system:** Centralized mission management with dynamic area-search autonomy allowing a single operator to divide an approved survey area among multiple S0-VTOL aircraft
- **Mission workflow:** Operator defines collection area and objectives; software creates optimized mission plan and assigns sectors; aircraft execute autonomously while remaining geofenced and monitored; mission manager reallocates unfinished sectors if an aircraft becomes unavailable
- **Data strategy:** High-resolution EO/IR imagery retained onboard with full metadata (position, time, attitude, aircraft state) for post-flight offload; selected preview imagery and thumbnails downlinked when link and C2 priorities permit
- **Operator authority:** Centralized through SwiftTab operator interface; operator retains launch authority, mission approval, ability to designate points of interest, and access to hold/return/alternate-recovery functions
- **Flight safety:** SwiftCore remains responsible for flight-critical control; geofences, altitude limits, energy reserves, weather limits, lost-link behavior, and approved contingency responses (hold, return, alternate landing, safe termination) protect operations

### Key Technical Capabilities
- **Autonomous flight execution:** SwiftPilot™ supports launch-to-recovery autonomy with aircraft health monitoring, payload interfaces, and automated fault responses
- **Centralized mission management:** Allocates collection sectors based on aircraft availability, required image overlap, route geometry, energy reserve, and recovery constraints; monitors progress and reallocates work; supports dynamic retasking
- **Communications architecture:** To be defined in System Concept; assessment includes simultaneous-link capacity, channel/spectrum needs, central ground-system failure modes, hot-spare/failover arrangements
- **Payload integration:** Mechanical fit, mass properties, power management, thermal management, vibration isolation, EMC compliance; image timing and georeferencing protocols; onboard high-resolution storage; post-flight export

### Cooperative-Autonomy Option (Option 2)
- Decentralized coordination layer with inter-aircraft status exchange
- Cooperative task allocation and replanning to reduce ground-station dependence
- Preserves operator authority, geofencing, and independent flight-safety functions

---

## Products & Capabilities Described

### S0-VTOL Aircraft
- **Specifications:**
  - Mass: 2.6 kg (5.73 lb)
  - Endurance: Up to 60 minutes
  - Design ceiling: Up to 15,000 ft AGL (subject to configuration, site, airspace, weather, reserve)
  - Configuration: VTOL fixed-wing hybrid (vertical launch, fixed-wing flight)
- **Use in this proposal:** Primary platform for distributed incident-area reconnaissance and fire-weather profiling
- **Atmospheric measurement suite (meteorological configuration):**
  - Measures: Pressure, temperature, humidity, three-dimensional winds
  - Relative-wind specifications: 0.38 m/s resolution, ±0.48 m/s accuracy
- **Heritage:** Air-deployed from NOAA WP-3D in tropical cyclones; concurrent operation of two air-deployed S0 aircraft demonstrated in testing and operational missions

### SwiftCore™ Flight-Management System
- Flight-critical control and contingency behavior
- Integrates onboard autonomy, aircraft health monitoring, payload interfaces
- U.S.-designed and U.S.-manufactured
- Provides foundation for multi-aircraft operations

### SwiftPilot™
- Autonomous flight from launch through recovery
- Aircraft health monitoring
- Payload interface management
- Automated fault responses

### SwiftTab™ Operator Interface
- Map-based mission planning
- Georeferenced data visualization
- In-flight mission changes
- Operator annunciation and alert management
- Display of status, health, map, collection progress

### SwiftStation™
- Portable command, control, and telemetry link
- Ground-system element
- Primary and spare configurations for mission continuity

### EO/IR Payload (to be selected)
- Lightweight integration (not yet downselected in this proposal)
- Records high-resolution imagery with synchronized metadata
- Supports preview-image downlink and full-resolution onboard storage
- Integration addresses mechanical fit, power, thermal management, vibration, EMC, image timing, georeferencing, onboard storage, and endurance impact
- Payload loss does not remove aircraft C2; C2 retains priority over imagery

### Multi-Aircraft Mission-Management Software
- Centralized allocation function
- Sector optimization and reassignment logic
- Progress monitoring and dynamic retasking
- Operator workload management

---

## Use Cases & Applications

### Emergency Response Imagery (Base Use Case)
- Distributed collection across smaller priority areas during wildfires, hurricanes, severe storms, and other hazardous events
- Rapid local deployment complements NOAA's existing crewed Emergency Response Imagery workflow
- Addresses situations where mobilizing/retasking crewed aircraft is not the most responsive approach
- Supports damage assessment, recovery planning, and public dissemination

### Fire-Weather Profiling (Option 1 — 10-system deployment)
- Controlled vertical profile missions (climbs, descents, level holds, repeated segments)
- Measures pressure, temperature, humidity, three-dimensional winds at selected altitude levels
- Complements surface stations and radiosondes by providing vertical structure information
- Supports National Weather Service Incident Meteorologist decision support
- Resolves inversions, moisture recovery, low-level winds, wind shear, and mixing
- Reusable platform (unlike expended radiosondes) can repeat observations as conditions change
- Post-flight workflow produces agreed exchange files for NWS/OAR model-data users

### Incident Airspace Operations
- Operates under demonstration waiver or FAA authorization for one-operator, multi-aircraft missions
- Designed to integrate into constrained incident airspace without interrupting firefighting or response operations
- Authorized integration path includes airspace, safety, and regulatory coordination

---

## Key Results / Existing Experience

### Relevant Operating Heritage
- **S0 tropical-cyclone deployment:** Air-deployed from NOAA WP-3D with established launch, communications, ground-control, and data-handling procedures
- **Multi-aircraft operation:** Concurrent operation of two air-deployed S0 aircraft demonstrated in both clear-air testing and operational missions

### Aerial Mapping Heritage (S1 Platform)
- CH2MHill fly-off results (historical S1 data, not representative of S0-VTOL performance):
  - 693 images collected over test area
  - 99.7% image utilization in processing
  - 7.1 cm mean reprojection error
  - Average 190.11 image connections per pair
  - Demonstrates data-centric flight planning, image overlap management, and completeness-checking principles
- Demonstrates importance of accurate flight tracking, consistent image overlap, rapid image cadence, and reliable geotagging

### Wildfire Remote-Sensing and Payload Integration
- **NOAA Nighttime Fire Observations eXperiment (NFOe):** S2 platform carried multisensor payload (visible, thermal, infrared) for wildfire mapping and fire-radiative-power characterization
- **Prior integrations:** Multispectral cameras, atmospheric sensors, trace-gas instruments, particulate sensors, radiometers across wildfire, volcanic, Arctic, and Earth-observation missions
- **Relevant experience:** Sensor integration, timing, metadata, onboard recording, scientific data handling; reduces integration risk

### Machine Vision and Autonomous Landing (NASA Swift Safe-to-Land Program)
- Onboard machine vision with small-form-factor computing
- Semantic segmentation for hazard identification
- Autonomous contingency landing support
- Demonstrates integration of onboard imaging, computing, flight controls, and safety behavior (though automated fire classification is not in base scope)

---

## Proposed Scope & Tasks

### Base Effort (15 months)
Produces five accepted EO/IR-capable S0-VTOL systems with primary and spare ground equipment, trained operators, and documented procedures.

**Task 1 — System Concept**
- Define mission, users, operating scenarios, imagery products, S0-VTOL/payload configuration, system boundary, data/operator interfaces, environmental envelope, airspace/safety construct
- Measurable performance targets for imagery, geolocation, coverage, latency, communications, workload, containment, recovery, data delivery
- Multi-aircraft C2 capacity, spectrum, communications, central ground-system failure-modes assessment
- Redundancy and sparing concept
- Preview-imagery and full-resolution offload workflow definition
- Lightweight EO/IR payload downselection
- Concept of operations, safety case, operating procedures
- System Concept Review before detailed integration
- Support FAA waiver or authorization pursuit

**Task 2 — EO/IR Payload Integration**
- Mechanical fit, mass properties, power, thermal management, vibration, EMC
- Image timing, georeferencing, onboard high-resolution storage
- Selected preview-image downlink capability
- Post-flight data export
- Payload health monitoring
- Endurance and handling impact assessment
- Bench, ground, and progressive single-aircraft flight verification before multi-aircraft testing

**Task 3 — Multi-Aircraft Dynamic Area-Search Autonomy**
- Centralized mission-allocation functions for one operator
- Area definition, aircraft allocation, progress monitoring, sector reassignment
- Point-of-interest designation and additional collection capability
- Integration with SwiftTab ground system
- Status, health, map, collection-progress displays

**Task 4 — Integrated Verification and Demonstration**
- Single-aircraft payload checkout through multi-aircraft survey missions
- Verify imagery quality and geolocation, collection overlap, assigned-area completion, sector reassignment, operator workload, airspace containment
- Communications and preview-image transfer verification
- Primary-to-spare ground-system recovery testing
- Launch, recovery, turnaround, degraded-mode behavior verification
- Support FAA/Government review and authorization process
- One Government-observed multi-aircraft distributed reconnaissance demonstration
- Synchronized aircraft, payload, telemetry, imagery, operator-action, and video records

**Task 5 — Fleet Delivery, Training, and Transition**
- Acceptance checkout following demonstration and closure of delivery-critical discrepancies
- Deliver multiple EO/IR-capable S0-VTOL aircraft, payloads, primary/spare ground-control/mission-management equipment, support equipment
- Released software configuration
- Operating and emergency procedures
- Operator and maintainer training
- Configuration records and test results
- Transition recommendations
- Documentation of demonstrated configuration limitations

### Option 1 — Fire-Weather Profiling Fleet and Workflow Validation (12 months after base)
- Configure two initial S0-VTOL fire-weather validation systems
- Establish controlled sensor and processing configuration
- Document calibration, timing, quality metadata, maintenance
- Compare profiles against accepted reference observations
- Characterize bias, uncertainty, response, repeatability, delivery latency
- Produce agreed exchange file
- Following acceptance review, produce remaining eight systems (10 total)
- Operationally representative fire-weather demonstration
- Close delivery-critical discrepancies
- Train designated users
- Deliver all systems with support equipment, transition documentation, field-support recommendations

### Option 2 — Cooperative Autonomy and Demonstration (12 months after base stabilization)
- Advance centralized fleet management to cooperative-autonomy configuration
- Implement communications and algorithms for cooperative task allocation and