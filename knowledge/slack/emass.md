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
- Nikhila (external, ML model training and bench-test app development)
- Moe (EMASS contact)
- Alex Lomis (flight operations/coordination)
- Meredith Needham (finance/invoicing)
- U0151201DMY (appears to be infrastructure/web portal team member)

**Activity Level:** Ongoing active project spanning November 2025 - May 2026+. Real flight testing commenced April 23-24, 2026. EMASS media release planned for first week of May creating hard deadline. Project entering critical phase with emerging concerns about EMASS controller performance specifications.

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
- **April 13-15:** Multiple firmware updates and GCS fixes deployed by Jack Elston to resolve communication issues; HWIL testing actively underway
- **April 16:** Weather assessment indicates Monday/Tuesday (April 21-22) suitable for E2 flight testing with EMASS payload
- **April 20-22:** GitLab project created (`blackswifttechnologies/emass-test`) for managing test software and binaries instead of passing zip files
- **April 22:** Committed to real-time debugging meeting with Nikhila and Moe (EMASS team) morning of April 23 (9-10am or flexible time) to troubleshoot command transmission issues; EMASS team willing to work flexible hours due to timezone/deadline pressure
- **April 23:** Flight testing plan approved with four flights per battery using two patterns (Easy Pattern and Dynamic Pattern from emass2.xml); testing with EMASS controller on/off for each pattern to enable comparative analysis. Jack Elston's proposal to test BST autopilot first on each pattern (to validate baseline), then EMASS controller, approved by Dan Prendergast. Additional flight test sets planned for the following week.
- **April 27:** Dan Prendergast decided not to proceed with afternoon data collection flight due to continued ECSDOT connectivity issues and control violations (VRATE and ROLL_ANGLE limit violations persisting). Decision made with assumption that Moe indicated data collection flights are for fine-tuning EMASS control model only. EMASS received 2nd invoice and are processing it. EMASS inquired about extending number of flights if necessary — decision pending on whether to establish cost per additional flight set.
- **April 28:** Dan Prendergast confirmed willingness to fly EMASS controller in "degraded" operational mode: reliable straight-line performance with controller restart required at each waypoint/corner transition. Intent is to collect actual flight data for efficiency performance on straight legs and model tuning. Jack Elston approved with caution: monitor limit violations closely, immediate landing if violations approach severity of 2nd flight test attempt, and immediate data sharing with EMASS team for review.

**May 4, 2026:**
- Moe (EMASS) indicated controller update/specification change under discussion: update rate potentially reduced from 75Hz to 14Hz during recent meeting with Dan Prendergast. Jack Elston flagged critical concern: 14Hz update rate is insufficient for disturbance rejection in real flight operations and unlikely to work despite potentially functioning in simulation. Maciej expressed skepticism about repeated specification reductions from EMASS team.

## Projects & Initiatives

### EMASS Integration (Primary)
**Status:** Real flight testing completed initial test set with mixed results. Follow-up test flights executed in degraded controller mode to collect efficiency data. Significant concern emerging regarding EMASS controller specifications—potential reduction from 75Hz to 14Hz update rate flagged as inadequate for flight control. Invoice processing ongoing with EMASS team.

**Scope:**
- Integrate EMASS's ECS-DoT evaluation board (AI chip with ML controller) onto E2 platform
- Develop interface between EMASS hardware and E2 autopilot
- Create simulation environment (Gazebo-based SWIL) for validation
- Conduct flight testing with comparative analysis (controller on/off)
- Timeline: Originally January-March 2026, pushed to March 11, 2026; further delays occurred due to EMASS team responsiveness and BST resource conflicts; HWIL testing active as of mid-April; bench testing on E2 platform started April 21-22; real flights commenced April 23-24, 2026; three total flight test sets planned (one completed, two in progress as of May 4)

**Technical Components:**

1. **Hardware Integration:**
   - Custom mount for AI board on E2
   - UART interface with level translation (3.3V to 5V)
   - Power delivery through 5V barrel connector
   - Magnetometer calibration adjustments after battery relocation
   - ECS-DoT eval board communication via two devices (UART and JTAG connections)
   - Serial connection options: DB9 connector or jumpers + USB microUSB (preferred per Jack Elston as of April 22)
   - Baud rate: 460800 bps (verified working April 22)
   - **Issue (April 27-28):** DB9 payload connector connectivity problems persist; USB microUSB alternative appears more reliable

2. **Firmware/Software (As of May 4):**
   - Autopilot modifications to accept EMASS actuator commands at 75Hz via UART (subject to change pending controller specification revision)
   - Two-mode operation: EMASS control or BST autopilot control (no blending)
   - EXTERNAL mode in autopilot for payload authority handoff
   - Protections to automatically revert to BST control on failure/timeout
   - Headless testing framework with pass/fail criteria
   - Serial baud rate adjustable through tablet interface (baud rate changes must be made via tablet, not command line)
   - Parameter synchronization via `param_mr_0x41000002.bst` file (safety limits enforced, model tuning allowed)
   - Recent updates (April 20-22):
     - Jack Elston added logging to capture state machine transitions and rates
     - Telemetry adjustments to ensure timing requirements met
     - New autopilot binary pushed April 22 with improved connection debugging
     - Binary version: 0x358094b (per Maciej April 21)
     - Fixes to bench-test and full