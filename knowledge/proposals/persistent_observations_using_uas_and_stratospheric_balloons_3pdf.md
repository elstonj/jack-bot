# Persistent Observations using UAS and Stratospheric Balloons

## Document Metadata
- **Type:** Proposal / NASA Aero RFI Response
- **Client/Agency:** NASA (NASA Ames implied)
- **Program/Solicitation:** NASA Aeronautics Research Institute (Aero RFI) – Stratospheric Balloon focus
- **Date:** April 2026
- **BST Products/Systems Referenced:** S0 UAS
- **Key Personnel:** Jack Elston (PI), Beck Cotter (last editor)
- **Partners/Collaborators:** NASA Ames, Aerostar (balloon provider), Urban Sky (flight test platform), USFS, NOAA

## Executive Summary
Black Swift Technologies proposes a 6-month demonstration project to integrate its S0 uncrewed aircraft system into a stratospheric balloon gondola, creating a hybrid persistent observation platform capable of deploying on-demand atmospheric profiling missions. This system would enable sustained, high-resolution measurements of boundary-layer conditions in extreme environments (wildfires, hurricanes, remote regions) where traditional platforms cannot operate, with immediate application to wildfire forecasting and broader potential for Earth science and planetary missions.

## Technical Approach

### System Architecture
- **Platform Integration:** Single S0 UAS mounted in a vertical tube launcher integrated into an Aerostar stratospheric balloon gondola
- **Operational Concept:** Balloon drifts over area of scientific interest (developing wildfire, ocean storm, rocket launch corridor) and releases S0 aircraft on-demand when conditions are optimal
- **Data Flow:** S0 collects high-fidelity atmospheric data during loiter/profiling missions and transmits to gondola for downlink or direct transmission

### Development Milestones (6-Month Timeline)

**Milestone 1: Design and Fabrication of Balloon Mount System (Months 1–2)**
- Develop simplified mechanical/electrical interface for one S0 into Aerostar gondola
- Design heated cradle/tube system to maintain aircraft within operational temperature pre-launch
- Define power and data interface for onboard warming and preflight checks
- Deliverables: CAD drawings, electrical schematics, fabricated prototype of 1-tube launch module, documented test plan

**Milestone 2: Command and Control System Integration (Months 2–3)**
- Develop minimal communication protocol to power on S0, check avionics, upload pre-defined mission plan
- Simulate balloon-S0 command loop in lab with serial or simulated RF link
- Integrate minimal UI interface for power control and launch execution
- Deliverables: Ground software/balloon-mounted microcontroller code, tethered lab demonstration, communication loop validation report

**Milestone 3: Flight Planning and Regulatory Coordination (Months 3–4)**
- Identify test location (NASA Ames, Edwards AFB corridor, or FAA-cleared area)
- Coordinate with FAA for balloon and UAS release approval (COA or Part 107 waiver)
- Finalize mission plan and emergency procedures
- Deliverables: FAA coordination logs, safety risk matrix, mission briefing materials, stakeholder communications

**Milestone 4: System Test and Demonstration (Months 5–6)**
- Lab system validation (launch sequence, power checks, telemetry transfer)
- Field demonstration of system functionality (dry run or live launch)
- Present results to NASA Flight Opportunities and stakeholder agencies (USFS, NOAA)
- Deliverables: Flight test summary report, integrated demo video/photos, roadmap for follow-on phase with expanded aircraft count

## Products & Capabilities Described

### Black Swift S0 UAS
**Physical Specifications:**
- Mass: 1.2 kg
- Wingspan: 83 cm
- Launch method: Sonobuoy-style tube
- Recovery: Controlled flight within seconds of launch

**Sensor Suite:**
- 3D wind vectors
- Pressure, temperature, humidity
- Surface temperature
- Terrain/wave height measurement

**Operational Capabilities:**
- Proven deployment in extreme environments including multiple 2024 hurricane flights (Cat. 5 Hurricane Milton)
- Can operate beneath cloud decks, inside turbulent wind layers, within smoke-filled/stormy environments
- Ability to loiter at altitudes of interest and steer laterally to track evolving features
- Low-cost platform with sophisticated avionics

**Proposed Role in Balloon Integration:**
- On-demand deployment from stratospheric altitude
- Sustained vertical profiling of atmosphere with superior spatial/temporal resolution compared to traditional weather balloons
- Direct data assimilation capability into atmospheric models

