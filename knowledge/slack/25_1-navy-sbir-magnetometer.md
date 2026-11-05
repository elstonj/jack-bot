# #25_1-navy-sbir-magnetometer

## Overview
This channel is focused on Black Swift Technologies' Navy Small Business Innovation Research (SBIR) project for developing magnetometer-equipped aircraft systems. The project involves integrating QuSpin and Bartington magnetometers with BST's aircraft platforms for magnetic signature detection applications (MAD - Magnetic Anomaly Detection). Key participants include Beck Cotter, Maciej, Tyler, Sam Hild, Alex Lomis, Joshua Fromm, Jack Elston, Spencer Hoehl, and Ethan Domagala from BST, with external collaboration from QuSpin (Jeff), Ultra Maritime (Paul), Navy DEVCOM (Morris "DeSi"), Navy TPOC (Angel Ruiz-Reyes), Navy personnel (Tony, Daniel Klier, Aaron Pyrah, Derek), Royal Navy contact Simon, Lockheed Martin UK (LMUK), Dan Prendergast, and external consultant Eric Correa. Activity spans from October 2025 through November 2026, covering Phase I completion, Phase II proposal submission and kickoff, Option period development with flight testing preparation, sensor optimization work, TCE (Technology Concept Experimentation) event participation at Camp Pendleton (September 14-24), on-site testing and TAK integration with Navy personnel, post-TCE reporting and meeting preparation, UK Navy RAVEN program contract finalization and kickoff (November 2026), and Arctic Edge 2027 participation planning (April 19-May 7, Alaska). Recent activity focuses on PCLT integration testing completion, altitude optimization for S0 drops, UK RAVEN project kickoff presentation finalization, site visit execution with UK Navy and LMUK (November 2-6, 2026), operational security regarding SOCOM program integration, simulator system preparation for UK delegation visit, and aircraft production planning for multiple program variants (November 4, 2026).

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
- S0 aircraft production planning: Plan to build extra S0 aircraft beyond immediate Phase II allocation to support Twin Otter test drop (April/May 2027) and maintain recovery capability for magnetometer variant (November 4, 2026). ATR variant specifically identified as requiring extra production units.

## Projects & Initiatives

**Navy SBIR Magnetometer Program (Primary)**
- **Status:** Option period complete; Phase II funding pending (as of November 2026)
- **Phase I:** Completed (concluded October 2025)
- **Option Period:** Completed; focus included TCE event at Camp Pendleton (September 14-24, 2026); PCLT integration validation; altitude optimization
- **Phase II:** Proposed; if funded from January 2027 kickoff, schedule calls for drop article readiness by April-May 2027
- **Key Deliverables:** 
  - Reusable S0-MAD flight article with Bartington and QuSpin magnetometers
  - Launch/recovery systems (manual hand-throw from UH-60 primary; PCLT tube-launched system validated for deployment)
  - Magnetic anomaly detection capability demonstration
  - Custom PCB for isolated power supply and 24-bit ADC for sensor integration
  - Multiple S0 aircraft variants (ATR variant, magnetometer variant, others) with planned production of additional units beyond Phase II initial allocation
- **Aircraft Production Schedule:** Planning discussions ongoing November 4, 2026 regarding quantity of S0 aircraft to be built across SOCOM, RAVEN (Royal Navy), and Arctic Edge (Twin Otter) programs with focus on recovery and reuse strategy

**Arctic Edge 2027 Participation** (Advanced Planning)
- **Dates:** April 19-May 7, 2027, Alaska
- **Status:** Planning stage; aircraft production planning tied to Twin Otter test drop requirements (April/May 2027)
- **Relationship to Phase II:** Potential demonstration opportunity if Phase II funding approved
- **Connection to PCLT Testing:** Recent PCLT validation testing supports readiness for Arctic Edge deployment scenarios
- **Aircraft Requirements:** ATR variant identified as requiring multiple test drops during Twin Otter testing phase (April/May 2027); Maciej recommending production of extra ATR variant aircraft to support testing and maintain recovery capability (November 4, 2026)

