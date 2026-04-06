# S2 Incident Report - S20011 Battery Failure

## Document Metadata
- **Type:** Incident Report
- **Client/Agency:** NASA Langley
- **Program/Solicitation:** CICADA (Collaborative Interdisciplinary Constellation for Advanced Data Analysis)
- **Date:** October 17, 2022 (initial version Oct 7, 2022; revisions through Oct 24)
- **BST Products/Systems Referenced:** S2 (aircraft system), S20011 (specific airframe), autopilot, power distribution board, ESC, air data system
- **Key Personnel:** Jack Elston (last editor)

---

## Executive Summary

On September 21, 2022, Black Swift Technologies S2 airframe S20011 experienced a critical battery failure during the fourth of four test flights at NASA Wallows Flight Facility, resulting in loss of the aircraft over water. The incident began approximately 12 minutes into flight when the battery voltage dropped rapidly below safe operating thresholds, triggering a system reset. Although multiple emergency systems performed as designed and maintained controlled flight through redundant sensors and autopilot recovery logic, cascading sensor failures (particularly the pitot/dynamic pressure sensor) prevented manual recovery, and the aircraft descended into the Atlantic Ocean. Analysis indicates the battery itself failed catastrophically rather than being caused by the flight profile, though high current draws during steep climbs may have contributed to the failure mode.

---

## Technical Approach & Analysis

### Flight Profile & Incident Timeline
- **Date:** September 21, 2022
- **Aircraft:** S20011 (Serial 0x4100005D)
- **Total Flights:** 4 (TOF: 22.5 min, 24.9 min, 32.2 min, 21.9 min with crash)
- **Location:** NASA Wallops Flight Facility (37°51.116'N, 75°24.9'W area)
- **Maximum Altitude:** 6,300 ft AGL (1,927 m)
- **Wind Conditions:** Surface SE winds, shifting to NW at altitude (17 knots sustained, 8.7 m/s)

### Incident Sequence
1. **~10 minutes into Flight 4:** Aircraft begins struggling to achieve commanded climb rate; voltage begins more rapid decline
2. **~12 minutes (735.5 seconds):** Battery voltage drops to 16.3V (2.72 V/cell); ground station loses telemetry connection
3. **~90 seconds later:** Connection re-established; battery voltage now ~6V, IAS sensor offline, dynamic pressure lost
4. **Post-incident:** Aircraft in preflight mode following autopilot reboot; positive attitude control maintained; aircraft descended 1,900 m over ~9 minutes in controlled descent
5. **Final:** Data loss at 400 ft AGL; presumed impact with water

### Power Analysis Methodology
- Compared S20011's 4 flights against 62 historical S2 flights with similar 1,500+ m climbs
- Analysis segmented battery discharge into four capacity regimes:
  - 100%–80% (black)
  - 80%–60% (green)
  - 60%–40% (blue)
  - 40%–20% (red)
- Measured voltage drop at cruise power (~12A) across each regime
- **Key Finding:** Flights 1–3 of S20011 showed normal battery performance matching historical baseline. Flight 4 showed severe voltage drop departure **only below 60% capacity**, suggesting sudden failure rather than gradual degradation.

### Current Draw Analysis
- Early flight sustained currents **above 40A max continuous rating** for ~100 seconds during initial climb
- Brief periods above 40A typical in steep climb scenarios but not nominal
- Most comparison flights maintained <40A despite similar climb profiles
- Flight 4 showed progressively higher current draw as climb rate decreased, indicating loss of climbing efficiency

---

## Products & Capabilities Described

### S2 Aircraft System
**What it is:**
- Small, long-duration UAS designed for scientific atmospheric sampling and surveillance
- Equipped with autonomous autopilot with redundant sensor architecture
- Powered by custom-integrated battery pack (4x Sanyo NCR18650GA cells in series; 14Ah nominal capacity, 18V nominal voltage)

