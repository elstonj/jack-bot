# Autonomous Ship-Relative UAS VTOL Recovery for Persistent Maritime Observation

## Document Metadata
- Type: White paper / Capability proposal
- Client/Agency: NOAA Office of Marine and Aviation Operations (OMAO) / Uncrewed Systems Operations Center
- Program/Solicitation: NOAA Standing Broad Agency Announcement (open through 30 September 2026); potential SBIR Phase III sole-source under 15 U.S.C. § 638(r)
- Date: August 17, 2026
- BST Products/Systems Referenced: S0-VTOL, S3, SwiftCore (Flight Management System), SwiftPilot (autopilot), SwiftStation (ground station), SwiftTab (operator interface), SwiftSTL (machine-vision landing-site assessment), Swift Safe-To-Land (semantic segmentation)
- Key Personnel: Cory Dixon (last editor)

## Executive Summary
BST proposes to develop and demonstrate autonomous ship-relative recovery capability for VTOL aircraft (S0-VTOL platform) operating from NOAA research vessels. The solution combines differential-GPS approach navigation with cooperative visual or infrared terminal guidance, eliminating manual pilot control during the most demanding recovery phase. Hardware-in-the-loop and surrogate testing will reduce risk before vessel demonstration, delivering a reusable integration package that supports fleet scaling and future transition to the larger S3 platform.

## Technical Approach

### Core Navigation & Guidance Architecture
- **Ship-relative navigation frame**: Establishes common reference between aircraft and vessel using onboard S0 sensors, SwiftCore flight-management functions, and ship-provided position, velocity, heading, and motion data
- **Differential GPS**: Supports outer approach corridor capture and initial vessel-motion matching
- **Cooperative terminal guidance**: Visible or infrared deck target provides independent relative-pose observation during final approach; enables transition from approach to hover, alignment, descent, and touchdown
- **Layered fusion architecture**: SwiftCore fuses differential GPS and terminal-sensor data to avoid single-point-of-failure dependence on any navigation source
- **Motion compensation**: Aircraft matches vessel motion and heading while remaining clear of superstructure keep-out zones

### Safety & Operational Gating
- Explicit hold, wave-off, go-around, abort, and manual-takeover behavior
- Pre-recovery safety gates evaluate: relative-navigation integrity, target confidence, aircraft state, deck-zone availability, approach geometry, environmental limits
- Failed gate commands hold or wave-off; loss of guidance during descent triggers go-around
- Ship master retains authority over deck availability and recovery continuation
- Manual takeover available under approved procedures

### Ground Control & Mission Management
- SwiftStation manages aircraft data link and ship-reference interface
- SwiftTab provides mission configuration, operator monitoring, status annunciation, and manual-control access
- UAS operator monitors aircraft, payload, telemetry, navigation integrity, and recovery status
- Data flows from aircraft through ground station to operator and designated users

### Vessel Integration
- Cooperative target (visual or infrared) avoids permanent ship modification
- Ship reference supplies time-aligned navigation and motion information
- Interface-control information and coordinate-frame definitions documented during baseline phase
- Approved approach direction and superstructure keep-out geometry account for vessel heading and motion

## Products & Capabilities Described

### S0-VTOL (Soloable VTOL - Lower Cost Iterative Platform)
- **What it is**: Commercial small VTOL aircraft serving as the primary test article for autonomous-recovery development
- **Proposed use**: Ship-relative recovery demonstration on moving vessel; iterative platform before S3 transition
- **Configuration**: Four aircraft deliverable to NOAA (3 operational/test articles + 1 attrition/spare)
- **Specifications**: Configured with differential-GPS receivers, cooperative-target sensors (visual/infrared), onboard recording, instrumentation for deck motion and relative-wind correlation
- **Operational heritage**: Integration with NOAA P-3 aircraft established procedures for deployment, RF integration, ground-station operation, operator displays, and environmental data delivery; measurements validated against towers, sondes, tail Doppler radar, and modeled fields

### S3 (Longer-Range, Higher-Payload Mission Platform)
- **What it is**: Next-generation VTOL aircraft with greater endurance and payload capacity than S0
- **Design requirements**: Up to 110 minutes flight time, 2.7 kg (6 lb) payload, 20,000 ft MSL ceiling, 110 km range, 30-knot wind resistance, IP42 ingress protection
- **Proposed use**: Transition path for validated ship-relative recovery architecture; extends to payload-intensive atmospheric, radiometric, electro-optical, fisheries, and coastal missions across NOAA line offices
- **Integration approach**: Option 4 transfers validated S0 architecture to S3 over 3-6 months; delivers two S3 development systems to NOAA
- **Advantage**: Allows iterative development on lower-cost S0 before committing higher-value S3 platform to vessel integration

### SwiftCore™ Flight Management System
- **Components**: SwiftPilot (autopilot), SwiftStation (ground station), SwiftTab (operator interface), aircraft/payload interfaces, mission management, autonomous flight-control functions
- **Capability demonstrated**: Autonomous mission execution from launch through recovery, including advanced landing algorithm and laser-based landing system for precise autonomous belly landings
- **Application to recovery**: Fuses navigation sources, manages approach-to-hover transition, enforces safety gates, coordinates terminal descent

### SwiftSTL™ (Swift Safe-To-Land Machine-Vision Processing)
- **What it is**: Onboard compact, low-power semantic-segmentation system for aerial imagery
- **Function**: Classifies terrain, water, roads, structures, and other scene elements at pixel level; identifies safe landing areas and hazards
- **Prior work**: Developed under NASA SBIR; establishes experience in onboard perception, scene segmentation, obstacle identification, landing-area assessment
- **Application to ship recovery**: Provides foundation for optional targetless ship/deck recognition (Option 1) and moving-deck touchdown assessment

