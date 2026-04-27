# BST_ECS-DoT_Investor_Briefing

## Document Metadata
- Type: Investor briefing / interim project report (presentation)
- Client/Agency: EMASS / Nanoveu (partnership); presented internally/to investors
- Program/Solicitation: Project ECS-DoT (Edge-AI Flight Control, Validated in the Sky)
- Date: 24 April 2026 (first flight date; briefing created/modified 27 April 2026)
- BST Products/Systems Referenced: E2 multirotor, SwiftPilot autopilot, SwiftCore FMS
- Key Personnel: Jack Elston (last editor)

## Executive Summary
On 24 April 2026, Black Swift Technologies and EMASS achieved the first live in-flight handover of full motor control authority from the SwiftPilot autopilot to the ECS-DoT edge-AI reinforcement-learning chip on a Black Swift E2 multirotor. The integration successfully demonstrated a sub-milliwatt AI inference accelerator that promises 10–20% flight-time gains while maintaining full safety guarantees through SwiftPilot envelope protection. All BST-side milestones were met, including power baselining, command-path validation, and automated safety recovery.

## Technical Approach

**Integration Architecture:**
- Two-port handshake between SwiftPilot autopilot and ECS-DoT learned controller
- Payload port: 75 Hz PWM uplink; 10 Hz position, 20 Hz orientation/control telemetry downlink
- GCS port: operator authority gate with CMD_PAYLOAD_CONTROL (READY/OFF) commands
- Five-state machine (DISCONNECTED → CONNECTED → READY → ACTIVE → SHUTDOWN)
- Envelope protection evaluated 250×/sec with hard limits: roll/pitch ±20°, vertical velocity −1.5 to +3.0 m/s, yaw rate 0.52 rad/s
- Safety-net response time: <1 second

**Hardware Stack:**
- ECS-DoT: sub-milliwatt PPO (Proximal Policy Optimisation) inference accelerator
- Host: Pi Pico 2 running BST protocol firmware (auto-boot)
- UART 460k level-shifted between 3.3 V and 5 V logic
- Motor ESC PWM applied at measured 143 Hz
- 3D-printed enclosure mounted on airframe

**Autopilot Core (SwiftPilot):**
- STM32F4 processor
- 250 Hz state estimation
- Version 3.0.28
- Full SDK and bench-test harness (SWIL soak validation, headless test suite)

## Products & Capabilities Described

### Black Swift E2 Multirotor
- **Specification:** 11.45 kg integrated weight, 6S Li-ion battery, 907 Wh capacity
- **Use in project:** Evaluation airframe for ECS-DoT integration
- **Heritage:** 2025 Small UAS of the Year (Commercial category, Innovation Vanguard Awards, XPONENTIAL)

### SwiftPilot Autopilot
- **What it is:** Deterministic flight control system with envelope protection logic and two-port payload protocol
- **Use in ECS-DoT:** Safety net and command authority arbitration; remains in control of airframe envelope at all times; forcibly recovers if AI controller diverges
- **Key feature:** Sub-1-second recovery from attitude divergence; zero hardware incidents in test

### SwiftCore FMS
- **What it is:** Payload-focused flight management system enabling real-time telemetry and control through autopilot data link
- **Relevance:** Modular field-swappable payload architecture that enabled ECS-DoT integration

### ECS-DoT Inference Accelerator (Nanoveu/EMASS)
- **What it is:** Sub-milliwatt edge-AI silicon running Proximal Policy Optimisation (PPO) policy
- **Performance claim:** <1 mW power consumption (orders of magnitude below GPU alternatives)
- **Training & retraining pipeline:** Gazebo + pymavlink + MAVProxy stack
- **Policy training:** Against simulated UAV dynamics; to be retrained against realized E20006 airframe dynamics post-Flight Day 1

## Use Cases & Applications

**Primary Mission:**
- Surrogate training mission: 8-phase, ~5,200 m, ~22 min pattern (Part-107 compliant)
- Head-to-head endurance comparison: identical 100 m square flown to 20% SOC by each controller

**End Applications (roadmap):**
- Inspection
- Agriculture
- Defence

**Flight Validation Context:**
- Test range: Boulder, Colorado
- Flight geometry: 35 m × 35 m square at 3.5 m/s cruise (baseline); 100 m square (efficiency test)