**Performance Specifications:**
- Cruise power draw: 8–12 watts typical
- Maximum rated battery discharge: 40A continuous (10A per cell × 4 cells)
- Recommended safe discharge limit: 60–70°C battery temperature
- Minimum operating voltage: ~2.5–3.0V per cell (15–18V pack)
- Maximum altitude capability: demonstrated to ~2.5 km AGL with appropriate flight profile

**Key Systems Identified in Incident:**
1. **Autopilot:** Handles preflight mode, attitude control, GPS-based navigation, failsafe logic
2. **Power Distribution Board:** Manages reverse voltage protection, overcurrent surge protection, dual 5V redundant supplies, electronic gas gauge (coulomb counter), battery state monitoring
3. **ESC (Electronic Speed Controller):** Supports voltage cutoff (disabled), receives throttle commands from autopilot
4. **Air Data System:** Primary pitot/dynamic pressure sensor + redundant static pressure sensor on separate PCB
5. **Battery Management:** Current limiting on supply board; autopilot monitors power draw against energy model (atmospheric conditions, control surface deflection, orientation) to detect powertrain failure
6. **Radio System:** 900 MHz link for telemetry/waypoint upload; 2.4 GHz independent manual control link
7. **Emergency Systems:**
   - **In-flight Reset Recovery:** Autopilot can detect and recover from reset events
   - **Brownout Mode:** Limited functionality with reduced power availability
   - **Sensor Redundancy:** Automatic switchover to backup static pressure sensor; fallback airspeed control without dynamic pressure
   - **Preflight Mode Glide:** Can maintain level flight (0° roll/pitch) using IMU alone if GPS lost

**Battery Integration:**
- Manufactured by external professional supplier; BST integrates into shell and attaches balance tap connector
- Anderson PP45 connectors (45A rated) for power
- Protection circuit board-based (not cell-integrated)
- Cell voltage tolerance in shell: ±50 mV max; charging to full capacity
- Discharge testing to ~30% SOC for shipping compliance
- State of charge calculated via coulomb counting (Amp-hours), not voltage (voltage insufficient indicator)

---

## Use Cases & Applications

### NASA Langley CICADA Program
- Atmospheric and oceanographic research missions
- Operations from coastal facilities (NASA Wallops Flight Facility demonstrated here)
- Multi-hour surveillance/sampling flights in diverse wind conditions
- Requirement for autonomous long-distance flight with operator monitoring from ground station

---

## Key Results & Findings

### Root Cause Analysis

**Primary Cause:** Battery pack failure (S/N 36)
- No evidence of prior degradation; Flights 1–3 showed healthy battery performance
- Failure was **sudden and catastrophic**, not gradual
- Voltage collapse occurred specifically **below 60% charge state**, indicating internal fault activation at low remaining capacity
- Bench testing reproduced pitot sensor failure at low voltages but could not reproduce the post-reset power readings, suggesting either:
  - Partial system brownout/shutdown to conserve remaining power
  - Fault in battery voltage/current measurement circuit
  - Combination of above

**Contributing Factors (Not Root Cause):**
- Flight profile with steep climbs (12° flight path angle) sustained high current draw (~40A+) for extended periods
- Mission design called for climb to 2,300m, higher than typical BST operations (usually ~2.5km over 30km flight path for gradual climb)
- Strong tailwind during climb phase required steeper climb angles to maintain planned track

### System Performance During Incident

**Successful Emergency Response:**
1. **In-flight Reset:** Autopilot successfully rebooted and resumed attitude control within 90 seconds
2. **Sensor Redundancy:** Automatic switchover from primary to backup static pressure sensor functioned
3. **Fallback Control:** Simplified airspeed controller maintained reasonable flight without dynamic pressure sensor
4. **Preflight Mode Stability:** Despite sensor failures and low power, aircraft maintained level flight using IMU
5. **GPS Recovery:** Regained fix immediately post-reset
6. **Attitude Hold:** Roll and pitch control maintained throughout 9-minute descent after incident
7. **Protection Circuits:** Board-level protection prevented complete system failure despite near-catastrophic battery condition

