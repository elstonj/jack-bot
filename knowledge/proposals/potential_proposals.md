# Potential Proposals - 2014

## Document Metadata
- Type: Internal planning document / proposal brainstorm
- Client/Agency: NASA
- Program/Solicitation: 2015 NASA SBIR (Phase 1 and Phase 2)
- Date: Created 2014-11-20; Modified 2015-01-02
- BST Products/Systems Referenced: S2 (Snow Depth), S3 (Salinity/Icing), A2 (Multi-vehicle GUI), A3 (Awareness), SuperSwift, CAPS, SMM, LDCR
- Key Personnel: Jack Elston (editor), Maciej, Al, Gijs, Ute (CU partner consideration)

## Executive Summary
Internal document outlining Black Swift Technologies' potential proposals for NASA's 2015 SBIR program. The company prioritizes a Phase 2 continuation of the CAPS project while identifying four primary Phase 1 concepts and several secondary ideas spanning cloud/icing detection, ocean salinity mapping, snow depth measurement, and wind profiling—leveraging existing SuperSwift platforms with novel sensor integrations and extended endurance capabilities.

## Technical Approach

### Primary Proposals

**1. Cloud Icing Mapper System (CIMS)**
- Subtopic: S1.07 or S3.04
- Integration of existing radar sensor with SuperSwift airframe
- Innovation focused on: integration, testing, rotating nose cone development
- Technical approach: Combine proven sensor with established platform; primary development is mechanical integration and nose cone design

**2. Long Endurance SuperSwift (LES)**
- Addresses novel propulsion and extended flight envelope
- Key technical strategy: Combine existing SuperSwift flight systems expertise with advanced energy management (avionics/payloads)
- Propulsion technologies: Fuel cells, solar panels, hybrid electric systems
- Advantage: Electric system not limited by altitude/elevation constraints
- Modular, low-cost operations design maintained

**3. Ocean Salinity Mapper (S3.04)**
- Leverage existing SMM (Soil Moisture Mapper) system
- Enhanced LDCR (Land/ocean Directional Calibration Radiometer) with ~10x increased sensitivity
- Platform: Long-range SuperSwift with solar, fuel cells, or hybrid power
- Flight capabilities: Terrain-following, 1-month Arctic summer endurance
- Technical requirements: Sub-5cm position accuracy for some variants
- Applications to Aquarius calibration near coastlines/estuaries and glacier melt rate measurement

**4. Snow Depth Mapper (S1.07)**
- 2D Synthetic Aperture Radar (SAR) or passive radiometer for snow pack thickness
- Flight profile: 5-10 m/s velocity using vehicle mobility for synthetic aperture
- GPS RTK integration for sub-5cm position accuracy (critical requirement)
- Platform consideration: Reference Tek drone (potential Phase II purchase)
- Reference radiometer previously flown on P-3 Orion (2003)

**5. Cloud/Wind Profiler (S1.07 and S3.04)**
- 3D wind measurement: 1 m/s accuracy/resolution at 10 Hz sampling
- In situ cloud profiling with SuperSwift
- Leverage MPH (Microwave Pressure Altimeter?) from CAPS Phase 1
- Potential enhancement: Autonomous soaring component for differentiation from CAPS
- Collaboration with Gijs on cloud measurement piece

## Products & Capabilities Described

| Product | Description | Proposed Use |
|---------|-------------|--------------|
| **SuperSwift** | Primary modular, low-cost electric UAS platform | Base vehicle for CIMS, LES, Salinity, and Wind Profiler proposals |
| **CAPS** | Existing sensor/system (Phase 1 complete) | Phase 2 continuation is highest priority; component reuse in Cloud/Wind Profiler |
| **SMM (Soil Moisture Mapper)** | Radiometer system with LDCR component | Foundation for Ocean Salinity Mapper; can be enhanced with 10x sensitivity increase |
| **LDCR** | Land/Ocean Directional Calibration Radiometer | Core sensor; target sensitivity improvement by factor of 10 for salinity work |
| **MPH** | Sensor/component from CAPS Phase 1 | Proposed reuse in Cloud/Wind Profiler development |
| **Rotating nose cone** | Mechanical innovation | CIMS integration enabling icing radar deployment |

## Use Cases & Applications

### Scientific/NASA Applications
- **Cloud and icing detection**: General aviation and small commercial aircraft icing condition sensing (GA/commercial safety)
- **Ocean salinity mapping**: NASA Earth science research goal; Aquarius mission calibration near coastlines/estuaries
- **Cryospheric sciences**: Glacier melt rate measurement via salinity sensing
- **Snow pack measurement**: Arctic summer operations, sub-5cm resolution mapping
- **3D wind profiling**: Cloud/atmospheric research with in situ sampling

### Commercial Applications
- **Snow pack mapping**: Boulder Watershed mapping; Norwegian company interest (via Alerion) for operational snow monitoring
- **Aircraft icing awareness**: GA and small commercial market for real-time icing condition detection
- **Long-endurance electric UAS**: Extended Arctic operations (1+ month endurance requirement)

## Key Strategic Considerations

### Strengths
- Leverage of proven SuperSwift platform across multiple proposals
- Reuse of CAPS Phase 1 components (MPH) in new applications
- Demonstrated scientific expertise (Jack's cloud deployment experience in Alaska; Al's prior snow/ice instrument development)
- Existing commercial interest (Boulder Watershed, Norwegian company contacts)
- Partnership opportunities (ReferenceTek for snow mapper, JPL interest in salinity, HF Design for GUI work, Ute at CU for topography)
- Hit multiple NASA subtopic bullets (S1.07, S3.04 overlap potential)

### Concerns/Challenges
- **Cloud/Wind Profiler redundancy**: Potential overlap with CAPS Phase 2 may weaken proposal (suggests adding autonomous soaring differentiation)
- **5cm resolution feasibility**: Snow mapper requires verification with Al that passive radiometer/SAR can achieve specified resolution
- **Commercialization weakness**: Salinity and wind profiling have primarily scientific markets (unless long-range SuperSwift becomes standalone commercial product)
- **Export regulations**: Long-range SuperSwift may face restrictions on international sales/partnerships
- **PI qualification**: Snow mapper proposal may be weak on principal investigator credentials without clarification of BST vs. Al's role

## Secondary Proposals Under Investigation
1. Ultra Wideband Passive Radar: sUAS detection (subtopic fit: S3.04 or A3.01; coordination with Al needed)
2. Multi-UA GUI Evaluation: Jack to contact HF Design as lead partner (A2.02 with subcontract structure)
3. Arctic Topography System: RTK-based mapping (potential CU partnership)
4. Hybrid UAS/Alternate Power: Fuel cell integration concept (generalized across multiple platforms)

## Notable Details
- **Proposal Due Dates**: Phase 2 CAPS (highest priority, due 12/17); Phase 1s due 1/28
- **Subcontract Structure**: HF Design for Multi-vehicle GUI (A2.02); Al's company for Awareness proposal (A3.01); methane project flight systems/certification support as subcontractor
- **JPL Interest**: Pre-existing interest in long-range SuperSwift salinity mapping capability
- **Modular Design Philosophy**: SuperSwift maintained as low-cost, usable platform across all primary proposals
- **Energy Management Expertise**: BST differentiator positioned as integration of flight systems expertise with advanced propulsion (fuel cells/solar)