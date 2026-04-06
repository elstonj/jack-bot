# Statement of Work for Black Swift Technologies - Creare Double Eagle Precision Landing Development

## Document Metadata
- Type: Statement of Work (SOW)
- Client/Agency: Creare
- Program/Solicitation: Double Eagle UAS - 2022 VTOL Extension (follow-on development)
- Date: April 1, 2020
- BST Products/Systems Referenced: SwiftPilot autopilot, Double Eagle UAS
- Key Personnel: Jack Elston (last editor)

## Executive Summary
BST will develop and demonstrate precision landing algorithms for the Creare Double Eagle UAS with focus on autonomous landing on surface water vessels. Work includes algorithm development in simulation, integration of avionics into a smaller prototype, and progressive flight testing from stationary platforms through moving platforms to final demonstrations on an unmanned surface vessel.

## Technical Approach

### Precision Landing Algorithm Development
**Sensor Fusion Architecture:**
- Utilizes Kalman filter approach to fuse multiple asynchronous sensor streams
- 6-state estimate of relative position and velocity between aircraft and landing target
- Synchronous controller time updates with asynchronous sensor measurement ingestion
- Provides confidence bounds on estimates for autonomous abort capability

**Sensor Integration Table:**
| Sensor | Rate | Accuracy | Availability |
|--------|------|----------|--------------|
| Onboard GPS | Slow | Medium | Most of the time with possible outages |
| Onboard IMU | Fast | Low | Always |
| Onboard Pressure Altitude | Fast | Medium | Always |
| Landing Platform GPS | Slow | Medium | Long range with occasional outages |
| Relative Position and Velocity | Medium | High | Short range with occasional outages |

**Control Algorithm:**
- Modified version of BST's existing landing algorithm
- PID control for simplicity, accuracy, and robustness
- Includes zeroing of both relative velocity and position at terminal phase
- Wind-adaptive landing orientation planning for high-wind scenarios

**State Machine Implementation:**
- Two-phase landing architecture:
  1. Approach phase: Uses relative GPS positioning to bring aircraft within range of relative navigation system
  2. Terminal landing phase: Uses full sensor suite for final guidance
- Emergency abort mode for sensor/tracking errors exceeding thresholds

### Avionics Integration & Flight Testing
- Integration of relative positioning system into SwiftPilot avionics (electrical and software interfaces)
- Iterative approach combining extensive simulation validation with flight testing and post-flight analysis
- Progressive testing sequence from stationary to moving platforms in varying wind conditions

## Products & Capabilities Described

### SwiftPilot Autopilot
- BST's existing autopilot system for Double Eagle UAS
- Modifications required: (1) onboard sensor fusion of relative positioning/velocity, (2) new landing controller with target tracking, (3) state machine updates, (4) user interface updates
- Capable of running Kalman filter time updates synchronously while ingesting asynchronous measurements

### Double Eagle UAS
- Target aircraft for precision landing development
- Creare developing smaller prototype version for safer ship landing testing

## Use Cases & Applications

1. **Stationary Platform Landing** - Baseline precision landing without dynamic elements
2. **Stationary Platform in High Wind** - Demonstrates wind-adaptive landing capabilities
3. **Moving Trailer Landing** - Tests precision landing on mobile ground platform, progressing from calm to medium/high wind conditions
4. **Unmanned Surface Vessel Landing** - Final demonstration landing on water-based moving vessel; 10-day on-site testing period
5. **Ship-based Operations** - Intended for handoff to Creare for operational demonstrations and evaluations

## Work Tasks & Deliverables

**Five Primary Work Tasks:**
1. Precision Landing Algorithm development and simulation demonstration
2. Avionics integration into Creare prototype system with flight testing
3. Precision landing flight tests on stationary platform
4. Testing on moving trailer platform (land-based)
5. Testing on unmanned surface vessel (10-day on-site demonstration)

**Deliverables:**
- Interim and final progress reports for each year of activity
- Integrated and fully functional prototype vehicle with support systems after three-year testing completion
- Handoff of fully operational aircraft to Creare

**Project Management:**
- Joint planning and monitoring with Creare
- Technical progress tracking and expense management
- Participation in joint project meetings

## Notable Details

- **Multi-year project scope:** Work structured over 3 years with progressive testing complexity
- **Robust sensor fusion design:** Specifically addresses real-world challenges of communication interruptions and asynchronous measurements
- **Existing capabilities leveraged:** BST has existing Kalman filter implementations and landing algorithms to build upon
- **Iterative validation approach:** Emphasizes continuous simulation-to-flight-test feedback loop throughout development
- **Safety-focused prototype:** Creare builds smaller prototype version for safer testing before full-scale Double Eagle demonstrations
- **Performance-based acceptance:** Final handoff includes evaluation of algorithm performance on actual water vessel
- **Integration complexity:** Requires electrical and software interface development between relative positioning system and SwiftPilot avionics