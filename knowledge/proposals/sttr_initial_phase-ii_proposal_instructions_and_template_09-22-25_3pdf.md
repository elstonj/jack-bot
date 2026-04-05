# Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- Type: STTR Phase II Initial Proposal
- Client/Agency: Office of Naval Research (ONR), U.S. Navy
- Program/Solicitation: Navy STTR Topic N25A-T025
- Phase I Contract: N6833525C0270
- Date: January 2, 2025
- BST Products/Systems Referenced: S0 UAS (unmanned aircraft system), S0-VTOL, S0-LR (long-range variant), S0-AD (air-deployed)
- Key Personnel: Dr. Jack Elston (PI/CEO), Dr. Joshua Wadler (Co-I, ERAU), Dr. Jun Zhang (Co-I, University of Miami), Dr. John Park (Co-I, Old Dominion University)

## Executive Summary
Black Swift Technologies proposes a Phase II effort to transition the S0 UAS from a NOAA-operational research platform into a Navy-integrated atmospheric profiling capability for hazardous weather observation, particularly tropical cyclones and cold maritime environments. The work spans 48 months (24-month base + 24-month option) with a total estimated cost of $1,940,958, structured to complete calibration/validation, advance onboard algorithms, and demonstrate forecast improvements in Navy operational models before fleet integration.

## Technical Approach

### Phase I Foundation
Phase I established:
- Sensing feasibility through past tropical cyclone data and controlled tower flights
- Core measurement validation using meteorological tower comparisons (ARM SGP 60 m tower, Lamont, Oklahoma)
- Performance requirements and test plans
- Advanced sensing capabilities for turbulence and sea surface state
- System design updates for cold-weather and icing conditions
- AI-based algorithm concepts for automated data collection

### Phase II Base Period Focus
Completing calibration and response characterization:
- Flight-relevant characterization of thermodynamic and wind sensing
- Real-time onboard execution of turbulence and wave-state algorithms
- Demonstrating measurable forecast improvements in Navy models (COAMPS-TC)
- Conducting extensive land-based validation flights

### Phase II Option Period Focus
Navy-specific integration and full operational capability path:
- Real-time data assimilation into Navy operational forecast models
- System hardening for icing and extreme cold conditions (-65°F)
- Integration with Navy Common Launch Tubes (CLT)
- Over-ocean validation and autonomous adaptive sampling demonstrations
- Ship and ground-based deployment concepts

## Products & Capabilities Described

### S0 UAS (Primary Platform)
**What it is:**
- Expendable, small unmanned aircraft system designed for atmospheric profiling in extreme environments
- Currently at TRL 9 in Category 5 hurricanes
- Proven operational platform with NOAA since 2023

**Sensing Suite (Target Accuracies):**
- Pressure: ±0.4 hPa (0.01s response time)
- Temperature: ±0.1°C (0.5s response time)
- Humidity: ±2% (0.3s response time)
- 3D Winds: ±0.2 m/s (0.01s response time)
- Sea Surface Temperature: ±0.3°C
- Wave Height: ±3% (Significant Wave Height)
- Mean Squared Slope: ±10%

**Performance Demonstrated:**
- 2-hour endurance in 2024-2025 missions (path to extension through propulsion improvements)
- Unit cost approximately $15,000 (10x reduction vs. dropsondes on cost-per-effective-profile basis)
- Can collect 2 hours of continuous data near air-sea interface vs. single profile from $1,000 dropsonde
- Capable of stepped-descent profiles, spiral ascent/descent maneuvers
- Ascent rates ~4 m/s, descent rates ~6 m/s

**Operational Validation Results (Phase I):**
- Wind measurement comparison at ARM SGP tower: mean differences within 0.50 m/s for all three wind components across 10 flights over 3 days
- Successfully reproduced variance and distribution of vertical velocity (turbulence capture)
- NOAA comparison with P-3 tail doppler radar and dropsondes showed "very good results"
- 19 S0 operated from NOAA WP-3D in 2024; 23 in 2025

