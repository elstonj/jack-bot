# #25_1-navy-sbir-magnetometer

## Overview
This channel is focused on Black Swift Technologies' Navy Small Business Innovation Research (SBIR) project for developing magnetometer-equipped aircraft systems. The project involves integrating QuSpin and Bartington magnetometers with BST's aircraft platforms for magnetic signature detection applications (MAD - Magnetic Anomaly Detection). Key participants include Beck Cotter, Maciej, Tyler, Sam Hild, Alex Lomis, Joshua Fromm, Jack Elston, Spencer Hoehl, and Ethan Domagala from BST, with external collaboration from QuSpin (Jeff), Ultra Maritime (Paul), Navy DEVCOM (Morris "DeSi"), Navy TPOC (Angel Ruiz-Reyes), Navy personnel (Tony, Daniel Klier, Aaron Pyrah, Derek), Royal Navy contact Simon, Lockheed Martin UK (LMUK), Dan Prendergast, and external consultant Eric Correa. Activity spans from October 2025 through October 2026, covering Phase I completion, Phase II proposal submission and kickoff, Option period development with flight testing preparation, sensor optimization work, TCE (Technology Concept Experimentation) event participation at Camp Pendleton (September 14-24), on-site testing and TAK integration with Navy personnel, post-TCE reporting and meeting preparation, UK Navy program work with LMUK involvement, and emerging participation in Arctic Edge 2027 (April 19-May 7, Alaska). Recent activity (October 2026) focuses on PCLT (Payload Containment Launch Tube) integration testing, deployment conops clarification, Arctic Edge 2027 planning, demo strategy refinement, clarification of Phase II development goals vs. demonstration requirements, and contingency planning for potential funding delays.

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

## Projects & Initiatives

**Navy SBIR Magnetometer Program (Primary)**
- **Status:** Option period underway; Phase II funding pending (as of October 2026)
- **Phase I:** Completed (concluded October 2025)
- **Option Period:** Active focus on TCE event preparation and demonstration (Camp Pendleton, September 14-24, 2026); transitioning to PCLT integration validation
- **Phase II:** Proposed; if funded from January 2027 kickoff, schedule calls for drop article readiness by April-May 2027
- **Key Deliverables:** 
  - Reusable S0-MAD flight article with Bartington and QuSpin magnetometers
  - Launch/recovery systems (manual hand-throw from UH-60 primary; PCLT tube-launched system validated for deployment)
  - Magnetic anomaly detection capability demonstration
  - Custom PCB for isolated power supply and 24-bit ADC for sensor integration

**Arctic Edge 2027 Participation** (Emerging)
- **Dates:** April 19-May 7, 2027, Alaska
- **Status:** Planning stage; strategy discussions ongoing (October 2026)
- **Relationship to Phase II:** Potential demonstration opportunity if Phase II funding approved
- **Connection to PCLT Testing:** Recent PCLT validation testing supports readiness for Arctic Edge deployment scenarios

**UK Navy Program (with LMUK)**
- **Status:** Contract execution in advanced stages; Simon (Royal Navy contact) on commercial path to finalize contract
- **Latest Status:** As of October 28, 2026, Simon received commercial approval on Friday (October 25), pending final move into formal contracting; described commercial issues as "hard yards" now complete
- **Participants:** Lockheed Martin UK (LMUK), Simon (Royal Navy contact), Dan Prendergast
- **Next Steps:** Site visit agenda to be distributed to LMUK for input after finalization by Dan Prendergast (October 28, 2026)

## Action Items & Commitments

**Pending/Open Items (October 28, 2026):**
- Agenda finalization & distribution: Dan Prendergast to incorporate Maciej's comments on agenda and distribute to full team, with LMUK providing input afterward (October 28, 2026)
- LMUK input on next week's discussion topics: Open line to Simon if LMUK hasn't provided input; Simon noted he "gave them plenty of steer" (October 28, 2026)
- Phase II Schedule Planning: Maciej to develop detailed work plan addressing gaps from Option period, including potential accelerated timeline adjustments if January 2027 funding approved

**Earlier Commitments (Status Unknown/Ongoing):**
- Sam Hild: Deployment tube checklist update and approval (June 5, 2026)
- Maciej: QuSpin power supply testing for noise reduction verification (June 12, 2026)
- QuSpin firmware status: Sensor sent to manufacturer for firmware update and QC check (July 2026)

## Client & External References

**Navy (Primary Client)**
- Navy TPOC: Angel Ruiz-Reyes (flight test requirements liaison)
- Navy DEVCOM: Morris "DeSi"
- Navy Personnel: Tony, Daniel Klier, Aaron Pyrah, Derek
- Various Navy contacts involved in TCE event and on-site testing; PCLT testing contacts (recent validation work on October 25-28, 2026)

**Sensor Manufacturers & Partners**
- QuSpin (Jeff): Magnetometer manufacturer; firmware updates and configuration support
- Bartington: Magnetometer supplier (UAS Mag PC298 model, 105 µT range)
- Ultra Maritime (Paul): Phase II subcontractor (selected January 2026)

