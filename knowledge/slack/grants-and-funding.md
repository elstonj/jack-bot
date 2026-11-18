# #grants-and-funding

## Overview

This channel tracks Black Swift Technologies' grant applications, funding pursuits, and government contracting efforts across federal agencies (NASA, DOD, NOAA, USDA, DOE, etc.). It serves as the central hub for proposal submissions, funding strategy discussions, budget development, and award management.

**Key Participants:** Jack Elston (primary decision-maker and proposal reviewer), Maciej (technical/proposal support and field operations), Meredith Needham (budget/administrative), Dan Prendergast (proposal coordination and logistics), Beck Cotter (program management/budget formatting/export compliance), Ira (ROSES/NASA work), Jeremy, Weile, Joshua Fromm (hardware/integration), Paige Smith (presentation/logistics support and opportunity scouting), Arthur (technical partner for payload/antenna work), Bryan (external contact for Vulcan opportunity), Sona (operational/budget planning), Gijs (BNL partner), Kirsten Boogard (777 PM at NOAA), Bob and Lisa (camera/integration leads), SkyMesa (RF/EW partner), Hank (external contact with S3 design requests), Ariel (pipeline/portfolio oversight), Lockheed Martin UK (LMUK - partnership contact), Annette (format/process coordinator), Kreateo (external legal/compliance consultant for USML classification), Alex Lomis (RF analysis), Trenton/NexTech (external contact for temperature capability discussions), C-Astral (external contact), Bassil (customer/funder for flight operations), Roger (external contact for COO/parts analysis), Angel (PACOM/Northern Edge contact), Evan (SOCOM contact), Bradley (Northern Edge contact), Chris Meek (Langley/procurement contact), Tony (Northern Edge registration contact), PrecisionTerra (subcontract partner), By Light (DIU partnership), Eryan (NASA radiometry project partner), Supercool Earth (cloud seeding/icing flight customer), Joe Cione (NOAA cyclone/hurricane research contact), Josh C (Navy STTR contact), Jana Kolb (NOAA hurricane contract CO), Angie and Cristoph (NOAA/USGS project contacts for IDIQ), Simon (UK Navy partner/contact), Tony (external contact involved with Camp Pendleton incident), Brian (template/formatting support), Chris Leek (Langley procurement contact), Jed and Brian from KS (external editing support for LC-ISR and DIU decks), Spencer L (wing/tailset manufacturer), Lisa Marie (demo scheduling contact).

**Activity Level:** Extremely high throughout the period (March 2024 - November 2026). The channel shows sustained proposal activity with multiple concurrent submissions across different agencies, averaging 3-5 active proposals at any given time. November 2026 shows continued Arctic operations support, partnership coordination, DIU program advancement, LC-ISR program development, and active technical decision-making on communication/avionics approaches.

**Time Range:** March 3, 2024 - November 17, 2026

---

## Key Decisions

### Funding Strategy & Approach
- **Pursued Republic for crowdfunding** (March 2024): Selected due to 5% commission, 2% equity structure, no C-Corp conversion required; escrow agent fees ~1.5-2%. Alternative investment banker Young American Capital deferred due to high costs and 18-week timeline.
- **Decided against exclusivity with Young American Capital** (March 2024) due to cost concerns.
- **Strategic positioning shift** (March 2024): Focus on positioning as platform enabling inspection UAS operations across challenging conditions (strong winds, precipitation, cold, redundancy, certification, ease of use).
- **Capital source constraints** (March 2024): Determined must avoid Chinese investor capital to maintain federal government contract eligibility.

