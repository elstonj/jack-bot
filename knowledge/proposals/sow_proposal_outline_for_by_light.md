# SOW / Proposal Outline for By Light – Long-Range Fixed-Wing Evaluation & DoD Autopilot Enablement (BYL-LRFE)

## Document Metadata
- **Type:** Statement of Work / Proposal Outline
- **Client/Agency:** By Light Professional IT Services (BYL)
- **Program/Solicitation:** Long-Range Fixed-Wing Evaluation & DoD Autopilot Enablement (BYL-LRFE)
- **Date:** Created 2025-09-30; Modified 2025-10-02
- **BST Products/Systems Referenced:** SwiftCore (data-logger), Mistral wing/tail system
- **Key Personnel:** Dan (PM/Systems), Maciej (Aero/Controls Lead), Dan Haselius (pilot/integration), Spencer Lisenby (aero review consultant)

---

## Executive Summary

BST proposes an 8-week evaluation and optimization effort for By Light-furnished fixed-wing airframes to achieve 400–500 km range at approximately 35 lb gross takeoff weight (GTOW). Work includes airworthiness assessment, comprehensive flight envelope characterization, performance modeling, ArduPilot autopilot parameter development, and ranked design recommendations. Optional hybrid integration testing with BST's Mistral wing/tail system is available to quantify endurance improvements.

---

## Technical Approach

### Phase 1: Intake & Instrumentation (Weeks 1–2)
- Quality assurance inspection: weighing, measuring, center-of-gravity (CG) audit, structural sanity check
- Propulsion bench runs and ESC timing verification
- Installation of **SwiftCore** as primary data-logger with taps for power, voltage, and ESC telemetry
- Pitot, GPS, and IMU alignment

### Phase 2: Ground Testing & Characterization (Weeks 1–2)
- Static thrust testing and power maps across prop selections
- Launcher speed repeatability and release dynamics characterization
- Performance data gathering to support endurance/range modeling

### Phase 3: Manual Flight Envelope Expansion (Weeks 2–3)
- Captive and low-risk flight profiles to map drag polar proxy (power vs. airspeed)
- Climb rate and glide polar sampling
- Data used to validate in-situ aerodynamic estimates given sparse aero documentation

### Phase 4: Performance Modeling & Autopilot Enablement (Weeks 3–5)
- Curve fitting and endurance/range projection at target weights
- Sensitivity analysis: battery energy density (Wh/kg), propeller selection, cruise speed
- Initial ArduPilot/Cube parameter set development: rates, PIDs, mixer, airspeed/TECS configuration, stall protections
- Parameter refinement based on verification flight results

### Phase 5: Design Assessment & Verification (Weeks 4–7)
- Ranked change list: aerodynamic (airfoil/incidence/twist), structural, propulsion, and mass targets with ROI analysis
- Repeatable verification flight profiles to validate performance model vs. actual flight

### Phase 6 (Optional): Hybrid "Mistral" Demonstration (Weeks 6–8)
- Integration of Mistral wing/tail with By Light fuselage
- Fit-check, CG verification, short flight series to quantify endurance delta vs. baseline

---

## Products & Capabilities Described

### SwiftCore
- **What it is:** BST's avionics/data-logging system
- **Proposed use:** Primary flight data recorder; provides synchronized power, voltage, ESC telemetry, pitot, GPS, and IMU data
- **Capability:** Enables time-aligned, replayable data packages essential for performance modeling validation

### Mistral Wing/Tail System
- **What it is:** BST-designed hybrid wing/tail aerodynamic surfaces
- **Proposed use (Option A):** Integration with By Light fuselage to assess endurance improvement over baseline
- **Expected value:** Quantifiable drag reduction and range/endurance delta

---

## Use Cases & Applications

- **Long-range fixed-wing operations:** Evaluation targeting 400–500 km range at ~35 lb GTOW (lightweight tactical/ISR profile)
- **DoD autopilot integration:** ArduPilot/Cube parameter development and safety envelope definition
- **Launcher-assisted launches:** Characterization of launcher performance and repeatability for repeatability-critical operations

---

## Deliverables

