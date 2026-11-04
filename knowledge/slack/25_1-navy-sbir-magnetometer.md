# #25_1-navy-sbir-magnetometer

## Overview
This channel is focused on Black Swift Technologies' Navy Small Business Innovation Research (SBIR) project for developing magnetometer-equipped aircraft systems. The project involves integrating QuSpin and Bartington magnetometers with BST's aircraft platforms for magnetic signature detection applications (MAD - Magnetic Anomaly Detection). Key participants include Beck Cotter, Maciej, Tyler, Sam Hild, Alex Lomis, Joshua Fromm, Jack Elston, Spencer Hoehl, and Ethan Domagala from BST, with external collaboration from QuSpin (Jeff), Ultra Maritime (Paul), Navy DEVCOM (Morris "DeSi"), Navy TPOC (Angel Ruiz-Reyes), Navy personnel (Tony, Daniel Klier, Aaron Pyrah, Derek), Royal Navy contact Simon, Lockheed Martin UK (LMUK), Dan Prendergast, and external consultant Eric Correa. Activity spans from October 2025 through November 2026, covering Phase I completion, Phase II proposal submission and kickoff, Option period development with flight testing preparation, sensor optimization work, TCE (Technology Concept Experimentation) event participation at Camp Pendleton (September 14-24), on-site testing and TAK integration with Navy personnel, post-TCE reporting and meeting preparation, UK Navy RAVEN program contract finalization and kickoff (November 2026), and Arctic Edge 2027 participation planning (April 19-May 7, Alaska). Recent activity (late October-early November 2026) focuses on PCLT integration testing completion, altitude optimization for S0 drops, UK RAVEN project kickoff presentation finalization, site visit preparation with UK Navy and LMUK, operational security regarding SOCOM program integration, and simulator system preparation for UK delegation visit. Most recent updates (November 3, 2026) involve final site visit logistics coordination and presentation refinement.

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
- TCE participation: Decided NOT to participate in April TCE due to early development status; planning for August TCE when system is more mature
- Technical approach: Task O.2 will use simulated classified model to avoid SCIF/clearance requirements

**April 2026:**
- Cetacean budget reallocation: Reduce Cetacean's subcontract in Option period and reallocate ~$10K for other uses, since Cetacean not continuing in Phase II (April 20, 2026)
- Acoustic component approach: Continuing with separate aircraft for acoustic sensors; Navy requires drone-based solution for Phase II
- CRT subcontract closure: CRT has invoiced only ~$2K of their Base Period allocation; remaining $8.5K plus all option funds available for reallocation (April 20, 2026)
- August Camp Pendleton demo: Confirmed as primary Option focus; will reallocate CRT funds for travel and demo costs (April 20-21, 2026)
- Reusable MAD S0 design: Decided to use stock S0 with smaller commercial LiPo battery, new antenna, and launch rail rather than hand-launch variant (April 22, 2026)
- Landing gear: Fixed spline (vs wing swivel), small wing tip skids to keep wings level on landing (April 22, 2026)
- Launcher development: Deferred CAD/explosive launch development to Phase II; focus Option period on manual hand-throw launch from UH-60 (April 21, 2026)
- Future launcher approach: Estes rocket assist identified as solution for boat/vehicle-based launches; tube-launched system for non-recoverable boat-based deployment (April 23, 2026)

**May 2026:**
- S0-MAD Reusable flight article: Reuse as many parts as possible from the ADONIS S0 rather than building a new aircraft (May 6, 2026)
- Ground test rig: Bartington sensor successfully integrated mechanically (May 6, 2026)
- Bartington logging approach: CSV format output selected for sensor data logging (May 27, 2026)
- Flight test methodology: 1-hour test of each logger deemed sufficient to satisfy Navy TPOC Angel Ruiz-Reyes requirements (May 27, 2026)
- Bartington sensor test configuration: Sequential 1-hour test runs for each sensor (Bartington and QuSpin) with aircraft off, planned as initial baseline validation (May 28, 2026)
- QuSpin filter configuration: Decision pending on 10Hz low-pass filter enablement for next test week; need to verify custom filter options available in QuSpin profile loading feature per Jeff (May 29, 2026)

