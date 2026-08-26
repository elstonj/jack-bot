# EMASS Flight Test Report Using ECS-DoT

## Document Metadata
- Type: Flight test report
- Client/Agency: EMASS (Drone AI Dev Team)
- Program/Solicitation: Not specified
- Date: July 6, 2026
- BST Products/Systems Referenced: BST autopilot control system
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
This report documents a controlled flight test campaign comparing the ECS-DoT autopilot controller against Black Swift Technologies' autopilot control system across a range of flight speeds and maneuver types. Conducted on June 26, 2026, the campaign flew a rectangular square-pattern mission to quantify energy efficiency, power consumption, and stability. ECS-DoT achieved +7.6% to +8.1% higher measured cruise efficiency than BST baselines, with notably superior performance in turn handling and altitude stability.

## Technical Approach

**Mission Design:**
- Rectangular square-pattern waypoint mission (4 waypoints, closed loop, counter-clockwise)
- Pattern dimensions: ~114 m (E-W legs) × 106 m (N-S legs), total perimeter ~440 m
- Altitude: 1549.06 m MSL (~15 m AGL)
- Location: 40.13°N, 105.07°W (Denver area)

**Test Protocol:**
- Nine flights conducted across five data logs on 2026-06-26
- Matched-pair comparison structure: BST autopilot baseline paired with ECS-DoT at corresponding speeds
- Three successful speed groups: 3.5/3.9 m/s (Log 6), 4.0/4.4 m/s (Log 7), 4.5 m/s (Log 8, BST only)

**Speed Implementation:**
- BST autopilot: Given target cruise speed (0.50 m/s below maximum), flies to meet it
- ECS-DoT: Given hard speed limit (0.50 m/s margin) with actual implemented max 0.10 m/s below stated limit to prevent overage
- Speed mapping groups:
  - Group 1: BST 3.5 m/s cruise vs. ECS-DoT 4.0 m/s max (hard limit 4.5)
  - Group 2: BST 4.0 m/s cruise vs. ECS-DoT 4.5 m/s max (hard limit 5.0)
  - Group 3: BST 4.5 m/s cruise vs. ECS-DoT 5.0 m/s max (hard limit 5.5)

## Products & Capabilities Described

**BST Autopilot Control System**
- Altitude reference: Above Ground Level (AGL)
- Altitude-hold performance: ±1.44 m std (AGL), ±1.98 m std (MSL) in cruise
- Yaw control: 95th percentile yaw rate 5.90–6.40 °/s
- Speed envelope tested: 3.5–4.5 m/s cruise
- Path repeatability: Greater loop-to-loop variation, particularly on northern leg; potential wind-correction behavior differences
- Turn performance: Marked speed reduction at corners (visible as lighter green in velocity plots), variable performance along straights
- Whole-flight efficiency: 2.898 mm/J (Log 6, 3.5 m/s) to 3.393 mm/J (Log 7, 4.0 m/s)

**ECS-DoT Controller (Comparison System)**
- Altitude reference: Mean Sea Level (MSL)
- Altitude-hold performance: ±0.68 m std (MSL), ±1.17 m std (AGL) in cruise — approximately 3× tighter MSL hold than BST
- Yaw control: 95th percentile yaw rate 4.20–5.33 °/s (superior to BST)
- Speed envelope: Successfully demonstrated up to 4.4 m/s; higher speeds (4.9–5.0 m/s) not tested due to weather constraints
- Path repeatability: Tight, repeatable rounded square with all five loops closely overlaid; speed-independent advantage
- Turn performance: Smoother turn control, larger turn radius, smaller velocity drop relative to entry speed
- Whole-flight efficiency: 3.118 mm/J (Log 6, 3.79 m/s measured) to 3.667 mm/J (Log 7, 4.40 m/s measured)

## Use Cases & Applications

The test framework is designed to evaluate autopilot controller performance in precision waypoint navigation tasks, particularly:
- Low-altitude loitering operations (~15 m AGL)
- Energy-constrained flight endurance missions
- Repeatable pattern flight (search, survey, monitoring applications)
- Multi-loop autonomous mission completion

The square pattern provides controlled assessment of:
- Straight-leg cruise efficiency
- Turn-handling efficiency
- Altitude stability over extended flight
- Path consistency across repeated loops

## Key Results

**Whole-Cruise Efficiency:**
- Log 6 (lower speed pair): ECS-DoT +7.6% efficiency gain (3.118 vs 2.898 mm/J)
- Log 7 (higher speed pair): ECS-DoT +8.1% efficiency gain (3.667 vs 3.393 mm/J)
- Trend: Efficiency improves with speed on both controllers; both follow a single airframe speed–efficiency curve

