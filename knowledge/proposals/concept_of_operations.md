# Terrain Following Obstacle Avoidance Concept of Operations

## Document Metadata
- Type: Concept of Operations (ConOps)
- Client/Agency: NASA
- Program/Solicitation: 2018 SBIR Phase I (Terrain Following)
- Date: October 1-8, 2018
- BST Products/Systems Referenced: SwiftCore (implied through SDK and flight control references)
- Key Personnel: Not named in document

## Executive Summary
This ConOps defines autonomous terrain-following and obstacle-avoidance capabilities for a fixed-wing UAS operating in challenging environments including heavy rain, low light, and volcanic plumes. The system will maintain autonomous altitude control relative to terrain while detecting and evading obstacles through a discrete set of response controllers with minimal flight plan deviation.

## Technical Approach

**Terrain Following Architecture:**
- Flight plans generated pre-mission using SRTM data or high-resolution photogrammetry maps
- Plans specified in above-ground-level (AGL) with conversion to absolute altitude commands
- Aircraft maintains running estimate of true ground height and AGL
- Two operational modes:
  - **Normal Mode**: Aircraft autonomously reacts if estimated AGL falls below safety threshold
  - **Terrain Following Mode**: Aircraft controls altitude on true AGL command using AGL estimates

**Obstacle Avoidance Logic:**
- Real-time sensor measurements of obstacles within flight path
- Threat assessment relative to aircraft projected flight path
- Obstacles evaluated against safety bounds
- Aircraft selects minimal-deviation response from discrete controller set
- Running obstacle map maintained for immediate region ahead; obstacles outside field of regard discarded
- Previously-flagged waypoints noted but individual obstacles not tracked

**Response Controllers (in priority/expected frequency order):**
1. **Climb Out** (expected primary response): Standard climb (minimal throttle change) or aggressive climb (throttle increase) for low obstacles (vegetation, small structures)
2. **Dive Out** (less common): Standard or aggressive descent for obstacles aircraft cannot climb over (bridges, power lines)
3. **Flap Jump** (last resort): Aggressive maneuver deploying flaps to rapidly gain altitude and drop airspeed for very close detections (large rocks, small trees)
4. **Turn Out**: Standard or aggressive turn radius for obstacles higher than climb capability or with insufficient detection time (utility poles, wind turbines, large structures, cliff walls)
5. **Bail Out**: Return to home waypoint or safety waypoint if obstacle avoidance engaged too frequently; triggered by response frequency thresholds or aggressive response count

**Control Integration:**
- SwiftCore SDK enables external controller interaction through flight path angle (climb/descent) and turn rate commands (roll maneuvers) as primary control interface

## Products & Capabilities Described

**SwiftCore Flight Control System:**
- Autonomous altitude control relative to terrain
- Real-time ground height estimation
- Integration point for external obstacle avoidance controllers
- Command interface: flight path angle and turn rate/roll maneuver commands
- Supports discrete response controller selection and execution

## Use Cases & Applications
- Arctic operations
- Volcanic plume sampling (50% sensor performance degradation requirement)
- Low-altitude terrain-following missions in GPS-denied or challenging environments
- All-weather operations (heavy rain, light snow conditions)
- Day/night operations (degraded passive optical sensor performance in low light)

## Project Requirements

| Requirement | Specification | Notes |
|---|---|---|
| Aircraft Type | Fixed-wing UAS | |
| Weather | Heavy rain, light snow | All-weather capability |
| Wind Speed (sustained) | ≤10 m/s | |
| Volcanic Plume Operation | 50% sensor performance reduction acceptable | |
| Obstacle Detection Rate (critical) | 99.999% | Marked as "stand-in" value |
| Obstacle Avoidance Distance | 10 m | Marked as "stand-in" value |
| Maximum Altitude | 4,267 m AGL | Above sea level |
| Minimum Altitude | 15 m AGL | Above ground level |
| Visibility | Daytime: full sensor performance; Low light: degraded passive optical sensor performance | |

## Notable Details

**Scope Limitations for Phase I:**
- Flight plan feasibility checking and auto-generation out of scope
- Plans assumed feasible from both obstacle and aerodynamics standpoints pre-mission

**Sensor Strategy:**
- Obstacle list and required sensor types to be compiled during effort
- Sensor suite design goal: maximize detection time for aircraft response
- Multi-sensor approach necessary to detect diverse obstacle types (vegetation, structures, rocks, natural features)

**Design Assumptions:**
- Feasible flight plan provided; frequent obstacle avoidance engagement indicates need for flight plan review/adjustment
- Climb out expected to be "far and away the more common reaction"
- Flap jump maneuver reserved for last-resort scenarios where obstacle detection occurs too late
- Controllers designed with both standard (conservative) and aggressive variants

**Integration Approach:**
- Modular controller design allowing selection of appropriate response type
- Flag-based engagement tracking to trigger bail-out decision