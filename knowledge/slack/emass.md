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
- U0151201DMY (infrastructure/web portal team member)
- U01511MEQ90 (infrastructure/GCS software support)

**Activity Level:** Ongoing active project spanning November 2025 - May 2026+. Real flight testing commenced April 23-24, 2026. EMASS media release planned for first week of May creating hard deadline. Project in critical evaluation phase following flight test results revealing fundamental navigation deficiencies and control stability issues.

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

**May 21, 2026:**
- **Critical Assessment Completed:** Latest EMASS controller version flies safely and reliably in simulation (only one speed limit violation over 15-minute run), but demonstrates fundamental navigation failure in actual flight:
  - E2 remains in same yaw orientation throughout square pattern instead of rotating to face each leg
  - After 1.5 loops, aircraft breaks off west-to-east leg and heads north without triggering limit violations
  - Multiple controller stop/restart cycles required to regain navigation around pattern
- Dan Prendergast scheduled meeting with EMASS team (May 22) to discuss results and determine viability
- **Open Question on Continued Flight Testing:** Dan Prendergast anticipated EMASS may question willingness to fly controller despite navigation failures; acknowledged EMASS likely won't want continued flights as current data is not meaningful for model improvement
- **Jack Elston Position:** Willing to continue flying; noted yaw heading immaterial to efficiency (controller's lack of rotation actually saves energy), but acknowledged mission requirements necessitate heading changes for sensor and mission accomplishment
- **Dan Prendergast Response:** Disagreed with Jack's assessment that lack of yaw rotation is acceptable — mission-relevant considerations cannot be ignored

**May 22, 2026:**
- Dan Prendergast inquired about ECSDOT warning message ("Denied send request, still sending last plan") appearing when ECSDOT powered on; Jack Elston confirmed ECSDOT attempting to send flight plan but doing so incorrectly
- **Real