### Product Development Approvals
- **S0 VTOL ISR variant approved** (March 2024) for development despite incomplete status, based on strong interest from potential customers.
- **Decided to pursue multiple aircraft configurations**: E2, S2, S0 for DIU Blue UAS submission; later expanded to S0-AD, S0-LR variants for specific government applications.
- **S3 folding wings reconsidered** (June 2026): Discussion regarding external request from Hank to make S3 with folding wings for boat deployment applications; Joshua Fromm noted S3 previously had folding wings capability but that period has passed, suggesting architectural constraints or design evolution away from this feature.
- **SOCOM demo aircraft allocated** (July 24, 2026): S0-85 and S0-86 reserved for SOCOM demo with parachute tube modification requirements.
- **Arctic customer cold-weather qualification design approach** (July 30, 2026): Decision to engineer and design components targeting -55°C requirement, with commitment to validate -40°C during current sprint. Optional -55°C validation (~$85k cost) offered as separate deliverable. Joshua Fromm to lead design starting week of August 5, 2026, with design details meeting to follow.
- **Arctic Edge 28 proposals submitted** (November 5, 2026): S3 and S0-VTOL aircraft proposed for Arctic Edge competition.
- **DIU S4 low-cost ISR demo selected for in-person pitch** (November 9, 2026): Advancement to next round for S4 configuration (S0 avionics with batteries on large glider aircraft for extended flight time optimization). Described by Maciej as "low-cost ISR demo"; physical build timeline not imminent but pitch preparation now underway.
- **LC-ISR wing/tailset supplier finalized** (November 17, 2026): Spencer L selected as primary supplier for LC-ISR aircraft with pricing and manufacturing timeline confirmed:
  - Full aircraft option (NRE + first unit): $27,900 (delivered January 2027)
  - Two aircraft: $52,300
  - Three aircraft: $76,700
  - **Financial approach**: Will order one unit initially to test and evaluate before committing to additional aircraft, reducing financial risk while maintaining manufacturing relationship
  - Spencer L wing inventory available but noted as too light for target LC-ISR weight specification
  - Large purchase commitment (Spencer L manufacturing beyond initial test unit) deferred until after pitch results received (Jack Elston directive maintained from November 15)

### LC-ISR Communication/Avionics Architecture (November 17, 2026)
- **Custom avionics board vs. Starlink trade study initiated**: Jack Elston and Maciej evaluating two approaches for LC-ISR command/control and data downlink:
  - **Option 1 (Custom board)**: Design and fabricate new board (~40-55 hours firmware/driver work, ~25-35 hours board work). Conservative estimates provided. Total calendar time longer due to fabrication cycle, but maintains full customization and system control. Estimated ~300 hours total work.
  - **Option 2 (Starlink integration)**: Eliminate custom board work (saves 40-55 hours), reduce driver work (~15-20 hours saved), but adds:
    - Power integration for 25-40W Starlink panel
    - SBC-to-autopilot bridge development
    - Full ground-side software architecture
    - VPN/relay infrastructure
    - Mechanical mounting for ~1kg Starlink panel (~25-40 hours)
    - Additional flight test validation required
    - Net total hours approximately equivalent (~300 hours) but calendar time 2-4 weeks shorter due to elimination of board fabrication cycle
    - **Trade-off**: Loses 1-2 hours of endurance; gains significant bandwidth (~1 Gbps vs. custom board capability)
  - **Bandwidth requirement assessment**: Jack Elston noting work appears to focus on ATR (Automatic Target Recognition) vs. FMV (Full Motion Video), suggesting Starlink bandwidth may exceed actual requirement and not justify trade-offs
  - **Cost impact**: Starlink approach generates savings toward COVAR (cost variance) budget
  - **Decision deferred to Thursday pitch preparation**: Team identified this as open question to include in pitch Q&A preparation materials (noted by Maciej as "FMV vs. ATR" question for customer)

### Proposal Strategy Decisions

#### AFWERX & Early 2024-2025 Proposals
- **AFWERX SBIR/STTR strategy** (October 2024):
  - BST leading STTR with CU on machine vision (GPS-denied nav, terrain following, autoland)
  - BST leading SBIR for S0 hurricane work with WC-130 squadron
  - Curable Composites leading SBIR with BST as subcontractor for edge-constructed group 2
  - Base security proposal dropped

- **Machine vision STTR scope** (October 2024): Limited Phase 1 to three core capabilities; narrowed based on customer findings in Phase 2.

- **Proposed S0-AD as STTR vehicle** (October 2024) due to unique characteristics (low cost, capable, air-deployable).

- **NOAA WPO proposal pivot** (November 2024): Shifted from NOAA payload calibration to real-time streaming of payload data into fire models; modified S3 aero design objectives to avoid "designing aircraft from scratch" perception.

- **NOAA Phase I SBIR topic selection** (November 2024): Selected Wildfire detection under extreme events topic (9.1) instead of hurricane focus after analysis showed better fit with call requirements and past awardees.

