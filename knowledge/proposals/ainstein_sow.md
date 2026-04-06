# Ainstein SOW (NASA SBIR Phase II)

## Document Metadata
- Type: Statement of Work / Technical Proposal
- Client/Agency: NASA
- Program/Solicitation: 2018 SBIR Phase II - Terrain Following
- Date: January 23, 2019
- BST Products/Systems Referenced: S2, S3 (implied through flight testing context)
- Subcontractor: Ainstein (µSharp Patch, µSharp3D radar systems)
- Key Personnel: Not named in document

## Executive Summary
This SOW outlines a Phase II NASA SBIR effort to develop a long-range, all-weather radar for UAS terrain-following applications. Phase I testing revealed performance gaps in existing UAS radar options, prompting BST to partner with Ainstein to modify their automotive-grade sense-and-avoid radar systems (µSharp product line) to fill the capability gap in the 24 GHz UAS-compatible frequency band.

## Technical Approach

### Problem Statement
Phase I flight testing identified significant limitations in candidate long-range sensors for terrain following:
- **Laser systems**: Degraded performance in fog and heavy snow; reduced range and false returns
- **Stereo depth sensors**: Unreliable detection in homogeneous texture; limited range in poor visibility
- **Existing UAS radars**: Too small/short-range (altimeter class) or too large/expensive (collision avoidance class)
- **Automotive radars**: 77 GHz prohibited for airborne use; 24 GHz automotive systems not adapted for UAS

### Proposed Solution
Collaborate with Ainstein to modify long-range automotive ADAS radar systems to UAS specifications. Phase II focuses on evaluating feasibility of modifications to two Ainstein products:
1. **µSharp Patch**: Reduce beamwidth; add Doppler output capability
2. **µSharp3D**: Increase detection range for car-sized objects

### Deliverables
- Feasibility evaluations of proposed modifications
- Selection of most feasible implementation path
- Prototype modifications
- Delivery of modified radar with documentation by end of 2-year effort

## Products & Capabilities Described

### µSharp Patch (Ainstein)
- Current application: Sense and avoid radar
- Proposed modification: Reduce beamwidth to >15° H and >15° V for mechanical scanning; add Doppler return values
- Target role: Mechanically scanned long-range radar for terrain following

### µSharp3D (Ainstein)
- Current application: 3D sense and avoid radar
- Proposed modification: Increase detection range to ≥100m for car-sized objects
- Target role: Extended-range detection capability

## Use Cases & Applications

**Primary Application**: Terrain-following navigation for UAS in all-weather conditions
- Enables safe low-altitude flight over varied terrain
- Operates in conditions where optical sensors (laser, stereo) fail (fog, snow, poor visibility)
- All-weather capability critical for operational reliability

**Related missions implied**: Arctic operations, mountainous terrain, adverse weather environments

## Long-Range Radar Requirements (Phase II Target)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Update Rate** | 5 Hz | Over full scan volume |
| **Minimum Range** | 0.5 m | Not a hard requirement |
| **Maximum Range** | 100 m | Minimum for car-sized target |
| **Range Resolution** | 40 cm | Minimum, not a hard requirement |
| **Field of View** | 45° H × 20° V | Scan volume |
| **Doppler Measurement** | 30 m/s unambiguous | Not a hard requirement |
| **Beamwidth** | >15° H × >15° V | Goal: >10° H × >10° V |
| **Size** | 120 × 90 × 30 mm | Notional max; goal closer to existing µSharp Patch |
| **Mass** | 400 g | Goal: 300 g |
| **Power** | 25 W | Goal: 15 W |
| **Unit Cost** | $4,000 | Target price point |

## Notable Details

- **Frequency selection**: 24 GHz chosen as the only FCC-compliant frequency band for airborne radar; 77 GHz prohibited for UAS (per FCC-15-16)
- **Competitive landscape**: Survey of 24 GHz UAS radars identified only collision-avoidance systems (EchoDyne EchoFlight, Ainstein uLab-D1) as reference points; both too large/expensive for terrain following
- **Strategic gap**: Clear market gap between low-performance altimeters and high-performance collision-avoidance radars; ADAS automotive radars demonstrate feasibility but required adaptation to UAS constraints
- **Partnership rationale**: Ainstein's existing radar IP (µSharp line) provides foundation; modifications more efficient than ground-up development
- **Multi-sensor strategy**: This work complements earlier BST evaluation of laser and stereo options; radar selected as most suitable for terrain following given performance trade-offs

## Project Status
Located in "Completed/Inactive/Unsubmitted Projects" folder, suggesting this Phase II proposal may not have been funded or was not pursued beyond this planning stage.