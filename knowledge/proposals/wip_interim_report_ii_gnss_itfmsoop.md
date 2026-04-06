# WIP Interim Report II (GNSS ITFM/SoOP)

## Document Metadata
- Type: Interim Report (Phase II progress)
- Client/Agency: NOAA
- Program/Solicitation: 2019 SBIR Phase II (GPS Denied navigation)
- Date: Created 2021-08-12; Modified 2021-10-07
- BST Products/Systems Referenced: GPS firmware, UAV/UAS navigation systems
- Key Personnel: Not named in document

## Executive Summary
This interim report documents Black Swift Technologies' Phase II SBIR progress on GPS-denied navigation systems, focusing on two primary technical areas: (1) GNSS spoofing and jamming detection using commercial receivers, and (2) evaluation of Signals of Opportunity (SoOP) for alternative positioning, navigation, and timing (PNT). The work involved hardware testing, extensive signal analysis across multiple technologies (cellular, digital TV, LEO satellites, FM/AM radio), and selection of LTE as the primary candidate SoOP for GPS-denied UAV operations.

## Technical Approach

### GNSS Spoofing/Jamming Detection (Task 2.2)
- **Hardware Selected:** uBlox ZED-F9P receiver with built-in spoofing/jamming detection capabilities
- **Spoofing Detection Method:** Monitors GPS signal for changes suggesting external manipulation; requires genuine initial signal and multiple GNSS signals available
- **Jamming Detection Method:** Monitors background noise changes; detects both broadband (BB) and continuous wave (CW) jamming with configurable thresholds
- **Implementation:** Added detection support to existing BST GPS firmware using uBlox's proprietary protocol
- **Testing Approach for Jamming:** USB drive induced RF interference via unshielded cable near receiver; detection was repeatable across multiple attempts and environments

### Signals of Opportunity (SoOP) Research
**Methodology:** Evaluated multiple signal types for accuracy, practicality, coverage, and development feasibility for UAV PNT in GPS-denied environments.

**SDR Selection:** Ettus Research E310
- Dual receivers, wide frequency range (supports multiple signal types)
- Good documentation and community support
- UHD and GNU Radio compatibility ensures portability to other Ettus platforms (B2xx, E3xx series)
- Advantage: NASA loan unit available in BST workshop

## Products & Capabilities Described

### GPS Firmware Enhancement
- Integration of spoofing/jamming detection into existing BST GPS firmware
- Compatibility with uBlox receivers and proprietary protocol
- Support for configurable detection thresholds

### Signals of Opportunity Navigation System (in development)
- Multi-signal architecture supporting various SoOP candidates
- SDR-based implementation with GNU Radio integration
- Real-time signal processing for pseudorange calculation

## Use Cases & Applications

**Primary Use Case:** GPS-denied UAV navigation in regions where GNSS is jammed or unavailable

**Operational Regions:**
- North America (primary focus)
- Europe
- Latin America
- Future expansion to Africa (requiring different signal coverage analysis)

**Environment Types:**
- Urban/populated regions (for cellular and digital TV SoOPs)
- Remote regions (for LEO constellation SoOPs)
- Areas with active GPS jamming

## Key Results

### Signal Evaluation Findings

**LTE (4G) - Selected as Primary SoOP**
- **Advantages:**
  - Excellent coverage in Americas, Europe, Asia
  - Highest carrier frequency (2.5 GHz) → precise carrier phase observables
  - Widest bandwidth (up to 20 MHz) → accurate time-of-arrival calculations
  - High transmit power (-65 to -75 dB average conditions) → resistant to jamming
  - Global standard with continued expansion; 5G built on LTE framework
  - **Critical Finding:** Real-world GPS-denied testing at Edwards AFB showed LTE base station clocks remain stable for ≥1 hour after losing GPS signal (most comprehensive study to date)
  
- **Challenges:**
  - Requires powerful computing resources for real-time processing
  - Raspberry Pi 4B (quad-core 64-bit @ 1.5 GHz) identified as potentially sufficient but may need dedicated hardware accelerators
  - Advanced processing required to extract timing information from LTE standard

**2G/GSM - Rejected**
- Low power and narrow bandwidth (200 kHz) require vehicle proximity to transmitters (few hundred meters)
- Unsynchronized base station clocks necessitate time-difference-of-arrival (TDoA) approach
- Networks being phased out globally by mid-2020s (see carrier sunsetting table)
- Declining usage in BST operational regions (NA, EU, LA)
- If revisited: gr-gsm open-source GNU Radio module available

