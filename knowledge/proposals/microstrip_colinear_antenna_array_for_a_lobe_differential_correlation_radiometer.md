# Microstrip Colinear Antenna Array for a Lobe Differential Correlation Radiometer (LDCR)

## Document Metadata
- **Type:** Technical report / deliverable (Phase II Quarter 2)
- **Client/Agency:** NASA
- **Program/Solicitation:** 2012 SBIR Phase II - Soil Moisture
- **Date:** October 17, 2014
- **BST Products/Systems Referenced:** Tempest UAS, LDCR (Lobe Differencing Correlation Radiometer)
- **Key Personnel:** Maciej Stachura (BST), Eryan Dai (CU), A.J. Gasiewski (CU)

## Executive Summary
This document presents the design, optimization, and testing of a 2x2 microstrip colinear (MiCo) antenna array operating at L-band (1.4135 GHz) for integration into the Tempest UAS. The antenna enables the LDCR system to perform high-resolution soil moisture mapping at ~15 m spatial resolution with sub-watershed coverage, validating NASA's SMAP mission data.

## Technical Approach

### Antenna Architecture
- **2x1 Subarray Unit:** Two radiating elements with half-wavelength (λ/2) horizontal separation, fed by a 0° 3-dB coupler. Each element comprises five segments of half effective wavelength, creating an alternating microstrip patch array design.
- **2x2 Complete Array:** Two 2x1 subarrays stacked vertically with quarter-wavelength (λ/4) separation via styrofoam blocks. The λ/4 vertical spacing creates 90° phase shift for quadrature-phased LDCR receiver channels.

### Operating Frequency
- Center frequency: 1.4135 GHz (SMAP allocated band 1400–1427 MHz, 27 MHz working bandwidth)
- Choice of L-band selected for compact design and soil moisture penetration (~5–10 cm under most conditions)

### Key Design Parameters
- Fabrication: Two-sided Rogers 4003C duroid substrate
- Feed lines: 100Ω microstrip lines with high impedance matching sections
- Radiation pattern: Each element omnidirectional; array exhibits null at horizon, broadside patterns in vertical/horizontal directions
- Measured horizontal radiation rejection: 20–47 dB

### Optimization & Tuning
1. **Frequency Pull Compensation:** Initial 2x2 array exhibited 20 MHz downward frequency shift due to mutual coupling and styrofoam block proximity; design dimensions were modified to compensate.
2. **Vertical Separation Optimization:** Tested separation distances of 53.5, 55.5, 57.5, 59.5, 61.5, and 67.5 mm to minimize mutual coupling and maximize main-to-back lobe ratio. Optimal separation identified at **55.5 mm** (λ/4 + 2.5 mm).
3. **Resonant Frequency Tuning Methods:**
   - Blue builder's styrofoam blocks: achieved 5 MHz reduction with return loss ≥ –18.5 dB
   - Silicon RTV strips (εr = 3.6): preferred for aerodynamic considerations

### Validation
- 2x1 prototype measured return loss compared favorably with HFSS simulations (v15.0), with ~4 MHz center frequency difference tuned out via dielectric loading
- 2x2 array integrated into Tempest fuselage mock-up showed 9.5 MHz measured resonant frequency offset vs. simulation (partially attributed to board material tolerances ~2 MHz; remainder being investigated)

## Products & Capabilities Described

### Tempest UAS
- Lightweight unmanned aerial system serving as platform for integrated LDCR payload
- Fuselage curvature accommodated via custom-fitted styrofoam separation blocks
- Antenna mounted on fuselage exterior; couplers pass through fuselage walls via slots

### LDCR (Lobe Differencing Correlation Radiometer)
- **Purpose:** High-resolution soil moisture mapping at arbitrary diurnal times for SMAP validation, precision agriculture, and evapotranspiration studies
- **Performance:** 
  - Spatial resolution: ~15 m
  - Coverage area: >0.6 km² per hour of flight
  - Soil moisture penetration depth: 5–10 cm
  - Sub-watershed (~1 km scale) coverage capability
  - Lightweight design suitable for UAS deployment at comparatively low operational cost
- **Antenna Function:** Broad-beam radiometer with lobes viewing both nadir and zenith via ±90° phase-shifted subarray pairs

## Use Cases & Applications

1. **SMAP Mission Validation:** Provide ground-truth measurements at finer spatial and temporal resolution than satellite products (which offer fixed crossing times and 5 km resolution)
2. **Precision Agriculture:** Monitor soil moisture at field scales (~15 m) for irrigation optimization
3. **Hydrological & Biogeochemical Studies:** Support boundary layer heat transport, evapotranspiration, and convective weather development studies
4. **Scaling Studies:** Enable validation of soil moisture retrieval algorithms across spatial scales
5. **Flood Runoff Prediction & Water Resource Management:** Provide high-resolution moisture data for improved hydrological models

## Key Technical Results

### Measured Performance
- **2x1 Subarray:** Input return loss agreement between measurement and HFSS simulation generally good across 27 MHz band; ~5 dB lower measured return loss across 200 MHz band (origin under investigation but acceptable)
- **2x2 Array (Optimized Separation at 55.5 mm):**
  - Average main-to-back lobe ratio maximized across working frequency band
  - Mutual coupling minimized via optimal vertical spacing
  - Radiation patterns (±90° phase shift): good end-fire beams in nadir/zenith directions; >20 dB horizon rejection
- **Frequency Tuning:** Silicon RTV dielectric loading capable of resonant frequency adjustment suitable for aerodynamic integration

### Array Factor Analysis
Using measured S-matrix and derived Y-matrix elements, the main-to-back lobe ratio was mathematically optimized by adjusting vertical separation (Δh) to counter mutual coupling effects (nonzero Y₁₂).

## Notable Details

1. **Three-Section Fabrication:** Antenna divided into three sections for installation in Tempest fuselage; sections soldered together on-board
2. **Styrofoam Dual Function:** Separation blocks serve both as mechanical supports and frequency tuning elements; designed to conform to fuselage curvature
3. **Phase Relationship:** Quarter-wave vertical separation providesthe required 90° phase shift for quadrature receiver channels integral to LDCR design
4. **Aerodynamic Consideration:** Transition from foam blocks to thin silicon RTV strips for tuning to reduce drag
5. **Design Robustness:** Manufacturing tolerances characterized; tuning methods developed to accommodate variations without performance loss

## Gaps & Notes
- Origin of 5 dB lower return loss in measured 2x1 subarray (across 200 MHz band) not fully resolved but deemed acceptable
- 9.5 MHz resonant frequency offset in fuselage-integrated array partially unexplained (~7.5 MHz after accounting for material tolerances); investigation ongoing but problem manageable via dielectric tuning