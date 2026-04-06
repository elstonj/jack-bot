# LDCR sUAS Soil Moisture Sensor Status Update

## Document Metadata
- Type: Status/Progress Report
- Client/Agency: NASA
- Program/Solicitation: 2012 SBIR Phase II (Soil Moisture)
- Date: January 20, 2016
- BST Products/Systems Referenced: Tempest UAS, LDCR (L-band Distributed Correlator Radiometer)
- Key Personnel: Eryan Dai, Albin J. Gasiewski, Maciej Stachura (BST)
- Affiliation: Department of Electrical and Computer Engineering, University of Colorado at Boulder

## Executive Summary
This document reports progress on development and field validation of the LDCR soil moisture sensor payload mounted on the Tempest UAS. Flight tests were conducted at the Canton Soilscape site on September 8-9, 2015, mapping approximately 41 acres using two antenna temperature estimation methods. Results demonstrate that LDCR brightness temperature measurements correlate with in-situ volumetric soil moisture (VSM) data, validating the sensor's capability for soil moisture remote sensing applications.

## Technical Approach

### Flight Operations
- **Platform**: Tempest UAS flown at altitude h=35 m
- **Flight Pattern**: Serpentine path covering ~41-acre rectangular mapping area
- **Flight Duration**: ~16 minutes per flight
- **Flight Speed**: v = 21 m/s
- **Test Dates/Conditions**:
  - September 8: 11:35 AM local time, ~60% cloud cover, 27°C ambient, dry green grass (~7 inch height)
  - September 9: 8:00 AM local time, 100% cloud cover, 20°C ambient, grass lightly moistened with dew
  - No precipitation observed on either day

### LDCR Sensor Specifications
- **Antenna**: MiCo antenna with 3 dB beam width of ~45° (from HFSS simulations)
- **Surface Pixel Size**: ~28 m at 35 m altitude
- **Video Filter**: Low-pass with time constant τ=1.5 ms
- **A/D Sampling**: Fundamental interval T=1 ms
- **Calibration Cycle Period**: Tcc=44 ms
- **Single-Sample TA Standard Deviation**: ~7.5 K
- **IR Sensor**: Onboard infrared sensor for surface physical temperature measurement

### Data Processing Methods

**Method 1: N-Sample Grid-Cell Averaging**
- Two-level averaging: (1) within each calibration cycle, (2) across discrete calibration cycles
- N1=6 samples available per calibration cycle (after dropping 5 post-transition samples)
- N2 ≈31 calibration cycles per grid cell
- Total averaged samples per pixel: N = N1×N2 = 186
- Resulting measurement noise standard deviation: σTA ≈ 0.9 K
- Median filter applied (window size 3) to reduce sporadic noise in IR temperature measurements

**Method 2: Unbiased Linear Minimum Mean Square Error (LMMSE)**
- Optimal antenna temperature estimator based on radially-symmetric covariance functions
- Equivalent to kriging method
- Radial covariance function: r(d) = σ²exp(-(d/a)²), where a=58 m (≈2× flight line separation)
- Data variances: 65.61 K² (Sept 8) and 62.41 K² (Sept 9)
- Lagrange multipliers applied to ensure unbiased estimation
- Sampled points selected within circle of half-pixel radius of user grid point

### Surface Temperature Measurements
- **September 8**: Mean 29.91°C, SD 0.79°C (over ~7 minute mapping period)
- **September 9**: Mean 19.87°C, SD 0.16°C

## Products & Capabilities Described

### LDCR (L-band Distributed Correlator Radiometer)
- **Function**: Passive microwave radiometer for measuring upwelling antenna temperature at L-band
- **Capabilities**: 
  - Maps brightness temperature across agricultural/soil areas
  - Spatial resolution enabling soil moisture detection at ~28 m pixel size
  - Uses infrared sensor to measure surface physical temperature
  - Receiver boards with chip-level components enabling portable deployment
- **Flight Validation**: Successfully collected radiometric data during two flight sorties at Canton Soilscape site

### Tempest UAS
- **Function**: Carrier platform for LDCR sensor payload
- **Capabilities**: 
  - Autonomous serpentine flight patterns
  - 35 m operational altitude suitable for ~28 m surface resolution
  - ~16 minute flight endurance adequate for mapping 41-acre sites
  - Precise GPS navigation enabling sample point geolocation

## Use Cases & Applications

### Primary Application: Soil Moisture Remote Sensing
- **Test Site**: Canton Soilscape site (Kansas)
- **Mapped Area**: ~41-acre rectangular region with mixed mollisol and inceptisol soils under grassland/herbaceous cover
- **Validation Approach**: Correlation with wireless soil moisture smart sensor network (12 nodes, 3 depths: 5cm, 15cm, 30cm)

### Specific Findings
- Brightness temperature sensitivity to VSM: 0.87-0.82 K/% (slope of best-fit line)
- Higher soil moisture areas show lower emissivity and lower upwelling antenna temperature
- Spatial anomalies detected: ~40 K warming over NW quadrant (~40% of mapping area) and ~40 K localized cooling in SW corner, persisted across both flight days
- Anomalies presumed related to soil moisture variations rather than vegetation differences (no correlated vegetation density/water content variations observed)

## Key Results

### Data Validation Results
- In-situ measurements from 12 smart sensor nodes (9 within LDCR mapping area) validated upwelling antenna temperature observations
- Correlation confirmed: areas of higher volumetric soil moisture (VSM) exhibited lower brightness temperatures
- Repeatable spatial patterns observed across sequential flights separated by ~20 hours

### Comparison of Estimation Methods
- **N-Sample Grid-Cell Averaging**: Simpler method, measurement noise σTA ≈ 0.9 K
- **Unbiased LMMSE**: More sophisticated kriging approach, higher estimation error than biased LMMSE but with unbiased constraint properly considered
- **Biased LMMSE**: Lower estimation error standard deviation than unbiased variant
- Maps generated from both methods show consistent spatial patterns

### Physical Temperature Data
- Clear diurnal difference: 11:35 AM measurements ~10°C warmer than 8:00 AM measurements (29.91°C vs 19.87°C)
- Temporal stability within day: low standard deviation on Sept 9 (0.16°C) despite 100% cloud cover suggests stable surface temperature during early morning

## Notable Details

### Manufacturing/Production
- Four additional LDCR receiver boards in production at Q.S.C. SYSTEMS, Inc
- Fabrication timeline: 2 weeks
- Detailed component layout drawings created to facilitate assembly (Figure 8)

### Data Quality Considerations
- Sporadic noise in IR sensor data identified and successfully filtered with median filter (window size 3)
- Time-deconvolution method to invert blurring from calibration state transitions identified as still needed
- Polarization and incident angle effects on TA-VSM sensitivity identified as topics for ongoing study

### Validation Framework
- In-situ soil moisture data being collected and processed by Soilscape site operators for comparison
- Hypothesis that NW/SW anomalies reflect soil moisture variations requires validation against soil temperature and moisture field data

### Academic/Research Context
- Work conducted at University of Colorado at Boulder Department of Electrical and Computer Engineering
- Leverages published kriging/geostatistical methods (references to Montero, Goovaerts, Pyrcz, etc.)
- Part of broader NASA-funded SBIR Phase II effort