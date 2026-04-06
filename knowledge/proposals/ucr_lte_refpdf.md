# LTE Navigation for UAVs: Signals of Opportunity Reference Article

## Document Metadata
- Type: Technical research article / reference material
- Source: GPS World Magazine, April 2017
- Client/Agency: Not applicable (academic research article)
- Program/Solicitation: Funded by Office of Naval Research (ONR Grant N00014-16-1-2305) and National Science Foundation (NSF Grant 1566240)
- Institution: University of California, Riverside (UCR) - Autonomous Systems Perception, Intelligence, and Navigation (ASPIN) Laboratory
- Key Personnel: Zaher M. Kassas (Director, ASPIN Lab), Joshua J. Morales, Kimia Shamaei, Joe Khalife
- Document Purpose: Reference material for BST's 2019 NOAA SBIR Phase I proposal

## Executive Summary
This article demonstrates that Long-Term Evolution (LTE) cellular signals and CDMA signals can be exploited as "signals of opportunity" (SOPs) for accurate autonomous vehicle navigation in GNSS-denied environments. Using a specialized software-defined receiver (MATRIX SDR), researchers achieved GPS-like performance in UAV navigation during GPS outages by combining cellular pseudoranges with inertial navigation systems (INS), using a tightly-coupled extended Kalman filter framework incorporating simultaneous localization and mapping (SLAM) principles.

## Technical Approach

### Core Navigation Framework
- **Integration Method**: Tightly-coupled Extended Kalman Filter (EKF) with dual modes:
  - **Mapping Mode**: Estimates both vehicle states and cellular base transceiver station (BTS) states using GNSS and cellular pseudoranges
  - **SLAM Mode**: Operates in GNSS-denied conditions, correcting INS errors using cellular BTS pseudoranges and previously estimated BTS states

### Cellular Signal Processing
The MATRIX (Multichannel Adaptive TRansceiver Information eXtractor) Software-Defined Receiver processes three signal types:

**CDMA (3G) Signals:**
- Exploits known pseudorandom noise (PN) sequences (1.2288 MHz spread, 32,768-chip short code)
- Receiver stages: signal acquisition → signal tracking (PLL/DLL) → message decoding
- Each BTS uses unique pilot offset (512 possible offsets, 64-chip increments)
- Produces pseudorange measurements via time-of-arrival (TOA) estimation

**LTE (4G) Signals - Three Reference Sequences:**
1. **Primary Synchronization Signal (PSS)**: Provides symbol timing; transmitted on middle 62 subcarriers (symbol 7 of slots 0, 10)
   - Limitation: Only 3 orthogonal sequences causes interference
   
2. **Secondary Synchronization Signal (SSS)**: Provides frame timing; 930 kHz bandwidth (comparable to GPS C/A code)
   - 168 different sequences for cell group identification
   - Comparable to GPS in non-multipath environments
   
3. **Cell-Specific Reference Signal (CRS)**: Channel estimation signal scattered across LTE bandwidth
   - Superior TOA accuracy in multipath environments
   - Requires advanced algorithms (MUSIC, ESPRIT, SAGE) for TOA extraction

### Key Technical Advantages of Cellular SOPs
- **Abundance**: Widespread BTS infrastructure
- **Geometric Diversity**: Favorable station geometry by design
- **Large Bandwidth**: Up to 20 MHz (LTE), enabling accurate TOA estimation
- **High Power**: Carrier-to-Noise Ratio (C/N₀) 35-70 dB-Hz (vs. GNSS 37-45 dB-Hz)

## Products & Capabilities Described

### MATRIX Software-Defined Receiver (SDR)
- **Type**: Specialized multi-signal processing system implemented in LabVIEW
- **Capabilities**: 
  - Simultaneous acquisition and tracking of CDMA and LTE signals
  - Pseudorange extraction from cellular BTSs
  - Processing architecture: CDMA module with three stages; LTE module with four stages
  - Integration with INS for navigation-grade positioning
- **Hardware**: Universal Software Radio Peripherals (USRPs—Ettus E-312), GPS-disciplined oscillator, multi-channel sampling

