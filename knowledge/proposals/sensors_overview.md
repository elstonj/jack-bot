# Sensors Overview

## Document Metadata
- Type: Technical specification/requirements document
- Client/Agency: NASA
- Program/Solicitation: 2018 SBIR - Terrain Following (Phase I)
- Date: 2018-10-01 to 2018-10-08
- BST Products/Systems Referenced: None explicitly (document evaluates sensor options for potential integration)
- Key Personnel: Austin Anderson (commentator)

## Executive Summary
This document evaluates sensor technologies suitable for autonomous terrain-following flight, establishing long-range and short-range obstacle detection requirements and comparing performance, SWaP-C (Size, Weight, Power, Cost), and processing needs across multiple sensor families including cameras, thermal imagers, lidar, radar, and lasers.

## Sensing Architecture
The document establishes a two-tier detection strategy modeled on automotive ADAS systems:
- **Long-range detection**: Coarse detection of large obstacles at distance for early corrective action
- **Short-range detection**: Fine detection of smaller obstacles at close range for terminal collision avoidance

---

## Long-Range Sensor Requirements

| Parameter | Value | Type |
|-----------|-------|------|
| Min Range | 10 m | Minimum |
| Max Range | 100 m | Maximum |
| Obstacle Size | 10 m² | Minimum |
| Obstacle Height | 5 m | Minimum |
| Range Resolution | 50 cm | Minimum |
| Field of View (Az, El) | 45°, 17° | Minimum (TBR) |
| Update Rate | 5 Hz | Minimum |
| Detection Rate | 99.9% | Minimum |

*Note: Internal comments indicate 50m min range was "ludicrously conservative" and FOV values are placeholder estimates requiring review.*

---

## Short-Range Sensor Requirements

| Parameter | Value | Type |
|-----------|-------|------|
| Min Range | 1 m | Minimum |
| Max Range | 20 m | Maximum |
| Obstacle Size | 1 m² | Minimum |
| Obstacle Height | 2 m | Minimum |
| Range Resolution | 5 cm | Minimum |
| Field of View (Az, El) | 60°, 20° | Minimum (TBR) |
| Update Rate | 20 Hz | Minimum |
| Detection Rate | 99% | Minimum |

---

## Products & Capabilities Described

### Single Cameras (Visible Light)

**Characteristics:**
- Small, light, low power consumption
- Require substantial processing for obstacle detection
- Performance highly dependent on visual diversity and lighting conditions

**Performance by Mission Type:**
- **Good performance**: Canopy sampling, mountain sampling, farm sampling (clear weather, good visual diversity), safe landing/takeoff with visual diversity
- **Poor performance**: Arctic/oceanic missions (lack visual diversity), volcanic plumes, fog, heavy rain, snow, icing, water on lens

**Obstacle Performance:**
- Large obstacles (structures, boulders, ridges, wind turbines): easily identified
- Vegetation/trees: detectable in multi-image depth maps
- **Challenge**: Small/thin structures (power lines)

**Processing Requirements:**
- Very high-density processing needed for depth maps and visual odometry
- Image data up to 50 Hz requires USB 3.0, GigE, or PCIe
- Deep learning: requires GPUs or dedicated accelerators with millions of computations per estimate
- Significant RAM and storage for image buffering

**Example Parts & SWaP-C:**

| Part | Size | Weight | Power | Cost |
|------|------|--------|-------|------|
| Ximea MC124CG-SY | 26×26×33 mm | 38g | 3.25 W | $3,055 |
| LI-USB30-C570X | 26×26×38 mm | 32g | 1.12 W | $699 |
| LI-USB30-M021 | 26×26×38 mm | 22g | 0.85 W | $229 |

**Critical Requirements:**
- **Shutter Type**: Global shutter (prevents motion blur critical for odometry/matching; rolling shutter may have higher pixel density but suffers from blur)
- **Focal Length**: Inversely proportional to FOV and stereo range resolution; directly proportional to disparity resolution
- **Field of View**: Wider FOV shows more obstacles and aids digital stabilization, but maps fixed-size obstacles to fewer pixels (harder detection); narrow FOV requires tighter pointing/stabilization
- **Imager Size**: Affects maximum stereo disparity
- **Pixel Count**: Critical for algorithmic performance; dictates minimum realizable disparity and pixel occupancy of objects; scales processing requirements
- **Color vs. Monochromatic**: Monochromatic produces 1/3 data of color; reduces processing if sufficient for task
- **Dynamic Range**: Determines lighting scenario tolerance
- **Frames Per Second**: Higher rates identify obstacles faster but generate more data

**Target Specs:**
- Global shutter
- 2M pixels minimum
- 4.5 µm maximum pixel size
- 50 dB dynamic range (10 bits)
- 5 Hz minimum frame rate
- Color preferred for deep learning
- 5.5 mm focal length, f/1.8 aperture
- 76°/64.5°/51° FOV (D/H/V)
- Max 26×26×33 mm, 50g, 4W, $1,000

---

### Thermal Cameras

**Characteristics:**
- Produces temperature-based imagery
- Lower resolution and limited performance compared to standard cameras
- Simpler processing than visible light (binning sufficient for many tasks)

**Performance by Mission Type:**
- **Good**: Farm mapping (man-made structure identification), populated areas
- Unlikely suitable for odometry/depth mapping

**Obstacle Performance:**
- Excels at detecting warm objects: power lines, humans, man-made structures, vehicles
- Shows contrast against environmental background

