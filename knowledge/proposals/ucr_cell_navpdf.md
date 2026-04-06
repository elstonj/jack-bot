# Signals of Opportunity Aided Inertial Navigation

## Document Metadata
- Type: Academic research paper / conference preprint
- Client/Agency: University of California, Riverside (UCR); sponsored by Office of Naval Research (ONR)
- Program/Solicitation: ONR Grant N00014-16-1-2305
- Date: 2016 (preprint of ION GNSS+ Conference, September 12-16, 2016; document dated January 8, 2019 in this archive)
- BST Products/Systems Referenced: None directly—this is external research potentially relevant to BST capabilities
- Key Personnel: Joshua J. Morales, Paul F. Roysdon, Zaher M. Kassas (University of California, Riverside)

## Executive Summary
This paper presents a tightly-coupled framework that fuses inertial measurement unit (IMU) data with pseudorange observations from unknown terrestrial "signals of opportunity" (SOPs) to enable bounded-error inertial navigation when GNSS signals become unavailable. The framework operates in a mapping mode when GPS is available (to estimate SOP transmitter states) and a SLAM mode when GPS is lost (using SOPs alone to aid INS). Experimental results demonstrate a ground vehicle navigating with cellular tower signals achieving 59.9% RMSE reduction versus unaided INS.

## Technical Approach

### Core Framework
- **Integration Strategy**: Tightly-coupled Extended Kalman Filter (EKF) that simultaneously estimates:
  - Receiver states: position, velocity, attitude (quaternion), clock bias/drift, gyroscope and accelerometer biases
  - SOP transmitter states: 3D position, clock bias, clock drift
  
- **Two Operational Modes**:
  1. **Mapping Mode** (GNSS available): Fuses GNSS pseudoranges with SOP pseudoranges and IMU to refine SOP state estimates
  2. **SLAM Mode** (GNSS unavailable): Uses only SOP pseudoranges and IMU; tracks relative clock biases (receiver vs. each SOP)

### Dynamic Models
- **SOP Dynamics**: Stationary terrestrial transmitters with state vector [position, clock bias, clock drift]. Clock dynamics modeled using power-law coefficients (h-α) characterizing oscillator frequency stability.
- **Vehicle Dynamics**: 16-state INS (quaternion orientation, position, velocity, gyro/accel biases) plus 2-state clock model
- **IMU Measurement Model**: Gyroscope and accelerometer measurements corrupted by scale factor, bias, misalignment, quantization, random walk, and rate ramp errors (grades: consumer and tactical)

### Observation Models
- **SOP Pseudorange**: ρ = ||receiver_pos - SOP_pos|| + c(receiver_clock_bias - SOP_clock_bias) + noise
- **GNSS Pseudorange**: ρ = ||receiver_pos - satellite_pos|| + c(receiver_clock_bias - satellite_clock_bias) + compensated delays + noise

### Key Innovation
Treats SOP navigation as a SLAM-type problem where receiver simultaneously localizes itself and maps unknown SOP transmitter states, enabling navigation in GNSS-denied environments without pre-surveyed beacon locations.

## Products & Capabilities Described

### Signals of Opportunity (SOPs)
- **Definition**: Terrestrial RF transmitters not designed for navigation (cellular BTS towers, FM/AM radio, digital TV, iridium, Wi-Fi)
- **Application Context**: Supplement or replace GNSS in challenged environments (urban canyons, tunnels, jamming)
- **Measurement Type**: Pseudoranges extracted from received signals; clock states must be estimated dynamically
- **Performance Dependency**: Sensitive to oscillator quality (TCXO vs. OCXO); framework demonstrates bounded errors even with worst-case oscillators

### IMU Integration
- Consumer-grade MEMS IMU demonstrated to produce lower position estimation uncertainty than tactical-grade IMU when aided by 2-4 SOPs
- Framework accommodates varying IMU grades; error models account for noise sources per IEEE 1293-1998 standard

### Software-Defined Receiver (SDR)
- **MATRIX SDR**: Multichannel Adaptive TRansceiver Information eXtractor
- Simultaneous acquisition/tracking of GPS L1 C/A and cellular CDMA signals via universal software radio peripheral (USRP)
- Produces pseudorange observables from both GNSS and terrestrial sources

## Use Cases & Applications

