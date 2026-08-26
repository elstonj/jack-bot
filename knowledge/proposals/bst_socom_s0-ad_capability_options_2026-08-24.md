# S0-AD Capability Development Options for USSOCOM

## Document Metadata
- **Type:** Technical Brief and Rough Order of Magnitude (ROM) Summary
- **Client/Agency:** USSOCOM (United States Special Operations Command)
- **Program/Solicitation:** USSOCOM-BST Cooperative Research and Development Agreement (CRADA)
- **Date:** 18 August 2026
- **BST Products/Systems Referenced:** S0-AD (air-deployed unmanned aircraft), SwiftCore (Flight Management System/autopilot), SwiftTab (operator interface), SwiftStation (ground radio and control unit), SwiftLink (display interface), multi-hole probe, PTH sonde
- **Key Personnel:** Jack Elston, Ph.D. (Founder & CEO, Black Swift Technologies); Daniel Prendergast (last editor); TSgt Evan Wolff (USSOCOM contact)

---

## Executive Summary
BST proposes three spiral development paths to enhance the S0-AD air-deployed unmanned aircraft for USSOCOM: mechanical integration with the Pneumatic Common Launch Tube (PCLT), objective-area weather reconnaissance (METAR capability), and EO/IR intelligence capabilities. All options build from a baseline S0-AD with proven autonomous flight, long-range command/data link, and operational pedigree in demanding environments (NOAA Hurricane Hunter deployments including a Guinness World Record wind measurement of 240 mph in Hurricane Milton, October 2024).

---

## Technical Approach

### Baseline S0-AD Platform Characteristics
- **Form Factor:** Tube-form-factor fixed-wing aircraft, approximately 3 lb, free-fall air-deployed
- **Autonomy:** Autonomous from release through mission completion; hand- and tube-launched variants share same avionics
- **Flight Management:** SwiftCore autopilot stack with SwiftTab rugged tablet operator interface and SwiftStation ground radio/control unit
- **Command & Data Link:** 430 MHz Microhard P400 narrowband at 2 W; tested to 400 km range (key constraint for imagery requirements); long-range, low-bandwidth architecture
- **Baseline Unit Price:** Approximately $18,000 in small quantities; currently non-reusable with typical light, repairable landing damage
- **Operational Pedigree:** Deployed in NOAA Hurricane Hunter P-3 missions; NCAR-verified record for highest wind speed measured by uncrewed aircraft (240 mph, Hurricane Milton, October 2024)

### Development Philosophy
- Spiral approach with each step independently useful and ending in real flight demonstration, not paper deliverables
- Single unified airframe, autopilot, and operator interface across all options (capabilities are stacked and cumulative)
- Emphasis on consumable price point (one to two orders of magnitude below comparable systems like ALTIUS family) enabling acceptance of risk into defended areas
- Rapid integration capability: small engineering team can integrate new payloads in weeks vs. program years

---

## Products & Capabilities Described

### Option 1: PCLT Launch Modification (ROM: $64,435)
- **What it is:** Mechanical design modification enabling S0-AD to be loaded and launched from SOCOM's Pneumatic Common Launch Tube
- **Technical approach:** Mechanical interface only—no electrical or data connection to tube. Design modification, test article fabrication, ground ejection testing with dummy round, live flight test
- **Scope coverage:** Structural design for tube compatibility, fabrication, ground testing, flight test with three round-trip travel for testing activities
- **Key assumption:** Aircraft powered on before tube loading; structural hardening for ejection loads not included (this is the single largest technical risk)
- **Assumptions to verify:** S0 survives pneumatic ejection intact; PCLT ejection profile (peak pressure, acceleration, pulse duration) needed from SOCOM
- **Estimated labor:** 162 hours
- **Recurring unit price:** $19,000 (unchanged from baseline)

