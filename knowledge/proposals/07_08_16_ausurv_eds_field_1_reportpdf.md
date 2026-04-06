# 07_08_16 ausurv eds field 1_report.pdf

## Document Metadata
- Type: Photogrammetry Quality Report (Pix4Dmapper Pro processing output)
- Client/Agency: Not specified (internal BST field survey)
- Program/Solicitation: GTK Survey / UASUSA project
- Date: Processed 2016-07-20; Report generated 2016-12-05
- BST Products/Systems Referenced: UAS (uncrewed aircraft system) with aerial survey capability
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This is a technical quality report from Pix4Dmapper Pro photogrammetry software documenting the processing and georeferencing results of 247-252 aerial survey images collected on 07_08_16. The survey achieved excellent calibration (100% of 247 images), high-resolution ground sampling (1.85 cm GSD), and reliable georeferencing using 11 ground control points across a ~18.66-hectare survey area.

## Technical Approach
- **Image Acquisition**: 252 aerial images captured with Sony ILCE-7R camera at 28mm focal length (7360×4912 RGB)
- **Processing Software**: Pix4Dmapper Pro v2.0.100
- **Calibration Method**: Standard calibration with optimization of all internal and external camera parameters
- **Georeferencing**: Ground Control Points (GCPs) and automatic tie points
- **Coordinate Systems**: WGS84 / UTM Zone 13N for output

## Products & Capabilities Described
**BST UAS Survey System**
- Equipped with Sony ILCE-7R full-frame camera (35.961mm × 24.000mm sensor)
- Capable of capturing high-resolution aerial imagery for photogrammetric processing
- Demonstrates capability for precision mapping and surveying operations

## Use Cases & Applications
- **Geographic/Terrain Survey**: Mapping of terrain and surface features with centimeter-level precision
- **Orthomosaic Generation**: Creation of georeferenced aerial mosaics
- **Digital Surface Model (DSM) Production**: 3D elevation data generation
- **GTK Survey Project**: Part of larger UASUSA survey initiative (specific application/location not detailed in this report)

## Key Results
**Image Processing Quality:**
- 247 of 252 images successfully calibrated (100% of usable images)
- 5 images disabled (quality control)
- Median 88,330 keypoints per image detected
- Median 22,094.9 matched keypoints per calibrated image

**Geospatial Accuracy:**
- **Ground Sampling Distance (GSD)**: 1.85 cm / 0.73 inches
- **Total Area Covered**: 0.1866 km² (18.6615 hectares / 46.1375 acres / 0.0721 sq mi)
- **Camera Parameter Optimization**: 2.61% relative difference between initial and optimized internal parameters
- **Bundle Block Adjustment**: 5,374,690 2D keypoint observations; 2,142,410 3D points; Mean reprojection error 0.257 pixels

**Ground Control Point Validation:**
- 11 GCPs established with 0.020m XY/Z accuracy specification
- All 11 check points verified (0 marked as inaccurate)
- Mean GCP errors: X = 0.406m, Y = 0.654m, Z = 0.509m RMS
- Individual GCP projection errors ranged 0.489–2.484 pixels

**Image Overlap & Coverage:**
- Excellent overlap in green areas (5+ images per pixel) across most survey area
- Some red/yellow areas indicating lower overlap (1–2 images), potential for quality variation
- Strong keypoint matching links between sequential images (Figure 5)

**3D Point Distribution:**
- Majority of 3D points observed in 2–3 images (1,617,738 in 2 images; 302,292 in 3 images)
- Robust multi-image observations up to 28 images for highly redundant points

## Notable Details
- **Hardware**: Processing conducted on Intel i7-4710HQ CPU with 16GB RAM and Intel HD Graphics 4600 GPU
- **Operating System**: Windows 10 Home 64-bit
- **Relative Geolocation Variance**: Within ±1m for 24.29% of images (X), 15.38% (Y), 19.43% (Z); within ±3m for ~65% of images, indicating reliable but variable geolocation consistency
- **Absolute Geolocation**: RMS errors X: 0.143m, Y: 0.170m, Z: 0.160m
- **Camera Calibration Details**: Sony ILCE-7R optimized focal length 5580.851 pixels (initial: 5730.670); principal point and distortion coefficients optimized during processing
- This represents BST's demonstrated UAS photogrammetry and high-precision surveying capability suitable for small-area (hectare-scale) detailed mapping