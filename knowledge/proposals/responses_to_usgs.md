# Responses to USGS

## Document Metadata
- Type: Email response to client questions/concerns
- Client/Agency: USGS (United States Geological Survey)
- Program/Solicitation: USGS volcano monitoring project; NASA Phase II E matching funds
- Date: 2019-07-19
- BST Products/Systems Referenced: S2, S2 XT UAS
- Key Personnel: Jack Elston (BST), Angie (USGS contact), Christoph (recipient of earlier platform documentation)

## Executive Summary
Jack Elston responds to USGS questions about a proposed volcanic observation deployment, clarifying the role of NASA Phase II E matching funds versus USGS funding, and defending BST's technical approach, capability claims, and budget decisions for a planned deployment to Makushin Volcano in Alaska.

## Technical Approach
**S2 Aircraft Enhancement Strategy:**
- Add VTOL (vertical takeoff and landing) capabilities to S2 for operation in remote regions without runways
- Develop high-wind VTOL capability to increase operational envelope
- Develop custom payload specifically for USGS volcanic observation needs
- Enhance subsystems and develop mission-specific software for atmospheric sampling
- Implement on-board data archiving with accurate timestamps
- Create software framework to convert compressed on-board data to ASCII tabular format compatible with USGS data standards
- Develop wireless ground station connection using open-source SDK for real-time data display
- Plan deployment to Makushin Volcano with multiple daily flights requiring additional batteries

**Communication & Range:**
- Target operational transmit range of ~40km (not full 50km aircraft range, as on-station sampling time is required)
- Wireless telemetry to ground station for real-time data access
- Investigation of antenna/radio requirements for extended range as part of NASA matching funds work
- No video transmission planned (noted as cost-prohibitive for distance involved)

**Flight Operations:**
- BVLOS (Beyond Visual Line of Sight) flights desired but not guaranteed; fallback is ground observers positioned at required distance from aircraft
- Remote launch planned if FAA waivers permit; backup is foot-carry to launch site and observer positioning

## Products & Capabilities Described

**S2 / S2 XT UAS:**
- Small UAS (typically <20 lbs with payload, FAA Part 107 compliant at 55 lb threshold)
- Maximum altitude: 20,000 ft ceiling
- Endurance: 90 minutes with 5 lb payload
- Operating temperature range: down to -20°C
- Payload capacity: 5 lb
- Payload bay: 8" x 12" section
- Runway-independent operation (no runway required)
- Corrosion-resistant construction for harsh environments
- **Unique capabilities claimed:**
  - Swappable/custom payload integration
  - Real-time custom payload message transmission to ground
  - On-board graphing of custom sensor data
  - In-flight flight pattern creation for atmospheric sampling
  - Open-source SDK for third-party system integration

**Comparative advantages cited over competitors:**
- C-Astral, UAV Factory, Altavian listed as similar platforms lacking BST's specific capabilities

## Use Cases & Applications
- **Makushin Volcano monitoring** (Alaska) - primary USGS deployment target
- **Volcanic gas/emission sampling** - inferred from context and atmospheric sampling capability
- **Remote site operations** - regions requiring multiple daily flights without runway access
- **Harsh environment operations** - corrosive volcanic gases, variable weather conditions
- **Atmospheric data collection** - real-time sensor data transmission and ground-based visualization

## Funding & Budget Details
- **USGS funding:** $100K
- **NASA Phase II E matching funds:** $104K (from NOAA subcontract NASA match)
- **Matching rules constraint:** NASA funds must "advance innovations developed under Phase II via further R&D on active Phase II contracts"; only dollar amounts paid to BST can be matched 1:1
- **Fund allocation split:** Only ~50% of proposed work items directly address USGS needs; remaining 50% support NOAA project requirements
- **USGS-funded work includes:** Custom payload development, mission-specific software, deployment execution
- **NASA-funded work (not USGS-line-item):** VTOL development, high-wind capability, long-range telemetry, payload data display framework, aircraft equipment/materials, operational range testing
- **Budget items requiring clarification/adjustment:**
  - Car rental costs proposed
  - Calibration gases for bench testing (BST wants USGS to supply)
  - Additional batteries for continuous daily operations
  - Data archiving/conversion software development

## Key Clarifications Provided

**Data Handling:**
- All collected data (sensor data + aircraft state) logged on-board with timestamps
- Conversion from compressed on-board format to ASCII tabular/spectral format required for USGS data standards
- Data available to third-party systems via wireless ground station connection during flight
- Short-term storage only at BST; no long-term archiving commitment from BST

**VTOL Capability:**
- Under concurrent development for NOAA subcontract on different aircraft
- S2 VTOL inclusion motivated by possibility of NASA match funding
- Not designed specifically for USGS project but may benefit deployment depending on selected operational site
- Cannot be formally changed as NASA proposal already submitted due to timing constraints

**Communications:**
- 40km operational transmit range realistic and testable; 50km aspirational but would leave no time for on-station sampling
- Video transmission excluded as cost-prohibitive for distance
- Observer positioning required for legal compliance if BVLOS waiver not granted

## Notable Details

**Contractual/Regulatory Context:**
- NASA Phase II E funding constrained by specific R&D continuation rules
- FAA Part 107 compliance maintained (small UAS classification)
- FAA waivers required for remote launch and/or BVLOS operations
- USGS not authorized to direct allocation of NASA matching funds

**Project Complexity Issues Flagged:**
- Jack notes "fundamental disconnect" between parties on funding/scope
- Proposes separating NASA and USGS budgets to reduce confusion
- Multiple contingencies flagged (BVLOS waiver status, range testing requirements, observer positioning)
- Acknowledges hour estimates may be underestimated in some tasks

**Tone/Approach:**
- Email frames this as clarification of earlier miscommunications
- Offers phone call to resolve disagreements
- Defensive on several points (VTOL necessity, data archiving scope, range capabilities)
- Pragmatic on fallback plans and trade-offs