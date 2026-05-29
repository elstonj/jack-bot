# #25_1-navy-sbir-magnetometer

## Overview
This channel is focused on Black Swift Technologies' Navy Small Business Innovation Research (SBIR) project for developing magnetometer-equipped aircraft systems. The project involves integrating QuSpin magnetometers with BST's aircraft platforms for magnetic signature detection applications (MAD - Magnetic Anomaly Detection). Key participants include Beck, Maciej, Tyler, Sam Hild, Alex Lomis, Joshua Fromm, and Jack Elston from BST, with external collaboration from QuSpin (Jeff), Ultra Maritime (Paul), Navy DEVCOM (Morris "DeSi"), Navy TPOC (Angel Ruiz-Reyes), and emerging Royal Navy contact Simon. Activity spans from October 2025 through May 2026, covering Phase I completion and Phase II proposal submission, kickoff, and ongoing Option period development with emerging Royal Navy engagement and active flight testing preparation.

## Key Decisions

**October 2025:**
- Magnetometer positioning: Decided to position sensor 2.5-5ft from motor with MuMetal shielding
- Shielding approach: MuMetal encasing around motor with short shaft design
- S0 aircraft modifications: 3x wing area increase to handle 1.3kg payload

**January 2026:**
- Partner selection: Chose Ultra Maritime over CRT as Phase 2 subcontractor
- Sensor approach: Decided on separate aircraft for magnetometer and acoustic sensors (not combined)
- Battery selection: Switch to pouch battery cells to reduce magnetic interference
- Computing: Add Google Coral TPU for compute needs (~2W power vs higher GPU power)

**March 2026:**
- TCE participation: Decided NOT to participate in April TCE due to early development status
- Will plan for August TCE when system is more mature
- Technical approach: Task O.2 will use simulated classified model to avoid SCIF/clearance requirements

**April 2026:**
- Cetacean budget reallocation: Decided to reduce Cetacean's subcontract in the Option period and reallocate ~$10K for other uses, since Cetacean is not continuing in Phase II
- Acoustic component approach: Continuing with separate aircraft for acoustic sensors; Navy requires drone-based solution for Phase II
- CRT subcontract closure: CRT has invoiced only ~$2K of their Base Period allocation; remaining $8.5K plus all option funds available for reallocation (April 20, 2026)
- August Camp Pendleton demo: Confirmed as primary Option focus; will reallocate CRT funds for travel and demo costs (April 20-21, 2026)
- Reusable MAD S0 design: Decided to use stock S0 with smaller commercial LiPo battery, new antenna, and launch rail rather than hand-launch variant (April 22, 2026)
- Landing gear: Fixed spline (vs wing swivel), small wing tip skids to keep wings level on landing (April 22, 2026)
- Launcher development: Deferred CAD/explosive launch development to Phase II; focus Option period on manual hand-throw launch from UH-60 (April 21, 2026)
- Future launcher approach: Estes rocket assist identified as solution for boat/vehicle-based launches; tube-launched system for non-recoverable boat-based deployment (April 23, 2026)

**May 2026:**
- S0-MAD Reusable flight article: Decided to reuse as many parts as possible from the ADONIS S0 for the reusable MAD S0 flight article rather than building a new aircraft (May 6, 2026)
- Ground test rig: Bartington sensor successfully integrated mechanically into ground test rig (May 6, 2026)
- Bartington logging approach: CSV format output selected for Bartington sensor data logging (May 27, 2026)
- Flight test methodology: 1-hour test of each logger deemed sufficient to satisfy Navy TPOC Angel Ruiz-Reyes requirements (May 27, 2026)
- **Bartington sensor test configuration (May 28, 2026):** Confirmed sequential 1-hour test runs for each sensor (Bartington and QuSpin) with aircraft off, planned as initial baseline validation

## Projects & Initiatives

**Phase I (Completed January 2026):**
- Status: Final Report and TABA successfully submitted January 11-12, 2026
- Payments: Final $20k payment received
- Technical achievements: Magnetic noise target of ~30 pT RMS (half Navy requirement of 3 pT/sqrt(Hz))

**Phase II (April 2026 - ongoing):**
- Budget: $1.4M over 30 months
- Proposal submitted March 27, 2026 (one day extension)
- Contract signed March 25th, option start date April 12, 2026
- Planned: 4 experimentation events, 6 S0-AD aircraft (4 base + 2 option)
- Phase II kickoff meeting completed April 21, 2026 with TPOC Angel Ruiz-Reyes
- Kickoff brief submitted April 14, 2026
- **Status Update (May 8, 2026):** Informal indication received that Phase II award appears likely based on "rumblings" from Navy contacts (not yet official)

**Phase II Option Period (August 2026 - focus area):**
- Status: Task modifications approved by Navy on April 21, 2026
- Primary objective: August 17-28 Camp Pendleton demo (confirmed schedule from Morris "DeSi" DEVCOM)
- Navy will provide test "objectives" (sea mines/land mines) for both water and land detection
- Demo audience: Marine groups interested in fixed-wing MAD options (currently use quads that are too slow or easy to shoot down)
- Deliverable: Reusable hand-launched S0 analog for local testing and Marine use case
- Navy will primarily launch from UH-60 helicopters
- **Local mag flights: Scheduled for July 1st, 2026** (May 6, 2026) with Bartington sensor testing

**Technical Development (May 2026 - ongoing):**
- Reusable MAD S0 configuration:
  - Stock S0 airframe with lighter weight operation
  - Smaller commercial LiPo battery (30-45 minutes TOF target)
  - New antenna to reduce landing damage
  - Launch rail for deployment
  - Fixed spline wing attachment (vs swivel)
  - Small skids on wing tips for level landing and anti-grab
  - SF20/C half-size laser rangefinder for landing (proven reliable from prior use)
  - Parts sourced from ADONIS S0 where possible to minimize new construction
- Ground testing: Bartington sensor mechanically integrated into ground test rig as of May 6, 2026
- **Launcher development:** Design phase (targeted completion during week of May 12-16, 2026 per Alex Lomis); parts ordering planned for June 15, 2026 to allow iteration before July 1st local mag flights
- **Bartington sensor logging:** Dronecan logging program being updated to support Bartington sensor with dynamic memory allocation (Sam Hild working on this); CSV format logging confirmed working as of May 27, 2026
- Status as of May 6, 2026: Team transitioning from S0-VTOL bug work to SBIR task prioritization
- **Flight test baseline validation (May 28, 2026):** Initial field testing completed with 1-hour sequential test runs for both Bartington and QuSpin loggers; photographic documentation captured for experimental setup

**Royal Navy Engagement (May 2026 - active):**
- Contact: Simon (Royal Navy contact), confirmed as program lead with secured funding as of May 21, 2026
- Project codename: **RAVEN** (Royal Navy designation)
  - **RAVEN-M:** Magnetic Anomaly Detection (MAD) - aligned with US Navy, first priority payload
  - **RAVEN-ISR:** Intelligence/Surveillance/Reconnaissance variant
  - **RAVEN-J:** UK-specific payload with potential classification restrictions (F2F discussion needed)
- Funding status: Simon has received funding; decision on which spirals to pursue TBD (likely single spiral focus due to budget constraints)
- Priority alignment: First choice is MAD payload (RAVEN-M), aligned with US SBIR effort
- Internal status: Jack Elston drafting initial response