**June 2026:**
- Electrical integration investigation: Potential source of increased magnetic noise identified—magnetometer now electrically connected to aircraft powered by aircraft regulator (vs. previous independent USB battery) and integration of carbon boom (June 1, 2026)
- Bartington sensor power isolation strategy: Decision to use isolated supply/comms for Bartington sensor due to extreme susceptibility to electronic noise (requires <1mV ripple on power supply) (June 2, 2026)
- ADC selection: Decided to pursue 24-bit ADC (or dual 24-bit ADCs interfaced via I2C) to achieve 1μV resolution required for Bartington sensor logging (June 2, 2026)
- Custom PCB approach: Agreed to design quick-turn PCB for isolated power supply and high-resolution ADC integration rather than using breakout boards (June 2, 2026)
- Eric Correa follow-up coordination: Maciej flagged need for team to reach out to Eric Correa with any remaining questions before his leave (June 3, 2026) - he is off duty after June 4th for a couple of weeks
- ADONIS S0 radio specification: Clarified that the S0 aircraft being used from ADONIS for flight testing uses a 430 radio (Microhard type to be confirmed) (June 4, 2026)
- Deployment tube checklist: Sam Hild to update and send deployment tube checklist for approval; Jack Elston requesting schematic review from Sam Hild (June 5, 2026)
- Custom PCB design fixes: Sam Hild fixed ADC 3.3V supply connection issue (U1 pin 26, C2+C4 isolation in inner copper) and JP1 jumper wiring; updates pushed and board ordered (June 9, 2026)
- QuSpin power isolation approach: Maciej requesting similar isolated power setup for QuSpin sensor as developed for Bartington to restore sensor accuracy from earlier performance (June 10, 2026)
- QuSpin power supply testing: Maciej to take over testing of QuSpin power supply while Sam Hild focuses on S3 development; testing focused on verifying noise reduction effectiveness (June 12, 2026)
- Bartington sensor model confirmation: Identified as UAS Mag PC298 with 105 µT range (June 16, 2026)
- Launcher parts procurement: Approved ordering launcher design parts totaling $1.3K from McMaster (June 22, 2026)
- Magnetometer power supply: Sam Hild identified that magnetometer draws ~1A at 5V (higher than expected); current LDO is 500mA max and causing under-voltage/current condition preventing output. Maciej requested quick-turn procurement of higher-capacity LDO; Sam Hild to check existing inventory first (June 23, 2026)
- TCE event dates: Originally planned for August 17-28, rescheduled to September 14-24 at Camp Pendleton (June 29, 2026)

**July 2026:**
- QuSpin firmware update approach: Decided to send QuSpin sensor back to manufacturer for firmware update and QC check rather than conducting testing in current "noisy mode" (July 7-8, 2026). Rationale: Quick turnaround expected from vendor for firmware update and configuration optimization, preferable to testing with known suboptimal settings

**October 2026:**
- Phase II project execution strategy: Acknowledged that Phase II kickoff (if funding approved by January 2027) will require accelerated schedule to meet April/May 2027 drop article readiness deadline (October 23, 2026)
- Contingency ocean testing: Discussed possibility of conducting team-funded ocean testing trip to validate magnetic sensing performance over water (versus land testing) if project advancement requires validation; explored potential cost-sharing with OOI (Ocean Observatories Initiative) or CAT (Cooperative Autonomous Technologies) testing initiatives (October 23, 2026)
- PCLT deployment integration: Communications verified functional within PCLT (Payload Containment Launch Tube) enclosure; fiberglass tube configuration confirmed as representative of fleet deployment conditions (October 28, 2026)
- S0 deployment conops: Confirmed Navy procedures involve carrying multiple payloads in host aircraft, keeping S0 powered off until final deployment readiness, then powering on and loading into PCLT for deployment (October 28, 2026)
- PCLT EMI paint: Confirmed that operational PCLT units in fleet aircraft would NOT have EMI paint (unlike test unit which had fiberglass only), with no anticipated comms/GPS complications (October 28, 2026)
- S0 drop altitude optimization: Simon (Royal Navy) specified target altitude of <1000ft for drops; Maciej assessed historical data (last 10 S0 drops ranged 1200'-2000') and identified achievable tightening through minimal design changes: sequence speed-up and removal of S0 tube ballast (October 29, 2026)
- UK RAVEN project channel management: Decided to keep all UK Royal Navy/LMUK RAVEN project communications within #25_1-navy-sbir-magnetometer channel rather than creating separate channel (October 29, 2026)

