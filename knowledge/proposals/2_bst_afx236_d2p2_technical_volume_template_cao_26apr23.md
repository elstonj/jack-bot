# An All-Weather Multi-Mission UAS

## Document Metadata
- Type: SBIR Phase II Direct-to-Phase II Proposal (Technical Volume)
- Client/Agency: U.S. Air Force (DAF)
- Program/Solicitation: AFX236-DPCSO1 (Direct-to-Phase II Call for Innovative Defense-Related Dual-Purpose Technologies/Solutions)
- Date: April 26, 2023 (submitted)
- Proposal Number: F2D-9055
- CAGE Code: 6PGF9
- BST Products/Systems Referenced: S2, S3, SwiftCore, SwiftTab UI, HD45 gimbal (Trillium Engineering), Vision Processing Unit (VPU), ATAK integration
- Key Personnel: Capt Ashley Maestas (NSDL Director of Innovation, Grand Forks AFB), Lt Col Michael Dunn (NSDL Director), MSgt Harland, MSgt Carey, Ed Kase (Business Development Consultant)

## Executive Summary
Black Swift Technologies proposes to develop an all-weather multi-mission UAS based on its S3 platform for perimeter security and incident response at U.S. Air Force bases. The S3 is a vertical takeoff and landing (VTOL) fixed-wing UAS designed to operate in extreme weather conditions, addressing a critical capability gap identified at Grand Forks AFB where commercial Blue UAS alternatives have proven unreliable (3 of 13 flights completed). The proposed Phase II effort will integrate autonomous capabilities, AI-based object detection, weatherization for -10°F+ operations, and ATAK ground system integration to provide 24/7/365 base security with minimal operator workload.

## Technical Approach

### Core Platform & Heritage
- **S3 Platform**: VTOL fixed-wing Group 2 UAS based on proven S2 design
- **Design Heritage**: S2 has operated commercially for 3+ years with NASA, NOAA, USGS; flown to -10°F in Greenland, in 50kt winds, in precipitation/icing conditions, and 25+ miles range at 7,000' altitude
- **Avionics**: SwiftCore modular avionics system with open interfaces, designed exclusively by UAS technology experts (not open-source)

### Key Technical Modifications for Air Force Application

**1. Perimeter Search Mission Capability**
- Integration of HD45 gimbal (Trillium Engineering) or similar EO/IR payload
- Machine learning-based object detection using neural networks (single-shot detector and semantic segmentation)
- Target: 90% success rate identifying pre-placed test objects during perimeter search
- Capability to detect, classify, and track multiple object types specific to base security

**2. All-Weather Readiness**
- Hardware modifications to maintain aircraft in mission-ready state in temperatures ≤-10°F while parked outdoors
- No climate-controlled infrastructure required
- Testing for maximum sustained wind, wind gusts, rain/snow operation
- Current S2 baseline: -10°F operation, 50kt wind capability proven

**3. Ground System Integration & Data Transmission**
- Integration with Android Tactical Assault Kit (ATAK) / Android Team Awareness Kit
- Dual civilian/military ATAK version compatibility planned
- Data pipeline: raw sensor video to onboard vision processing unit (VPU) to neural network processing to ATAK ground station
- Real-time anomaly alerts with minimal operator lag
- Support for secure DoD data delivery interfaces

**4. Autonomy & Workload Reduction**
- Automated preflight self-checks
- Automated system readiness monitoring
- Automatic post-flight checks
- Mission planning tool abstraction: target <1 minute to input new surveillance mission (vs. traditional waypoint creation)
- Onboard failure detection and preventative maintenance algorithms
- GPS-denied navigation capability (NOAA collaboration for jamming/spoofing detection)

**5. Hardware Specifications** (Current S3)
| Specification | Value |
|---|---|
| Maximum Takeoff Weight | 33 lbs |
| Maximum Flight Time | 90 minutes |
| Maximum Payload | 5 lbs |
| Cruise Speed / Max Speed | 45 mph / 100 mph |
| Group Classification | Group 2 |

