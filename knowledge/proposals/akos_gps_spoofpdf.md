# Effective GPS Spoofing Detection Utilizing Metrics from Commercial Receivers

## Document Metadata
- Type: Academic research paper / technical reference
- Client/Agency: Not applicable (published academic work by university researchers)
- Program/Solicitation: Not directly BST-related; referenced in BST's 2019 NOAA SBIR Phase I proposal folder
- Date: 2019-01-08 (file date in BST archives)
- BST Products/Systems Referenced: None directly mentioned
- Key Personnel: Authors are from external institutions (Politecnico di Torino, University of Colorado Boulder, Stanford University); not BST staff

## Executive Summary
This paper presents anti-spoofing techniques for GNSS receivers that use outputs from commercial off-the-shelf (COTS) receivers to detect GPS spoofing attacks. The approach combines two complementary methods: power measurement monitoring via automatic gain control (AGC) observation, and signal quality monitoring (SQM) via correlation function asymmetry analysis. The techniques are validated using real Wide Area Augmentation System (WAAS) station data and the Texas Spoofing Test Battery (TEXBAT) dataset.

## Technical Approach

### Power Measurement Monitoring (AGC Method)
- **Principle**: Monitors the automatic gain control (AGC) response of the receiver's front-end to detect additional signals in the RF bandwidth
- **Metric**: AGC gain (G_AGC) computed from receiver's "Pulse Width" output, normalized to dB values
- **Threshold**: G_AGC < γ_AGC where γ_AGC = 4σ_AGC, yielding false alarm probability < 3×10⁻⁶
- **Calibration**: Standard deviation σ_AGC = 0.25 dB derived from 480+ hours of clean data from six WAAS stations
- **Detection Type**: Static indicator (detects spoofing from moment receiver is turned on)
- **Effective Against**: Over-powered spoofing attacks where spoofer has significant power advantage

### Signal Quality Monitoring (SQM Method)
- **Principle**: Detects asymmetries in the GPS L1 C/A code correlation function, which distorts under spoofing
- **Metric**: M = (L_x - E_x) / P_0, a ratio of correlator outputs from Novatel G-III multicorrelator spacing (±0.1016 chips)
- **Distribution**: Modeled as Student's t-distribution with 9 degrees of freedom, σ = 0.005
- **Thresholds** (two-tailed):
  - P_fa = 10⁻⁵: γ_M = 0.041
  - P_fa = 10⁻⁶: γ_M = 0.055
- **Detection Type**: Transient indicator (only detects when spoofing actively distorts correlation peak)
- **Effective Against**: Matched-power spoofing attacks where spoofer has minimal power advantage (e.g., +1.3 dB)

### Discrimination Between Spoofing and RFI
- **Key Observation**: Spoofing and jamming affect AGC and C/N₀ differently
  - RFI: AGC decreases, C/N₀ decreases (noise floor increases)
  - Spoofing: AGC decreases, C/N₀ increases (aligned carrier adds power)
- **Method**: Plot AGC vs. C/N₀ difference; separate regions indicate spoof vs. interference
- **Validation**: Controlled lab tests using white noise, continuous wave (CW), and chirp interference sources confirm threshold discrimination

## Products & Capabilities Described

### Novatel G-III Receiver
- Commercial multicorrelator GNSS receiver used for testing and validation
- Provides AGC metric ("Pulse Width"), C/N₀ estimates, and multi-tap correlator outputs
- Deployed at six WAAS reference stations for nominal behavior characterization

### WAAS Reference Stations (Data Sources)
Six stations across United States provided baseline data:
- HNL (Honolulu, Hawaii)
- FAI (Fairbanks, Alaska)
- ZMA (Miami, Florida) – observed RFI interference
- ZSE (Auburn, Washington)
- ZBW (Nashua, New Hampshire) – observed RFI interference
- ZAU (Aurora, Illinois)

**Data collected:**
- 120 hours AGC data per station
- 24 hours SQM (correlator) data per station
- Total 480+ hours clean baseline for AGC calibration

### Texas Spoofing Test Battery (TEXBAT)
Reference dataset collection from University of Texas at Austin containing:
- **ds0**: Clean baseline (no spoofing)
- **ds2**: Over-powered time-push attack (+10 dB power advantage, extra noise added)
- **ds3**: Matched-power time-push attack (+1.3 dB power advantage)
- **ds5**: Over-powered dynamic spoofing scenario