**November 2026:**
- SOCOM program confidentiality: Decision to avoid connecting SOCOM program variants in discussions with UK Navy and LMUK partners; present parallel payload development as work for "another customer" with intentional vagueness regarding specific variant development (November 2, 2026)
- UK RAVEN kickoff presentation scope: Alternate payloads section kept minimal (one slide) for brief marketing awareness rather than extensive technical disclosure (November 2, 2026)
- Google Slides format adoption: Converted UK RAVEN presentation from PowerPoint to Google Slides format for easier collaborative editing and content integration from multiple sources (November 2, 2026)
- Google Slides template best practice: Future slide imports should use "use styles in this presentation" option to maintain theme master slides and allow theme-wide formatting updates (November 3, 2026) - lesson learned from formatting issues during presentation finalization
- Remote meeting integration: Decision to start online meeting in conference room to include remote participants during site visit (November 3, 2026)

## Projects & Initiatives

**Navy SBIR Magnetometer Program (Primary)**
- **Status:** Option period underway; Phase II funding pending (as of November 2026)
- **Phase I:** Completed (concluded October 2025)
- **Option Period:** Active focus on TCE event completion (Camp Pendleton, September 14-24, 2026); transitioned through PCLT integration validation and altitude optimization; now transitioning to Phase II planning with accelerated timeline if funding approved by January 2027
- **Phase II:** Proposed; if funded from January 2027 kickoff, schedule calls for drop article readiness by April-May 2027
- **Key Deliverables:** 
  - Reusable S0-MAD flight article with Bartington and QuSpin magnetometers
  - Launch/recovery systems (manual hand-throw from UH-60 primary; PCLT tube-launched system validated for deployment)
  - Magnetic anomaly detection capability demonstration
  - Custom PCB for isolated power supply and 24-bit ADC for sensor integration
- **Recent Focus (November 2-3, 2026):** UK RAVEN kickoff presentation finalization; simulator system preparation; site visit logistics and agenda finalization for incoming UK delegation; presentation content enhancements including ship ID imagery

**Arctic Edge 2027 Participation** (Emerging)
- **Dates:** April 19-May 7, 2027, Alaska
- **Status:** Planning stage; strategy discussions ongoing (October 2026)
- **Relationship to Phase II:** Potential demonstration opportunity if Phase II funding approved
- **Connection to PCLT Testing:** Recent PCLT validation testing supports readiness for Arctic Edge deployment scenarios

**UK Navy RAVEN Program (with LMUK)** (Active Execution Phase)
- **Status:** Commercial approval received October 25, 2026; contract moving to formal execution phase; kickoff presentation finalized November 2-3, 2026; site visit with UK Navy and LMUK delegation imminent (week of November 2-6, 2026)
- **Participants:** Lockheed Martin UK (LMUK), Simon (Royal Navy contact), Dan Prendergast (program coordination), Beck Cotter (logistics), Jack Elston (comms & spectrum lead), Spencer Hoehl (simulator and flight safety lead), Maciej, and BST team
- **Technical Requirements:** 
  - Altitude specification <1000ft for drops (per Simon, October 29, 2026)
  - Payload development variants (with SOCOM integration intentionally undisclosed to UK partners)
- **Key Milestones:** 
  - Commercial approval achieved (October 25, 2026)
  - Kickoff presentation finalized (November 2-3, 2026)
  - Site visit agenda finalized (November 2, 2026); updated content on slides 2 and 32 of RAVEN presentation
  - Jack Elston: Lead Wed 10-12 discussions on comms & spectrum, Merlin integration
  - Spencer Hoehl: Simulator startup tomorrow (November 3) at 15:00; Wed 13:00 discussion on flight safety and certifications
  - Simulator system ready for demonstration to UK delegation with online meeting capability for remote participants
