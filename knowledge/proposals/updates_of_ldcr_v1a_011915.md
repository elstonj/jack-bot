# Updates of LDCR v1a

## Document Metadata
- Type: Technical status report / experimental instrument update
- Client/Agency: NASA
- Program/Solicitation: 2012 SBIR Phase II (Soil Moisture)
- Date: January 19, 2015
- BST Products/Systems Referenced: LDCR (Low-frequency Dielectric and Conductivity Reflectometer) Build01
- Key Personnel: Eryan Dai (University of Colorado), A.J. Gasiewski (University of Colorado), Maciej Stachura (Black Swift Technologies)

## Executive Summary
This report documents refinements to the LDCR Build01 experimental soil moisture sensor instrument, specifically improvements to its mechanical mounting and stability. Key improvements include development of an experimental fixture using a long pole with dual fulcrums to reduce operator influence on measurements and decrease system noise, resulting in better performance approaching theoretical predictions.

## Technical Approach
The LDCR Build01 is a portable, single-operator soil moisture sensor using LDCR measurement technique. Key refinements:
- **Mechanical stabilization**: Replaced hand-held operation with experimental fixture using long pole with two fulcrums at midpoint to maintain stable orientation
- **Level control**: Added electronic level meter to ensure horizontal pole positioning and consistent sensor height during upward/downward measurements
- **Data collection modes**: Tested in both antenna mode and computer-controlled mode with 4 switching states (States 0-3)
- **Sampling strategy**: Investigated ignoring samples immediately after calibration state transitions to reduce low-pass filter artifacts from brightness difference contributions

## Products & Capabilities Described

### LDCR Build01 (Experimental Soil Moisture Sensor)
- **What it is**: Portable, single-person-operable Low-frequency Dielectric and Conductivity Reflectometer for measuring soil moisture
- **Measurement principle**: Radiometric reflectance technique with calibration states
- **Operating modes**: 
  - Antenna mode (passive measurement)
  - Computer control mode (active switching between 4 calibration states)
- **Output**: DC voltage measurements proportional to soil dielectric properties
- **Key specifications and performance**:
  - Measured noise temperature (ΔT_B): 2.96K with fixture-held unit (improved from 3.7K with hand-held)
  - Theoretical ΔT_B: 2.57K
  - Measurement error with fixture: 15% above theoretical (vs. 44% with hand-held operation)
  - Voltage output range in State 0: 1.605-1.613V (6σ variation of 0.008V)

## Use Cases & Applications
- Soil moisture measurement via ground-based portable instrumentation
- Radiometric characterization of soil dielectric properties
- Calibration and validation of soil moisture remote sensing techniques

## Key Results
- **Noise reduction**: Experimental fixture reduced output voltage noise from 0.01V (man-held) to 0.008V (fixture-held) — a 20% improvement
- **Accuracy improvement**: Measured ΔT_B improved from 3.7K (hand-held) to 2.96K (fixture-held)
- **Performance vs. theory**: Fixture-held unit operates only 15% above theoretical predictions, compared to 44% above for hand-held operation
- **Data stability**: Ignoring 5 samples after state transitions significantly reduced noise floor and improved data smoothness

## Notable Details
- Collaboration between University of Colorado Department of Electrical and Computer Engineering and Black Swift Technologies
- References prior detailed analysis in "LDCR Build01 Experimental Data Analysis v1d" (Dai et al., October 2014)
- **Future work planned**:
  - Increase sample rate to 32 kS/s with 32x data averaging
  - Implement 0.1 ms RC time constant filtering
  - Quantitatively investigate PIN diode switch control signal crosstalk with output DC signal
  - Correct identified crosstalk effects