**International Partners**
- Royal Navy: Simon (contact; commercials approval received October 25, 2026; expects contract finalization imminent)
- Lockheed Martin UK (LMUK): UK Navy program collaboration; on contract execution path pending Simon's fund transfer

**Research & Testing Partners**
- Ocean Observatories Initiative (OOI): Potential cost-sharing for ocean validation testing
- Cooperative Autonomous Technologies (CAT): Potential cost-sharing for testing initiatives

**External Consultants & Operational Contacts**
- Eric Correa: Technical consultant (on leave after June 4, 2026; availability for follow-up questions flagged)
- Dan Prendergast: External contact serving as coordinator for LMUK engagement and site visit logistics

**Other References**
- Joshua Fromm: Participated in recent PCLT testing; documented Navy procedures and technical specifications from testing

## Recurring Topics & Themes

1. **Sensor Integration Challenges**: Ongoing work on Bartington and QuSpin integration, with significant focus on electrical noise isolation and power supply optimization (power isolation strategy, ADC resolution, PCB design iterations)

2. **Aircraft Modifications & Launcher Development**: Iterative refinement of S0-MAD reusable flight article design, landing gear configuration, and launcher systems (from hand-throw to tube-launched deployments with PCLT validation)

3. **Flight Testing Methodology**: Sequential 1-hour test runs for baseline validation; requirements driven by Navy TPOC Angel Ruiz-Reyes specifications

4. **Magnetic Performance Validation**: Repeated concerns about noise sources affecting sensor accuracy (motor positioning, electrical integration, power supply isolation); decision to test over water for realistic validation

5. **Schedule & Funding Contingency Planning**: Tracking of project phases, funding status, and contingency planning for accelerated timelines if Phase II funding approved

6. **Demonstration Events & Operational Integration**: Multi-stage demonstration strategy involving TCE event (September 2026), Arctic Edge 2027 (April-May 2027), and ongoing PCLT integration validation for actual Navy deployment scenarios

7. **Budget & Resource Reallocation**: Active management of subcontractor funds (CRT, Cetacean) and reallocation to high-priority areas (TCE demo preparation, launcher development, travel)

8. **International Collaboration & Contract Execution**: UK Navy program contract negotiations with LMUK and Royal Navy; tracking of commercial approvals and contracting timelines

## Important Resources

**Documentation:**
- Site visit agenda draft (in preparation for LMUK input): Managed by Dan Prendergast; Maciej provided comments for incorporation (October 28, 2026)

**Technical Specifications:**
- Bartington sensor: UAS Mag PC298, 105 µT range
- S0 aircraft radio: 430 MHz (Microhard type, to be confirmed)
- Magnetometer power requirements: ~1A at 5V
- ADC specification: 24-bit (dual 24-bit ADCs via I2C) targeting 1μV resolution
- Bartington power supply requirement: <1mV ripple
- PCLT operational configuration: Fiberglass tube (no EMI paint in fleet aircraft); communications verified functional within enclosure

**Procurement:**
- Launcher parts: Approved $1.3K order from McMaster (June 22, 2026)

**Testing Validation:**
- PCLT testing completed (October 25-28, 2026): Communications verified functional; deployment conops validated with Navy; EMI considerations confirmed

## Recent Activity

**October 28, 2026 - PCLT Integration Testing & Contract Progress:**

**PCLT Deployment Integration (Jack Elston, Dan Prendergast, Joshua Fromm):**
- Communications testing confirmed: S0 communications functional within PCLT enclosure
- Configuration verification: Test PCLT was fiberglass tube (no EMI paint); confirmed that operational fleet PCLT units would NOT have EMI paint
- RF environment validation: Current test setup confirmed as representative of actual fleet RF conditions
- Operational procedures documented: Navy carries multiple payloads in host aircraft (S0s, loitering munitions, etc.); S0 kept powered off until final deployment readiness; powered on and loaded into PCLT immediately before deployment
- Key takeaway: No anticipated complications with communications or GPS in actual deployment scenario; procedures support operational readiness

**UK Navy Program Contract Status (Maciej, Beck Cotter, Dan Prendergast, Simon):**
- Simon (Royal Navy) provided update: Received commercial approval on Friday (October 25, 2026) after resolving "commercial glitches"
- Contract execution: Hard commercial work completed; awaiting formal transition to contracting phase
- LMUK coordination: Beck Cotter confirmed team has completed due diligence on contract side while awaiting Simon's fund transfer
- Next steps: Dan Prendergast to finalize site visit agenda (incorporating Maciej's comments) and distribute to LMUK for their input
- Team sentiment: Simon expressed enthusiasm for "agile and innovative" collaboration with BST

**Strategic Implications:**
- PCLT testing validates critical deployment integration; removes technical barriers for Phase II execution
- LMUK contract imminent; enables parallel UK Navy program execution if Phase II funding approved
- Site visit agenda preparation reflects confidence in near-term contract finalization
- Overall positioning supports accelerated Phase II timeline if January 2027 funding approved