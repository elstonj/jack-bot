# BAH UAM Executive Briefing

## Document Metadata
- Type: Executive Briefing / Market Study Report
- Client/Agency: National Aeronautics and Space Administration (NASA) - Aeronautics Research Mission Directorate
- Program/Solicitation: Not explicitly stated; appears to be a NASA-commissioned Urban Air Mobility market assessment
- Date: October 5, 2018
- BST Products/Systems Referenced: None mentioned (this is a Booz Allen Hamilton study, not a BST document)
- Key Personnel: Not explicitly named as BST team; document is from external research organizations

## Note on Document Sourcing
**This document is NOT a Black Swift Technologies product, proposal, or technical document.** It is a market study conducted by Booz Allen Hamilton (BAH) in partnership with the Transportation Sustainability Research Center (TSRC) at UC Berkeley, presented to NASA. It appears to have been filed in BST's reference materials for the Wind Sensing SBIR program context, likely as background research on Urban Air Mobility markets. As such, it does not contain information about BST's products, capabilities, or technical approaches.

## Executive Summary
This comprehensive market study analyzes the viability of three Urban Air Mobility (UAM) markets—Airport Shuttle, Air Taxi, and Air Ambulance—across ten major U.S. urban areas (New York, Washington DC, Miami, Houston, Dallas, Denver, Phoenix, Los Angeles, San Francisco, and Honolulu). The analysis finds that while these markets represent a total available market of $500B in unconstrained scenarios, significant legal/regulatory, technological, societal, and weather constraints reduce near-term market capture to only 0.5% of total available market, worth approximately $2.5B. The study concludes that eVTOL-based air ambulance services face insurmountable technology constraints (particularly battery recharging times) unless hybrid VTOL aircraft or battery-swapping capabilities are employed.

## Technical Approach
The study employed a comprehensive multi-disciplinary assessment methodology:

### Market Selection and Calibration
- **Step 1**: Screened 40 candidate urban markets; selected three focus markets based on interesting barriers
- **Step 2**: Applied calibration criteria across six dimensions:
  - Economics (market size, growth rate, technology cost, competitive pricing, willingness to pay)
  - Technology (speed, range, TRL, payload, autonomy capabilities)
  - Operational Challenges (enabling infrastructure, navigational constraints, network scalability)
  - Societal factors (noise, community acceptance)
  - Legal & Regulatory (ATM, federal/state/local laws)
  - Technical Specs and cost challenges

- **Step 3**: Selected three focus markets: Airport Shuttle (early market), Air Taxi (mass market), Air Ambulance (complex market)

### Key Operational Assumptions (for demand modeling)
- Pilot on-board control (no autonomy) for first years of operation, though aircraft designed for full autonomy from beginning
- Maximum mission distance: 50 miles per single charge
- Passenger load factor: 50-80%
- Aircraft utilization: 1,000-2,000 flight hours per year
- Reserve fuel: 20-30 minutes (FAA Part 91 requirement)
- Deadend trips (non-revenue): 25-50%
- Detour factor: 5-15% above great circle distance
- Cruise altitude: 500-5,000 feet

### Analysis Framework Components

**Societal Barriers Analysis**: Employed STEPS Framework (Spatial, Temporal, Economic, Physiological, Social) developed by BAH and TSRC/UC Berkeley. Included literature review, focus groups (multiple cities), and large-scale survey (~1,700 respondents across 5 major cities).

**Weather Analysis**: Used multiple data sources:
- METAR (Meteorological Aerodrome Report) - hourly surface observations at takeoff/landing
- Vertical soundings from weather balloons (twice daily) for in-flight conditions
- Pilot Reports (PIREP) - supplemental real-world observations
- Analysis focused on IFR conditions, high winds (>20 kts), storms, temperature extremes, wind shear, low visibility

