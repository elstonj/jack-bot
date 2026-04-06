# Long-Range Fixed-Wing Evaluation & DoD Autopilot Enablement (BYL-LRFE)

## Document Metadata
- **Type:** Statement of Work (SOW) / Subcontractor Task Order
- **Client/Agency:** ByLight (appears to be a DoD-related program)
- **Program/Solicitation:** BYL-LRFE (Long-Range Fixed-Wing Evaluation & DoD Autopilot Enablement)
- **Date:** Created 2025-09-30; Modified 2025-10-15
- **BST Products/Systems Referenced:** ArduPilot/Cube autopilot integration; airframe evaluation (details of specific BST systems not provided in this SOW)
- **Key Personnel:** Jack Elston (PI), Daniel Prendergast (PM/System Engineer), Maciej Stachura (Aero/Controls Lead), Spencer Lisenby (Aero review), Dan Hesselius (Pilot/integration), unnamed Flight Test Engineer + Tech

## Executive Summary
Black Swift Technologies will evaluate 1–2 fixed-wing airframes furnished by ByLight for airworthiness and endurance potential, generate validated performance data, and deliver design recommendations to achieve 400–500 km range at ~35 lb GTOW. The 8-week engagement includes comprehensive flight testing, autopilot integration, performance analysis, and design optimization recommendations.

## Technical Approach

**Core Tasks:**
1. Intake and quality assurance of furnished airframes (weights, CG, build verification)
2. Ground and launcher testing (thrust mapping, speed repeatability validation)
3. Flight testing and data collection (raw logs, time-aligned merged datasets)
4. Aerodynamic modeling and performance analysis (drag proxy curves, endurance/range estimation)
5. ArduPilot/Cube autopilot parameter development, tuning, and safety limits definition
6. Design change prioritization and recommendation matrix
7. Optional hybrid propulsion demonstration with measured performance deltas
8. Final technical memorandum and airframe return condition report

**Key Technical Focus:**
- Target performance: 400–500 km range at ~35 lb GTOW (gross takeoff weight)
- Cruise optimization and endurance calculations
- Autopilot tuning for stability and safety limits
- Launcher performance validation
- Airworthiness assessment

## Products & Capabilities Described

**ArduPilot/Cube Integration:**
- Parametrization and tuning for the furnished airframes
- Safety limits definition and operational checklists
- Parameter tuning steps for flight envelope optimization

**BST Flight Testing Capabilities:**
- Instrumentation and flight operations
- Data acquisition and processing (raw logs, CSV merging, time-alignment)
- Performance analysis and modeling

**BST Aerodynamic/Controls Expertise:**
- Drag proxy curve development
- Endurance and range estimation modeling
- Control systems tuning and optimization

## Use Cases & Applications

- **Long-range fixed-wing operations** for DoD applications
- **Launcher-based deployment** (airframe designed for catapult/launcher launch)
- **Extended endurance missions** (~35 lb airframe, 400–500 km range target)
- **Autonomous operations** via ArduPilot integration

## Deliverables

| Deliverable | Description |
|---|---|
| D1 | Intake/QA Report (weights, CG, build notes, photos) |
| D2 | Ground/Launcher Test Report (thrust maps, speed repeatability) |
| D3 | Flight Data Package (raw logs + merged CSV, time-aligned; plotting scripts) |
| D4 | Performance Brief (drag proxy curves, endurance/range estimates, recommended cruise) |
| D5 | Autopilot Params + tuning steps, safety limits, and checklist |
| D6 | Design Change Matrix (priority/benefit/effort with rationale) |
| D7 (Optional) | Hybrid Demo Note with measured deltas vs. baseline |
| D8 | Final Tech Memo and return condition report |

## Period of Performance
- **Start:** 10/13/25
- **End:** 12/5/25
- **Duration:** 8 weeks

## Staffing & Roles

| Role | Personnel | Responsibility |
|---|---|---|
| Principal Investigator | Jack Elston | Overall leadership |
| PM/System Engineer | Daniel Prendergast | Oversight, communications, acceptance |
| Aero/Controls Lead | Maciej Stachura | Aerodynamic modeling, control tuning, analysis |
| Aero Review/Concept | Spencer Lisenby | Aerodynamic review support |
| Pilot/Integration | Dan Hesselius | Flight operations, "Mistral" wingset integration support |
| Flight Test Engineer/Tech | (NAME not provided) | Instrumentation and operations |

## Pricing Structure

**Base Contract (Tasks 1–8, 8 weeks):** 
- Fixed price: **$215k** (reflects compressed schedule and opportunity cost)
- Plus travel at cost

**Optional Tasks:**
- **Option A (Hybrid/Mistral demo):** +$65k (wingset procurement/loan outside scope)
- **Option B (On-site NC campaign):** +$45k/week for weeks requiring in-person flight team; remote ops with data turns otherwise
- **Option C (External experts):** Pass-through at cost + 10% admin

**Payment Model:** Milestone-based; invoices submitted upon successful completion of each deliverable milestone.

## Notable Details

1. **ByLight Furnishes:** Two flightworthy airframes + spares, launcher or launcher performance data, specified motor/ESC/props, batteries, ArduPilot/Cube parameter sets, wiring, logs (if available), flight site access, range safety support

2. **Scope Clarifications:** The document includes a placeholder for exclusions ("Be certain to indicate specifically...any items that are excluded") but these are not filled in, suggesting final scope boundaries may still be under negotiation

3. **Hybrid Propulsion Interest:** Optional deliverable D7 and Option A suggest exploration of hybrid (likely hybrid-electric) propulsion as a range/endurance enhancement option; "Mistral" wingset appears to be a specific hybrid component

4. **Remote Flexibility:** Option B allows for remote operations with data turns, or on-site flight team presence; suggests adaptability to client location constraints

5. **Compressed Schedule:** The fixed-price base contract notes "compressed schedule" as a cost factor, indicating this is an accelerated 8-week effort relative to normal timelines