**Processing Requirements:**
- Lower resolution (single channel) produces much smaller images than comparably-priced visible cameras
- Simple binning algorithm produces pixel maps of objects of interest
- Simpler identification algorithms than deep learning networks

**Example Parts & SWaP-C:**

| Part | Size | Weight | Power | Cost |
|------|------|--------|-------|------|
| FLIR Lepton | 12.5×12.5×10 mm | 5g | 0.16 W | $239.95 |
| FLIR Duo | 41×59×29.6 mm | 84g | 3.3 W | $1,000 |
| FLIR Duo Pro R | 85×81.3×68.5 mm | 325g | 10 W | $7,600 |

**Target Specs:**
- 4.8k pixels minimum
- 17 µm maximum pixel size
- 40 dB dynamic range (8 bits)
- 5 Hz minimum frame rate
- 5.5 mm focal length, f/1.8 aperture
- 50°/60° FOV (H/D)
- Max 41×60×30 mm, 50g, 4W, $1,000

---

### Stereo Cameras (Visible Light)

**Characteristics:**
- Two synchronized cameras producing simultaneous depth images via visual disparity
- Many commercial systems available with integrated processing accelerators
- Simplified processing compared to single-camera depth mapping but less design flexibility

**Performance:** Same as single cameras

**SWaP-C:**
Smaller and cheaper than single cameras due to widespread mobile robotics use.

**Example Parts & SWaP-C:**

| Part | Size | Weight | Power | Cost |
|------|------|--------|-------|------|
| RealSense D435 | 90×25×25 mm | 72g | 3.5 W | $179 |
| ZED-M | 175×30×30 mm | 159g | 2 W | $449 |
| ZED | 124.5×30.5×26.5 mm | 63g | 2 W | $449 |

**Target Specs:**
- 10 m minimum range
- 10 Hz minimum update rate
- 1280×720 minimum pixels
- 80°×50° FOV (H×V)
- Max 200×40×40 mm, 160g, 4W, $500

**Processing:** Similar to single cameras with baseline requirement for stereo matching

---

### Structured Light Cameras

**Characteristics:**
- Similar to stereo cameras but include active structured light component
- Struggle in bright lighting and inclement weather

**Performance:** Same as single/stereo cameras

**Processing:** Same as stereo cameras

**Example Parts & SWaP-C:**

| Part | Size | Weight | Power | Cost |
|------|------|--------|-------|------|
| RealSense D435 | 90×25×25 mm | 72g | 3.5 W | $179 |

**Target Specs:** Same as stereo cameras

---

### 1D Lasers (Single Point Range Sensors)

**Characteristics:**
- Very accurate, rapid range measurements to fixed points
- Narrow beamwidth leaves large unmapped regions
- Multiple lasers can build sparse point clouds when corrected with IMU

**Performance by Mission Type:**
- **Excellent**: Areas without significant vegetation, farm sampling, mountain sampling, landing/takeoff
- **Challenging**: Canopy sampling (varied range response), arctic/oceanic sampling (snow/water reflectivity dependent), volcanic plumes
- **Weather-independent** (mostly)

**Obstacle Performance:**
- **Excellent**: Solid large obstacles (structures, utility poles, wind turbines, vehicles, boulders, ridge lines)
- **Challenging**: Foliage, dense vegetation, power lines (due to narrow beam width)

**Processing Requirements:**
- Minimal processing (single range measurements)
- Array systems or temporal filtering may require light estimation

**Example Parts & SWaP-C:**

| Part | Size | Weight | Power | Cost |
|------|------|--------|-------|------|
| LightWare LW20/C | 20×30×35 mm | 20g | 0.55 W | $370 |

**Target Specs:**
- 100 m minimum range
- 20 Hz minimum update rate
- 0.2° maximum beamwidth
- Max 20×30×35 mm, 20g, 1W, $400

---

### Lidar (Scanning Laser Rangefinder)

**Characteristics:**
- Single or multi-channel scanning laser producing point clouds
- Works well across most mission scenarios
- Larger, heavier, more expensive than single lasers

**Performance by Mission Type:**
- **Excellent**: All missions except potentially arctic/oceanic (surface reflection), volcanic plumes

**Obstacle Performance:**
- **Excellent**: All obstacle types
- Better than single lasers in canopies (point cloud catches minimum distances across canopy)
- **Excellent**: Power line detection

**Processing Requirements:**
- Point cloud filtering/clustering
- More significant data generation than single lasers
- Requires larger RAM and storage
- Does not require pixel matching or deep learning

**Example Parts & SWaP-C:**

| Part | Size (D/H) | Weight | Power | Cost |
|------|-----------|--------|-------|------|
| Velodyne PUCK VLP-16 | 103/72 mm | 830g | 8 W | $4,000 |
| LightWare SF40/C | 79/91 mm | 270g | 30 W | $1,000 |

**Target Specs:**
- 100 m minimum range
- 5 Hz minimum update rate
- 180° minimum horizontal FOV
- ±10° minimum vertical FOV
- Max 20×30×35 mm, 450g (ideally 225g), 10W typical, $5,000
- Weight is significantly over budget requirement

---

### Radar (Electronically Scanning)

**Characteristics:**
- Rapid volumetric scanning capability
- Works in all weather, day/night
- Can be coarse for fine obstacle avoidance
- May struggle with low-RCS targets and wind turbines (Doppler effects)

**Performance by Mission Type:**
- **Excellent**: All scenarios

**Obstacle Performance:**
- **Excellent**: Large RCS targets at great range
- **Challenging**: Small RCS obstacles (tree branches,