**Market Demand Modeling**: Cascading constraint scenarios:
1. Unconstrained (infrastructure and cost unlimited)
2. Infra + WTP Constrained (willingness to pay, using existing heliports/airports)
3. Capacity Constraint (infrastructure operational limitations)
4. Time of Day Constraint (specific operational windows)
5. Weather Constraint (VFR-only operations initially)

Monte Carlo analysis (10,000 iterations) used for cost modeling, particularly for Air Ambulance scenarios.

## Products & Capabilities Described
This document does not describe BST products or capabilities. It analyzes three categories of aircraft/concepts:
- eVTOL (electric vertical takeoff and landing) aircraft
- Hybrid VTOL aircraft
- Rotary wing helicopters (baseline for comparison)

The document references several real-world eVTOL manufacturers mentioned in SAG context (Boeing, Airbus, Bell Helicopters) and specific concepts (Zee.Aero Z-P1, Volocopter), but does not evaluate BST systems.

## Use Cases & Applications

### Airport Shuttle
- Service to/from airport for passengers
- Early market with relatively defined routes and infrastructure
- Operates in constrained geographic corridors

### Air Taxi
- Point-to-point urban transportation
- Most commercially viable mass market potential
- Intra-city trips varying from 5-50 miles
- Survey respondents indicated preference for inter-regional trips (DC-Baltimore, LA-San Diego) over very short trips

### Air Ambulance
- Emergency medical transport from accident scenes to hospitals
- Inter-hospital transfers
- Public safety/lifeline service with high public acceptance
- Complex due to mission profile requirements (response, transport, return to service)

### Geographic Focus Areas
Analysis concentrated on ten representative U.S. urban areas representing various climatological, geographic, and density profiles:
- **Eastern/Dense**: New York, Washington DC
- **Southeastern**: Miami
- **South-Central**: Houston, Dallas
- **Southwest/Mountain**: Phoenix, Denver
- **Western**: Los Angeles, San Francisco
- **Pacific**: Honolulu

## Key Results and Findings

### Market Size and Value Projections

**Air Taxi (Near-Term - Base Year)**
- Unconstrained demand: 11,000,000 daily trips across all 10 urban areas
- After applying all constraints (infrastructure, capacity, weather, time of day): 55,000 daily trips / ~82,000 daily passengers
- Aircraft required: ~4,100 eVTOLs
- Annual market value: ~$2.5 billion
- Cost per passenger mile: 5-seat eVTOL ~$6.25/mile (near term); potential 60% reduction long-term with improvements

**Airport Shuttle**
- Viable market with significant potential
- High variability by urban area

**Air Ambulance**
- Total cost per transport: eVTOL ~$9,000; Hybrid ~$9,800; current rotary wing ~$10,000; ground ambulance ~$500
- **Critical finding**: eVTOLs NOT viable due to battery recharging constraints (total call time with recharging: 275 minutes vs. 130 minutes for rotary wing)
- Dispatch reliability for eVTOLs: 88% (vs. 99% for rotary wing at current utilization)
- **Solution pathways**:
  - Fast recharging (4x current rate) could enable 100% of RW market capture
  - Battery swapping could enable 100% of RW market capture
  - Hybrid VTOL aircraft more viable alternative

### Demand Sensitivity Analysis
- **Negative demand drivers** (reduce demand 50-100%):
  - Autonomous ground vehicles as competition
  - Increased telecommuting
  - No technical improvements
- **Positive demand drivers** (increase demand 100-500%):
  - High network efficiency
  - Increased value of travel time
  - Technology cost reductions (15-30%)
  - Infrastructure capacity doubling
  - Autonomous eVTOL capability

### Individual Urban Area Results
Constrained daily demand varies significantly:
- New York: 8,000 daily trips
- Los Angeles: 7,500 daily trips
- Houston: 4,890 daily trips
- Dallas: 4,750 daily trips
- San Francisco: 1,250 daily trips
- Denver: 1,460 daily trips
- Honolulu: 550 daily trips

