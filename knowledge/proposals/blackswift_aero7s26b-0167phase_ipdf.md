# All-Weather, Terrain and Wind-Aware Autonomous Sensing for Wildfire Aviation

## Document Metadata
- Type: NASA SBIR Phase I Proposal
- Client/Agency: NASA (Advanced Aeronautics Division)
- Program/Solicitation: NASA SBIR 2026, Subtopic AERO.7.S26B ("Nontraditional Airspace Operations and Aerial Wildfire Response")
- Date: Submitted 2026-05-20
- BST Products/Systems Referenced: S3 (long-endurance fixed-wing VTOL), S0-VTOL (backpackable rapid-deploy node), SwiftCore (modular avionics/FMS), NightFOX (IR/multispectral fire payload), meteorological probe
- Key Personnel: Dr. Jack Elston (PI, CEO), Dr. Maciej Stachura (CTO, Co-Investigator)

## Executive Summary
Black Swift Technologies proposes a platform-agnostic framework of terrain- and wind-aware autonomous sensing algorithms combined with modular mission payloads for wildfire aviation operations. The framework addresses three critical gaps exposed by the 2024-2025 Colorado fire seasons: (1) no aerial platform routinely operates at night or in smoke/extreme drainage winds (50-100+ mph); (2) no platform samples fine-scale fire weather with research-grade instruments inside the convective boundary layer where wind-fire feedbacks occur; and (3) incident commanders lack real-time calibrated data delivery (currently 4+ hours latency). The work is anchored on BST's operational heritage from ten NOAA hurricane field deployments (2023-2025) involving 44 sorties, 36+ hours in-storm data, and extreme conditions (209-kt gust in Hurricane Milton, 119-minute eyewall flight in Hurricane Melissa).

## Technical Approach

**Five Core Innovations:**

1. **Terrain- and Wind-Aware Autonomous Mission Planning**
   - Fuses a priori terrain (DEM), a priori fine-scale wind from NCAR WRF-SFIRE/CAWFE products, and onboard 100-Hz 3-D wind/turbulence measurements to generate continuously updated flyable envelopes
   - Constraints: energy, comms line-of-sight, sensor geometry
   - Phase I scope: terrain + a priori wind + synthetic onboard wind validation
   - Phase II scope: real-time onboard obstacle/terrain refinement via Maxar GPS-alternative system; full real-time wind assimilation
   - Test cases: drainage-channelized flow, plume convergence, ridge-top inversion regimes from Marshall Fire and East Troublesome Fire archives

2. **Automated Fire-Line Mapping via Objective-Seeking Autonomy**
   - Generalizes BST's flight-proven cyclone maximum-wind-seeking and storm-center-fix controllers to fire applications
   - Primitive: "follow a contour of an evolving scalar field while respecting an envelope"
   - Phase I: scoping and de-risking only (algorithm-level specification, not SIL implementation)
   - Phase II: full SIL implementation, validation against archived WRF-SFIRE perimeters, TRL-5 flight demonstration
   - Catalog includes: plume-edge tracking, fire-front following, convective-updraft profiling, standoff loitering

3. **Automatic NWS-Grade In-Situ Weather Sampling**
   - Leverages BST's existing NWS-approved meteorological probes (100-Hz pressure, temperature, humidity, 3-D wind/turbulence)
   - Integrates with fine-scale fire weather models (WRF-SFIRE/CAWFE)
   - Prior Marshall Fire collaboration with NCAR Dr. James Pinto showed sparse UAS profiles improved forecasts up to 8 hours forward
   - Phase II lifts prior NASA SBIR Phase I automatic weather sampling work product onto new objective-seeking framework; aircraft autonomously selects sampling locations based on model assimilation needs

4. **Modular, Platform-Agnostic Payload and Avionics Interface**
   - SwiftCore avionics stack service contract: sensor data bus, command bus, runtime-assurance boundary, third-party algorithm host interface
   - BST modular payload interface (mechanical, electrical, power, data-bus, COT message schema)
   - Payload library includes: NightFOX IR/multispectral, NWS-approved met probe, in-situ plume payload (CO₂, CO, aerosol, RH, p, T), multi-source airspace-awareness package (ADS-B In, Long-Range Remote ID, software-defined radio for non-cooperative aircraft detection)
   - Designed for adoption by non-BST airframes (ACERO partners, Overwatch Aero, L3Harris, etc.)
   - SwiftCore architecture explicitly designed to host third-party algorithms (including LLM-based mission supervisors) behind deterministic runtime-assurance boundary
   - Interface implemented as reference on BST S3

5. **All-Weather Operational Heritage in Extreme Boundary-Layer Environments**
   - Ten NOAA tropical cyclone field deployments (2023-2025): 44 operational sorties, 36+ hours in-storm data
   - Maximum measured wind: 209 kt (Hurricane Milton, 2024)
   - Longest flight: 119.5 minutes (Hurricane Melissa, 2025)
   - Maximum communications range: 300 statute miles from launching P-3 (Melissa, 2025)
   - Same airframes, autopilot, sensors, communications stack form foundation of wildfire framework

## Products & Capabilities Described

### S3 (Long-Endurance Fixed-Wing VTOL)
- Production platform with NASA flight heritage
- End-to-end BST control
- Will demonstrate Phase I framework implementation
- Multi-role payload capability for IR, meteorological, plume, and airspace-awareness sensors
- Supports BVLOS operations in high-wind, mountainous terrain

### S0-VTOL (Backpackable Rapid-Deploy Node)
- Backpackable rapid-deployment platform
- NASA flight heritage from NOAA hurricane deployments
- Proven in extreme atmospheric environments
- Will demonstrate framework on alternative airframe form factor

