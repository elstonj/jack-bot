# RFI For BluFlux Project 2482: Payload Integration for DCA PoC Testbed

## Document Metadata
- Type: Request for Information (RFI)
- Client/Agency: BluFlux (internal or partner project)
- Program/Solicitation: BluFlux Project 2482
- Date: 2020-05-31
- BST Products/Systems Referenced: None directly (this is a payload integration RFI, not BST-authored)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
BluFlux is seeking payload integration services for a Proof of Concept (PoC) Testbed designed to evaluate directional vs. omnidirectional antennas for UAV cellular connectivity. The RFI requests recommendations for suitable UAV platforms (with DJI M200 series as primary focus), payload integration planning, and confirmation of design engineering capabilities for the Electronics Unit and Antenna System.

## Technical Approach
The DCA PoC Testbed comprises two main subsystems:
1. **Antenna System** – Three interchangeable configuration forms:
   - Configuration A: Patch Cube Plus Circular Ground Plane with Monopole
   - Configuration B: Patch Cube Only
   - Configuration C: Circular Ground Plane with Monopole Only

2. **Electronics Unit** – Battery-powered unit mounted inside/above antenna system with functions:
   - Power the cellular module (design intent: Sierra Wireless WP7610)
   - Log cellular network interaction data
   - Control antenna port selection (up to 5 ports) based on received signal strength from cellular PCIs
   - Interface via 5 coaxial cables to Antenna System

**Key Constraint:** All electrically conductive materials below the payload prohibited; UAV landing gear must be non-conductive.

## Products & Capabilities Described

### Antenna System
- **Configuration A (Patch Cube + Ground Plane + Monopole):**
  - Circular ground plane: 100–150 mm diameter, 22–49 g
  - Cube face width: 80–100 mm, height: 60–80 mm, weight: 107–178 g (without fasteners/connectors)
  - Monopole extension: 35–50 mm below ground plane
  
- **Configuration B (Patch Cube Only):**
  - Same dimensions as Config A cube
  
- **Configuration C (Ground Plane + Monopole Only):**
  - Ground plane and monopole only (lightest option)

### Electronics Unit
- Standalone box designed to fit within or above antenna cube
- Mechanical design TBD by engineering services provider
- Firmware to run on Sierra Wireless WP7610 cellular module (possibly Linux-executable, potentially eliminating need for separate microcontroller)
- Expected to log data and implement antenna sector control algorithm

## Use Cases & Applications
- **Primary UAV Platform:** DJI M200 series (M210 specified)
- **Mission Type:** Cellular connectivity performance testing via directional vs. omnidirectional antenna comparison
- **Flight Operations:** Up to 25-minute flights at altitudes of 100, 250, or 400 feet AGL at 30 knots cruise speed
- **Geographic Scope:** Colorado and Oregon flight operations requested
- **Operating Conditions:** Night flying preferred

## Key Payload Specifications
| Parameter | Value |
|-----------|-------|
| Maximum Payload Weight | ~1.2 kg (2.64 lbs) target for DJI M210 |
| Required Flight Endurance | 25 minutes total (15 minutes at cruise speed) |
| Electronics-Antenna Interface | 5 coaxial cables |
| Antenna Ports | Up to 5 selectable ports |
| Cellular Module | Sierra Wireless WP7610 (design intent) |

## Required Services Requested

**Immediate (Payload Integration):**
1. Recommend one or more UAV models suitable for payload integration
2. Create payload integration plan and maintain interface specifications
3. Develop UAV-payload CAD model and maintain BOM/mass budget
4. Provide visual mockups showing payload installed on proposed UAV platforms
5. Provide UAV leasing rates (if available) for CO and OR operations
6. Provide piloting rates for CO and OR operations

**Secondary (Electronics Unit Design – Subject to Upcoming RFQ):**
- Mechanical design (CAD models, Electronics Unit/Antenna mechanical integration)
- Electrical design (component specification, schematic, PCB layout, EMI mitigation)
- Firmware development (data logging, cellular antenna control algorithm, bring-up)

**Tertiary (Flight Operations – Desired Services):**
- Test flight management and airspace authorization
- UAV piloting services in Colorado and Oregon

## Notable Details
- **Flexibility:** Three antenna configuration forms allow evaluation of directional/omnidirectional tradeoffs on same platform
- **Non-Conductive Requirement:** Standard UAV landing gear will likely require modification (currently conductive)
- **Cellular Module Selection:** Sierra Wireless WP7610 chosen as design intent; capable of running Linux, potentially consolidating firmware/microcontroller functions
- **Cable Management:** Coaxial cable routing and orientation consistency emphasized for RF performance
- **Future Scalability:** Request acknowledges other UAV platforms may be suitable beyond DJI M210; indicates desire to make Electronics Unit/alternate antenna compatible with multiple airframes
- **Design Philosophy:** Phased approach—RFI for payload integration first, RFQ for Electronics Unit design to follow

## Status
This is an active RFI seeking responses from potential integrators/service providers. Document reflects preliminary payload specifications subject to refinement based on responder feedback.