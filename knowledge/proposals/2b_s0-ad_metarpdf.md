# S0-AD METAR

## Document Metadata
- Type: Technical proposal with ROM (Rough Order of Magnitude) budget
- Client/Agency: SOCOM (Special Operations Command)
- Program/Solicitation: SOCOM ROM - S0-AD METAR Option 2B
- Date: 2026-08-24
- BST Products/Systems Referenced: S0-AD airframe, PTH Sonde, MHP wind sensor, SwiftLink, SwiftControl, SwiftCore, PCLT module
- Key Personnel: Elston/Hild, Stachura (M), Fromm (J), Lomis (A), Strauss (N), Busby (B), Prendergast (D), Beck Cotter (Business Official)

## Executive Summary
Black Swift Technologies proposes to develop a METAR-equivalent weather observation capability for the S0-AD small unmanned aircraft to support SOCOM direct action, covert logistics, and hostage rescue operations. The system will provide real-time automated measurements of precipitation, cloud cover, visibility, and atmospheric conditions to enable near-term tactical decisions on landing zone safety and ground maneuver conditions in enemy-controlled battlespace.

## Technical Approach
The R&D effort builds on the existing S0-AD atmospheric sensing suite (which currently measures pressure, temperature, humidity, and winds via PTH Sonde and MHP sensors). The approach involves:

1. **Trade Studies** to investigate sensor options for three new capabilities:
   - **Precipitation**: Capacitive, resistive, or optical sensors (e.g., Apogee SG-050) for type and intensity measurement
   - **Cloud Cover**: Upward-looking sensors including cameras with computer vision, single-point Lidar, and longwave infrared radiometry
   - **Visibility**: Forward-looking sensors including single-point Lidar and longwave infrared radiometry (e.g., Benewake TFA1500-L)

2. **Integration & Design**: Feasibility assessment against SWaP constraints, then design and build S0-AD variant with selected sensors

3. **Data Pipeline**: Numerical weather observations transmitted every 30 seconds at 50 nm range via Microhard P400 datalink radio; aircraft telemetry transmitted minimum every 20 seconds

4. **Control & Display**: Leverage existing SwiftLink tablet interface and SwiftControl web-based UI served by SwiftCore FMS; modifications to display METAR-equivalent measurements (precipitation, cloud cover, visibility) alongside existing PTH data

## Products & Capabilities Described

**S0-AD Airframe**
- Small unmanned aircraft with low visual and acoustic signature
- Endurance: >1 hour
- Range: >50 nm with LoS datalink
- Equipped with PCLT module
- Currently not reusable; sustains light damage on approximately half of landings (future path to reusability noted)

**Existing Sensors (to be retained)**
- PTH Sonde: pressure, temperature, humidity, dew point
- MHP: wind direction and speed

**New Sensors (to be integrated)**
- Precipitation sensor (type/intensity automated measurement)
- Cloud layer altitude & ceiling sensor (upward-looking)
- Horizontal visibility sensor (forward-looking)
- Objective: Nighttime capability for all three parameters

**SwiftCore**: Existing flight management system; software updates required to handle new sensor data streams

**SwiftControl**: Existing web-based operator UI served by SwiftLink tablet; modifications needed to display new weather parameters

**SwiftLink**: Existing control tablet and datalink interface (hardware basis for operator station)

**Microhard P400**: Datalink radio for transmitting telemetry and weather observations

## Use Cases & Applications
- **Direct action operations** in enemy-controlled battlespace
- **Covert logistics** and supply insertion
- **Hostage rescue** missions
- **Advanced force operations**
- **Route/objective area reconnaissance** (few hours pre-mission)
- **Landing zone assessment**: Rotary-wing landing zones, fixed-wing expeditionary runways, parachute drop zones
- **Ground maneuver and combat condition assessment** via precipitation/visibility data
- **Mission abort/continue decisions** based on weather at objective

Operators may be positioned at objective area with visual range or exercise standoff in host aircraft platform.

## Key Specifications & Requirements

| Requirement | Specification |
|---|---|
| **Endurance** | >1 hour |
| **Range** | >50 nm (LoS dependent) |
| **Data Transmission Rate** | Weather observations every 30 sec; telemetry every 20 sec minimum |
| **Transmission Range** | 50 nm |
| **Precipitation** | Binary type indication + numerical intensity rate/droplet size (automated, no human input) |
| **Cloud Cover** | Numerical lowest layer and ceiling altitudes (automated) |
| **Visibility** | Numerical horizontal visibility distance (automated) |
| **Night Operation** | Objective capability for all three new parameters |
| **Prerequisite** | GPS/GNSS required |

## Budget (ROM Estimate)
- **Total Personnel Cost**: $84,678 (7 personnel, blended rate ~$125/hr with 29.28% fringe)
- **Equipment**: $10,000
- **Travel**: $4,000 (1 round trip, 2 people)
- **Subtotal Direct Costs**: $98,678
- **Indirect Costs (OH + G&A)**: $64,837
- **Total Costs**: $163,515
- **Fee (7%)**: $11,446
- **Total Request**: $174,961
- **Cost Sharing**: $0

**Note**: ROM is preliminary, non-binding, and subject to change. Blended personnel rate applied; specific personnel not yet identified at proposal stage.

## Notable Details

- **Reusability Path**: S0-AD currently sustains light damage on ~50% of landings; document notes future path to improve robustness of frequently-damaged components for reusability
- **METAR Equivalency**: System aims to provide automated METAR-standard measurements without human interpretation
- **Bounded R&D Scope**: Explicitly framed as determining what a 3 lb aircraft can achieve for cloud/ceiling/visibility measurements and associated accuracy levels
- **Fallback Documentation**: If certain parameters prove unachievable in this SWaP class, deliverable includes documented findings of infeasibility
- **Operational Constraints**: Maintains LoS contact requirement; maximum 50 nm range dependent on host aircraft platform or operator proximity
- **Integration with Existing Ecosystem**: Reuses BST's existing control infrastructure (SwiftCore, SwiftControl, SwiftLink) minimizing development overhead