# RFI Response: Small Unmanned Aerial Systems (sUAS) and Component Domestic Production Capability

## Document Metadata
- Type: RFI (Request for Information) Response
- Client/Agency: U.S. Air Force (Air Force Research Laboratory)
- Program/Solicitation: RFI Number FA8650-19-S-5027
- Date: December 2019
- BST Products/Systems Referenced: SwiftCore FMS, S2 sUAS, E2 sUAS, BST Multi-Hole Probe (MHP), Soil Moisture Mapping (SMM) Radiometer
- Key Personnel: Jack Elston (CEO, POC)

## Executive Summary
Black Swift Technologies responded to an Air Force RFI regarding domestic production capability for small unmanned aerial systems and components. BST detailed its existing manufacturing infrastructure, supply chain resilience, and product portfolio—specifically the SwiftCore flight controller system and several sUAS platforms—all designed and manufactured in the U.S. The company argued it could scale production to meet DoD requirements within 6-12 months with purchase orders and highlighted the need for government purchasing commitments to help American companies compete against foreign competitors like DJI.

## Technical Approach

### SwiftCore Flight Management System (FMS)
- **Architecture**: Multi-layer PCB assembly with commodity electronic components, mostly sourced from U.S. manufacturers
- **Key Components**:
  - Flight controller PCB board (assembled by U.S. Contract Electronic Manufacturers)
  - Android-based tablet (Samsung) for user interface
  - Cable assemblies (local Colorado supplier)
  - 3D-printed hard shell cases (American suppliers like Shapeways, Protolabs)
  - Wireless radios: Options include Digi International, Freewave, and Microhard (all modular integration)
  - Single-board computers (SBCs) for ground stations and onboard advanced processing
- **Software**: Open-source/open-architecture autopilot, proprietary firmware and control software (no open-source code from outside company used)
- **Capabilities**: IP-based data links, optional backup control link, support for GPS/GLONASS/GALILEO, night vision operation, functional safety design (IEC61508 standards), SLAM and video processing algorithms

### Manufacturing Process
- **Equipment**: Industry-standard PCB assembly and inspection equipment (no special equipment required)
- **Quality**: Most CEMs operate under ISO 9001 quality systems
- **Yield**: Expected to be high; defects discovered during testing and addressed through process improvements
- **Location**: PCB assembly at various U.S.-based CEMs in Denver area; final assembly at BST's Boulder, CO facility
- **Scaling**: No DoD investment or loans needed—merely purchase orders required

## Products & Capabilities Described

### 1. SwiftCore Flight Management System (FMS)
- **What it is**: End-to-end avionics system for autonomous flight on fixed-wing, multirotor, and VTOL aircraft
- **Components**: SwiftPilot (control unit), SwiftStation (ground station), SwiftTab (Android tablet interface)
- **Use context**: Approved/deployed by NASA, NOAA, DOE; proposed for military ISR, RSTA, surveillance
- **Specifications**: 
  - Open SDK for custom development
  - Compatible with nVidia onboard computers for machine vision/ML
  - All electronics, firmware, software designed and tested in U.S.A.
- **Production rates**: 
  - Current: 2/month
  - Immediate max: 10/month
  - 6-month max: 400/month

### 2. S2 sUAS
- **What it is**: Purpose-built airframe for demanding atmospheric environments
- **Capabilities**: High-altitude, corrosive particulates resistance, strong turbulence, cold environment operation
- **Performance**: Larger payload capacity, longer endurance, higher ceiling, greater range than quadrotors
- **Payload**: Max 5 lbs
- **Unique feature**: Autonomous launch/flight/landing (demonstrated in Northern Greenland, Hawaii, Costa Rica volcanoes)
- **Airframe**: 10 ft wingspan, uses pneumatic launcher
- **Production rates**:
  - Current: 1/month
  - Immediate max: 2/month
  - 6-month max: 10/month

