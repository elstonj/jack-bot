# S0-AD EO/IR IPB Record and Recover

## Document Metadata
- Type: Rough Order of Magnitude (ROM) Proposal
- Client/Agency: SOCOM (Special Operations Command)
- Program/Solicitation: SOCOM ROM submission
- Date: August 24, 2026
- BST Products/Systems Referenced: S0-AD airframe, SwiftCore (FMS), SwiftControl, SwiftLink UI, Samsung Tablet interface
- Key Personnel: Elston/Hild, Fromm (J), Lomis (A), Strauss (N), Busby (B), Prendergast (D), Beck Cotter (Business Official)

## Executive Summary
Black Swift Technologies proposes a record-and-recover system for Intelligence Preparation of the Battlefield (IPB) using the S0-AD airframe with fixed EO/IR cameras and autonomous flight capability. The system will conduct extended surveillance of enemy-controlled areas, capturing high-resolution imagery without real-time transmission, for post-mission analysis and operational planning support.

## Technical Approach
**Mission Profile:**
- Fully-autonomous flight routing with no-communication (no-comm) mode capability
- Pre-mission programming for route execution to objective areas
- Fixed camera payload recording throughout flight
- Post-flight data recovery and analysis using automated target recognition (ATR) or human intelligence analysis
- Operator can maintain line-of-sight (LoS) communication if desired, or system operates completely autonomous

**System Architecture:**
- **Airframe:** S0-AD with PCLT (Precision Composite Landing Technology) module
- **Flight Control:** SwiftCore (Flight Management System)
- **Operator Interface:** SwiftControl software on Samsung Tablet via SwiftLink UI
- **Autonomous Capability:** Code updates required to enable no-communication flight execution and post-landing recovery messaging
- **Datalink:** Microhard P400 radio for status transmission (if operating in semi-autonomous mode)

**Data Collection & Storage:**
- EO camera: Fixed downward-looking, 12 megapixel resolution, continuous coverage with no gaps for ≥1 hour
- IR camera: Fixed downward-looking, 5 megapixel resolution, continuous coverage with no gaps for ≥1 hour
- Data storage: Removable media or high-speed data transfer port for fast download
- Photogrammetry-compliant mapping protocols for imaging coverage verification

**Telemetry & Control:**
- Payload and data collection status transmitted every 20 seconds (if semi-autonomous)
- Aircraft telemetry transmitted minimum every 20 seconds at 50 nm range
- Recovery location and status reporting (pre-landing or post-landing)

## Products & Capabilities Described

**S0-AD Airframe:**
- Endurance: >1 hour
- Range: >50 nm
- Low visual signature
- Low acoustic signature
- Uses PCLT (Precision Composite Landing Technology) module for landing capability
- Note: Currently not fully reusable; sustains light damage on ~50% of landings requiring repairs. Future path to improved reusability identified.

**SwiftCore (Flight Management System):**
- Enables autonomous mission execution without operator input
- Requires software modifications to support no-communication flight modes
- Autonomous route following and navigation

**SwiftControl (Operator Interface):**
- Tablet-based ground control software
- Requires updates for no-comm mission support
- Monitoring and command capabilities when LoS communication maintained

## Use Cases & Applications

**Primary Mission: Intelligence Preparation of the Battlefield (IPB)**
- Pre-combat operation surveillance (weeks, days, or hours prior to engagement)
- Objective area reconnaissance in enemy-controlled territory
- Route mapping and reconnaissance with active enemy presence/patrols
- Enemy formation, disposition, and activity observation
- Temporal change detection over extended periods
- Supporting operational planning for:
  - Course of action development
  - Preplanned targeting
  - Supporting fires coordination
  - Aviation support requests
  - Operational logistics planning

**Operational Modes:**
- Standoff operations (ground-based or from host aircraft)
- Line-of-sight communication maintained during flight (semi-autonomous)
- Fully-autonomous no-communication mode with post-flight recovery

## Implementation Tasks & Development Plan

1. Select cameras and storage hardware
2. Design modifications for IR and EO camera integration and storage
3. Code updates for no-comm flight execution and recovery messaging
4. Fabricate/purchase components and build test article
5. Bench testing, ground testing, and flight testing with iterations/fixes
6. Operational test with SOCOM personnel

## Cost Estimate (Rough Order of Magnitude)

**Total System Cost: $21,000** (system hardware estimate)

**Full Program ROM: $116,048** (including labor, travel, equipment, overhead)

**Labor Breakdown:**
- Personnel: $53,974 (base)
- Fringe (29.28%): ~$15,785
- Subtotal with fringe: $69,759
- Overhead (46.67%): $25,190
- G&A (18.32%): $16,793
- Subtotal: $91,664
- Fee (7.00%): $7,592

**Purchased Equipment:** $8,500
**Travel:** $4,000 (2 roundtrips, airfare and car rental)

**Personnel Allocated (in months):**
- Fromm, J: 0.70 months (112 hours) – primary technical effort
- Elston/Hild: 0.38 months (60 hours)
- Lomis, A: 0.38 months (60 hours)
- Busby, B: 0.25 months (40 hours)
- Prendergast, D: 0.20 months (32 hours)
- Strauss, N: 0.19 months (30 hours)

## Assumptions and Limitations

**Current S0-AD Status:**
- Not currently reusable; sustains light damage on approximately half of landings
- Repair capability exists for damage incurred
- Future path identified for improved reusability through robust redesign of frequently damaged components

**GPS/GNSS Requirement:**
- System depends on GPS/GNSS for autonomous navigation and positioning

**Post-Flight Analysis:**
- Intelligence production occurs after system recovery and data download
- Not real-time intelligence delivery; better suited for planning than tactical ISR
- Supports operational planning cycles rather than immediate targeting

## Notable Details

**Competitive Advantages:**
- Fully-autonomous capability enables operation in GPS-denied or no-comm environments
- Low acoustic and visual signatures suit clandestine IPB operations
- Extended 1+ hour endurance adequate for large area coverage
- PCLT landing technology enables recovery and reuse (with current limitations)
- Integrated ground control via commercial tablet reduces operational footprint

**Key Differentiators:**
- Record-and-recover approach optimizes for area coverage rather than real-time transmission
- Post-flight processing enables use of computationally intensive ATR algorithms
- Photogrammetry-compliant imaging supports precise geolocation and multi-temporal analysis

**Budget Status:**
ROM is explicitly noted as "preliminary, non-binding, and subject to change." Personnel rates are blended averages; specific staffing not yet finalized.