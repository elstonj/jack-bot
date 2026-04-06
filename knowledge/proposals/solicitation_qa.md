# DARPA Albatross Solicitation Q&A

## Document Metadata
- Type: Questions and Answers (Q&A) document for solicitation
- Client/Agency: DARPA
- Program/Solicitation: DARPA Albatross (autonomous soaring for extended endurance)
- Date: 2024 (document modified through December 19, 2024)
- BST Products/Systems Referenced: None
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
This is a Q&A document from DARPA's Albatross program solicitation, addressing 107 questions from prospective bidders. Albatross aims to develop autonomous soaring technologies for small unmanned aircraft systems (sUAS) to achieve 75% energy reduction over baseline while maintaining mission completion and prediction accuracy. The document clarifies technical requirements, testing protocols, aircraft specifications, and submission requirements.

## Technical Approach Overview
Albatross focuses on two Technical Challenges (TCs):
- **TC-1:** Autonomous soaring flight planning and prediction
- **TC-2:** Real-time soaring detection and exploitation

The program emphasizes a test-driven development model with three test events (TEs) over the contract period, preceded by practice test events (PTEs). All performers must address both TCs to meet program metrics.

## Key Program Requirements & Specifications

### Aircraft Requirements
- **Class:** Group 1 sUAS, under 55 lbs (Group 2 considered but less preferred due to cost/safety)
- **Range:** 50-150 km capability with excursions possible
- **Endurance:** Aircraft should fly 50 miles without soaring to establish baseline
- **Speed:** No threshold specified, but must efficiently traverse environment
- **Altitude:** Any altitude within National Airspace System (NAS) permitted; higher-altitude capable ranges will be prioritized
- **Launch/Recovery:** Small commercial vessel (~50 feet) assumed for sea operations; flexible approaches acceptable
- **Configuration:** Single aircraft preferred, but multiple distinct UAS for different test events allowed if techniques are widely applicable

### Energy & Performance Metrics (Equally weighted)
- **75% energy reduction** over baseline (through soaring)
- **15% prediction accuracy** (for soaring lift prediction)
- **100% mission completion** rate
- **Baseline energy establishment:** Open to proposer methods; ideally flying same environment/mission, but flexibility allowed
- **Power measurement:** Recording at 100 Hz onboard acceptable; telemetry at 10 Hz minimum; voltage drop tracking acceptable with justification; all onboard compute/avionics energy consumption counts against soaring benefit

### Soaring Techniques
- No single soaring type mandated (dynamic soaring, ridge soaring, thermal soaring all considered)
- Wide array of techniques needed for varying weather/environmental conditions
- Dynamic soaring over water with ship deck landing noted as most challenging condition
- Ground-effect exploitation classified as enhancement, not baseline

### Communications & Data
- Two-way communications allowed; uplink to vehicle permitted
- Downlink required for aircraft location identification
- Loss of link and GPS degradation should be assumed (RF-denied ops not focused effort)
- Safety-critical data must be telemetered in real-time
- Communications rate not dictated by DARPA; proposers to justify approach
- Internet access at test sites planned but not guaranteed

### Sensors & Payloads
- Camera use permitted for Albatross development (video review required before removal from test site)
- Sensor adaptation/integration preferred over full development
- Payload constraints: should not interfere significantly with vehicle safety of flight
- Sensing/detection of lift sources emphasized as critical to success

### Baseline Aircraft Concept
- Baseline configuration must be as similar as possible to soaring configuration except for soaring-specific added equipment
- Baseline does NOT include soaring payloads or sensors
- Any added mass/equipment counted as detracting factor toward soaring goal
- Vehicles must demonstrate established baseline capability before soaring test events
- Instruments inherent in baseline configuration not counted against energy usage; added instruments for soaring are counted

## Test Event Structure

### Practice Test Events (PTEs) & Test Events (TEs)
- **Location:** Practice test events at same location as corresponding test event
- **Duration:** Week-long (Monday-Friday) with 3 specific flight days per test event
- **Timing:** Daylight operations only (no night ops)
- **Simultaneous Operations:** Ideally yes, but requires coordination
- **Setup Time:** Up to one day expected, but minimizing setup time encouraged
- **Readiness Review:** System checkout performed prior to soaring test events
- **Aircraft Attrition:** Performers responsible for providing backup sUAS sufficient for program attrition; each test includes multiple flights

### Test Planning & Range
- Test plan developed iteratively in months prior to each test with sufficient lead time for range approval
- DARPA providing range for PTEs and TEs only; performers strongly recommended to access additional contractor-provided sites for development
- Range support team selected by DARPA to handle scouting, range control, approvals; range locations not yet finalized (DARPA open to options)
- DTED terrain data available upon request (Level 2 possible if conditions met); accuracy/resolution not guaranteed
- High Performance Computing access provided as Government Furnished Equipment (GFE), though performers may use own resources or both

### Performance Assessment
- Performance evaluated on results achieved during week-long test event
- Flexibility to adjust measurements if results indicate need
- Three flight test events provide opportunities for incremental improvements
- Loss of aircraft: if cause not safety concern, testing resumes; if safety concern, mitigation required before resuming
- Metrics flexibility: more rigorous measurement methods encouraged in abstracts/orals if proposed

### Safety & Approvals
- Each range must independently approve UAS (no centralized list of approved COTS systems)
- Loss of link and GPS behaviors must be addressed for range approval
- Payload should not interfere with vehicle safety of flight
- Any UAS modifications during test must be documented with range safety
- FAA regulatory compliance required (Part 107 compliance easier for aircraft <55 lbs)

