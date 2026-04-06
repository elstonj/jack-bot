# SOCOM RFI Notes Jul24

## Document Metadata
- Type: RFI Response (Request for Information) / Internal Planning Notes
- Client/Agency: USSOCOM (United States Special Operations Command)
- Program/Solicitation: Long Range/Long Endurance (LR/LE) Uncrewed Aerial System (UAS) Event 2024-25
- Date: July 2024 (RFI submission deadline: July 12, 2024; Vendor presentations: August 6-8, 2024)
- BST Products/Systems Referenced: S2 (Fixed Wing), S3 (VTOL), SwiftCore™ Flight Management System (FMS), MultiSpectral Arrays, SwiftSTL
- Key Personnel: Jack Elston (Ph.D., Founder and CEO, Technical POC), David Hendrickson (Pembroke Defense - external advisor)
- BST CAGE Code: 6PGF9
- BST UEI: C2J3K9NRE3L3

## Executive Summary
Black Swift Technologies proposed its S2 fixed-wing and S3 VTOL uncrewed aerial systems to USSOCOM's LR/LE UAS Event, demonstrating compliance with most basic threshold requirements and many desired traits for Special Operations Forces missions. BST positioned its modular, open-systems platforms built on the SwiftCore FMS as suitable for rapid customization and autonomous operations in contested environments, with clear development pathways for enhanced endurance and GPS-denied navigation capabilities.

## Company Background
BST is a Boulder, CO-based small business founded in 2011, specializing in small unmanned aircraft platforms and technologies. The company has been awarded numerous federal contracts from NASA, DoD, NOAA, and USGS spanning small business, SBIR Phase I-III, and unrestricted awards. Key work areas include extreme environmental monitoring, volcano observation, atmospheric data collection, runway integrity assessments, and wildland firefighting decision support. BST collaborates with industry partners including Creare LLC, Orbital Micro Systems, and Anduril Industries.

**Key Competitive Advantages:**
- Proprietary modular SwiftCore™ FMS (autopilot, ground station, user interface, support electronics)
- Quality guarantee on critical components meeting NDAA and ASDA requirements
- Complete solutions from aircraft design and manufacturing through field operations
- ASDA (American Security Drone Act) compliant systems

## Technical Approach

### SwiftCore™ Flight Management System
The foundational technology for both S2 and S3, providing:
- Proprietary autopilot and ground station software
- User interface and support electronics
- Optimized for rapid customization across scientific, security, and commercial sectors
- Modular architecture supporting government-developed platform-agnostic collaborative autonomy plugins
- API interfaces for integration with Android Team Awareness Kit (ATAK)

## Products & Capabilities Described

### S2 UAS (Fixed Wing)

**Specifications:**
| Parameter | Value |
|-----------|-------|
| Wing Span | 120.6" |
| Length | 73.4" |
| Engine | KDE4215XF |
| Propellant | 6S 14Ah rechargeable battery |
| Max Speed | 48 knots |
| Cruise Speed | 37 knots (27 KIAS noted in compliance table) |
| Rate of Climb | 950 ft/min |
| Rate of Descent | 810 ft/min |
| Construction | Fiberglass and carbon fiber |
| Wing Loading | 38.9 oz/ft² |
| Empty Weight | 13.5 lbs |
| Max Gross Weight | 18.5 lbs |
| Payload Capacity | 5 lbs |
| Glide Ratio | 14.3:1 |
| Stall Speed | 23 knots |
| Glide Speed | 29 knots |
| Max Altitude | 10,000 ft |
| Max Range | 63 miles |
| Max Duration | 90 minutes (current); 3+ hours with payload-battery tradeoff; 8+ hours with hybrid fuel-generator system |

**Key Capabilities:**
- High-endurance range: Proven operations over 20 nautical miles in up to 50-knot winds and icing conditions (USGS volcano monitoring in Alaska)
- Operational range potential: Up to 3 hours on rechargeable battery with 80 NM operational range; projected 8+ hours with hybrid system
- Payload flexibility: Field-swappable payload nose cone; open interface for third-party sensor integration including cameras, AI computational support, and collaborative autonomy systems
- Environmental hardening: Flight tested from -25°C to 46°C; heated sensors adaptable to -51°C/-60°F; engineered for high-altitude flights with strong winds and damaging particulates
- Launch/recovery: Operates in headwinds exceeding 25 knots, crosswinds exceeding 5 knots, tailwinds up to 5 knots; deployable from diverse environments including maritime platforms with potential for water recovery
- Autonomy: Autonomous launch, fly, and land in mountainous regions; NLOS (Non-Line of Sight) autonomous flight to 45 NM out-and-back or 90 NM one-way missions; autonomous flight when communications unavailable
- GNSS-denied operations: In-house solution at TRL 4; adaptable to third-party jamming-resistant solutions

### S3 UAS (VTOL)

**Overview:**
Built on proven S2 design and SwiftCore FMS with Vertical Take-Off and Landing (VTOL) capabilities. Shares performance envelope with S2 while addressing portability and launch/recovery in rugged conditions.

**Key Features:**
- Vertical transition to forward flight; no launcher required
- Modular payload system similar to S2 for flight-line mission conversion
- User-friendly autonomous operation with terrain-aware navigation and onboard computer vision
- Advanced autonomous capabilities in development:
  - Computer vision system for automatic target recognition (ATR)
  - Real-time video/sensor analysis for threat identification (unauthorized personnel/vehicles)
  - Automatic landing and GPS-denied navigation capabilities
  - Reduced operator workload
