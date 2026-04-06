# Test Report No. 3: FRAGA D3-250 UAS Flight Test

## Document Metadata
- Type: Test Report
- Client/Agency: ByLight (Mustang program - expired)
- Program/Solicitation: Not specified
- Date: 17 July 2025 (test conducted 16 July 2025)
- BST Products/Systems Referenced: None directly; document concerns FRAGA D3-250 UAS (external system)
- Key Personnel: Jack Elston (last editor), UAV Operator #1, UAV Operator #2

## Executive Summary
This test report documents the third flight test of the FRAGA D3-250 unmanned aerial system, which resulted in a crash due to roll instability during bungee launch. The test aimed to replicate the bungee launch from Flight #1 and demonstrate net recovery from Flight #2. The aircraft experienced a stall on launch followed by pilot overreaction and extreme roll rates that prevented recovery before ground contact.

## Technical Approach
Test conducted under controlled conditions with the following parameters:
- **Launch method:** Bungee catapult (manual release by Operator #1)
- **Flight control:** Operator #2 controlled via remote controller in stabilized mode until handoff to autonomous flight controller
- **Aircraft configuration:** No changes from Flight #2
- **Recovery method planned:** Net recovery (not reached due to crash)

## Products & Capabilities Described
**FRAGA D3-250 UAS:**
- Mass: 7 kg (maximum takeoff weight)
- Equipped with flight controller and autopilot system
- Uses aileron control surfaces for roll control
- Capable of autonomous flight via flight controller
- Previous flights (Flight #1 and #2) had experienced similar but less severe instability

## Use Cases & Applications
Not explicitly stated; document focuses on testing basic flight envelope and recovery procedures rather than operational applications.

## Key Results

### Flight Sequence and Failure Analysis:
1. **t=0s:** Horizontal release at bungee launch (unsuccessful)
2. **t=0.65s:** Aircraft enters right bank with stall condition; speed only 24 km/h (below recommended 80 km/h launch speed)
3. **t=1.15s:** Maximum right bank angle reaches 45°; speed 62 km/h (confirms stall hypothesis)
4. **t=1.5s:** Operator #2 successfully recovers with correct aileron deflections; aircraft returns to horizontal, speed 83 km/h
5. **t=2.4s:** Aircraft overshoots into extreme left bank of -105°; speed 99 km/h; insufficient lift generated
6. **t=2.85s:** Left wing contacts ground at 96 km/h with -64° roll angle

### Root Cause Analysis:
Three contributing factors identified:
- **Insufficient launch acceleration:** Bungee pull force inadequate; engine did not start immediately after launch, resulting in stall condition with too-low launch speed
- **Pilot overreaction:** Operator #2's correction inputs were excessive, creating roll rate of 226 deg/sec (previous flights: max 80 deg/sec)
- **Control surface sensitivity:** Aileron deflections too responsive; roll rate overshoot made aircraft difficult to control and unstable

### Telemetry Findings:
- Roll rate of 226 deg/sec observed (significantly higher than previous flights)
- Both autopilot and operator had not previously requested 100% aileron deflections in Flights #1 and #2
- Roll angle consistently overshot desired attitude

## Notable Details

**Previously Unexplained Issue Resolved:** Flight #1 roll instability, initially attributed solely to poor flight controller tuning, now confirmed to have partial origin in inadequate launch acceleration leading to wing stall.

**System Tuning Status:** Flight controller parameters remain unchanged from Flight #2; suggests tuning was not the primary issue, supporting the acceleration/stall hypothesis.

**Control Authority vs. Precision Trade-off:** Report identifies fundamental design tension between control authority (needed for recovery) and precision (lost with excessive control surface deflection). Recommendations balance mechanical and software solutions.

## Improvements Recommended

1. **Increase launch acceleration** via stronger bungee pull force or catapult launcher to achieve minimum takeoff speed quickly
2. **Reduce aileron control surface deflection** during manufacturing of Units 3 and 4; requires flight controller retuning but improves control precision
3. **Tune flight controller parameters** on existing Units 1 and 2 to limit maximum aileron deflections without mechanical modification (accepts minor precision loss)