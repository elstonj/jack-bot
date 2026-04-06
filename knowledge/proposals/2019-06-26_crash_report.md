# 2019-06-26 Crash Report

## Document Metadata
- Type: Flight incident report
- Client/Agency: INSTAAR (Institute of Arctic and Alpine Research)
- Program/Solicitation: Not specified
- Date: 2019-06-26 (flight date); 2019-07-08 (document created/modified)
- BST Products/Systems Referenced: S2 (aircraft S20010)
- Key Personnel: Maciej Stachura (last editor)

## Executive Summary
On 2019-06-26, BST S2 aircraft S20010 experienced a catastrophic structural failure during launch when the right wing disconnected, resulting in loss of critical sensors and control surfaces. The aircraft entered failsafe mode and spiraled into the ground approximately 30 seconds after takeoff. The payload sustained more damage than the airframe, but full damage assessment was pending.

## Incident Details

### Root Cause
Right wing disconnected on launch, causing immediate loss of:
- Airspeed sensor
- Right aileron
- Right flap
- Laser altimeter

All sensor losses occurred at the moment of launch (visible in telemetry data).

### Aircraft Response & Failsafe Behavior
1. **Failsafe triggered** due to loss of airspeed measurement
2. **Throttle disabled** automatically
3. **Flaps commanded to deploy** (only left flap deployed due to right wing loss)
4. **Roll control degraded** - bank angle set to 30° command:
   - Aircraft overshot to 70° due to single aileron control
   - Control system compensated for missing right aileron and pulled back to ~30° bank
   - Eventual uncontrollable spiral resulted

### Impact
- **Impact G-load:** +8g's on y-axis (indicating right wing struck first)
- **Ground speed at impact:** 19 m/s
- **Pitch attitude:** Aircraft pitched up at impact
- **Damage:** Payload sustained more damage than airframe; full assessment pending

## Technical Observations
- Telemetry data captured the event in detail (Figures 1 & 2)
- Control system demonstrated ability to adapt to loss of one aileron (pulling roll back from 70° overshoot to 30° commanded angle)
- Loss of airspeed sensor triggered automatic failsafe as designed
- Aircraft remained controllable despite severe structural failure until spiral developed

## Notable Details
- This appears to be an INSTAAR-related project (likely environmental/research monitoring)
- Structural failure (wing disconnect) suggests potential manufacturing, assembly, or attachment point issue requiring investigation
- Failsafe logic functioned as intended but insufficient to prevent loss of aircraft given the severity of structural damage
- Report authored by flight operations personnel; implies BST maintains detailed telemetry and analysis protocols