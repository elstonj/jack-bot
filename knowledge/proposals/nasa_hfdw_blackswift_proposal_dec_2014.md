# NASA SBIR Phase I Proposal: Multiple Unmanned Asset Management System (MUAMS)

## Document Metadata
- **Type:** NASA SBIR Phase I Proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR (solicitation year not explicitly stated; context suggests 2014-2015)
- **Date:** December 2014
- **BST Products/Systems Referenced:** SwiftCore, SwiftTab, SwiftPilot, SwiftStation
- **Key Personnel:** Dr. Jack S. Elston (Black Swift Technologies CEO/co-founder), Dr. Cory Dixon (Black Swift Technologies Director of Engineering), Scott Scheff (HF Designworks CEO/PI), Dr. Lindsay Tack, Dr. Jack S. Elston
- **Partner Company:** HF Designworks, Inc. (prime contractor); Black Swift Technologies (subcontractor)

---

## Executive Summary

HF Designworks and Black Swift Technologies propose developing a Multiple Unmanned Asset Management System (MUAMS) to enable a single operator to effectively supervise and manage up to five UAS simultaneously while monitoring sensor payloads, shifting the operational paradigm from "pilot" to "asset manager." The system introduces a novel triage role to handle malfunctioning aircraft, reducing cognitive workload on primary operators, and incorporates advanced ground control station (GCS) features including automation, heat mapping visualizations, and sensor fusion based on Black Swift's tablet-based SwiftTab platform.

---

## Technical Approach

### Core System Architecture
The proposed MUAMS comprises two integrated subsystems:

1. **MUAMS-Manager (Primary):** Tablet-based GCS (Black Swift's SwiftTab) optimized for supervising up to 5 healthy UAS
   - Single operator manages multiple assets and sensor payloads
   - Focus on high-level mission management, not low-level flight control
   - Implements adaptive automation to reduce cognitive load
   
2. **MUAMS-Triage Command (Secondary):** Larger hardware interface (proposed Microsoft Surface Table) for triage personnel
   - Dedicated role for managing distressed/malfunctioning aircraft (one triage person per ~5 managers = up to 25 total UAS)
   - Enables task shedding when assets require intensive operator attention
   - Shared Common Operating Picture (COP) with primary operators

### Key Technical Components

**Paradigm Shift from Piloting to Managing:**
- Current systems require multiple operators per UAS (e.g., Ikhana requires 4+ operators)
- Proposed system emphasizes high-level mission supervision with onboard autonomy handling low-level flight control
- Cognitive workload reduced through automation and delegated control

**Automation Strategy:**
- **Phase I focus:** Detect and Avoid (DAA) automation in cooperative communications environment; predictive path planning if comms lost
- **Phase II expansion:** Route planning assistance based on historical asset locations and coverage patterns
- Adaptive automation that increases with task complexity and cognitive workload

**User Interface Innovations:**
- **SwiftTab baseline:** Android tablet-based GCS with multi-gesture inputs (drag-drop, sketch gestures), touch screens, haptic feedback, accelerometers
- **Current SwiftTab capabilities:** 
  - Mid-flight flight plan design and upload
  - Vehicle health/status monitoring
  - Gesture-based map view and flight plan modification
  - Three operating modes: Observer (view-only), Operator (standard control), Integrator (autopilot tuning)
  - Status color-coding: black (nominal), blue (manual control), yellow (warning), red (fault/intervention required)

- **Proposed Phase I enhancements:**
  - Optimization for 1:5 operator-to-asset ratio
  - New Triage mode interface for damaged aircraft management
  - Heat mapping visualizations showing asset coverage patterns and areas requiring attention
  - Gesture-based asset handoff mechanism ("flick" gesture to transfer control to triage personnel)
  - Reduced alert clutter through filtered information display
  - Global situational awareness displays enabling route planning ahead of mission execution
  - Sensor fusion for combined payload data understanding

**Visualization and Decision Support:**
- Heat mapping algorithm (developed by HF Designworks, tested with helicopters and Soldiers in Afghanistan) visualizes:
  - Asset coverage areas
  - Sensor coverage zones
  - Areas not yet covered
  - Historical traversal frequency
- Information filtering based on operator role (manager vs. triage personnel)
- Multimodal information presentation (visual, auditory, haptic) to distribute cognitive load

### Operational Concept (CONOPS)

**Standard Mission Flow:**
1. Operator plans missions for up to 5 UAS with assistance from automation and visualizations
2. Assets execute missions; operator monitors health and sensor data
3. Operator views incoming sensor payloads as primary responsibility (not flight control)

**Contingency Flow - Asset Malfunction:**
1. Malfunctioning asset identified by operator, triage personnel, or system (Phase II)
2. Asset transferred from operator to triage personnel via:
   - Operator "pushes" troubled asset (gesture-based)
   - Triage personnel "pulls" troubled asset when alerted
   - System automatically routes to triage (Phase II)
3. Operator returns focus to remaining healthy UAS; triage personnel recovers distressed asset

**Manned-Unmanned Teaming:** (mentioned but not fully detailed)
- System enables single operator to task teams of UAS alongside manned assets
- Example: firefighter directing unmanned assets to scan mountainous region for hot spots
- Example: scientist autonomously running volumetric sampling mission

---

## Products & Capabilities Described

### Black Swift Technologies SwiftCore Flight Management System

**Components:**
- **SwiftPilot:** On-board autopilot system for autonomous flight control
- **SwiftTab:** Tablet-based ground station using Android OS
  - Multi-gesture input support
  - Touch screen, haptic feedback, accelerometer integration
  - Intuitive UI designed for rapid operator familiarization (5-10 minutes for novice users)
  - Three operating modes (Observer/Operator/Integrator)
  - Vehicle status visualization with color-coded health indicators
  - Real-time telemetry plotting and display
  - Flight plan design and mid-mission modification
  
- **SwiftStation:** Portable communication relay between UAS and tablet

**Performance Claims:**
- Average user (no aviation experience) can familiarize with controls in 5-10 minutes
- Supports supervised operation of up to 5 UAS by single operator with triage support
- Maximum operator-to-asset ratio: 1:5 based on prior testing

**Related BST Work Referenced:**
- NASA Phase I SBIR: "Advanced Technologies for Coordinated In Situ Atmospheric Sensing" (CAPS system)
  - Multi-aircraft atmospheric profiling system
  - Designed for manned-unmanned teaming
  - Focus on back-end multi-vehicle coordination; this proposal adds improved human interface
  
- NASA Phase II SBIR: "Soil Moisture Mapping sUAS"
  - Advanced UAS for soil moisture mapping missions

### HF Designworks Contributions

- Heat mapping algorithm and visualization tools (proven in Afghanistan with Soldiers, tested with unmanned helicopters)
- User-centered design methodology and human factors expertise
- Distributed team workload assessment tools (developed for OSD)
- Persona development and task analysis methodologies
- Formal usability testing plan development

---

## Use Cases & Applications

### Scenario 1: Dynamic Fire Detection and Monitoring
- **Context:** Rapid response to detected forest fire requiring asset deployment to mountainous region
- **Mission:** Multiple UAS rush to fire area to assess scope, location, and growth
- **Operator Role:** Manager supervises asset paths while reviewing sensor feeds in real-time
- **MUAMS Features Leveraged:**
  - Automation handles routine flight control
  - Heat mapping shows UAS coverage over past 6 hours
  - System identifies hot spots; operator receives alerts
  - Manager maintains overview of all assets without low-level control burden

### Scenario 2: Scientific Field Sampling with Contingency
- **Context:** Less urgent soil data collection mission
- **Mission:** 4-5 UAS fly coordinated grid pattern over field to collect soil data
- **Contingency:** One asset malfunctions mid-mission
- **Operator Role:** Manager supervises flight paths and payload data; triage personnel alerted to malfunction
- **MUAMS Features Leveraged:**
  - Manager and triage personnel communicate over shared COP
  - Triage personnel pulls control of malfunctioning asset via triage window
  - Manager reassigns new healthy asset to complete mission
  - Manager focuses on remaining healthy assets without high-stress malfunction response

### Additional Applications Mentioned (Not Detailed)
- Volcano monitoring (Dragoneye deployment referenced)
- Weather pattern detection
- Manned-unmanned teaming for firefighting operations
- Volumetric atmospheric sampling by scientist with minimal crew
- Sensor platform operations (viewing multiple sensors as data sources rather than aircraft)

---

## Technical Objectives (Phase I)

1. **Incorporate automation** into existing Black Swift GCS
2. **Revise operational concept** to support task shedding via triage personnel handoff
3. **Incorporate global situational awareness visualizations** enabling multi-UAS supervision and route planning
4. **Integrate sensor fusion** for improved understanding of incoming payload data

---

## Work Plan Summary (Phase I)

### Tasks Proposed

**Task 1: Literature Review**
- Review existing multi-asset tasking interfaces and tools (commercial: Piccolo Command Center, QGround Control)
- Leverage HF Designworks' Navy Littoral Combat Ship work (single operator controlling two remote minehunting vehicles)
- Consult subject matter experts (former UAS operators)
- Identify emerging technologies for integration

**Task 2: System Requirements, Architecture, and CONOPS**
- Develop formal requirements for proof-of-concept system
- Define system architecture and operational constraints
- Document CONOPS describing end-user perspective, capabilities, and usage

**Task 3: Scenario Development**
- Develop two detailed scenarios (fire detection, field sampling) with UAS operators
- Demonstrate automation and advanced features (heat mapping) supporting supervisor role
- Illustrate triage personnel task-shedding concept

**Task 4: Personas Development**
- Create composite user characters:
  - UAS Manager, Researcher/Scientist (focus on sensors/data)
  - UAS Manager, Pilot (focus on aviation aspects)
  - Triage Personnel (troubled asset recovery)
- Coordinate with scenarios for consistency

**Task 5: Task Analysis and Cognitive Information Flow**
- Predict task analysis based on scenarios and personas
- Assess physical and mental activities, timing, frequency, complexity, workload
- Leverage HF Designworks' Multiple Resource Theory (MRT) workload tool
- Evaluate 1:N control ratios and data/function allocation requirements

**Task 6: Design Development and Iterative Internal Review**
- Frequent (bi-weekly) design reviews with internal SMEs
- Evaluate designs for safety, understanding, usability, intuitiveness, desirability
- Outline formal usability testing plan for Phase II
- Begin human use approval process for Phase II testing

**Task 7: Proof-of-Concept Development**
- Implement updates to Black Swift GCS
- Develop limited 1:N capability based on one scenario
- Deliverable: working prototype integrated into SwiftTab

**Task 8: Reporting**
- Comprehensive Phase I summary documenting activities, results, interface designs
- Prototype system walkthrough

**Task 10: Phase I Presentation Preparation**

### Key Meetings
- Meeting 1: Kickoff (HF Designworks Boulder facility or teleconference)
- Meeting 2: Phase I Final Presentation (customer location)

---

## Key Results (N/A - Proposal Document)

This is a proposal document, not a final report. No experimental results or findings are presented. However, the proposal references completed prior work:

### Related Completed Projects

**Black Swift Technologies:**
- NASA Phase I SBIR: "Advanced Technologies for Coordinated In Situ Atmospheric Sensing"
  - Resulted in CAPS multi-aircraft atmospheric sensing system
  - Focus on backend coordination; this proposal augments with improved GCS interface

**HF Designworks:**
- **U.S. Marines SBIR (2014-2015):** HSI Module and Material-Design Software for concurrent design
- **U.S. Navy SBIR (2014-2015):** Littoral Combat Ship (LCS) operational console modernization evaluation
- **NASA/U.S. Marines (2012-Present):** UAS in the NAS project
  - Supporting NASA Dryden Flight Research Center
  - Reviewing UAS advances, waypoint navigation, autopilot technologies