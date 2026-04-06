# Statement of Work (SOW) for Black Swift Technologies — Long-Range Fixed-Wing Evaluation & DoD Autopilot Enablement (BYL-LRFE)

## Document Metadata
- **Type:** Statement of Work (SOW) / Proposal
- **Client/Agency:** ByLight (Bryan Sparling, contact signatory)
- **Program/Solicitation:** ByLight Mustang program (internal reference: BYL-LRFE)
- **Date:** Created 2025-10-06; Modified 2025-10-08
- **BST Products/Systems Referenced:** SwiftCore (flight computer, autopilot, data logging/telemetry system)
- **Key Personnel:** Jack Elston (Black Swift Technologies, signatory)

---

## Executive Summary

Black Swift Technologies proposes a nine-week effort to design, build, and flight-test a second-generation (G2) long-range fixed-wing UAS ("Mustang") meeting ByLight's requirements: ≤55 lb gross takeoff weight (GTOW), full electric propulsion, 400–450 km range, and compatibility with government-provided autopilot and launcher hardware. The work is divided into two efforts: Effort 1 (10/6–10/17) focuses on rapid validation of SwiftCore integration and truck-launch reliability using an existing Mustang Unit 3; Effort 2 (10/6–12/5) encompasses detailed design, COTS procurement, prototype assembly, comprehensive flight testing, and integration of government-supplied components (EchoMAV autopilot, cameras, gimbal, payload).

---

## Technical Approach

### Effort 1: Initial Flight Demonstration (10/6–10/17)
- **Objective:** Validate SwiftCore flight computer performance and truck-launch reliability on existing Mustang Unit 3.
- **Tasks:**
  - Integrate SwiftCore into Unit 3 airframe
  - Execute truck-launch demonstration
  - Collect high-rate flight telemetry (IMU, GPS, power, ESC data) using SwiftCore onboard logging
  - Generate ground and airborne video documentation
  - Deliver preliminary flight data analysis and technical summary
- **Expected Outcome:** Demonstrated reliable flight with documented video and SwiftCore telemetry logs

### Effort 2: G2 UAS Design, Build & Flight Test (10/6–12/5)

#### Task 1: Mission Definition & Concept Design
- Freeze vehicle requirements for payload, range, endurance, and launch constraints
- Leverage SwiftCore's real-time telemetry, logging, and system-identification capabilities to feed early aerodynamic and power-system data into sizing models
- Deliver Mission & Constraints document

#### Task 2: Design Loop (Aerodynamic & Propulsion)
- **Aerodynamic Configuration Selection:**
  - Evaluate candidate wings: BST in-house design, CU "Mistral" wing, and COTS 4–5 m options
  - Use lift/drag estimation tools and Reynolds-scaled polars to achieve 400–450 km range with realistic battery mass fractions
  - Deliver aerodynamic coefficients and performance predictions
  
- **Power-to-Weight Optimization:**
  - Conduct electric propulsion trade studies: motor Kv, propeller diameter/pitch, ESC efficiency, battery energy density
  - Optimize for target cruise power and climb margins to meet 55 lb GTOW and 450 km range goals
  
- **Structural Integrity & Launch Loads:**
  - Compute quasi-static launch loads for rail or truck-launch scenarios
  - Define safety factors for wing joiners, fuselage attachment points, and landing gear
  - Ensure survivability during high-acceleration launch
  
- **Deliverable:** Comprehensive design package including aerodynamic coefficients, propulsion selections, predicted range vs. payload curves, and structural analysis

#### Task 3: COTS Component Procurement
- Vendor down-select and procurement of COTS airframe components (wings, tails, test fuselage)
- Perform dimensional and structural verification (mass properties, stiffness, joiner fit, control-surface play)
- Provide CAD and interface-control drawings for wing-to-fuselage and tail integration
- **Out-of-scope:** Tool-less field assembly, shipping fixtures, or simplified packaging for non-UAS experts

#### Task 4: SwiftCore Integration & Flight Validation
- Install SwiftCore flight computer, avionics, wiring harnesses, sensors, and telemetry systems
- **Launch Testing:**
  - Conduct dry launches with instrumented dummies to characterize release speeds and repeatability
  - Execute staged flight cards (manual launch, stabilization, speed sweeps, climb/descend) to build aerodynamic data sets
  
- **Data-Driven Verification:**
  - Use SwiftCore's onboard high-rate logging to evaluate system stability, vibration environment, and launch dynamics
  - Extract thrust-to-power ratios, trim states, and control effectiveness
  
- **Deliverables:** Ground and airborne videos, flight logs, technical brief on system stability and propulsion performance

#### Task 5: Fuselage Selection
- Evaluate Unit 4 fuselage for available volume, weight, and structural stiffness based on SwiftCore mass-distribution data
- If required, design new fuselage optimized for battery volume, wing joiner loads, and cooling airflow
- Conduct thermal validation using onboard thermal sensors to characterize internal temperature rise
- Deliver selection memo with performance data recommending reuse or redesign

#### Task 6: Progressive Load Testing (up to 55 lb GTOW)
- Conduct sequential flights at multiple gross weights (e.g., 42, 48, 52, 55 lb) using payload simulants
- Confirm CG position and control response at each weight step using SwiftCore telemetry
- Establish stall margins and document structural behavior
- Update aerodynamic models using SwiftCore logs
- **Acceptance Criteria:** Stable flight demonstrated at ≤55 lb GTOW without structural or control anomalies