- **Channel Management:** All communications consolidated within #25_1-navy-sbir-magnetometer (decision made October 29, 2026)
- **Presentation Status:** 
  - Final link: https://docs.google.com/presentation/d/1l6kDsTF_w8hIT3s5Tkwm7f4RUz7jGJpOGz3ZOTg6dd4/edit?slide=id.h444cf934131a2cee_1_42
  - Converted to Google Slides format (November 2, 2026) from PowerPoint for collaborative editing
  - Alternate payloads section: One slide intentionally minimal (marketing awareness only)
  - Phase I and Phase II sections updated with content from Option Final Presentation
  - Ship ID imagery added for comms & spectrum section (November 3, 2026)
  - Formatting refinements completed (November 3, 2026) to address text overlap and theme consistency issues
- **Next Steps:** 
  - Site visit execution (week of November 2-6, 2026)
  - Comms & spectrum discussion (Wed 10-12)
  - Flight safety and certifications discussion (Wed 13:00)
  - Merlin integration discussion (Wed, Jack Elston lead)
  - Alternate payloads discussion (Dan Prendergast leading; intentionally vague on SOCOM variants)

## Action Items & Commitments

**Immediate/In Progress (November 3, 2026):**
- Spencer Hoehl: Prepare to start up sim system in main conference room November 3 at 15:00 (3pm) for UK delegation visit; ensure online meeting capability is functional for remote participants (November 2-3, 2026)
- Dan Prendergast: Manage online meeting setup in conference room during site visit tour to include remote participants (November 3, 2026)
- Jack Elston: Lead comms & spectrum and Merlin integration discussions Wed 10-12 with UK Navy/LMUK (November 2, 2026)
- Spencer Hoehl: Participate in flight safety and certifications discussion Wed 13:00 with UK delegation (November 2, 2026)
- Dan Prendergast: Conduct alternate payloads discussion (one slide, intentionally brief marketing overview; avoid specific SOCOM variant connection) (November 2, 2026)
- Beck Cotter: Continue coordinating breakfasts and lunches for UK visit week (November 2, 2026 - acknowledged with thanks)
- Maciej: UK RAVEN presentation finalization (November 2-3, 2026); content integration and plot updates from Option Final Presentation completed; formatting issues resolved; ship ID imagery added to appropriate section

