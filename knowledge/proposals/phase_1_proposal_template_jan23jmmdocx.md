# VLFTS Phase 1 NASA SBIR Proposal (UASUSA)

## Document Metadata
- **Type:** NASA SBIR Phase 1 Proposal (draft/template)
- **Client/Agency:** NASA (Subtopic S3.04)
- **Program/Solicitation:** NASA SBIR Phase 1
- **Date:** January 2014 (proposal template dated Jan23)
- **BST Products/Systems Referenced:** BlackSwift autopilot system (SwiftPilot Pro), tablet-based ground station
- **Key Personnel:** Jack Elston, Ph.D. (BST connection); UASUSA team: Skip Miller (PI/CEO), Mark Treibes (VP Design/Production), Thomas Akers (Aeronautical Engineering), Steve Fuerstenau, Ph.D. (RadMet)

## Executive Summary
UASUSA proposes to develop VLFTS (Vertical Lift Fixed-wing Test System), a small unmanned aircraft system combining fixed-wing efficiency with autonomous vertical takeoff and landing (VTOL) capability. The system will be based on UASUSA's proven TEMPEST airframe but will incorporate innovative vertical lift systems, allowing deployment from constrained field sites (e.g., jungle clearings, rocky terrain) unsuitable for traditional fixed-wing UAS. The VLFTS will integrate a BlackSwift autopilot system and be designed for NASA research missions including volcanic plume sampling, cloud formation studies, and Arctic environmental monitoring.

## Technical Approach

**Overall Strategy:** Phase I will evaluate two primary vertical lift concepts and integrate them into the proven TEMPEST airframe:

### Four Major Phase I Tasks:

1. **Design and Evaluate Vertical Lift Systems; Build Prototype**
   - Evaluate two concepts: (i) single collapsible helicopter blade, (ii) two-engine tilt-wing system
   - Design analysis and preliminary modeling of each approach
   - Select optimal concept and build prototype grafting it into TEMPEST airframe
   - Conduct indoor ground tests
   - Timeline: Design work June-July, modeling July-September, prototype build by October 31

2. **Preliminary Airframe Design**
   - Use TEMPEST as design starting point
   - Optimize airframe to maintain TEMPEST-level flight characteristics while accommodating vertical lift system and sensor payloads
   - Goal: Concept-level design matching current TEMPEST performance
   - Incorporate sensor placement, air intake design, and weight distribution considerations
   - Timeline: Theoretical study through September 30, conceptual drawings by November 15

3. **Preliminary Autopilot Integration and Sensor Integration**
   - Expand BlackSwift autopilot capabilities for new airframe and autonomous vertical takeoff/landing
   - Develop simulation of VLFTS aircraft with avionics validation for all flight phases
   - Integrate sensor (initially RadMet sensor, later Droplet Measurement Technologies particle counter) into prototype
   - Address technical challenges: sensor data correlation with autopilot metadata (georeferenced location, altitude, airspeed, ground velocity, barometric pressure, wind data)
   - Identify motor/sensor interference issues and airflow contamination risks
   - Timeline: Complete by October 31

4. **Permitting and Phase II Team Assembly**
   - Apply for necessary FAA/NASA permits for Phase II flight testing
   - Primary test location: NASA Wallops Flight Facility
   - Fallback: Universities with existing TEMPEST COAs
   - Begin identifying and recruiting flight test teams from university connections
   - Permitting activities June-September, team assembly September onward

## Products & Capabilities Described

### TEMPEST (Reference System)
- **What it is:** Proven, high-efficiency small UAS based on sailplane design principles
- **Key specifications:**
  - Weight: 12 lbs
  - Wingspan: 10 feet
  - Power: Electric (lithium-ion battery)
  - Payload capacity: 10 lbs (study possibility of 15 lbs in Phase I)
  - Flight duration: 1.5 hours (stock battery)
  - Flight distance: 100 miles (conditions dependent)
  - Speed: 12 m/s stall, 20 m/s cruise, 50 m/s max
  - Assembly/launch time: 5 minutes
  - Crew requirement: 2 people (preferably)
  - Max wind conditions: 50 mph (has handled higher in tornado research)
  - Landing: Fully autonomous
  - Battery recharge: 1 hour
  - Maintenance: 6-month intervals (operator-performed)
  - Launch: Hand launch or simple transportable catapult
- **Experience base:**
  - 69+ successful tornado research flights for University of Colorado (NOAA/NSF VORTEX 2 project)
  - 110+ FAA Certificates of Authorization granted
  - University of Colorado operates under blanket COA
  - Naval Research Laboratory high-altitude test: lifted to 57,000 feet, deployed at -60°F, glided 28 miles in 50-knot headwinds without motor

### VLFTS (Proposed System)
- **What it is:** TEMPEST airframe with integrated autonomous vertical lift system + BlackSwift autopilot
- **Proposed specifications (end of Phase II):**
  - TEMPEST-like flight characteristics with added VTOL capability
  - Intended retail price: ~$45,000
  - Vertical takeoff/landing from 20'×20' clearing
  - Fully autonomous through autopilot tablet interface (Android-based)
  - Can operate remotely or via line-of-sight RC control with mode toggling
  - Designed for in situ sensor missions (volcanic plume, cloud formation, atmospheric phenomena)
  - Reduced propwash/dust interference due to lighter weight and broader thrust distribution
  - Can glide (soar) to extend range and reduce operating costs
- **Proposed vertical lift concepts being evaluated:**
  - Single collapsible helicopter blade (rotor)
  - Two-engine tilt-wing system

