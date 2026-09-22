# S0-AD Capability Development Options for USSOCOM

## Document Metadata
- **Type:** Executive summary of technical brief & ROM (rough order of magnitude estimate)
- **Client/Agency:** United States Special Operations Command (USSOCOM)
- **Program/Solicitation:** CRADA (Cooperative Research and Development Agreement)
- **Date:** Prepared 18 Aug 2026; document created 3 Sep 2026
- **BST Products/Systems Referenced:** S0-AD (S0 air-deployed), SwiftCore autopilot, SwiftTab/SwiftStation ground system, Microhard 430 MHz radio link
- **Key Personnel:** Daniel Prendergast (last editor)

## Executive Summary
Black Swift Technologies responded to USSOCOM's request for ROM estimates on three capability areas for the S0-AD unmanned aircraft: (1) launch from the Pneumatic Common Launch Tube (PCLT), (2) objective-area weather reconnaissance (METAR-equivalent), and (3) EO/IR observation. BST proposes a spiral development approach with independently useful operational milestones, leveraging proven air-deployment technology from NOAA hurricane operations at consumable-class pricing ($19K–$38K per unit).

## Technical Approach

### Baseline S0-AD Platform
- Fixed-wing, tube-form, ~3 lb autonomous aircraft
- SwiftCore autopilot with autonomous operation from release
- Ground control via SwiftTab/SwiftStation
- 430 MHz Microhard radio link (narrowband, tested to 400 km—identified as key constraint on imagery options)
- Free-fall deployment capability demonstrated from 12,000 ft and 20,000 ft MSL
- Consumable/expendable design (not currently reusable)

### Proposed Spiral Development Approach
**Spiral 1 (Foundational):** PCLT launch modification
- Mechanical adaptation for ejection from Pneumatic Common Launch Tube
- Single largest technical risk identified: need PCLT ejection profile data (peak pressure, acceleration, pulse duration) from SOCOM
- ROM: $64,435 development; $19,000 unit price

**Spiral 2 (Weather Reconnaissance):**
- **Option 2A – METAR Weather Capability (low risk, near-term):** Fixed camera + existing calibrated pressure-temperature-humidity (PTH) and wind probe sensors; human estimation for precipitation/cloud-cover/visibility; ROM: $152,690 dev / $23,000 unit
- **Option 2B – Automated Weather Measurement (bounded research):** Adds upward- and forward-looking Lidar + capacitive precipitation sensor for quantitative automated sensing; ROM: ~$174,961 dev / TBD unit price

**Spiral 3 (EO/IR):**
- **Option 3a – EO/IR Record & Recover (lowest cost/risk stepping stone):** ROM: $116,048 dev / $21,000 unit
- **Option 3b – EO/IR Real-time ATR (Automatic Target Recognition):** BST integrates third-party/Government-Furnished Equipment (GFE) ATR rather than developing; ROM: $221,262 dev / $29,000 unit
- **Option 3c – Full Motion Video (FMV):** Uncooled LWIR camera (640×512 threshold / 1280×1024 objective); real-time imagery cadence ~60 seconds per target on narrowband link; limited to ~15 nm range; gimbal ~45% of cost; ROM: $219,597 dev / $38,000 unit

**Key Technical Constraint:** Narrowband 430 MHz radio link caps real-time imagery cadence and FMV range (~15 nm). FMV option requires broadband radio.

## Products & Capabilities Described

### S0-AD (S0 Air-Deployed)
- **What it is:** Consumable-class fixed-wing unmanned aircraft (~3 lb, tube-form), air-deployed via free-fall or PCLT launch
- **Proven heritage:** NOAA Hurricane Hunter P-3 deployments; holds NCAR-verified Guinness record for highest wind measured by UAS (240 mph, Hurricane Milton, October 2024)
- **Autonomy:** Fully autonomous from release via SwiftCore autopilot
- **Ground control:** SwiftTab/SwiftStation system with 430 MHz Microhard narrowband link
- **Deployment methods:** Free-fall from altitude (12,000–20,000 ft demonstrated); PCLT launch (under development)
- **Training requirement:** One day of operator training sufficient for SOCOM personnel
- **Current pricing:** $18K baseline; $19K–$38K depending on configuration

### SwiftCore Autopilot
- Embedded autopilot system enabling autonomous flight from release/launch
- One airframe, autopilot, and interface maintained across all spiral options

### SwiftTab/SwiftStation Ground System
- Ground control and telemetry system
- Operates on 430 MHz Microhard link

## Use Cases & Applications

1. **Objective-Area Weather Reconnaissance:** METAR-equivalent meteorological observations (pressure, temperature, humidity, wind, cloud cover, visibility, precipitation) for SOCOM operational planning; rapid weather assessment in denied/contested areas
2. **Low-Signature EO/IR Observation:** Tactical imagery collection on objective without high-signature platforms; record-and-recover, real-time ATR, or full-motion video options
3. **Hurricane/Severe Weather Sampling:** Demonstrated capability through NOAA/NCAR partnerships; extreme-wind measurement
4. **High-Threat Area Operations:** Consumable pricing ($19K–$38K) acceptable for high-threat deployments where loss is acceptable; air-launch capability maintains stand-off distance

## Notable Details

### Demonstrated Capability & Recent Testing
- Successful free-fall deployments from 12,000 ft (17 Aug 2026) and 20,000 ft (18 Aug 2026) executed by SOCOM operators after one day of training
- Same S0 airframe reused for second deployment on 18 Aug, indicating durability
- All testing conducted under active CRADA with USSOCOM

### Market Positioning & Competitive Advantage
- Fills gap between exquisite air-launched-effects class (e.g., ALTIUS, 20–27 lb, $20–27K) and other platforms
- Unique combination: METAR-equivalent weather observation + low-signature EO/IR + consumable pricing
- Price point commanders will accept risking in high-threat areas (vs. expensive reusable platforms)
- Proven hurricane/extreme-weather pedigree

### Technical Constraints & Trade-offs
- **Narrowband link limitation:** 430 MHz Microhard link is key constraint on all imagery options; ~400 km range but limits real-time video cadence to ~60 s per target; FMV limited to ~15 nm
- **EO/IR sensor:** Uncooled LWIR (unspecified manufacturer/model), 640×512 threshold / 1280×1024 objective
- **ATR approach:** BST integrates third-party/GFE ATR rather than developing in-house
- **Gimbal cost:** Gimbal represents ~45% of FMV configuration cost

### SOCOM Support Requirements
- **Critical:** PCLT ejection profile data (peak pressure, acceleration, pulse duration)
- **Desired:** Physical PCLT tube for ground testing in Boulder, Colorado
- **Recommended follow-on:** Tube-resident readiness firmware (pre-loaded mission, powered standby) to reduce operational setup time

### Risk Stratification
- **Lowest risk:** Option 1 (PCLT—mechanical only), Option 2A (METAR—existing sensors), Option 3a (record & recover EO/IR)
- **Medium risk:** Option 2B (automated weather measurement—bounded research task)
- **Higher complexity:** Option 3b/3c (real-time imagery, ATR integration, FMV with broadband)

### Pricing & Development
- All ROMs assume Options 2A–3c include completion of Option 1 (PCLT); foundational cost not re-priced
- Unit prices reflect small-quantity estimates; scale with volume
- ROM figures are non-binding; firm proposal follows SOCOM direction on scope