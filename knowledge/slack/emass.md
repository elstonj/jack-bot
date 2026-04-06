# #emass

## Overview
Channel for coordination of the EMASS (machine learning AI chip) integration project with Black Swift Technologies. The project involves integrating EMASS's custom AI hardware and ML-based flight controller onto the E2 aerial platform to evaluate potential improvements in flight efficiency and endurance.

**Key Participants:**
- Dan Prendergast (project lead, primary point of contact)
- Jack Elston (software/firmware engineer)
- Ethan Domagala (hardware integration)
- Maciej (controls/simulation)
- Beck Cotter (proposals/planning)
- Scott and Mark (CEO) from EMASS (external partner)
- Nikhila (external, ML model training)

**Activity Level:** Ongoing active project spanning November 2025 - April 2026, with increasing intensity as hardware integration progressed. Activity continues into early April 2026.

## Key Decisions

**November 2025:**
- Beck Cotter created initial kickoff presentation based on proposal
- Clarified task division: EMASS would run simulators and AI training; BST would provide aerodynamic models and E2 parameters
- Dan Prendergast noted in proposal that any BST simulations would be low-res, for safety only, not proof of EMASS chip efficacy

**January 2026:**
- Project completion date pushed to March 11, 2026
- Jack Elston identified interface freeze as critical milestone to prevent firmware/AI scope creep
- Agreed to emphasize need for stable interfaces early, demo-focused success criteria, and fast turnaround on decisions
- Performance expectations reset: EMASS initially claimed 40-85% improvement (deemed "delusional"), Scott later agreed to target 30%, BST set realistic expectation of 10-15%

**February 2026:**
- Ethan Domagala completed mount and interface cable; identified voltage mismatch (3.3V UART input vs 5V output) requiring level translator
- Jack Elston provided level shifter solution
- Created external EMASS-BST Slack channel for coordination

**March 2026:**
- Decided on full control handoff model: EMASS controller operates at 75Hz with full actuator authority or BST autopilot operates at 250Hz; no mixed control
- Pitch/roll/yaw angle commands chosen as safe outer control loop (not rates) for EMASS to command
- Jack Elston completed major sim architecture rework with headless testing mode and dual socket architecture (payload port 55551, GCS port 55555)

**April 2026:**
- Ordered Pico 2 with headers for new hardware requirement from EMASS

## Projects & Initiatives

### EMASS Integration (Primary)
**Status:** Active hardware/software integration phase as of April 2026

**Scope:**
- Integrate EMASS's ECS-DoT evaluation board (AI chip with ML controller) onto E2 platform
- Develop interface between EMASS hardware and E2 autopilot
- Create simulation environment (Gazebo-based SWIL) for validation
- Conduct flight testing with comparative analysis (controller on/off)
- Timeline: Originally January-March 2026, pushed to March 11, 2026; further delays occurred due to EMASS team responsiveness and BST resource conflicts

**Technical Components:**
1. **Hardware Integration:**
   - Custom mount for AI board on E2
   - UART interface with level translation (3.3V to 5V)
   - Power delivery through 5V barrel connector
   - Magnetometer calibration adjustments after battery relocation

2. **Firmware/Software:**
   - Autopilot modifications to accept EMASS actuator commands at 75Hz via UART
   - Two-mode operation: EMASS control or BST autopilot control (no blending)
   - EXTERNAL mode in autopilot for payload authority handoff
   - Protections to automatically revert to BST control on failure/timeout
   - Headless testing framework with pass/fail criteria

3. **Simulation:**
   - Gazebo SWIL with realistic E2 dynamics
   - Current model implementation (with power consumption calculations)
   - Support for headless automated testing
   - Trajectory replay capability

**Known Challenges:**
- EMASS team organization/responsiveness (especially Nikhila for ML model retraining)
- Schedule conflicts with other BST projects (ADONIS, USGS, hurricane)
- Integrator wind-up issues in simulator
- Plugin loading issues in simulation environment
- Voltage interface compatibility between hardware
- Scope creep pressure (mixed control requests, additional output formats)
- Financial/budgetary considerations emerging (April 6, 2026)

## Action Items & Commitments

**Outstanding (as of April 6, 2026):**
- Nikhila (EMASS) to retrain ML model with E2 flight data containing EMASS payload (as of March 8, no update received yet)
- Dan Prendergast to order Pico 2 with headers for EMASS's new hardware requirement
- EMASS team to: define flight plan, run scenario in simulation with hardware, freeze HW/SW interface specifications
- Jack Elston to work on HWIL interface for EMASS hardware (pending return from Florida)
- **Jack Elston: Financial follow-up/review (flagged April 6, 2026)**

**Completed:**
- Beck Cotter: Kickoff deck creation (Nov 2025)
- Dan Prendergast: E2 Gazebo model files shared with EMASS; magnetometer calibration file updates (Feb-Mar 2026)
- Ethan Domagala: Mount and interface cable design with level shifter (Feb 2026)
- Jack Elston: SDK telemetry modifications, dual-socket architecture, headless test framework, autopilot binary rebuild with EMASS flags (Mar 2026)
- Maciej: Current/thrust model implementation in Gazebo (Mar 2026); test script execution (Mar 2026)

**In Progress:**
- Dan Prendergast: Meeting EMASS on schedule and scope resets; preparing simulation tarball for external team
- Jack Elston: HWIL integration, autonomy report (higher priority), financial review
- Maciej: Simulation environment debugging (plugin loading)

## Client & External References

**EMASS Inc.:**
- Mark: CEO
- Scott: Primary contact from EMASS (senior, appears to be operations/management)
- Nikhila: ML model training engineer (remote, communication challenges)
- ECS-DoT evaluation board: Custom AI accelerator chip with onboard ML model for flight control

**Internal Cross-Projects Affecting Schedule:**
- ADONIS project
- USGS project  
- Hurricane project

**Flight Test Locations Mentioned:**
- Pepper Jack (previous flight test site with E2)
- Crested Butte (previous flight test site with E2)
- Florida (Jack Elston travel for unrelated work)

## Recurring Topics & Themes

1. **Scope Creep & Interface Clarity:** Repeated emphasis on need for frozen interface specifications, clear task boundaries, and resistance to expanded control formats (pitch/roll/yaw + vertical rate mixing)

2. **Communication/Responsiveness Challenges:** Frustration with EMASS team's organization and response times, particularly Nikhila. Dan noted need for Scott to manage expectations within EMASS technical team.

3. **Schedule Pressure:** Repeated pushback and reprioritization as project competed with other BST initiatives and EMASS delays

4. **Performance Expectations Management:** Ongoing discussion about realistic vs. optimistic improvement metrics (40-85% claimed → 30% target → 10-15% realistic)

5. **Technical Integration Hurdles:** Serial problems discovered during integration (voltage compatibility, integrator wind-up, plugin failures, control mode conflicts)

6. **Simulation Validation:** Emphasis that EMASS team must validate their approach in simulation before hardware testing to avoid wasting BST resources

7. **Financial/Budget Considerations:** Emerging concern about project finances (flagged April 6, 2026)

## Important Resources

**Shared Documents/Repositories:**
- Kickoff Presentation: https://docs.google.com/presentation/d/1Z5SP3Y6aqCO91LTuliNUwj_8Z62CY8d_QILv-DaVHCo/edit?usp=drive_link
- Project Tracking (Asana): https://app.asana.com/1/