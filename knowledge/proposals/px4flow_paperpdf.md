# PX4FLOW: Open Source Optical Flow Sensor Paper

## Document Metadata
- Type: Academic research paper / technical reference
- Authors: Dominik Honegger, Lorenz Meier, Petri Tanskanen, Marc Pollefeys (ETH Zürich)
- Date: Pre-2019 (referenced in BST's 2019 SBIR Phase I proposal)
- Context: Filed in BST's NOAA 2019 SBIR Phase I project references
- Relevance to BST: Technical reference for optical flow-based navigation systems

## Executive Summary
PX4FLOW is an open-source, open-hardware optical flow sensor system based on a CMOS machine vision camera and ARM Cortex M4 microcontroller. It performs real-time optical flow processing at 250 Hz with high light sensitivity suitable for indoor and outdoor UAV navigation, addressing limitations of mouse-sensor-based alternatives that require strong lighting.

## Technical Approach

### System Architecture
- **Image Sensor**: Aptina MT9V034 CMOS imager (6 µm pixel size, up to 60 FPS at full 752H×480V resolution)
- **Processing**: STM32F407 32-bit ARM Cortex M4F microcontroller at 168 MHz (192 KB RAM, hardware floating-point unit)
- **Optical Flow Algorithm**: Sum of Absolute Differences (SAD) block matching at 250 Hz update rate
- **Sensor Fusion**: Onboard L3GD20 MEMS gyroscope (16-bit, up to 2000°/s) for angular rate compensation; optional ultrasonic sensor for distance measurement and metric scaling

### Processing Pipeline
1. **Frame Grabbing**: DMA with double buffering captures pixel data at 4×4 pixel binning (resolution 188H×120V at 250 Hz)
2. **Flow Computation**: SAD block matching with 8×8 pixel blocks, ±4 pixel search range, 64 sample points per frame
3. **Subpixel Refinement**: Bilinear interpolation for half-pixel accuracy
4. **Rotation Compensation**: Gyroscope-based correction of rotational motion field components
5. **Metric Scaling**: Distance-based conversion to translational velocity (equation: vm,trans = v × Z / f)

### Lens & Optics
- 16 mm M12 lens with 21° FOV and IR-block coating
- Minimal radial distortion (0.15 pixels) within operating subsampled patch
- Optional wide-angle lens (180° FOV) for corridor navigation applications

## Products & Capabilities Described

### PX4FLOW Sensor Specifications
| Parameter | Value |
|-----------|-------|
| **Size** | 45 mm × 35 mm |
| **Power Consumption** | 115 mA @ 5.0V (0.575 W) |
| **Update Rate** | 250 Hz |
| **Maximum Flow Velocity** | ±1.5 rad/s (±86°/s) |
| **Resolution (standard)** | 64×64 pixels at 250 Hz |
| **Resolution (wide aspect)** | 120H×32V for corridor navigation |
| **Subsampled Resolution** | 188H×120V (4× binning) |

### Key Capabilities
- **High light sensitivity**: Operates at 6–45 Lux (CCFL), vs. 47–800 Lux for mouse sensors
- **Real-time processing**: 250 Hz optical flow at subsampled resolution
- **Onboard compensation**: Gyroscopic rotation correction and metric velocity scaling
- **Configurable architecture**: Parametrizable block size, search range, aspect ratio, sample point locations
- **Low-latency velocity output**: Direct MAVLink protocol format for autopilot integration

## Use Cases & Applications

### Velocity Estimation (Primary)
- Downward-facing mount for 2D translational velocity estimation
- Supports hovering flight stability and position integration
- Demonstrated on PIXHAWK Cheetah quadrotor with VICON ground-truth validation

### Obstacle Avoidance / Direction Estimation
- Wide aspect ratio (120H×32V) + wide-angle lens for corridor detection
- Enables detection at extreme image edges; alternative to multiple mouse sensors

### Indoor & Low-Light Navigation
- Operates in typical office lighting (500–700 Lux) without active infrared
- Suitable for indoor autonomous flight, contrast to mouse sensors

### Outdoor Trajectory Following
- Tested on ground-based rig and aerial platforms; drift primarily from magnetometer, not optical flow

## Key Results

### Flight Performance
- Hovering test: PX4FLOW velocity measurements (x, y directions) matched Vicon ground-truth with Kalman filtering; raw output showed expected noise envelope consistent with 250 Hz sampling
- Integration of velocity over 192.16 m outdoor trajectory showed high consistency with orthophoto overlay; loop closure error minimal

### Illumination Comparison
- **PX4FLOW**: 6 Lux (CCFL) / 3 Lux (Halogen) minimum
- **ADNS-2080 mouse sensor**: 47 Lux (CCFL) / 34 Lux (Halogen)
- **Conclusion**: PX4FLOW requires ~8× less light; mouse sensor unsuitable for typical indoor conditions

### Indoor Trajectory Test
- 28.44 m square trajectory with 0.25 m start/end spacing
- Velocity integration without filtering/motion model; good fidelity in structured environments

### Outdoor Comparison
- PX4FLOW vs. ADNS-2080 on several-hundred-meter road trajectory
- Similar integrated position drift; PX4FLOW advantage is indoor/low-light applicability
- Drift primarily from attitude estimation (magnetometer interference), not optical flow sensor

## Notable Details

### Open-Source & Hardware Design
- **Software**: Fully written in C, compiled with GNU GCC, released under BSD open-source license
- **Hardware**: CC-BY-SA creative-commons licensed open hardware
- **Availability**: Design and code available at https://pixhawk.ethz.ch/px4/

### Computational Efficiency
- Uses dedicated ARM Cortex M4 integer vector instructions (SIMD) for 4-pixel SAD computation per clock cycle
- Efficient histogram filtering for 64 sample points per frame
- Achieves real-time processing without FPGAs (contrast to contemporary FPGA-based approaches)

### Related Ecosystem
- Integration with PIXHAWK autopilot platform
- MAVLink protocol output for seamless autopilot communication
- Complements IMU and compass for full state estimation

### Future Enhancements
- Vision-based heading reference to overcome local magnetic anomalies in urban environments
- Lookup-table-based distortion correction for high-distortion wide-angle lenses

---

**Relevance to Black Swift Technologies**: This paper provides foundational technical background for optical flow-based UAV navigation. BST likely referenced PX4FLOW as a benchmark or design precedent when developing vision-based velocity estimation for their own systems (possibly SwiftCore or AeroPod platforms). The paper's emphasis on low-power, low-cost, real-time processing on embedded systems aligns with BST's design philosophy for autonomous air vehicles.