- **DIU Long-Range One-Way Platform passed** (2024): Decision not to pursue due to 10-25kg payload weight requirement vs BST's 3kg max, and requirement for loitering munition capabilities (outside scope).

- **Navy SBIR magnetometer focus** (February 2025): Determined viable despite cost constraints; selected QuSpin for magnetometer integration, Cetacean Research Technology for hydrophone/acoustic work.

- **XPrize Wildfire competition declined** (2024): Decided not to pursue due to funding requirements and lack of expertise fit; identified Rain.aero, FireFly, Anduril as serious competitors.

#### NASA & Q2 2026 Intensive Planning
- **NASA SBIR/STTR FY25 planning** (December 2024): Planned 3-4 submissions across topics including small UAV compatible sensors, autonomy for rapid research (NDAA-compliant avionics), nontraditional aviation for wildfire response, CH4 sensing.

- **Leadership continuity with partners** (April 2026): Confirmed BST comfortable taking lead role on unnamed initiative; scope discussions planned.

- **NASA RFI submission strategy** (April 17-30, 2026):
  - **April 17 decision:** Jack Elston requested exhaustive list of all proposal possibilities based on previous and current projects
  - **April 30 final decision:** Decided to submit **4 RFIs** (not 3) due to May 7 deadline:
    1. S0 with stratospheric balloon integration (under Aeronautics Flight Accelerator)
    2. S3 Nomad (revolutionary tech: Energy Autonomy, Environmental Hardening, Edge-AI Navigation, UTM in remote areas)
    3. Autonomy/Avionics proposal
    4. 24-hour fire surveillance with S2 and NightFOX sensor (includes Albatross concept integration)
  - **April 30:** Jack Elston confirmed all 4 RFIs would be submitted

- **NASA Appendix 26B SBIR Phase I proposal submitted** (by October 6, 2026): "All Weather, Terrain and Wind-Aware Autonomous Sensing for Wildfire Aviation" under AERO.7.S26B-0167.

#### LC-ISR Program Strategy (November 2026)
- **LC-ISR pitch timing** (November 15, 2026): 5-minute virtual pitch scheduled for Thursday (8am timeslot preferred over Tuesday). Demo window April-June 2027. Decision to avoid committing to large supplier purchases (Spencer L wing/tailset manufacturing) before pitch results received.
- **LC-ISR procurement approach** (November 17, 2026): Will order single test unit from Spencer L at $27,900 (delivered January 2027) to validate aircraft and manufacturing relationship before committing to two- or three-unit orders ($52,300 or $76,700 respectively). Full NRE ($3,500) paid with first unit; subsequent units reduce per-unit cost.

### Partnership & Collaboration Decisions
- **LMUK partnership engagement** (October 27, 2026): Ongoing collaboration with Lockheed Martin UK; Jack Elston awaiting clarity on timeline and partnership details before finalizing meeting agendas and budgets.

---

## Projects & Initiatives

### Active Government Proposals (as of November 17, 2026)

#### LC-ISR Program (Imminent - Pitch Thursday)
- **Status**: 5-minute virtual pitch scheduled for Thursday, November 20-22, 2026 window (8am timeslot confirmed); Q&A preparation materials being developed in shared Google Drive spreadsheet
- **Configuration**: Custom tube fuselage + wing pylon design with Spencer L wing/tailset manufacturing
  - 3 sets of integrated wings with servos: 4-surface design (flaps + ailerons on wings, horizontal stabilizer, vertical stabilizer) = 6 MKS HV6130 servos total
  - 4.5m span, 40lbs GTOW capacity
  - 15-20% more efficient than Chilli baseline (flight-tested at multiple weights)
  - Full aircraft with servos installed and wiring completed by manufacturer
- **Avionics/Command Architecture Decision Pending**: Two approaches under evaluation:
  - **Custom avionics board**: Full system control, maintains endurance; ~300 hours total work (~40-55 hours firmware/driver, ~25-35 hours board, plus integration/test); longer calendar time due to board fabrication
  - **Starlink integration**: Shorter calendar time (2-4 weeks), cost savings to COVAR, significant bandwidth; adds power integration, SBC-autopilot bridge, ground infrastructure, mechanical mounts (~25-40 hours); loses 1-2 hours endurance; estimated ~300 hours total work
  - **Trade-off analysis**: Jack Elston noting work appears to focus on ATR (Automatic Target Recognition) rather than FMV (Full Motion Video), suggesting custom board approach may better match actual bandwidth requirements
  - **Customer question deferred to Thursday pitch Q&A**: Confirm whether FMV capability is required or if ATR with more constrained bandwidth is acceptable; will inform final technical approach