**Cascading Failure Points:**
1. Battery voltage collapse triggered autopilot reset
2. Pitot/dynamic pressure sensor voltage dropout during brownout
3. Loss of GPS signal (IAS required for full flight mode exit)
4. Aircraft stuck in preflight mode without ability to accept manual joystick control (disabled in preflight)
5. Manual control link (2.4 GHz) likely out of range for out-of-sight portion of flight (>5.4 km slant range)
6. Radio signal strength degraded (RSSI near -87 dB, approaching sensitivity limit of -110 dB)

### Battery Bench Testing Results (Post-Incident)

**Test 1: B2-0009 at 40A (rated continuous discharge)**
- Smoke observed at ~300 seconds into test
- Test terminated at 322 seconds
- IR monitoring limited; no temps >160°F observed on external surfaces (actual failure was internal)
- **Failure Mode:** Likely foam/PVC insulation between carbon straps or balance tap wire insulation melting due to internal bus bar heating

**Test 2: B2-0035 at 30A (75% of rated maximum)**
- No smoke, but plastic shrink wrap deformation and burning smell
- IR thermography: ~315°F measured at mid-rear of pack (near bus bars), with >100°F temperature gradients across pack
- Test continued to 2.5V/cell (15V cutoff): 11.65 Ah capacity @ 30A; ~9 Ah @ nominal 18V cutoff
- Shrink wrap damage and delamination observed post-test
- Pre-existing shrink wrap damage noted on previously flown packs, indicating repetitive heating issues

**BST Response to Testing:**
- Acknowledged shrink wrap melting on two packs previously "pushed very hard"
- Smoke attributed to foam insulation between carbon straps or PVC balance tap wire insulation
- Noted that typical flight profiles (brief full-throttle climbout, extended cruise, occasional maneuvers) do not sustain conditions seen in NASA test
- Concluded mission profile exceeded safe operating envelope for battery
- Temperature management concern: Bus bar heating can damage balance tap wire insulation, risking internal short circuit
- Recommended safe operating temperature limit: 60–70°C (battery not currently monitored for temperature)

---

## Notable Details

### Qualification/Verification Procedures
- **Upon Receipt:** Visual inspection, cell voltage check (±100 mV tolerance), mass verification
- **Post-Integration:** Charge, cell voltage check (±50 mV), fitment test, max throttle RPM check, visual inspection, partial discharge to ~30% SOC
- **In-Service:** Current and voltage monitoring via electronic gas gauge; coulomb counting for state of charge; power draw estimation via autopilot model

### Recommended System Changes

**Immediate (to resume flight testing):**
1. Reduce maximum flight path angle from 12° to 10° to lower sustained throttle demand
2. Add firmware voltage monitoring under load with Level 3 failure warning if sustained below threshold (operator selects "Return to Land" or "Terminate Flight")
3. Improve air data system firmware for brownout conditions
4. Provide operator method to force system into flying mode (manual control)

**Future Improvements:**
1. Auto-exit preflight mode on in-flight reset even with IAS sensor failure
2. Prevent throttle commands during dangerous battery state
3. Block calibrations in flight when lateral/vertical velocity detected
4. Alert operator when switching to backup static pressure sensor
5. More sophisticated control scheme for pitot failure

### Radio Performance
- 900 MHz telemetry link: ~29 dB margin at 9.3 km per NASA link analysis
- RSSI during incident: Average -87 dB at max range 4.3 km; briefly approached -110 dB sensitivity limit (likely due to aircraft orientation)
- 2.4 GHz manual control link: Likely out of range during out-of-sight descent (aircraft slant range >5.4 km)

### Operational Context
- First occurrence of battery failure in BST S2 operational history
- Four total flights conducted on incident date with same battery (S/N 36) in flights 1–2, then different batteries (S/N