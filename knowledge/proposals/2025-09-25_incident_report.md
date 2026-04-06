# S0 Incident Report - 2025 Season

## Document Metadata
- Type: Incident Report
- Client/Agency: NOAA
- Program/Solicitation: NOAA-Cione Hurricane Phase II, 2025 Season
- Date: 25 September 2025
- BST Products/Systems Referenced: S0 UAS (Unmanned Aircraft System)
- Key Personnel: Jack Elston (last editor)

## Executive Summary
During NOAA WP-3D hurricane reconnaissance missions in September 2025, multiple S0 UAS aircraft suffered critical failures immediately after deployment, with some losing power mid-flight. Root cause analysis identified a firmware-level bug in the Power Sensing and Switching (PSNS) module where transient negative current readings (as small as -0.4 A) incorrectly triggered charge mode and shut down the autopilot. A firmware fix has been developed and bench-tested and is now undergoing validation.

## Technical Approach

### Root Cause Identified
The PSNS module firmware contained a logic error where negative current events sustained for approximately 500 milliseconds forced the system into charge mode, cutting power to the autopilot. Contributing factors included:
- Rapid throttle-down during turbulence
- Motor back-EMF at separation
- Precipitation and sensor noise
- Arcing on deployment tube board connections (both old and new variants)
- Radio reinitialization failures masking brief reboots

### Proposed Fix Components

**Firmware Upgrade (PSNS + Autopilot)**
- New state machine architecture for power management
- Requires ≥5 seconds of sustained negative current (all samples negative) before entering charge mode (vs. previous ~500 ms threshold)
- Autopilot must confirm non-flight state before allowing shutdown
- Low-pass filtered voltages to avoid false trigger events

**Parameter Adjustments**
- Throttle filter increased from 2 seconds full range to reduce risk of negative current spikes while maintaining flight stability
- Clog detector re-enabled to safeguard against pitot tube blockages

**Procedural Improvements**
- Streamlined "ready-to-launch → enable engine" workflow on tablet interface

## Products & Capabilities Described

### S0 UAS
- **What it is**: Small unmanned aircraft system designed for hurricane reconnaissance missions
- **Performance in successful missions**: 
  - S0-59 completed 106.9 minute flight
  - Operated 40+ minutes below 50 m AGL
  - Handled peak wind gusts of 72 mph
  - Successfully operated in heavy rain
- **Deployment method**: Launch from deployment tubes on NOAA WP-3D aircraft
- **Key subsystems**: PSNS module, autopilot, motor/throttle control, radio communications

## Use Cases & Applications
- Hurricane reconnaissance and sampling missions for NOAA
- Low-altitude operations in severe weather (high wind gusts, precipitation)
- Sustained flights in tropical storm/hurricane conditions

## Key Results

### Failure Summary
| Date | Aircraft SN | Outcome | Notes |
|------|------------|---------|-------|
| 9/20 | S0-59 | 106.9 min success | 40+ min <50 m AGL, peak gust 72 mph |
| 9/20 | S0-50 | Immediate failure | Shutdown on launch |
| 9/21 | S0-57 | Immediate failure | Shutdown on launch |
| 9/21 | S0-54 | Partial (30 min) | Lost power mid-descent |
| 9/21 | S0-52 | Immediate failure | Shutdown within seconds |

### Validation Completed (as of Sept 24–25)
- Flight test of PSNS fix on S10019 completed
- Conducted 3 local S0 flight tests confirming resilience
- One S0 operated for >1 hour in heavy rain
- Throttle filter stability validated

## Notable Details
- Four aircraft (S0-50, S0-57, S0-52, S0-54) experienced failures across a 2-day period during active hurricane operations
- Failures affected both old and new deployment tube board variants, suggesting the issue was firmware/firmware-interaction rather than hardware-specific
- The fix represents a significant increase in the negative current threshold tolerance (from ~500 ms to ≥5 seconds), indicating the original threshold was overly sensitive to transient power conditions during flight operations
- Successful flight of S0-59 during same period demonstrates that the aircraft platform is capable of extended hurricane operations once the firmware issue is resolved
- Document marked as company confidential and proprietary