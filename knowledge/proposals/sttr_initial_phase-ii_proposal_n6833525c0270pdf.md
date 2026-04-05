# STTR Initial Phase-II Proposal: Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- **Type:** STTR Phase II Initial Proposal
- **Client/Agency:** U.S. Navy / Office of Naval Research (ONR)
- **Program/Solicitation:** Navy STTR Topic N25A-T025
- **Contract Number:** N6833525C0270 (Phase I)
- **Date:** January 2, 2025
- **BST Products/Systems Referenced:** S0 UAS (primary), S0-VTOL, S0-LR (long-range variants)
- **Key Personnel:** Dr. Jack Elston (CEO/PI), Dr. Jun Zhang (Co-I), Dr. Joshua Wadler (Co-I), Dr. John Park (Co-I)

---

## Executive Summary

Black Swift Technologies proposes to transition the S0 unmanned aircraft system from a proven NOAA research platform into an operational Navy capability for atmospheric profiling in hazardous weather. The S0 has successfully completed 19 deployments in 2024 and 23 in 2025 from NOAA's WP-3D aircraft, operating in Category 5 hurricane conditions. Phase II will complete sensor calibration and validation, mature real-time algorithms for turbulence and wave-state estimation, demonstrate forecast improvements in Navy models (COAMPS-TC), and harden the system for cold-weather and icing environments—establishing the foundation for full operational capability (FOC) and fleet integration.

---

## Technical Approach

### Core Platform: S0 UAS
- **Design Philosophy:** Expendable, air-deployed fixed-wing UAS optimized for rapid, targeted sampling in severe weather
- **Operational Maturity:** TRL 9 in Category 5 hurricanes; proven with 40+ deployments in 2024-2025
- **Endurance:** Currently 2 hours; incremental improvements targeted during Phase II
- **Cost Structure:** ~$15,000 unit cost, enabling 10x cost reduction per effective profile vs. dropsondes (~$1,000 each for single-use devices)

### Sensing Suite
**Base Thermodynamic & Wind Package:**
- 3D winds (3-axis measurements)
- Atmospheric pressure
- Temperature
- Humidity
- Sea surface temperature (SST)
- Wave height via radar

**Proposed Advanced Capabilities (Phase II):**
- Real-time turbulence algorithms (drag coefficient [C_D], momentum flux, turbulent kinetic energy)
- Wave-state estimation via Kalman filter (Significant Wave Height [H_s] and Mean Squared Slope [MSS])
- High-frequency wind data (up to 100 Hz) for boundary-layer turbulence characterization

### Onboard Computing Upgrade
- Linux-based single-board computer (SBC) integration with avionics
- Enables real-time execution of turbulence and wave-state algorithms
- Future support for AI-based autonomous guidance

### Data Assimilation & Forecasting Integration
- Phase I demonstrated successful assimilation into NOAA forecast models (Hurricane Analysis and Forecast System)
- Phase II targets Navy's Coupled Ocean/Atmosphere Mesoscale Prediction System–Tropical Cyclone (COAMPS-TC)
- Data compatible with modern data assimilation frameworks
- Goal: Improve track, intensity, and boundary-layer structure forecasts

---

## Products & Capabilities Described

### S0 UAS (Air-Deployed Variant - Primary Focus)
**What it is:**
- Small, expendable fixed-wing UAS designed for deployment from manned aircraft (P-3, P-8, C-130, MH-60)
- Autonomous flight management with rule-based autonomy (center fixes, eyewall following)
- Onboard storage and telemetry for data transmission

**Proposed Use in This Context:**
- Rapid deployment to hazardous weather regions (tropical cyclones, polar lows, maritime storms)
- Extended loitering near air-sea interface (lowest 2 km) for continuous profiling
- Profiles executed via stepped descent (~10 min per altitude level) or spiral ascent/descent (4 m/s ascent, 6 m/s descent)
- Supports Navy's need for persistent, scalable atmospheric observations without risking crewed aircraft

