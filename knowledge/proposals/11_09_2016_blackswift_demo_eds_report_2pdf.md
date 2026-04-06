# Black Swift Technologies Demo EDS Report

## Document Metadata
- Type: Photogrammetry Quality Report
- Client/Agency: Internal/Demo (GTK Survey project)
- Program/Solicitation: UASUSA / GTK Survey
- Date: November 9, 2016 (survey date); November 28, 2016 (processed)
- BST Products/Systems Referenced: Black Swift UAS (implied as data collection platform)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This is a Pix4D photogrammetry quality report documenting the processing results from a Black Swift UAS aerial survey conducted on November 9, 2016. The survey captured 450 images over a 0.1633 km² area with 1.53 cm ground sampling distance using an ILCE-5100 RGB camera, achieving high-quality orthomosaic and digital surface model (DSM) outputs with strong calibration and geolocation accuracy.

## Technical Approach
The workflow involved:
1. **Image Acquisition**: 450 RGB images captured with Sony ILCE-5100 camera (16mm lens, 6000x4000 resolution)
2. **Photogrammetric Processing**: Pix4D Discovery v3.0.13 software
3. **Calibration**: Bundle block adjustment with automatic tie point extraction and camera parameter optimization
4. **Georeferencing**: Ground control points (GCPs) used for absolute positioning
5. **Product Generation**: Orthomosaic and DSM creation at 1 cm/pixel resolution

## Products & Capabilities Described

### Orthomosaic and Digital Surface Model (DSM)
- **Output Resolution**: 1.53 cm/pixel GSD
- **Coverage Area**: 0.1633 km² (16.33 hectares, 40.36 acres)
- **Processing**: Full 100% image calibration with densification; includes noise filtering and sharp surface smoothing

### Camera System
- **Camera**: Sony ILCE-5100 with 16mm F2.8 lens
- **Resolution**: 6000 x 4000 pixels
- **Sensor Dimensions**: 23.333 mm x 15.556 mm
- **Optimized Focal Length**: 3964.042 pixels (15.416 mm)

## Key Results

### Image Processing Quality
- **Keypoint Detection**: Median 92,045 keypoints per image
- **Keypoint Matching**: Median 52,434 matches per calibrated image
- **Total 3D Points**: 6,181,308 points generated from bundle block adjustment
- **Reprojection Error**: 0.256 pixels (excellent)
- **Image Calibration**: 450/450 images (100%) successfully calibrated and geolocated

### Positional Accuracy

**Absolute Camera Position/Orientation Uncertainties (Mean ± Sigma)**:
- X: 0.119 ± 0.020 m
- Y: 0.121 ± 0.021 m
- Z: 0.148 ± 0.033 m
- Omega: 0.071 ± 0.007 degrees
- Phi: 0.060 ± 0.014 degrees
- Kappa: 0.035 ± 0.002 degrees

**Relative Camera Position/Orientation Uncertainties (Mean ± Sigma)**:
- X: 0.028 ± 0.005 m
- Y: 0.035 ± 0.007 m
- Z: 0.050 ± 0.029 m
- Omega: 0.043 ± 0.013 degrees
- Phi: 0.049 ± 0.023 degrees
- Kappa: 0.012 ± 0.004 degrees

### Ground Control Point Performance
- **GCPs Evaluated**: 11 check points
- **Marked Inaccurate**: 1 (90.9% acceptance rate)
- **Mean Error**: 2.23 m (X), -2.08 m (Y), -1.46 m (Z)
- **RMS Error**: 2.37 m (X), 2.16 m (Y), 1.61 m (Z)
- **Relative Geolocation Accuracy**: 
  - 97.33% of images within ±2.0 m in X
  - 100% of images within ±2.0 m in Y
  - 94.67% of images within ±2.0 m in Z

### Image Overlap
- Strong multi-image overlap achieved across survey area
- Green areas indicate 5+ image overlap per pixel (good quality zones)
- Red/yellow areas with low overlap minimal

## Notable Details

### Technical Specifications
- **Survey Area**: Small-scale (0.1633 km²) demonstration survey
- **Ground Sampling Distance**: 1.53 cm/pixel—excellent resolution for detailed mapping
- **Processing Hardware**: Intel i7-4710HQ, 16GB RAM, Windows 10
- **Coordinate System**: WGS84 / UTM zone 13N

### Processing Performance
- Camera parameter optimization showed only 3.65% relative difference between initial and optimized values, indicating stable calibration
- 23,426,064 total 2D keypoint observations processed
- Majority of 3D points (3.12 million) observed in 2 images; significant points (up to 28 images) for dense coverage verification

### Quality Indicators
- High-quality orthomosaic generation confirmed by:
  - Low reprojection error (0.256 pixels)
  - Consistent keypoint matching across all images
  - Strong absolute and relative position uncertainties within acceptable ranges
  - Most GCPs verified in 6/6 calibrated images

**Assessment**: This report demonstrates successful high-resolution UAS survey execution and processing, validating Black Swift's capability to conduct precise aerial mapping missions with sub-centimeter ground sampling distance and meter-level absolute accuracy suitable for detailed geospatial analysis applications.