### Ship-Reference & Cooperative Terminal Guidance Equipment
- **Differential-GPS capability**: Time-aligned vessel position, velocity, heading, and motion information
- **Cooperative targets**: Visual or infrared deck-mounted markers providing independent relative-pose observation
- **Deck kit**: Associated mounting, electrical, and integration hardware
- **GCS modifications**: Ground-control-station software updates to interface with ship reference and accept terminal-guidance inputs

## Use Cases & Applications

### Primary Mission: Maritime Observation from NOAA Vessels
- **Atmospheric profiling**: Aircraft launches vertically, transitions to fixed-wing flight, performs approved observation mission, returns for autonomous recovery
- **Payload types**: Atmospheric, imaging, fisheries, hydrographic, sea-surface sensors
- **Operational advantages**: Extends observational reach beyond immediate ship vicinity; reusable "mobile weather tower" replacing single-use expendable sensors
- **Current constraint addressed**: Manual terminal recovery limits routine use and scales poorly across vessels; proposed autonomous recovery enables repeatable operations

### NOAA Fleet Integration
- **Ronald H. Brown concept**: S0-VTOL discussed for NOAA Ship Ronald H. Brown to profile/orbit before returning with autonomous recovery
- **Fleet scaling**: Reusable integration package supports multiple vessels with reduced one-off engineering
- **Future expansion**: S3 option extends to longer-range, higher-payload missions

### Operating Environment
- **Deck motion**: Vessel translation, heading change, and bounded motion compensation
- **Relative wind**: Up to 30-knot wind resistance specified for S3
- **Wake turbulence**: Aircraft trajectory accounts for vessel wake patterns
- **Degraded conditions** (Option 2): Coastline matching supports near-shore degraded-GPS navigation where open-ocean GPS denied

## Key Results & Demonstration Plan
This is a forward-looking proposal; no results yet exist. However, the document outlines demonstrable milestones:

### Surrogate Testing Phase (Task 4)
- Stationary-deck checkout and moving-target tracking verification
- Approach-corridor capture testing
- Vessel-motion matching and heading alignment
- Terminal descent, touchdown, hold, wave-off, go-around, and abort demonstrations
- Defined stop criteria govern envelope expansion

### At-Sea Demonstration (Task 5)
- One Government-vessel event validating autonomous recovery within approved envelope
- Embarkation, crew training, test execution, after-action reporting
- Data and video delivery
- Operating and emergency procedures documentation
- Configuration records and fleet/S3 transition recommendations

### Data Deliverables (Base Effort)
1. Vessel/mission interface baseline and success measures (ARO + 3 months)
2. Recovery architecture, hazards, and interface-control information (ARO + 5 months)
3. Surrogate and progressive test plan (ARO + 7 months)
4. S0-VTOL surrogate demonstration data/video and report (ARO + 13 months)
5. S0-VTOL at-sea data package and after-action report (ARO + 17 months)
6. Procedures, training, safety support, and integration report (ARO + 18 months)

## Notable Details

### Heritage & Risk Reduction
- **NOAA S0 Integration**: Prior P-3 air-deployment integration establishes proven RF, ground-control, data workflows, and measurement validation
- **Arctic Operations**: S2 operations in Greenland (INSTAAR collaboration) inform testing controls, moisture/EMI protection, onboard recording, lost-communications behavior, early safety coordination
- **MIZOPEX Full-System Readiness**: Lessons from previous operations apply to proposed progression from hardware-in-the-loop through vessel demonstration
- **Machine-Vision Foundation**: NASA SBIR work on Safe-To-Land reduces perception and autonomy-integration risk for optional targetless recognition

### Competitive Advantages
- **Reusable integration package**: Reduces one-off engineering across future NOAA vessels
- **Layered navigation architecture**: Avoids permanent ship modification through cooperative targets; enables upgrade path to targetless recognition
- **Explicit safety model**: Defined hold, wave-off, go-around, abort paths with ship-master authority preservation
- **Modular options**: Separable growth paths (targetless recognition, coastline matching, deck ranging, S3 transition) allow NOAA to select desired capability tier

### Intellectual Property
- Deliverables incorporate BST pre-existing proprietary airframes, SwiftCore, SwiftPilot, SwiftTab, ground-station software, centralized fleet-management software, simulation assets, operator-interface software, autonomy functions
- SBIR data rights lineage enables Phase III sole-source award under 15 U.S.C. § 638(r) via NAVAIR N251-016, STTR N6833525C0270, and Air Force AF192-005
- Data rights assertions in software, designs, algorithms, and improvements to be defined in resulting agreement

### Funding & Timing
- **Base ROM**: $0.90M for 18-month effort
- **Option ROMs**: Targetless recognition ($0.30M), Coastline matching ($0.25M), Deck ranging ($0.25M), S3 transfer/validation ($0.60M)
- **Total potential**: $2.30M (all options)
- **Obligation path**: NOAA Standing Broad Agency Announcement (open through 30 September 2026); existing NOAA IDIQ vehicle (1305M226D0012)
- **Timing**: Award by mid-September permits FY26 ORF fund obligation before lapse; deliveries run into FY27
- **Government support required**: Vessel and deck access, deck geometry/navigation/motion data, ship-master coordination, test windows/ports, airspace access, spectrum/safety/airworthiness decisions

### Alignment with National Policy
- Proposed capability aligns with NOAA FY2027 budget request ($75M autonomous research vessels, $60M Class C vessel acquisition) supporting Executive Order 14269, *Restoring America's Maritime Dominance*
- Uncrewed-aircraft complement remains unspecified in current authorization; proposal establishes documented organic aerial layer as NOAA advances autonomous maritime operations
- Quarterly-briefing directive on OMAO activities creates reporting pathway for capability demonstration and fleet-readiness evidence