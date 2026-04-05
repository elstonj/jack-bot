# STTR Initial Phase II Proposal: Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- **Type:** STTR Phase II Initial Proposal
- **Client/Agency:** U.S. Navy, Office of Naval Research (ONR)
- **Program/Solicitation:** Topic #N25A-T025 (Expendable Air-sea Profiling Observations in Hazardous Weather Conditions)
- **Date:** January 2, 2025
- **BST Products/Systems Referenced:** S0 UAS (unmanned aircraft system), S0-VTOL, S0-LR (long-range variant), S0-AD (air-deployed variant)
- **Key Personnel:** Dr. Jack Elston (PI/CEO), Dr. Joshua Wadler (Co-I, ERAU), Dr. Jun Zhang (Co-I, University of Miami), Dr. John Park (Co-I, Old Dominion University)

## Executive Summary
Black Swift Technologies proposes a Phase II effort to transition the S0 unmanned aircraft system from a NOAA-operational research platform into a Navy-adoptable atmospheric profiling capability for hazardous weather environments, including tropical cyclones and cold maritime conditions. Building on Phase I validation that demonstrated S0 wind measurements within 0.50 m/s of reference tower data and successful deployments in the 2024-2025 hurricane seasons (19-23 aircraft deployed from NOAA P-3), Phase II will complete calibration and validation, mature real-time algorithms for turbulence and wave-state sensing, demonstrate forecast improvements in Navy operational models (COAMPS-TC), and harden the system for icing and extreme cold conditions. The 24-month Base period ($971,990) plus optional 24-month extension ($968,448) will validate the S0's operational utility and establish a path to full operational capability (FOC) for Navy maritime and expeditionary deployments.

## Technical Approach

### Core Technical Strategy
BST proposes a structured, spiral-development approach to validate and operationalize the S0 UAS for Navy hazardous-weather operations:

1. **Sensor Validation & Calibration** – Execute detailed flight-test matrix comparing S0 measurements (pressure, temperature, humidity, 3D winds, sea-surface temperature, wave height) against independent references (meteorological towers, dropsondes, buoys, ocean arrays, NASA Glenn Icing Research Tunnel) to establish statistically defensible error bounds and response-time characterization under dynamic flight conditions.

2. **Algorithm Maturation** – Transition Phase I prototype algorithms from offline post-flight analysis to real-time onboard execution:
   - Turbulence metrics (drag coefficient, momentum flux, turbulent kinetic energy) computed onboard in real-time using high-frequency (up to 100 Hz) wind data
   - Radar-based Kalman filter for Significant Wave Height (Hs) and Mean Squared Slope (MSS) optimized for heavy precipitation and cloud cover
   - Both algorithms validated in land-based flight campaigns before deployment in operational storms

3. **Forecast Impact Demonstration** – Conduct Observing System Experiments (OSEs) assimilating S0 high-density thermodynamic observations (lowest 2 km) into Navy forecast models (COAMPS-TC) to quantify reductions in track, intensity, and boundary-layer structure errors compared to baseline assimilation of traditional observational data.

4. **System Hardening & Environmental Adaptation**:
   - **Icing Mitigation:** Integrated PTC (positive temperature coefficient) heating within 3D-printed nose cone to protect pressure ports; passive NANOMYTE® SuperAi coatings on wings, tail, and propeller; validation at NASA Glenn Icing Research Tunnel
   - **Cold Weather:** Environmental chamber and field testing to validate reliable operation at −65°F with assessment of sensor accuracy, battery discharge, processor performance, and startup reliability

5. **Navy Integration & Logistics** – Adapt S0 for compatibility with Navy Common Launch Tubes (CLT), sonobuoy canisters, and existing aircraft platforms (P-8, MH-60, C-130); develop Navy-specific CONOPS for headless autonomous operation; demonstrate ship-based and ground-based launch concepts.

