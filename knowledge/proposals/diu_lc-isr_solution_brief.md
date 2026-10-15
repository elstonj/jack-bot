# DIU Low Cost ISR Solution Brief — KONDOR

## Document Metadata
- **Type:** Solution brief / capability proposal (presentation format)
- **Client/Agency:** Defense Innovation Unit (DIU)
- **Program/Solicitation:** DIU Low Cost ISR; Fly Off #2 (Long-Endurance 12-24+ Hours)
- **Date:** October 9, 2026 (submitted October 14, 2026)
- **BST Products/Systems Referenced:** S3 (KONDOR platform); SQA2 (heritage VTOL); C3P (autonomy/GCS software); MWT (multi-UAV relay)
- **Key Personnel:** Jack Elston (CEO/Co-Founder), Maciej Stachura (CTO/Co-Founder), Beck Cotter (last editor)

---

## Executive Summary

Black Swift Technologies proposes **KONDOR**, a hybrid-electric blended-wing VTOL aircraft for persistent, long-endurance ISR. Built on proven C-Astral airframe heritage and BST's SQA2/C3P autonomy foundation, KONDOR delivers 20+ hours endurance, 1,000+ mile range, day/night EO/IR collection, and expeditionary mobility—all at approximately **95% lower cost per mission hour than MQ-9**. The system combines commercial technology acceleration with a secured U.S. production path through KrateoSky industrialization.

---

## Technical Approach

### Aircraft & Propulsion
- **Blended wing body** form factor with **detachable wings** for transport by case or backpack
- **Hybrid-electric powertrain:** COTS engine/generator (modified for aircraft integration) powers propulsion and charges battery; generator cycling reduces acoustic signature
- **Electric-only quiet mode** option with planned stop/restart capability
- **Full-mission endurance modeling** informed by May 2026 hover/propulsion bench testing and June 2026 Design Concept Review

### Flight Performance (Projected)
| Parameter | Specification |
|-----------|---------------|
| **Endurance** | 20+ hours (full-mission simulation with VTOL launch/recovery, transitions, climb/cruise/descent) |
| **Range** | 1,000+ miles; example: 1,161 miles in 23-hour mission |
| **MTOW** | 55 lbs (24.9 kg) design target |
| **Cruise Speed** | 48 mph nominal |
| **Ceiling** | 3,000m (9,842 ft) nominal; 15% endurance reduction 1,500–4,000m |
| **Fuel Consumption** | 7 L for example 23-hour mission (no reserve) |
| **Battery** | 800 Wh onboard; generator replenishes during cruise |
| **Power Margin** | ~1,080 W generator output − 560 W cruise draw = margin for battery/reserve and payload growth |

### Development Timeline
- **Apr 2026:** Program kickoff
- **May 2026:** Hover & propulsion testing completed (demonstrated)
- **Jun 2026:** Design Concept Review (aerodynamic, endurance, payload, risk analyses)
- **Sep 2026:** Advanced composite fabrication; wings built/wired (in integration)
- **4Q2026:** Integrated flight-test campaign (VTOL transitions, cruise, sensor/comms integration, endurance, envelope verification) — projected
- **1Q2027:** Industrialization & DFM/DFA refinement

---

## Products & Capabilities Described

### KONDOR System (S3 Platform)
**What it is:**  
Group 2 UAS built on C-Astral blended-wing aircraft heritage (140,000+ global fleet flight hours), integrated with BST's SQA2 VTOL design and C3P autonomy software.

**Proposed use:**  
Persistent expeditionary ISR: day/night collection, BVLOS SATCOM, autonomous mission execution with operator authority, repeat sorties from austere sites.

**Key features:**
- Modular, detachable airframe for field transport
- <10-minute mobilization target (2-operator setup)
- Field refuel/refit capability for regenerating sorties
- MOSA-oriented architecture enabling payload swaps and third-party integration

---

### C3P Autonomy & Ground Control Software
**What it is:**  
Mission planning, flight supervision, payload control, and data recording interface; supports MAVLink, TAK/ATAK, STANAG 4609, MISB 0601.

**Capabilities:**
- Terrain/DTED-informed mission planning with guided preflight checks
- Autopilot execution with altitude/loiter modes and configurable failsafes
- Live video, remote payload control, target/convoy tracking
- Onboard recording, geolock, laser rangefinder integration
- Multi-UAV relay operations (demonstrated Sep 2026 SQA2/MWT in Portugal; KONDOR extension planned)
- **GNSS-denied navigation** in development: 100 km+ progress with 30m P95 horizontal error (no terrain-map or magnetic-field-map matching required)
- Operator retasking authority retained; operator approves, supervises, can intervene

---

### Payload Integration
**Selected prototype payload:**  
**Atmolab REX-151E Spatium**
- **Sensors:** 1920×1080 EO; 30× optical zoom; 55° wide FOV; uncooled LWIR 640×512
- **Stabilization:** 2-axis mechanical + software; continuous pan; pitch +50° to −150°
- **Mass/Power:** 2.15 kg, 20 W; dimensions 218.67 mm height / 147 mm dome
- **Functions:** Tracking, geolock, onboard recording; laser rangefinder separately available
- **Design Class:** ≤3 kg; adaptable payload/battery locations managed through mass/CG/power trade-offs

