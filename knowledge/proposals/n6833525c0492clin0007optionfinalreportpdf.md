# Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking, and Classification

## Document Metadata
- **Type:** SBIR Phase I Option Period Final Report
- **Client/Agency:** U.S. Department of the Navy / Naval Air Systems Command (NAVAIR)
- **Program/Solicitation:** SBIR Topic N251-016
- **Contract Number:** N6833525C0492
- **Period of Performance:** March 23, 2026 – September 28, 2026
- **BST Products/Systems Referenced:** S0 UAS (expendable sonobuoy-launched unmanned aerial system), QuSpin QTFM Gen-2 magnetometer, Bartington UAS-MAG fluxgate magnetometer
- **Key Personnel:** 
  - Dr. Jack Elston (Principal Investigator)
  - Dr. Maciej Stachura (Report prepared by)
  - Meredith Needham (Corporate Official)
  - TPOC: Angel Ruiz-Reyes (Navy)

## Executive Summary

The Phase I Option Period matured Black Swift Technologies' sonobuoy-launched S0 UAS platform from a static magnetometer feasibility demonstration into a flight-validated magnetic anomaly detection (MAD) system. BST successfully characterized an integrated QuSpin QTFM Gen-2 optically pumped magnetometer on the S0 airframe, identified and isolated a dominant telemetry-transmitter noise source, demonstrated in-flight compensation achieving sub-3 nT crossover spread, and developed a reusable ground-launch rail for repeated magnetometer flight testing. The integrated aircraft meets the Navy's 20 pT/√Hz noise requirement from 0.1–30 Hz with the telemetry transmitter isolated.

## Technical Approach

### Magnetometer Performance Requirement & Evaluation
- **Requirement:** 20 pT/√Hz amplitude spectral density (ASD) or better over 0.01–100 Hz band
- **Testing Method:** Two-magnetometer differential ground tests using identical QuSpin sensors (aircraft-mounted and ground-reference) to separate platform noise from geomagnetic variation
- **Frequency Resolution:** Welch spectral estimation with 262-second Hann-windowed segments, 50% overlap (0.0038 Hz resolution)
- **Analysis:** Reported as median and power-additive ASD across seven frequency sub-bands

### Sensor Configuration
- **Primary Sensor:** QuSpin QTFM Gen-2 optically pumped magnetometer (hybrid vector mode)
  - Scalar output at 250 Hz
  - Three vector components at 83.3 Hz each
  - Quiet zero-crossing setting (ZC200), all internal filters disabled
  - Vector mode selected for direct Tolles-Lawson aeromagnetic compensation capability
- **Secondary Sensor:** Bartington UAS-MAG fluxgate magnetometer (alternate, under integration)
  - Interfaced over DroneCAN with limited 16-bit output resolution
  - BST designed dedicated 24-bit ADC acquisition board (ADS131M08 Texas Instruments) to overcome quantization issues
  - Separate power rails with ultra-low-noise regulators

### Magnetometer Mount Design
- **Location:** Phenolic tube boom extended ahead of S0 nose
- **Standoff Distances:**
  - 112 cm from motor
  - 95 cm from 433 MHz antenna
  - 30 cm from autopilot
- **Isolation:** Soft-mounted through neoprene foam to absorb mechanical vibrations
- **Materials:** Non-magnetic components (nylon, PLA) throughout boom
- **Data Logging:** Raspberry Pi running BST's quspin_split logger; zero sample loss across ~0.9 million samples per hour

### Reusable Flight-Test Aircraft & Launch Rail
- **Configuration:** Lightened S0 variant with reinforced carbon-composite wings for repeated belly landings
- **Battery:** Reduced from 6S 6,500 mAh to 6S 2,000 mAh (~350 g weight savings, 30% wing-loading reduction)
- **Endurance:** ~30 minutes (down from standard, but adequate for data collection)
- **Launch System:** Passive elastic rail (no active components)
  - 2.5 m aluminum extrusion
  - Two extra-extension springs with 2:1 pulley system
  - Design: 10.6 g peak acceleration, 16.7 m/s predicted exit velocity
  - **Actual Performance:** 10.7 g peak, 18.7–18.8 m/s exit velocity (exceeds 16 m/s requirement)
  - Stroke duration: ~0.26–0.30 seconds
  - Portable, fits in checked luggage

### Noise Source Identification & Isolation
- **Dominant Platform Noise:** 433 MHz telemetry transmitter supply current
  - Produces 0.9–1.2 nT square-wave pulses at magnetometer
  - Regular pulse train: ~2.2 pulses/second, 128 ms nominal duration
  - Creates comb of spectral lines 0.3–10 Hz
  - Localized to autopilot; corrective wiring changes recommended
  - **With radio isolated:** Aircraft residual drops to 9–14 pT/√Hz (median) from 0.1–30 Hz, meeting requirement
- **Secondary Noise Sources:**
  - Motor spectral lines shift above 10–100 Hz band at high cruise throttle
  - Meets 20 pT/√Hz at 112 cm (low cruise) and 148 cm (high cruise) standoff
  - At cruise power, motor contribution is confined to 30–100 Hz band; below 30 Hz motor off/on produce negligible difference with radio off
  - Aircraft pitch oscillation at 0.66 Hz (~4° RMS, 24 nT/√Hz)

### Ground Testing Protocol
- **24 September 2026:** All avionics powered, motor off, telemetry on
  - 65 minutes logged
  - Aircraft/reference spacing: 5 m
  - Identified dominant telemetry transmitter pulses
