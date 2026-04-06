# MICROSTRIP COLINEAR ANTENNA ARRAY FOR A LOBE DIFFERENCING CORRELATION RADIOMETER (LDCR)

## Document Metadata
- Type: Technical paper / design report
- Client/Agency: NASA
- Program/Solicitation: 2012 NASA SBIR Phase II (Soil Moisture topic)
- Date: January 9, 2015 (submitted); document created/modified January 20, 2015
- BST Products/Systems Referenced: Tempest UAS, Lobe Differencing Correlation Radiometer (LDCR)
- Key Personnel: Maciej Stachura (Black Swift Technologies); Eryan Dai and A.J. Gasiewski (University of Colorado, Dept. of ECEE)

## Executive Summary
This paper presents the design, optimization, and testing of a 2x2 microstrip colinear (MiCo) antenna array operating at L-band (1.4135 GHz) for integration into Black Swift Technologies' Tempest UAS to support a Lobe Differencing Correlation Radiometer (LDCR). The antenna enables high-resolution soil moisture mapping at sub-watershed scales with spatial resolution ~15 meters and coverage of 0.6 km² per flight hour—capabilities unavailable from existing validation methods or manned platforms.

## Technical Approach

### Antenna Architecture
- **2x1 Subarray Unit**: Two radiating elements with half-wavelength (λ/2) horizontal separation, fed by a 0° 3-dB coupler via 100Ω microstrip feed lines. Each radiating element consists of five segments (each λ/2 effective wavelength) of alternating 100Ω line and ground plane, creating a thin/thick section microstrip patch array.
- **2x2 Array**: Two 2x1 subarrays stacked with quarter-wavelength (λ/4) vertical separation using styrofoam blocks. The λ/4 separation provides 90° phase shift for quadrature-phased receiver channels.

### Substrate & Materials
- Rogers 4003C duroid (two-sided), εr = 3.55, thickness = 1.534 mm
- Radiating element centerline separation: 106 mm
- Operating frequency: 1.4135 GHz (within allocated SMAP band 1400–1427 MHz)
- Fabricated in three sections with soldered board patch connections for fuselage installation

### Key Design Parameters (Table 1)
| Parameter | Value |
|-----------|-------|
| Narrow line width | 1 mm |
| Wide line width | 14 mm |
| 100Ω feed line length | 54 mm |
| Short matching line | 4 mm × 0.3 mm |
| Section length | 59.12 mm |

### Simulation & Validation
- HFSS (v15.0) models compared favorably with measured return loss (within ~4 MHz center frequency, 5 dB difference across 200 MHz band attributed to material tolerances and mesh limitations)
- Measured radiation pattern confirmed 20–47 dB rejection of horizontal radiation as designed
- Return loss better than -18.5 dB in working band achieved

### Orientation & Coupling Analysis
Three possible 2x2 configurations studied; first orientation selected (upper subarray top surface facing +z, lower facing –z) to minimize 0° coupler coupling. Mirror-symmetric design preferred.

### Frequency Tuning & Optimization
- **Frequency pull**: Proximity of subarrays and styrofoam blocks shifted resonant frequency down 20 MHz; compensated by modifying design parameters (section length reduced to 57.94 mm, matching line adjusted)
- **Mutual coupling analysis**: Tested vertical separation distances of 53.5–67.5 mm to optimize main-to-back lobe ratio; **optimum identified at 55.5 mm (2.5 mm above λ/4)**, yielding 19.6 dB average main-to-back ratio
- **Practical tuning method**: Styrofoam blocks achieved 5 MHz frequency reduction; silicon RTV strips (εr = 2.54) identified as preferred aerodynamically-compatible tuning method

## Products & Capabilities Described

### Tempest UAS
- Lightweight unmanned aerial system designed to carry the LDCR payload
- Fuselage-integrated antenna array with curved surface requiring conform-fitting styrofoam separation blocks
- Enables low-cost, high-spatial-resolution soil moisture surveys

### Lobe Differencing Correlation Radiometer (LDCR)
- Lightweight L-band radiometer with broad nadir and zenith-viewing beams
- Measures soil moisture to 5–10 cm depth
- Provides spatial resolution of ~15 meters at platform altitude
- Coverage: >0.6 km² in one flight hour
- Cost-effective alternative to in situ networks or manned airborne systems
- Quadrature-phased receiver requiring 90° phase-shifted antenna channels (provided by λ/4 subarray separation)

## Use Cases & Applications