### S0 Variants
**S0-VTOL:**
- Short-range shipboard operations variant
- Reusable UAS, significant cost reduction

**S0-LR (Long-Range):**
- Land-launched missions
- Flight time >12 hours
- Reusable UAS

**S0-AD (Air-Deployed):**
- Deployable from Navy aircraft (P-8, MH-60 compatibility planned)
- Can leverage Navy aircraft for rapid deployment at great distances
- Simplified operational logistics vs. dedicated launch/recovery crews
- Current certification on P-3; C-130 integration in progress

## Use Cases & Applications

### Primary Naval Mission
- Tropical cyclone profiling in hazardous conditions
- Polar low monitoring in cold maritime environments
- Maritime storm observation for Navy operational forecasting
- Force readiness and mission planning support

### Specific Operational Scenarios
- Hurricane observation at air-sea interface (demonstrated in Hurricanes Ernesto 2024, Melissa 2025, and others)
- Data assimilation into Navy COAMPS-TC forecast model
- Integration with P-8 and MH-60 platforms
- Ship-launched and ground-based independent deployment
- Multi-platform coordination (fleet-deployed UAS networks)

### Secondary/Dual-Use Applications
- NOAA hurricane and weather observations
- Wildland fire awareness (USFS, DOI)
- Disaster response (FEMA)
- Border security (DHS)
- Maritime wind farm siting
- Environmental research
- Precision agriculture

## Phase II Technical Objectives

### Objective 1: Calibration and Validation of S0 Base Sensing
Complete flight-relevant characterization of pressure, temperature, humidity, and 3D wind sensors to establish statistically defensible error bounds under representative operating conditions. Closes gap between research validation and operational acceptance. **Base period.**

### Objective 2: Real-Time Turbulence Sensing and Wave-State Algorithms
Transition Phase I algorithm frameworks from offline analysis to real-time onboard execution. Compute turbulence metrics (drag coefficient, momentum flux, turbulent kinetic energy) onboard in real time. Optimize wave-state Kalman filter for performance in heavy precipitation and cloud cover. **Base period maturation, Option period validation.**

### Objective 3: Demonstration of Forecast and Situational Awareness Improvements
Demonstrate operational value through real-time data assimilation and forecast impact studies in Navy models (COAMPS-TC). Focus on leveraging high-density thermodynamic observations in lowest 2 km to reduce track/intensity errors and improve near-surface structure. **Base period configuration, Option period real-time demos.**

### Objective 4: Severe Weather Enhancements for Cold and Icing Environments
Harden system for icing and extreme cold down to -65°F. Mitigation strategies: PTC heaters integrated into 3D-printed nose cone to keep pressure ports clear; Ice-X coatings on wings/propellers. Validation at NASA Glenn Icing Research Tunnel. **Option period.**

### Objective 5: Autonomous Adaptive Sampling
Advance from rule-based autonomy (center fixes, eyewall following) to closed-loop adaptive sampling using onboard AI. Machine-learning–based guidance algorithms dynamically update flight paths in real time to maximize information gain by targeting forecast-sensitive regions. **Base period simulation, Option period storm deployment.**

### Objective 6: Navy Integration and Path to Full Operational Capability
Adapt S0 for compatibility with Navy Common Launch Tubes (CLT) and existing aircraft/ship/ground-based deployment mechanisms. Leverage P-3 certifications and C-130 integration efforts to accelerate adoption on P-8 and MH-60. Initial demo flights with Navy/Air Force in Base period; deeper integration and FOC-enabling work in Option. **Both periods.**

## Phase II Work Plan Summary

### Base Period (24 months) Tasks

**B.1: Data Impact Study with Navy Models**
- Observing System Experiments (OSEs) quantifying S0 value in COAMPS-TC
- Data denial experiments comparing baseline vs. S0-assimilation forecasts
- Focus on track, intensity, surface winds, near-surface thermodynamics, boundary-layer structure
- **Milestone**: Quantitative assessment and technical report supporting Navy adoption
- Lead: Dr. Zhang

