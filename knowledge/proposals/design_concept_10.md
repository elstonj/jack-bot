# Design Concept 1.0

## Document Metadata
- Type: Design presentation/concept document
- Client/Agency: Not explicitly named (referenced as "they/their")
- Program/Solicitation: Unknown
- Date: Created June 19, 2020; Modified June 25, 2020
- BST Products/Systems Referenced: Appears to be for an airborne platform (nose cone, pressure sensing system)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This document presents design concept iterations for a flush air ballast cover system with integrated static pressure ports and water intrusion prevention mechanisms. The design addresses pressure measurement and environmental protection for what appears to be an airborne platform, with focus on resolving water ingestion and electromagnetic interference (EMI) issues.

## Technical Approach

### Flush Air Ballast Cover Assembly
- Inner radius configured in 'x'-pattern at 15° from centerline
- Outer radius in standard '+'-pattern at 25° from centerline
- Enclosed removable lid design
- Optional metal-mesh insert for improved EMI shielding
- Manifold required to distribute pressure to differential sensors
- Static pressure lines routed into system

### Static Ports
- Four (4) holes drilled in nose cone perimeter
- Ports glued directly into nose cone
- Simple design with no integrated water prevention at port level

### Water Intrusion Prevention Mechanisms
- **Surface ridges**: 0.5mm ridges prevent water from running along surface and covering holes
- **Hole sizing**: 2mm diameter holes reduce likelihood of total blockage by small water droplets; can be enlarged if needed
- **Direct impact requirement**: Design relies on water requiring direct droplet impact rather than surface flow

### Moisture Trap Design
- Printed as separate component, installed into cap pocket
- Provides outer lip on cap
- Includes weep hole on back side to allow airflow and water clearing
- Weep hole created by melting with heated metal rod/needle near nipple junction
- Wicking mechanism within trap clears main air channel once droplet reaches trap
- Cannot print 0.5mm wall on cover surface; moisture trap tube provides this wall function

### Enclosure & Integration
- Box with removable lid
- Support rails for PCBA slide-in/out installation
- Cable passthrough via drilled/cut holes in back lid
- Tight fit design for internal tubing

## Use Cases & Applications
Airborne environmental sensing platform requiring:
- Pressure measurement (differential sensors)
- Static pressure sampling
- Operation in wet/humid conditions with water ingestion risk

## Interference Issues Noted
- **Front clearance area**: Client may not update requested clearance; design can still be delivered but with severely restricted feature additions and port blockage solutions
- **Pressure line routing**: If clearance not updated, pressure lines must be routed within 3D-printed components (feasible but constrained)
- **EMI concerns**: Addressed through optional metal-mesh insert in box

## Notable Details
- Design relies on active airflow to clear moisture trap (passive system limitation)
- Extensive use of 3D printing with manufacturing constraints (0.5mm wall features not feasible)
- Iterative design process showing unresolved interference issues and client coordination challenges
- Unconventional weep hole creation method (heated needle melt-through) suggests tight spatial constraints
- Design prioritizes simplicity over sophistication due to physical space limitations