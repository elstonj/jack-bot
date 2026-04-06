# Radio-Frequency Interference Mitigation for the Soil Moisture Active Passive Microwave Radiometer

## Document Metadata
- **Type:** Peer-reviewed journal article (IEEE Transactions on Geoscience and Remote Sensing)
- **Client/Agency:** NASA (SMAP mission)
- **Program/Solicitation:** SMAP (Soil Moisture Active Passive) mission
- **Date:** Published January 2014 (manuscript received September 2012, accepted June 2013)
- **BST Products/Systems Referenced:** None directly; this is a NASA/academic publication
- **Key Personnel:** Jeffrey R. Piepmeier (NASA GSFC, lead author), Joel T. Johnson (Ohio State), Priscilla N. Mohammed (GESTAR/GSFC), Damon Bradley (University of Maryland/NASA GSFC), Christopher Ruf (University of Michigan), Mustafa Aksoy (Ohio State), Rafael Garcia, Derek Hudson, Lynn Miles, Mark Wong (all NASA GSFC)

## Executive Summary
This paper describes NASA's comprehensive approach to radio-frequency interference (RFI) mitigation for the SMAP spaceborne L-band microwave radiometer. Because SMAP operates in the protected 1400–1427 MHz spectrum vulnerable to out-of-band emissions and illegal transmitters, the mission employs an innovative digital back-end radiometer with ground-based signal processing algorithms to detect and remove RFI. The system collects ~1000× more data than conventionally necessary, enabling multi-domain RFI detection and removal while maintaining soil-moisture measurement accuracy of <0.04 m³/m³.

## Technical Approach

### RFI Environment Characterization
SMAP conducted a multifaceted characterization:
- **Prediction modeling:** Simulations of out-of-band (OOB) emissions from known L-band radar facilities in North America, predicting received power levels up to 2 W
- **Ground-based observations:** Measured RFI characteristics at fixed locations, identifying narrow-band spurious emissions (1 MHz or less)
- **Aircraft-based observations:** 9 flights (~24 hours) during SMAPVEX08 (2008) using digital and analog back-end systems to map RFI across North America
- **Satellite data analysis:** Leveraged SMOS and Aquarius L-band observations to characterize global RFI environment

**Key Finding:** RFI environment includes pulsed radar emissions, continuous-wave (CW) sources, wideband and narrow-band interference. Low-level RFI equivalent to 0.1–10 K brightness temperature would jeopardize mission without aggressive mitigation.

### Radiometer Digital Back-End Design
Rather than conventional square-law diode detectors, SMAP uses:
- **Two Analog Processing Units (APU):** One per polarization, with 14-bit ADCs sampling at 96 megasamples/second (MSPS)
- **One Digital Processing Unit (DPU):** Coordinates signal processing and data management
- **Seven radiation-tolerant FPGAs** performing:
  - **Digital Downconverter (DDC):** Shifts 24 MHz bandwidth (96 MSPS) to baseband, applies 63rd-order low-pass filter with on-orbit programmable coefficients
  - **16-channel Polyphase Filter Bank:** Separates full-band data into 1.5 MHz subbands; uses custom pipelined FFT
  - **Statistics Calculation Unit (SCU):** Computes first four raw moments of signal for full-band and all 16 subbands

**Key Capability:** Outputs the first four raw moments of receiver-system noise voltage (enabling kurtosis calculation and Stokes parameter measurement) rather than simple detector counts. Synchronous integration with radar pulse-repetition interval (~350 μs).

### RFI Detection Algorithms (Ground Processing)
Four complementary detectors, each producing binary RFI flags:

1. **Pulse Detection (Time Domain):** Searches for impulsive RFI via anomalous antenna temperatures
   - Compares individual T_A against mean m and standard deviation σ_td
   - Detection: T_A − m ≥ β_td · σ_td
   - Best for large-amplitude, short-duration, low-duty-cycle sources

2. **Cross-Frequency Detection:** Identifies RFI spanning multiple frequency channels
   - Operates on 16 subband channels at 1.4 ms integration
   - Uses 16−N channels with smallest T_A values to estimate mean/σ
   - Flags channels >β_cf standard deviations above mean, plus adjacent subbands
   - More sensitive to CW interference

3. **Kurtosis Detection:** Tests for non-Gaussianity of received signals
   - Computes kurtosis K = (fourth central moment) / (second central moment)²
   - Detection: |K − K_nom| > β_K · σ_K
   - Applied independently to I and Q components of every subband and polarization
   - Effective for both CW and pulsed RFI classification

4. **Polarization Detection:** Thresholds third and fourth Stokes parameters (T₃, T₄)
   - Detects anomalous linear and circular polarization signatures
   - T₄ expected ~0 over land; T₃ varies with Faraday rotation
   - Detection: |T₃,₄ − T_nom| ≥ β₃,₄ · σ₃,₄

**Maximum Probability of Detection (MPD) Flag:** Logical OR of all four detector outputs maximizes probability of catching RFI; outputs combined for removal of contaminated time–frequency samples.

### Data Collection Strategy
- **Full-band measurements** at 350 μs interval (~44 samples per 15.4 ms L1B product)
- **Subband measurements** at 1.4 ms interval (11 time samples × 16 frequency channels per product)
- **Total data multiplier:** ~1000× more measurements than minimum needed for single Stokes vector measurement
- **Single-product NEDT:** 0.96 K (nominal system temperature 540 K, 24 MHz bandwidth)

