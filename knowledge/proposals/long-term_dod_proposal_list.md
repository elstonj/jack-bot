# Long-term DoD Proposal List

## Document Metadata
- Type: Strategic proposal pipeline document / concept portfolio
- Client/Agency: U.S. Department of Defense (multiple commands)
- Program/Solicitation: Multiple open solicitations listed (SIETE, WOLF, SIFTER, etc.)
- Date: Created 2025-09-01; Modified 2025-09-30
- BST Products/Systems Referenced: S0 VTOL, S3
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
This document outlines Black Swift Technologies' long-term DoD proposal strategy, presenting seven complete system concepts and five subsystem/algorithm concepts prioritized via competitive assessment. The portfolio emphasizes electromagnetic spectrum (EMS) collection and analysis capabilities, tactical network integration via NGC2, and multi-UAS coordination for intelligence, surveillance, and reconnaissance (ISR) and electronic warfare (EW) missions. Systems are sized for small tactical platforms (S0 VTOL and S3) with weight budgets under 30 lbs.

## Competitive Assessment Framework
BST evaluates proposal ideas across five dimensions (1=best, 3=worst):
- Military Function (operational necessity)
- Unique Solution (competitive differentiation)
- DoD Customer Base (market breadth)
- Operational Reward to Risk
- Feasibility (technical/schedule risk)

**Top-ranked Complete Systems (lowest index):**
- Company-level Electronic Patrol: Index 6
- EMS Unit Profiling (Pattern-of-Life): Index 7
- Base Perimeter Patrol: Index 8
- Expeditionary Runway Assessment: Index 11

## Complete System Concepts

### 1. Long-duration, Self-sustaining ISR
- **Index:** 10 (moderate priority)
- **Status:** Concept outlined but minimal detail provided

### 2. Expeditionary Runway Assessment Platform
- **Index:** 11
- **Mission:** Assess airfield suitability for expeditionary operations
- **Aircraft:** S0 VTOL or S3
- **Status:** Concept outlined; no detailed requirements provided

### 3. Electromagnetic Spectrum Unit Profiling (EMS Pattern-of-Life)
- **Index:** 7 (high priority)
- **Mission:** Collect EM pattern-of-life intelligence on enemy military formations to identify unit characteristics (type, specific identification, location, arrangement, activities)
- **Applications:** 
  - Intelligence analysis for operations planning
  - Friendly force characterization for force protection
  - Development of decoy operations
- **CONOPS:**
  - Single UAS with wideband RF receiver approaches known enemy position at acoustic standoff
  - Extended collection over time and at multiple times of day
  - GPS-denied, low-/no-comm operation capability required
  - Post-processing analysis to extract EM signatures
- **T/E Placement:** Battalion through Division level
- **Aircraft:** S0 VTOL or S3
- **Aircraft Requirements:**
  - Weight: <30 lbs
  - Payload Weight: >3.5 lbs
  - Cruise Speed: >40 knots
  - Dash Speed: >80 knots
  - Endurance: >2 hours
  - Wingspan: <7 ft
- **System-level Requirements:**
  - Receive and record N hours of RF data (frequency range X to Y at rate Z) [specifics not provided]
- **RF Payload:** Wideband RF receiver (specifications TBD)
- **NGC2 Integration Requirements:**
  - System discovery on NGC2 network
  - Broadcast target information over NGC2
  - Mesh repeating of NGC2 data traffic
  - Execute tasks from other NGC2 nodes
- **Supporting Requirements:**
  - Hardened radio (256-bit encryption, frequency hopping/shifting)
  - Low-/no-comm operation
  - GPS-denied navigation
- **End-user Units:** USMC/Army Battalion+ Intelligence, SOF intel units, SIGINT/COMINT units, NSA (potential)

### 4. Company-level Electronic Patrol
- **Index:** 6 (highest priority complete system)
- **Mission:** Security patrol of Battalion or Company-size area of operations using UAS-mounted RF sensors to detect and locate infiltrating aircraft and ground units
- **CONOPS:**
  - Multiple UAS with wideband RF receivers conduct individual patrol patterns
  - Signal detection triggers collaborative cueing: second aircraft approaches first and flies complementary pattern to localize signal source
  - Target information (type, location, frequency band, signal strength) transmitted over tactical data network
- **T/E Placement:** Battalion or Company
- **Flight Profile:** 
  - Area coverage ~100 sq km per aircraft
  - 40 knots cruise
  - 500 feet AGL
- **Target Systems:** 
  - Ground radios (squad comms, WiFi, Bluetooth)
  - Aircraft radios (drone control/telemetry, VHF/UHF)
