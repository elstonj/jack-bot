# ECS-DoT UAS Integration and Validation — Final Technical Report

## Document Metadata
- Type: Final Technical Report (Phase 4b Deliverable)
- Client/Agency: EMASS (Embedded A.I. Systems Pte Ltd), a Nanoveu business
- Program/Solicitation: ECS-DoT UAS Integration and Validation contract
- Date: 24 August 2026
- Period of Performance: 17 November 2025 – 26 June 2026
- BST Products/Systems Referenced: Black Swift E2 quadrotor, SwiftPilot autopilot
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
This report documents the integration of EMASS's ECS-DoT ultra-low-power Edge-AI System-on-Chip into the Black Swift E2 quadrotor and comprehensive flight testing conducted April–June 2026. The integration objective was achieved: the ECS-DoT was installed, powered, interfaced through the aircraft payload port, and integrated into the SwiftPilot control loop as a commanding element, successfully flying five complete pattern loops with no envelope violations. However, the endurance improvement objective was not met: while measured whole-cruise efficiency gains were +7.6% and +8.1%, analysis reveals these correspond entirely to cruise speed differences between paired flights (+0.29–0.31 m/s faster for ECS-DoT). When speed is normalized against the airframe efficiency trend (R² = 0.997), both ECS-DoT flights fall 1.0–1.2% below the trend. The campaign was conducted in the speed band where specific range is dominated by airspeed rather than control strategy.

## Technical Approach

### Integration Architecture
The ECS-DoT was integrated as a commanding element in the SwiftPilot layered control stack, not as an additive or competing controller. The SoC receives aircraft state telemetry at the start of each 300 Hz control cycle and returns commands. When the payload is in RUNNING state, its commands replace the autopilot's output at that layer; the autopilot resumes command immediately on envelope violation, operator intervention, or communication loss.

### Hardware Interface
- **Connection**: Four-wire cable between E2 payload port (9-position D-sub) and ECS-DoT evaluation board
- **Power**: Raw battery (19.2–25.2 V) via inline 5V regulator, 3 A max
- **Data**: UART (pins 3/4), with SoC UART at 3.3 V requiring level shifter to aircraft 5 V logic
- **Autoboot**: Raspberry Pi Pico 2 holding application image, loaded via JTAG at power-up; flashing handled by Python utility
- **Payload Enclosure**: 3D-printed, mounted to E2 payload rail; device generates negligible heat

### Control Modes (Evolution)
1. **Initial (April–May)**: Direct actuator control via ACTUATORS_VALUES packets with 16-channel PWM array
2. **Final (Late May–June)**: World-frame velocity and yaw control (CMD_VEL_CTRL tuples + CMD_YAW) commanding vx, vy, vz and absolute yaw target

The migration from actuator to velocity control was the single most consequential architectural decision, enabling more stable closed-loop performance and reducing interface defects.

### Safety Architecture
SwiftPilot enforces a hard flight envelope irrespective of commanding element:

| Limit | Value | Rationale |
|-------|-------|-----------|
| Roll | ±20.0° | Recovery margin at low altitude |
| Pitch | ±20.0° | Recovery margin at low altitude |
| Roll/Pitch rate | 6.98 rad/s | Structural and estimator margin |
| Yaw rate | 0.52 rad/s | Estimator and heading-hold margin |
| Side speed | 4.00 m/s (relaxed to 5.0 m/s during June campaign) | Stability margin |
| Vertical speed | −1.50 to +3.00 m/s | Safety |
| Lost GPS | 5 s | Navigation integrity |
| Max PDOP | 3.0 | Navigation integrity |

When limits are violated, autopilot immediately revokes payload control, reverts to own controller, and signals PAYLOAD_CTRL_SHUTDOWN.

### Telemetry Definition
Aircraft provides to ECS-DoT at specified rates: PWM (each rotor, 20 Hz max 300 Hz), speed over ground (10 Hz), climb/descent rate (10 Hz), battery current (1 Hz), battery voltage (1 Hz), orientation roll/pitch/yaw (20 Hz max 1000 Hz), altitude (10 Hz), barometric pressure (2 Hz). ECS-DoT derives throttle and power calculations on-board.

### Payload State Machine
Six-step handshake with operator safety interlock:
1. Heartbeat/initialization → CONNECTED
2. Wait state
3. **Operator grants CMD_PAYLOAD_CONTROL = READY** (deliberate safety design; payload cannot self-promote)
4. Payload requests ACTIVE
5. State becomes RUNNING; payload issues actuator/velocity commands
6. Relinquish (OFF) or shutdown (PAYLOAD_CTRL_SHUTDOWN) returns to WAITING

## Products & Capabilities Described

### Black Swift E2 Quadrotor
- **Configuration**: 4-rotor multirotor, X configuration
- **Mass as flown**: 11.45 kg (including ECS-DoT payload and enclosure)
- **Battery**: 6-cell Li-Ion, 907.2 Wh (nominal 22.2 V, 21.4–22.7 V in cruise)
- **Autopilot**: BST SwiftPilot (SW 3.0.28, comms 3.22.0, HW 2050)
- **Control loop rate**: 300 Hz (exceeds simulation environment rate)
- **Mean cruise power**: ~1200 W (measured 3.5–4.6 m/s, 11 m AGL)
- **Maximum-range airspeed**: ~8 m/s
- **Waypoint capture radius**: 8.0 m
- **Powered endurance**: ~7 minutes in baseline cruise conditions

