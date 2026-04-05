# N251-016 Expendable Sonobuoy-Launched Unmanned Aerial Vehicle for ASW Cued Search, Detection, Tracking, and Classification – Phase I Internal Meeting

## Document Metadata
- Type: Internal meeting presentation
- Client/Agency: U.S. Navy
- Program/Solicitation: SBIR Phase I (N251-016)
- Date: October 30, 2025
- BST Products/Systems Referenced: S0 UAS, S1 UAS
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
This internal meeting reviewed Phase I progress on integrating a QuSpin QTFM Gen-2 magnetometer into BST's S0 UAS platform for anti-submarine warfare (ASW) detection and classification missions. The focus was on characterizing the aircraft's magnetic signature and demonstrating that on-board magnetometer integration is feasible without requiring the large spatial separations (booms/cables) typical of towed configurations.

## Technical Approach
- **Magnetometer Integration**: Mounted QuSpin QTFM Gen-2 directly on S0 UAS rather than towed configuration
- **Electromagnetic Noise Mitigation**: 
  - Ground testing at multiple distances (0 ft, 5 ft, 10 ft, 20 ft, 50 ft) to characterize platform magnetic signature
  - MuMetal magnetic shielding material sourced and planned for testing (reported to reduce motor magnetic field by up to 10x)
  - Frequency-space analysis to identify noise sources (motor throttle, aliasing, RF interference from 400 MHz ground station comms)
- **Testing Methodology**: Aircraft tested in off state, idle, and cruise power configurations in electromagnetically quiet environment (farm, away from roads/structures/power lines)

## Products & Capabilities Described

### S0 UAS
- Unmanned platform for magnetometer deployment
- Compact form factor compatible with sonobuoy-launched constraints
- Flight envelope permits close magnetometer proximity without degraded performance

### S1 UAS
- Referenced for flight analysis showing frequency-space noise during motor throttle events
- Demonstrates need for electromagnetic mitigation strategies

### QuSpin QTFM Gen-2 Magnetometer (Third-party Integration)
- **Specifications vs. Navy Requirements**:
  - Measurement Bandwidth: 500 Hz (exceeds 100 Hz requirement)
  - Measurement Range: 150 μT (exceeds 100 μT requirement)
  - Operating Temperature: -15 °C – 55 °C (exceeds 0 °C – 50 °C requirement)
  - MAD In-Air Noise Level: 3 pT/√Hz (exceeds 20 pT/√Hz requirement by 6.7x)
  - Heading Error: <3 nT uncompensated (meets requirement)
- **SWaP**:
  - Sensor head: 17.7 × 19.8 × 35.8 mm, 12 grams
  - ECU housing: 14.7 × 24.4 × 92.3 mm, 29 grams total (6.5 g without housing)
  - Power: +5 V (via SCB) or 10–12 V direct, 2.5 W nominal, 3.5 W startup

## Use Cases & Applications
- **Primary Mission**: Expendable sonobuoy-launched UAV for ASW cued search, detection, tracking, and classification
- **Magnetometer Application**: Detect and classify submarines via magnetic anomaly detection (MAD)

## Key Results

### Ground Testing Findings
1. **Magnetic Noise at Distance**:
   - **0 ft (aircraft on, cruise power)**: 767.4 pT RMS / 34.9 pT/√Hz noise (unacceptable)
   - **5 ft and beyond**: 29.9–32.3 pT RMS / 1.4–1.5 pT/√Hz noise (meets requirement of ≤20 pT/√Hz by 2× margin)
   - **Critical Insight**: No large spatial separation needed; 5 ft equivalence reduces design complexity vs. traditional towed MAD systems

2. **Noise Source Characterization**:
   - Primary electromagnetic interference: 400 MHz ground station communications (25% noise increase when transmitting)
   - Motor contribution: Only ~25% additional noise at 0 ft when throttling
   - Filter behavior: 10 Hz filter shows odd interference patterns with 400 MHz comms; filtering disabled for clearer data

3. **Frequency-Space Analysis** (S1 flight data):
   - High-frequency noise and aliasing observed during motor throttle-up
   - Aliasing identified as primary problem (low-pass filters insufficient to mitigate)
   - MuMetal shielding expected to reduce motor-induced magnetic field by up to 10x in forthcoming tests

### Confidence Assessment
- Preliminary results indicate **no requirement for boom/cable towed configuration**
- 5 ft spacing achieves noise floor equivalent to 50 ft, enabling compact sonobuoy-compatible design
- Magnetometer performance exceeds Navy specifications with margin for integration challenges
- Motor noise contribution is manageable; primary focus shifts to RF interference mitigation via shielding

## Notable Details
- **Design Innovation**: Elimination of boom/towed magnetometer configuration is critical for sonobuoy-launched deployment (size/weight constraints)
- **Testing Environment**: Carefully selected farm location to minimize environmental electromagnetic noise for accurate platform signature characterization
- **Phased Integration Plan**: MuMetal shielding testing deferred to later Phase I work
- **Known Issues**: 400 MHz ground station communications present interference; filter configuration and shielding strategy to be optimized
- **Margin**: Measured noise at 5 ft (1.4–1.5 pT/√Hz) is 13–14× better than Navy requirement (20 pT/√Hz), providing significant integration margin