- **Aircraft:** 2x S0 VTOL
- **Individual System Requirements:**
  - Provide line of bearing to RF source (20-second emission)
  - Locate RF source using flight pattern (20-second emission)
  - Classify RF source (e.g., "DJI drone," "FRS radio")
  - Close distance to weak RF source for better acquisition
  - Send collaborative location requests
- **Multiple System Collaboration Requirements:**
  - Respond to collaborative location requests
  - Fly complementary patterns to locate RF sources
- **Aircraft Specifications:**
  - Weight: <20 lbs
  - Payload Weight: >3.5 lbs
  - Cruise Speed: >40 knots
  - Dash Speed: >80 knots
  - Endurance: >2 hours
  - Wingspan: <7 ft
- **Sensor Requirements:**
  - Receive signals from X kHz to Y GHz [specifics not provided]
- **NGC2 Integration Requirements:**
  - System discovery on NGC2 network
  - Broadcast target information over NGC2
  - Mesh repeating of NGC2 data traffic
  - Execute tasks from other NGC2 nodes
- **Supporting Requirements:**
  - Hardened radio (256-bit encryption, frequency hopping/shifting, low-/no-comm mode)
  - GPS-denied return-to-base capability

### 5. Emulation of Unit Electromagnetic Spectrum Signature
- **Index:** 9
- **Status:** Title only; no details provided

### 6. Base Perimeter Patrol
- **Index:** 8
- **Status:** Title only; no details provided

### 7. Air-deployed Weather Sensing Platform
- **Index:** 9
- **Status:** Title only; no details provided

## Subsystems/Algorithms
All subsystems/algorithms listed without detailed requirements:
1. **Terrain Flight Algorithm** (Index: 7)
2. **Auto Landing Zone Selection** (Index: 8)
3. **Swarm Tasking Optimization for Maximum Information Gain** (Index: 9)
4. **Battle Damage Assessment** (Index: 8)
5. **Preflight Mission Planner** (Index: 7)

## System Enabling Functions
BST identifies five core enabling capabilities required across concepts:
- Hardened Radio (256-bit encryption, frequency hopping/shifting)
- Low-/No-comm Operation
- GPS-denied Navigation
- Obstacle Avoidance
- Terrain Flight
- Tactical Network Integration (NGC2)

## Open Solicitations Pipeline
BST tracks the following DoD solicitations:

| Solicitation | Type | Due Date | Notes |
|---|---|---|---|
| EW Payload for sUAS | RFI | 26-Sep-2025 | Relevant to Company-level Electronic Patrol |
| Silent Swarm 2026 | Conf/Demo | 31-Oct-2025 | No funds |
| SIETE (Signals Information Exploitation Tech Enhancements) | ARA | 28-Feb-2026 (Rolling) | Not directly applicable |
| NAWCAD WOLF Airborne Systems Integration Division BAA | BAA | 9-Apr-2026 | High relevance expected |
| SIGINT Solutions for Evolving Scenarios | BAA | 25-Sep-2028 (Rolling) | High relevance expected |
| AAL BAA for Disruptive Technologies | BAA | 4-Apr-2029 (Rolling) | Potential fit |
| SIFTER (Signals Intelligence Focused Tech for Exploitation) | ARA | 29-Sep-2029 (Rolling) | High relevance expected |
| BPA for Blue List Drones | BPA | 31-Jul-2030 | High relevance expected |
| Foreign Military Sales | — | N/A | Open opportunity |

## Key Talking Points
- Intuitive drone platform
- EW capabilities executed at the company level (tactical decentralization)
- Discoverable and reporting node on NGC2 network (multi-platform integration)
- EW antennas integrated into airframe for SWAP (Size, Weight, and Power) minimization

## Notable Details
- **Platform Focus:** Both concepts with highest detail (EMS Pattern-of-Life and Company-level Electronic Patrol) center on RF collection and analysis using small VTOL platforms
- **Emphasis on Low-comm/GPS-denied ops:** Multiple requiring requirements highlight autonomous operation in contested/denied environments
- **NGC2 Network Criticality:** All detailed complete systems include NGC2 integration, indicating DoD emphasis on tactical data network interoperability
- **Competitive Advantage:** EW antenna integration into airframe, multi-UAS collaborative tasking, and autonomous source localization differentiate BST offerings
- **Customer Base:** Battalion to Division-level intelligence units, SOF, SIGINT/COMINT, and potentially NSA identified as end-users
- **Solicitation Strategy:** Portfolio aligned with multiple rolling BAAs with deadlines extending through 2030; emphasis on SIGINT/EW solicitations and airborne systems integration