**Recommended Follow-On (not priced):** Tube-resident readiness firmware to (a) optimize power consumption for extended in-tube storage without battery depletion, and (b) allow pre-loaded/stored mission profiles, collapsing ten-minute preflight sequence into short readiness check. Converts S0 from "something you set up" to "something you carry ready."

---

### Option 2a: METAR Core Capability (ROM: ~$152,690)
- **What it is:** Advanced weather reconnaissance of routes and objective areas supporting go/no-go decisions for rotary-wing landing zones, fixed-wing expeditionary runways, and drop zones
- **Mission context:** Operated by reconnaissance element within line-of-sight or operator standing off in host aircraft
- **Weather observation capability delivered:**
  - Pressure, temperature, humidity, dew point from BST's calibrated PTH sonde (existing, Hurricane Hunter-proven)
  - Wind direction and speed from BST's multi-hole probe (existing, Hurricane Hunter-proven)
  - Day/night-capable still-imaging payload, operator-commanded, for precipitation presence/type determination, gross obscuration along route and objective, and cloud level verification against safe minimums
  - Vertical profiles of measured parameters through aircraft descent
- **Sensors:** BST-designed atmospheric instrumentation (not adapted commercial camera ball)
- **Estimated labor:** 474 hours
- **Recurring unit price:** $23,000

**Unique capability:** Delivers METAR-equivalent information from no other fielded air-launched platform; provides actual observations (not forecasts) with ability to route and loiter over objective area unlike dropsondes.

---

### Option 2b: METAR Automated Sensing (ROM: ~$174,961)
- **What it is:** Bounded research, integration, and flight-validation task for METAR elements S0-AD does not measure today: precipitation type/intensity, lowest cloud layer and ceiling altitude, horizontal visibility
- **Objective:** Produce weather observation equivalent to METAR automatically and numerically with no human interpretation of imagery
- **Technical approach:** Three parallel trade studies evaluated through component selection, integration, and testing:
  - **Precipitation sensing:** Capacitive, resistive, and optical approaches for precipitation type and numerical intensity/rate/droplet-size measurement
  - **Cloud layer and ceiling:** Upward-looking approaches (computer vision cameras, single-point lidar, longwave infrared radiometry) for numerical lowest-layer and ceiling altitudes
  - **Horizontal visibility:** Forward-looking approaches (single-point lidar, longwave infrared radiometry)
- **Follow-on phase:** Design finalization, sensor integration, SwiftCore and SwiftControl stack modifications for automated data processing, METAR-equivalent actionable values on SwiftLink interface, flight-test demonstration with SOCOM personnel
- **Estimated labor:** 524 hours
- **Recurring unit price:** TBD

---

### Option 3a: EO/IR, Record and Recover (ROM: $116,048)
- **What it is:** Intelligence preparation of the battlefield via autonomous photogrammetric coverage with onboard recording, no real-time transmission
- **Mission profile:** Flies fully autonomous route with programmed photogrammetric coverage, records EO and IR imagery onboard without gaps, egresses to recovery point. Imagery downloaded and exploited after recovery
- **Transmission option:** Can execute with datalink fully suppressed, transmitting only aircraft telemetry and payload status if permitted
- **Sensor specification:**
  - EO: 12 MP
  - IR: 640 × 512 baseline threshold; 1280 × 1024 objective (reflects uncooled longwave infrared core realities; cooled mid-wave sensors not appropriate for consumable aircraft)
- **Optics:** Sized to SOCOM detection/recognition range requirement if specified
- **Why recommended as entry point for EO/IR:** Lowest cost, lowest risk, requires no new radio, all components directly reused in Option 3b
- **Estimated labor:** 334 hours
- **Recurring unit price:** $21,000

---

