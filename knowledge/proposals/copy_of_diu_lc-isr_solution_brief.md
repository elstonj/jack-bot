# DIU Low Cost ISR Solution Brief: KONDOR

## Document Metadata
- Type: Solution brief / capability presentation
- Client/Agency: Defense Innovation Unit (DIU)
- Program/Solicitation: DIU Low Cost ISR competition (Fly Off #2)
- Date: October 9-14, 2026
- BST Products/Systems Referenced: S3 (KONDOR platform), SQA2, C³P autonomy software
- Key Personnel: Jack Elston (CEO and Co-Founder), Maciej Stachura (CTO and Co-Founder)

## Executive Summary
Black Swift Technologies proposes KONDOR, a hybrid-electric VTOL long-endurance ISR platform combining C-Astral blended-wing aircraft with KrateoSky program leadership and U.S. industrialization. The system delivers 20+ hour endurance, day/night EO/IR collection, BVLOS SATCOM via Starlink, spectrum-agile RF, and autonomous mission control at ~95% lower cost per mission hour than MQ-9 (~$476 vs. ~$8,841).

## Technical Approach

### Core Platform
- **Aircraft Foundation**: Hybrid-electric VTOL based on C-Astral blended wing body design
- **Propulsion**: Hybrid-electric system with generator-powered cruise and battery-electric start/quiet modes; ~1,080W generator output minus 560W cruise electrical draw
- **Airframe**: Detachable composite wings and removable booms for expeditionary transport (approx. 150×66×30 cm case dimensions)
- **MTOW**: 55 lbs design target
- **Wingspan**: 4.2 meters (13.7 feet)

### Communications Architecture
- **RF Link (Primary Local)**: Silvus StreamCaster 4400 4×4 MIMO radio
  - Link budget: 9.8 Mbps capacity at 20 km / 2,440 MHz / 20 MHz bandwidth
  - Dual-band MIMO, adaptive modulation, licensed MANET interference avoidance
  - Carries C2, telemetry, and EO/IR data within local coverage
- **SATCOM (Primary Long-Range BVLOS)**: Modified Starlink Mini Terminal with auto-tracking antenna
  - Repackaged commercial hardware for reduced airborne mass
  - Redundant path to Silvus RF
  - DDIL (Deny, Delay, Disrupts, Interacts, Limits) operating approach prioritizes C2/telemetry

### Autonomy & Control
- **C³P Software Heritage**: Extended from SQA2 with 20+ years ISR mission experience
- **Flight Control**: MAVLink integration; separate flight safety, sensor processing, communications
- **Operator Authority**: Mission planning, supervision, control, and retasking maintained by operator
- **Mission Functions**:
  - Terrain/DTED-informed planning with preflight checks
  - Autopilot route execution with altitude/loiter modes
  - Live video, remote payload control, target tracking, retasking
- **Autonomy Development**:
  - Multi-UAV control from single interface
  - GNSS-denied navigation: 100+ km range with 30m P95 horizontal error (no terrain/magnetic mapping required)
  - Relay-enabled cooperation (demonstrated September 2026 with SQA2/MWT in Portugal)

### Software Architecture
- **MOSA-Oriented Design**: Separate flight safety, sensor processing, communications, ground software with standard electrical/data boundaries
- **Standards Support**: TAK/ATAK, STANAG 4609, MISB 0601, CoT interfaces
- **Ground Control Station (C3P)**: Mission planning, telemetry monitoring, payload supervision, recording, and export
- **Optional Enhancement**: EagleEye adds streaming, scene/object tracking, roll compensation, defog, KLV metadata, H.264/H.265 handling

## Products & Capabilities Described

### KONDOR System (S3)
**What It Is**: Long-endurance hybrid-electric VTOL ISR platform combining persistent collection capability with expeditionary deployment flexibility.

**Proposed Use**: 
- Persistent ISR in compact deployable package
- Day/night collection with modular payload integration
- Group 2 UAS category operation
- Expeditionary sorties with <10 minute mobilization objective

**Key Specifications**:
- **Endurance**: 20+ hours (projected, full-mission simulation including vertical launch/recovery, transitions, climb/cruise/descent)
- **Range**: 1,161+ miles (example mission: ~23 hours flight, 3.3 kg payload, 2,500m altitude, 48 mph cruise)
- **Cruise Speed**: 48 mph nominal at 3,000m ceiling (15% endurance reduction from 1,500–4,000m)
- **Ceiling**: 3,000m nominal (9,842 ft)
- **Fuel Consumption**: 7 liters for 23-hour mission profile (no reserve modeled)
- **Electric Reserve**: 800 Wh battery maintained at landing through generator cycling
- **Power Architecture**: 
  - Generator output: ~1,080 W
  - Cruise electrical draw: ~560 W
  - Available margin: shared with battery/reserve and payload growth

### Payload Integration
**Selected Baseline Payload**: Atmolab REX-151E Spatium (demonstrated)
- **EO/IR Capability**: 1920×1080 EO with 30× optical zoom, 55° wide FOV; uncooled LWIR 640×512
- **Stabilization**: 2-axis mechanical + software with continuous pan; pitch +50° to −150°
- **Sensor SWaP**: 2.15 kg / 20 W; 218.67 mm height / 147 mm dome
- **Collection Functions**: Tracking, geolock, onboard recording; laser rangefinder separately selected
- **Environmental Tolerance**: −40°C to +50°C / 30G shock / MIL-STD-810G

**Payload Modularity**:
- Designed for ≤3 kg payload class (reference payloads)
- Heavier payloads conditional within 27 kg MTOW margin; mass, CG, drag, cooling, power, reserves assessed together
- Fuel tank positioned at aircraft CG to minimize fuel-burn balance changes
- ~1,080 W generator output supports payload growth within margin

### SQA2 (Referenced for Heritage)
- **Type**: eVTOL platform
- **Operational Heritage**: 140,000+ fleet flight hours across 10+ sovereign entities and 100+ commercial/scientific operators
- **Role in KONDOR**: Basis for detachable assemblies, field sustainment practices, autonomy architecture (C³P software), and operational proven concepts

## Use Cases & Applications

1. **Persistent ISR Collection**: 20+ hour continuous area surveillance without prepared runways
2. **Expeditionary Operations**: Deployable from austere sites with minimal ground infrastructure
3. **Hostile/Contested Environments**: Spectrum-agile RF (Silvus), GNSS-denied autonomy, multiple communication paths (RF/SATCOM redundancy)
4. **Multi-Aircraft Operations**: Single operator controls multiple KONDOR units; relay-enabled cooperation for extended coverage
5. **Area Coverage Mission**: Example 4.6× more area coverage per dollar vs. MQ-9 at matched resolution
6. **Rapid Deployment**: <10 minute mobilization objective with 2-person team
7. **Sustained Coverage**: Multiple repeat sorties with field refueling, inspection, and quick turnaround

## Key Development Progress

| Milestone | Status | Details |
|-----------|--------|---------|
| Apr 2026 – Program Kick-Off | Completed | Mission requirements and verification approach defined |
| May 2026 – Hover/Propulsion Testing | Demonstrated | Initial hover and bench testing completed |
| Jun 2026 – Design Concept Review | Completed | Aerodynamic, endurance, payload, interface analyses consolidated |
| Sep 2026 – Build and Integration | In Integration | Composite fabrication with built/wired wings; composite design complete |
| 4Q2026 – Flight Testing Program | Projected | VTOL transitions, cruise, sensor/comms integration, endurance verification |
| 1Q2027 – Industrialization | Projected | DFM/DFA application, manufacturability refinements |

## Cost & Business Model

### Pricing (ROM estimates; notional, subject to final prototyping/flight test)
| Quantity | Aircraft Unit | Payload | RF Link | GCS | Spares/Tools | Mission-Equipped Unit Price | Quantity-Price Reduction | Lead Time |
|----------|---------------|---------|---------|-----|--------------|--------------------------|-------------------------|-----------|
| 25 | $210k | $50k | $52.5k | $2k | $10k | $8.1M | 0% | 6 months |
| 100 | — | — | — | — | — | $31.5M | 3% | 7 months |
| 500 | — | — | — | — | — | $154.1M | 5% | 11 months |

### Cost Comparison vs. MQ-9 (August 2026 dollars, 20-year lifecycle)
| Metric | KONDOR | MQ-9 | Advantage |
|--------|--------|------|-----------|
| Cost per mission hour | ~$476 | ~$8,841 | 18.6× |
| Area coverage (km² per $1M at matched resolution) | 312,000 | 68,000 | 4.6× |
| Assets in service for $50M/year | 86 | 4.4 | 20× |
| Mission hours for $50M/year | 105,000 | 5,700 | 19× |

**Key Economic Insight**: For same annual budget, KONDOR keeps 19× more aircraft on station to deliver 4.6× more area. Aircraft loss costs ~1% of fielded capacity, improving fleet resilience to threats.

**Scaling Economics**: Multi-operator control at 10 coverage lines (~6 units) reduces cost per flight hour by ~14%.

**Acquisition Flexibility**: Open to GOCO (Government-Owned Contractor-Operated) and COCO/ISR-as-a-Service models.

## Manufacturing & Supply Chain

### Current & Planned Locations (SCF 2 baseline)
- **Final Assembly**: Slovenia (migrating to USA under "DoW" – likely Demonstration of Warfighting)
- **Structures/Props**: Czech Republic, Slovenia, UK, Italy, USA, Taiwan
- **Imaging/Optics**: Slovenia
- **Motors, ESCs, Battery/BMS, Flight Controller, Data Links, Ground Station**: USA
- **Active Components, GNSS**: TBD

### U.S. Industrialization Path
- **Texas Campus**: 130,000+ sq ft facility secured; U.S. build-out underway
- **In-House Capability**: Aerodynamics, CAD/CAM, composites, system integration
- **DFM/DFA Support**: Munro Defense partnership for manufacturability, assembly, and procurement optimization
- **Rapid Prototyping**: Additive manufacturing and composite capability for design iteration
- **COTS Integration**: Modified commercial engine/generator leverages established supply base vs. bespoke development
- **Scaling Partners**: Volume engine/generator modifications, camera, data links identified as key constraint areas for industrialization phase (1Q2027)

### NDAA Compliance & Supply Chain Security
- KrateoSky aligned with Drone Dominance Program (DDP) Supply Chain Framework
- Commitment to secure supply chain with documented component sourcing

## Environmental & Operational Robustness

### Environmental Tolerance
- **Operating Temperature**: −20°C to +55°C (target, informed by SQA2 IP65 design principles)
- **Wind Tolerance**: VTOL 20/25 km/h (threshold/objective); cruise 35/40 km/h
- **Aircraft Design Provisions**: Composite structures, fuel-resistant materials, thermal protection, accessible servicing
- **Sensor Compliance**: −40°C to +50°C / 30G shock / MIL-STD-810G

### Field Serviceability
- **Repeatable Checks**: C3P checklist, warning, telemetry foundation; KONDOR preflight/postflight procedures capture aircraft condition and corrective actions
- **Modular