**Modularity approach:**
- Payload growth managed through defined interfaces, balance, and energy—no wholesale redesign required
- Heavier payloads conditional within 27 kg MTOW margin; installed mass, CG, drag, cooling, power, and reserves assessed together
- Fuel tank positioned at aircraft center-of-gravity to minimize balance-change during fuel burn

**Post-collection processing:**
- C3P supplies common aircraft/sensor supervision and acquisition-quality monitoring
- Optional **EagleEye** adds streaming, scene/object tracking, roll compensation, defog, KLV metadata, and H.264/H.265 handling

---

### Communications Architecture

**Local RF:**  
**Silvus StreamCaster 4400 4×4 MIMO radio**
- RF link-budget analysis: 9.8 Mbps capacity at 20 km / 2,440 MHz / 20 MHz bandwidth against 2.5 Mbps traffic / 25% airtime
- Dual-band MIMO, adaptive modulation, licensed MANET interference avoidance
- Carries aircraft commands, telemetry, EO/IR data within local RF coverage

**Long-range SATCOM:**  
**Starlink Mini Terminal** (repackaged commercial hardware, weight-reduced for airborne installation)
- Primary long-range BVLOS path
- Auto-tracking antenna
- Thermal, environmental, communications performance verified in integrated configuration

**DDIL Operating Approach:**  
Prioritize essential C2/telemetry over video demand; preserve onboard recordings; validate lost-link, reconnection, and RF/SATCOM transition behavior before fly-off.

**Government Integration:**  
C3P heritage includes TAK/CoT and STANAG 4609/MISB interfaces; KONDOR's integration package defines supported profiles, APIs, and rights for customer C2, battle-management, and ISR dissemination.

---

## Use Cases & Applications

### Expeditionary ISR Workflow
1. **Transport/Displacement:** Segmented airframe in case (~150 × 66 × 30 cm), man-backpackable load concept
2. **Deploy & Prepare:** Assemble, connect, complete preflight checks in <10 minutes (2-person team)
3. **Launch/Relaunch:** Vertical takeoff from austere site, no runway or launcher required
4. **Collect:** EO/IR imagery in wing-borne flight under operator supervision; 20+ hours continuous or segmented operations
5. **Recover:** Return to field site, land without dedicated recovery equipment
6. **Refuel/Sustain:** Refuel, inspect, refit, and generate repeat sorties (turnaround time TBD by detailed logistics planning)
7. **Control & Processing:** Plan, supervise, retask, record; deliver observations for human review

### Mission Profile Example
- **Flight time:** ~23 hours
- **Range:** 1,161 miles
- **Payload:** 3.3 kg
- **Cruise altitude:** 2,500 m
- **Cruise speed:** 48 mph
- **Fuel consumption:** 7 L (no reserve); battery maintained at landing
- **Endurance reduction:** ~15% from 1,500–4,000 m altitude band

### Environmental Suitability
- **Operating temperature:** −20°C to +55°C (target IP65 per SQA2 design principles)
- **Sensor OEM spec:** −40°C to +50°C / 30G shock / MIL-STD-810G
- **VTOL wind tolerance:** 20/25 km/h threshold/objective; cruise 35/40 km/h

---

## Key Results

### Development Maturity Status (as of October 2026)
| Milestone | Status |
|-----------|--------|
| Hover & propulsion testing | **Demonstrated (May 2026)** |
| Design Concept Review | **Completed (Jun 2026)** |
| Composite fabrication, wing build & wiring | **In integration (Sep 2026)** |
| Integrated flight testing (VTOL, cruise, sensors, comms, endurance, envelope) | **Projected 4Q2026** |
| Industrialization & DFM/DFA | **Projected 1Q2027** |

### Heritage Flight-Hour Base
- **C-Astral global fleet:** 140,000+ flight hours
- **Sovereign entities using C-Astral:** >10
- **Commercial/scientific operators:** 100+
- **SQA2 operational heritage:** Years of ISR missions with C3P software

### Cost & Efficiency Advantage

**Mission-Hour Economics (August 2026 dollars, CBO lifecycle model, 20-year horizon):**

| Metric | KONDOR | MQ-9 | Advantage |
|--------|--------|------|-----------|
| **Cost per mission hour** | ~$476 | ~$8,841 | **18.6× cheaper** |
| **Area coverage per $1M** (km² at matched resolution) | 312,000 | 68,000 | **4.6× more area** |
| **Assets in service per $50M/year** | 86 | 4.4 | **20× more aircraft** |
| **Mission hours per $50M/year** | 105,000 | 5,700 | **19× more hours** |

**Resilience benefit:**  
Losing one KONDOR aircraft costs ~1% of fielded capacity vs. ~23% for MQ-9 fleets, making KONDOR fleets more resilient to attrition and threats.

**Multi-aircraft economy:**  
Single operator controlling multiple aircraft via one interface reduces cost per flight hour by ~14% at 10 coverage lines (6 units).

### ROM Pricing (Notional, subject to prototyping and industrialization)

| Component | Price |
|-----------|-------|
| Aircraft system (each) | $210,000 |
| Payload (REX-151E, each) | $50,000 |
| RF communications link (each) | $52,500 |
| GCS (each) | $2,000 |
| Spares, tools, training, acceptance (each) | $10,000 |
| **Mission-equipped unit price** | **$324,500** (1 unit @ 0% discount) |

**Volume scaling (25/100/500 units):**
- 25 units: $8.1M total, 6-month lead time, 0% discount
- 100 units: $31.5M total, 