# Phase II Application Discussion

## Document Metadata
- Type: Internal teleconference notes and summary
- Client/Agency: NASA
- Program/Solicitation: NASA 2012 SBIR Phase II (Soil Moisture); references ROSES solicitation
- Date: August 27 – October 18, 2013
- BST Products/Systems Referenced: Tempest, SuperSwift, SwiftPilot Pro (SP Pro)
- Key Personnel: Geoff (likely Geoff Bland), Mahta (soil moisture/radar specialist), Al, Maciej Stachura, Phil Paulsen, Skip

## Executive Summary
BST is preparing a Phase II SBIR proposal to NASA for soil moisture monitoring using the Tempest UAS platform. The proposal emphasizes field testing at two validation sites (Oklahoma and California), development of the SuperSwift variant with modular payload capability, and potential collaboration with NASA's AirMOSS project. The goal is to demonstrate the Tempest/SuperSwift as a lower-cost alternative to manned aircraft for soil moisture and salinity science missions, with pathway toward Greenland deployment.

## Technical Approach

### Tempest/SuperSwift Development
- **Tempest baseline**: Hand-launched UAS with narrow fuselage; established platform with autopilot (noted as "prototypical" and needing Phase II testing to demonstrate scientific capabilities)
- **SuperSwift variant**: Tempest with removable modular nosecone to accommodate larger payloads (radiometer, radar antenna). Photo mockup and P-band antenna drawing planned.
- **Key advantage**: Hand-launch eliminates need for launcher deployment infrastructure, reducing shipping overhead and enabling deployment to remote locations
- **Flight control**: SwiftPilot Pro (SP Pro) autopilot can fly neutrally stable airframes with increased nose-cone size

### Sensor Integration
- **Radiometer payload**: Target integration with modular nosecone
- **L-band/P-band radar**: Mahta's work; target weight ~10kg; candidate for future UAS missions (Phase I SBIR S1.08 being considered)
- **Tetracam integration**: Wide range of agricultural cameras; integrates IMU with Tetracam for geo-rectification
- **NDVI boards**: Integrated with SwiftPilot Pro; demonstrates key capabilities of the autopilot
- **Mapping GUI**: New graphical mapping features developed by BST independently for this mission

### Autopilot Capabilities
- SwiftPilot Pro is described as "prototypical" with superior scientific capabilities versus competing systems
- Can manage neutrally stable airframes (important for accommodating larger payloads like modular nosecone)

## Products & Capabilities Described

### Tempest
- Hand-launched UAS platform
- Established system with modular nosecone capability
- Autopilot integration via SwiftPilot Pro
- Advantage: eliminates launcher overhead, suitable for remote deployment

### SuperSwift
- Tempest variant with removable/modular nosecone
- Designed to accommodate radiometer and radar payloads
- Emphasizes low-altitude flying capability
- Positioning as pathway toward S3.05 capability

### SwiftPilot Pro (SP Pro)
- Autopilot system
- Capable of flying neutrally stable airframes
- Integrates with sensor packages (NDVI boards, Tetracam, etc.)
- Provides autonomous mission planning and execution
- Described as superior to competing autopilot systems for scientific applications

## Use Cases & Applications

### Phase II Test Sites
1. **Canton, Oklahoma test site**
   - 21 capacitive in situ moisture probes at various depths
   - 300m × 500m area
   - Privately owned (relative of Phil Paulsen)
   - May overlap with FAA COA area already applied for by CU
   - Phase II Year 1 deployment (validate Phase I prototype); consider University of Nebraska-Lincoln (UNL) as alternative

2. **California test site**
   - 120+ (expanding to 150) in situ probes
   - ~36km × 36m coverage area (approximately SMAP footprint)
   - Tests sparser sampling pattern
   - Phase II Year 2 deployment (larger-scale demonstration)
   - Serves as SMAP calibration/validation site

### Science Applications
- **Soil moisture monitoring**: L-band/P-band radar for subsurface moisture profiling
- **SMAP validation**: Both OK and CA sites designated for SMAP satellite validation
- **Salinity measurement**: 
  - Aquarius satellite validation and coastal calibration (Aquarius does not operate near land boundaries)
  - Greenland runoff mapping—appealing for scientific merit and favorable UAS regulatory environment
  - Phase II goal: system ready for Greenland deployment (Phase II E/X funding augmented by ROSES for actual deployment)
- **Comparison with manned airborne science**: Collaboration with Mahta's EV-1 project (Gulf Stream-based soil moisture work through 2015) to position Tempest/SuperSwift as lower-cost alternative for continued work post-2015

## Key Strategic Points

### Alignment with NASA Priorities
- Connection to decadal survey goals
- Registration with NASA Airborne Science program
- Alignment with ROSES solicitation guidelines and NASA science objectives
- Demonstrates "proof in the pudding" through rigorous field testing

### Phase I to Phase II Transition
- Key Phase I goals: integrated, airworthy Tempest system; field data collection (non-flying)
- Phase II goals: 
  - Flight testing to demonstrate scientific superiority of SwiftPilot Pro autopilot
  - Oklahoma deployment Year 1
  - California deployment Year 2
  - Greenland system readiness by end of Phase II

### Competitive Positioning
- Lower cost than manned aircraft (EV-1 "Cadillac" system) while maintaining scientific capability
- Hand-launch eliminates launcher overhead vs. competing UAS
- SwiftPilot Pro autopilot superior for scientific work vs. competitors
- Modular payload design enables mission flexibility

### Funding Strategy
- Phase II SBIR for system development and testing
- ROSES funding for actual Greenland deployment
- Phase I SBIR S1.08 considered for radar development (potential partnership with CEI for UAS-suitable radars)

## Notable Details

- **Flight documentation**: Noted that COA (Certificate of Airworthiness) documentation for Oklahoma and California sites should be stated as "filled out and ready to submit at onset of Phase II"
- **Collaboration with external partners**: 
  - Mahta to provide letter of support and intent to work with BST and CET (Cooperative Earth Technology?)
  - CEI contacts for radar development
  - CU partnership for COA coordination
- **Proposal focus**: Emphasis on keeping proposal "very focused" and highlighting the connection between BST systems and improved science outcomes
- **Regulatory advantages**: Greenland characterized as having "simpler regulatory environment" for UAS operations compared to continental U.S.
- **Payload integration**: GUI mapping features developed independently by BST for broader mission applicability beyond this project