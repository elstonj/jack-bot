# Intelli-Copter Micro-Unmanned Aerial System White Paper

## Document Metadata
- Type: White Paper / Proposal
- Client/Agency: Intuitive Research and Trading Organization (INTUITIVE)
- Program/Solicitation: Not specified
- Date: July 22, 2013
- BST Products/Systems Referenced: Custom MUAS (Micro Unmanned Aerial System), Intellicopter
- Key Personnel: Not named (document refers to team members generically)
- Partner Organizations: Leptron (helicopter platforms), Chiaro Technologies (structured light 3D imaging)

## Executive Summary
This white paper proposes development of the "Intellicopter," a fieldable micro-unmanned aerial system (MUAS) that can autonomously search, map, and visualize the interior of confined structures (caves, buildings) using custom VTOL design integrated with advanced 3D imaging and autonomous navigation. The system would provide operators real-time 3D models and situational awareness of interior environments from a safe stand-off distance, addressing missions where time-critical interior intelligence is needed.

## Technical Approach

**System Architecture Overview:**
- Custom-designed micro helicopter with minimum 30-minute flight time
- Vertical takeoff and landing (VTOL) capability for confined space operation
- Six degree of freedom (6DOF) simultaneous localization and mapping (SLAM) using 3D range measurements
- Structured light 3D imaging technology (both visible and IR)
- Autonomous navigation and GPS-denied environment operation via autopilot
- Ad hoc wireless communication with reactive control system
- Tablet-based operator control unit (OCU) with touch/gesture controls

**Structured Light 3D Imaging:**
- Custom IR structured light pattern and projector designed for SWaP constraints of micro aircraft
- Operates across full spectrum from complete darkness to direct sunlight
- Array of EO/IR cameras capture structured light patterns for real-time range measurements
- Enables autonomous collision avoidance and obstacle navigation
- Real-time 3D model generation overlaid on operator display

**Phased Development Approach:**
- **Phase 1 (8-12 months):** Design vehicle and sensor systems separately; develop and test first working prototypes to TRL-6; initial testing on small COTS platform
- **Phase 2 (6-8 months):** Integrate vehicle with imaging and communications payload; deliver complete system at TRL-8
- Significant unit and field testing in each phase

## Products & Capabilities Described

**Intellicopter System**
- What it is: A man-portable, ruggedized MUAS designed for indoor/cave mapping and structure reconnaissance
- Proposed use: Autonomous search and 3D mapping of confined interior environments; rapid deployment for law enforcement, military, or emergency response scenarios
- Key specifications:
  - Minimum 30-minute flight time
  - VTOL design for confined spaces
  - GPS-denied environment capable
  - Structured light 3D imaging with IR capability
  - Real-time autonomous navigation and obstacle avoidance
  - Tablet-based control interface
  - Secure wireless communication system

## Use Cases & Applications

- Interior mapping of multi-level buildings and confined structures
- Cave exploration and mapping
- Search and rescue operations (locating people in structures)
- Law enforcement reconnaissance (identifying hidden rooms, tactical situational awareness)
- Emergency response scenarios requiring time-critical interior intelligence
- Operations where operator safety requires stand-off distance from structure

## Technical Development Scope

**Key System Components:**
1. Custom micro helicopter airframe
2. Autopilot for augmented/autonomous operation in constrained environments
3. EO/IR camera system for remote video
4. 3D structured light imaging payload (visible and IR)
5. Wireless communication with reactive control
6. Compact tablet-style operator control unit

**Development Process:**
- Requirements definition (customer and contractor collaboration)
- Detailed design specifications
- Hardware, software, and mechanical development
- Unit testing of individual elements
- Integrated system testing
- Comprehensive field testing
- Final acceptance review against requirements

## Notable Details

**Team Composition & Rationale:**
- **Black Swift Technologies:** UAS design, integration, and deployment; FAA regulatory expertise; hundreds of field deployments across U.S.; experience with multiple airframes
- **Leptron:** Industrial helicopter platforms; focus on law enforcement, military, civilian use; high payload capacity, range, altitude, harsh environment operation
- **Chiaro Technologies:** Structured light and triangulation-based 3D imaging; patented algorithms and optical technology; OEM components for 3D capture systems

**Cost/Schedule Risk Mitigation:**
- Two-phase approach reduces customer risk
- Sensor system developed on COTS platform first before custom helicopter integration
- Phased TRL advancement (TRL-6 Phase 1, TRL-8 Phase 2)

**Competitive Advantages:**
- No existing UAS system available that is fieldable and meets mission objectives
- Integration of structured light 3D imaging with autonomous flight in GPS-denied environments
- Real-time 3D model generation with measurement capability
- Man-portable deployment capability
- Multi-mission, minimally trained operator interface

**Unique Technical Capability:**
- Custom IR structured light projector designed to SWaP constraints of micro aircraft—key innovation for operating across full lighting spectrum in confined spaces