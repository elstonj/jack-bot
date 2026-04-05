# Statement of Work (SOW) for Black Swift Technologies: Long-Range Fixed-Wing Evaluation & DoD Autopilot Enablement (BYL-LRFE)

## Document Metadata
- Type: Statement of Work (SOW)
- Client/Agency: ByLight (Bryan Sparling)
- Program/Solicitation: Mustang UAS development program
- Date: Created 2025-11-25, Modified 2025-12-05
- BST Products/Systems Referenced: SwiftCore (flight computer, autopilot, data logging/telemetry system)
- Key Personnel: Jack Elston (Black Swift Technologies), Maciej Stachura (last editor)

## Executive Summary
Black Swift Technologies will conduct a 9-week, two-effort program to develop and flight-test a long-range, fully electric fixed-wing UAS (Mustang G2) meeting DoD requirements: ≤55 lbs gross takeoff weight, 400–450 km range, and truck/government launcher compatibility. Effort 1 focuses on integrating SwiftCore into an existing Mustang Unit 3 for rapid baseline data collection; Effort 2 encompasses full G2 design, COTS procurement, assembly, and comprehensive flight testing with SwiftCore as the primary flight computer, culminating in handoff to ByLight for integration of government-provided autopilot (EchoMAV/Cube) systems.

## Technical Approach

### SwiftCore-Centric Design Loop
- **Real-time telemetry & logging**: High-rate onboard data collection (IMU, GPS, power, ESC telemetry) feeds aerodynamic and propulsion data directly into sizing and performance models
- **System identification**: Extract thrust-to-power ratios, trim states, and control effectiveness from flight logs
- **Data-driven iteration**: Use SwiftCore analytics and open NetCDF data export to rapidly validate aerodynamic coefficients and refine propulsion trades

### G2 Design Process
1. **Mission & constraints freeze**: Payload, range, endurance, and launch load requirements
2. **Power-to-weight optimization**: Electric propulsion trade studies—motor Kv, propeller diameter/pitch, ESC efficiency, battery energy density—to achieve target cruise power and climb margins
3. **Aerodynamic configuration selection**: Evaluate candidate wings (BST in-house, CU "Mistral," COTS 4–5 m options) using lift/drag estimation and Reynolds-scaled polars; aim for specified range with realistic battery mass fractions
4. **Structural integrity & launcher loads**: Quasi-static launch load analysis; safety factors for wing joiners, fuselage attachment, landing gear for rail/truck launch survivability
5. **COTS procurement**: Vendor down-select and quality verification of wings, tails, test fuselage; dimensional and structural checks (mass properties, stiffness, joiner fit, control-surface play)

### Flight Testing & Performance Validation
- **Truck launch** with SwiftCore integration and high-rate data logging
- **Staged flight cards**: Manual launch, stabilization, speed sweeps, climb/descend to build aerodynamic data sets
- **Incremental weight testing**: Sequential flights at 42, 48, 52, 55 lbs GTOW; confirm CG and control response at each step
- **Power-vs-speed testing**: Controlled speed points recording voltage, current, ESC temperature, GPS airspeed; compute Wh/km and extrapolate range
- **GOTS integration prep**: Design power buses/harnesses allowing ByLight to later integrate EchoMAV FC, payload, gimbal, cameras; use SwiftCore's open data interface (NetCDF) for future Cube/ArduPilot parameter translation
- **Government launcher integration**: Adapter/rail-mount design, CG alignment validation, acceleration characterization via SwiftCore IMU/GPS; define abort thresholds and environmental limits
- **Reliability criteria**: Minimum 3 consecutive successful flights meeting stability and endurance metrics

## Products & Capabilities Described

### SwiftCore Flight Computer
- **What it is**: Integrated flight computer and autopilot system with real-time telemetry, high-rate onboard logging (IMU, GPS, power, ESC telemetry), and open data export capabilities (NetCDF format)
- **Role in this project**: Primary flight computer for Mustang Unit 3 (Effort 1) and Mustang G2 prototype (Effort 2); all system identification, aerodynamic data collection, propulsion performance validation, and launch dynamics characterization will use SwiftCore
- **Key capabilities leveraged**:
  - Real-time system identification tools to feed aerodynamic and power data into sizing models
  - Onboard power logging and analysis scripts for Wh/km computation and range modeling
  - High-rate IMU and GPS for launch acceleration and control-response characterization
  - Open data interface enabling future handoff to government autopilots (EchoMAV/Cube)

### Mustang Unit 3 (Existing)
- **What it is**: Current fixed-wing platform
- **Use**: Integration target for Effort 1; rapid baseline flight data collection using SwiftCore to validate truck launch procedures and gather initial aerodynamic/propulsion metrics
- **Deliverables from Unit 3**: Ground and air video, flight logs, short technical summary

