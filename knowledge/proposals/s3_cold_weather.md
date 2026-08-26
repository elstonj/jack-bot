# S3 Cold Weather

## Document Metadata
- **Type:** White Paper / Proposal
- **Client/Agency:** U.S. Special Operations Command (USSOCOM) / U.S. Air Force
- **Program/Solicitation:** USSOCOM FY27 Experimentation Calling Message (PAYCOM)
- **Date:** 2026-08-07 to 2026-08-08 (created/modified)
- **BST Products/Systems Referenced:** S3 VTOL UAS, S2 (predecessor), SwiftCore Flight Management System, REX110 EO/IR Gimbal
- **Key Personnel:** Dr. Jack Elston (Primary Author), Daniel Prendergast (Last Editor)

## Executive Summary
Black Swift Technologies proposes to qualify and field-validate the S3 VTOL fixed-wing UAS as an all-weather ISR platform optimized for severe cold, heavy precipitation, and high-wind environments. The effort targets operational capability down to –40 °C (with roadmap to –55 °C) and sustained winds exceeding 30 knots (up to 45 knots), closing critical coverage gaps in arctic and sub-zero environments where traditional small UAS fail.

## Technical Approach
**Core Strategy:** Intensive engineering sprint and field demonstration leveraging the proven S2 heritage (100+ flights in Greenland at –20 °C, rated to –40 °C) to transition the S3 VTOL platform into a cold-weather-qualified ISR asset. Environmental chamber qualification to –40 °C is being completed under ongoing Canadian Joint Forces Command (CJFC) Arctic UAS Phase II effort in advance of demonstration.

**Key Engineering Modifications:**
- Airframe construction using low-thermal-expansion carbon-fiber composites and polyamide materials with specialized cold-weather laminating resins
- IP54 ingress sealing protection against blowing snow, ice melt, and moisture during freeze-thaw cycles
- Re-engineered mechanical latches, wing connections, and battery retention for tool-less operation with thick arctic mittens
- Heated, vehicle-powered transit and staging cases to pre-condition batteries before launch
- Integration of cold-weather EO/IR gimbal with encrypted data link

## Products & Capabilities Described

### S3 VTOL Fixed-Wing UAS
**What it is:** All-electric, NDAA-compliant transitional VTOL fixed-wing UAS; evolved from the S2 platform with added multirotor hover capability eliminating runway dependencies.

**Cold-Weather Configuration for this Context:**
- **Endurance:** 120+ minutes
- **Mission Range:** 160 km
- **Dash Speed:** >100 mph (45 m/s)
- **Ceiling:** 15,000 ft AGL
- **Operational Temperature Range (Target):** –40 °C field-validated (roadmap to –55 °C)
- **Wind Capability:** Launch/land in up to 45 knots; sustained flight in 30–45 knot winds
- **Deployment:** Packs into two ruggedized hard cases; assembled by two-person crew in <5 minutes; zero specialized launch equipment required
- **Ingress Protection:** IP54 (upgraded from IP42/43 baseline)

### REX110 EO/IR Gimbal
**What it is:** Field-swappable modular payload with dual-spectrum optics for 24/7 surveillance.

**Specifications:**
- High-definition optical daylight sensor with optical zoom
- High-sensitivity Long-Wave Infrared (LWIR) thermal core
- Multi-axis active gyro-stabilization for smooth Full-Motion Video (FMV)
- Targeting modes: Object Tracking, Geolocation Stare, Manual Point-of-Interest Slew

### SwiftCore Flight Management System (FMS)
**What it is:** Onboard flight control paired with Linux Single-Board Computer (SBC) for edge-AI acceleration.

**Capabilities Being Developed:**
- Automated Threat Detection: Deep learning vision models process live REX110 video for real-time detection, classification, and tracking (personnel, vehicles, perimeter intrusions)
- Cursor-on-Target (CoT) Native Output: Converts target geocoordinates, slant range, and telemetry into CoT data packages
- ATAK/WinTAK Interoperability: Broadcasts target tracks and sensor metadata over encrypted datalinks to tactical handhelds and command posts, integrating with common operational maps

## Use Cases & Applications

**Primary Mission Sets:**
1. **Arctic Base Security:** Perimeter surveillance and rapid threat response for northern military installations (Grand Forks AFB, JBER)
2. **Persistent 24/7/365 Reconnaissance:** Fills coverage gaps in severe weather where Group 1/2 UAS are grounded
3. **Northern Allied Operations:** Supports Canadian Forces and allied arctic security operations

**Operational Environments:**
- Sub-zero arctic regions (–40 °F / –40 °C ambient)
- High surface winds and blowing snow
- Freeze-thaw cycles with moisture ingress risk
- Low-light and thermal-contrast terrain detection

## Sponsorship & Partnerships

**Institutional Support:**
- **Grand Forks AFB (North Spark Defense Laboratory, ND):** MOU and proposal package established to address severe winter security vulnerabilities; installation experiences –40 °F with high winds and blowing snow
- **Joint Base Elmendorf-Richardson (JBER / Arctic Spark, Alaska):** Partnership with Air Force Security Forces; critical operational need for Group 2 VTOL platform for arctic winter perimeter surveillance
- **Canadian Joint Forces Command (CJFC):** BST selected for Arctic UAS Phase II Engineering Sprint; tasked with transitioning S3 to arctic-qualified baseline; funding environmental chamber qualification, heated staging cases, IP54 sealing, and REX110 integration
- **NexTech Solutions:** Coordination partner on CJFC effort
- **Canadian Rangers:** Ongoing winter Arctic mission collaboration planned

## Notable Details

**Heritage & Proven Performance:**
- S2 platform has completed 100+ flights in Greenland at temperatures down to –20 °C with rating to –40 °C, providing direct engineering foundation for S3 cold-weather variant
- VTOL capability identified as rapidly becoming standard for Group 2 fixed-wing UAS; S3 upgrade addresses this market and operational trend

**Demonstration Strategy:**
- Environmental chamber qualification to –40 °C will be completed before demonstration event
- Demonstration site ambient conditions expected to be warmer than –40 °C, so event focuses on operator-facing evaluation (handling, staging, workflow) rather than full thermal envelope testing
- Combined target capabilities to be validated through demonstration events, internal flight tests, and ongoing Canadian Rangers winter missions

**Operational Logistics Advantages:**
- Two-person crew deployment with <5-minute assembly
- Commercial air or light tactical vehicle transportable
- Tool-less operation designed for thick-gloved arctic personnel
- Zero specialized launch rails or ground support equipment

**Competitive Positioning:**
- Addresses critical market gap: traditional small UAS suffer severe performance degradation or total failure below freezing due to battery chemistry, actuator freezing, structural brittleness, lens icing, and operator dexterity loss
- Qualified Group 2 VTOL platform specifically designed for severe weather reduces grounding risk for northern operations