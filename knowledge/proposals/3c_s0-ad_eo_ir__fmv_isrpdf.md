# S0-AD EO/IR Full Motion Video ISR System

## Document Metadata
- **Type:** Rough Order of Magnitude (ROM) Proposal
- **Client/Agency:** SOCOM (Special Operations Command)
- **Program/Solicitation:** SOCOM ROM submission
- **Date:** August 24, 2026
- **BST Products/Systems Referenced:** S0-AD airframe, SwiftCore, SwiftControl, SwiftLinkUI
- **Key Personnel:** Elston J., Hild S., Stachura M., Fromm J., Lomis A., Straus N., Busby B., Prendergast D., Beck Cotter (Business Official)

## Executive Summary
Black Swift Technologies proposes integrating full motion video (FMV) ISR capabilities into the S0-AD UAS platform to enable persistent, real-time surveillance for SOCOM combat operations. The system combines EO/IR gimballed camera payload with datalink transmission and operator control interface to support target custody, indirect fire coordination, and aviation fire support missions in contested environments.

## Technical Approach

**System Architecture:** Record, Recover, Post-Process approach providing remote human operator FMV for real-time, high-cognition ISR tasks with manual and automated control modes.

**Key Components:**
- Gimballed camera system with manual control and automated tracking capabilities
- Dual sensor payload (EO and IR) with real-time compression and transmission
- Datalink radio infrastructure for command/control and video/telemetry relay
- Operator control station with tablet-based UI and flight management integration

**Integration Points:**
- Modify SwiftCore (FMS) and SwiftControl (operator interface) to accommodate camera control functions
- Investigate single-radio solution for consolidated aircraft control/telemetry and camera video/control (pre-selected Microhard pMDDL2280 for evaluation)
- No-comm autonomous transit mode capability to FMV operator location or objective area

## Products & Capabilities Described

### S0-AD Airframe
- Purpose: Platform for EO/IR FMV ISR system
- Specifications:
  - Endurance: >1 hour
  - Range: >50 nm
  - Low visual and acoustic signature
  - PCLT (Pulsed Control Link Telemetry) enabled

### Nextvision Dragoneye (Gimballed Camera)
- Purpose: Integrated EO/IR imaging payload
- EO capability: 1920×1080 resolution, 30 fps, real-time compression
- IR capability: 640×480 resolution, 30 fps, real-time compression
- Control modes: Manual gimbal slewing, object tracking, geolocation stare mode
- Output: Displays FMV centerpoint latitude/longitude and elevation to operator

### SwiftCore/SwiftControl Integration
- SwiftCore: Flight Management System modifications required
- SwiftControl: Operator UI software modifications to support camera functions
- Hardware: Samsung tablet as operator control station
- SwiftLinkUI: Operator interface for FMV display and camera control

### Datalink System
- Payload telemetry transmission: ≥2 Hz at 15 nm range
- EO FMV transmission: 1920×1080, 30 fps at 15 nm range
- IR FMV transmission: 640×480, 30 fps at 15 nm range
- Aircraft telemetry transmission: ≥once every 2 seconds at 50 nm range
- Constraint: Line-of-Sight (LoS) datalink requirement limits FMV availability to operators within 15 nm despite 50 nm aircraft transit capability

## Use Cases & Applications

**Operational Context:**
- Persistent observation during ISR tasks in enemy-controlled battlespace
- Real-time ISR support for combat actions (target fixing, custody maintenance)
- Indirect fire coordination and aviation fire support
- Objective area surveillance with potential enemy combatants or active patrols present

**Operational Modes:**
- Forward fires/aviation controller employment on objective area
- Standoff operation by system operator (ground-based or airborne) maintaining LoS datalink
- No-comm autonomous transit to operator location or objective area followed by LoS-dependent FMV operations

## Key Tasks and Deliverables

1. Select and design modifications for gimballed camera system
2. Select and design modifications for radio/datalink hardware
3. Develop basic UI for camera control and FMV viewing
4. Implement no-comm transit mode capability
5. Design, fabricate, and purchase components; build test article
6. Bench, ground, and flight testing with iterative refinements
7. Operational test with SOCOM personnel

## Budget Summary

**Total Estimated Cost: $219,597** (ROM estimate, preliminary and non-binding)

**Cost Breakdown:**
- Direct Labor: $103,262 (8 personnel, blended rate $125/hr with 29.28% fringe)
- Purchased Equipment: $17,000
- Travel (airfare, car rental, MIE): $5,000
- Overhead (46.67%): $48,192
- G&A (18.32%): $31,777
- Fee/Profit (7.0%): $14,366

**Staffing Estimate:** 23.87 months of effort distributed across 8 team members

**System Estimated Cost:** $38,000 (operational system cost)

## Notable Details

- **LoS Datalink Limitation:** Critical constraint—while aircraft can transit 50 nm, FMV operator location is restricted to 15 nm LoS range, requiring positioning of operator relatively close to operational area
- **Autonomous Capability:** No-comm transit mode addresses communication gaps during aircraft movement to/from FMV operator location
- **Parallel Development:** Datalink radio selection informed by equivalent requirements being evaluated in parallel project context
- **Personnel Rate Standardization:** Blended $125/hr rate applied across all labor categories as best estimate given preliminary stage; actual rates to vary with final staffing selections
- **ROM Nature:** Document explicitly disclaims binding nature and emphasizes preliminary status subject to requirement refinement
- **SOCOM Operational Testing:** Includes planned operational test phase with SOCOM personnel prior to system completion