### BlackSwift Autopilot System (SwiftPilot Pro)
- **What it is:** State-of-the-art autonomous flight control system
- **Application in VLFTS:**
  - Handles all phases of flight: vertical takeoff, transition to horizontal flight, cruise, transition back to vertical, and autonomous landing
  - Tablet interface for mission planning and control
  - Integrates with sensors to correlate data with flight metadata
  - Integration of autopilot with new airframe represents major Phase I/II challenge (transition from vertical to horizontal flight)
  - Black Swift Technologies (Boulder, CO-based) will conduct simulation-based avionics validation

### Sensor Integration Partners:
- **RadMet LLC** (San Mateo, CA): Designing lightweight sensor for Phase II; Phase I involvement in sensor placement, airflow interference analysis
- **Droplet Measurement Technologies** (Boulder, CO): Planned Phase II development of miniature particle counter for in situ measurement

## Use Cases & Applications

### NASA Research Applications (Emphasized)
1. **Volcanic Plume Research:** Rapid deployment to sample "belched" clouds above tropical canopy; integration with sensor recently used at Turrialba Volcano, Costa Rica (NASA "In Situ Validation and Calibration of Remotely Sensed Volcanic Emission Data and Models" project)

2. **Arctic/Cryospheric Operations:** Rapid response to ephemeral atmospheric phenomena; ice coverage monitoring along shoreline; operation in extreme wind conditions without concern for landing zones

3. **Cloud Formation Research:** Calibration of in situ observations with satellite remote sensing; rapid deployment when phenomena develop

### Non-NASA Government Applications
- NOAA projects
- EPA air quality monitoring
- DOE radiation monitoring
- Department of Interior wildlife monitoring
- DHS facilities inspection, radiation/chemical detection
- USDA forest health, grassland monitoring, fire monitoring

### Commercial/NGO/Educational Applications
- **Search and Rescue:** Combine fixed-wing endurance with hover/landing capability; deliver small payloads (medicines, parts)
- **Wildlife Protection:** Operating in rocky/brushy terrain unsuitable for traditional VTOL; night operations when poachers active
- **Industrial Inspection:** Transmission line and railway inspection; ability to cover large territory with hover-for-inspection capability
- **University Research:** Atmospheric and environmental monitoring

## Key Technical Challenges Identified

1. **Vertical Lift System Design:** Major Phase I focus; two competing concepts with different efficiency/performance tradeoffs
2. **Airframe Integration:** Balancing payload capacity, durability, and efficiency while accommodating vertical lift system
3. **Autopilot Transition Management:** Smooth autonomous transition from vertical to horizontal flight and back
4. **Sensor Integration:** Motor interference, airflow contamination, weight balance, power supply, data correlation with flight metadata
5. **Propwash Management:** Minimizing dust/debris kickup during takeoff/landing (less critical due to lower weight)
6. **Permitting:** Coordination with NASA Wallops and FAA for Phase II flight testing

## Notable Details

### TEMPEST Track Record
- Successfully performed in extreme conditions (tornado research, high-altitude/low-temperature deployment)
- Proven reliability earning 110+ FAA Certificates of Authorization
- Unique gliding capability (no other VTOL can soar) extends range and reduces operating costs
- Minimal maintenance requirements

### Competitive Positioning
- Claimed to be first sUAS combining high-performance fixed-wing flight with vertical lift
- Significantly lower cost than existing VTOL systems (V-Bat priced $275,000-$325,000; VLFTS targeted at ~$45,000)
- TEMPEST proxy demonstrates what VLFTS will achieve in flight efficiency/turbulence tolerance

### Export/Regulatory Advantages
- No military funding in design pedigree
- Expected to be classified under Department of Commerce Export Administration Regulations (class 9A012.A) rather than ITAR
- Easier international transport and customs clearance due to non-military appearance

### Team Capabilities
- **Skip Miller:** 40 years remote control aircraft design/manufacturing; former World RC Soaring Champion; 11-time National Champion; 6-time USA RC Soaring Team member; World Championship aircraft in Smithsonian
- **Mark Treibes:** 17 years experience; VP Design/Production; responsible for airframe design/production
- **Thomas Akers:** Aerospace Engineering background; formerly Chairman/Director of Aeromech Engineering (now Lockheed Martin subsidiary)
- **Jack Elston, Ph.D.:** BlackSwift principal (mentioned in Nature feature "Drones in Science: Fly, and Bring Me Data," June 2013)

### Phase II Roadmap
- Evaluate and test airframe design
- Build final airframe combining TEMPEST characteristics with vertical lift
- Full autopilot integration with latest generation system
- Sensor integration (miniature particle counter, refined RadMet sensor)
- Flight testing at NASA Wallops (or alternative facility)
- Automated flight testing including precision landing/takeoff
- Turbulent condition testing on full autopilot
- Sensor calibration
- Training of multiple "for hire" flight teams for mission services

### Commercialization Plan
- Phase II will deliver more than minimum viable product—a ready-to-fly, permit-ready system
- Dual business model: direct equipment sales or per diem flight services lease
- Flight teams available for contract missions with experienced pilots trained in research protocols
- Minimal engineering required for mission-specific customization

### Company Background (UASUSA)
- Based in Boulder, Colorado
- Established 2009 (TEMPEST launch)
- Controls manufacturing: molding facility in California, assembly facility in Boulder
- Over 50 TEMPESTs placed with end users as of January 2014
- Strong supplier relationships through Skip Miller's remote control aircraft parts dealer background

**Document Status Note:** This is a draft proposal template with multiple incomplete sections marked "[SKIP FILL IN]" and editorial notes, indicating it was in preparation stage. Specific budget information, personnel resumes, detailed schedules, and facility descriptions are incomplete.