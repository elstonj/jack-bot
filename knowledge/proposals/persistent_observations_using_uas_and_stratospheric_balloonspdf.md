# Persistent Observations using UAS and Stratospheric Balloons

## Document Metadata
- **Type:** NASA proposal / demonstration project plan
- **Client/Agency:** NASA (NASA Ames, NASA Flight Opportunities program)
- **Program/Solicitation:** Not explicitly stated; appears to be a direct proposal to NASA for a technology demonstration
- **Date:** Document created/modified July 1, 2025
- **BST Products/Systems Referenced:** S0 UAS, stratospheric balloon gondola integration, command & control software
- **Key Personnel:** Jack Elston (Principal Investigator), Beck Cotter (last editor)

## Executive Summary
This proposal presents a 6-month demonstration project to integrate Black Swift's S0 uncrewed aircraft system into a stratospheric balloon gondola, enabling on-demand deployment of the UAS from high altitude for persistent atmospheric observations. The hybrid platform addresses critical gaps in lower-atmosphere data collection for weather prediction, wildfire monitoring, and Earth system science by combining the balloon's persistence and reach with the S0's maneuverability and sensor sophistication.

## Technical Approach

**Core Integration Concept:**
- Deploy a single S0 UAS from an Aerostar stratospheric balloon gondola at altitude
- S0 launched via sonobuoy-style tube from gondola-mounted launcher
- Aircraft maintains communication with balloon platform for command, telemetry relay, and downlink
- Balloon acts as persistent mobile base station; S0 conducts adaptive, targeted measurements below

**System Architecture (4 Milestones over 6 months):**

1. **Milestone 1 (Months 1–2): Mechanical & Electrical Integration**
   - Design single vertical tube launcher with heated cradle to maintain aircraft operational temperature pre-launch
   - Develop power and data interfaces for onboard warming and preflight checks
   - Fabricate prototype 1-tube launch module
   - Deliverables: CAD drawings, electrical schematics, built prototype, integration test plan

2. **Milestone 2 (Months 2–3): Command & Control System Integration**
   - Minimal communication protocol for power-on, avionics check, and mission plan upload
   - Lab simulation of balloon-S0 command loop (serial or simulated RF link)
   - Minimal UI for power control and launch execution
   - Deliverables: Ground software/microcontroller code, lab C&C demonstration, validation report

3. **Milestone 3 (Months 3–4): Regulatory & Flight Planning**
   - Identify test location (NASA Ames, Edwards AFB corridor, or FAA-cleared area)
   - Secure FAA approval for balloon/UAS release (COA or Part 107 waiver)
   - Develop mission plan and emergency procedures
   - Deliverables: FAA coordination logs, safety risk matrix, mission briefing materials

4. **Milestone 4 (Months 5–6): System Test & Demonstration**
   - Lab validation of launch sequence, power, telemetry
   - Field demonstration (dry-run or live launch per permissions)
   - Present results to NASA Flight Opportunities and stakeholders (USFS, NOAA)
   - Deliverables: Flight test summary report, video/photos, roadmap for multi-aircraft expansion

## Products & Capabilities Described

### Black Swift S0 UAS
- **Specifications:**
  - Mass: 1.2 kg
  - Wingspan: 83 cm
  - Compact, low-cost design
  - Launched from sonobuoy-style tube; recovers to controlled flight in seconds
  
- **Sensor Suite:**
  - 3D wind vectors
  - Pressure, temperature, humidity
  - Surface temperature
  - Terrain/wave height
  - Optional thermal infrared capability (referenced as FireTIRS)
  
- **Proven Performance:**
  - Multiple hurricane deployments in 2024, including Category 5 Hurricane Milton
  - Capable of operating in extreme, hazardous environments
  - Can operate beneath cloud decks, in turbulent layers, smoke-filled conditions
  