### Option 3b: EO/IR, Real-Time ATR (ROM: $221,262)
- **What it is:** Human-monitored, machine-assisted ISR for pre-operation confirmation with mid-mission retasking capability
- **Mission profile:** Third-party automatic target recognition algorithm runs onboard; transmits compact target data packets and occasional low-resolution target chips rather than video
- **Technical components:** Trade study between camera + separate single-board computer vs. camera with integrated AI processing; operator interface for detected targets, metadata, and imagery
- **Sensor specification:** Same as Option 3a (12 MP EO, 640 × 512 baseline / 1280 × 1024 objective IR)
- **Transmission rates:** Imagery cadence estimated no more frequently than every 60 seconds per identified target (bandwidth-limited on narrowband link at 50 nm); target data packets remain at 5-second intervals
- **Key assumption:** ATR algorithm provided by SOCOM as GFE (government-furnished equipment) to remove license cost and integration uncertainty; export classification of ATR software and imaging payload to be confirmed during component selection
- **Estimated labor:** 634 hours
- **Recurring unit price:** $29,000

---

### Option 3c: EO/IR, Full Motion Video ISR (ROM: $219,597)
- **What it is:** Persistent real-time observation for human-in-the-loop tasks: target custody maintenance or observation for indirect/aviation fires
- **Payload:** Gimbaled EO/IR camera (NextVision DragonEye class) with manual slew, object tracking, geolocation stare modes; streams 1080p30 EO and 640 × 480 IR; no-comm transit mode to reach operator/objective
- **Datalink:** Requires broadband link upgrade (Microhard pMDDL2280 pre-selected for equivalent requirements on parallel BST program)
- **Critical range constraint:** Aircraft can transit 50 nm but FMV only available to operator within ~15 nm (full motion video range ≠ aircraft range)
- **Economic constraint:** Gimbal comprises ~45% of recurring unit price ($38,000 total) on non-recoverable airframe; expending entire aircraft for video sortie materially different from $21,000 consume
- **Recommendation:** Pair with airframe recoverability effort (Section 8) or recovery-focused CONOPS to avoid consuming most expensive payload on every sortie
- **Estimated labor:** 639 hours
- **Recurring unit price:** $38,000

---

## Use Cases & Applications

### Weather Reconnaissance Applications (Options 2a, 2b)
- Pre-assault weather observation for rotary-wing landing zone decisions
- Fixed-wing expeditionary runway suitability determination
- Drop zone weather assessment (pressure, temperature, humidity, wind for precision operations)
- Route weather reconnaissance in hours before direct action, covert logistics, hostage rescue, advanced force operations
- Provides METAR-equivalent data unavailable from other air-launched platforms; actual observations rather than forecasts

### ISR Applications (Options 3a, 3b, 3c)
- **Option 3a:** Intelligence preparation of the battlefield in weeks/days/hours before operation; photogrammetric coverage with post-recovery exploitation
- **Option 3b:** Pre-operation intelligence confirmation; human-monitored target detection with mid-mission retasking on new findings
- **Option 3c:** Persistent target observation; maintaining target custody; observation support for indirect and aviation fires

### Launch Profile Applications (Option 1)
- Enables air deployment from Pneumatic Common Launch Tube (addresses SOCOM RFI for air-launched loitering munitions and sources-sought notice for Group 1/2 UAS from CLT)
- Deployment from C-130, AC-130J, P-3, UH-60, and ground/maritime launchers (reference systems capability)
- Enables on-sortie launch integration alongside other payloads

---

## Key Results from Current CRADA Demonstration

### Demonstrated Capabilities (as of 18 August 2026)
- **Successful Free-Fall Deployment:** 17 August free-fall deployment from 12,000 ft MSL executed successfully by SOCOM operators after one day of training
- **Operator Training:** Effective operator training achieved in single day of instruction
- **Follow-on Deployment:** Second deployment scheduled at altitude to be confirmed
- **Operational Status:** S0-AD is "flying now, under the CRADA, with SOCOM personnel in the loop"
- **Autonomous Capability:** Autonomous from release through mission completion with working autopilot, operator interface, and command-and-data-link demonstrated on SOF range

### Historical Operational Pedigree
- NOAA Hurricane Hunter deployments from P-3 aircraft
- NCAR-verified Guinness World Record: