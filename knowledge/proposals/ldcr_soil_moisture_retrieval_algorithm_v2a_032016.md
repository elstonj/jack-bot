# LDCR Soil Moisture Retrieval Algorithm v2a

## Document Metadata
- Type: Technical Report / Algorithm Documentation
- Client/Agency: NASA
- Program/Solicitation: 2012 SBIR Phase II
- Date: March 20, 2016
- BST Products/Systems Referenced: Tempest UAS, LDCR (Lobe Differencing Correlation Radiometer)
- Key Personnel: Eryan Dai, A.J. Gasiewski

## Executive Summary
This report documents the antenna temperature mapping and soil moisture retrieval algorithms developed for the LDCR radiometer system deployed on the Tempest UAS. Flight tests were conducted at the Canton Oklahoma Soilscape site on September 8-9, 2015, using two mapping methods (N-sample grid averaging and unbiased Linear Minimum Mean Square Error estimation) to generate high-resolution soil moisture maps from microwave radiometric measurements.

## Technical Approach

### Data Processing Pipeline
- **Temporal collocation**: Radiometric data sampled at ~1 ms intervals were collocated with navigation data (~22 ms intervals) via linear interpolation
- **Calibration**: Pre-flight calibration performed over calm fresh water using thermistor temperature measurements
- **Antenna temperature mapping**: Two parallel methods employed:
  1. N-sample grid-cell averaging within and across calibration cycles
  2. Unbiased Linear Minimum Mean Square Error (LMMSE) estimation using radial covariance functions

### Mapping Methods

**N-Sample Averaging:**
- First stage: Averaged N₁=6 samples within each calibration cycle, achieving measurement noise standard deviation of σ_TA ≈ 2.7 K
- Second stage: Further averaged across N₂≈31 calibration cycles per grid cell, reducing noise to ~0.9 K
- Total averaging: N = N₁ × N₂ = 186 samples per pixel
- LDCR characteristics: Low-pass video filter τ=1.5 ms, A/D sampling T=1 ms, calibration cycle period T_cc=44 ms

**Unbiased LMMSE Estimation:**
- Based on geostatistical kriging methodology with radially-symmetric covariance function
- Covariance function: C(h) = σ₀²[1 - 1.5(h/a) + 0.5(h/a)³] for h ≤ a, where a=58 m (roughly 2× flight line separation)
- Orthogonality principle applied with Lagrange multipliers to enforce unbiased constraint
- Regional covariance σ₀²: 65.61 K² (Sept 8), 62.41 K² (Sept 9)
- Estimation window: circular region with half-pixel radius around each grid point

### Soil Moisture Retrieval Algorithm

**Radiative Transfer Model:**
- Upwelling brightness temperature combines direct soil emission, vegetation opacity effects, and atmospheric coupling
- Equations for V and H polarization account for:
  - Soil emissivity: esv, esh
  - Vegetation water content (VWC): derived from MODIS NDVI
  - Vegetation opacity: τc = (s × VWC × sec θi) with empirically-derived stem factor (s)
  - Antenna gain: Simulated GVV and GHH using HFSS 15.0

**Key Equations:**
- Antenna temperature relationship to dielectric constant: TA = (GVV·GHH·TBV·TBH)/G_norm + T_antenna
- Dielectric mixing model: εs relates to volumetric soil moisture via soil texture-dependent parameters (sand%, clay%, silt%)
- Forward model iteratively inverts measured TA to retrieve VSM

**Vegetation Parameter Estimation:**
- Stem factor s estimated from in-situ measurements at 9 nodes
- Measured sensitivity: 0.81 K/% VSM change
- Estimated values: s_H = 0.39, s_V = 0.36 (H-pol ~8-10% higher than V-pol)
- MODIS NDVI maximum/minimum: 1.02 vs 0.88 kg/m² VWC across mapping area

**Antenna Temperature Calibration Correction:**
- Systematic offsets identified between measured and calculated antenna temperatures
- Sept 8 offset: 43 K; Sept 9 offset: 31 K (different values indicate need for improved calibration)

## Products & Capabilities Described

### LDCR (Lobe Differencing Correlation Radiometer)
- **What it is**: Dual-polarization L-band microwave radiometer designed for UAS deployment
- **Key specifications**:
  - Frequency: L-band (~1.4 GHz, implied)
  - Dual polarization: H and V
  - Antenna: MiCo (Microstrip Colinear) array, 3 dB beamwidth ~45°
  - Antenna radiation efficiency: 95.8%
  - Radiometric sampling: ~1 ms interval
  - Includes thermal IR sensor for surface temperature measurement
  - Calibration cycle period: 44 ms with 4 calibration states
- **Used in**: Airborne soil moisture mapping via passive microwave radiometry
- **Associated sensor**: Thermal IR for down-looking surface temperature measurement

### Tempest UAS
- **Specifications**: Flying altitude h=35 m, flight speed v=21 m/s
- **Capabilities**: Serpentine grid mapping patterns over ~32-acre areas
- **Flight duration**: ~16 minutes per mission
- **Navigation**: GPS-based position tracking (~22 ms update rate)

## Use Cases & Applications

### Soil Moisture Mapping
- **Site**: Canton Oklahoma Soilscape (36.00°N, 98.63°W)
- **Mapping area**: ~260 m (W-E) × 500 m (N-S), 32 acres
- **Spatial resolution**: ~28 m pixel size (from 35 m altitude, 45° beamwidth)
- **Test conditions**:
  - Sept 8: 60% cloud cover, 27°C ambient, dry grass (~7" height)
  - Sept 9: 100% cloud cover, 20°C ambient, dew-moistened grass
- **Retrieved soil moisture**: 0-70%+ VSM range, with anomalous high values (~70%) in SW quadrant requiring investigation

### In-Situ Validation
- 12 wireless soil moisture sensor nodes at 3 depths (5, 15, 30 cm)
- Soil types: Mollisols and Inceptisols
- Land cover: Grassland/Herbaceous
- Soil texture: Sandy loam (60% sand, 10% clay, 30% silt)

## Key Results

### Antenna Temperature Mapping
- **Sept 8 (11:35 AM)**: Mean TA ~20 K higher than Sept 9, consistent with warmer surface temperature (mean 29.91°C ± 0.79°C)
- **Sept 9 (8:00 AM)**: Lower TA due to early morning conditions (mean TP 19.87°C ± 0.16°C)
- **Spatial patterns**: Repeatable warming signature over ~40% of mapping area (NW quadrant) with ~20 K amplitude across both test days
- **Noise reduction**: Median filtering (window size 3) effectively removed sporadic IR sensor noise

### Temperature Mapping Comparison
- **N-sample averaging**: Achieved ~0.9 K measurement noise standard deviation for 186 samples per pixel
- **LMMSE mapping**: Superior handling of irregular sampling patterns; unbiased constraint increases estimation error vs. biased method but provides theoretical guarantee
- **Estimation uncertainty**: LMMSE error covariance calculated for both biased and unbiased formulations

### Soil Moisture Retrieval Performance
- **Vegetation water content**: 0.88-1.02 kg/m² range from MODIS NDVI data
- **TA-VSM sensitivity**: 0.81 K per % VSM (measured from in-situ nodes)
- **Dielectric range**: Soil dielectric constant 3-6 range for 0-50% VSM in sandy loam
- **Calibration issues**: 31-43 K systematic offsets between measured and modeled TA indicate need for:
  - Refined antenna temperature calibration procedures
  - Time-deconvolution method to account for calibration state transitions
  - Further investigation of SW quadrant anomalies

## Notable Details

### Technical Innovations
- **Kriging-based LMMSE**: Application of geostatistical methods to radiometric data interpolation, ensuring optimal minimum variance estimates
- **Dual-method comparison**: N-sample averaging provides simple, computationally efficient mapping; LMMSE provides superior theoretical foundation
- **Vegetation parameter estimation**: Site-specific derivation of stem factor (s) from in-situ measurements rather than literature values, improving retrieval accuracy

### Data Integration
- Multi-source data fusion: Radiometric measurements + IR surface temperature + MODIS NDVI + soil texture database + in-situ VSM validation
- Temporal synchronization: Careful handling of mixed radiometric (~1 ms) and navigation (~22 ms) data rates

### Calibration Challenges
- **Pre-flight calibration**: Over calm fresh water (standard approach, though limited validation)
- **Systematic offsets**: Different on Sept 8 vs. 9, suggesting temperature-dependent or time-varying calibration drift
- **Known issues**: Sporadic IR sensor noise (source unidentified), time-deconvolution for calibration transitions not yet applied

### Future Work (Stated)
- Revised LMMSE covariance function based on actual antenna radiation pattern
- Surface roughness correction implementation
- Separate physical temperature modeling for soil vs. vegetation
- Improved antenna temperature calibration to eliminate observed offsets

### Software
- Complete MATLAB implementation provided in appendix
- 140 × 100 LMMSE grid estimation points
- Iterative VSM retrieval using forward model inversion (convergence criterion: error < 1%, step size 0.81 K/%)

### Partnerships/Data Sources
- CU/CET (University of Colorado/Center for Environmental Testing) antenna development
- NASA Soilscape wireless sensor network infrastructure
- MODIS Terra satellite NDVI data (250 m resolution, Level 3)
- STATSO soil texture database