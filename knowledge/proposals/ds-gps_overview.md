# DS-GPS Overview

## Document Metadata
- Type: Project overview presentation
- Client/Agency: NOAA
- Program/Solicitation: 2019 SBIR Phase I
- Date: 2020-05-29
- BST Products/Systems Referenced: FMS (Flight Management System)
- Key Personnel: Not named in document

## Executive Summary
Black Swift Technologies proposed Diverse Source GPS (DS-GPS), an autopilot-agnostic navigation package for beyond-line-of-sight (BLOS) UAS operations that provides position solutions in GPS-denied environments by integrating multiple navigation sources. The system aims to achieve <50m RMS position accuracy without relying on GPS as the sole navigation source, addressing vulnerabilities to jamming and spoofing.

## Technical Approach

DS-GPS combines multiple complementary navigation techniques:

1. **VINS (Visual-Inertial Navigation System)**
   - High-performance embedded processor (Jetson TX2 or Nano option)
   - USB3 rolling shutter camera (e-con Systems See3Cam CU135)
   - Provides fast velocity estimates (~1 m/s accuracy)
   - Integrates optical flow with inertial data
   - Position integration accuracy below error goal for 45 seconds

2. **Optical Position Correction Methods**
   - GPS-tagged map generation for return-to-home capability
   - SLAM (Simultaneous Localization and Mapping) for driftless navigation
   - Deep learning-based localization on coastline or roadway maps
   - Both demonstrated to provide rapid absolute position corrections onboard

3. **RF Signal Navigation**
   - GPS monitoring for jamming/spoofing detection
   - Software-defined radio (SDR) for flexible signal source access
   - VHF navigation aids (up to 40 NM range, bearing to known towers)
   - Cell tower and TV tower signal utilization
   - Cross-validation with VINS system to detect solution divergence

4. **Mission Planning Tool**
   - Automated optical quality assessment of flight routes
   - RF navigation source identification
   - Road/coastline map identification and population

## Products & Capabilities Described

### Jetson TX2
- Embedded processor for imaging payload
- Size: 87x50 mm
- Weight: 220g
- Power: 7.5W
- Cost: $676

### See3Cam CU135
- High-performance USB3 rolling shutter camera
- Size: 30x30 mm
- Weight: 23g
- Power: 1.85W
- Cost: $299

### Combined DS-GPS Package (Phase I Goals)
- Total size: 87x50 mm
- Target weight: <350g (prototype: 243g)
- Target power: <50W (prototype: 9.35W)
- Target cost: $6,000
- Serial-like interface for host UAS
- Autopilot-agnostic integration
- Compatible with fixed-wing and multirotor platforms

## Use Cases & Applications

**Ideal Commercial Application Profile:**
- Fixed-wing, long-range missions
- Daytime operations in clear weather
- Over land or near coastline (not fully over water)
- Linear flight paths or large mapping missions
- 6-8 hour endurance maximum

**Non-ideal Environments:**
- Nighttime operations (limits optical techniques)
- Poor weather (fog, clouds, rain)
- Over water/ice (optical techniques struggle)

## Key Results (Phase I Findings)

Performance characteristics by navigation technique:

| Technique | Conditions | Coverage | Accuracy | Notes |
|-----------|-----------|----------|----------|-------|
| VINS | Daytime/clear | Land/coast only | <50m RMS (45 sec), ~1 m/s velocity | Accumulates error over time |
| GPS Breadcrumbs | Daytime/clear | Land/coast only | <20m | Requires partial GPS coverage |
| SLAM | Daytime/clear | Land/coast only | <10m (with GPS cal) | Driftless solution possible |
| Road/Coast Following | Daytime/clear | Over features only | <20m | Limited by preloaded maps |
| Signals of Opportunity | All weather | Signal coverage dependent | 5-50m | Most robust to conditions |

## Notable Details

1. **Problem Statement**: Commercial UAS missions require BLOS operation, but GPS-only navigation is vulnerable to jamming and spoofing, creating safety and regulatory barriers.

2. **Modular Approach**: System exploits different navigation techniques suited to different mission profiles, allowing flexibility in deployment.

3. **Hybrid Validation**: Cross-validation between VINS and RF/GPS solutions proposed to detect failures before they compromise safety.

4. **Development Gap**: Document notes "It would help to have a targeted mission or application at NOAA for this technology," suggesting Phase II would benefit from a specific operational need or demonstration opportunity.

5. **Scalability Trade-offs**: VINS and optical techniques offer very small SWaP advantages; RF techniques offer all-weather capability at expense of complexity and coverage dependency.

6. **Integration Strategy**: Designed as standalone hardware package with serial interface, enabling integration across various UAS platforms rather than being autopilot-specific.