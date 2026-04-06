# BST Mustang - Long-Range Fixed-Wing Evaluation (BYL-LRFE)

## Document Metadata
- Type: Purchase Order with Statement of Work (SOW)
- Client/Agency: By Light Professional IT Services LLC (DISA Global Operations)
- Program/Solicitation: Mustang Program; Project Number 15423.00.0001.000001
- Date: 10/8/2025
- BST Products/Systems Referenced: SwiftCore (flight computer), Mustang (fixed-wing UAS platform)
- Key Personnel: Jack Elston (Black Swift Technologies), Josh Whetstine (By Light POC), Bryan Sparling (By Light SVP Strategic Programs), Beck Cotter (BST contact)

## Executive Summary
Black Swift Technologies will conduct a nine-week engineering effort to design, build, and flight-test a next-generation Mustang UAS (G2) meeting specified requirements: ≤55 lb gross takeoff weight, 400–450 km range, full-electric propulsion, and integration with government-provided launcher and GOTS autopilot systems. The work leverages SwiftCore flight computer for rapid data-driven design iteration and flight validation.

## Technical Approach

### Phase Structure (Effort 1 + Effort 2)

**Effort 1: Rapid Initial Validation (10/6–10/17, 2 weeks)**
- Integrate SwiftCore into existing Mustang Unit 3
- Execute truck launch and flight operations
- Collect ground/air video and flight telemetry
- Analyze data to validate airframe and propulsion baseline

**Effort 2: G2 Design, Build, and Flight Test (10/6–12/5, 9 weeks)**

1. **G2 Conceptual Design (Weeks 3–4, MS1)**
   - Mission & constraints freeze: payload, range, endurance, launch method
   - SwiftCore-enabled rapid design loop: real-time telemetry, logging, and system-identification tools feed aerodynamic and power data directly into sizing models
   - Power-to-weight optimization: trade studies on motor Kv, propeller diameter/pitch, ESC efficiency, battery energy density to achieve target cruise power and climb margins
   - Aerodynamic configuration selection: evaluate BST in-house wings, CU "Mistral" wing, and COTS 4–5 m options using lift/drag estimation and Reynolds-scaled polars
   - Structural analysis: quasi-static launch load calculations; safety factors for wing joiners, fuselage attachment, landing gear
   - Deliver design package with aerodynamic coefficients, propulsion selections, and predicted range vs. payload curves

2. **COTS Procurement (Weeks 3–4, MS1)**
   - Vendor down-select for wings, tails, test fuselage meeting geometric and structural requirements
   - Dimensional and structural verification (mass properties, stiffness, joiner fit, control-surface play)
   - CAD/drawings for wing-to-fuselage and tail interfaces

3. **Assembly & Ground Integration (Weeks 5–7, MS2)**
   - Install SwiftCore flight computer, avionics, wiring, sensors, telemetry
   - Bench and ground power testing
   - Launcher fit-checks and dry runs
   - CG verification, battery placement, sensor alignment
   - Thermal validation using onboard sensors

4. **Flight Testing & Performance Validation (Weeks 8–9, MS3–4)**
   - Staged flight cards: manual launch stabilization, speed sweeps, climb/descend
   - Incremental weight loading: 42, 48, 52, 55 lb GTOW
   - Power-vs-speed testing: controlled speed points recording voltage, current, ESC temperature, airspeed
   - SwiftCore data logging: extract thrust-to-power ratios, trim states, control effectiveness
   - Range modeling: SwiftCore power logging and analysis scripts to compute Wh/km and extrapolate endurance under mission profiles
   - Minimum 3 consecutive successful flights meeting stability and endurance metrics

5. **GOTS Integration**
   - Mechanical/electrical accommodation for EchoMAV FC, payload, gimbal, cameras
   - Design power buses and harnesses isolating SwiftCore from GOTS payload power systems
   - Data compatibility: SwiftCore NetCDF export interface for By Light to translate into Cube/ArduPilot parameters
   - Environmental verification: structural mounting, vibration isolation, EMI cleanliness
   - Note: Physical EchoMAV/Cube installation and tuning by By Light (out of scope)

6. **Government Launcher Integration (MS4)**
   - Launcher interface design: adapter or rail-mount solution for GOV launcher
   - Launch envelope characterization: acceleration, exit speed via SwiftCore IMU/GPS
   - Safety limits definition: abort thresholds, environmental limits (wind, temperature, battery state-of-charge)
   - Minimum three successful GOV-launcher flight sequences with video and data logs

## Products & Capabilities Described