## Key Results

### Flight Day 1 (24 April 2026, Log E20006)

**Objective 01 – Power Baseline:**
- Mean rotor power: **1199 W** (stable ±30 W across 17 independent legs)
- Sortie duration: 167 s
- Total energy: 55.8 Wh
- Energy per lap: 12.5 Wh
- Battery SOC swing: 6.1 percentage points
- **Result:** Repeatable baseline established; any AI-flown sortie >1250 W mean exceeds the autopilot reference

**Objective 02 – Command Path:**
- Actuator apply rate: **143 Hz** (measured in-flight)
- ICD floor for actuator stream: 75+ Hz (exceeded)
- Telemetry streams: 100% at or above spec
- READY command acceptance: 2 of 2 successful
- **Result:** Full end-to-end control path validated from PPO inference to motor PWM

**Objective 03 – Safety Net:**
- Hardware incidents: **0**
- Attitude divergence events: 2 (both triggering envelope protection)
  - Attempt 1 (T+752.6 s): Roll spike to 45° within 1 s; recovery 0.95 s; altitude loss <1 m
  - Attempt 2 (T+777.5 s): Roll 73°, pitch 43°, yaw 90°; recovery 3.5 s; autopilot forced landing
- Airframe damage: None; flew again same day
- **Result:** SwiftPilot envelope protection fired in <1 second both times; clean recovery to stable hover

## Acceptance Gates (Formal Clearance for Future Flights)

Before Flight Days 2–3, ECS-DoT must clear four SWIL gates:

1. **Hover Stability:** Hold roll & pitch within ±5° RMS for 60 s post-handover (±150 µs PWM tolerance)
2. **Bumpless Handover:** PWM discontinuity ≤300 µs on every rotor between last SwiftPilot command and first ECS-DoT command
3. **Re-engagement Soak:** 20× state-machine cycles (READY → ACTIVE → SHUTDOWN → CONNECTED → READY) without new failure modes
4. **Envelope Sweep:** Verify controller does not converge near envelope boundaries when ramping roll, pitch, yaw rate, throttle individually from steady hover

## Forward Plan

**May 2026:** EMASS retrains ECS-DoT controller against realized E20006 dynamics; clears four SWIL acceptance gates

**June 2026 (Flight Day 2 – Dynamic Pattern):**
- Pass 1: BST autopilot flown surrogate training mission (data capture for retraining)
- Pass 2: ECS-DoT flown identical pattern (like-for-like comparison)

**July 2026 (Flight Day 3 – Energy Showdown):**
- Sortie A: BST autopilot flies 100 m square at constant MSL to ~20% SOC
- Sortie B: ECS-DoT flies identical pattern; Wh delta is the deliverable

**Q3 2026:** Final report with efficiency hypothesis settled; comparison metrics include Wh per phase, time aloft, cross-track error, attitude error, and envelope events

## Notable Details

**Partnership Structure:**
- Black Swift Technologies: Airframe & autopilot (Boulder, CO; founded 2011)
- Nanoveu/EMASS: AI co-pilot silicon (Singapore-listed semiconductor specialist)
- Fixed-price SOW: $90K for 3 flight events + energy-delta report

**Safety Philosophy:**
- SwiftPilot stays in command of the airframe envelope at all times
- Learned controller "flies"; SwiftPilot "guarantees recovery"
- Both AI departures during Flight Day 1 were contained and analyzed for controller retraining

**Heritage & Credibility:**
- 15 years of UAS engineering (founded 2011)
- NASA mission heritage
- NOAA hurricane observations partnership
- AFWERX SBIR/D2P2 partner
- 2025 Small UAS of the Year award

**Key Competitive Advantage:**
- Sub-milliwatt inference on dedicated silicon (not GPU/CPU)
- Modular payload integration architecture proven across LiDAR, trace gas, and AI payloads
- On-board augmented intelligence already shipping (preventative maintenance, anomaly detection, safe-to-land decisions)
- Deterministic autopilot as safety net around learned controller (risk mitigation for emerging AI/ML in aviation)

**Efficiency Hypothesis:**
- Target: +10–20% flight-time gain from learned control over deterministic baseline
- Validation method: Wh delta on controlled geometry (100 m square to 20% SOC)
- Measurement standard: Apples-to-apples head-to-head under identical conditions