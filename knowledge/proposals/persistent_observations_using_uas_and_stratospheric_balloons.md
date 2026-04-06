# Persistent Observations using UAS and Stratospheric Balloons

## Document Metadata
- **Type:** NASA proposal / Project application
- **Client/Agency:** NASA (Flight Opportunities program, with stakeholders including NASA Ames, USFS, NOAA)
- **Program/Solicitation:** NASA Balloon Observations (specific solicitation not named)
- **Date:** Submitted between May 28, 2025 (created) and July 8, 2025 (last modified)
- **BST Products/Systems Referenced:** S0 UAS, stratospheric balloon gondola integration
- **Key Personnel:** Jack Elston (PI); Maciej Stachura (editor)

---

## Executive Summary

Black Swift Technologies proposes a 6-month demonstration project to integrate the S0 uncrewed aircraft system into a stratospheric balloon gondola, enabling on-demand deployment of the aircraft from high altitude for targeted, adaptive measurements over areas of scientific interest. The hybrid system would allow real-time video and sensor data collection near the surface while leveraging the balloon as both a persistent platform and communication relay, with primary applications in wildfire monitoring, Earth system modeling, and extreme weather observation.

---

## Technical Approach

**Core Integration Strategy:**
- Mount a single Black Swift S0 UAS in a sonobuoy-style tube launcher integrated into an Aerostar balloon gondola
- Design a heated cradle/tube system to maintain aircraft operational temperatures pre-launch
- Develop command and control interface to enable balloon-mounted systems to power on the S0, verify avionics, and upload pre-defined mission plans
- Create minimal ground software (or balloon-mounted microcontroller code) to issue launch commands
- Conduct lab validation of communication loop followed by field demonstration with NASA stakeholders

**Phased Execution (6 months):**
1. **Months 1–2:** Design and fabricate mechanical/electrical balloon mount system; produce CAD drawings, schematics, and lab-tested prototype
2. **Months 2–3:** Develop and validate command & control software; demonstrate simulated communication loop in tethered lab setup
3. **Months 3–4:** Coordinate FAA regulatory approval (COA/Part 107 waiver); finalize mission plan and safety risk matrix
4. **Months 5–6:** Conduct integrated system validation and live field demonstration with NASA Ames and Aerostar; deliver flight test report and recommendations for follow-on phase

---

## Products & Capabilities Described

### Black Swift S0 UAS
- **What it is:** Compact, low-cost uncrewed aircraft system (1.2 kg, 83 cm wingspan)
- **Proven capabilities:** Multiple deployments in extreme environments including Category 5 Hurricane Milton (2024); sonobuoy-style tube launch with recovery to controlled flight within seconds
- **Sensor suite:** 3D wind vectors, pressure, temperature, humidity, surface temperature; expandable with machine vision camera for high-resolution video/stills near surface
- **Proposed use in this project:** Deploy from stratospheric balloon to collect targeted, adaptive measurements; capture high-resolution video/imagery far closer to ground than balloons or satellites; loiter and be retasked based on real-time sensor data; relay data through balloon to eliminate need for costly onboard satellite communications
- **Cost:** $18,000 per aircraft for this project

### Stratospheric Balloon Gondola (Aerostar Platform)
- **Role:** Acts as persistent observing platform and mobile base station; drifts over areas of scientific interest; provides power and communication infrastructure for S0 launch and data relay
- **Integration approach:** Single vertical tube launcher module; heated interface for pre-launch thermal management; electrical/data connections for power and preflight checks

---

## Use Cases & Applications

### Primary Use Case: Wildfire Monitoring
- Real-time imagery of fire plumes for direct assimilation into WRF-SFIRE or similar fire-atmosphere models
- Detection of new and small smoke plumes not yet visible to satellites or higher-altitude platforms
- Machine vision algorithms for real-time smoke classification and tracking
- Support for emergency managers and firefighters protecting lives, property, and ecosystems
- Addresses gap highlighted by NASA's FireSense efforts for rapid, high-resolution data in high-risk areas
- Avoids deployment risks from severe wind shear and visual obstructions from smoke near ground level