6. **Autonomous Adaptive Sampling** – Advance from rule-based autonomy (center fixes, eyewall following) to closed-loop AI-based adaptive sampling using machine-learning guidance algorithms that dynamically target high-forecast-sensitivity regions in real time.

### Key Technical Specifications & Performance Targets

| Parameter | Target Accuracy | Response Time | Validation Method |
|-----------|-----------------|----------------|-------------------|
| Pressure | 0.4 hPa | 0.01 s | Dropsondes, towers, ocean arrays |
| Humidity | 2% | 0.3 s | Dropsondes, towers, ocean arrays |
| Temperature | 0.1°C | 0.5 s | Dropsondes, towers, ocean arrays |
| 3D Winds | 0.2 m/s | 0.01 s | Dropsondes, towers, TDR, dynamic wind tunnel |
| Sea Surface Temp | 0.3°C | N/A | Floating buoys, ocean arrays |
| Wave Height (Hs) | 3% error | N/A | Ocean arrays |
| Mean Squared Slope | 10% error | N/A | Ocean arrays |

### Phase I Validation Results (Foundation for Phase II)
- **Tower Comparison:** S0 wind measurements at ARM SGP 60-m tower (Lamont, OK) showed mean differences <0.50 m/s across all three wind components over 10 flights in 3 days; successfully resolved boundary-layer turbulence and variance distribution
- **NOAA P-3 Comparison:** S0 data compared favorably against P-3 tail Doppler radar and multiple dropsonde types
- **Operational History:** 19 S0 UAS deployed from NOAA WP-3D in 2024; 23 in 2025; demonstrated 2-hour endurance with credible path to further extension; recovered full storm evolution data from Hurricane Melissa (12 missions)

## Products & Capabilities Described

### S0 UAS (Primary Product)
**What it is:** Small, expendable, air-deployable unmanned aircraft system designed for atmospheric profiling in extreme weather (tropical cyclones, polar lows, maritime storms). Operates at TRL 9 in Category 5 hurricane environments.

**Phase I Proven Capabilities:**
- Continuous near-air-sea-interface observations for ~2 hours per sortie (demonstrated in 2025, extensible)
- Stepped-descent, spiral ascent/descent profiling patterns; typical ascent rates ~4 m/s, descent rates ~6 m/s
- Real-time data streaming compatible with Navy data assimilation frameworks
- Autonomous flight management reducing operator burden
- Cost-effectiveness: ~$15,000 per unit at ~10× cost reduction compared to dropsondes (vs. ~$1,000 per single-use dropsonde yielding <5 minutes data)

**Phase II Development Focus:**
- Upgrade onboard computational architecture with Linux-based single-board computer (SBC) to enable real-time execution of turbulence and wave-state algorithms
- Integrate icing mitigation hardware (PTC heaters, Ice-X coatings)
- Validate in cold-weather environments (−65°F)
- Adapt for Navy Common Launch Tubes and existing aircraft platforms (P-3, C-130, P-8, MH-60)
- Enable autonomous adaptive sampling via onboard AI guidance

**Deployment Variants Proposed:**
- **S0-AD (Air-Deployed):** Launched from Navy aircraft (P-8, MH-60, C-130) for rapid far-range deployment; identified as highest-value for Navy operational logistics
- **S0-VTOL:** Short-range shipboard operations capability
- **S0-LR (Long-Range):** Land-launched missions with 12+ hour endurance

### Advanced Sensing Payloads (Phase II Additions)
- **Turbulence Sensors:** High-frequency (100 Hz) wind measurement suite for real-time computation of drag coefficient (CD), momentum flux, and turbulent kinetic energy
- **Wave-State Radar:** Radar-based Kalman filter system for Significant Wave Height (Hs) and Mean Squared Slope (MSS) estimation optimized for precipitation/cloud scenarios
- **Icing/Cold-Weather Hardening:** Internal PTC heaters within pressure-port nose cone; NANOMYTE® SuperAi passive anti-ice coatings