## Use Cases & Applications

### Spoofing Detection Scenarios
1. **Over-powered spoofing** (power advantage > +5 dB): Detected reliably by AGC metric; SQM less effective
2. **Matched-power spoofing** (+1-2 dB advantage): Detected by SQM when spoof separates from satellite signal; AGC less reliable
3. **Time-push attacks**: Coordinated delay of all satellites to manipulate PVT without changing position; tested via TEXBAT

### Critical Infrastructure Protection
- Aviation navigation (ARNS – Aeronautical Radionavigation Service)
- Maritime vessel positioning and collision avoidance
- Power grid timing synchronization
- Telecommunications network timing
- Transportation fleet tracking and dispatch

### RFI Discrimination
- Urban areas with RF interference (TV antennas, illegal transmitters near GPS band)
- Highway corridors with localized interference sources
- Static ground monitoring stations

## Key Results

### TEXBAT Testing Results

**Clean Dataset (ds0):**
- No false alarms from AGC or SQM metrics
- Both metrics remain well within thresholds

**Over-powered Spoofing (ds2):**
- **AGC metric**: Detects spoofing at ~1.6 minutes (onset of attack), maintains alert for duration of test
- **SQM metric**: Only detects 1-2 asymmetries; one false alarm at ~1.2 minutes (attributed to TEXBAT file artifact)
- **Finding**: AGC is primary detector for power-dominant attacks

**Matched-power Spoofing (ds3):**
- **SQM metric**: Reliably detects asymmetries between 2nd-4th minute as spoofer separates from satellite signals; loses detection after 4th minute (transient behavior)
- **AGC metric**: Also detects but with less dramatic impact than ds2; could be masked by higher thresholds
- **Finding**: SQM is primary detector for low-power-advantage attacks; complementary detection required

**RFI vs. Spoofing Discrimination:**
- **WAAS station data**: Stations ZMA and ZBW showed AGC metric triggers from real-world interference
- **Controlled lab tests**: White noise, CW, and chirp interference produced distinct AGC vs. C/N₀ signatures
- **Threshold result**: Linear discriminant separates RFI (below line) from spoofing scenarios (above line) with clear separation in AGC-C/N₀ space

## Notable Details

### Methodology Strengths
1. **COTS receiver approach**: Requires no additional hardware; applicable to existing deployed systems
2. **Extensive baseline data**: 480+ hours of real WAAS station data for statistical calibration
3. **Complementary techniques**: Two independent metrics cover both high and low power-advantage attacks
4. **Real-world validation**: Tested against both synthetic (TEXBAT) and naturally-occurring RFI

### Limitations & Caveats
1. **SQM correlator spacing limitation**: Cannot detect spoofers outside correlator spacing region (limited to ±0.1016 chips); classified as transient indicator
2. **Threshold environment dependency**: AGC thresholds derived from stable WAAS sites; likely need reassessment for dynamic platforms (aircraft, vehicles) or variable thermal environments
3. **Conservative SQM approach**: Uses mean M across all satellites to reduce per-satellite computation; may lose sensitivity for low C/N₀ satellites
4. **TEXBAT artifacts**: Unexplained false alarms in SQM metric (observed at ~0.9-1.2 min in ds2 and ds3) attributed to dataset creation methodology, not observed in real WAAS data
5. **Smart spoofing vulnerability**: Algorithm could be defeated by spoofing that maintains C/N₀ constant or decreases it while increasing AGC; requires temporal dynamics or multi-metric fusion

### Integration & Decision Algorithm
Paper proposes receiver-level decision logic:
- **Both AGC and SQM trigger (AND condition)**: High confidence spoofing detection
- **Only SQM triggers**: Possible matched-power spoofing or multipath; requires additional validation (continuity checks, known receiver location)
- **Only AGC triggers**: Possible overpowered spoofing or jamming; disambiguate using AGC vs. C/N₀ correlation

### Broader Context
- Part of growing anti-spoofing research at academic institutions (Stanford, CU Boulder, Politecnico di Torino)
- Addresses vulnerability of civilian GPS signals due to low power and open-access nature
- Relevant to emerging threats: increased availability of programmable GNSS simulators and software-defined radio platforms makes spoofing more accessible to non-experts
- Paper emphasizes combining complementary techniques for robust defense against diverse attack types