**Specifications & Performance Claims:**
- **Pressure:** ±0.4 hPa accuracy, 0.01 s response time
- **Temperature:** ±0.1°C accuracy, 0.5 s response time
- **Humidity:** ±2% accuracy, 0.3 s response time
- **3D Winds:** ±0.2 m/s accuracy, 0.01 s response time
- **SST:** ±0.3°C accuracy
- **Wave Height:** ±3% accuracy
- **Mean Squared Slope:** ±10% accuracy
- **Endurance:** 2 hours demonstrated; credible path to extension
- **Wind Tolerance:** Successfully operated in Category 5 hurricanes (tested in Hurricane Milton: 209 kt horizontal winds, 30 m/s vertical velocities)
- **Temperature Range (Phase II Goal):** -65°F for cold/polar operations

### S0-VTOL (Vertical Takeoff/Landing Variant)
**What it is:**
- Reusable variant for short-range shipboard operations
- Enables launch/recovery from ships without dedicated facilities

**Proposed Use:** Option phase evaluation; lower priority than air-deployed variant for Navy applications

### S0-LR (Long-Range Variant)
**What it is:**
- Reusable variant for land-based missions
- Flight time >12 hours

**Proposed Use:** Option phase evaluation; lower priority than air-deployed variant for Navy applications

---

## Use Cases & Applications

### Primary: Navy Hazardous Weather Operations
1. **Tropical Cyclone (TC) Profiling**
   - Real-time boundary-layer characterization during storm intensification
   - Multiple S0s deployed during single mission (e.g., 4 S0s during Hurricane Ernesto with stepped-descent pattern)
   - Direct support for track and intensity forecasting

2. **Cold Maritime Environments**
   - Polar lows and rapidly evolving maritime storms
   - Arctic operations (Phase II/Option objective)
   - Extended to -65°F operations

3. **Situational Awareness & Decision Support**
   - Integration with Navy operational forecast models
   - Near-real-time data assimilation into COAMPS-TC
   - Enhanced surface wind, temperature, and boundary-layer structure estimates for fleet operations

### Secondary (Phase I Validation / Dual-Use):
- **NOAA Hurricane Research:** 19-23 deployments per season; data assimilation into HAFS (operational by June 2026)
- **Air-Sea Interaction Research:** Validation against instrumented towers, dropsondes, radar, ocean arrays
- **Civilian/Commercial:** Wind farm siting, environmental monitoring, disaster response

---

## Technical Objectives & Phase II Work Plan

### Base Period (24 months) – Data Credibility & Initial Navy Demos

**Objective 1: Calibration & Validation of S0 Base Sensing**
- Execute comprehensive flight-relevant characterization of thermodynamic and wind sensors
- Test matrix covering response time, lag, cross-sensitivities, and uncertainty
- Validation flights near 2,000-ft NOAA meteorological tower in Colorado
- Deliverable: S0 sensing accuracy datasheet with error bounds

**Objective 2: Real-Time Turbulence Sensing & Wave-State Algorithms**
- Transition Phase I algorithms from offline analysis to onboard real-time execution
- High-frequency wind data (up to 100 Hz) processing
- Compute turbulence metrics: C_D, momentum flux, turbulent kinetic energy
- Optimize radar-based Kalman filter for H_s and MSS in heavy precipitation/cloud

**Objective 3: Demonstration of Forecast & Situational Awareness Improvements**
- Observing System Experiments (OSEs) with Navy COAMPS-TC model
- Data denial experiments comparing baseline forecasts to S0-assimilated runs
- Focus on track, intensity, surface winds, near-surface thermodynamics, boundary-layer structure

**Objective 4: Severe Weather Enhancements for Cold & Icing (Deferred to Option)**
- Hardware design only in Base; full testing in Option

