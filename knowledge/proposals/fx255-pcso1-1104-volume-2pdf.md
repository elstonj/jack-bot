# All Weather UAS for Long Term Tactical Deployments

## Document Metadata
- **Type:** SBIR Phase I Proposal (Volume 2)
- **Client/Agency:** U.S. Department of the Air Force (DAF)
- **Program/Solicitation:** AFWERX Open Topic 25.5E (unsubmitted)
- **Date:** Prepared for submission (document created/modified 2025-08-05)
- **Proposal Number:** FX255-PCSO1-1104
- **BST Products/Systems Referenced:** S3 UAS, S2 UAS, E2 multirotor, SwiftCore Flight Management System, S0 UAS
- **Key Personnel:** Dr. Jack Elston (lead engineer, electronic design & firmware), Dr. Maciej Stachura (autonomy, regulatory compliance, multi-UAS control)

## Executive Summary
Black Swift Technologies proposes the S3 UAS, a next-generation autonomous platform designed for persistent operations in extreme and contested environments including CBRN zones, active conflict areas, and severe weather. The S3 combines VTOL capability, vision-based GPS-denied autonomy, solar-powered autonomous recharge for days-to-months endurance, and TAK integration to deliver tactical ISR at the edge without traditional logistical burdens.

## Technical Approach

### Core Technical Innovations

**All-Weather, Field-Hardened VTOL Airframe**
- New swept-wing configuration and vertical stabilizer optimized for turbulent low-altitude flight in gusts exceeding 50 knots
- Precipitation resistance and de-icing enhancements; conformal electronics bay with ingress protection sealing for rain, snow, dust, corrosive environments
- Redundant avionics, fault-tolerant power distribution, reinforced landing gear for semi-prepared surfaces and remote landings
- Aerodynamic and structural redesign based on real-world deployment data from legacy S2 platform

**GNSS-Denied Autonomy & Vision-Based Navigation**
- Stereo camera system with onboard embedded processing for terrain-relative navigation, obstacle avoidance, and semantic classification of safe landing zones in real time
- Enables precision autonomous landings at unprepared sites, loitering over moving/dynamic targets, adaptive route replanning
- Hierarchical control architecture informed by flight-proven software from NASA and NOAA deployments
- Launch, patrol, and autonomous landing without operator in the loop; capable of failover, route replanning, and decision-making for patrol and alert response missions

**Long-Endurance, Unattended Operation**
- Wing-mounted solar arrays with smart battery management and advanced thermal regulation enable recharging in the field
- Multiple sorties per day for weeks at a time; unattended capability for distributed coverage without full-time operator presence or vehicle recovery
- In-flight wind estimation and dynamic cruise optimization maximize energy efficiency in adverse weather
- Ground-effect-aware landing procedures, automated health checks, post-flight diagnostics reduce wear

**TAK (Tactical Assault Kit) Integration**
- Full integration with TAK system for common operational picture among security forces, base defense, and remote operators
- S3 telemetry, video feeds, mission plans, alerts streamed directly to ATAK/CivTAK environments
- Missions planned through TAK plugins; live alerts from onboard analytics (motion detection, anomaly tracking) trigger notifications
- Seamless interoperability with base security systems; reduced need for specialized ground control infrastructure

**Modular Payload Support & Smart Response**
- Swappable EO/IR, multispectral, or RF payloads
- Customizable for night surveillance, signals detection, CBRN sensor carriage
- Onboard autonomy allows mission behavior modification in response to live alerts, external sensor cues, or human override
- Auto re-tasking to monitor fence line breaches, loiter over suspicious activity, autonomously shadow vehicles
- Multi-aircraft configuration: cooperative coverage with some platforms executing perimeter patrol while others remain docked in solar charging stations for rapid dispatch
- Swarm-like capability is scalable and survivable, reducing effectiveness of single-point failures or spoofing attacks