**B.2: Upgrade S0 Onboard Compute**
- Linux-based single-board computer integration with S0 avionics
- Support real-time turbulence and wave-state algorithms
- Interface with autopilot; support future AI-based guidance
- Build several prototypes as test vehicles
- **Milestone**: Upgraded S0 aircraft ready for Phase II testing

**B.3: Implement Turbulence Algorithms**
- Real-time onboard execution of Phase I algorithms using high-frequency wind data
- Initial validation during land-based flights, opportunistic testing during NOAA hurricane missions
- Deliverables: Flight datasets, algorithm performance analysis, technical report

**B.4: Land-Based In-Flight Validation**
- Extensive flight campaign near 2,000-ft NOAA meteorological tower in Colorado
- Characterize accuracy, response time, and uncertainty of pressure, temperature, humidity, wind measurements
- Collect statistically significant data across range of atmospheric conditions
- Two upgraded S0 aircraft dedicated to this effort
- **Milestone**: Datasheet of S0 sensing accuracy with error bounds for all sensed quantities

**B.5: Wave Height Algorithm**
- Refine radar-based Kalman filter for real-time Significant Wave Height (Hs) and Mean Squared Slope (MSS) estimation
- Tune using ONR SASCWATCH historical wave spectra data
- Target: Hs errors <3%, MSS errors <10%
- Deliverable: Validated real-time algorithm ready for operational testing

**B.6: AI-Based Autonomy in Simulation**
- Simulation-based validation using JSBSim environment
- Expand weather library for broader tropical cyclone structures via external weather servers
- Software-in-the-loop (SIL) evaluation of adaptive sampling algorithms
- Ensure compatibility with S0 avionics and safety constraints
- Demonstrate closed-loop mission execution maximizing information gain
- Deliverables: Simulation results and readiness for onboard testing

**B.7: Demo Mission with DoD** ⭐ **KEY MILESTONE**
- Fabricate two additional S0 aircraft with Phase II upgrades
- Conduct demonstration flights with Navy (preferred) or Air Force (backup)
- Generate operationally relevant datasets
- Identify remaining hardware, software, CONOPS gaps
- Deliverables: Flight data, demonstration report, lessons-learned assessment

### Option Period (24 months) Tasks

**O.1: Real-Time Data Assimilation into Navy Models** ⭐ **MILESTONE**
- Demonstrate real-time assimilation during representative field operations
- Ingest S0 thermodynamic and wind measurements into COAMPS-TC
- Focus on low-latency delivery, correct formatting, operational compatibility
- Evaluate forecast impacts (track, intensity, storm size, boundary layer height, eyewall slope, warm core characteristics, vertical velocity, convergence distributions)
- Deliverable: Documented real-time S0 data contribution to Navy forecast products

**O.2: Mitigating Aircraft Icing**
- Dual icing-mitigation strategies:
  - Active: PTC heaters in nose cone protecting pressure ports
  - Passive: NANOMYTE® SuperAi coatings on wings, tail, propeller
- Validation at NASA Glenn Icing Research Tunnel (IRT)
- Test across representative icing conditions (liquid water content, droplet sizes)
- Metrics: Sensor data continuity, aerodynamic degradation, visual ice accretion
- Avionics upgrades for heater control
- Deliverable: Final report supporting Navy operational approval in icing

**O.3: Extreme Cold Capability**
- Validate operation down to -65°F
- Environmental chamber evaluations and/or cold-weather field trials
- Assess sensor accuracy, battery discharge, processor performance, startup reliability
- Identify temperature-driven biases, latency increases, failure modes
- Deliverable: Validated operating envelope and mitigation strategies

**O.4: Integration of S0-AD with Navy Systems**
- Finalize mechanical, electrical, software interfaces