- **Development Timeline**: 
  - Spencer L quote provided November 17, 2026
  - First aircraft delivery: mid-January 2027
  - Remaining aircraft (if ordered): March 2027
  - Demo window: April-June 2027
  - Design details meeting to establish CAD delivery timeline and interface specifications
- **Design Approach**: Custom tube fuselage + wing pylon designed by BST; motor mounts designed by BST; wing/tail/tailset aerodynamics and integration by Spencer L
- **Procurement Strategy**: Initial order of single test unit ($27,900 all-in with NRE) to validate performance and manufacturing relationship; decision on two- or three-unit orders deferred until after pitch results received. Spencer L pricing:
  - 1 aircraft (January): $27,900 (includes $3,500 NRE for new vertical stab design/tooling/layup schedule + $24,400 aircraft with installed servos and wiring)
  - 2 aircraft: $52,300 total (~$26,150 each for second unit)
  - 3 aircraft: $76,700 total (~$25,567 each additional)
- **Alternative wing inventory**: Spencer L has pre-made wing available but notes layup is too light for LC-ISR target weight specification
- **Financial Gate**: Large purchases deferred pending pitch outcomes; Jack Elston directive maintained

#### NASA SBIR Phase I
- **Status**: Wildfire autonomy proposal submitted October 6, 2026 (AERO.7.S26B-0167); awaiting evaluation and award decisions

#### DIU Low-Cost ISR Demo (S4)
- **Status**: Selected for in-person pitch phase (November 9, 2026)
- **Configuration**: S0 avionics with batteries on large glider aircraft for extended flight time optimization
- **Next Phase**: In-person pitch preparation; physical aircraft build timeline deferred

#### Arctic Edge 28
- **Status**: Submitted November 5, 2026 (S3 and S0-VTOL aircraft variants); awaiting evaluation

#### SOCOM Demonstration
- **Status**: S0-85 and S0-86 aircraft allocated with parachute tube modification requirements

#### LMUK Partnership Initiative
- **Status**: Partnership scope and timeline being finalized; awaiting LMUK response on timeline clarification (as of October 27, 2026)

### Advanced Development
- **S0-AD, S0-LR, S3 Nomad, S0-VTOL, S4 variants**: Multiple aircraft configurations in active development for government applications
- **Arctic cold-weather qualification**: -40°C validation targeted for current sprint; optional -55°C engineering and validation (~$85k) being scoped
- **Autonomy/Avionics integration**: NDAA-compliant systems in development across multiple platforms
- **LC-ISR airframe**: Custom integration of Spencer L wing/tailset with BST tube fuselage and motor mounts; avionics architecture decision pending customer requirements clarification on ATR vs. FMV capability

---

## Action Items & Commitments

### Immediate/Pending (as of November 17, 2026)
- **Thursday Pitch Q&A Preparation**: Team contributing questions and answers to shared Google Drive spreadsheet (link provided by Maciej). **Question identified for customer**: Confirm ATR (Automatic Target Recognition) requirement vs. FMV (Full Motion Video) requirement to inform custom board vs. Starlink avionics architecture decision. Jack Elston added updates to Q&A document on November 17.
- **Spencer L Supplier Relationship**: Initial test unit order ($27,900) to be placed pending Thursday pitch outcomes; subsequent manufacturing quantities deferred until pitch decision received
- **CAD/Interface Coordination**: Spencer L to provide wing/tailset CAD within one week (as of November 17) for fuselage interface and motor mount design by BST team