## Use Cases & Applications

### Primary: Wildfire Monitoring and Forecast Improvement
- Addresses NASA FireSense initiative and WRF-SFIRE model development needs
- Captures critical parameters: near-surface wind fields, boundary layer stability, plume structure
- Enables 3D profiling of thermodynamic and wind fields directly within/above fire plume
- Supports real-time model assimilation for improved fire behavior forecasts essential for emergency management

### Secondary Applications
- **Arctic operations:** Remote monitoring over ice-covered regions
- **Ocean basin monitoring:** Persistent observations over water without traditional launch infrastructure
- **Rocket launch corridor support:** Real-time atmospheric characterization for launch operations
- **Planetary science analog studies:** Potential application to Venus atmospheric missions (proof-of-concept for deploying drones from high-altitude balloons to enable lower-altitude in-situ measurements)
- **Earth system modeling and climate monitoring:** Modular, scalable platform adaptable to different payloads

## Budget Summary

**Total Budget (including overhead, G&A, profit): $225,049**

### Cost Breakdown by Category:
| Category | Amount |
|----------|--------|
| Direct Labor (PI + Aerospace Engineer, ~650 hrs) | $47,627 |
| Equipment (launch tube, thermal/electrical interface, integration rig) | $2,000 |
| Materials & Supplies (LUCID Phoenix camera, consumables) | $2,086 |
| Travel (1 engineer/PI trip to NASA site) | $1,868 |
| S0 Aircraft Procurement (1 fully equipped system) | $18,000 |
| Urban Sky Flight Test Support | $64,500 |
| Overhead (46.67%) | $28,736 |
| General & Admin (18.32%) | $32,566 |
| Profit (7%) | $14,723 |

### Key Budget Notes:
- Personnel: Jack Elston (~350 hrs for technical direction/integration oversight) + Aerospace/Avionics Engineer (~300 hrs for electrical interface/command system/simulation)
- Labor scoped to critical development only; extended flight operations deferred to future phase
- Single-aircraft demonstration with no multi-aircraft capabilities or full-scale UI infrastructure
- Equipment costs minimized through simplified mounting strategies
- Urban Sky component covers balloon platform mission planning, control, integration, performance, and testing support
- No expansion to multiple aircraft or full operational infrastructure in this phase

## Notable Details

### Competitive Advantages Highlighted
- **Low cost platform** with proven extreme environment capability (hurricane penetrations 2024)
- **Rapid deployment** from tube launch: recover to controlled flight within seconds
- **Unique atmospheric access:** Can operate where traditional platforms struggle—beneath clouds, in turbulent layers, in smoke/storms
- **Adaptive measurement:** Can steer laterally, loiter at specific altitudes, return real-time data stream rather than single-snapshot ascent profile

### Technology Benefits for NASA Objectives
- Addresses critical gap in sustained, in-situ boundary-layer observations in hazardous/remote environments
- Improves both spatial and temporal resolution of environmental data vs. traditional radiosondes
- Enables direct assimilation into operational forecasting models (WRF-SFIRE)
- Modular architecture supports payload diversity and scalability
- High return on investment relative to cost

### Regulatory/Operational Approach
- Single-aircraft demonstration limits complexity; multi-aircraft swarming deferred
- Leverages existing FAA approval pathways (COA, Part 107 waivers)
- Targets FAA-cleared test zones (NASA Ames, Edwards AFB corridor)
- Includes risk-managed flight test profile with safety matrix

### Scientific Impact Areas
- **Wildfire science:** Real-time boundary-layer profiling for fire behavior prediction
- **Weather/climate modeling:** In-situ data for model improvement and validation
- **Disaster response:** Enhanced forecasting for hurricane and extreme weather support
- **Planetary science:** Proof-of-concept for Venus atmosphere exploration (drone-from-balloon concept)

### Document Notes
This is a focused, well-scoped proposal for rapid prototyping and demonstration rather than full operational system development. The 6-month timeline concentrates on integration feasibility and single-aircraft deployment validation, explicitly deferring expanded capabilities (multi-aircraft swarms, advanced UI, operational deployment) to future phases. The emphasis on simplification and risk reduction suggests this is positioned as a technology demonstration for potential larger follow-on investments.