- Mission data integration: Data transmitted to operations center and integrated into ATAK (Android Team Awareness Kit) for decision-maker and tactical team access
- Performance: Cruise at 27 knots, dash at 48 knots (same propulsion as S2)
- Payload: 5 lbs dual payload capacity with modular design

## Use Cases & Applications

**Historical/Proven Applications:**
- Volcano observation and emissions monitoring (USGS, NOAA contracts)
- Extreme environmental atmospheric data collection
- Runway integrity assessments
- Wildland firefighting decision support
- Scientific research requiring beyond-line-of-sight (BLOS) autonomous operations

**SOCOM-Relevant Applications:**
- Airborne intelligence, surveillance, and reconnaissance (ISR)
- Kinetic operations support
- Perimeter inspections and surveillance
- Covert operations with RF signature reduction through limited communications and automated flight
- Close combat operations in contested battle space
- GPS-denied area penetration with image-based navigation (SwiftSTL technology mentioned)

## Compliance Assessment vs. RFI Requirements

### Basic Traits (Threshold) - Compliance

| Requirement | S2 | S3 | Notes |
|------------|----|----|-------|
| Group 2 UAS | Yes | Yes | S3 is Group 3 |
| Multi-Mission Capability | Yes | Yes | Modular payload, rapid swap with open interface |
| Range: 35+ NM | Yes | Yes | 20 NM standard radio; 120+ NM with low-bandwidth radio; capable of NLOS to 45 NM out-and-back or 90 NM one-way |
| Endurance: 6+ hours | Partial | Partial | Current: 90 min; 3+ hrs with payload-battery tradeoff; 8+ hrs projected with hybrid system |
| Sea Level Elevation | Yes | Yes | — |
| Payload/Sensor: 2+ payloads, 5+ lbs combined | Yes | Yes | 5 lbs total capacity |
| Day/Night Ops in Adverse Weather | Yes | Yes | — |
| Temperature Range: -51°C to 49°C | Partial | Partial | Tested -25°C to 46°C; -51°C/-60°F possible with heated sensors |
| Wind Performance: 25+ kt headwind, 5+ kt crosswind, 0+ kt tailwind | Yes | Yes | T/O: 25 kt headwind, 5 kt crosswind, 5 kt tailwind capability |
| RF/GNSS Contested Operations | Yes | Yes | Autonomous flight without comms; radio-agnostic; GNSS-denied navigation at TRL 4 |
| Modular Components (30-min reconfiguration) | Yes | Yes | No-tools assembly; rapid payload swap |
| Electric/Hybrid Propulsion | Yes | Yes | Electric with rechargeable batteries; adaptable for fuel-powered generator (8+ hrs) |
| Cruise/Dash Speeds: 25/35+ KIAS | Yes | Yes | Cruise 27+ KIAS, dash 48 knots (exceeds requirement) |
| Modular Open Systems Approach | Yes | Yes | Supports government platform-agnostic collaborative autonomy plugins |
| Collaborative Autonomy | Yes | Yes | Proven in NOAA volcano emissions monitoring; NLOS data collection |
| ASDA Compliance (2024) | Yes | Yes | Full compliance |

### Desired Traits (Objective) - Compliance

| Capability | S2 | S3 | Notes |
|-----------|----|----|-------|
| Multiple artificial environment launch/recovery | Yes | Yes | Autonomous no-comms flight; radio-agnostic; GNSS-denied TRL 4 |
| Water/maritime launch/recovery | Partial | Partial | Cannot land in water currently |
| Remain afloat for recovery | No | No | Cannot land in water currently |
| Multi-platform launch/recovery (ground, aircraft, maritime) | Partial | Yes | S2: light rail launcher or hand launch; S3: VTOL, no launcher required |
| RF/GNSS ground jamming ops | Yes | Yes | GNSS-denied solution TRL 4; supports third-party jamming-resistant options |
| Signature reduction (acoustic, visual, IR, RF) | Yes | Yes | RF signature reducible through limited comms and automated flight |
| ATAK Integration | Yes | Yes | Short implementation time with BST's API |

## Key Development Pathways

**Identified capability gaps and development plans:**
1. **Endurance Enhancement:** Trade payload weight for additional batteries (achieves 3+ hours); hybrid fuel-powered generator system development projected to achieve 8+ hours
2. **GPS-Denied Navigation:** In-house solution currently at TRL 4; design supports integration of third-party solutions with better jamming resistance
3. **Water Operations:** Currently cannot land in water; no development timeline specified
4. **Advanced Autonomy:** Computer vision ATR system in development for S3
5. **Extended Range Communications:** Low-bandwidth radio systems already integrated on Swift air-deployed UAS; applicable to S2/S3

## Notable Details

**Strengths Emphasized:**
- Proven track record with federal agencies (NASA, DoD, NOAA, USGS)
- Modular design enabling 30-minute field reconfiguration without tools
- Open systems approach for third-party and government-developed integrations
- Complete lifecycle support (design, manufacturing, payload integration, testing, operations)
- Already ASDA-compliant (significant regulatory advantage)

**Market Positioning:**
- New to SOF customer base; positioning as "door opener" to early-adopter SOF community
- Positioning as conduit to broader DoD and international military forces
- Business development advisor David Hendrickson from Pembroke Defense involved in RFI strategy

**Submission Timeline & Process:**
- RFI Response due: July 12, 2024 (3-5 page unclassified white paper)
- Vendor Presentations: August 6-8, 2024 (Tampa)
- Qualified vendor invitations: September 13, 2024
- Fall/Winter Training and Technical Evaluation phases
- OT&E (Operational Test & Evaluation) phase: February-March 2025
- Portal: USSOCOM eSOF portal (engagesof.com); BST requires eSOF registration

**Internal Questions/Uncertainties:**
- 90-minute end