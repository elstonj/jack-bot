# SOCOM S0-AD EO/IR IPB Real-time ATR

## Document Metadata
- **Type:** Proposal (Rough Order of Magnitude estimate)
- **Client/Agency:** SOCOM (Special Operations Command)
- **Program/Solicitation:** SOCOM ROM submission
- **Date:** August 24, 2026
- **BST Products/Systems Referenced:** S0-AD, SwiftCore, SwiftControl, SwiftLinkUI
- **Key Personnel:** Elston/Hild, Stachura M, Fromm J, Lomis A, Straus N, Busby B, Prendergast D (Daniel Prendergast listed as last editor)

## Executive Summary
Black Swift Technologies proposes an AI-enabled Intelligence Preparation of the Battlefield (IPB) system using the S0-AD airframe equipped with EO/IR cameras and onboard Automated Target Recognition (ATR). The system will conduct pre-mission surveillance in contested airspace to confirm enemy formations and dispositions, transmitting compact target data and still images in near real-time while maintaining operator control via line-of-sight datalink.

## Technical Approach

**Core Concept:** Record, Recover, Post-process
- Automated target recognition of camera imagery with near real-time transmission of target data packets (not full motion video)
- Human-monitored, AI-enabled ISR operated by ground or aircraft-based operator maintaining LoS communication
- Onboard processing for autonomous/no-communication mission capability with end-of-flight data dump

**System Architecture:**
1. **Sensor Processing:** EO/IR cameras feed onboard ATR algorithm
2. **ATR Hardware Selection:** Trade study between (a) camera + separate single-board computer or (b) integrated AI processing camera
3. **Data Transmission:** Target packets + still images via Microhard datalink radio (P400 or higher bandwidth alternative)
4. **Control:** Samsung Tablet with SwiftLinkUI software, SwiftControl FMS, and SwiftCore modifications

**ATR Processing:** Load, integrate, and test third-party ATR algorithm to identify target type, number, location, elevation, and orientation.

## Products & Capabilities Described

### S0-AD Airframe
- **What it is:** Reusable tactical ISR platform (with future robustness improvements; currently sustains light damage on ~50% of landings)
- **Specifications:**
  - Endurance: >1 hour
  - Range: >50 nm
  - Low visual and acoustic signature
  - GPS/GNSS capable
  - Operates with LoS datalink to 50 nm

### EO/IR Payload
- **EO Camera:** 12 megapixel, fixed downward/forward-looking, no gaps in coverage over 1+ hour
- **IR Camera:** 5 megapixel, fixed downward/forward-looking, objective requirement (threshold is EO only)
- **Storage:** Removable media or high-speed data transfer port

### SwiftCore & SwiftControl Software
- **Modifications required:**
  - Low-comm mode with selectable transmission rates or complete suppression in LoS
  - Fully autonomous/no-communication mission execution capability
  - Display detected targets and metadata on operator UI
  - Pull-up target still images (1280x720 resolution)
  - Near-end-of-flight data dump functionality

### Datalink & Communications
- **Radio:** Microhard P400 (or higher bandwidth alternative) for aircraft telemetry, atmospheric data, and still images
- **Transmission Requirements:**
  - Single target data packet every 5 seconds over 50 nm
  - Single target image (1280x720) no more frequently than every 60 seconds over 50 nm
  - Aircraft telemetry minimum every 20 seconds at 50 nm range

## Use Cases & Applications

**Mission Context:** Intelligence Preparation of the Battlefield (IPB) in hours prior to SOCOM operations
- Confirm previous intelligence estimates of enemy formations, dispositions, and activities
- Operate in enemy-controlled battlespace with active enemy combatants and patrols
- Support pre-mission planning and go/no-go decision criteria
- Allow mid-mission system retasking based on findings
- Standoff operation from ground or host aircraft

## Key Technical Tasks

1. Select and design modifications for EO & IR cameras, ATR processing hardware, image storage
2. Integrate ATR algorithm (including subcontractor licensing)
3. Datalink radio selection and low-comm/no-comm code updates
4. UI updates for target detection display and still image retrieval
5. Fabricate/purchase components and build test article
6. Bench, ground, and flight testing with iterations
7. Operational test with SOCOM personnel

## Cost & Staffing

**ROM Estimate:** $221,262 (total with fee/profit)
- **Direct Costs:** $126,954
  - Personnel: $102,454 (7 staff members, 802 total hours at $125/hr with 29.28% fringe)
  - Equipment (purchased): $11,500
  - Travel: $5,000 (2 travelers, 3 nights)
  - Software licenses/other direct: $8,000

- **Indirect Costs:** $79,833 (OH 46.67%, G&A 18.32%)
- **Fee:** $14,475 (7%)

**Disclaimer:** ROM is preliminary, non-binding, intended for planning/budgeting only. Personnel rates are blended averages; specific personnel not yet identified.

## Notable Details

- **Operational Model:** Near real-time target data transmission eliminates need for full motion video transmission, reducing bandwidth requirements
- **Autonomous Capability:** System designed for fully autonomous mission execution with no communication, enabling operation in radio-denied environments
- **Iterative Approach:** Includes bench, ground, flight testing phases with fixes/iterations before SOCOM operational test
- **Reusability Path:** Document acknowledges S0 is currently non-reusable but identifies path to future reusability through component robustness improvements
- **Algorithm Integration:** ATR algorithm selection and integration appears to involve third-party IP requiring licensing
- **Contingency:** If Microhard P400 insufficient for datalink, proposal includes investigation of higher bandwidth alternatives