**UK Navy RAVEN Program (with LMUK)** (Active Execution Phase)
- **Status:** Commercial approval received October 25, 2026; contract moving to formal execution phase; kickoff presentation finalized November 2-3, 2026; site visit with UK Navy and LMUK delegation completed/ongoing (week of November 2-6, 2026)
- **Participants:** Lockheed Martin UK (LMUK), Simon (Royal Navy contact), Dan Prendergast (program coordination), Beck Cotter (logistics), Jack Elston (comms & spectrum lead), Spencer Hoehl (simulator and flight safety lead), Maciej, and BST team
- **Technical Requirements:** 
  - Altitude specification <1000ft for drops (per Simon, October 29, 2026)
  - Payload development variants (with SOCOM integration intentionally undisclosed to UK partners)
  - Aircraft production: Minimum 3 S0 aircraft planned for Royal Navy (November 4, 2026)
- **Key Milestones:** 
  - Commercial approval achieved (October 25, 2026)
  - Kickoff presentation finalized (November 2-3, 2026)
  - Site visit agenda finalized (November 2, 2026); updated content on slides 2 and 32 of RAVEN presentation
  - Jack Elston: Led Wed 10-12 discussions on comms & spectrum, Merlin integration
  - Spencer Hoehl: Simulator startup November 3 at 15:00; Led Wed 13:00 discussion on flight safety and certifications
  - Simulator system demonstrated to UK delegation with online meeting capability for remote participants
- **Channel Management:** All communications consolidated within #25_1-navy-sbir-magnetometer (decision made October 29, 2026)
- **Presentation Status:** 
  - Final link: https://docs.google.com/presentation/d/1l6kDsTF_w8hIT3s5Tkwm7f4RUz7jGJpOGz3ZOTg6dd4/edit?slide=id.h444cf934131a2cee_1_42
  - Converted to Google Slides format (November 2, 2026) from PowerPoint for collaborative editing
  - Alternate payloads section: One slide intentionally minimal (marketing awareness only)
  - Phase I and Phase II sections updated with content from Option Final Presentation
  - Ship ID imagery added for comms & spectrum section (November 3, 2026)
  - Formatting refinements completed (November 3, 2026) to address text overlap and theme consistency issues
- **Next Steps:** 
  - Site visit ongoing (week of November 2-6, 2026)
  - Comms & spectrum discussion (completed Wed 10-12)
  - Flight safety and certifications discussion (completed Wed 13:00)
  - Merlin integration discussion (completed Wed, Jack Elston lead)
  - Alternate payloads discussion (Dan Prendergast led; intentionally vague on SOCOM variants)

**SOCOM Program (Parallel Development, Confidential)**
- **Status:** Active development; aircraft production planning ongoing (November 4, 2026)
- **Aircraft Requirements:** Multiple S0 variants under development; quantity tracking and production planning to be coordinated with Dan Prendergast and Beck Cotter (November 4, 2026)
- **Operational Security:** Intentional separation maintained from UK RAVEN discussions; presented to international partners as work for "another customer" (November 2, 2026)
- **Quality Control:** S0 aircraft production for SOCOM program not currently tracked in QC system; Beck Cotter and Dan Prendergast to establish tracking process (November 4, 2026)

## Action Items & Commitments

**Immediate/In Progress (November 4, 2026):**
- Beck Cotter & Dan Prendergast: Schedule meeting to discuss S0 aircraft production numbers across programs (SOCOM, RAVEN, Arctic Edge); establish QC tracking system for all S0 variants being built; clarify Phase II allocation vs. additional production units (November 4, 2026)
  - Maciej input: Plan for extra ATR variant units for Twin Otter testing (April/May 2027) beyond standard Phase II allocation
  - Jack Elston query: Confirm Phase II allocation quantity (Maciej believes ~4 aircraft; needs verification)
  - Key issue: Current tracking does not reflect SOCOM program S0 variants; need comprehensive production plan
