# Nanoveu EMASS ECS-DoT White Paper

## Document Metadata
- Type: ASX Release / White Paper
- Client/Agency: ASX (Australian Securities Exchange) / Public announcement
- Program/Solicitation: Not applicable (commercial technology validation announcement)
- Date: 2 September 2025
- Products Referenced: ECS-DoT (ultra-low-power AI chip), EyeFly3D™, Nanoshield™
- Key Personnel: Dr. Mohamed M. Sabry Aly (Founder and CTO of EMASS), Mark Goranson (CEO of Nanoveu's Semiconductor Division), Alfred Chong (Nanoveu MD and CEO)

## Executive Summary
Nanoveu's subsidiary EMASS has achieved significant results in drone energy efficiency through its ECS-DoT ultra-low-power AI chip, demonstrating 60% average extended flight times (up to 85% in some cases) across 300+ simulated drone trials without hardware modifications. The chip operates real-time AI control at sub-1mW power consumption, positioning EMASS for market entry into the projected USD$163-165 billion global drone market by 2030.

## Technical Approach

**ECS-DoT Architecture & Operation:**
- Ultra-low-power AI chip consuming <1 milliwatt during operation
- Real-time closed-loop control cycles at 50 Hz (20ms cycle time)
- Sub-milliwatt AI engine for deterministic flight control without cloud reliance
- Proprietary surrogate power models trained on real propulsion and telemetry data to dynamically predict and optimize energy usage per flight condition

**Testing Methodology:**
- Hardware-in-the-loop (HIL) and software-in-the-loop (SIL) simulation on Gazebo with ArduPilot
- 300+ unique campaigns executed, each with 100+ distinct flight paths
- Real-time sensor integration: receives data from IMUs, airspeed/altitude sensors, powertrain monitors (voltage, current, motor command signals)
- Generates motor control outputs at 50 Hz maintaining deterministic cycles
- Stress tested under varied payloads, wind profiles, and flight geometries

**AI Control Stack:**
- Energy-efficient AI flight control without modifying batteries, rotors, or propulsion systems
- Embedded flight control stack with chip-level architecture
- AI-powered energy modelling framework

## Products & Capabilities Described

### ECS-DoT (Edge AI Chip)
- **What it is:** An ultra-low-power AI systems-on-chip (SoC) for edge computing and real-time autonomous control
- **How used:** Embedded directly in drone control loops to optimize flight endurance through intelligent energy management
- **Key specifications:**
  - Power consumption: <1 mW during operation
  - Control cycle rate: 50 Hz (20 ms)
  - Operates without cloud reliance or latency
  - Compatible with industry-standard autopilot stacks (ArduPilot)

## Use Cases & Applications

**Drone Market Segments:**
1. **Autonomous Delivery Drones** - Estimated USD$10.5B market by 2030
   - Extended range and efficiency improve delivery logistics economics
2. **Agricultural Drones (Precision Farming)** - Estimated USD$22.5B market by 2030
   - Payload-constrained drones gain endurance for surveying, spraying, and monitoring large farmlands
3. **Military/ISR Drones** - Estimated USD$88.0B market by 2030
   - Autonomous flight with limited battery capacity, edge-based autonomy without cloud reliance
4. **Consumer Drones** - Estimated USD$11.6B market by 2030
5. **Infrastructure Inspection & Surveillance**
   - Enables continuous, anomaly-powered monitoring with extended airborne duration for greater coverage and cost-effectiveness

**Drone Platforms Validated:**
- Quadcopters (4 rotors): Common in consumer and enterprise markets
- Hexacopters (6 rotors): Used in agriculture, logistics, terrain mapping
- Octocopters (8 rotors): Heavy-lift industrial inspection, defense, professional cinematography

## Key Results (Phase 2 Evaluation)

**Performance Improvements in Flight Endurance:**
- **Quadcopters:** Up to 80% improvement in mission endurance; 60% average extended flight time
- **Hexacopters:** Up to 75% improvement under payload-intensive stress testing
- **Octocopters:** Up to 85% improvement; 57% average improvements despite high mass and complexity

**Test Scale & Methodology:**
- 300+ total simulation scenarios across varied payloads, wind profiles, and mission conditions
- Each campaign included 100+ unique flight paths
- Flight profiles simulated: waypoint navigation, loiter, climb/descent under wind
- Evaluation metrics: energy consumed (Joules), distance per Joule, mission endurance (minutes)

**Power Efficiency:**
- Achieved real-time AI control at <1 mW power consumption
- Results obtained without changing batteries, rotors, or propulsion systems
- Extended missions translate to greater range, improved efficiency, and higher utility per battery cycle

**Validation Environment:**
- Built on Gazebo with ArduPilot (same environment used by NASA and DARPA)
- High-fidelity aerodynamic dynamics, sensor noise modelling, and atmospheric disturbance profiles
- Hardware-in-the-loop with live telemetry integration (IMUs, airspeed, altitude, powertrain monitors)

## Phase 1 Foundations (Prior Work)
- Initial integration into software-in-the-loop (SITL) and HIL simulations
- Recorded up to 33% endurance increases in early testing
- Proved ECS-DoT compatibility with industry-standard autopilot stacks
- Demonstrated stability across altitude shifts, wind bursts, and mission irregularities
- Introduced surrogate power model trained on empirical propulsion data

## Notable Details

**Commercial Positioning:**
- EMASS advancing to engage global drone OEMs and avionics manufacturers for next-generation flight platform integration
- Global drone market projected to grow to USD$163-165 billion by 2030
- Single ECS-DoT can manage core flight control with potential for multiple chips per unit for expanded functions (navigation, stability enhancement, system resilience)

**IP Protection:**
- Patent filings in progress for:
  - AI-powered energy modelling framework
  - Embedded flight control stack
  - Chip-level architecture
- Foundation for global licensing and strategic defensibility

**Next Steps:**
1. Direct engagement with OEMs and avionics manufacturers for design-ins
2. Live flight mapping and physical trials to validate performance in uncontrolled environments
3. Transition to Phase 3 with real drone integration and field trials

**Corporate Structure:**
- Nanoveu Limited (ASX: NVU, OTCQB: NNVUF) is parent company
- EMASS (Embedded A.I. Systems Pte Ltd) is wholly owned subsidiary specializing in ultra-low-power AI SoC solutions

**Broader Nanoveu Portfolio:**
- **EyeFly3D™:** Glasses-free 3D platform combining screen technology, software, and EMASS low-power SoC
- **Nanoshield™:** Self-disinfecting film with antimicrobial nanoparticles (includes marine and solar variants)

**Acknowledged Limitations:**
- EMASS acknowledges minor discrepancies are inevitable when transferring from Gazebo simulation to physical systems
- Phase 3 will validate sensor-control loops in operational UAV platforms