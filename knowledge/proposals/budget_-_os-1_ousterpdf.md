# OS-1 — Ouster Product Specifications

## Document Metadata
- Type: Product specification sheet / vendor datasheet
- Client/Agency: Black Swift Technologies (internal reference document)
- Program/Solicitation: 2018 NASA SBIR Phase II - Terrain Following
- Date: 1/24/2019
- BST Products/Systems Referenced: None directly (this is a third-party component specification)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This document is a product specification sheet for the Ouster OS-1 LIDAR sensor, captured during BST's 2018 NASA SBIR Phase II proposal for terrain-following operations. The OS-1 is a compact, eye-safe LIDAR with multiple channel configurations (16, 64, or 128) offering 360° horizontal coverage and various vertical field-of-view options.

## Technical Specifications

### Physical Characteristics
- Height: 74mm (2.90in)
- Diameter: 80mm (3.14in)
- Mass: 380g (13.4oz)

### Performance Parameters
| Parameter | Specification |
|-----------|---------------|
| Channels | 16, 64, or 128 |
| Vertical FOV | 16/64: ±16.6° (33.2°); 128: ±22.5° (45°) |
| Horizontal FOV | 360° |
| Angular Resolution (Vertical) | 16/64: 0.52°; 128: 0.35° |
| Angular Resolution (Horizontal) | 0.18° |
| Range | Up to 150m (80% reflectivity); Up to 50m (10% reflectivity) |
| Range Accuracy | ±1.5-10cm (3cm average std dev) |
| Beam Divergence | 0.18° full angle |
| Rotation Rate | 10–20 Hz |
| Laser Classification | Class 1 Eye-Safe |

### Data Output
- Distance
- Intensity
- Ambient near-IR
- Reflectivity
- Angle
- Timestamp

### Sampling Rates (by channel configuration)
- 16-channel: 655,360 points/sec
- 64-channel: 1,310,720 points/sec
- 128-channel: 2,621,440 points/sec

### Additional Features
- Multiple time syncing input/output options
- On-the-fly programming of frame rate and resolution
- Fixed angle and fixed timing measurement modes
- Multi-sensor crosstalk immunity
- Factory calibration (intrinsic and extrinsic)
- Pluggable connector
- Over-the-network firmware updates
- Embedded IMU

## Pricing (as of 1/24/2019)
- 16-channel: $3,500
- 64-channel: $12,000 ($8,000 for non-profit research)
- 128-channel: $18,000 ($10,000 for non-profit research, summer 2019 availability)

## Notable Details
- Document sourced from Ouster.io product page
- Preserved in BST archives as supporting material for NASA SBIR terrain-following proposal, suggesting evaluation as potential sensor payload for autonomous aircraft operations
- Compact form factor and 360° coverage suggest applicability to aerial platform integration
- Eye-safe classification important for regulatory compliance in autonomous operations