**3G/CDMA - Not Pursued**
- While more longevity than 2G (some carriers lack sunsetting plans), phasing out in BST primary regions
- Research shows <10m error with ≥2 signals tracked, but requires:
  - Per-transmitter clock bias/drift modeling
  - Extraction of pilot, sync, and paging channels
  - PN code offset identification
- gr-cdma open-source receiver exists but unmaintained (5+ years without updates)
- Higher development burden justified by sunsetting timeline in BST regions

**Digital TV (ATSC/DVB) - Rejected**
- No timing information transmitted → requires TDoA approach
- Middle-of-pack bandwidth (6-8 MHz ATSC, 1.7 MHz DVB)
- Colocated transmitters reduce signal diversity
- More susceptible to multipath than LTE
- Regional fragmentation: ATSC (US only) vs. DVB (rest of world) complicates testing
- No open-source ATSC receiver; only DVB has gr-dvbt module
- Practical testing limitation: difficult to access live DVB signals from US-based BST

**Iridium/LEO Satellites - Considered but Problematic**
- **Advantage:** Theoretically global coverage (ideal for remote regions)
- **Critical Limitation:** Frequency proximity to GNSS L1, Galileo, GLONASS → likely to be jammed simultaneously with GNSS
- **Complexity:** Requires real-time satellite position calculation
- **Performance:** ~12m accuracy with 25 LEO satellites; 360m with 2 Orbcomm satellites
- **Development:** gr-iridium module exists for burst detection/demodulation but adds significant processing complexity
- **Conclusion:** Not viable for GPS-denied scenarios where jammer targets GNSS frequencies

**FM/AM Radio - Evaluated but Suboptimal as Primary SoOP**
- **Advantages:**
  - Ubiquitous coverage in populated regions
  - High transmit power
  - Lower processing complexity than LTE
  - Constant transmit power enables RSSI-based approaches
  
- **Disadvantages:**
  - Unsynchronized transmitters (time, frequency, phase)
  - No timing information; requires TDoA approach
  - High susceptibility to multipath and NLOS effects
  - UAS orientation affects antenna RSSI measurements
  
- **Alternative Approaches Identified but Not Primary:**
  - Prior-knowledge approach: Create transmitter signal strength models, match flight RSSI to models
  - RF mapping approach: Pre-flight GNSS-tagged signal strength survey, match real-time RSSI
  - Both require significant preparation and have orientation-dependency issues

### Network Coverage Analysis
Detailed cellular coverage comparison (2G/3G/4G) across regions with carrier-specific sunsetting timelines:

**Key Findings by Region:**
- **USA:** 4G/LTE superior; 2G ended by 2020; 3G ending by April 2022 (all major carriers)
- **Europe:** LTE expansion ongoing; 3G sunsetting by 2021-2025; 2G by 2025-2030
- **Mexico:** 2G ended Jan 2021
- **Canada:** 2G by 2019-2021; 3G by March 2021
- **Asia/Pacific:** Mixed timelines; Japan 2G phased 2008-2012, 3G by 2022-2026; Australia 3G ended 2019
- **Global Trend:** Spectrum "refarming" from 2G/3G to 4G/5G LTE; 4G coverage doubled 2015-2020 but growth slowing (only 1.3% increase 2019-2020)

## Notable Details

### Document Status
- **Warning:** Document represents work-in-progress; content superseded by Overleaf Phase II final report
- **Incomplete Sections:** Marked with placeholders [a][b][c][d][e][f][g][h][i][j][k][l][m] indicating ongoing edits
- Multiple unfinished technical descriptions (e.g., "DESCRIPTION OF LTE PSEUDORANGE TECHNIQUE HERE")

### Research References
- Extensive academic literature review conducted (Kassas, Thevenon, Kapoor et al., GSM Association)
- Real-world testing validated by Edwards AFB GPS-denied experiments
- International Telecommunication Union data for global network coverage trends

### Hardware Considerations
- Real-time LTE processing may require beyond Raspberry Pi 4B: matrix accelerators or dedicated floating-point units considered
- Trade-off analysis between signal complexity (processing power) and coverage reliability

### Future Development Considerations
- System must support multiple SoOP backends despite selecting LTE as primary
- Portability to other Ettus SDR platforms built into architecture
- Modular design for future signal additions (gr-gsm, gr-dvbt modules identified as potential integrations)

---

**Note:** This interim report contains substantial technical research but incomplete implementation details and several sections marked for revision. Final Phase II findings documented in separate Overleaf report referenced in document header.