- Maciej: Verify Phase II aircraft allocation quantity and provide details to Beck Cotter/Dan Prendergast meeting (November 4, 2026)

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
- Royal Navy: Simon (contact; commercials approval received October 25, 2026; specified <1000ft altitude requirement for drops; participated in site visit week of November 2-6, 2026)
- Lockheed Martin UK (LMUK): UK Navy program collaboration; on contract execution path; participated in site visit (week of November 2-6, 2026) with discussions on comms, spectrum, Merlin integration, and flight safety/certifications

**Research & Testing Partners**
- Ocean Observatories Initiative (OOI): Potential cost-sharing for ocean validation testing
- Cooperative Autonomous Technologies (CAT): Potential cost-sharing for testing initiatives

**External Consultants & Operational Contacts**
- Eric Correa: Technical consultant (on leave after June 4, 2026; availability for follow-up questions flagged)
- Dan Prendergast: External contact serving as primary coordinator for LMUK engagement, site visit logistics, presentation finalization, and UK RAVEN project leadership; driving SOCOM confidentiality strategy and operational messaging; coordinating S0 production planning across programs (November 2-4, 2026)

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

8. **International Collaboration & Contract Execution**: UK Navy program (RAVEN) contract negotiations with LMUK and Royal Navy (Simon); tracking of commercial approvals and contracting timelines; active transition to program execution phase; presentation materials coordination and finalization; site visit execution completed (November 2-6, 2026)

9. **Aircraft Launch/Recovery Constraints**: Technical considerations for different launch platforms (UH-60 hand-throw, horizontal tube launch, altitude/velocity effects on aircraft aerodynamics and separation dynamics)

10. **Presentation & Documentation Development**: Active creation and refinement of project presentation materials (UK RAVEN kickoff slides, reference to Option Final Presentation) incorporating data and plots from multiple sources; technical challenges with format conversion and slide style management; strategic inclusion of visual assets (ship ID imagery)

11. **Operational Security & Program Confidentiality**: Managing disclosure of parallel payload development (SOCOM variants) in discussions with international partners; strategic messaging around "other customers" and intentional vagueness regarding specific variant development

12. **Simulator System Readiness**: Preparation and demonstration of simulation capabilities to UK delegation for technical discussions and system demonstration; integration of online meeting capability for remote participation

13. **Aircraft Production Planning & QC Tracking**: New recurring theme (November 4, 2026): Coordination of S0 aircraft production across multiple programs (Phase II Navy, SOCOM confidential, UK RAVEN, Arctic Edge Twin Otter), with focus on establishing unified QC tracking system and managing recovery/reuse strategy for magnetometer variants

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
    - 10:00-12:00: Jack Elston - Comms & spectrum and Merlin integration (completed)
    - 13:00: Spencer Hoehl - Flight safety and certifications (completed)

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
- Main conference room simulator system: Demonstrated to UK delegation November 3, 15:00 (Spencer Hoehl operated); online meeting capability confirmed functional for remote participant inclusion

**Technical Best Practices:**
- Google Slides import lesson: Use "use styles in this presentation" option when copying slides to maintain theme master slides and allow theme-wide formatting updates (lesson learned November 3, 2026 from formatting issues in RAVEN presentation conversion)

## Recent Activity

**November 4, 2026 - S0 Aircraft Production Planning & QC Tracking Initiative:**

Maciej, Beck Cotter, Jack Elston, and Dan Prendergast began comprehensive aircraft production planning discussion (November 4, 2026):

- **Maciej's Production Guidance (15:52):** Recommended planning for extra S0 aircraft units, specifically noting:
  - Multiple S0 variants being built across programs (SOCOM and Royal Navy confirmed; Twin Otter Arctic Edge implied)
  - Emphasis on building "a couple extra of at least the ATR variant" to support Twin Otter test drop in April/May 2027
  - Strategic planning for recovery capability on magnetometer variants (desire to recover most aircraft after drops for reuse/continued testing)
  - Rationale: Extra aircraft provide buffer for test operations, damage recovery, and continued system refinement