**Deployment**: E2 flown under FAA Part 107 at Sunny Slope Sod Farm, Longmont, Colorado. Two airframes (E20006, E20009) used; same aircraft flown in both ECS-DoT and baseline modes to eliminate airframe variation.

### ECS-DoT Edge-AI SoC
- **Function**: Ultra-low-power on-sensor inference chip intended for sub-milliwatt operation
- **Operating mode**: Executes local AI inference without cloud connectivity
- **Integration**: Evaluation board (NTU-2_EVB_RevA, ~70 mm × 60 mm) powered and programmed via JTAG micro-USB or 5 V barrel jack
- **Telemetry latency**: Minimal, with SoC UART directly routed via level shifter to aircraft payload port
- **Storage**: No on-board logging; application image held by Raspberry Pi Pico 2 autoboot module
- **Control capability**: Issues velocity commands and yaw setpoints at rates up to 75 Hz (achieved ~64 Hz practical)

**Simulation origin**: EMASS had previously evaluated the device in Gazebo simulation with ArduPilot across quadcopter, hexacopter, and octocopter classes, reporting substantial improvements in modeled flight endurance.

### SwiftPilot Autopilot
- **Role**: Core flight control autopilot with layered control architecture
- **Native speed control**: Target cruise speed mode (3.5, 4.0, 4.5 m/s tested) without upper bound; achieves setpoint ±0.1 m/s
- **Waypoint navigation**: Tight path tracking with 8.0 m capture radius; slows markedly at corners
- **Envelope protection**: Unrelaxable hard limits; immediate reversion to autopilot on violation
- **Integration flexibility**: Accepts external commands at multiple control layers (direct actuator, velocity/yaw, waypoint sequencing)
- **Altitude reference**: Supports both constant AGL (terrain-following) and constant MSL waypoint definitions

## Use Cases & Applications

### Primary Mission Profile
- **Closed-course autonomous flight**: Rectangular pattern of four waypoints (440 m perimeter) flown repeatedly at constant altitude
- **Altitude**: 15 m above ground level (1549 m MSL) at test site elevation of 1534 m
- **Duration**: 5–6 minute pattern flights to characterize energy consumption and control performance
- **Constraint**: Environmental sensing payload weight and power budget; demonstrable improvement in flight endurance

### Test Matrices
**Speed-resolved efficiency evaluation (final June 2026 campaign)**:
- BST baselines at 3.5, 4.0, 4.5 m/s cruise setpoint
- ECS-DoT controllers trained/limited to 3.9, 4.4, 4.5 m/s peak speeds
- Objective: Measure efficiency gains independent of speed effects

**Progressive validation approach**:
- Phase 1: Reference flight energy baseline
- Phase 2: First handover and envelope-protection testing
- Phase 3: Square-pattern closed-loop stability
- Phase 4a: Axis-by-axis microtest (vertical, lateral, forward, yaw, combined)
- Phase 4b: Final paired efficiency comparison

## Key Results

### Integration Success
- **Objective met**: ECS-DoT fully integrated, powered, interfaced, and commanding the aircraft within normal operating envelope
- **Timeline**: Hardware integration Feb 2026; bench validation Apr 2026; first live handover Apr 2026; progressive debugging May 2026; final data campaign Jun 2026
- **First closed-loop success**: Two complete loops flown under ECS-DoT control on 5 June 2026; five-loop run on 26 June 2026
- **Envelope protection**: Activation on every required occasion; no damage or injury; largest excursion recorded was 73° roll / 43° pitch (recovered at 10 m AGL with safe margin)

### Efficiency Results (Whole-Cruise Specific Range)

| Flight Log | BST Speed (m/s) | ECS-DoT Speed (m/s) | BST (mm/J) | ECS-DoT (mm/J) | Reported Gain |
|------------|-----------------|-------------------|-----------|---------------|---------------|
| Log 6 (3.5 / 3.9) | 3.50 | 3.79 | 2.898 | 3.118 | +7.6% |
| Log 7 (4.0 / 4.4) | 4.09 | 4.40 | 3.393 | 3.667 | +8.1% |

**Speed-normalized analysis**:
- BST baselines define airframe efficiency trend: **R² = 0.997** (nearly perfect linearity)
- Trend slope: 0.919 mm/J per m/s
- ECS-DoT flights fall **on the trend**, 1.0% and 1.2% below it
- Speed differences: ECS-DoT flew +0.29 m/s and +0.31 m/s faster than baselines
- **Conclusion**: Reported gains correspond entirely to speed difference; speed-normalized controller difference is **within ±1.2%** and not resolvable

### Power Analysis
Mean cruise power across entire test band (3.5–4.6 m/s):
- **Range**: 1176–1216 W (variation of 3.3%)
- **Speed variation across band**: 32%
- Aircraft operates in **induced-power-dominated regime** where power is nearly constant with forward speed
- Specific range therefore rises nearly proportionally to airspeed in this band

### Segment-Level Performance
EMASS reported segment-level gains:
- **Straight legs**: +7.1% (both pairings)
- **Turns**: +10.9% and +12.4%
- **Mechanism**: ECS-DoT maintains higher speed through corners (wider turning radius, less speed loss); SwiftPilot slows markedly at waypoints
- **Root cause**: Difference in path-tracking strategy (loose vs. tight), amplified in the region where power is speed-independent

### Altitude Hold and Path Consistency
- **