### Primary Application: Soil Moisture Mapping
- **SMAP Validation**: Sub-watershed (~km scale) coverage with high spatial resolution (~15 m) to validate NASA's Soil Moisture Active/Passive (SMAP) mission data (launched 2015)
- **Precision Agriculture**: Diurnal soil moisture measurements on arbitrary timescales (not limited to fixed SMAP crossing times)
- **Hydrological Studies**: Evaporation and transpiration measurements; boundary layer heat transport analysis
- **Water Resource Management**: Flood runoff prediction; agricultural planning
- **Climate/Weather**: Convective weather development; precipitation prediction

### Measurement Capability Advantage
- Existing methods limited to either in situ point measurements or airborne sensors requiring manned aircraft
- LDCR on Tempest enables unmanned, autonomous sub-watershed scale surveys at comparatively low operator cost

## Key Results

### Performance Metrics Achieved
1. **Return Loss**: Measured -18.5 dB or better across 1400–1427 MHz working band
2. **Radiation Pattern**: 20–47 dB rejection of horizontal radiation; strong end-fire beams in nadir and zenith directions with ±90° phase shift
3. **Resonant Frequency Tuning**: 
   - Original 2x1 subarray: 1.4135 GHz
   - Modified design (compensating for subarray proximity): 1.4335 GHz
   - Further tuned to 1.417 GHz using styrofoam blocks
4. **Main-to-Back Lobe Ratio**: Maximum 19.6 dB at 55.5 mm vertical separation (optimal)
5. **Mutual Coupling**: Quantified as function of vertical separation; λ/4 separation insufficient; 2.5 mm additional separation required

### Design Modifications Validated (Table 2)
| Parameter | Before | After |
|-----------|--------|-------|
| Operating center frequency | 1.4135 GHz | 1.4335 GHz |
| Short matching line length | 4 mm | 4.2 mm |
| Short matching line width | 0.3 mm | 0.5 mm |
| Section lengths | 59.12 mm | 57.94 mm |

### Integration Achievement
- Complete 2x2 antenna array successfully integrated into Tempest fuselage mock-up with curved-conform styrofoam separation blocks
- Measured resonant frequency post-integration: 9.5 MHz above simulated (within acceptable tolerance; remaining error <2–4 MHz from material/mesh effects)
- Practical frequency tuning via dielectric loading identified and validated

## Notable Details

### Manufacturing & Integration Challenges Addressed
1. **Three-section fabrication** with soldered board patch connections enables installation in confined fuselage space
2. **Styrofoam separation blocks** serve dual purpose: mechanical stabilization and resonant frequency tuning
3. **Frequency compensation workflow** developed: design modification → fabrication → measurement validation → tuning refinement
4. **Aerodynamic consideration**: Silicon RTV strips preferred over foam blocks for final tuning to minimize drag

### Collaboration & Expertise
- University of Colorado (Dept. of ECEE, Prof. A.J. Gasiewski) provided antenna design expertise and HFSS modeling
- Black Swift Technologies integrated design into Tempest platform and managed overall development

### Design Philosophy
- **Lobe differencing approach**: λ/2 horizontal separation creates null at horizon; λ/4 vertical separation (plus 2.5 mm optimization) creates phased end-fire beams
- **Omnidirectional elements with phased arrangement**: Simpler than complex individual element design; enables quadrature-phased receiver architecture inherent to radiometer

### Specifications Summary
| Specification | Value |
|---------------|-------|
| Operating frequency | 1.4135 GHz (SMAP L-band: 1400–1427 MHz) |
| Array configuration | 2×2 (four elements total) |
| Horizontal element separation | λ/2 (106 mm) |
| Vertical subarray separation | 55.5 mm (λ/4 + 2.5 mm) |
| Radiation pattern | End-fire nadir/zenith, horizon null |
| Main-to-back lobe ratio | 19.6 dB (band-averaged) |
| Return loss | ≥18.5 dB (working band) |
| Substrate | Rogers 4003C (εr = 3.55, 1.534 mm thick) |
| Phase shift between ports | 90° |
| Soil moisture penetration depth | 5–10 cm |
| Measurement spatial resolution | ~15 m (at platform altitude) |
| Coverage area | >0.6 km² per flight hour |

### Status & Next Steps Noted
- Frequency offset (9.5 MHz measured vs. simulated) "still being investigated" but deemed acceptable
- Dielectric loading tuning via silicon RTV strips identified as preferred method (vs. foam blocks) for aerodynamics
- Document represents Phase II deliverable (Quarter 3) of 2012 NASA SBIR contract