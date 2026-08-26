# Extending Lower-Atmosphere Observations with Air-Deployed and Reusable UAS

## Document Metadata
- Type: White paper / capability proposal
- Client/Agency: NOAA Office of Marine and Aviation Operations (OMAO) / Uncrewed Systems Operations Center
- Program/Solicitation: Not specified; mentions potential pathways including existing agreement, competitive pilot, BAA, or SBIR Phase III
- Date: May 21, 2026
- BST Products/Systems Referenced: S0, S0-VTOL, SwiftCore, SwiftPilot™, SwiftTab™, S2
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
Black Swift Technologies proposes an 18-month pilot program to NOAA in which one autonomous enclosure paired with two S0-VTOL aircraft would conduct repeated, scheduled or event-driven lower-atmosphere profiles at a fixed site, with autonomous recovery, recharge, and data transfer. This reusable system would complement NOAA's existing radiosonde network by enabling more frequent measurements in the lower atmosphere with reduced staffing growth, leveraging BST's heritage of S0 operations in severe weather from NOAA P-3 aircraft and proven atmospheric-sensing and SwiftCore autonomous-flight technologies.

## Technical Approach

### System Architecture
- **Aircraft**: S0-VTOL modified for autonomous station operation
  - Vertical takeoff/landing (VTOL) with pivoting motors; fixed-wing cruise configuration
  - Maximum altitude: 15,000 feet AGL (subject to site elevation, airspace, weather, energy reserve, approval)
  - Maximum endurance: 60 minutes
  - Equipped with landing camera, companion computer, vision-assisted terminal guidance
  - Battery-management and charging interfaces integrated
  - Data transfer capability with timestamps, position, aircraft state, calibration, and quality indicators

- **Autonomous Enclosure** (prototype, one unit)
  - Environmental protection and aircraft storage
  - Internal and external condition monitoring (temperature, precipitation, wind, aircraft state, battery, communications, navigation, landing-area status)
  - Automated health checks and readiness-status presentation to remote operator
  - Controlled battery charging with temperature, voltage, current, and health limits
  - Launch preparation and precision recovery support
  - Data transfer and event logging
  - Safe maintenance access
  - Cold and icing risk management through bounded envelope (not unrestricted icing claim)

- **Command and Control**
  - SwiftCore autonomous flight management
  - GNSS-supported approach with confidence gates for position integrity, visual confidence, landing-zone status, wind, and aircraft health
  - Hold, go-around, alternate landing, or operator intervention on unacceptable conditions
  - VLOS (visual line of sight) controls for base demonstration; BVLOS (beyond visual line of sight) transition path documented but not required for base completion
  - Remote monitoring and operator authority for launch (supervised operation during pilot)

### Sensor Suite
- Pressure
- Temperature
- Relative humidity
- Three-dimensional winds (higher-rate measurements from controlled flight vs. drifting balloons)
- Onboard recording and ground-system transmission with metadata

### Environmental Hardening
- Assessment and mitigation of cold and icing effects on atmospheric probe, propulsion, control surfaces, batteries, camera, enclosure mechanisms, and communications
- Candidate measures: coatings, localized heating, component changes, icing awareness, enclosure thermal management, procedural weather gates
- Bounded operating envelope established through environmental and flight evidence

## Products & Capabilities Described

### S0-VTOL
- **What it is**: Reusable vertical-takeoff-and-landing variant of the air-deployed S0, designed for autonomous atmospheric profiling from austere locations
- **Core technologies**: SwiftCore flight-management architecture, atmospheric-sensing expertise shared with S0
- **Proposed use**: Base operational aircraft for the autonomous station; one primary, one spare/test article
- **Configuration modifications**: Battery-management and charging interfaces, health/status outputs, landing camera, companion computing, vision-assisted terminal guidance, data transfer, mechanical and electrical interfaces for enclosure integration
- **Capabilities**: 
  - Ascend/descend at controlled rates
  - Hold at selected altitudes
  - Repeat vertical segments to capture lower-atmosphere evolution
  - Return to release point with precision landing
  - Support repeated profiles from same location within approved envelope
  - Operate under autonomous SwiftCore control or with remote operator oversight

### S0 (Air-Deployed)
- **Existing capability**: Deployed from NOAA WP-3D aircraft in tropical cyclones
- **Operational heritage**: Established launch procedures, long-range communications, ground control, NOAA data workflows; proven in extreme winds and precipitation
- **Measurements**: Pressure, temperature, humidity, three-dimensional winds from locations inaccessible to crewed aircraft
- **Validation background**: Prior measurements compared with instrumented towers (DOE ARM Southern Great Plains site), radiosondes, dropsonses, streamsondes, tail Doppler radar, and high-resolution atmospheric models
- **Proposed secondary use**: Option 2 offers 50 air-deployed S0 systems for selected NOAA Atmospheric River, winter-weather, or other airborne-science campaign

### Autonomous Enclosure
- **What it is**: Prototype station providing complete workflow integration for aircraft protection, launch, recovery, recharge, and data management
- **Capabilities**:
  - Aircraft restraint and storage with environmental protection
  - Internal environmental monitoring (temperature, precipitation, wind)
  - Battery management with multi-parameter health checks
  - Communications, navigation, and landing-area assessment
  - Automated health checks and readiness status determination
  - Controlled launch authorization (under VLOS during pilot)
  - Precision recovery support with landing-zone preparation
  - Controlled recharge with safety interlocks
  - Data transfer, event logging, maintenance access
- **Operational concept**: Reduces personnel needed to collect repeated profiles through automation; physical maintenance, cleaning, calibration, battery replacement, and exception response still required ("unattended" ≠ maintenance-free)