### SwiftCore Flight Computer
- **What it is:** BST's flight computer and data acquisition system with real-time telemetry, high-rate logging (IMU, GPS, power, ESC telemetry), and open data interface (NetCDF export)
- **Proposed use:** Primary flight computer for Mustang G2; enables rapid iterative design via system-identification tools feeding aerodynamic and power data into sizing models; high-fidelity onboard logging for performance validation and thermal monitoring
- **Key capabilities:**
  - Real-time telemetry and onboard logging at high sample rates
  - System-identification tools for aerodynamic coefficient extraction
  - Power logging for range/endurance modeling
  - Thermal sensor integration for subsystem monitoring
  - NetCDF data export for downstream autopilot adaptation
  - Vibration/launch dynamics characterization

### Mustang Platform
- **What it is:** Fixed-wing tactical UAS, existing Units 3 and 4; G2 variant is redesigned full-electric evolution
- **Effort 1 use:** Unit 3 retrofitted with SwiftCore for rapid baseline validation
- **Effort 2 use:** G2 design based on COTS airframe components (wings, tail, fuselage) optimized for 55 lb GTOW and 400–450 km range; truck-launch compatible
- **Specifications (G2 targets):**
  - GTOW: ≤55 lb (minimum required for 450 km range)
  - Range: 400–450 km (full electric)
  - Launch method: truck launch + GOV government launcher
  - Endurance: modeled via SwiftCore power telemetry
  - Propulsion: electric (motor, ESC, propeller trade studies; battery energy density TBD)
  - Payload: TBD per mission requirements; design loop includes payload accommodation

## Use Cases & Applications

1. **Long-range tactical reconnaissance:** 450 km range enables extended-range ISR missions
2. **Rapid prototyping & design validation:** SwiftCore-enabled iterative loop compresses development cycle (9 weeks from concept to flight-proven prototype)
3. **Government platform adaptation:** Designed for integration with GOTS EchoMAV/Cube autopilots and government-supplied launcher for future By Light operational deployment
4. **Electric propulsion validation:** Demonstrates full-electric long-range platform; battery draw modeling provides confidence bounds for mission planning

## Key Results / Deliverables

**Effort 1 (by 10/17/25):**
- Ground and air video of Unit 3 flying reliably with SwiftCore
- Flight data logs and technical summary
- Baseline performance validation

**Effort 2 (by 12/5/25):**
- **G2 Mustang prototype:** ≤55 lb GTOW, 400–450 km range, full-electric, truck-launch and GOV-launcher compatible
- **Design package:** aerodynamic coefficients, propulsion selections, structural analysis, range vs. payload curves
- **Flight test data:** minimum 3 successful flights; power-vs-speed data; thermal logs; launcher integration validation
- **Range model:** validated Wh/km performance curves and endurance predictions under mission profiles
- **System identification data:** control responses, trim states, aerodynamic parameters extracted from SwiftCore telemetry
- **Integration documentation:** CAD/interface drawings for GOTS component accommodation; power bus schematics; thermal validation report
- **Video and data package:** flight test footage, consolidated SwiftCore logs, analysis plots
- **Government-purchasable IP:** all deliverables and designs become non-proprietary property of By Light upon completion

## Notable Details

1. **IP Terms:** Black Swift explicitly waives all proprietary claims; all deliverables and design data become sole property of client upon payment, enabling By Light to adapt for government purchase and operational deployment.

2. **Rapid Iterative Design Loop:** SwiftCore's real-time telemetry and system-identification tools are central to the technical approach, enabling BST to compress traditional design-build-test cycles by feeding live flight data directly into aerodynamic models and propulsion sizing.

3. **Data-Driven Battery Modeling:** Flight tests will include controlled speed sweeps with full power logging to establish Wh/km consumption and extrapolate reliable 400–450 km range with confidence margins and recommended cruise speeds.

4. **Modular Autopilot Accommodation:** Design isolates SwiftCore from GOTS EchoMAV/Cube payloads via power bus separation and uses NetCDF export to enable By Light's later parameter translation, decoupling BST's role from downstream autopilot tuning.

5. **Launcher Flexibility:** Effort 2 includes both truck-launch (Effort 1 baseline) and government launcher integration, with IMU/GPS characterization of launch dynamics and abort threshold definition.

6. **Schedule Risk Mitigation:** Effort 1 (immediate 2-week Unit 3 validation) funded at $100K up-front to validate approach before committing full Effort 2 resources; remaining $350K contingent on milestone completion. Schedule contingency notes dependency on personnel availability and long-lead component delivery.

7. **Subcontractor References:** CU "Mistral" wing option mentioned; no COTS vendors named but wing/tail procurement from standard suppliers anticipated.

8. **Budget:** $450K fixed labor + actual cost for materials, supplies, and travel; payment milestones tied to design review, assembly completion, flight test, and final package delivery.