- **25 September 2026:** Two sequential hour-long tests with telemetry off
  - Motor off: baseline (65 min)
  - Motor on at cruise: propulsion characterization (61 min)
  - Time-alignment using geomagnetic coherence in 5-minute windows
- **18 September 2026:** Endurance validation
  - T2M0-00SE: 61.6 minutes unbroken, 0.0008% sample loss

### Flight Testing & In-Flight Compensation
- **Calibration Pattern:** Crossover star (eight 400 m passes on cardinal & diagonal headings through common point) + orbits (150 m and 300 m radius, both directions)
- **Conditions:** Fixed 1,649 m MSL (400 ft AGL), 21.9 m/s median airspeed, ~4 m/s wind
- **Compensation Method:** Tolles-Lawson aeromagnetic model using aircraft's direction cosines
  - **Direction Source 1:** Autopilot attitude + local field direction
  - **Direction Source 2:** QuSpin vector channel (in-flight calibrated, 12 parameters, 0.99–1.01 scale factors)
- **Model Terms Tested:** Permanent magnetic moment, induced fields, eddy currents, battery current, telemetry pulse state
  - Permanent-moment terms with QuSpin vector generalize best via cross-validation

## Products & Capabilities Described

### S0 UAS (Sonobuoy-Launched Variant)
- **Purpose:** Expendable, air-deployed anti-submarine warfare platform launched from P-8A sonobuoy launch container
- **Folded Configuration:** Fits LAU-126A sonobuoy launch container under 39 lb limit
- **Propulsion:** Electric motor with tuned throttle schedule to place motor spectral lines above 10–100 Hz band
- **Variants:**
  - S0-MAD: Carries high-sensitivity magnetometer
  - S0-Acoustic: Carries passive hydrophone/E-field acoustic suite
- **Unclassified Status:** At rest, remains unclassified
- **Ground-Launch Version (Phase I Option):**
  - Reusable, structurally reinforced airframe
  - 30-minute endurance with 2,000 mAh battery
  - Representative magnetic signature to air-deployed S0

### QuSpin QTFM Gen-2 Optically Pumped Magnetometer
- **Frequency Response:** 0.01–100+ Hz measurement band
- **Output Modes:** Scalar (250 Hz) and hybrid vector (83.3 Hz per axis)
- **Measured Performance (Ground, Motor Off, Radio Isolated):**
  - **0.1–30 Hz:** 9–12 pT/√Hz median, 10–16 pT/√Hz power-additive → **Meets 20 pT/√Hz requirement**
  - **Below 0.1 Hz:** Dominated by natural geomagnetic variation; base-station correction reduces 3–11×
  - **Vector Calibration:** 12-parameter (bias, scale, cross-axis); 0.18° systematic direction error, 0.014° random direction noise (1 s)
  - **Sensor Heads Used:** T2M0-00SE (aircraft), T2M0-00CX (ground reference)
- **In-Flight Performance (Compensated):**
  - Crossover spread: 64 nT (raw) → 2.1 nT (compensated) = within 3 nT target
  - Residual RMS over 14.7-min flight: 1.7 nT (QuSpin vector compensation) vs. 2.8 nT (autopilot attitude)
  - **Key Advantage:** Vector channel provides superior direction cosines vs. aircraft attitude solution (4.5° median difference)

### Bartington UAS-MAG Fluxgate Magnetometer
- **Integration Status:** Partial; designed custom 24-bit acquisition board in this phase
- **Issue Identified:** DroneCAN interface limited to 16-bit output (inadequate quantization for requirement)
- **BST Solution:** ADS131M08 24-bit ADC with:
  - Dedicated analog and digital power supplies
  - Ultra-low-noise, high-PSRR regulators
  - Direct differential analog sensing
  - Informed by NAWCAD reference designs
- **Status:** Two additional Government-furnished units shipped July 2026; designed approach established, further qualification pending Phase II

### Elastic Launch Rail
- **Design Parameters:** Spring rate, preload, rail length, launch angle optimized via parametric model
- **Components:** 2.5 m aluminum extrusion, two extra-extension springs, 2:1 pulley (springs below rail)
- **Design Performance:** 10.6 g peak, 16.7 m/s exit velocity
- **Validated Performance:**
  - 10.7 g peak (matches design)
  - 18.7–18.8 m/s exit (12% above design, exceeds 16 m/s Navy requirement)
  - MAD-equipped aircraft: 8.6 g peak, 17.3 m/s exit
- **Passive Design:** No active components; meets ~10 g sonobuoy-tube deployment load profile
- **Portability:** Fits checked luggage

## Use Cases & Applications

### Anti-Submarine Warfare (ASW) Cued Search
- **Mission Profile:** Expendable UAS deployed from P-8A Poseidon maritime patrol aircraft via sonobuoy launcher
- **Search Function:** Airborne magnetic anomaly detection for submerged contact localization and classification
- **Target Detection:** Designed for ferromagnetic submarines at ranges of interest (10–200 m closest approach)
- **Operational Environment:** Over deep ocean (telemetry/platform noise reduced; geomagnetic variation lower than land site)

### Magnetic Anomaly Detection (MAD) Sensor Platform
- **Frequency Band of Interest:** Below 1–3 Hz for target signals at S0 cruise speeds; upper band (above 5 Hz) serves as integrity monitor and alias guard
- **Typical Target Signatures (Dipole Model at 30 m/s airspeed):**
  - 10 m closest approach: 