# AUSurv ED's Survey Quality Report

## Document Metadata
- Type: Photogrammetry processing report (Pix4Dmapper Pro quality assessment)
- Client/Agency: AUSurv (implied from project name)
- Program/Solicitation: GTK Survey (implied from file path)
- Date: Generated 2016-07-20; Document created 2016-12-05
- BST Products/Systems Referenced: None explicitly (UAS data collection and processing)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This is a Pix4Dmapper Pro photogrammetry quality report documenting the processing of 253 calibrated aerial images from a UAS survey mission. The survey achieved 1.84 cm ground sampling distance across 0.1908 km² with 100% image calibration and strong geometric overlap, producing high-quality orthomosaic and digital surface model outputs suitable for precision mapping applications.

## Technical Approach
Survey data processed using Pix4Dmapper Pro v2.0.100 photogrammetry software with the following specifications:

**Image Calibration:**
- 253 out of 290 images calibrated (100% of usable images; 37 disabled)
- All 290 images geolocated
- Camera model: Sony ILCE-7R with 28mm lens (7360×4912 RGB)
- 5.97% relative difference between initial and optimized internal camera parameters

**Feature Matching & 3D Reconstruction:**
- Median 89,226 keypoints per image
- Median 14,912.1 matched keypoints per calibrated image
- 4,075,416 total 2D keypoint observations
- 1,685,901 3D points generated
- Mean reprojection error: 0.283345 pixels

**Bundle Block Adjustment:**
- 3D point distribution: 1,326,978 points observed in 2 images; decreasing to 1 point observed in 28 images
- Strong image overlap: green areas (5+ image overlap) dominate orthomosaic

## Products & Capabilities Described

### Orthomosaic & Digital Surface Model (DSM)
- High-resolution orthomosaic generated
- Sparse DSM created before densification
- Coverage: 0.1908 km² / 19.0814 hectares / 47.1757 acres
- Ground Sampling Distance: 1.84 cm / 0.72 inches (very high precision)

### Ground Control Point (GCP) Georeferencing
- 11 GCPs established with 0.020m XY/Z accuracy specification
- Mean geolocation error: 1.147 m (X), -0.352 m (Y), -0.016 m (Z)
- RMS error: 1.159 m (X), 0.455 m (Y), 0.129 m (Z)
- All GCPs verified/marked across calibrated images (7-12 per GCP)

### Image Overlap Analysis
- Multiple areas with 5+ image overlap (quality indicator)
- Some red/yellow zones indicating lower overlap (1-2 images per pixel)
- Dense linking between images confirms strong network geometry

## Use Cases & Applications
- Precision UAS surveying for mapping applications
- Survey-grade orthomosaic production
- Digital elevation model generation
- Geospatial data collection with georeferencing

## Key Results

**Processing Quality Metrics:**
- 100% calibration success rate (253/253 usable images)
- Minimal keypoint extraction variation (Min: 40,926; Max: 94,886; Mean: 87,164)
- Strong matching consistency (Min matches: 5,489; Max: 32,507; Median: 14,912)
- Absolute geolocation variance RMS: 0.110 m (X), 0.143 m (Y), 0.238 m (Z)

**Relative Geolocation Accuracy:**
- 27.27% of images within ±1.0m relative error (X)
- 24.51% of images within ±1.0m relative error (Y)
- 11.46% of images within ±1.0m relative error (Z)
- 74.31% of images within ±3.0m relative error (X)

**No inaccurate images or check points flagged** (0 out of 253 images, 0 out of 11 check points)

## Notable Details

**Hardware & System Configuration:**
- Processing completed on Intel i7-4710HQ CPU, 16GB RAM, Windows 10 Home 64-bit
- GPU: Intel HD Graphics 4600
- Coordinate systems: WGS84 (image); WGS84/UTM zone 13N (GCPs and output)

**Camera Optimization:**
- Focal length optimized from 5888 to 5536.413 pixels
- Principal point adjustments: X (3680→3666.917), Y (2456→2274.618 pixels)
- Radial distortion parameters computed: R1 (-0.032), R2 (0.040), R3 (-0.026)
- Tangential distortion: T1 (0.001), T2 (-0.001)

**Processing Parameters:**
- Keypoint extraction: Full resolution, automatic targeted number
- Matching strategy: Geometric verification disabled; standard calibration with all parameter optimization enabled; rematch enabled
- Aerial grid/corridor matching applied

This report demonstrates successful execution of a high-precision UAS survey with excellent image geometry, strong control, and minimal registration error—suitable for professional mapping and surveying applications.