**6. Manufacturing & Component Origin**
- All major components (avionics, software, radios, ground systems) designed and manufactured in United States
- Target unit cost: <$50K per aircraft (2-5x cost reduction vs. comparable DoD-specific UAS)

## Products & Capabilities Described

### S3 UAS
- **What it is**: VTOL fixed-wing Group 2 sUAS, derivative of proven S2 platform
- **Status**: Late-stage prototype (2 prototypes tested/flown), planned Q4 2023 commercial release
- **Proposed use**: Base perimeter security, incident response, all-weather surveillance
- **Current TRL**: TRL 6 (system-level); many components at TRL 7
- **Commercial traction**: Pre-order from University of Maryland Eastern Shore for 2 aircraft + services ($150K) for winter cargo delivery over Chesapeake Bay

### SwiftCore Avionics System
- Modular architecture with open, well-defined interfaces
- Enables simplified third-party component integration
- Central to advanced capabilities: subsystem tracking, preventative maintenance, redundancy-based safety, automated sensor-driven control
- Designed by UAS technology experts vs. open-source collective

### Vision Processing Unit (VPU)
- Currently based on Intel Myriad-X platform
- Runs onboard neural networks for real-time object detection/classification
- Supports semantic segmentation and single-shot detector networks
- Enables safe automated landing (original application) and perimeter defense

### SwiftTab User Interface
- Current ground control station (tablet-based)
- Planned replacement/integration with ATAK for Phase II

### Neural Network Capabilities
- **Single-shot detector**: Real-time person detection from video
- **Semantic segmentation**: Per-pixel image classification for safe landing zone identification
- **Machine learning-based preventative maintenance**: Onboard failure prediction
- **GPS-denied navigation**: Jamming/spoofing detection (NOAA collaboration)

## Use Cases & Applications

### Primary Use Case (Phase II Focus)
**Base Perimeter Security & Incident Response** - Grand Forks Air Force Base
- 5,000+ acre installation requiring perimeter coverage
- 2,700 on-base residents, up to 6,500 transient employees daily
- $3B in aircraft/radar systems requiring protection
- Current pain points: 3 of 13 Blue UAS flights completed (unreliable in North Dakota extreme weather), high personnel workload, no centralized database workflow
- Target capability: 24/7/365 autonomous surveillance with minimal personnel required

### Scalable Air Force Bases
- **Eielson AFB** (Alaska) - extreme cold, wind
- **Malmstrom AFB** (Montana) - extreme weather vulnerability
- General applicability to 90% of U.S. Air Force installations due to all-weather operation

### Non-Defense Government Missions (Leveraging S2/S3 Heritage)
- **NASA**: Volcano monitoring, vehicle design, soil moisture mapping, CO2 detection
- **NOAA**: Hurricane observations, soil moisture mapping, aircraft platform evaluation
- **USGS**: Volcano monitoring, soil moisture mapping
- **DOE**: Solar panel inspections (E2 UAS)
- Additional inquiries from NOAA, NASA, University of Colorado operators

### Commercial Applications (Market Opportunity)
- Wildland fire monitoring and assessment
- Volcano monitoring and assessment
- Tornado and hurricane observation
- Agriculture (crop health, irrigation, weed identification)
- Real estate, mining, oil/gas surveys
- Infrastructure inspection
- Product delivery (demonstrated with University of Maryland Eastern Shore agreement)
- Wildlife research and conservation

## Phase II Technical Objectives & Key Results

### Objective 1: Perimeter Search Capabilities
- Select payload package (Trillium HD45 or equivalent) with pros/cons document
- Validate payload performance (sensor range vs. target size, coverage area metrics)
- Demonstrate ≥90% success rate identifying pre-placed test objects using ML-based classification

