# S0-AD Capability Development Options for USSOCOM

## Document Metadata
- Type: Executive Summary of Technical Brief & ROM (Rough Order of Magnitude)
- Client/Agency: USSOCOM (U.S. Special Operations Command)
- Program/Solicitation: CRADA (Cooperative Research and Development Agreement) with USSOCOM
- Date: Prepared 18 Aug 2026; Document created/modified 4 Sep 2026
- BST Products/Systems Referenced: S0-AD (air-deployed unmanned aircraft), SwiftCore autopilot, SwiftTab/SwiftStation ground system
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
Black Swift Technologies proposes ROM estimates for three capability development options for the S0-AD air-deployed unmanned aircraft system to address USSOCOM operational gaps: (1) launch modification for the Pneumatic Common Launch Tube (PCLT), (2) objective-area weather reconnaissance (METAR) configurations, and (3) EO/IR observation configurations. BST offers a proven, consumable-priced fixed-wing aircraft ($19K–$38K unit cost) that fills gaps in low-cost, high-risk-tolerant capabilities for tactical operations.

## Technical Approach

**Baseline S0-AD System:**
- ~3 lb tube-form fixed-wing aircraft, autonomous from release
- SwiftCore autopilot with SwiftTab/SwiftStation ground control system
- 430 MHz Microhard narrowband link tested to 400 km range
- Autonomous operation after deployment; operators require minimal training (one day demonstrated)
- Non-reusable consumable platform

**Spiral Development Approach:**
- Spiral 1: PCLT launch modification (foundational)
- Spiral 2: Objective-area weather capability (METAR-equivalent, then automated sensing)
- Spiral 3: EO/IR options (record & recover, real-time ATR, full motion video)
- One airframe, autopilot, and operator interface across all spirals

## Products & Capabilities Described

### S0-AD (S0 Air-Deployed)
- **What it is:** 3 lb fixed-wing unmanned aircraft system, tube-form factor for air deployment
- **Heritage:** Proven through NOAA Hurricane Hunter P-3 deployments; verified 240 mph wind measurement in Hurricane Milton (Oct 2024) — Guinness record for UAS
- **Baseline unit cost:** ~$18K (non-reusable)
- **Use in context:** Deployed from SOCOM aircraft via free-fall or PCLT; autonomous operation in objective area with narrowband command/control and data return
- **Recent validation:** Successful free-fall deployments from 12,000 ft and 20,000 ft MSL (17–18 Aug 2026), flown by SOCOM operators with one day training; aircraft reused across multiple deployments

### SwiftCore Autopilot
- Integrated autopilot enabling autonomous flight from release
- Supports all proposed configurations without redesign

### SwiftTab/SwiftStation Ground System
- Command and control system compatible with 430 MHz Microhard narrowband link
- Operator interface for mission planning and data reception

## Use Cases & Applications

**Primary Context:** Special Operations tactical missions in high-threat environments where commander risk tolerance is low and cost-effectiveness is critical.

**Specific Capability Gaps Addressed:**

1. **Weather Reconnaissance (METAR-Equivalent):**
   - Objective-area meteorological observation (pressure, temperature, humidity, wind, cloud cover, visibility, precipitation)
   - Option 2A (low risk): Uses existing calibrated sensors + fixed camera; human operator estimation for precipitation/cloud/visibility
   - Option 2B (bounded research): Automated sensing via upward/forward-looking Lidar and capacitive precipitation sensor
   - Fills gap where exquisite air-launched effects platforms (e.g., ALTIUS, 20–27 lb class) do not operate

2. **EO/IR Reconnaissance:**
   - Low-signature observation platform at consumable price point
   - Option 3a (Record & Recover): Lowest cost/risk; uncooled LWIR (640×512 threshold / 1280×1024 objective)
   - Option 3b (Real-time ATR): ~60-second imagery cadence per target on narrowband link; BST integrates third-party/GFE ATR
   - Option 3c (Full Motion Video): ~15 nm range limit on narrowband; gimbal ~45% of unit cost; requires broadband radio
   - Competitive advantage: Consumable platform tolerable for commanders to risk in high-threat areas vs. exquisite systems

## ROM Summary (Non-Binding Development & Unit Costs)

| Option | Development Cost | Unit Price | Risk/Notes |
|--------|------------------|-----------|-----------|
| 1. PCLT Launch Modification | $64,435 | $19,000 | Foundational; mechanical only |
| 2A. METAR Weather Capability | $152,690 | $23,000 | Low risk — existing sensors + fixed camera |
| 2B. Automated Weather Measurement | ~$174,961 | TBD | Bounded research task |
| 3a. EO/IR — Record & Recover | $116,048 | $21,000 | Lowest EO/IR cost & risk |
| 3b. EO/IR — Real-time ATR | $221,262 | $29,000 | BST integrates, does not develop ATR |
| 3c. EO/IR — Full Motion Video | $219,597 | $38,000 | Video ≤15 nm; gimbal ~45% of price |

**ROM Notes:**
- ROMs are non-binding, non-recurring development cost including one SOCOM test event
- Unit prices are small-quantity estimates; scale with volume
- Options 2A–3c assume Option 1 (PCLT) is complete and do not re-price it

## Key Technical Constraints & Realism Factors

**Narrowband Link Limitation (430 MHz Microhard):**
- 400 km range but severely constrains imagery options
- Real-time imagery cadence capped at ~60 seconds per target
- FMV requires broadband radio; limits range to ~15 nm

**EO/IR Specifications:**
- Uncooled LWIR sensors: 640×512 threshold / 1280×1024 objective
- FMV full-motion video limited to ~15 nm on narrowband

**PCLT Integration Risk:**
- Ejection profile (peak pressure, acceleration, pulse duration) is largest technical risk
- BST requires SOCOM to provide PCLT ejection profile specification and ideally a tube for ground testing in Boulder

**Follow-On Capability:**
- Tube-resident readiness firmware (pre-loaded mission, powered standby) recommended to transition S0 from "set up" to "carry ready" configuration

## Notable Details

**Proven Pedigree:**
- Real-world validation through NOAA Hurricane Hunter operations
- Guinness-verified record: 240 mph wind measurement by UAS (Hurricane Milton, Oct 2024)
- Demonstrates survivability and sensor capability in extreme conditions

**Competitive Positioning:**
- Fills tactical gap between expensive exquisite air-launched effects (ALTIUS class, $20–27 lb) and no low-cost consumable option
- Addressable gaps: METAR-equivalent weather reconnaissance and low-signature EO/IR observation
- Unit cost ($19K–$38K) positions platform as acceptable risk for high-threat operational use

**CRADA Status & Current Demonstrations:**
- Live ongoing under CRADA agreement
- 17–18 Aug 2026: Successful free-fall deployments at 12K and 20K ft MSL by SOCOM operators after minimal training
- Aircraft reused across multiple flights, demonstrating durability

**Integration Approach:**
- One airframe and autopilot across all capability options
- BST integrates third-party/government-furnished ATR for Option 3b; does not develop ATR in-house
- Maintains operator interface consistency across spirals

**Document Classification:** Marked "PROPRIETARY — GOVERNMENT PLANNING USE ONLY"