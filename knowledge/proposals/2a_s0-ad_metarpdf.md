# S0-AD METAR

## Document Metadata
- Type: ROM (Rough Order of Magnitude) proposal with cost estimate
- Client/Agency: SOCOM (Special Operations Command)
- Program/Solicitation: SOCOM S0-AD METAR Option 2A
- Date: 2026-08-24
- BST Products/Systems Referenced: S0-AD, SwiftCore, SwiftControl, SwiftLink, PTH Sonde, MHP wind sensor, Microhard P400 datalink radio
- Key Personnel: Elston/Hild, Stachura (M), Fromm (J), Lomis (A), Strauss (N), Busby (B), Prendergast (D), Beck Cotter (Business Official)

## Executive Summary
This proposal describes a concept to equip the S0-AD tactical UAS with electro-optical and infrared cameras plus enhanced software to provide METAR-equivalent weather observations for special operations planning in denied/contested battlespace. The system would enable real-time assessment of precipitation, cloud cover, and visibility in objective areas within hours of direct action missions, supporting landing zone safety and maneuver assessment decisions.

## Technical Approach

**Core Concept:** Augment existing S0-AD atmospheric sensors (PTH sonde, wind/humidity sensor) with:
- Forward-looking EO & IR still image cameras (visible-NIR bandwidth 400-700 nm to match NVG compatibility)
- Vertical field of view design to assess cloud layers
- Aircraft maneuvering (spirals, turns) and altitude correlation for cloud ceiling/layer determination
- S0 operator visual interpretation of images to estimate precipitation type, intensity, cloud altitudes, and horizontal visibility

**Data Architecture:**
- Atmospheric parameters (pressure, temperature, humidity, wind) transmitted every 30 seconds at 50 nm range; every 0.5 nm during enroute
- Still images (1280x720) transmitted every 5 minutes at 50 nm range
- Aircraft telemetry every 20 seconds minimum
- Datalink: Leverage existing Microhard P400 radio; evaluate upgrade if bandwidth insufficient

**Software Integration:**
- Use existing SwiftControl (web-based UI on Samsung tablet) and SwiftCore (flight management system)
- Operator commands image capture via tablet
- Display PTH data and still images to operator
- Integrate changes to SwiftControl and SwiftCore for METAR-equivalent functionality

## Products & Capabilities Described

**S0-AD Airframe:**
- Existing tactical UAS platform with PCLT (Photochromic Light-Tracking) modification
- Endurance: >1 hour
- Range: >50 nm
- Low visual and acoustic signatures
- Current payload capacity accommodates additional cameras

**Existing Sensors Retained:**
- PTH Sonde: pressure, temperature, humidity, dew point
- MHP sensor: wind direction/speed

**New Sensors (EO & IR Cameras):**
- Still image cameras with large vertical field of view (forward-looking, side hemisphere for turning)
- IR camera capability in visible-NIR (400-700 nm) for night operations matching NVG bandwidth
- Images at 1280x720 resolution

**SwiftCore/SwiftControl/SwiftLink:**
- Existing FMS, operator UI, and control tablet infrastructure leveraged
- Software modifications required to display environmental data and manage image transmission

**Microhard P400 Radio:**
- Existing datalink; viability investigation required for combined telemetry, numerical data, and image transmission

## Use Cases & Applications

**Mission Profile:** Real-time weather reconnaissance for special operations direct action, covert logistics, hostage rescue, advanced force operations in contested/enemy-controlled battlespace

**Specific Decisions Supported:**
- **Rotary-wing landing zone safety:** Precipitation, visibility, cloud cover assessment for helicopter operations
- **Fixed-wing expeditionary runway assessment:** Visibility and precipitation data for aircraft landings
- **Parachute drop zone evaluation:** Cloud cover, winds, and visibility for airborne insertions
- **Ground maneuver assessment:** Precipitation data informing combat/movement conditions on objective
- **Abort/Continue decisions:** Operational minimums for cloud ceiling (>±200 ft precision) and horizontal visibility sufficiency

**Deployment Scenario:** Long-range reconnaissance element operating within visual range of objective, or standoff operator in host aircraft

## Key Technical Requirements

**Environmental Data Precision:**
- Cloud layer altitude determination: ±200 feet
- Precipitation: Binary indication with type and qualitative intensity
- Visibility: Sufficient to assess helicopter/fixed-wing landing capability
- Night capability: IR assessment of all three parameters (precip, clouds, visibility)

**Operational Parameters:**
- LoS contact to 50 nm maximum range
- GPS/GNSS required
- Operator interpretation of images (human-in-loop for altitude, visibility, precipitation assessment)

**Reusability Note:** S0-AD currently sustains light damage on ~50% of landings requiring repair; future path to full reusability by hardening frequently-damaged components

## Cost Estimate (ROM)

**Total Project Cost: $152,690**

**Cost Breakdown:**
- Personnel: $73,366 (7 BST staff, ~412 estimated hours blended, $125/hr blended rate + 29.28% fringe)
  - Fromm (J): 122 hrs (lead engineering effort)
  - Elston or Hild: 80 hrs
  - Lomis (A): 100 hrs
  - Strauss (N): 40 hrs
  - Busby (B): 60 hrs
  - Stachura (M): 20 hrs
  - Prendergast (D): 32 hrs
- Equipment (cameras, sensors): $9,000
- Travel: $4,000 (1 round trip for 2 personnel)
- Indirect Costs (OH 46.67% + G&A 18.32%): $56,335
- Fee/Profit: $9,989 (7%)

**Estimated System Cost at Completion: $23,000**

## Notable Details

- **Reusability constraint:** S0-AD is currently non-reusable; sustainability improvements targeted for future iterations
- **Human interpretation:** System deliberately leverages operator expertise for cloud altitude and visibility assessment rather than automated sensor measurement; operator uses aircraft maneuvering and altitude cues
- **Existing infrastructure leverage:** Proposal maximizes use of SwiftCore FMS, SwiftControl UI, SwiftLink tablet, and Microhard datalink to minimize development
- **Night operations:** IR camera bandwidth (visible-NIR 400-700 nm) specifically matched to NVG compatibility for aircrew compatibility
- **Data transmission:** Dual mode transmission (telemetry every 30 sec at 50 nm; images every 5 min at 50 nm) with pause capability during image transmission
- **ROM disclaimer:** Cost estimate is preliminary, non-binding, and subject to change pending further requirements definition
- **Staffing note:** At proposal stage, specific personnel not yet identified; blended rate of $125/hr used as planning estimate