### Earlier Commitments (October-November 2026)
- **Maciej**: Coordinate LC-ISR pitch presentation for Thursday 8am timeslot; prepare team for 5-minute pitch + Q&A format
- **Jack Elston**: Review pitch materials and Q&A responses; make go/no-go decision post-pitch on manufacturing commitment beyond initial test unit
- **Lisa Marie**: Check availability for later demo slot (April-June 2027) if needed for LC-ISR program
- **Beck Cotter**: Prepared budget and draft agenda for partnership meeting; sent to Jack Elston (U014U9WMK2A) for review before distribution. Budget and agenda documents stored in shared Google Drive folder.
- **Jack Elston (U04CZK4K7P0)** (or team member with this ID): Sending clarification note to LMUK regarding timeline and expectations
- **LMUK contact**: Expected to provide timeline clarity that will inform final budget and agenda adjustments
- **Team (DIU S4)**: Prepare for in-person pitch; design and engineering details for S4 configuration to be finalized for presentation

### Earlier Commitments (July-August 2026)
- **Joshua Fromm**: Leading cold-weather component design starting week of August 5, 2026, targeting -40°C validation with design details meeting to follow
- **Team**: Design details meeting to establish action items and timeline for arctic qualification work

---

## Client & External References

### Government Agencies
- **NASA** (multiple programs: ROSES, SBIR, RFI track, Aeronautics Flight Accelerator)
- **DOD/Air Force** (AFWERX, SBIR/STTR)
- **NOAA** (WPO, SBIR, hurricane/wildfire work)
- **Navy** (SBIR magnetometer, STTR machine vision)
- **SOCOM** (demonstration platform requests)
- **USDA, DOE** (occasional references)
- **Arctic Edge program** (military/defense exercise or competition, November 5, 2026 submission deadline)
- **DIU (Defense Innovation Unit)** (S4 low-cost ISR demo program, in-person pitch phase as of November 9, 2026; LC-ISR program with pitch scheduled for November 20-22, 2026)

### International Partners
- **Lockheed Martin UK (LMUK)** (active partnership, timeline and scope being finalized as of October 27, 2026)
- **Simon** (UK Navy partner/contact)

### Technical & Subcontract Partners
- **University of Colorado (CU)**: Machine vision STTR collaboration
- **Curable Composites**: Edge-constructed group 2 SBIR partnership
- **QuSpin**: Magnetometer integration
- **Cetacean Research Technology**: Hydrophone/acoustic integration
- **Gijs (BNL partner)**: Brookhaven National Laboratory collaboration
- **By Light**: DIU partnership
- **PrecisionTerra**: Subcontract partner
- **SkyMesa**: RF/EW partner
- **C-Astral**: External partner contact
- **Spencer L**: Wing/tailset manufacturer for LC-ISR program; pre-made mold available, proven design validated in flight testing at multiple weights; NRE $3,500 (vertical stab design/tooling/layup schedule); full aircraft with installed servos and wiring $24,400 per unit

### External Customers & Field Contacts
- **Eryan**: NASA radiometry project partner
- **Joe Cione**: NOAA cyclone/hurricane research contact
- **Jana Kolb**: NOAA hurricane contract CO
- **Supercool Earth**: Cloud seeding/icing flight customer
- **Trenton/NexTech**: Temperature capability discussion contact
- **Lisa Marie**: Demo scheduling contact for LC-ISR program
- **Various military personnel**: Angel (PACOM/Northern Edge), Evan (SOCOM), Bradley (Northern Edge), Tony (Northern Edge registration), Chris Meek (Langley/procurement), Chris Leek (Langley procurement contact)

---

## Recurring Topics & Themes

### Proposal Development Cycles
- Continuous pipeline management across NASA (SBIR/STTR/ROSES), DOD (AFWERX, Navy SBIR/STTR, DIU), NOAA (WPO, SBIR), Arctic programs, and other agencies
- Seasonal submission windows driving proposal intensity (April RFI push, November Arctic Edge deadline, October-November SBIR cycles)
- Iterative refinement of proposal strategies based on customer feedback and topic analysis
- Multi-phase competitive processes (selection → in-person pitch → contract award), exemplified by DIU S4 and LC-ISR advancement to pitch phase

### Technical Architecture Decisions
- Ongoing evaluation of custom vs. commercial-off-the-shelf (COTS) solutions for avionics, communication, and data handling systems
- Trade studies balancing development time, endurance, bandwidth, cost, and customization requirements
- Example: Custom avionics board vs. Starlink integration for LC-ISR program, with decision point contingent on customer requirements clarification (ATR vs. FMV)