### SwiftCore
- **What it is**: BST's autonomous flight-management and guidance architecture
- **Use in station**: Controls climb, profile execution, altitude hold, descent, approach, and precision landing
- **Features**: Confidence gates for safe landing (position integrity, visual confidence, landing-zone status, wind, aircraft health); default-safe behavior on threshold exceedance

## Use Cases & Applications

### Primary Use Case: Lower-Atmosphere Profiling at Fixed Sites
- **Problem addressed**: NOAA needs more frequent, targeted observations in the lower atmosphere where temperature, moisture, winds, stability, and turbulence change rapidly
- **Operational advantage over radiosondes**:
  - Returns to same site (no drift)
  - Can collect scheduled or event-driven observations
  - Supports repeat profiles and altitude-hold at selected levels
  - Can measure higher-rate three-dimensional winds from controlled flight
  - Reusable (no expendable balloon, lifting gas, or radiosonde consumed per profile)
  - Enables more frequent observations with reduced staffing growth
  - Particularly valuable at remote sites where radiosonde staffing and resupply are challenging

### Reference Context
- Complements radiosondes for lower-atmosphere observations
- Proposed co-location with upper-air or comparable reference capability at approved range
- Paired/closely timed comparison with radiosonde observations during pilot
- Preserves radiosondes for full-depth soundings (troposphere to stratosphere) which S0-VTOL does not replicate

### Secondary Use Case: Air-Deployed S0 Campaign Support (Option 2)
- Supports selected OMAO Atmospheric River, winter-weather, or other airborne-science campaigns
- Requires approved host-aircraft integration and deployment interface
- Provides 50 calibrated, flight-ready air-deployed S0 systems
- Includes campaign-readiness training, documentation, logistics support, and one deployment plus after-action review

## Key Results
No results data included. This is a forward-looking proposal, not a report of completed work. Document includes prior S0 validation comparisons (against towers, sondes, radar, models) that provide basis for risk reduction, but specific numerical results are not presented.

## Notable Details

### Risk Reduction Strategy
- Builds on established S0 operational heritage in NOAA severe-weather campaigns (air-deployed from P-3 aircraft in hurricanes)
- Applies proven atmospheric-sensing and SwiftCore technologies to reusable VTOL configuration
- Prior measurement-validation work against multiple reference sources (towers, radiosondes, dropsondes, radar, models) identifies effects requiring continued characterization
- Identified characterization items: sensor response during rapid vertical motion, aircraft-induced temperature/humidity bias, wind-estimation behavior in tight turns
- Pilot will quantify these effects at system level for station configuration rather than relying on nominal component specifications

### Scope Structure (Gated Development)
- **Base Effort** (18 months, $3.00M ROM):
  1. System design concept and safety reviews
  2. Aircraft integration and environmental hardening
  3. Autonomous enclosure development and integration
  4. Progressive verification and unattended VLOS demonstration readiness
  5. Co-located VLOS demonstration at approved range beside reference capability
  6. Transition package (procedures, training, production concept, cost-per-profile analysis, recommendations)

- **Option 1** (12 months, $1.00M ROM): Production maturation and one additional site kit (enclosure + S0-VTOL + support equipment)

- **Option 2** (12 months, $1.15M ROM): 50 air-deployed S0 systems for winter campaign ($18,000 unit price planning estimate); campaign readiness, support, and one deployment event

### Operational Model
- NOAA (OMAO) leads operational evaluation and UAS integration; retains authority over mission, site, airspace, approvals, data use
- NWS and OAR participants define observation requirements, provide reference data, assess data usability
- Qualified remote pilot and visual observers retain launch authority and intervention capability during VLOS phase
- Production concept: one enclosure and one aircraft per operational site, with separate spares strategy established from pilot results
- BVLOS transition path documented but not approved or required for base completion

### Environmental Considerations
- Cold and icing effects assessed and managed through bounded envelope rather than unrestricted claim
- Measures include coatings, localized heating, component changes, icing awareness, enclosure thermal management, procedural weather gates
- Environmental and flight evidence establish approved operating conditions

### Government Furnishing and IP
- **NOAA provides**: Mission ownership and pilot-site designation, observation schedule, altitude/airspace constraints, NWS/OAR evaluation participants, reference data, network/cybersecurity requirements, range/site access, power/backhaul, spectrum/flight approvals, qualified personnel participation, design/readiness decisions
- **BST intellectual property**: S0-VTOL airframe, SwiftCore, SwiftPilot™, SwiftTab™, ground-station software, atmospheric wind-estimation methods, autonomy functions, interfaces, models, manufacturing know-how remain BST proprietary
- **Hardware title transfer**: Delivered systems to NOAA (2 S0-VTOL, 1 enclosure, support equipment)
- **Software/design rights**: To be defined; BST intends private investment in commercial-applicable station architecture and product maturation

### Deliverables Timeline
- System design concept: ARO + 4 months
- Integration design and environmental qualification: ARO + 7 months
- Integrated system readiness review: ARO + 11 months
- Progressive verification and VLOS demonstration evidence: ARO + 14 months
- Co-located VLOS demonstration data and report: ARO + 17 months
- Procedures, training, production concept, transition report: ARO + 18 months

### Candidate Procurement Pathways
- Existing agreement or task order
- Competitive pilot or research procurement
- Broad agency announcement (BAA)
- SBIR Phase III (if applicable lineage and scope confirmed)

### Success Metrics (Pilot Evaluation)
- Observation quality compared to reference systems
- Data availability and repeatability
- Recovery and recharge functionality
- Environmental limitations and operating envelope verification
- Staffing and maintenance requirements
- Logistics and cost per usable profile
- Unattended technical operation under VLOS controls
- Readiness evidence for later BVLOS transition