**Segment-Level Efficiency (Straight Legs vs. Turns):**
- Log 6 straight legs: ECS-DoT +7.1%
- Log 6 turns: ECS-DoT +10.9%
- Log 7 straight legs: ECS-DoT +7.1%
- Log 7 turns: ECS-DoT +12.4%
- **Key finding:** Turn handling is the primary efficiency advantage for ECS-DoT

**Per-Corner Performance (Log 6):**
- WP30: +7.5% (mean)
- WP31: +7.9% (mean)
- WP32: +11.8% (mean)
- WP33: +14.3% (mean)
- Average: +10.9% per-corner gain

**Per-Corner Performance (Log 7):**
- WP30: +13.4%
- WP31: +10.3%
- WP32: +15.7%
- WP33: +7.0%
- Average: +12.4% per-corner gain

**Altitude-Hold Stability (Speed-Independent):**
- ECS-DoT MSL hold: 0.68 m std (Log 6) / 0.26 m std (Log 7)
- BST AGL hold: 1.44 m std (Log 6) / 0.55 m std (Log 7)
- **Interpretation:** ECS-DoT holds its altitude reference ~3× tighter; attributable to controller design, not operating speed

**Path Repeatability (Speed-Independent):**
- ECS-DoT: 5 loops closely overlaid; tight, repeatable rounded square
- BST: Greater loop-to-loop variation; drift, particularly along northern leg
- Likely cause: Wind-correction behavior differences (not determined in this analysis)

**Yaw Control Quality (Speed-Independent):**
- Both controllers: Smooth, regular yaw ramps with no hunting or oscillation
- ECS-DoT yaw-rate distribution: Shorter high-rate tail (95th percentile 4.20–5.33 °/s vs 5.90–6.40 °/s for BST)

**Flight Success Rates:**
- Log 4 & 5 (ECS-DoT 4.0 m/s): Both failed early (1.5–2.5 legs), required safety pilot recovery
- Log 6: ECS-DoT 5 full loops (primary dataset), BST 5 full loops
- Log 7: ECS-DoT 2.5 loops (initial waypoint-sequencing anomaly, then resumed), BST 5 full loops (middle 2 used for comparison)
- Log 8: ECS-DoT early failures at 4.5 m/s, BST 5 full loops

## Notable Details

**Methodology Strengths:**
- Analysis window isolated by longest contiguous cruise (ground speed >2.50 m/s) to exclude takeoff, landing, turnaround transients
- Identical analysis criteria applied to both controllers
- Turn/straight segmentation: 12.0 °/s heading-rate threshold applied uniformly
- Efficiency metric: GPS ground-track distance / battery energy consumed (mm/J units)
- Loop detection: Geometric bearing sweep method around pattern center

**Role of Speed in Results:**
- The report explicitly acknowledges that a "substantial part" of whole-cruise and per-corner gains is attributable to ECS-DoT operating at higher cruise speeds
- When speed-normalized, controller-only contribution to efficiency ratio is smaller than headline numbers suggest
- **Critical caveat:** Altitude-hold and path-repeatability results are speed-independent and directly attributable to controller design
- Recommendation: Efficiency gains should be reported alongside measured speeds; not framed as speed-independent

**Test Limitations:**
- ECS-DoT controllers at 4.9–5.0 m/s targets not flown due to increasing gusty wind conditions and low-altitude pattern turbulence sensitivity
- Upper-speed ECS-DoT envelope remains uncharacterized
- Log 7 ECS-DoT profile incomplete (2.5 loops vs. 5 for BST baseline)
- Log 8 ECS-DoT attempts all failed

**Operational Observations:**
- Early ECS-DoT failures (Logs 4–5) at 4.0 m/s suggest controller robustness issues at higher speeds or in gustier conditions
- Waypoint-sequencing anomaly in Log 7 Flight 3 (direct-to-WP32) indicates potential navigation logic issue at higher speeds
- Safety pilot recovery required for early failures; no autonomous recovery observed

**Data Quality:**
- All five successful loops in Log 6 complete and usable
- Telemetry includes cumulative watt-hour battery counter, GPS ground-track position, attitude quaternion (yaw), vertical rate, heading rate, ground speed
- Altitude data: Both MSL and AGL available; analyzed separately per controller reference frame

**Weather/Environmental:**
- Test site: 1534.06 m ground elevation (Colorado, Denver area)
- Conditions: Increasingly gusty winds restricted higher-speed testing; wind-correction behavior differences between controllers noted but not analyzed