### Budget & Administrative Coordination
- Regular budget development and formatting by Meredith Needham and Beck Cotter
- Multi-level review processes (draft → Jack Elston → external partners)
- Budget tracking for complex partnerships with multiple entities
- Financial gate mechanisms for deferring large commitments (e.g., Spencer L manufacturing orders pending pitch outcomes)
- Cost variance (COVAR) budget management and optimization strategies (e.g., Starlink approach identified as generating cost savings)

### Technical Integration Challenges
- Payload integration (cameras, sensors, magnetometers, hydrophones, radiometry equipment)
- Aircraft variant customization (folding wings, parachute tubes, cold-weather modifications, aerodynamic optimization)
- Autonomy/avionics alignment with government requirements (NDAA compliance, GPS-denied navigation, terrain following)
- Glider platform optimization for extended endurance (S4 configuration, LC-ISR airframe design)
- Wing/tailset manufacturing partnerships and integration with custom fuselage designs (e.g., Spencer L partnership requiring BST-designed tube fuselage, motor mounts, wing pylon interface)
- Servo system standardization across platforms (MKS HV6130 servos matching S2 configuration standards)

### Partnership & Collaboration Management
- Ongoing scope negotiations with international partners (LMUK as of October 2026)
- Timeline synchronization across multiple stakeholders
- Subcontractor coordination and role definition
- Supplier quality verification and performance validation (e.g., Spencer L flight testing at various weights)
- Risk mitigation through phased procurement approaches (initial test unit validation before full manufacturing commitment)

### Environmental & Operational Qualifications
- Cold-weather operation requirements (-40°C, optional -55°C)
- Arctic operations and extreme environment resilience
- Hurricane/extreme weather resilience
- Extended duration and endurance profiles
- Remote area operations
- Low-cost ISR capability optimization
- Sensor data streaming and real-time processing (ATR vs. FMV capability assessment)

### Pitch & Presentation Strategy
- Compressed presentation formats (5-minute pitches for LC-ISR, Q&A sessions)
- Timing optimization to allow for proposal development time (preference for Thursday vs. Tuesday LC-ISR pitch slot to gain additional preparation week)
- Demo window scheduling and negotiation with program management
- Collaborative Q&A preparation involving technical and proposal teams
- Early customer requirement clarification through pitch discussions to inform downstream technical decisions

---

## Important Resources

### Shared Documents & Folders
- **Google Drive folder** (October 27, 2026): Contains budget and draft meeting agenda for partnership coordination; location: https://drive.google.com/drive/folders/1aXrfLIr-ZFW9i5cYveByW0DRerX8SBzI?usp=drive_link
- **LC-ISR Pitch Q&A Preparation Spreadsheet** (November 17, 2026): Collaborative document for team Q&A development; link provided by Maciej at 2026-11-17 13:09 UTC (docs.google.com/spreadsheets format); Jack Elston added updates November 17, 17:14 UTC

### Suppliers & Manufacturers
- **Spencer L (Wing/Tailset Manufacturer)**: 
  - Primary supplier for LC-ISR aircraft
  - Quote provided: November 17, 2026
  - Full aircraft pricing (including NRE):
    - 1 aircraft: $27,900 (delivered January 2027)
    - 2 aircraft: $52,300 total
    - 3 aircraft: $76,700 total
  - Delivery timeline:
    - First set (or aircraft): mid-January 2027
    - Remaining sets: March 2027
  - Design specs: 4.5m span, 40lbs GTOW capacity, 15-20% efficiency improvement over Chilli baseline, MKS HV6130 servos (x6)
  - Manufacturing includes: full aircraft assembly, servo installation, wiring completion, NRE for new vertical stab design/tooling/layup schedule
  - CAD delivery: within one week of November 17 for fuselage interface and motor mount design coordination
  - Inventory note: Pre-made wing available but layup assessed as too light for LC-ISR weight specification

### Proposal Templates & Support
- External editing/formatting support: Jed and Brian from KS (LC-ISR and DIU decks)
- Format and process coordinator: Annette
- Legal/compliance support: Kreateo (external consultant for USML classification)

### Technical Reference Materials
- NASA SBIR/STTR topic details and appendices (26B referenced)
- AFWERX proposal requirements and submission portals
- NOAA wildfire detection topic specifications
- Arctic Edge program requirements and submission guidelines
- DIU S4 low-cost ISR demo program specifications and pitch guidelines
- LC-ISR program specifications and demo window requirements (April-June 2027)
- Government contracting compliance documentation