### Mustang G2 (Proposed Design)
- **Requirements**: 
  - Full electric propulsion
  - ≤55 lbs gross takeoff weight
  - 400–450 km range
  - Truck or government rail launcher compatible
- **Design outputs**: Aerodynamic coefficients, propulsion selections, predicted range vs. payload curves, CAD/interface drawings
- **Fuselage decision**: Evaluate reuse of Unit 4 fuselage or design new fuselage optimized for battery volume, wing joiner loads, cooling airflow
- **Candidate wing options**: BST in-house design, CU "Mistral," COTS 4–5 m commercial airfoils

## Use Cases & Applications

### Primary Use Case: DoD Long-Range ISR
- Full-electric UAS with 400–450 km range suitable for extended surveillance missions
- Truck-transportable and government-launcher compatible (meets DoD logistics and deployment constraints)
- ≤55 lbs design aims for simplified logistics and field operations

### Launch Scenarios
- **Truck launch**: Rapid deployment from mobile platform
- **Government-provided launcher**: Rail or catapult system integration; characterized for acceleration, exit speed, and abort thresholds

### Payload Accommodation
- Future integration of government-provided components: EchoMAV FC, payload sensors (gimbal, cameras), without compromising SwiftCore data integrity
- Architecture allows SwiftCore to remain as primary data logger while GOTS autopilots assume control post-delivery

## Key Results / Deliverables

### Effort 1 (Target: 10/17/25)
- SwiftCore integration into Mustang Unit 3
- Truck launch execution
- Ground and airborne video
- Flight logs and short technical summary
- **Goal**: Demonstrate Unit 3 flying reliably with SwiftCore

### Effort 2 (Target: 12/05/25)

**Milestone 1 – Design & Procurement (11/01/25)**
- G2 conceptual design meeting ≤55 lbs GTOW, 400–450 km range requirements
- Aerodynamic configuration, propulsion sizing, structural load analysis finalized
- COTS wings, tail, test fuselage sourced and ordered
- Design review briefing, CAD drawings, SwiftCore integration plan
- Design & Procurement Report

**Milestone 2 – Assembly & Ground Integration (11/22/25)**
- Prototype airframe assembly with SwiftCore installed
- Bench and ground power tests completed
- Launcher fit-checks and dry runs performed
- CG, battery placement, sensor alignment verified
- Integration and Ground Test Report

**Milestone 3 – Flight Testing & Performance Validation (12/05/25)**
- ≥3 successful flights demonstrating launch reliability and stable flight at incremental weights
- Power-vs-speed data and battery draw metrics
- Preliminary range and performance model
- Flight Test Report with logs and videos

**Milestone 4 – Final Design Package (12/05/25)**
- Final design documents for Mustang G2
- Production recommendations
- Comprehensive data package (SwiftCore logs, plots, models, videos)
- Final Technical Memo and Close-out Brief
- Hardware and documentation transfer to ByLight for Cube/ArduPilot adaptation

## Notable Details

### Budget & Payment
- **Total Fixed Price**: $450,000 (9-week effort)
- **Materials, supplies, travel**: Billed separately at actual cost
- **Payment schedule**:
  - Up-front: $100,000 (award + long-lead procurement)
  - Milestone 1: $100,000 (design & procurement)
  - Milestone 2: $100,000 (assembly & integration)
  - Milestone 3: $100,000 (flight testing & performance)
  - Milestone 4: $50,000 (final package & close-out)
- **Terms**: Net 15 days from invoice per milestone completion

### Intellectual Property
- **All deliverables, designs, data, and materials become non-proprietary property of ByLight upon completion and final payment**
- BST retains no proprietary claims; ByLight receives full and unlimited rights to use, reproduce, modify, or distribute work product
- This enables government purchasability of IP

### Regulatory & Safety
- All flight operations per FAA Part 107 (or applicable waiver/COA)
- Airspace coordination, pilot certification, and safety requirements compliance required

### Out-of-Scope Clarifications
- Tool-less field assembly, shipping fixtures, or simplified packaging for non-UAS experts
- Physical installation or tuning of EchoMAV/Cube autopilots (to be performed by ByLight post-delivery)

### Schedule Risk Mitigation
- Document explicitly notes schedule is based on current labor availability and component delivery timelines
- Personnel availability and long-lead material delivery are critical path items
- ByLight will be promptly coordinated with for schedule adjustments if needed
- Milestone buffers included (e.g., 2-week buffer in Milestone 1 for vendor lead-times, ~3 weeks in Milestone 2 for receipts/assembly/rework)

### Data Handoff Strategy
- SwiftCore's open NetCDF export enables ByLight to translate flight data into Cube or ArduPilot parameter sets during their later autopilot integration phase
- Full separation of SwiftCore power/data systems from GOTS payload power systems via isolated harnesses and buses
- SwiftCore remains primary data logger even after GOTS autopilot installation