**Technical Maturity & Risk Mitigation**
- Builds on 10+ years of operational UAS experience with flight-tested components and autonomy stacks proven in NASA, NOAA, DoD field campaigns
- Many platform elements have completed environmental testing for EMI, temperature extremes, vibration, ingress protection
- Software modules (autonomy, navigation, failsafe control) are modular, containerized, portable to higher-assurance processing environments
- Architecture accommodates future autonomy frameworks and sensor upgrades for long-term compatibility with AFWERX autonomy efforts and software-defined ISR architectures

## Products & Capabilities Described

### S3 UAS (Primary Product)
- **Classification:** Group 2 UAS with unique capabilities typically found only in larger systems
- **Key Differentiators:** Combines VTOL deployment, GPS-denied autonomy, and solar-based endurance at fraction of logistical burden/cost compared to Group 4/5 ISR assets
- **Endurance:** Days to months of autonomous operation without returning to base through solar recharge and hopping between landing sites
- **Performance Specs:**
  - Gust tolerance: exceeds 50 knots
  - All-weather operation: precipitation, icing, high winds
  - Autonomous flight: launches, patrols, lands without operator
  - Multi-sortie capability: multiple sorties per day for weeks
- **Heritage:** Derived from proven S2 platform used by NASA, NOAA, USGS in volcanic plume sampling, severe weather research, wildfire monitoring, hurricane sampling
- **Regulatory Classification:** EAR-classified (not ITAR), enabling commercial sales and international collaboration

### SwiftCore Flight Management System
- Advanced autopilot system anchoring all avionics work at BST
- Enables sophisticated integration of payloads for meaningful scientific research
- Utilized in multiple atmospheric sampling campaigns
- Foundation for S3's autonomy capabilities

### Legacy S2 Platform
- Fixed-wing UAS proven in severe weather conditions
- Successfully deployed in volcanic plume monitoring (Makushin, Costa Rica), CO₂ mapping at jungle canopy levels, satellite calibration/validation campaigns (NEON sites)
- Demonstrated 25+ mile range, 7000 ft altitude gain capability
- Onboard semantic segmentation performing pixel-level classification of video feeds
- Methane emissions detection and localization capability
- Used extensively in NightFOX wildfire monitoring (NOAA), hurricane research

### E2 Multirotor
- Commercially available UAS platform used in GIS, precision agriculture, infrastructure inspection, environmental research

### S0 UAS
- Ultra-light platform; swarming variant developed under AFWERX funding demonstrating coordinated surveillance and reconnaissance

## Use Cases & Applications

### Defense/Air Force Primary Use Cases
1. **Base Perimeter Security & Installation Protection**
   - Persistent autonomous overwatch
   - Drone detection integration
   - Response to fence line breaches, suspicious activity
   - Reduces personnel burden in dispersed, contested environments
   - Primary anchor customer: Joint Base Elmendorf-Richardson (JBER) 673rd Security Forces Squadron for Arctic/sub-Arctic perimeter patrol and remote facility monitoring

2. **Forward Area ISR & Airfield Support**
   - Autonomously scout and validate C-130 landing strips, temporary airstrips, cargo drop zones in austere environments
   - Landing zone evaluation for Agile Combat Employment (ACE)
   - Logistics route reconnaissance
   - Ideal for forward-operating bases and temporary sites

3. **Battlefield Damage Assessment**
   - Repeatable autonomous flyovers to detect structural changes after kinetic engagements
   - Real-time 3D wind and environmental data critical for flight planning and tactical drops

4. **CBRN & Environmental Monitoring**
   - Integration of specialized payloads for detecting airborne hazards, gas leaks, radiological signatures at remote sites
   - Remote sensing of CBRN threats

5. **Convoy Overwatch**
   - Pre-positioned S3 systems loiter over known routes
   - Autonomous response to movement or sensor triggers

6. **Counter-UAS/Drone Detection**
   - Mobile sensor node for identifying and localizing hostile UAS
   - Collaboration with Ukrainian partners to integrate lightweight drone detection capabilities
   - Protects high-value assets (aircraft on ground, munitions storage) from drone-borne threats

7. **Discreet Island-Hopping Missions (South China Sea)**
   - Geopolitically sensitive region operations
   - Small size, low acoustic signature, extended endurance
   - Autonomous GNSS-denied navigation
   - Performs reconnaissance, surveillance, assessment of adversary activities without alerting hostile forces
   - Operates in electromagnetic-contested environments with reliable performance under electronic warfare or deliberate GNSS disruption

