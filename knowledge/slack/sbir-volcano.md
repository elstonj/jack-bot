# #sbir-volcano

## Overview
This channel is primarily used for coordinating Black Swift Technologies' SBIR (Small Business Innovation Research) projects focused on volcanic monitoring using unmanned aircraft systems. The main projects involve deploying S2 and S3 aircraft with specialized sensor payloads to study volcanic emissions and activity, with NASA oversight and collaboration with USGS scientists.

Key participants include:
- **Jack Elston** (Project lead, technical decisions, circuit design, documentation, flight logistics, equipment assessment)
- **Joshua Fromm** (Payload development, technical integration, diagnostics, aircraft inventory tracking)
- **Danny Troke** (Flight operations, equipment)
- **Maciej Smolka** (Regulatory, reporting, flight planning, translation support, payload documentation, external liaison coordination)
- **Dan Prendergast** (Flight planning software, technical development, logistics, contracting inquiries, documentation, S3 operator's manual, data collection patterns, site selection analysis, translation testing, Mission Plan document development, vendor coordination)
- **Meredith Needham** (Administrative support, travel coordination)
- **Ethan Domagala** (Flight operations support)
- **Nate** (Remote ID/registration support)
- **Alex Lomis** (Team member, availability flexible)
- **Spencer Hoehl** (Flight permissions tracking, external liaison coordination, partner communication, regulatory contact identification, AFAC liaison efforts)

The channel covers activities from 2020 through October 2026, with high activity during deployment periods and report deadlines.

## Key Decisions

**Mission Parameters & Equipment (2020-2021)**
- Switched from 1 sq km to 1km x 0.5km mapping area to fit S2 mission profile
- Selected S2-9 as primary aircraft (75g lighter than S2-3)
- Approved dual payload approach: photogrammetry payload vs. gas detection payload
- Set payload door operation range 1500-2000 with neutral at closed position
- Determined total payload replacement cost at ~$20,200

**Radio/Communications (2021)**
- Reduced radio transmit power to 23dBm for FCC Part 15 compliance
- Selected 1W transmit power with 14dBi yagi antenna configuration
- Decided on standalone 2.4GHz video system instead of dual data/video feed

**Propulsion System (2022-2023)**
- Selected 15x10E propeller over 14x12E based on 26-29% better power efficiency in cruise
- Switched to new battery configuration enabling missions old setup couldn't complete

**Aircraft Selection for High-Altitude Missions (2024)**
- Decided to focus on S3 as primary aircraft for Mexico deployment due to S2 altitude/performance limitations at 19,500-20,000 ft

**Export & Regulatory (April 2026)**
- Determined that S3 falls under "Temporary Export Exception" as a "Tool of the Trade" - no export license required for Mexico deployment
- Required documentation identified: Letter of justification, proof of ownership, FAA registration, proof of USGS contract
- Carnet needed to avoid import fees (1-2 day turnaround)
- FAA Remote ID registration obtained: 20686S30001

**Mexico Deployment Personnel & Timeline (April 2026)**
- Decision made to defer Mexico deployment from planned April 19-27 window to later date (decision finalized by April 16, 2026)
- Reason: S3 aircraft requiring repairs; issue to be resolved and testing completed by Friday April 18 required before proceeding
- Deferral allows proper S3 testing and validation rather than proceeding with incomplete aircraft readiness

**Gas Payload Isolation Circuit Design (April 18, 2026)**
- **Opto-isolator Configuration**: Determined that single-side isolated optocoupler (SparkFun OPT3001) insufficient for simultaneous TX/RX isolation; requires dual configuration
- **Solution Selection**: Decided to use ADUM1201 magnetic isolator instead of dual optocoupler boards - simpler approach with better high-speed capability
- **Rationale**: ADUM1201 selected for superior baud rate support; will be positioned near high-power lines with expected robust noise immunity
- **Potential Secondary Application**: Discussed possible future application of magnetic isolators on CAN lines to motor and pivot servo to mitigate noise, though impact may be limited

**Operating Manual Documentation (April 28, 2026)**
- **Decision**: Jack Elston initiated development of operating manual as required for flight permissions
- **Approach**: Overleaf document shared with team members for collaborative editing and refinement
- **Content Generation** (May 19, 2026): Jack Elston confirmed manual contains "AI fill in the gaps" content but assessed as "accurate enough"
- **Compliance Expectation**: Jack Elston indicated that AFAC (Mexican authorities) unlikely to scrutinize manual extensively

**C-130 Integration & S0/S0-AD Procurement (June 13, 2026)**
- **Clarification needed on funding**: Jack Elston questioned whether client is paying for S0-AD aircraft, deployment, or both
- **C-130 Setup Work**: Acknowledged additional work required to configure aircraft for integration with C-130 cargo aircraft and establish handoff procedures
- **S0 Aircraft Spares**: Decision to procure extra S0 aircraft units; inventory tracking confirms procurement on schedule

**S0 Aircraft Inventory Status (June 14, 2026)**
- Confirmed S0 aircraft delivery numbers accurate in Asana project management system
- Projected total inventory of approximately 37 S0 aircraft units on track to be delivered
- No inventory shortage issues identified

**Photogrammetry Payload Conversion for Popocatépetl (July 1, 2026)**
- Joshua Fromm inquiry regarding required modifications to photogrammetry payload originally used in Kentucky deployment for volcano mission application
- Gas payload parts on order with projected arrival and conversion completion before end of July 2026
- Plan includes test flight before full deployment

**Photogrammetry Payload/System Performance Validation (July 2, 2026)**
- Jack Elston confirmed that photogrammetry payload system "worked quite well" - assessment indicates readiness for Popocatépetl deployment

**Takeoff/Landing Location Selection for Popocatépetl (July 16-17, 2026)**
- **Issue**: Three candidate takeoff/landing sites identified, with analysis of southernmost location's proximity to crater
- **Constraints**: Paso de Cortés confirmed as end of public access - may be required as operational base
- **Options**: Jack Elston recalled that the closer location (presumably the southernmost site) was discussed as an option but Paso de Cortés may be necessary operational constraint
- **Status**: Decision finalized - operations will likely proceed from Paso de Cortés as the designated takeoff/landing location
- **Reference tool**: Google Earth project created documenting candidate locations

**Popocatépetl Flight Planning Parameters (July 20, 2026)**
- **Altitude Profile Decision**: Selected level flight at 120m AGL above highest volcano point (5,380m elevation) over terrain-following approach
- **Rationale for Level Flight**: Reduces mission complexity from 85 waypoints/90km (terrain-following) to 34 waypoints/39km (level); maintains communication line-of-sight on far side of crater; avoids excessive climbing/descending in challenging terrain and wind environments at altitude where S3 may struggle to maintain required climb rates
- **Approved Parameters**: 80% overlap in both directions maintained
- **Performance Consideration**: S3 will operate above 100 km/h true airspeed at that altitude

**Operating Manual Translation & Finalization (July 23, 2026)**
- **Translation Approach Decision**: Evaluating online and offline translation tools for Spanish language conversion
  - **Online Option**: ForgeFile service (claims GDPR compliance with automatic deletion of documents after translation)
  - **Offline Option**: Cassandre Python tool for local processing without external data transfer
- **Testing Strategy**: Dan Prendergast to test PDF translation first via ForgeFile; fall back to .tex file processing if PDF approach fails
- **Current Status**: Operating manual finalized and ready for translation after document editing conflicts resolved

**Photogrammetry Payload Camera Upgrade Discussion (July 27, 2026)**
- Jack Elston flagged that both Sony A5100 camera (16mm lens) and FLIR equipment in photogrammetry payload should be reviewed for potential upgrades
- **Rationale**: Current equipment sufficient

**Mexico Deployment Status - Indefinite Hold (October 28, 2026)**
- **Decision**: Mexico deployment placed on hold indefinitely pending AFAC (Mexican FAA equivalent) approval
- **Trigger**: Authorization required from Mexican regulatory authorities before deployment can proceed
- **Contingency Planning**: When/if AFAC approval received, deployment date will be set far enough in future to allow completion of all outstanding logistics and coordination tasks
- **Outstanding Tasks Identified**:
  - Aligning schedules with USGS and CENAPRED partners
  - S3 aircraft export procedures
  - Battery shipping arrangements
  - Travel arrangements for team

## Projects & Initiatives

### Popocatépetl (Volcano) Monitoring Mission
**Status**: On hold indefinitely pending AFAC approval (as of October 28, 2026)

**Project Parameters**:
- Primary aircraft: S3 (selected for high-altitude capability)
- Target volcano: Popocatépetl, Mexico (5,380m elevation)
- Operational base: Paso de Cortés (designated takeoff/landing location)
- Flight profile: Level flight at 120m AGL with 34 waypoints, ~39km total distance
- Payload: Photogrammetry system with Sony A5100 camera (16mm lens) and FLIR equipment
- Coverage: 80% overlap in both directions
- Partner agencies: USGS, CENAPRED (Mexican volcanic monitoring agency)

**Recent Progress**:
- Operating manual finalized in English (with AI-assisted content)
- Manual translation to Spanish in progress (using either ForgeFile or Cassandre tools)
- Photogrammetry payload system validated as functional and ready
- S3 aircraft export documentation prepared (requires Carnet and proof of documentation)
- Flight planning completed with optimized waypoint design

**Blockers**:
- AFAC (Mexican FAA) approval outstanding as of October 28, 2026
- S3 aircraft repairs required before deployment (noted in April 2026)

### C-130 Integration Project
**Status**: In progress (ongoing as of June 2026)

**Scope**:
- Configure S0/S0-AD aircraft for integration with C-130 cargo aircraft
- Establish handoff procedures for deployment operations
- Procure extra S0 aircraft units for inventory (~37 units total projected)

**Current Status**:
- Clarification needed on client funding scope (aircraft vs. deployment vs. both)
- Additional work acknowledged but not yet scheduled

### Gas Payload Development (Isolation Circuit)
**Status**: Decision phase complete, implementation underway

**Technical Specifications**:
- Isolation solution: ADUM1201 magnetic isolator (selected over dual optocoupler approach)
- Application: Protects gas sensor communications from electrical noise in high-power aircraft environment
- Positioning: Near high-power aircraft lines
- Potential secondary application: CAN lines to motor and pivot servo

## Action Items & Commitments

### Pending (as of October 28, 2026)
- **Dan Prendergast & Team**: Await AFAC approval before proceeding with Mexico deployment
- **USGS/CENAPRED Coordination**: Schedule alignment required once deployment date re-established
- **Dan Prendergast**: Complete S3 export procedures when deployment date confirmed
- **Meredith Needham**: Coordinate battery shipping and travel arrangements once deployment timeline set
- **Operations Team**: Prepare all logistics for deployment (date TBD pending AFAC approval)

### Completed
- Operating manual finalized (English version) - Jack Elston (April 28 - July 23, 2026)
- Manual translation to Spanish in progress - Dan Prendergast testing ForgeFile/Cassandre tools (July 23, 2026)
- Flight plan optimization for Popocatépetl - Dan Prendergast (completed by July 20, 2026)
- S3 aircraft export documentation preparation - completed (April 2026)
- Photogrammetry payload validation - Jack Elston (July 2, 2026)

## Client & External References

### Government/Regulatory Partners
- **NASA** (SBIR program oversight)
- **USGS** (US Geological Survey - scientific collaboration, volcanic monitoring)
- **CENAPRED** (Centro Nacional de Prevención de Desastres, Mexico - volcanic monitoring partner)
- **AFAC** (Mexican FAA equivalent - flight permissions/approval authority)
- **FAA** (US Federal Aviation Administration - Remote ID registration 20686S30001)

### External References
- Mexico Popocatépetl volcano deployment location
- C-130 cargo aircraft integration (unspecified client/partner)

## Recurring Topics & Themes

**Regulatory Compliance & Export**
- Ongoing focus on Mexican flight permissions and AFAC approval requirements
- Documentation and export procedures for aircraft transit to Mexico
- Operating manual development and translation for regulatory compliance

**Deployment Readiness Assessment**
- Regular evaluation of aircraft condition and mission readiness before proceeding
- Equipment functionality validation (payloads, cameras, sensors)
- Logistics coordination (scheduling, shipping, travel)

**High-Altitude Flight Operations**
- Aircraft performance at extreme elevations (19,500-20,000 ft and above)
- Mission complexity trade-offs (terrain-following vs. level flight)
- Navigation and communication line-of-sight requirements in mountainous terrain

**Payload Integration & Technical Development**
- Sensor payload modifications for specific mission requirements
- Electrical isolation and noise mitigation for specialized equipment
- Performance validation and equipment upgrades assessment

**Inventory & Procurement Management**
- S0/S0-AD aircraft inventory tracking and procurement status
- Spare parts and equipment ordering with delivery timeline management

## Important Resources

**Project Management**
- Asana project management system (S0 aircraft inventory tracking)

**Technical Documentation**
- Overleaf collaborative document (Operating Manual in English)
- Google Earth project (Popocatépetl candidate site locations)
- Mission Plan document (flight planning specifications)

**Software Tools**
- ForgeFile (online PDF translation service, claims GDPR compliance)
- Cassandre Python tool (offline local PDF/LaTeX translation)

**Equipment References**
- S2 and S3 unmanned aircraft systems
- S0/S0-AD aircraft (for C-130 integration project)
- Sony A5100 camera with 16mm lens (photogrammetry payload)
- FLIR thermal imaging equipment (photogrammetry payload)
- ADUM1201 magnetic isolator IC (gas payload isolation)

## Recent Activity

**October 28, 2026**
- **Announcement**: Dan Prendergast announced Mexico deployment placed on indefinite hold pending AFAC approval
- **Rationale**: Regulatory authorization from Mexican FAA equivalent required before proceeding
- **Contingency Plan**: Once approval received, deployment date will be established with sufficient lead time to complete outstanding logistics (schedule coordination with USGS/CENAPRED, S3 export, battery shipping, travel arrangements)
- **Impact**: All deployment activities suspended until regulatory clearance obtained

**July 23-27, 2026**
- Operating manual translation methodology finalized
- Photogrammetry payload equipment reviewed (camera upgrade discussion initiated)
- Manual ready for Spanish translation after resolving document editing conflicts

**July 20, 2026**
- Flight planning parameters optimized for Popocatépetl mission
- Level flight approach selected over terrain-following to reduce complexity and improve feasibility

**July 1-2, 2026**
- Photogrammetry payload system validated as functional
- Gas payload parts confirmed on order with conversion completion targeted before end of July