- **Operational Advantages Over Radiosondes:**
  - Loiters at altitudes of interest (vs. rapid ascent)
  - Lateral steering to track evolving features
  - High-fidelity data stream to gondola for downlink or direct transmission
  - Sustained profiling with superior spatial and temporal resolution

### Stratospheric Balloon Integration
- Acts as mobile, persistent observation platform
- Drifts over areas of scientific interest
- Releases S0 on-demand when conditions optimal
- Provides power, thermal management, and communications relay
- Gondola: Aerostar platform (partner organization)

## Use Cases & Applications

1. **Wildfire Monitoring & Forecasting** (primary use case)
   - Addresses NASA FireSense initiative and WRF-SFIRE model needs
   - Measures near-surface wind fields, boundary layer stability, plume structure
   - S0 deployed above active fire to capture 3D thermodynamic and wind profiles
   - Data assimilated directly into fire behavior models
   - Outcome: More accurate fire spread forecasts for emergency managers and firefighters

2. **Atmospheric & Climate Science**
   - High-resolution boundary-layer observations in remote/hazardous locations
   - Weather and climate model improvement
   - Disaster response support

3. **Arctic Operations**
   - Adaptable for polar region atmospheric studies

4. **Oceanic Observations**
   - Deployment over ocean basins

5. **Planetary Science Analog & Venus Missions**
   - Potential testbed for upper-atmosphere Venus balloon missions
   - Drone deployment from Venus balloon could enable lower-atmosphere in-situ measurements

6. **Rocket Launch Corridor Monitoring**
   - Support for NASA's rocket launch operations

## Budget Summary

**Total Project Cost: $225,049**
- Direct Labor: $47,627 (350 hrs PI + 300 hrs Aerospace/Avionics Engineer)
- Equipment: $2,000 (launch tube, thermal/electrical interface, integration rig)
- Materials & Supplies: $2,086 (LUCID Phoenix camera $325, consumables)
- Travel: $1,868 (one trip to NASA Ames or California site)
- S0 Aircraft Procurement: $18,000 (one fully-equipped S0)
- Urban Sky Flight Test (balloon platform support): $64,500
- Overhead (46.67%): $28,736
- G&A (18.32%): $32,566
- Profit (7%): $14,723

**Key Budget Notes:**
- Scope intentionally reduced for 6-month demonstration (single aircraft, no multi-aircraft swarm, minimal UI)
- Extended flight operations and UI expansions deferred to future phases
- Simplified mounting strategies to reduce complexity
- Remote demonstration support supplements limited in-person presence
- Urban Sky contracted for balloon platform mission planning, control, integration, and testing support

## Notable Details

1. **Competitive Positioning:**
   - Unique among small UAS for boundary-layer observations in extreme conditions
   - Low-cost hybrid approach with high ROI for NASA
   - Demonstrated hurricane operational capability (2024 flights into Category 5 Milton)

2. **Partners & Stakeholders:**
   - Aerostar (gondola/balloon provider)
   - NASA Ames Research Center
   - NASA Flight Opportunities program
   - USFS and NOAA (demonstration audience)
   - Urban Sky (subcontractor for balloon platform operations)

3. **Risk Management:**
   - Safety risk matrix and emergency procedures developed in Milestone 3
   - FAA regulatory coordination built into development timeline
   - Lab validation precedes field demonstrations

4. **Scalability & Modularity:**
   - Platform described as modular and scalable for different payloads
   - Current demonstration limited to single S0; roadmap includes expansion to multi-aircraft count
   - Adaptable sensor suites for different applications

5. **Strategic Alignment:**
   - Directly supports NASA strategic priorities: improved predictive capabilities, enhanced in-situ observations, resilience to climate/weather extremes
   - Fosters aerospace innovation with dual scientific and societal benefits

6. **Data Assimilation:**
   - Emphasis on real-time model integration (WRF-SFIRE for fires, regional air quality forecasting)
   - High-fidelity telemetry stream enables rapid decision-making in emergency response scenarios