---

## Recent Activity

### November 17, 2026 (Latest - Technical Architecture Decision Point)
- **November 17 at 08:10 UTC**: Jack Elston noted new design and firmware/protocol approach with conservative estimates
- **November 17 at 08:37-08:51 UTC**: Maciej presented Spencer L quote and pricing for LC-ISR aircraft:
  - **Quote Summary**: 
    - Full aircraft with servos installed and wiring: $24,400 (MKS HV6130 servos x6)
    - NRE for new vertical stab design + tooling + layup schedule: $3,500
    - Total first unit (January): $27,900
    - Two aircraft: $52,300
    - Three aircraft: $76,700
  - **Supplier flexibility**: Spencer L willing to accept initial single-unit order with option to order additional units afterward
  - **Inventory note**: Spencer L has pre-made wing but notes layup is too light for target weight specification
  - **Assessment**: Maciej characterized pricing as "pretty decent" with significant time savings vs. internal fabrication
- **November 17 at 08:57-08:59 UTC**: Jack Elston initiated custom board vs. Starlink architecture trade study:
  - **Custom board approach**: Removes ~40-55 hours firmware/driver work and ~25-35 hours board work, requires full ground infrastructure and VPN/relay setup; total net ~300 hours; longer calendar time due to fabrication cycle; maintains full endurance
  - **Starlink approach**: Eliminates custom board work (saves 40-55 hours) and driver work (saves 15-20 hours) but adds power integration (25-40W), SBC-autopilot bridge, ground-side software, mechanical mounting for ~1kg panel (25-40 hours), flight test validation; net total hours similar (~300 hours); calendar time 2-4 weeks shorter; loses 1-2 hours endurance; provides significant bandwidth increase
  - **Bandwidth consideration**: Jack Elston noting work appears to focus on ATR (Automatic Target Recognition) vs. FMV (Full Motion Video), suggesting Starlink bandwidth may exceed actual requirements
  - **Cost impact**: Maciej noted Starlink approach generates savings toward COVAR budget
  - **Decision**: Deferred pending Thursday pitch; to be included in customer Q&A as "FMV vs. ATR" question to clarify actual requirements
- **November 17 at 13:09 UTC**: Maciej created collaborative Google Drive spreadsheet for LC-ISR pitch Q&A preparation; team members to contribute questions and answers
- **November 17 at 17:14 UTC**: Jack Elston added updates to Q&A spreadsheet

### November 9, 2026
- **November 9 at 12:19 UTC**: Maciej announced DIU S4 proposal selection for in-person pitch phase. Confirmed as "low-cost ISR demo" configuration: S0 avionics loaded with batteries mounted on large glider aircraft to maximize flight time. Noted timeline for physical aircraft build is not imminent; focus currently on pitch preparation.
- **November 9 at 12:24 UTC**: Beck Cotter responded with acknowledgment emoji, indicating awareness and support of DIU advancement.

### November 5, 2026
- Dan Prendergast commended proposal submitter (@U07FN4QSNDN) for successfully completing Arctic Edge 28 submissions. Two proposals submitted: S3 and S0-VTOL aircraft variants. Recognition indicates high-quality proposal preparation and successful deadline management.

### October 2026
- **October 27**: Beck Cotter prepared budget and draft agenda for upcoming partnership meeting with LMUK. Documents shared in Google Drive folder pending Jack Elston's review before external distribution. Jack Elston (U04CZK4K7P0) sending clarification communication to LMUK regarding partnership timeline and expectations. Further budget/agenda adjustments awaiting LMUK response on timeline.

### Earlier Notable Recent Activity (August-October 2026)
- **October 6**: NASA Appendix 26B SBIR Phase I proposal submitted on wildfire autonomy topic (AERO.7.S26B-0167)
- **Late September/Early October**: LC-ISR and DIU slide deck final preparation with external editors (Jed and Brian from KS)
- **July 24**: SOCOM demonstration aircraft (S0-85, S0-86) allocated with parachute tube modification requirements
- **July 30**: Arctic customer cold-weather qualification approach finalized; Joshua Fromm designated to lead -40°C design validation efforts starting week of August 5

---

**Last Updated:** November 17, 2026