### Commercial/Dual-Use Applications
1. **Methane Leak Detection**
   - Long-range autonomous inspection of energy infrastructure and methane super-emitters
   - 40,000+ oil and gas wells in Permian Basin alone represent substantial addressable market
   - No need for human operators or local infrastructure

2. **Wildfire Monitoring & Atmospheric Sensing**
   - Operation in harsh environments with smoke, turbulence, low visibility
   - Integration with NASA and USFS for drone detection capabilities to improve water bomber safety
   - Real-time atmospheric data collection for operational forecasting and response strategies

3. **Disaster Response & Search & Rescue**
   - Persistent overwatch and communications relay in post-disaster areas
   - Rapid assessment capability
   - Partnerships with NOAA and FEMA for hurricane monitoring and post-hurricane recovery

4. **Infrastructure Monitoring & Mapping**
   - Long-range inspection missions
   - Environmental compliance monitoring
   - GIS and surveying applications
   - Critical infrastructure protection

5. **Scientific Research**
   - Volcano monitoring in remote regions
   - CO₂ sensing and soil moisture analysis
   - High-altitude meteorological data collection
   - Satellite calibration/validation

## Key Results & Performance Data

### Historical S2 Platform Results
- **Volcanic Operations:** Successfully mapped CO₂ emissions over jungle canopy at ~20m above treetops in Costa Rica
- **Range/Altitude:** Demonstrated 25+ mile range and 7,000 ft altitude gain from ground station
- **Weather Performance:** Operated successfully in severe turbulence, high winds, and precipitation conditions
- **Wildfire Monitoring (NightFOX):** Provided real-time atmospheric data that improved NOAA operational forecasting and response strategies
- **Hurricane Research:** Collected turbulent flux data in hurricane boundary layer conditions

### Company Performance Metrics
- **Revenue:** Over $6.8 million generated since 2011
- **SBIR Awards:** 18 awards from NASA, NOAA, USAF, Navy, and others
- **FAA Certificates of Authorization:** Over 140 COAs secured and maintained by Dr. Stachura for operations in Colorado, Kansas, Nebraska
- **Flight Operations:** Hundreds of flight experiments including Arctic deployments
- **COA Applications:** Over 100 authored

### Technical Achievements
- Multiple atmospheric sampling campaigns successfully completed
- 4 different unmanned aircraft systems developed
- NASA Airworthiness Flight Safety Review Board (AFSRB) and Flight Readiness Review Board process completed for NAS operations
- Cooperative control algorithms for multi-UAS demonstrated and evaluated in flight experiments
- Soil moisture mapping UAS development and commercialization (NASA SBIR Phase I & II)

## Notable Details

### Competitive Advantages
- **Unique Capability Gap Fill:** Bridges gap between short-endurance hand-launched drones and large, expensive Group 4/5 ISR assets requiring significant logistical support
- **Infrastructure-Independent:** VTOL eliminates need for launch infrastructure; solar recharge enables repeated sorties without returning to base
- **Dynamic Repositioning:** Unlike fixed surveillance systems, can dynamically reposition based on mission needs, follow patrol routes, respond to emerging threats
- **Incremental Development Path:** Progresses from low-risk semi-autonomous overwatch to fully autonomous, networked teams

### Market Opportunity
- Global small UAS market exceeded $10.4 billion in 2021, projected to reach $35+ billion by 2030
- Defense and critical infrastructure protection among fastest-growing verticals
- 120+ active Air Force installations with vast perimeters and complex security challenges
- Strong near-term private-sector interest in methane monitoring sector to complement government demand

### Strategic Partnerships & Stakeholder Engagement
- **NASA:** Phase III contract awarded for volcano monitoring, CO₂ sensing, soil moisture analysis
- **NOAA:** NightFOX wildfire monitoring campaign, tropical cyclone research partnership (ongoing)
- **USGS:** Multiparametric volcanic data collection (ongoing)
- **