# Persistence Demo Final Report

## Document Metadata
- **Type:** Final Report
- **Client/Agency:** NASA (contract with NOAA partnership)
- **Program/Solicitation:** NASA Contract 80NSSC25CA043
- **Date:** September 25, 2025
- **BST Products/Systems Referenced:** S2 (fixed-wing UAS)
- **Key Personnel:** Meredith Needham (last editor)

## Executive Summary

This final report documents Black Swift Technologies' successful demonstration of persistent infrared measurements and airspace surveillance over wildfire operations using the S2 fixed-wing UAS. The project integrated NOAA's NightFOX Wildfire Detection Payload for real-time fire monitoring, developed UAS-based detection systems for identifying unauthorized drones in Temporary Flight Restriction (TFR) zones, and validated procedures for sustained continuous operations through coordinated aircraft handovers. Results demonstrate the S2's capability as a force multiplier for wildfire response, addressing both fireline intelligence needs and aviation safety challenges.

## Technical Approach

### NightFOX Wildfire Detection Payload Integration
- Mounted NOAA-developed multispectral sensor suite on S2 UAS platform
- Demonstrated calibration and data collection at Pawnee National Grasslands (August 20, 2025)
- Conducted validation flights at 400m and 800m AGL covering 45 square kilometers in 50 minutes
- Successfully streamed multispectral imagery in near real-time via S2 Ground Station datalink

### UAS-Based Airspace Detection System
Three complementary detection methods integrated into single platform:
1. **ADS-B Reception:** Commercial receiver modified for S2 integration to track Forest Service assets
2. **Long-Range Remote ID Detection:** Custom Bluetooth 5.2 module using Nordic nRF52840 (realistic operational range: 1-1.3 km vs. ground-based 400-1,000m)
3. **Software-Defined Radio (SDR) Signal Interception:** Custom algorithms detecting drone control signals across common frequencies (1.2 GHz, 2.4 GHz, 5.8 GHz)

### Persistent Operations Architecture
- **On-station handover procedure:** Sequential aircraft relief maintaining continuous coverage
- Designed deconfliction protocols using altitude blocks, lateral separation, and time-based scheduling
- Two 30-minute sequential flights demonstrated continuous monitoring capability
- Validated procedures scalable to operational wildfire scenarios

## Products & Capabilities Described

### Black Swift S2 UAS
- **Configuration:** Fixed-wing unmanned aircraft system
- **Endurance:** Up to 2 hours with payload onboard
- **Payload Capacity:** Accepts both NightFOX multispectral sensor suite and detection systems
- **Communication:** Ground Station datalink with ~30 km maximum range (per datalink limitations documented)
- **Capabilities Demonstrated:**
  - High-resolution multispectral data collection and streaming
  - Simultaneous ADS-B target tracking (multiple targets)
  - Remote ID detection at extended ranges (1+ km)
  - RF signal detection/localization of non-cooperative drones
  - WFTAK integration for standardized display of all sensor data
  - Mesh network capability for multi-aircraft data sharing

### NightFOX Wildfire Detection Payload
- **Spatial Resolution:** ~25-meter pixel size (vs. ~375m from NASA VIIRS satellite)
- **Spectral Bands:** 
  - Visible: FLIR Duo R, 1920×1080 pixels, 90°×51° FOV
  - SWIR (1.0-1.6 µm): Custom camera, 64×64 pixels, 23°×23° FOV
  - Near IR (1.6 µm): Custom scanning scope, 1° FOV, ±30° scan
  - Mid IR (4 µm): Custom scanning scope, 1° FOV, ±30° scan
  - Thermal IR (7.5-13.5 µm): FLIR Duo R, 160×120 pixels, 57°×44° FOV
- **Outputs:** Fire radiative power measurements, fireline delineation, hotspot identification
- **Historical Validation:** Previously validated on 2019 Rabbit Mountain prescribed burn and Granite Gulch Fire
- **Data Integration:** Compatible with Wildland Fire Team Awareness Kit (WFTAK)

### Detection System Components
- **ADS-B Receiver:** COTS receiver tracking position, altitude, velocity of multiple simultaneous targets
- **Bluetooth 5.2 Remote ID Module:** Nordic nRF52840 with external antenna optimization
- **SDR Platform:** Compact system identifying drone RF signatures with detection/confidence level
- **Data Display:** WFTAK-compatible interface showing position, altitude, speed/vectors, target classification, detection method, time-since-update

## Use Cases & Applications