### Demonstrated Scenarios
1. **Aerial Vehicle Navigation** (simulation): 200-second trajectory with climb and orbit maneuver; GPS loss at 100 seconds
2. **Ground Vehicle Navigation** (field experiment): 30-second run with GPS available for first 16 seconds; navigation using cellular tower (CDMA BTS) signals
3. **GNSS-Denied Urban/Indoor Operations**: SOPs abundant in environments where satellite signals unavailable
4. **Extended Navigation Post-GNSS-Loss**: Framework produces bounded position/velocity/attitude errors indefinitely, unlike unaided INS (which diverges quadratically)

### Key Performance Metrics
- **Simulation (Aerial Vehicle)**:
  - GPS-INS (tactical-grade IMU): position error diverges to ~150m+ after 100s GPS loss
  - SOP-aided INS (consumer IMU, 2-4 SOPs): error remains bounded at ~20-30m throughout 100-second GNSS-denied period
  
- **Field Experiment (Ground Vehicle, 14 seconds post-GPS-loss)**:
  - Unaided INS: 23.5m RMSE
  - SOP-aided INS (1 cellular tower): 9.42m RMSE (59.9% improvement)
  - Tower localization error: 15.5m (estimated position vs. true tower location)

## Key Results (for reports)

### Simulation Findings
1. **Superior Performance with SOP Aiding**: SOP-aided INS with consumer-grade IMU and 2-4 SOPs consistently outperforms traditional tightly-coupled GPS-INS with tactical-grade IMU in GNSS-denied mode
2. **Bounded Error Growth**: Unlike GPS-INS (which diverges when GNSS lost), SOP-aided framework establishes observable bounds on position, velocity, and attitude uncertainty
3. **Sensitivity to SOP Quantity**: Position and attitude estimation error covariance inversely proportional to number of exploited SOPs (M=2, 3, 4 tested)
4. **Sensitivity to SOP Quality**: 
   - Oscillator quality (TCXO vs. OCXO) has minimal impact during GPS availability
   - Significant sensitivity when GPS unavailable; best OCXO yields ~10-20x lower error variance than worst TCXO
   - Even worst-case oscillators permit bounded navigation

### Experimental Validation
- Software-defined receiver successfully extracted pseudoranges from cellular CDMA base station simultaneous with GPS L1 C/A
- Dual-antenna system enabled signal acquisition under dynamic vehicle motion
- 59.9% RMSE improvement over INS-only navigation using single SOP source (cellular tower)
- Framework observability sufficient to estimate 3D SOP transmitter location during mapping phase

## Notable Details

### Technical Distinctions
- **vs. Traditional SLAM**: SOP signal map is dynamic and stochastic (transmitter clocks drift), unlike static environmental maps
- **vs. Prior Work**: Paper [24] (MacDoran et al., 2013) used SOP Doppler for INS aiding; this work uses pseudoranges in tightly-coupled framework with detailed observability/performance characterization
- **GNSS Compensation**: Methodology for compensating ionospheric and tropospheric delays in GNSS pseudoranges; SOP delays treated as part of unknown transmitter clock states

### Framework Flexibility
- Modular design permits insertion of varying numbers of SOPs and GNSS satellites
- Clock state estimation framework generalizable to any RF source with estimated clock dynamics (power spectral density characterized by h-α coefficients)
- Extended Kalman Filter update equations scale with measurement quantity without requiring closed-form solutions

### Practical Considerations
- **IMU Grade Trade-off**: Consumer-grade IMU reduces cost/size/weight/power vs. tactical-grade but requires more SOP aiding to achieve bounded errors
- **Oscillator Stability**: Cellular and FM radio transmitters typically equipped with TCXO (adequate for bounded INS aiding); precision timing not prerequisite
- **Coverage**: SOPs abundant in GNSS-challenged urban/indoor environments where satellite signals weak/unavailable

### Experimental Hardware
- National Instruments USRP (two-channel, simultaneous GPS + cellular downmix)
- UCR Navigation System: consumer-grade MEMS IMU, tactical-grade IMU, u-blox GPS receiver (ground truth reference)
- MATLAB-based EKF filter, LabVIEW-based SDR backend

### Future Research Directions
- Observability analysis for optimal receiver trajectories during mapping phase
- Multi-receiver collaborative localization/mapping (mentioned but not detailed)
- Performance under multipath-rich urban channels
- Integration with additional sensor modalities (cameras, lidar)

---

**Note**: This document is academic research from UCR, not a Black Swift Technologies proposal or report. It is likely archived in BST's reference materials because it represents relevant prior work on signals of opportunity-based navigation, potentially informative for BST proposals or technical development in GNSS-denied navigation systems.