#### Task 7: Battery & Range Characterization
- **Power-vs-Speed Testing:** Fly controlled speed points while recording voltage, current, ESC temperature, and GPS-based airspeed
- Use SwiftCore power logging and analysis scripts to compute Wh/km
- Extrapolate endurance/range under mission profiles with confidence bounds
- Provide recommended cruise speed for 400–450 km endurance
- **Deliverable:** Validated range model (plots, tabulated data) for ByLight's future autopilot adaptation

#### Task 8: GOTS Component Integration (EchoMAV, Payload, Gimbal, Cameras)
- Design power buses and harnesses to accommodate future integration by ByLight
- Isolate SwiftCore from GOTS payload power systems to prevent EMI/power conflicts
- Export SwiftCore data in open NetCDF format to enable ByLight's translation to Cube or ArduPilot parameter sets
- Verify structural mounting points, vibration isolation, and EMI cleanliness
- **Out-of-scope:** Physical installation or tuning of EchoMAV/Cube autopilots (to be performed by ByLight)

#### Task 9: GOTS Component Flight Validation
- Execute multiple stable flights with SwiftCore as primary flight computer and data logger
- Perform system identification to derive aerodynamic and control-response parameters
- **Reliability Criteria:** Minimum of 3 consecutive successful flights meeting stability and endurance metrics
- **Deliverables:** Consolidated data package, post-flight analysis plots

#### Task 10: Government Launcher Integration
- Design adapter or rail-mount solution for government-provided launcher
- Validate CG alignment and clearances
- **Launch Envelope Characterization:** Use SwiftCore IMU and GPS data to measure acceleration and exit speed
- Define abort thresholds and environmental limits (wind, temperature, battery SoC)
- Execute minimum of 3 successful government-launcher flight sequences
- **Deliverables:** Video, data logs, launcher-integration report

---

## Products & Capabilities Described

### SwiftCore Flight Computer & Autopilot
- **What it is:** BST's integrated flight computer, autopilot, real-time telemetry system, and high-rate data logging platform
- **Capabilities:**
  - Real-time sensor acquisition (IMU, GPS, power measurements, ESC telemetry)
  - Onboard high-rate logging (all flight parameters at flight-test frequencies)
  - System-identification and aerodynamic parameter extraction from flight data
  - Open data export (NetCDF format) for compatibility with third-party autopilots (Cube, ArduPilot)
  - Thermal and vibration environment monitoring
  - Launch-dynamics characterization (acceleration, release speed, dynamics)
  
- **Proposed Use in BYL-LRFE:**
  - Primary flight computer for all BST flight test and validation phases
  - Rapid aerodynamic and power-system data collection to feed design models
  - System identification for control-law development
  - Data source for ByLight's future Cube/ArduPilot parameter set development
  - Comprehensive logging for performance validation and range modeling

---

## Use Cases & Applications

### Mustang G2 Platform — Long-Range DoD ISR/Surveillance UAS
- **Mission Profile:** Full-electric, long-endurance (400–450 km range), truck-launchable, under 55 lb GTOW
- **Payload Integration:** Compatible with government-supplied EchoMAV autopilot, cameras, gimbal, and payload instruments
- **Launch Constraint:** Compatible with both truck launch (Effort 1) and government-provided rail launcher (Effort 2, Task 10)
- **Autopilot Adaptation Path:** SwiftCore validates platform; ByLight translates data/parameters to Cube or ArduPilot for final fielded version
- **Target Customer:** U.S. Department of Defense (indicated by "gov't purchasable IP" requirement)

---

## Timeline

| Week | Date Range | Phase/Milestones |
|------|------------|------------------|
| **Effort 1** |
| Week 1 | 10/6–10/10 | SwiftCore integration & truck launch (Mustang Unit 3) |
| Week 2 | 10/13–10/17 | Flight data collection & analysis; Effort 1 wrap-up |
| **Effort 2** |
| Weeks 3–4 | 10/20–11/01 | G2 design finalization & COTS procurement |
| Weeks 5–7 | 11/03–11/22 | Prototype assembly & ground integration |
| Weeks 8–9 | 11/24–12/05 | Flight testing & final deliverables |

**Critical Path Dependency:** Effort 2 schedule assumes timely availability of personnel and on-time delivery of long-lead materials. BST reserves right to adjust schedule with ByLight coordination if delays occur.

---

## Key Deliverables

### Effort 1 (Due 10/17/25)
- Ground and airborne video of Mustang Unit 3 in stable flight
- SwiftCore flight data logs (raw telemetry)
- Short technical summary of flight reliability and SwiftCore performance
- **Payment:** $100K (upfront at award)

### Effort 2

| Milestone | Target Date | Deliverables | Payment |
|-----------|-------------|--------------|---------|
| **Milestone 1: Design & Procurement** | 11/01/25 | G2 conceptual design (≤55 lb, 400–450 km range); aerodynamic configuration & propulsion sizing; structural load analysis; COTS airframe components sourced & ordered; Design & Procurement Report; CAD drawings & SwiftCore integration plan | $100K |
| **Milestone 2: Assembly & Ground Integration** | 11/22/25 | Prototype airframe assembled with SwiftCore installed; bench & ground power tests completed; launcher fit-checks & dry runs performed; CG, battery placement, sensor alignment verified; Integration and Ground Test Report | $100K |
| **Milestone 3: Flight Testing & Performance** | 12/05/25 | Flight test campaign (≥3 successful flights); launch reliability & stable flight at incremental weights demonstrated; power-vs-speed and battery-draw data collected; preliminary range & performance model; Flight Test Report, logs, videos | $100K |
| **Milestone 4: Final Design Package & Close-Out** | 12/05/25 | Final design documents for Effort 2 airframe; production recommendations; comprehensive data package (SwiftCore logs, plots, models, videos