## Use Cases & Applications

### Primary Navy Use Cases
1. **Tropical Cyclone Operations** – Real-time boundary-layer profiling during hurricane reconnaissance missions to improve track/intensity forecasts and characterize air-sea exchange in Category 1–5 conditions; continuous loitering capture of turbulence and coherent structures unresolvable by ballistic dropsondes.

2. **Cold Maritime & Polar Operations** – Atmospheric profiling in polar lows and extreme-cold maritime storms; Navy expeditionary operations in arctic and sub-arctic environments (validated down to −65°F).

3. **Rapid Force Projection** – Air-deployed S0-AD launched from P-8 or MH-60 platforms to conduct rapid environmental assessment at great distances from the fleet without requiring dedicated launch/recovery crews; supports decentralized naval operations.

4. **Shipboard/Forward-Deployed Operations** – S0-VTOL and ground-based variants for short-notice atmospheric sensing from ships or austere shore locations, minimizing infrastructure requirements.

5. **Forecast Impact & Decision Support** – Real-time data assimilation into Navy operational models (COAMPS-TC) to reduce forecast errors in storm track, intensity, boundary-layer structure, and surface winds; improved situational awareness for force-protection decisions.

### Dual-Use/Commercial Applications
- **NOAA Hurricane Operations** – Currently operational; slated for assimilation into NOAA HAFS (Hurricane Analysis and Forecast System) beginning 2026
- **Wildland Fire Awareness** – USFS and DOI deployments
- **Disaster Response** – FEMA applications
- **Border Security** – DHS operations
- **Commercial Wind Farm Siting** – Maritime and land-based wind resource assessment
- **Environmental Research & Precision Agriculture**

## Phase II Work Plan & Deliverables

### Base Period (24 months, $971,990)

| Task | Objective | Key Deliverables |
|------|-----------|------------------|
| **B.1: Data Impact Study with Navy Models** | Quantify S0 observation value in Navy forecast models (COAMPS-TC) via Observing System Experiments (OSEs); compare baseline vs. S0-assimilation forecasts on track, intensity, boundary-layer structure | Quantitative assessment of forecast skill improvements; technical report for Navy forecaster adoption; **MILESTONE** |
| **B.2: Upgrade S0 Onboard Compute** | Integrate Linux-based single-board computer (SBC) with S0 avionics and sensing core to enable real-time turbulence/wave-state algorithm execution; support future AI-based guidance | Upgraded S0 airframe with additional avionics interfaces; multiple test vehicles fabricated; **KEY MILESTONE** |
| **B.3: Implement Turbulence Algorithms** | Transition Phase I turbulence metric algorithms (drag coefficient, momentum flux, turbulent kinetic energy) from offline analysis to real-time onboard execution using 100 Hz wind data | Flight datasets; algorithm performance analysis under dynamic conditions; technical report on real-time validation |
| **B.4: Land-Based In-Flight Validation** | Extensive flight campaign near NOAA 2,000-ft Colorado meteorological tower to characterize S0 pressure, temperature, humidity, 3D wind accuracy/response-time under dynamic conditions; statistically significant dataset across atmospheric range | **S0 SENSING ACCURACY DATASHEET** with error bounds for all measured quantities; multiple vertical profiles & multi-point comparisons |
| **B.5: Wave Height Algorithm** | Refine radar-based Kalman filter (Phase I) for real-time estimation of Significant Wave Height (Hs) and Mean Squared Slope (MSS); tune using historical ONR SASCWATCH wave spectra; optimize for heavy precipitation/cloud cover | Validated real-time algorithm ready for field testing; target Hs errors <3%, MSS errors <10% |
| **B.6: AI-Based Autonomy in Simulation** | Validate adaptive sampling autonomy algorithms (Phase I) in BST's JSBSim simulation environment using expanded tropical-cyclone weather library; software-in-the-loop (SIL