### 3. E2 sUAS
- **What it is**: Quadrotor platform designed/manufactured by BST in U.S.A.
- **Flight controller**: Uses SwiftCore FMS
- **Performance**: Flight times >40 minutes, operates in high wind environments
- **Payload**: Max 4 lbs
- **Manufacturing advantage**: Robust design allows scaling to large quantities with minimal investment
- **Production rates**:
  - Current: 2/month
  - Immediate max: 10/month
  - 6-month max: 100/month

### 4. BST Multi-Hole Probe (MHP)
- **What it is**: Integrated atmospheric sensor package for sUAS
- **Measurements**: Air speed, altitude, angle-of-attack, side-slip, ambient temperature, relative humidity
- **Additional sensors**: Magnetometer, IMU with fusion algorithms for full wind vector solution
- **Manufacturing**: Designed and manufactured in U.S.A. using 3D printing for rapid scaling
- **Production rates**:
  - Current: 2/month
  - Immediate max: 20/month
  - 6-month max: 100/month

### 5. Soil Moisture Mapping (SMM) Radiometer
- **What it is**: Passive microwave radiometer sensor package integrated with S2 airframe
- **Capability**: Measures soil moisture content under dense canopy crops
- **Coverage**: Up to 600 acres per flight
- **Operating altitude**: 15-30m AGL for 5 cm depth measurement at 15m resolution
- **Manufacturing**: Entirely in U.S.A.
- **Production rates**:
  - Current: <1/month
  - Immediate max: 4/month
  - 6-month max: 10/month

## Use Cases & Applications

### Civilian Markets (Current Focus)
- Atmospheric monitoring
- Biome-specific research
- Soil moisture monitoring
- Aerial survey and mapping
- Construction and mining

### Potential Government/Defense Applications
- Intelligence, Surveillance, and Reconnaissance (ISR)
- Reconnaissance, Surveillance, and Target Acquisition (RSTA)
- Cargo transportation/parcel delivery
- Continuous surveillance of public events
- Land surveys/mapping
- Crop management
- Surveillance of floods, wildfires, natural disasters

## Supply Chain & Manufacturing Details

### Vertical Integration Strategy
- **In-house**: Aircraft manufacture (S2, E2), flight controller design and final assembly, firmware/software development, payload integration, flight services
- **Contracted**: PCB assembly (U.S. CEMs), mechanical cases (3D printing services), cable assemblies (local Colorado), SBCs (sourced from American companies: Gateworks, nVidia, Gumstix)
- **Rationale**: BST shifted to backward integration after quality/availability issues with external aircraft suppliers

### Supply Chain Nodes & Diversity
1. **Discrete electronic components/sensors**: Multiple suppliers per component; diversified globally but interchangeable
2. **Board manufacture/assembly**: Strong U.S. presence with multiple suppliers
3. **Mechanical cases**: Growing 3D printing domestic capability (Shapeways, Protolabs, others)
4. **Android devices**: Multiple options from friendly nations; BST agnostic to specific device
5. **Single-board computers**: American suppliers with modular code allowing rapid switching between platforms

### Sourcing & Supply Chain Risk
- **Domestic sourcing**: PCB assembly in Denver; final assembly in Boulder, CO
- **Electronics components**: Commodity items with multiple sources; less common components available from U.S. manufacturers
- **Foreign components**: Some electronic components manufactured offshore but typically commodity items from multiple manufacturers
- **Single points of failure**: BST has identified multiple suppliers for each major component; no critical single-point failures identified to date
- **Mitigation**: In-house design expertise allows rapid circuit board iteration to accommodate component/supplier changes; strategic decision to always use most advanced available components

### Risk Mitigation Capabilities
- Full control of source code (no external open-source dependencies in flight controller)
- Ability to rapidly redesign and source alternative components
- Multiple suppliers identified for all major subsystems

## Market & Business Context