## Use Cases & Applications

### Primary Application: UAV Navigation in GNSS-Denied Environments
- **Urban/Dense Environments**: Areas with severe multipath, signal blockage, or GNSS jamming/spoofing
- **Autonomous Vehicle Navigation**: GPS-independent positioning for safety and reliability
- **GPS Outage Recovery**: Maintaining navigation during temporary GNSS signal loss

### Tested Scenarios

**Simulation (Downtown Los Angeles):**
- 200-second trajectory with 100-second GPS outage
- UAV equipped with consumer-grade IMU (vs. tactical-grade in GPS-aided baseline)
- Four cellular BTSs, two LTE eNodeBs

**Field Tests:**
1. **Semi-urban ground vehicle test**: LTE standalone navigation with moderate multipath
2. **Urban ground vehicle test**: CRS-based receiver in severe multipath environment
3. **UAV flight test**: 50-second GPS outage trajectory using two LTE eNodeBs + three CDMA BTSs

## Key Results

### Simulation Results
- **During GPS availability (first 100 sec)**: Cellular-aided INS with consumer-grade IMU outperformed traditional GPS-aided INS with tactical-grade IMU in estimation error bounds
- **During GPS outage (100-200 sec)**: 
  - GPS-aided INS errors diverged (>100 m RMS)
  - Cellular-aided INS maintained bounded errors throughout outage
  - BTS position estimates converged with manageable uncertainty

### Experimental Results

**Standalone LTE Navigation (Ground Vehicle):**
- Semi-urban: SSS-based receiver degraded by multipath; CRS-based receiver resolved issues
- Urban: CRS-based receiver maintained tracking in severe multipath (superior TOA accuracy demonstrated)

**UAV Cellular-Aided INS (50-sec GPS Outage):**

| Metric | INS-Only | SOP-Aided INS |
|--------|----------|---------------|
| 2D RMSE | >100 m | 4.68 m |
| 3D RMSE | >100 m | 7.76 m |
| Final 3D Error | >100 m | 4.92 m |

**Key Finding**: Achieved near-GPS-level performance (4.92 m final error) using ambient cellular signals in the absence of GNSS, a ~20× improvement over unaided INS.

## Notable Details

### GNSS vs. Cellular BTS Attributes Comparison
| Attribute | GNSS SVs | Cellular BTSs |
|-----------|----------|---------------|
| Position Knowledge | Transmitted | Not transmitted; requires estimation or cloud database |
| Clock Errors | Known | Unknown; must be estimated |
| Oscillators | Atomic | OCXO (Oven-Controlled Crystal Oscillator) |
| Signal Structure | Known | Known |
| Typical C/N₀ | 37-45 dB-Hz | 35-70 dB-Hz |

### Technical Constraints Addressed
- **BTS State Unknowns**: Solved via SLAM framework (simultaneous position and clock error estimation)
- **Multipath Interference**: CRS (vs. SSS) provides superior accuracy; MUSIC/ESPRIT/SAGE algorithms enable advanced processing
- **Near-Far Effect**: System information blocks (SIBs) provide neighboring cell IDs for extended eNodeB discovery
- **SWaP-C Benefits**: Cellular SOPs avoid need for expensive/bulky aiding sensors (cameras, LiDAR)

### Research Support & Context
- Part of broader ONR/NSF-funded research program on signals of opportunity for autonomous systems
- Addresses critical vulnerability: GNSS jamming/spoofing resilience for autonomous vehicles
- Demonstrates feasibility of "free" ambient signal navigation without proprietary infrastructure

### Relevance to BST 2019 NOAA SBIR
This reference article was likely included in BST's NOAA SBIR Phase I proposal (2019) to demonstrate:
1. Academic validation of cellular/LTE-based navigation concepts
2. Technical foundation for signal-of-opportunity approaches
3. UAV navigation capabilities applicable to NOAA missions (weather, coastal, environmental monitoring)
4. Proof-of-concept for GNSS-independent operations in challenging environments (likely relevant to NOAA's ocean/weather observation needs)