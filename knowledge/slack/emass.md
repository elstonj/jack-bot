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

**Activity Level:** Ongoing active project spanning November 2025 - May 2026+. Real flight testing commenced April 23-24, 2026. EMASS media release planned for first week of May creating hard deadline. Project entering critical phase with emerging concerns about EMASS controller performance specifications and fundamental ML model training approach.

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

**May 11, 2026:**
- Dan Prendergast planned to share E2 autopilot PID gains with EMASS during evening meeting (with Maciej's approval after clarifying the cascading nature of the gains: roll/pitch Kp=8, yaw Kp=1.5 are angle-to-rate converters only, with separate rate PIDs handling actual control)
- Jack Elston cautioned against sharing implementation details beyond XML parameters, citing ongoing IP protection negotiations with EMASS
- **Fundamental concern surfaced:** EMASS ML model likely not ingesting telemetry data at sufficient rate or with correct signal composition to properly train for path navigation. Dan Prendergast identified multiple potential issues:
  - EMASS cost function appears to lack trajectory-following terms despite recent addition of next waypoint lat/lon/alt to input vector (~2 weeks prior)
  - Telemetry rate mismatch: some signals arriving at EMASS significantly slower than BST autopilot operates
  - EMASS controller update rate may be too low to recover from aircraft state divergence
  - EMASS team may lack expertise to properly structure cost function for navigation task
- Jack Elston recommended reverting to simplest possible validation: pure hover performance, then simple velocity tracking, rather than attempting full waypoint-based path navigation
- Dan Prendergast disagreed: hovering was never the original intent; fundamental issues with EMASS model training architecture would manifest equally in hover as in path following

## Projects & Initiatives

### EMASS Integration (Primary)
**Status:** Real flight testing completed initial test set with mixed results. Follow-up test flights executed in degraded controller mode to collect efficiency data. Critical emerging concern regarding EMASS controller specifications and ML model training approach. Invoice processing ongoing with EMASS team. Project entering decision point regarding viability of EMASS ML model with current architecture.

**Current Critical Issues (as of May 11):**
1. **ML Model Training Deficiencies:**
   - EMASS model may not be properly ingesting trajectory/navigation information despite receiving waypoint data
   - Cost function structure unclear regarding whether it includes trajectory-following objectives
   - Telemetry data rate to EMASS significantly slower than BST autopilot operation rate
   - Model may be fundamentally incapable of waypoint-based path navigation as currently implemented

2. **Controller Specification Uncertainty:**
   - Update rate potentially reduced from 75Hz to 14Hz (flagged May 4 as insufficient for flight control)
   - Repeated specification changes from EMASS team raising confidence concerns

**Scope:**
- Integrate EMASS's ECS-DoT evaluation board (AI chip with ML controller) onto E2 platform
- Develop interface between EMASS hardware and E2 autopilot
- Create simulation environment (Gazebo-based SWIL) for validation
- Conduct flight testing with comparative analysis (controller on/off)
- Timeline: Originally January-March 2026, pushed to March 11, 2026; further delays occurred due to EMASS team responsiveness and BS