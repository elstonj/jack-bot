# Flash LIDAR Capabilities

## Document Metadata
- Type: Capability brief/technical document
- Client/Agency: Program Manager (Intuitive Research/Intellicopter context)
- Program/Solicitation: Not specified
- Date: Created 2013-02-23; Modified 2013-06-14
- BST Products/Systems Referenced: Flash LIDAR system (general technology evaluation)
- Key Personnel: Maciej Stachura (Black Swift Technologies LLC), Dr. Jay McMahon (University of Colorado Boulder)

## Executive Summary
This document evaluates Flash LIDAR technology for unmanned aircraft system (UAS) applications, specifically for indoor 3D mapping and small UAS detection. It compares two commercial Flash LIDAR systems (ASC TigerEye and Mesa Imaging AG) and discusses advantages of flash LIDAR over conventional scanning LIDAR in terms of accuracy, reliability, and mapping performance.

## Technical Approach
Flash LIDAR captures an entire scene in a single shot, eliminating the need for vehicle movement between observations. This approach offers several advantages:
- Reduces accuracy requirements for vehicle attitude/state information
- Enables overlapping frames for accurate scene stitching with less approximation than scanning LIDAR
- Improves reliability by eliminating moving parts (no scanning mirror), reducing susceptibility to damage and breakdown

Two proposed operating modes for UAS detection application: scanning and tracking modes for detecting small UAS in airspace.

## Products & Capabilities Described

### Flash LIDAR Technology (General)
- **What it is:** Emerging imaging technology that captures full 3D scene data instantaneously, as opposed to conventional scanning LIDAR
- **Proposed uses:** 
  - Indoor 3D mapping of environments
  - Detection and tracking of small UAS (ground-based and airborne collision avoidance)
- **Key advantages:** Single-shot imaging, fewer moving parts, reduced computational/state estimation requirements, higher reliability

### ASC TigerEye
- Price: ~$150,000
- Size: 11×15×10.7 cm
- Weight: 2 kg
- Range: 60m, 150m, 450m, or 1100m (selectable)
- FOV: 3°, 9°, or 45° (selectable)
- Framerate: 30 fps
- Pixel resolution: 128×128
- Range accuracy: Not published
- Applicable conditions: Works in all conditions (outdoor-capable)

### Mesa Imaging AG (SwissRanger)
- Price: $4,295
- Size: 6.5×6.5×7.6 cm
- Weight: 0.5 kg
- Range: 5m or 10m
- FOV: 43.6°×34.6° or 56°×69°
- Framerate: 50 fps
- Pixel resolution: 176×144
- Range accuracy: ±15 mm
- Applicable conditions: Indoor use only (uses IR rather than laser)

## Use Cases & Applications

1. **Indoor 3D Mapping:** Rapid generation of 3D maps of indoor environments
   - Mesa system suitable for smaller spaces (10m/32' range limit)
   - TigerEye suitable for larger indoor structures (extended range options)

2. **Small UAS Detection:** Detection and tracking of small unmanned aircraft systems
   - Ground-based system (primary application)
   - Airborne collision avoidance application (secondary/expansion capability)
   - Advantage over conventional radar for detecting small targets

## Notable Details

- **Trade-offs:** TigerEye offers superior range and outdoor capability but is heavier (2 kg) and significantly more expensive (~$150,000), potentially limiting use on small, man-portable airframes. Mesa system is lightweight and affordable but restricted to indoor use and limited range.
- **Technology comparison:** Mesa's use of IR rather than laser reduces cost and weight but eliminates outdoor functionality.
- **Document context:** Appears to be part of inactive/completed Intuitive Research work related to Intellicopter program; represents early-stage technology evaluation circa 2013.