## Baseline Mission Scenarios
- **Range/Endurance missions:** No specific time cap beyond operational times
- **Timed waypoint missions:** Meeting timed waypoint may be critical
- Reference examples provided for both loiter and range-oriented missions

## Technical Approach Preferences

### Soaring & Flight Planning
- Preflight planning tool: DARPA primarily interested in function over form; reliability key for users
- Mission flight path computation: allowed on ground (GCS sends updates) or onboard
- Alternate energy extraction techniques (e.g., wind energy): possibly acceptable with description in abstracts/orals
- Multi-aircraft coordination: technically allowed but must be justified; single-vehicle performance should be understood and measurable

### Propulsion & Power Systems
- Internal Combustion Engine (ICE): not precluded but preference against due to cost/complexity
- Liquid fuel systems: acceptable assuming power consumption can be monitored at high rate
- Onboard energy storage: no particular limitations anticipated

### Architecture & Interfaces
- Open-source interfaces acceptable (MAVLINK examples given)
- No requirements against open-source; proposers to recommend best approach
- Open architecture framework desired for wide application across defense

## Submission & Award Requirements

### Abstract & Proposal
- 5-page abstract limit (references/citations not included in page count but material beyond 5 pages unlikely to be reviewed)
- No specific ROM, template, or PI bio requirement stated; see Program Statement (PS) for details
- Should address: technical approach, team composition, schedule, transition plan, FAA compliance strategy

### Oral Proposals
- Selected abstracts advance to oral presentations (couple days allocated for reviews)
- Three weeks after notification to prepare oral proposal
- Appendices (5 required) released only to oral presentation selectees:
  - Integrated Master Schedule (IMS) down to Level 4/Activities in contractor-created format; should capture critical elements of technology advancement and cost
  - Value Based Assessment questions (answers encouraged but not required)
  - Model OT Agreement (released with oral invitation)
  - Other appendices TBD
- No template provided for IMS format

### Team Composition
- Full team building encouraged; partial bids less desirable
- Government prefers awards addressing both TCs collectively; teaming encouraged for partial capabilities
- Non-traditional contractors: definition and "significant extent" participation assessed per contribution to cost reduction, schedule improvement, or performance increase; should be on critical path
- Prime contractors may not simultaneously be subs on competing teams (unless differences clearly justified; raises concerns about resource allocation to multiple teams)
- Universities encouraged with partnerships; partnerships support universities interested in specific technological needs

### Deliverables & Transition
- Items developed under effort and interfaces to SOTA are critical outputs: software, firmware, hardware, designs, documentation
- sUAS platform may be included or just s/w + docs (clarity in commercialization plan desired)
- Commercialization/transition plan desired (not major program element but emphasized by DARPA)
- Immediate transition partner not required
- DARPA actively engaged with potential transition partners and will invite to test events
- No specific platform identified as transition-preferred; transition partners open to multiple solutions
- Both tactical relevance and programmatic performance goals valued

### Cost & Resources
- Performers provide platform, transport, setup, and operations support
- DARPA provides range access and interface for PTEs/TEs
- Government resources: HPC access (performers may use USG resources, own, or both)
- No cost/duration limits specified for IMS items; focus on critical technology advancement elements

## Award Timeline
- Expected start date: Spring 2025 (awards by Spring 2025)

## Notable Details

### External Dependencies
- Weather updates, airspace condition changes, traffic density variations acceptable
- Well-defined interface to government strongly preferred for external dependencies

### Aircraft Selection & Design Evolution
- Aircraft design changes between test events possible but not preferred
- Preference for developing single aircraft configuration that explores different soaring in varying conditions
- PS does not prohibit aircraft changes between test events
- System checkout prior to soaring test events establishes baseline capability

### Unique Constraints & Considerations
- Range-approved COTS systems variable by range; proposers should have experience obtaining range approvals
- Over-water operations emphasized; full program concept (not just water ops) should be addressed
- Detect-and-Avoid capability for BVLOS: not specifically requested but may be considered if helps achieve program metrics
- Indoor testing: may be viable for team verification between PTEs/TEs
- Public visibility flight testing: allowed (Albatross CUIG does not identify sight-sensitive elements)
- Multiple small distinct UAS use: permissible for different test events if techniques widely applicable; niche solutions less desirable

### Evaluation & Flexibility
- Evaluation criteria per PS (not specified in this Q&A)
- Evaluation weights: all three metrics (75% energy reduction, 15% prediction accuracy, 100% mission completion) equally desired
- Communication efficiency not tested as performance criterion
- Proposers may suggest more rigorous performance measurement methods
- "Grey area" issues (e.g., whether certain instruments count toward energy assessment) handled case-by-case; totality of progress toward program objectives considered in evaluation

### FAA & Regulatory
- FAA Part 107 compliance easier for <55 lb aircraft (more latitude for contractor-provided testing)
- Proposers must state compliance with applicable laws/regulations or method for obtaining exemptions
- FAA Regulatory Compliance must be addressed in abstract proposal

---

## Document Quality Note
This is a comprehensive, well-structured Q&A document providing detailed guidance to prospective bidders on technical, programmatic, and administrative aspects of the DARPA Albatross solicitation. It reflects iterative refinement of requirements through Q&A process. No BST-specific content present.