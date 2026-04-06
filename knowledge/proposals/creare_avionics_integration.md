# Creare Avionics Integration

## Document Metadata
- Type: Technical integration guide / design documentation
- Client/Agency: Creare (partner/customer)
- Program/Solicitation: 2019 VTOL Autopilot project
- Date: 07 August 2020 (Version 1.1)
- BST Products/Systems Referenced: SwiftPilot™ (autopilot)
- Key Personnel: Danny Troke (contact), Jack Elston (last editor)

## Executive Summary
This document provides detailed technical guidance on integrating avionics and flight control systems into the Double Eagle VTOL aircraft platform. It describes the mechanical mounting architecture, component layout, integration procedures, and weights for all avionics components, with emphasis on maintaining structural integrity, CG flexibility, and environmental protection during operation.

## Technical Approach

**Mounting Architecture:**
- Three-plate fiberglass foam-core assembly spaced by standoffs matching battery height
- 5 standoffs per battery level to secure batteries during flight; accommodates battery swelling with spacers
- 90° aluminum mounting brackets bolt assembly to carbon fiber side plates of main frame
- Vertical dot markers on CF plates allow CG adjustment to accommodate VTOL-to-forward-flight transitions

**Avionics Layout:**
- SwiftPilot™ mounted to dedicated plate with anti-vibration material, secured with loosely-bound screws and locknuts to prevent material compression
- Actuator boards mounted in 3D-printed trays, glued or taped to main avionics tray adjacent to respective ESC/motor
- Power board, radio, and laser actuator board mounted below main avionics trays
- GPS mounted via 90° aluminum bracket and standoff, aligned with autopilot axis
- ESCs screwed directly to frame mounting cubes
- RC receiver mounted outside carbon fiber plate with antennas positioned 90° apart on opposite sides for maximum range and reduced CF interference

**Environmental Protection:**
- Upper avionics trays sealed with Kapton tape during flight
- Lower avionics secured in 3D-printed cases or wrapped in Kapton tape to prevent contamination
- Future iterations planned for consolidated 3D-printed avionics enclosure

## Products & Capabilities Described

**SwiftPilot™ (Autopilot)**
- Weight: 16g
- Mounted on isolated anti-vibration plate to reduce noise transmission
- Serves as primary flight control system for VTOL platform
- Aligned with GPS for coordinated navigation

**Avionics Components:**
- Castle 120A ESCs (4x, 152g each = 608g total)
- Laser Altimeter (20g)
- Radio (15g)
- Actuator boards (6x, 7g each = 42g total)
- Power Supply Board (50g)
- Anderson Connectors (2x, 25g each = 50g total)

## Use Cases & Applications
- Double Eagle VTOL platform operations
- Dual-mode flight (vertical takeoff/landing with forward flight capability)
- Operations requiring altitude measurement (laser altimeter)
- Remote control and autonomous flight modes

## Notable Details

**Total Avionics Weight:** 801g for complete system

**Design Considerations:**
- Nonconductive materials preferred for mounting structure to avoid electrical interference
- CG adjustability built in for flight mode transitions
- Extensive use of 3D-printed components for custom fit and weight optimization
- Kapton tape used throughout for environmental sealing
- Anti-vibration isolation specifically implemented for autopilot to improve performance

**Manufacturing Details:**
- Fiberglass foam-core plates
- Carbon fiber structural frame integration
- Aluminum standoffs and brackets for precision mounting
- Rubber grommets for wire routing

**Status:** Project marked as "Completed/Inactive" in file system (created Aug 2020, last modified Sept 2020)