- **Beck Cotter's QC Tracking Issue (15:56):** Identified critical process gap:
  - S0 aircraft builds for SOCOM program are "not being tracked in the QC"
  - Requested meeting with Dan Prendergast to establish what is known about current aircraft and implement proper tracking
  - Implies current production underway without unified visibility into quantity, configuration, or status

- **Dan Prendergast's Meeting Response (17:36):** Agreed to meet November 5, 2026 to address S0 production coordination

- **Jack Elston's Phase II Quantity Question (19:17):** Inquired about Phase II aircraft allocation quantity
  - Question directed to Maciej regarding contract-funded S0 aircraft

- **Maciej's Partial Answer (19:19):** 
  - Believes Phase II contract funds ~4 aircraft
  - Notes uncertainty ("I'll have to check")
  - Expresses intent to recover most aircraft for magnetometer program reuse after delivery
  - Implies Phase II allocation of ~4 aircraft must be supplemented with additional builds to meet all program demands (SOCOM, RAVEN 3 units, Arctic Edge variants)

**Implications & Status:**
- Production planning meeting scheduled November 5, 2026 (Dan Prendergast & Beck Cotter)
- Need to reconcile:
  - Phase II contract aircraft allocation (~4 confirmed tentatively)
  - Royal Navy/RAVEN production requirement (minimum 3 aircraft per Maciej, November 4)
  - SOCOM program aircraft (quantity unknown; not currently tracked in QC)
  - Arctic Edge/Twin Otter variant requirements (ATR variant extra units specifically flagged)
  - Recovery/reuse strategy for magnetometer variants across programs
- Follow-up verification needed on exact Phase II quantity and configurations

**November 3, 2026 - UK RAVEN Site Visit Execution:**

Site visit with UK Navy and LMUK delegation proceeded as planned during week of November 2-6, 2026:
- Spencer Hoehl successfully started simulator system in main conference room November 3 at 15:00
- Online meeting capability integrated during tour for remote participant inclusion (confirmed November 3)
- Jack Elston led scheduled discussions on comms & spectrum and Merlin integration (Wednesday 10:00-12:00)
- Spencer Hoehl participated in flight safety and certifications discussion (Wednesday 13:00)
- Presentation delivered with finalized ship ID imagery and formatting refinements
- All technical discussion sessions completed with UK Navy and LMUK participants
- Site visit appears to have concluded successfully by November 4, 2026

**November 2-3, 2026 - UK RAVEN Presentation Finalization & Delivery:**

Final presentation completion (November 2-3, 2026):
- Maciej added ship identification visual asset to comms & spectrum section (supporting Jack Elston's Wednesday 10-12 discussion) (November 3, 2026)
- Offered flexibility for Jack Elston to remove imagery if presentation flow required adjustment
- Jack Elston acknowledged completion with praise emoji (November 3, 2026)
- All formatting and structural issues resolved prior to site visit delivery
- Presentation ready for UK Navy/LMUK technical discussions

---

## Summary of November 4, 2026 Key Discussion

The November 4, 2026 channel activity represents a critical transition point in project execution. The successful completion of the UK RAVEN site visit (November 2-6, 2026) triggered initiation of comprehensive aircraft production planning across multiple concurrent programs. The discovery that SOCOM program aircraft production is not being tracked in quality control systems, combined with growing clarity on UK RAVEN (3 aircraft minimum) and Arctic Edge/Twin Otter (extra ATR variants) requirements, prompted Maciej to advocate for strategic over-production of key variants to support testing, recovery, and reuse objectives. The production planning meeting scheduled for November 5, 2026 between Dan Prendergast and Beck Cotter will establish unified visibility across programs and synchronize builds with contract allocations and operational requirements.