**Objective 5: Autonomous Adaptive Sampling**
- Simulation-based validation of closed-loop AI guidance using BST's JSBSim environment
- Algorithm development to maximize information gain via real-time flight path updates
- Software-in-the-loop (SIL) testing for avionics compatibility

**Objective 6: Navy Integration & Path to FOC (Base + Option)**
- Mechanical, electrical, and software interfaces for Navy Common Launch Tubes (CLT) and A-size sonobuoy canisters
- Leverage existing P-3 certifications and C-130 integration
- Support transition to P-8 and MH-60 platforms
- CONOPS documentation for Navy-specific deployment scenarios

### Option Period (24 months) – Navy-Specific Integration & Full Operational Capability

**Task O.1: Real-Time Data Assimilation into Navy Models**
- Operational demonstration during field operations
- Low-latency data delivery, correct formatting, compatibility with COAMPS-TC
- Evaluate forecast impacts (track, intensity, storm structure metrics)

**Task O.2: Mitigating Aircraft Icing**
- Dual strategy: positive temperature coefficient (PTC) heating in nose cone + passive NANOMYTE® SuperAi coatings
- Validation at NASA Glenn Icing Research Tunnel
- Performance metrics: sensor data continuity, aerodynamic degradation, ice accretion

**Task O.3: Extreme Cold Capability**
- System validation down to -65°F
- Environmental chamber and/or cold-weather field trials
- Assessment of sensor accuracy, battery performance, processor reliability under sustained cold

**Task O.4: Integration of S0-AD with Navy Systems**
- Finalize mechanical/electrical/software interfaces for Navy Common Launch Tubes
- Adapt to Navy A-size sonobuoy canisters
- "Headless" operation for autonomous mission execution
- Updated CONOPS for Navy deployment scenarios

**Task O.5: Over Ocean Validation**
- Extended over-ocean flight testing in representative maritime environments
- Metrics: wind/thermodynamic data quality, communications reliability, autonomous execution
- Milestone demonstrating fleet deployment readiness

**Task O.6: AI-Based Autonomy in a Storm**
- Onboard execution of adaptive sampling during actual storm deployments
- Real-time autonomous targeting of high-value sampling regions
- Evaluation of responsiveness, stability, and scientific prioritization

**Task O.7: Ship & Ground-Based S0 Operational Concepts**
- Demonstrate launch/recovery from ships and austere ground sites
- Alternative deployment concepts for distributed operations
- Emphasis on minimal infrastructure and rapid deployment

---

## Key Results from Phase I (Completed)

### Sensing Performance Validation
- **Wind Measurement:** Comparison with ARM Southern Great Plains 60m tower (10 flights over 3 days) showed mean differences <0.50 m/s for all three wind components; S0 reproduced boundary-layer turbulence variance and vertical velocity distribution
- **Multi-Source Comparison:** NOAA validation against P-3's tail Doppler radar and various dropsonde types showed "very good results"
- **Operational Heritage:** 42 S0 units deployed across 2024-2025 hurricane seasons; performed reliably in extreme conditions (Hurricane Milton: 209 kt winds, 30 m/s vertical velocity)

### Algorithm Development
- Turbulence metrics formulation completed (Phase I offline analysis)
- Radar-based Kalman filter framework developed for wave-state estimation (H_s, MSS)
- Phase I CONOPS and simulation frameworks established

### System Maturity Assessment
- TRL 9 in Category 5 hurricanes
- Ready for hardware upgrades (onboard compute) and algorithm transition to real-time execution
- Data integration pathways demonstrated with NOAA HAFS (full operational assimilation by June 2026)

---

## Commercialization & Transition Plan

### Navy Stakeholder Engagement
- Outreach to PMW 120 (Battlespace Awareness), PEO (U&W), PMA-298 (Mission Integration), PMA-266 (Multi-Mission Tactical UAS), PMA-263 (Small Tactical UAS), PMA-262 (Persistent Maritime UAS), PMA-268 (Unmanned Carrier