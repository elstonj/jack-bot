# E2 Testing and Capabilities

## Document Metadata
- Type: Capability brief / Testing plan
- Client/Agency: NREL (National Renewable Energy Laboratory)
- Program/Solicitation: Not explicitly stated; appears to be internal planning document
- Date: 23 October 2020
- BST Products/Systems Referenced: E2 (UAS platform with gimbal and camera system)
- Key Personnel: Not named in document

## Executive Summary
This document outlines NREL's planned testing of Black Swift Technologies' E2 UAS for imaging heliostat mirrors in solar installations. It specifies both immediate testing requirements (November 2020) and full operational capabilities needed for the E2 to autonomously scan and photograph heliostats across large solar fields while tracking reflected images of collector towers.

## Technical Approach

### Immediate Testing Requirements
The E2 must support:
1. **Remote hover control**: Ability to hover at specified latitude, longitude, altitude, and heading
2. **Remotely triggered photography**: Capture images while hovering
3. **Gimbal pitch angle control**: Set and lock gimbal pitch to establish known pointing vectors to heliostats

### Full Operational Capabilities
The E2 system must support autonomous waypoint-based flight with the following mission parameters per waypoint:
- E2 position (lat/lon/altitude)
- Target location (lat/lon/altitude) — the heliostat or collector tower being imaged
- Velocity command (held constant until next waypoint reached)
- Camera parameters:
  - **Video mode**: Remote trigger to start/stop recording at waypoints
  - **Still mode**: Automatic photo capture at user-defined intervals (X seconds) with operational limits; start/stop sequences at waypoints

## Products & Capabilities Described

### E2 UAS Platform
- **Purpose**: Autonomous imaging platform for solar facility inspection
- **Key capability**: Fly to specified waypoints while maintaining targeting on designated camera targets
- **Camera system**: Supports both video and still photography; gimbal allows pitch angle adjustment
- **Multi-lens support**: Capable of operating with multiple lenses; testing planned with varying focal lengths

## Use Cases & Applications

**Primary Application**: Solar thermal power plant heliostat inspection
- Installations may contain thousands of mirrors
- Goal: Divide mirror field into zones by focal length
- Mission profile: Scan heliostats one at a time using 3-waypoint flight paths designed to capture collector tower reflections traversing across mirror surfaces
- Focus: Optical characterization and alignment verification of heliostats

## Notable Details

1. **Flight path design**: Waypoints are deliberately configured to fly the aircraft on a path allowing capture of collector tower reflections moving across the mirror surface (indicates focus on optical performance verification)

2. **XML flight plan format**: Document includes example waypoint XML structure showing expected data format for autonomous flight planning, including:
   - Waypoint sequencing (num, next)
   - Altitude relative ground level (AGL_ALT waypoint action type)
   - Shoot mode selection (still vs. video)
   - Shoot interval for still photography

3. **Testing phasing**: 
   - **Test Sequence 1**: Fixed-point imaging at varying distances from heliostat with multiple lenses
   - **Test Sequence 2**: Vertical scanning of heliostats via altitude-holding flight

4. **NREL partnership**: Document reflects collaborative refinement of E2 capabilities for NREL's specific solar facility monitoring needs