### Current Market Position
- **Market served**: Primarily civilian (96% SwiftCore FMS to U.S. customers, 4% to EU)
- **DoD revenue**: Zero—no products sold to DoD to date; business with NASA, NOAA, DOE
- **Domestic focus**: 96% of SwiftCore production to U.S. customers
- **Market challenge**: DJI dominance (76.8% FAA market share as of June 2019); however, survey data shows 88% of public safety professionals would prefer U.S.-made drones if options were equivalent

### Competitive Position
- **Technology**: Advanced capabilities but "flying under the radar" compared to DJI/Parrot
- **Weakness**: Location in Colorado (lacks venture capital infrastructure of coasts); hardware-intensive business model difficult to finance in Colorado VC market
- **Opportunity**: 88% of public safety professionals prefer U.S. equipment if capabilities equivalent

### Production Scaling Capability
- **Timeline**: Can scale to DoD requirements within 6-12 months with purchase orders
- **Investment required**: None from DoD—merely need purchase commitments
- **Limiting factor**: CEM capacity, not design or component availability
- **Minimum sustaining rate**: CEMs have minimum volumes, but BST can supply smaller quantities at higher unit cost
- **Lead times**: 6 months to 1 year for maximum production rates

## Key Findings & Recommendations

### Manufacturing Feasibility
- SwiftCore flight controller manufacturing is **low-risk** and easily scalable
- No special equipment required beyond industry-standard PCB assembly tools
- U.S.-based CEM capacity sufficient for DoD requirements
- Expected high manufacturing yields with ISO 9001-compliant suppliers

### Supply Chain Resilience
- **Strengths**:
  - Majority of components are commodity items available from multiple sources
  - Core IP in firmware/software and integration (not hardware)
  - In-house design capability allows rapid component substitution
  - No open-source dependencies in critical flight controller code
  
- **Vulnerabilities**:
  - Some electronic components manufactured offshore (though commodity/interchangeable)
  - Android tablet has consumer-grade security profile (mitigated by using Samsung tablets already approved for DoD classified work)

### Security Posture
- **Flight controller electronics**: Low threat risk (commodity components from multiple sources, no embedded code)
- **Software**: Controlled by BST (all code written internally, no external open-source code in flight controller)
- **Tablet interface**: Standard consumer Android security profile; existing DoD-approved tablets can integrate directly

### Economic Incentives Recommended
- **Purchase Commitments** (highest priority): Guaranteed purchase orders would allow BST to maintain scaling infrastructure and justify internal investments
- **Advance Partial Payments**: Helpful for larger quantity orders (BST currently requires deposits from commercial customers)
- **Purchases/Equipment Subsidies**: Not necessary for flight controller manufacturing
- **Loans/Loan Guarantees**: Not required if purchase orders are provided

### Key Market Insights
- **Main demand drivers**: BVLOS (Beyond Visual Line of Sight) flight adoption, AI/ML integration, advances in autopilots
- **Regulatory constraints**: FAA restrictions on BVLOS limit technology potential
- **Government role**: DoD purchasing from U.S. companies would help domestic manufacturers compete globally; maintain COTS classification (avoid ITAR restrictions that push customers to foreign equivalents)
- **Competitive threat**: DJI dominance and Chinese-built products; international opportunities exist for competitive U.S. platforms

### Strategic Recommendations to DoD
1. Announce intention to purchase specific sUAS technologies from small, innovative U.S. companies
2. Award purchase commitments rather than R&D contracts (jumpstart manufacturing not development)
3. Maintain COTS classification to avoid export restrictions
4. Focus on purchasing existing products from non-traditional DoD suppliers
5. Recognize that larger purchase volumes will reduce prices and improve international competitiveness
6. Consider investment in software (API robustness, ML integration) and hardware (most U.S. investment lacks hardware focus)

## Notable Details

- **3D Printing Advantage**: BST uses 3D printing for rapid prototyping and production scaling, particularly for multirotor/fixed-wing airframe development and avionics cases
- **Open Interface Philosophy**: SwiftCore FMS