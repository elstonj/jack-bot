# LDCR Build01 Experimental Data Analysis

## Document Metadata
- Type: Technical Report / Experimental Data Analysis
- Client/Agency: NASA
- Program/Solicitation: 2012 SBIR Phase II (Soil Moisture)
- Date: October 17, 2014
- BST Products/Systems Referenced: LDCR (L-band Differential Correlation Radiometer) Build01
- Key Personnel: Eryan Dai, A.J. Gasiewski, Maciej Stachura (BST)

## Executive Summary
This report analyzes experimental data from LDCR Build01, a human-portable ground test unit designed to measure soil moisture via L-band microwave radiometry. The instrument successfully demonstrated measurement of brightness temperature differences in nadir and zenith directions over a grass field, with measured sensitivity of 3.7 K (44% higher than theoretical prediction of 2.57 K).

## Technical Approach
LDCR Build01 employs a correlation radiometer architecture operating in two modes:
- **Antenna Mode**: Measures differential brightness temperature between up-looking and down-looking L-band patch antennas
- **Computer Control Mode**: Enables four switch states for system diagnostics and calibration using internal thermal reference resistors on Peltier thermoelectric cooler/heater chips

The instrument outputs a DC voltage proportional to antenna temperature difference, sampled and recorded on SD card. Key specifications include:
- Bandwidth: 27 MHz per channel
- RC integration time constant: 1.5 ms
- Two ZFL-1000LN+ amplifiers and AD5391 correlator board
- Two NDVI sensor boards (thermal IR, near IR, visible red) positioned 10 cm from antennas
- GPS/navigation microcomputer for location, orientation, and NDVI logging
- Operating height: 1-1.3 m above ground

## Products & Capabilities Described

### LDCR Build01 (L-band Differential Correlation Radiometer - Build01)
**What it is**: Portable, person-operable L-band correlation radiometer for soil moisture measurement

**Technical specifications**:
- Measured sensitivity (ΔS): 3.7 K (achieved)
- Theoretical sensitivity: 2.57 K
- Output voltage stability: 6σ variation of 0.01 V
- Vertical orientation capability (nadir/zenith measurement)
- Portability: Single-person operation

**Use in this context**: Ground validation/testing unit for LDCR technique before integration onto UAS platform; feasibility demonstration of correlation radiometer approach for soil moisture remote sensing

**Performance claims**:
- Output voltage good agreement with theoretical calculations in antenna mode (measured 0.17 V difference vs. calculated 0.1755 V when inverted)
- Adequate sensitivity for soil moisture measurement despite 44% higher noise floor than theoretical prediction

## Use Cases & Applications

1. **Soil Moisture Monitoring**: Primary application; validation of NASA's SMAP (Soil Moisture Active Passive) mission capabilities
2. **Sub-watershed Scale Coverage**: Proposed deployment on lightweight UAS for ~km-scale coverage at ~15 m spatial resolution
3. **Scaling Studies**: High spatial resolution measurements suitable for scaling research between point measurements and satellite data
4. **Low-Cost Airborne Validation**: Alternative to existing manned aircraft-based soil moisture sensors; lower operator cost model
5. **Hydrological Applications**: Support for weather pattern development prediction, precipitation modeling, water resource management, agriculture, flood runoff prediction, and freeze/thaw state determination

## Key Results

**Antenna Mode Testing**:
- Average output voltage (horizontal orientation): 1.43 V
- Average output voltage (inverted orientation): 1.6 V
- Measured voltage difference: 0.17 V
- Calculated voltage difference (assuming Zenith brightness temp = 5 K, Nadir = 200 K): 0.1755 V
- **Result**: Excellent agreement between measurement and theory

**Computer Control Mode (Four-State Calibration)**:
- State 0 (Reference-Reference) stability: 1.53-1.54 V with 0.01 V 6σ variation
- Measured system sensitivity (ΔS): 3.7 K
- Theoretical system sensitivity: 2.57 K
- **Result**: Measured sensitivity 44% higher than theoretical; attributed to additional correlator circuitry noise

**Stability Analysis**:
- State transition artifacts significant; data quality improves with 5+ ignored samples post-transition
- Demonstrated need for stable mechanical holding during measurements

## Notable Details

**Discrepancies & Issues Identified**:
- Measured sensitivity exceeds theoretical prediction by 44%, likely due to additional noise in correlator circuitry—identified as area for future investigation
- State transition data artifacts require post-processing to achieve stable voltage readings
- Thermal reference elements not powered during testing; future work includes powered cold target calibration

**Future Work Planned**:
1. Mechanical stabilization: Pole-mounted fixture with fulcrum to eliminate orientation drift
2. Cold LN2 calibration target development for end-to-end sensor calibration
3. Increased sampling rate: 32 kS/s with 32x averaging and 0.1 ms time constant to minimize transition artifacts
4. Investigation of PIN diode switch control signal crosstalk effects

**Technical Validation**:
- Demonstrates feasibility of LDCR technique for soil moisture measurement
- Confirms adequate sensitivity despite engineering challenges
- Theory-to-practice correlation validates design approach
- Single-person portability achieved as design requirement

**Context**: This is Phase II deliverable for NASA SBIR program (Soil Moisture topic, 2012); represents mid-development stage of LDCR technology pathway toward UAS integration for SMAP validation missions.