### Price Comparison
- 5-seat eVTOL: ~$11/passenger mile
- 2-seat eVTOL: ~$6.25/passenger mile (comparable to current helicopter air taxi services)
- Luxury ride-sharing (ground): $3-6/mile
- Economy ride-sharing (ground): ~$0.50/mile
- Helicopter (baseline): comparable to 5-seat eVTOL
- Autonomous ground taxi (future): $0.35/mile

## Constraints and Barriers

### Technology Constraints
- **Battery Technology**: Weight and recharging times detrimental to eVTOL air ambulance viability
- **Weather Sensitivity**: Adverse conditions significantly affect operations and performance
- **Economics**: High capital and operating costs; battery costs particularly problematic
- **Air Traffic Management**: High-density operations will stress current ATM infrastructure
- **Environmental Impacts**: Noise pollution could affect community acceptance
- **Cybersecurity**: Autonomous systems vulnerable; no mature security protocols

### Legal and Regulatory Barriers
**Current regulatory gaps and required new regulations**:
- Beyond Visual Line of Sight (BVLOS) operations (currently only with lengthy waiver process)
- Operations over people, streets, populated areas
- Commercial cargo transport across state lines
- Passenger transport (remotely or autonomously piloted)
- Flight in instrument conditions
- Airworthiness certification for remotely piloted and autonomous aircraft
- Pilot/operator training and knowledge requirements
- Privacy frameworks addressing surveillance concerns

**Certification Challenges**:
- System redundancy and failure management standards not yet defined
- Determining appropriate certification basis (Part 21.17(b) leverage of Parts 23, 27, 33, 35)
- Lack of clear path for autonomous vehicle failure decision-making
- DO-178C testing for software could be onerous
- Multi-copter propulsion and energy storage redundancy standards undefined

**State/Local Legal Diversity**:
- Some states prohibit all drones (Hawaii)
- Others provide immunity to first responders (California, Arizona)
- Some restrict operations near critical facilities (Texas)
- Patchwork creates significant barrier to national operations

### Societal/Public Perception Barriers
**Key Concerns from Survey and Focus Groups** (~1,700 respondents across 5 cities):
- **Safety**: Primary concern (unruly/violent passengers, aircraft sabotage, "lasing" of pilots)
- **Automation Trust**: Significantly lower willingness to fly autonomous aircraft vs. piloted
- **Brand Trust**: Passengers trust systems from established companies more than startups
- **Crew Confidence**: Preference for experienced pilots (age bias); preference for flight attendants for non-user confidence (though didn't impact user willingness)
- **Cost Sensitivity**: Primary consideration for mode choice
- **Privacy Concerns**: Flying overhead, sight lines into homes/yards
- **Noise**: Expected to be more noticeable as electric ground vehicles reduce ambient noise

**Survey Results** (Likert scale responses for willingness to travel by UAM):
- Piloted: 14% willing alone; 25% with known passengers; 12% with unknown passengers
- Remotely piloted with flight attendant: 10% alone; 29% with known; 10% with unknown
- Remotely piloted without attendant: 11% alone; 27% with known; 10% with unknown
- Automated with attendant: 10% alone; 28% with known; 10% with unknown
- Automated without attendant: 11% alone; 27% with known; 10% with unknown

**Key Findings**:
- General public shows neutral to positive reaction to UAM concept
- Strong preference for piloted operations (may require mixed fleet or discounts for remote/automated)
- Most interested in short inter-regional trips (DC-Baltimore, LA-San Diego)
- Potential peer-to-peer (P2P) market could supplement commercial supply
- Flight attendant presence increased confidence from ground-observer perspective but did NOT increase user willingness to fly

### Weather Constraints

**San Francisco Urban Area**:
- Strong winds (>20 kts) most frequent adverse condition
- IFR conditions frequent during morning hours in summer
- Afternoon winds significantly higher at SFO than Oakland