### SwiftCore Flight Management System (FMS)
- Modular avionics architecture
- DEM-aware path planning capability (demonstrated S2 BVLOS missions to 7,000 ft MSL over Aleutian volcanoes in 50-kt headwinds and downdrafts exceeding 1,600 fpm)
- Supports deterministic runtime-assurance boundary for AI/algorithm safety
- Being matured in parallel under separately-funded NASA Phase II safe-autonomy effort

### NightFOX Payload (IR/Multispectral Fire Payload)
- Developed for NOAA CSL under FIREX-AQ
- Multispectral fire perimeter, fire radiative power, combustion-efficiency products
- Designed to feed fire weather forecasting
- Successfully flown on S2; transfers to S3 with documented mechanical/electrical interfaces

### Meteorological Probe
- NWS-approved for research-grade measurements
- 100-Hz sampling: pressure, temperature, humidity, 3-D wind, turbulence
- Field-proven in NOAA hurricane deployments
- Data suitable for WRF-SFIRE/CAWFE assimilation

### In-Situ Plume Payload
- Measures: CO₂, CO, aerosol, relative humidity, pressure, temperature
- FIREX-AQ heritage
- Supports fire-emissions science and model improvement

### Airspace-Awareness Package
- ADS-B In receiver
- Long-Range Remote ID receiver
- Software-defined radio for non-cooperative aircraft detection
- Recently demonstrated; enables coordination with manned aircraft and other UAS in wildfire TFRs

## Use Cases & Applications

**Primary Mission Phases (4 operational contexts):**

1. **Initial Attack**: First-on-scene fire perimeter mapping under extreme winds and mountain terrain; autonomous fire-and-forget perimeter mapping in adverse weather
2. **Extended Attack**: Persistent monitoring with multi-airframe handover; continuous fire perimeter and meteorological data delivery to incident command
3. **Second-Shift/Nighttime Suppression Support**: NightFOX IR enables night operations; all-weather autonomy enables sampling in conditions where crewed aircraft cannot operate
4. **Post-Fire Damage Assessment**: Multispectral mapping for burn severity and recovery monitoring

**Specific Applications:**
- **Fire Perimeter Estimation**: Autonomous following of active fire lines; delivery of real-time perimeter data to WFTAK/CoTAK Common Operating Picture (eliminates current 4+ hour latency from helicopter mapping or satellite stitching)
- **Fire Weather Profiling**: Autonomous sampling of wind, temperature, humidity, pressure in convective boundary layer; direct assimilation into WRF-SFIRE/CAWFE; demonstrated 8-hour forecast improvement on Marshall Fire
- **Persistent Monitoring**: Night and all-weather surveillance with multi-platform handover for continuous coverage
- **Incident Command Decision Support**: Calibrated data products published as COT messages for direct integration with WFTAK/CoTAK interfaces used by incident commanders
- **Plume Sampling**: In-situ combustion-product measurements (CO₂, CO, aerosol) for emissions science and smoke-impact modeling
- **Airspace Coordination**: Integration with NASA ACERO airspace management system and federated UTM; aircraft serves as communications relay over terrain

## Technical Objectives

**TO-1: Terrain- and Wind-Aware Autonomous Planning Algorithm (Phase I focal R&D)**
- Develop and validate in software-in-the-loop (SIL) a mission-planning algorithm fusing DEM, archived WRF-SFIRE/CAWFE wind, and synthetic 100-Hz onboard wind measurements
- Exercise across ≥3 representative scenarios per fire (Marshall and East Troublesome)
- Validate flyable routes with quantified deviation from baseline wind-agnostic planner
- Document interface for Phase II additions: Maxar real-time terrain refinement, real-time wind assimilation

**TO-2: Automated Fire-Line Mapping Algorithm — Phase I Scoping and De-Risking**
- Intentionally limited to enabling Phase II flight demonstration, not delivering it
- Characterize current practice through Boulder Emergency Squad engagement
- Define terrain, wind, comms, sensor-geometry inputs for Phase II implementation
- Generalize cyclone-interior controllers to fire objectives at algorithm-specification level
- Produce Phase II SIL implementation and flight test plan
- Scope companion primitives (updraft profiling, standoff loitering) at catalog level

**TO-3: Framework Architecture and Modular Interface Specification**
- Document SwiftCore avionics service contract
- Specify BST modular payload interface (mechanical, electrical, power, data-bus, COT schema)
- Enable porting of algorithms to non-BST airframes in Phase II/III
- Produce architecture document and reference interface implementation on BST S3

**TO-4: Phase II Transition Plan**
- Three sequential demonstrators in order of maturity:
  1. Automatic NWS-grade weather sampling with real-time forecast-model interfacing (first Phase II demo)
  2. Fire-line mapping flight demonstration (headline TRL-5 deliverable)
  3. Maxar real-time terrain/obstacle refinement integrated with TO-1 planner
- Identify operational testing partners: Boulder Emergency Squad, federal land managers, state forestry, utilities, ACERO partners

## Key Results

*Phase I is a proposal, not a completed report. No results are presented.*

**Phase I Success Criteria (defined in proposal):**
1. Terrain- and a priori-wind planning algorithm produces flyable routes in SIL across ≥3 Marshall/East Troublesome scenarios with quantified deviation from baseline
2. Fire-line mapping scoping delivers current-practice analysis, input/interface specification, algorithm-level controller generalization sufficient for Phase II SIL within first month of Phase II
3. Framework architecture documented to level where third-party developer could begin porting algorithms to non-BST airframe
4. Phase II plan approved by BST commercialization committee with ≥2 letters of intent from prospective operational/commercial users

**Phase I Deliverables (6-month program):**
- M1: Kickoff briefing
- M2: Concept of Operations v1.0
- M3: Tradeoff Analysis report
- M4: Terrain-and-wind-aware planner SIL validation (software + report)