### Secondary Applications
- **Arctic operations:** Observations over remote areas lacking conventional launch infrastructure
- **Ocean basins:** Storm and weather monitoring from persistent floating platform
- **Rocket launch corridors:** Monitoring conditions during NASA launch windows
- **NASA planetary science campaigns:** Modular design enables support for airborne and balloon-based missions
- **Upper atmosphere analog studies:** Proof-of-concept for Venus atmospheric missions, where balloon-launched drone could make in-situ measurements in lower Venusian atmosphere

---

## Key Results

This is a **proposal**, not a completed project report. No results are presented. The document outlines deliverables expected upon completion:
- CAD drawings, electrical schematics, and prototype launch module
- Validated command & control software and demonstration
- FAA coordination documentation and safety risk matrix
- Flight test summary report with telemetry and system behavior observations
- Integrated demo video and field photos
- Roadmap for follow-on phase with expanded aircraft count or capabilities

---

## Budget & Resource Allocation

**Total Project Cost:** $225,049 (including overhead, G&A, and profit)

**Direct Costs Breakdown:**
| Category | Amount |
|----------|--------|
| Direct Labor (PI + Aerospace/Avionics Engineer) | $47,627 |
| Equipment (launch tube, thermal/electrical interface, integration rig) | $2,000 |
| Materials & Supplies (LUCID Phoenix 6.3 MP camera $325, misc.) | $2,086 |
| Travel (CA site visit, airfare, lodging) | $1,868 |
| S0 Aircraft Procurement (1 unit, full sensor suite) | $18,000 |
| Urban Sky Risk Reduction Flight (platform, integration, testing) | $64,500 |
| **Subtotal Before Overhead** | $136,081 |

**Applied Rates:**
- Overhead (46.67%): $28,736
- General & Admin (18.32%): $32,566
- Profit (7%): $14,723

**Personnel Allocation:**
- **Jack Elston (PI):** ~350 hours for technical direction, interface design, integration oversight, stakeholder coordination
- **Aerospace/Avionics Engineer:** ~300 hours for electrical interface prototyping, launch command system integration, simulation testing

---

## Notable Details

**Competitive Advantages:**
- S0 has **proven operational record** in extreme environments (Category 5 hurricane deployments in 2024)
- **Low cost and operational flexibility** compared to crewed aircraft
- **Data relay through balloon eliminates need for onboard satellite communications**, reducing weight and cost of UAS
- **Adaptive, on-demand capability:** Unlike balloons, S0 can loiter and be retasked based on real-time data
- **High spatial and temporal resolution** near surface, filling gap between satellite and crewed aircraft capabilities

**Partnership & Coordination:**
- Collaboration with **NASA Ames** (demonstration site and stakeholder)
- Integration with **Aerostar** gondola platform (partnership already implied)
- **Urban Sky** contracted for balloon platform mission planning, control, integration, performance, and testing support ($64,500 budget line)
- Stakeholder coordination with USFS and NOAA planned

**Risk Mitigation & Regulatory Path:**
- Phase 1 scoped narrowly to **single-aircraft demonstration** (no multi-aircraft swarm capabilities, no full-scale UI infrastructure)
- FAA coordination planned for COA (Certificate of Airworthiness) or Part 107 waiver
- Safety risk matrix and mission briefing materials required before flight test
- Lab validation precedes field demonstration

**Future Expansion Potential:**
- Document explicitly notes this is a **6-month demonstration** with roadmap for follow-on phase
- Expansion possibilities include multi-aircraft capabilities, extended flight operations, and expanded UI infrastructure
- Modular sensor payload design supports diverse mission sets

**Noted Sensor Additions:**
- LUCID Phoenix 6.3 MP Camera (3072 x 2048 px, 17.7 fps) selected for machine vision and high-resolution imagery near surface
- Existing S0 sensor suite (winds, pressure, temperature, humidity, surface temperature, terrain/wave height) retained

---

**Document Observation:** This is a well-structured, focused proposal demonstrating clear understanding of NASA's scientific priorities (wildfire monitoring, Earth observation, extreme weather), regulatory requirements, and realistic 6-month demonstration scope. The budget is transparent with detailed labor justification and clear line items.