**Earlier Commitments (Status Unknown/Ongoing):**
- Sam Hild: Deployment tube checklist update and approval (June 5, 2026)
- Maciej: QuSpin power supply testing for noise reduction verification (June 12, 2026)
- QuSpin firmware status: Sensor sent to manufacturer for firmware update and QC check (July 2026)
- S0 drop altitude optimization: Maciej continuing development of design modifications to achieve <1000ft target altitude; validate sequence speed-up and ballast removal approaches (linked to Simon's requirements)
- Phase II Schedule Planning: Maciej to develop detailed work plan addressing gaps from Option period, including potential accelerated timeline adjustments if January 2027 funding approved

## Client & External References

**Navy (Primary Client)**
- Navy TPOC: Angel Ruiz-Reyes (flight test requirements liaison)
- Navy DEVCOM: Morris "DeSi"
- Navy Personnel: Tony, Daniel Klier, Aaron Pyrah, Derek
- Various Navy contacts involved in TCE event and on-site testing; PCLT testing contacts (October 25-28, 2026)

**Sensor Manufacturers & Partners**
- QuSpin (Jeff): Magnetometer manufacturer; firmware updates and configuration support
- Bartington: Magnetometer supplier (UAS Mag PC298 model, 105 µT range)
- Ultra Maritime (Paul): Phase II subcontractor (selected January 2026)

**International Partners - UK RAVEN Program**
- Royal Navy: Simon (contact; commercials approval received October 25, 2026; specified <1000ft altitude requirement for drops; participating in site visit week of November 2-6, 2026)
- Lockheed Martin UK (LMUK): UK Navy program collaboration; on contract execution path; participating in site visit (week of November 2-6, 2026) with scheduled discussions on comms, spectrum, Merlin integration, and flight safety/certifications

**Research & Testing Partners**
- Ocean Observatories Initiative (OOI): Potential cost-sharing for ocean validation testing
- Cooperative Autonomous Technologies (CAT): Potential cost-sharing for testing initiatives

**External Consultants & Operational Contacts**
- Eric Correa: Technical consultant (on leave after June 4, 2026; availability for follow-up questions flagged)
- Dan Prendergast: External contact serving as primary coordinator for LMUK engagement, site visit logistics, presentation finalization, and UK RAVEN project leadership; driving SOCOM confidentiality strategy and operational messaging (November 2, 2026)

**Other References**
- Joshua Fromm: Participated in recent PCLT testing; documented Navy procedures and technical specifications from testing

## Recurring Topics & Themes

1. **Sensor Integration Challenges**: Ongoing work on Bartington and QuSpin integration, with significant focus on electrical noise isolation and power supply optimization (power isolation strategy, ADC resolution, PCB design iterations)

2. **Aircraft Modifications & Launcher Development**: Iterative refinement of S0-MAD reusable flight article design, landing gear configuration, and launcher systems (from hand-throw to tube-launched deployments with PCLT validation); now including altitude optimization for UK RAVEN requirements

3. **Flight Testing Methodology**: Sequential 1-hour test runs for baseline validation; requirements driven by Navy TPOC Angel Ruiz-Reyes specifications; altitude constraints per Simon (UK RAVEN)

4. **Magnetic Performance Validation**: Repeated concerns about noise sources affecting sensor accuracy (motor positioning, electrical integration, power supply isolation); decision to test over water for realistic validation

5. **Schedule & Funding Contingency Planning**: Tracking of project phases, funding status, and contingency planning for accelerated timelines if Phase II funding approved

6. **Demonstration Events & Operational Integration**: Multi-stage demonstration strategy involving TCE event (September 2026 - completed), Arctic Edge 2027 (April-May 2027), ongoing PCLT integration validation for Navy, and UK RAVEN program execution

7. **Budget & Resource Reallocation**: Active management of subcontractor funds (CRT, Cetacean) and reallocation to high-priority areas (TCE demo preparation, launcher development, travel)

8. **International Collaboration & Contract Execution**: UK Navy program (RAVEN) contract negotiations with LMUK and Royal Navy (Simon); tracking of commercial approvals and contracting timelines; active transition to program execution phase; presentation materials coordination and finalization; site visit logistics and meeting configuration

9. **Aircraft Launch/Recovery Constraints**: Technical considerations for different launch platforms (UH-60 hand-throw, horizontal tube launch, altitude/velocity effects on aircraft aerodynamics and separation dynamics)

10. **Presentation & Documentation Development**: Active creation and refinement of project presentation materials (UK RAVEN kickoff slides, reference to Option Final Presentation) incorporating data and plots from multiple sources; technical challenges with format conversion and slide style management; strategic inclusion of visual assets (ship ID imagery)

11. **Operational Security & Program Confidentiality**: Managing disclosure of parallel payload development (SOCOM variants) in discussions with international partners; strategic messaging around "other customers" and intentional vagueness regarding specific variant development

12. **Simulator System Readiness**: Preparation and demonstration of simulation capabilities to UK delegation for technical discussions and system demonstration; integration of online meeting capability for remote participation

## Important Resources

**Documentation:**
- UK RAVEN project kickoff presentation (FINAL):
  - Link: https://docs.google.com/presentation/d/1l6kDsTF_w8hIT3s5Tkwm7f4RUz7jGJpOGz3ZOTg6dd4/edit?slide=id.h444cf934131a2cee_1_42
  - Converted from PowerPoint to Google Slides format (November 2, 2026)
  - Content consolidated from Jack Elston's initial draft and multiple existing decks
  - Site visit agenda on slides 2 and 32 (updated November 2, 2026)
  - Phase I and Phase II sections updated with content from Option Final Presentation
  - Ship ID imagery integrated into comms & spectrum section (November 3, 2026)
  - Formatting refinements completed November 3, 2026 (text overlap, theme consistency)
  - Alternate payloads section: One slide (intentional marketing overview, SOCOM variants not disclosed)
  
- Option Final Presentation: Reference source for S0 drop performance plots and technical data
  - Link: https://docs.google.com/presentation/d/1fq-zhaRyCQSqUoThZKvihDjNq4s0x5pTRlL1D0Ku5OM/edit?slide=id.g96f86c98aa_3_0

- Site visit agenda: Finalized November 2, 2026; distributed to LMUK for input
  - Wednesday schedule confirmed:
    - 10:00-12:00: Jack Elston - Comms & spectrum and Merlin integration
    - 13:00: Spencer Hoehl - Flight safety and certifications

**Technical Specifications:**
- Bartington sensor: UAS Mag PC298, 105 µT range
- S0 aircraft radio: 430 MHz (Microhard type, to be confirmed)
- Magnetometer power requirements: ~1A at 5V
- ADC specification: 24-bit (dual 24-bit ADCs via I2C) targeting 1μV resolution
- Bartington power supply requirement: <1mV ripple
- PCLT operational configuration: Fiberglass tube (no EMI paint in fleet aircraft); communications verified functional within enclosure
- S0 drop altitude: Historical range 1200'-2000'; target <1000ft for UK RAVEN program (October 29, 2026)
- Altitude optimization feasibility: Achievable through sequence speed-up and ballast removal with minimal design changes (October 29, 2026)

**Procurement:**
- Launcher parts: Approved $1.3K order from McMaster (June 22, 2026)

**Testing Validation:**
- PCLT testing completed (October 25-28, 2026): Communications verified functional; deployment conops validated with Navy; EMI considerations confirmed
- S0 drop altitude assessment: Historical performance data reviewed; design modification feasibility assessed (sequence speed-up, ballast removal) (October 29, 2026)

**Simulator & Demonstration:**
- Main conference room simulator system: Ready for November 3, 15:00 startup for UK delegation demonstration (Spencer Hoehl to operate); online meeting capability configured for remote participant inclusion

**Technical Best Practices:**
- Google Slides import lesson: Use "use styles in this presentation" option when copying slides to maintain theme master slides and allow theme-wide formatting updates (lesson learned November 3, 2026 from formatting issues in RAVEN presentation conversion)

## Recent Activity

**November 3, 2026 - Final Site Visit Preparation & Online Meeting Coordination:**

Dan Prendergast coordinated final logistical details for the UK Navy and LMUK site visit (November 3, 2026):
- Requested that online meeting be started in conference room during tour to ensure remote participants are included in discussions
- Rationale: Facilitate full participation from remote attendees during on-site sessions
- Jack Elston praised presentation work ("taco" emoji acknowledgment) for fixing formatting issues in the deck (November 3, 2026)
- Maciej added ship ID imagery to the presentation for use in Jack Elston's comms & spectrum section (scheduled for Wed afternoon discussion); offered flexibility for Jack to remove imagery if preferred (November 3, 2026)
- Status: All logistics and content refinements completed; presentation ready for delivery

**November 3, 2026 - UK RAVEN Presentation Final Content Integration:**

Maciej completed final content enhancements to UK RAVEN kickoff presentation (November 3, 2026):
- Added ship identification visual asset to comms & spectrum section (supporting Jack Elston's Wednesday 10-12 discussion)
- Noted that Jack Elston has flexibility to remove imagery if it doesn't fit presentation flow
- Presentation finalized and ready for site visit week (November 3-6, 2026)
- Recognition from Jack Elston for addressing all formatting and structural issues

**November 2-3, 2026 - UK RAVEN Site Visit Logistics & Agenda Finalization (Continued):**

Final coordination for site visit preparation (November 2-3, 2026):
- Simulator system startup confirmed for November 3, 15:00
- Online meeting capability to be integrated during tour for remote participant inclusion
- Presentation with ship ID imagery finalized
- All technical discussion sessions scheduled and leads confirmed
- Beck Cotter coordinating meal logistics for visit week

**November 2, 2026 - SOCOM Program Confidentiality Strategy (Continued):**

Dan Prendergast established operational security guidelines for site visit discussions with UK Navy and LMUK (November 2, 2026):
- Decision to avoid connecting SOCOM program variants in discussions with UK partners
- Alternative payload development to be presented generically as work for "another customer" with intentional vagueness
- Rationale: UK Navy and Lockheed partners expected to understand intentional discretion and not press further
- Alternate payloads section limited to one slide (marketing awareness only, no technical depth)
- Channel-wide notification to all team members regarding messaging discipline (November 2, 2026)