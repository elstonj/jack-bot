# Sales — Shared Drive

## Overview
- **Total files:** 20 | **Total folders:** 4
- **Date range:** 2026-06-05 (all files created and modified on same date)
- **Primary purpose:** Flight test data storage and drone application testing documentation

## Folder Structure

```
Sales/
├── Flight Data/
│   ├── 20260522/ (3 files)
│   │   └── Early flight tests (ECSDOT flights, drone app data)
│   ├── 20260528 - Microtests/ (3 files)
│   │   └── Microtest flights with filter variations (yaw, speed)
│   └── 20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/ (13 files)
│       └── Recent flight summaries, test loops, and comparative flight data
└── [Root level] (1 image file)
```

## Key Documents by Category

### **Reports & Analysis**
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/20260605 Flight Summaries` | Modified: 2026-06-05 | Editor: Daniel Prendergast

### **Flight Test Data & Logs**
- `Flight Data/20260522/ECSDOT_Flight1-20260522.nc` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260522/ECSDOT_Flight2-20260522.nc` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260522/droneapp_20260523_025444` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260528 - Microtests/droneapp_microtest1_20260527_215900` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260528 - Microtests/droneapp_microtest2_20260528_004237_yaw_and_speed_filtered_max_3.0` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260528 - Microtests/droneapp_microtest3_20260528_005850_only_speed_filtered_max_3.0` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/20260605-Flights1_and_2.nc` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/20260605-Flight_3.nc` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/20260605-Flight4.nc` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/20260605-Flight5.nc` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/droneapp_test_loop_20260602_211646_AI_10HZ_LPF_64Hz_max3.5_to_3.8_NOS_wp` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/droneapp_test_loop_20260605_145418_AI_10HZ_LPF_64Hz_max3_hardcodedwp_ALT1565` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/droneapp_test_loop_20260605_150531_AI_10HZ_LPF_64Hz_max3p6_hardcodedwp_ALT1565` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/droneapp_test_loop_20260605_153609_AI_10HZ_LPF_64Hz_max3p83_hardcodedwp_ALT1565` | Modified: 2026-06-05 | Editor: Daniel Prendergast

### **Visualizations**
- `Image.png` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/20260605-Flights1_and_2.png` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/20260605-Flight3.png` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/20260605-Flight4.png` | Modified: 2026-06-05 | Editor: Daniel Prendergast
- `Flight Data/20260605 - 3 Hardcoded Controllers and 1 with AP waypoints/20260605-Flight5.png` | Modified: 2026-06-05 | Editor: Daniel Prendergast

## Recent Activity Patterns
- **Primary contributor:** Daniel Prendergast (100% of edits — all 20 files last modified by this user)
- **Activity concentration:** All files timestamped 2026-06-05; bulk data organization/consolidation activity
- **Focus areas:** Drone flight testing with emphasis on controller variations and autopilot (AP) waypoint testing
- **Testing progression:** Chronological test sequence from 2026-05-22 through 2026-06-05, with increasing sophistication (microtests → hardcoded controllers → waypoint-based autopilot)

## Project/Client Document Mapping
- **ECSDOT Project** — Early flight tests (2026-05-22): `ECSDOT_Flight1-20260522.nc`, `ECSDOT_Flight2-20260522.nc`
- **Drone Application Testing** — Ongoing development and testing of drone control systems with variations in:
  - Microtest filtering approaches (yaw, speed)
  - Hardcoded waypoint controllers
  - Autopilot (AP) waypoint navigation
  - Low-pass filter (LPF) parameters and altitude variations

## Notes on Drive Mismatch
⚠️ **Data inconsistency detected:** The existing knowledge file referenced 2 EMASS proposal files (modified 2026-06-03), but the new raw data shows 20 flight data files with no EMASS proposals present. This suggests either:
1. The drive was recently cleared and repurposed for flight data
2. EMASS proposals may have been moved to a different shared drive
3. Raw data extraction did not capture all files

**Recommendation:** Verify current state of EMASS proposal documents and whether they should be preserved in a separate archive location.