| # | Deliverable | Content |
|---|---|---|
| **D1** | Intake/QA Report | Weights, CG, build notes, structural assessment, photos |
| **D2** | Ground/Launcher Test Report | Thrust maps, speed repeatability data |
| **D3** | Flight Data Package | Raw logs + merged CSV (time-aligned), plotting scripts |
| **D4** | Performance Brief | Drag polar proxy curves, endurance/range projections, recommended cruise settings |
| **D5** | Autopilot Parameters | ArduPilot parameter set, tuning steps, safety limits, checklist |
| **D6** | Design Change Matrix | Ranked aerodynamic, structural, propulsion, and mass recommendations with benefit/effort/ROI |
| **D7** (Opt) | Hybrid Demo Note | Mistral integration measured deltas vs. baseline |
| **D8** | Final Tech Memo + Return Report | Full data package consolidation, vehicle condition on hand-back |

---

## Schedule

**8-Week Critical Path:**
- **Wk 1:** Intake, QA, instrumentation planning
- **Wk 2:** Instrumentation install; ground/launcher characterization
- **Wk 3:** Manual flights; first performance model; D2 draft
- **Wk 4:** Initial autopilot parameters; safety envelope definition; D3/D4 drafts
- **Wk 5:** Verification flights; parameter refinement; D5 draft
- **Wk 6:** Design change matrix completion; (Opt) Hybrid fit-check
- **Wk 7:** (Opt) Hybrid flights; findings consolidation
- **Wk 8:** Final data/package delivery; vehicle hand-back; D8 completion

---

## Acceptance Criteria

1. Complete, replayable, synchronized data package (power, airspeed, attitude, time-aligned)
2. Quantified range/endurance projection at 35 lb GTOW with sensitivity analysis (Wh/kg, cruise speed)
3. Ranked, actionable design change list tied to measurable range/endurance improvements

---

## Staffing & Resources

- **PM/Systems:** Dan (oversight, client comms, acceptance)
- **Aero/Controls Lead:** Maciej (modeling, autopilot tuning, analysis)
- **Flight Test Engineer + Technician:** Instrumentation, flight operations, launcher support
- **Consultants/Optional:** Spencer Lisenby (aerodynamic review/concept), Dan Haselius (pilot/integration support), Mistral wing/tail engineering support

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| Launcher speed variability / under-speed launches | Pre-flight launcher characterization; minimum launch speed threshold enforcement |
| Sparse aerodynamic documentation | In-situ measurements via instrumented flights; conservative test cards; multi-profile validation |
| Holiday/weather delays | Parallelize analysis work; reserve buffer days in weeks 5–7 |

---

## Commercial Terms

### Base Pricing
- **Fixed Price (Base Tasks 1–8, 8 weeks):** $215,000 + travel at cost
  - Reflects compressed schedule and opportunity cost

### Options
- **Option A (Hybrid/Mistral demo):** +$65,000 (wingset procurement/loan outside scope)
- **Option B (On-site NC campaign):** +$45,000/week for in-person flight operations; remote ops with data turns otherwise
- **Option C (External experts):** Pass-through at cost + 10% admin (e.g., Lisenby day-rate, Mistral support)

### Alternative Structure
- **T&M with NTE $500k** for Base; same option pricing

### Invoicing
- 40% on award
- 40% at D5 delivery
- 20% at D8 final delivery
- Net 15 payment terms

---

## Data Rights & IP

- All vehicle data returned to By Light
- BST retains methods, analysis scripts, and SwiftCore avionics design/implementation intellectual property

---

## Notable Details

- **Compressed 8-week schedule** reflects BST's established rapid-cycle evaluation capability
- **Mistral integration option** (Option A) leverages BST's proprietary hybrid aerodynamic design to provide endurance delta benchmarking
- **Scope assumes** By Light provides two flightworthy airframes, spares, launcher/launcher performance data, motor/ESC/prop, batteries, and ArduPilot/Cube baseline parameters
- **Data package approach** (D3: raw logs + merged CSV + scripts) designed for By Light's internal reproducibility and future iteration
- **Consultant network** (Lisenby, Haselius) available for specialized aero review and pilot integration support at pass-through rates