## Products & Capabilities Described

### SMAP Microwave Radiometer
- **What it is:** Spaceborne L-band (1400–1427 MHz) radiometer with digital back-end for soil-moisture measurement
- **Specifications:**
  - Operates in protected Earth Exploration Satellite Service band
  - Full bandwidth: 24 MHz
  - 16 frequency subbands of 1.5 MHz each
  - Dual-polarization (V and H)
  - Measures full Stokes vector + kurtosis
  - Radiometric accuracy requirement: <1.3 K uncertainty
  - Soil-moisture retrieval requirement: <0.04 m³/m³ uncertainty
  - 40° nominal incidence angle

- **Proposed Use:** Global high-resolution active–passive L-band observations of Earth from space; primary objective is soil-moisture measurements
- **Key Innovation:** First spaceborne digital radiometer with raw-moment outputs (vs. detector counts) enabling advanced RFI detection on ground

### Engineering Test Unit (ETU)
- **What it is:** Fully functional pre-flight radiometer with identical RF and digital electronics (minus antenna)
- **Use in context:** Verified RFI detection and mitigation performance before flight
- **Test Capability:** Accepts injected RFI signals (pulsed sinusoids at various widths: 2, 30, 450 μs, and continuous) with controllable power levels (0.1 K to >1000 K brightness temperature)

## Use Cases & Applications

### Primary Mission
- **Global soil-moisture measurement:** Daily, high-resolution observations of Earth's surface soil moisture with <0.04 m³/m³ uncertainty
- **Application areas:** Agriculture, hydrology, climate modeling, drought monitoring
- **Requirement context:** Must maintain measurement fidelity despite ubiquitous RFI in global L-band environment

### RFI Environment Characterization Uses
- **North American validation:** SMAPVEX08 aircraft campaign mapped RFI spatial distribution
- **Global RFI assessment:** Leveraged SMOS and Aquarius satellite data to extend beyond regional (North America-centric) predictions
- **Regulatory/spectrum management:** Results inform international radio spectrum management for passive remote sensing

## Key Results (Measurements & Demonstrations)

### RFI Environment Findings
1. **Global RFI distribution (Aquarius data, April–May 2012):**
   - Large RFI sources observed on every continent
   - North America less corrupted than Europe and Asia
   - Emphasizes importance of global characterization vs. North America-only studies

2. **RFI Statistics (SMOS analysis):**
   - Generalized Extreme Value (GEV) distribution fits RFI brightness-temperature tail behavior
   - GEV parameters fitted from SMOS data: a=0.77, σ=3.75 K, μ=3.2 K
   - SMOS-derived RFI levels significantly higher than SMAPVEX08 airborne campaign (due to global coverage)
   - **Conservative SMAP assumption:** 10% of observations will contain RFI ≥20 K

3. **RFI Source Types Observed:**
   - Pulsed radar emissions (wide-band)
   - Narrow-band continuous-wave (CW) emissions (<1 MHz bandwidth)
   - Spurious emissions from communication systems
   - Likely illegally operating emitters within protected band

### Radiometer Hardware Performance (ETU Testing)

**Kurtosis Measurements:**
- Full-band kurtosis measured at 350 μs resolution in presence of injected sinusoidal RFI
- Good theoretical agreement for mean kurtosis; measured standard deviations slightly higher (due to fourth-moment discretization)
- Kurtosis values <3 for sinusoidal interference; >3 for pulsed interference (enables source classification)

**Cross-Frequency RFI Mitigation (Low-Level CW Example):**
- Injected 1413.5 MHz sinusoid at 17.3 K brightness temp in center channel (1.08 K integrated effect)
- Cross-frequency detector at 15.4 ms resolution removed corrupted channel + adjacent channels
- Result: 46 of 176 measurements discarded; 16.3% NEDT increase; **mitigated brightness 114.6 K vs. true 114.7 K (0.1 K error)**
- Successful detection/mitigation demonstrated from <1 K to >100 K RFI power levels

**Pulsed RFI Removal (2 μs Pulses at 596 Hz):**
- **High-amplitude case (3.84 K RFI contribution):**
  - Original: 120.01 K → Mitigated: 116.15 K (after 0.19 K bias correction)
  - Mitigated 3.86 K vs. true 3.84 K RFI (**excellent agreement**)

- **Low-amplitude case (1.74 K RFI contribution):**
  - Original: 117.75 K → Mitigated: 117.12 K
  - Mitigated only 0.63 K vs. true 1.74 K (**1.11 K uncorrected bias**)
  - Note: Full-band measurements used primarily for land flagging; spectrogram-based (subband) detectors perform better at low amplitude

**Simulated Global Performance:**
- Integration of simulated SMAP mitigation biases with SMOS-derived RFI pdf enables prediction of global expected RFI impact
- Example: Pulsed RFI at 1.74 K brightness temp → <0.1 K post-mitigation bias (after algorithm improvements from initial testing)
- NEDT increase from RFI mitigation quantified as function of RFI brightness temperature

### Detection Threshold & False-Alarm Rate
- Prelaunch threshold (β) set to limit false-alarm rate to **9.3%**
- This corresponds to **5% increase in effective NEDT** when no RFI present
- Threshold varies geographically via 1° × 1° lookup table to account for regional RFI likelihood/type
- Expected revision post-launch based on actual on-orbit RFI environment

### Data Loss from RFI Removal
- Trade-off between RFI mitigation and measurement noise: discarding contaminated samples increases