### Primary Use Case: Wildfire Response
- **Fireline Monitoring:** Continuous tracking of fire front position, rate of spread, intensity, and direction
- **Fire Prediction Support:** Real-time fire behavior data enabling dynamic suppression planning and tactical decision-making
- **Hotspot Detection:** Identifying flare-ups and secondary fire activity
- **Structure Protection:** Prioritizing resource deployment for community/resource protection
- **Personnel Safety:** Enabling immediate hazard detection for crew evacuation/redeployment

### Secondary Use Case: Aviation Safety in TFRs
- **Unauthorized Drone Detection:** Early warning system for non-participating aircraft entering restricted wildfire airspace
- **Asset Coordination:** Real-time tracking of authorized Forest Service aircraft and ground vehicles
- **Incident Command Support:** Comprehensive airspace picture enabling proactive conflict mitigation
- **Manned Aircraft Protection:** Preventing collisions and forced groundings during critical suppression phases

### Operational Scenarios Demonstrated
- **Single-Aircraft Operations:** Localized airspace awareness for smaller incidents
- **Multi-Aircraft Deployment:** Distributed sensor networks for large, complex fires
- **24-Hour Coverage:** Extensible to continuous operations with doubled staffing (day/night operations)

## Key Results

### NightFOX Validation Flight (August 20, 2025)
- Successfully generated multispectral imagery at 400m and 800m AGL
- Covered 45 sq km during 50-minute flight
- Calibration tarp validation confirmed proper sensor operation
- All imagery products successfully streamed in near real-time to ground station
- Validated technical feasibility for actual wildfire operations

### UAS Detection System Demonstrations
- **ADS-B:** Successfully tracked multiple ground and airborne targets simultaneously with accurate position relay to WFTAK
- **Remote ID Detection:** Effective detection ranges >1 km confirmed in field conditions (Figure 6 demonstration)
- **RF Signal Detection:** Laboratory testing confirmed drone identification; flight demonstration proved >1 km detection range
- **TAK Integration:** All detection data successfully integrated with real-time updates and standardized symbology (Figure 7 screenshot)

### Persistent Operations Demonstration (August 20, 2025, Sunny Slope Sod Farm)
- Two sequential 30-minute S2 flights executed continuous overwatch
- On-station handover procedure validated:
  1. Primary S2 (S20003) established at 380' AGL Operations Orbit
  2. Secondary S2 (S20009) launched
  3. Secondary established at 300' AGL Standby Orbit
  4. Primary transitioned to Landing Orbit while secondary moved to Operations Orbit
  5. Seamless handover maintaining continuous coverage
- Demonstrated scalability of procedures to operational wildfire scenarios
- Confirmed safe deconfliction with separation based on altitude, lateral position, and time

### Resource Estimation Models
Developed persistent coverage calculator with assumptions:
- Day-only operations (staffing doubles for 24-hour coverage)
- BVLOS authorizations maximizing operational radius
- Revisit time as defining metric (adjustable based on aircraft count)
- 30 km maximum range constraint from datalink limitations
- Scalable framework applicable to both fireline monitoring and rogue drone detection

Estimated fleet requirements: 20-30 equipped S2 aircraft for nationwide high-priority incident coverage

## Notable Details

### Recent Incident Context
Report documents escalating unauthorized drone threat in 2024-2025 wildfire season:
- **Palisades Fire (Jan 9, 2025):** DJI Mini 3 collision with Super Scooper firefighting aircraft caused wing puncture and grounding
- **California Incidents (2024-2025):** Park Fire, Fairview Fire, Bridge Fire each involved TFR violations and aircraft groundings
- **Manitoba (May 2025):** Unauthorized drone flights forced water bomber grounding for 6+ hours

### Detection Capability Advantages
- Airborne platform overcomes terrain line-of-sight constraints limiting ground-based systems
- Extended detection ranges (1-1.3 km Remote ID vs. 400-1,000m ground-based; SDR beyond Remote ID limitations)
- Early warning capability (minutes before conflict zones reached)
- Can identify non-cooperative drones lacking Remote ID broadcasts

### Operational Integration
- Seamless WFTAK integration within existing incident management frameworks
- Compatible with established air attack channels and deconfliction protocols
- Mesh network architecture enabling multi-aircraft data sharing
- Automatic failover between cellular, satellite, or line-of-sight communications

### Cost-Effectiveness Arguments
- Prevention of aircraft collisions saves millions in replacement costs
- Reduced aircraft downtime enables more aggressive initial attack strategies
- Quantifiable safety improvements for both manned and unmanned platforms
- Scalable implementation with existing BST support infrastructure

### Stakeholder Coordination
- Demonstration team included representatives from NOAA, NASA, and US Forest Service
- Project addresses critical needs identified by incident commanders
- Quoted incident commander (Anthony Marrone, Palisades Fire) emphasizing urgency of solutions