### Objective 2: Data Transmission to DAF Operators
- Integrate sensor data through ATAK interface
- Transmit anomalous activity data with minimal operator lag measurement
- Demonstrate continuous data transmission for full mission duration

### Objective 3: All-Weather Operation
- Demonstrate successful mission below -10°F
- Establish lowest operating temperature
- Measure maximum sustained wind, gusts for takeoff/landing
- Measure maximum rain/snow operation capability

### Objective 4: Reduced Operator Workload
- Compile current workload metrics (setup, flight, post-flight, maintenance)
- Identify and rank workload reduction opportunities through autonomy
- Implement and test changes at BST test site and Grand Forks AFB
- Deliver one-page assessment of equipment/personnel requirements for daily perimeter security

### Test & Evaluation Success Criteria (Grand Forks AFB)
1. ≥90% success rate on subscale perimeter search with pre-placed object identification
2. Immediate data transmission on anomalous activity detection via ATAK
3. ≥1 hour continuous operation at <-10°F at/within 50 miles of Grand Forks AFB
4. One-page assessment of daily UAS operations equipment and personnel requirements

## Key Results (Historical/Demonstrated)

### S2 Platform Track Record
- **104 consecutive missions** in Northern Greenland (summer 2023)
- **Operational in -10°F temperatures** with demonstrated reliability
- **50kt sustained wind** capability
- **25+ mile range** beyond visual line of sight with 7,000' altitude gain
- **Multiple NASA airworthiness certifications** and flight safety reviews
- **11 years of continuous operation** in extreme environments (volcanoes, Arctic, hurricanes, tornadoes)

### Commercial Sales & Adoption
- **Last 12 months non-Defense revenue**: ~$750K
- **S2 customers**: NASA, NOAA, USGS, DOE, Embry Riddle, Alerion, multiple research institutions
- **S3 pre-orders**: University of Maryland Eastern Shore ($150K for 2 aircraft + services)
- **Inquiries for Phase II capabilities**: NOAA, NASA, University of Colorado operators

### Customer Discovery Results (Phase I Feasibility Study)
- **64 Federal Government contact attempts**
- **31 successful email contacts**
- **8 successful phone contacts**
- **1 in-person contact**
- **9 unique Federal Government organizations reached**
- **37 unique USAF organizations contacted**
- Engaged with AF/A3WR, AFSOC, AFLCMC/HBAW, HQ AFSOC/A3OW, AFRL/RQ

## Notable Details

### Competitive Advantages Over Current Solutions
- **All-weather operation**: Significant pain point with "drone-in-a-box" competitors (Skydio, Easy Aerial)
- **Faster response and perimeter inspection time** vs. competitors
- **Fixed-wing VTOL design**: No competitor possesses all of: fixed-wing, VTOL, all-weather, rechargeable without infrastructure simultaneously
- **Significantly lower cost**: 2-5x price reduction vs. comparable DoD-specific UAS ($50K target vs. typical DoD platforms)
- **Proven reliability**: 3 of 13 Blue UAS flights completed at Grand Forks AFB vs. S2's 104 consecutive Greenland missions

### Empowered End-User Commitment at Grand Forks AFB
- **Primary TPOC**: Lt Col Michael Dunn (NSDL Director), Capt Ashley Maestas (Director of Innovation)
- **Supporting stakeholders**: 319 RW/NSDL, 319 SFS, 319 OSS, 319 AMXS, 319 sUAS Working Group
- **Infrastructure support**: Access to GrandSky (dedicated UAS test environment)
- **Phase III strategy**: NSDL indicated interest in purchasing once operational; enterprise sourcing model across ACC bases under consideration
- **Grand Forks AFB context**: Evaluated 40+ UAS systems; identified significant technology gaps addressed by S3

### Market & Commercialization Context
- **Global UAS market**: $20.71B (2018) → $52.30B (2025); CAGR 14.15%
- **Military UAS procurement**: U.S. military projected to spend $18B on drones over next decade