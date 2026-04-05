# Navy STTR Phase II Proposal: Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- **Type:** Navy STTR Phase II Subcontract Proposal
- **Client/Agency:** Office of Naval Research (ONR); prime contractor Black Swift Technologies
- **Program/Solicitation:** ONR STTR N25A-T025; STTR Topic N2-9533
- **Date:** February 17-18, 2026
- **Subcontractor:** Old Dominion University Research Foundation (ODURF)
- **Principal Investigator:** Dr. Hyoshin (John) Park, Old Dominion University, Department of Engineering Management & Systems Engineering
- **Period of Performance:** Base period 1/1/2027–12/31/2028; Option period 1/1/2029–12/31/2030
- **BST Products/Systems Referenced:** S0 sUAS (small UAS), JSBSim simulation framework
- **Key Personnel (BST contact):** Beck Cotter (beck.cotter@blackswifttech.com)
- **Total Project Value:** $160,000 (ODURF subcontract); $80,000 base period + $80,000 option period

## Executive Summary
Old Dominion University proposes to develop and validate autonomous, AI-driven adaptive sampling algorithms for small unmanned aircraft systems (S0 sUAS) operating in hazardous tropical cyclone environments. The work integrates physics-informed machine learning, information-theoretic path planning (IT-RRT*), and data compression techniques to enable real-time environmental profiling and uncertainty-driven waypoint generation during active storm deployments. The research builds on Phase I foundational work and focuses on transitioning simulation and algorithm development to hardware-in-the-loop testing and operational field validation.

## Technical Approach

### Core Technical Tasks:

**Task 1: Simulation Environment Development (JSBSim Integration)**
- Develop Python-wrapped research code executable in Black Swift's JSBSim framework
- Integrate external weather server data with realistic tropical cyclone structures (wind gradients, turbulence, pressure fields)
- Model sUAS sensor noise and errors consistent with historical data

**Task 2: Onboard Path Planning Implementation (IT-RRT*)**
- Redevelop "Information-Theoretic Rapidly-Exploring Random Tree" (IT-RRT*) algorithm for S0-P3 environments with realistic data
- Address current limitation of unreasonably high dimensionality by redesigning architecture with variable path-growing step sizes and trajectory optimization
- Implement cost functions balancing information gain versus wind/risk constraints

**Task 3: Trajectory Tracking and Smoothing**
- Smooth RRT*-generated paths into realistic flight trajectories respecting S0 sUAS physical constraints and limits

**Task 4: AI-Based Data Compression (Generative Superobbing)**
- Develop "Data Loop" for on-the-fly data reduction and uncertainty quantification
- Create inference-based Temporal Multimodal Multivariate (TMML) encoder as a manifold of belief state; convert to cost function for path planner feedback
- Integrate latent space spatiotemporal correlations to inform trajectory decisions in real-time

**Task 5: Model Integration (Software-in-the-Loop Training)**
- Train models offline using historical NOAA/P-3 hurricane data
- Implement lightweight onboard inference for immediate short-term environmental evolution (wind changes)
- Refine to high-resolution version with data imputation for realistic flight
- Optimize RRT* path planner for online execution; balance high-performance cloud environments with limited onboard computing and communication
- Test multiple resolutions, communication scenarios, and RRT* parameters

**Task 6: Hardware-in-the-Loop (HITL) Validation**
- Verify computational load of RRT* planner and AI inference on actual mission hardware
- Validate safety constraints (geofencing, minimum altitude, maximum turbulence tolerance)

**Task 7: AI-Based Autonomy in a Storm**
- Execute adaptive sampling algorithms onboard S0 sUAS during active storm deployments
- Implement "Closed Loop" control strategy: upon release, IT-RRT* planner dynamically generates waypoints targeting high-uncertainty regions (inflow/outflow boundaries) based on real-time sensing
- Conduct parallel "Open Loop" (rule-based) sorties to quantify information gain improvement

**Task 8: Post-Mission Analysis & Validation**
- Compare flown trajectories against optimal pre-planned paths to assess planner responsiveness to wind shifts
- Evaluate "Superobs" (compressed data products) transmitted by S0 sUAS against full-resolution onboard data to validate compression efficiency and accuracy
- Produce reports detailing autonomous system performance with flight logs and information gain metrics

## Products & Capabilities Described

### S0 sUAS (Small Unmanned Aircraft System)
- **What it is:** Black Swift's expendable small unmanned aircraft platform designed for harsh environments
- **Proposed use in this context:** Primary platform for executing autonomous adaptive sampling during tropical cyclone operations; carries onboard sensor suite and runs lightweight AI inference models
- **Performance/technical requirements:** Must operate under extreme wind/turbulence; support onboard path planning, inference, and sensor data processing; communicate limited data via available communication link

### JSBSim Flight Simulation Framework
- **What it is:** Black Swift's proprietary or adopted simulation environment for aircraft dynamics
- **Proposed use:** High-fidelity simulation environment for algorithm development, testing, and validation before flight operations
- **Integration:** Python wrapper for seamless integration with machine learning/planning algorithms

### IT-RRT* (Information-Theoretic Rapidly-Exploring Random Tree*)
- **What it is:** Sampling-based motion planning algorithm optimized for information gain in uncertain environments
- **Capabilities described:** Plans trajectories that maximize environmental information acquisition while respecting physical and risk constraints; redeveloped in Phase II to handle realistic high-dimensional spaces and variable step sizes
- **Performance claims:** Can dynamically adapt waypoints in real-time based on sensed environmental evolution

### Temporal Multimodal Multivariate (TMML) Learning / Generative Superobbing
- **What it is:** AI-based data compression and representation learning system fusing acoustic, visual, and flow-field sensor data
- **Capabilities:** Quantifies uncertainty; encodes high-dimensional sensor data into low-dimensional latent representations; infers immediate short-term environmental changes; outputs compressed "Superobs" products for transmission
- **Performance objective:** Enable real-time transmission of limited data while retaining information content and uncertainty estimates

## Use Cases & Applications

### Primary Use Case: Tropical Cyclone (Hurricane) Profiling
- **Mission Context:** Expendable air-sea profiling observations during active hazardous weather (tropical cyclones/hurricanes)
- **Specific Application:** Deploy S0 sUAS to sample regions of high atmospheric/oceanographic uncertainty (inflow/outflow boundaries, eyewall structures, wind shear layers)
- **Information Goals:** Improve understanding of storm structure evolution, intensity change mechanisms, and air-sea interaction in extreme conditions
- **Operational Scenario:** Real-time adaptive sampling where the aircraft autonomously decides where to fly next based on uncertainty maps and environmental observations, rather than following pre-planned waypoints

### Comparison Flights
- Parallel "Open Loop" (human-planned, rule-based) and "Closed Loop" (AI autonomous) sorties to quantitatively compare information gain and operational effectiveness

## Key Technical Details & Design Rationale

### Sensor and Communication Constraints
- Limited onboard computing (necessitates lightweight inference models)
- Limited communication bandwidth (drives need for intelligent data compression and superobbing)
- Hazardous operating environment (extreme winds, moisture, salt spray) motivates expendable aircraft design

### Physics-Informed AI Integration
- Models trained on historical NOAA/P-3 hurricane reconnaissance data (established ground truth)
- Manifold learning and latent space methods preserve spatiotemporal correlations
- Cost functions explicitly balance:
  - **Information gain:** regions of high uncertainty in environmental fields
  - **Physical constraints:** wind limits, turbulence tolerance, altitude bounds
  - **Risk:** geofencing, mission safety

### Closed-Loop Adaptive Sampling Strategy
- **Real-time sensor feedback** informs path planner
- **Uncertainty quantification** drives waypoint selection
- **Dynamic replanning** as new data arrives
- Contrasts with traditional pre-planned fixed-waypoint missions

## Budget Summary (ODURF Subcontract)

| Category | Year 1 | Year 2 | Year 3 | Year 4 | Total |
|----------|--------|--------|--------|--------|--------|
| **Labor** | $20,454 | $20,149 | $19,251 | $21,376 | $81,230 |
| **Fringe Benefits** | $1,734 | $1,861 | $1,636 | $1,934 | $7,165 |
| **Travel** | $500 | $500 | $500 | $500 | $2,000 |
| **Total Direct** | $22,688 | $22,510 | $21,388 | $23,810 | $90,396 |
| **Indirect (77% MTDC)** | $17,469 | $17,333 | $16,468 | $18,334 | $69,604 |
| **PROJECT TOTAL** | $40,157 | $39,843 | $37,856 | $42,144 | **$160,000** |

**Base Period:** $80,000 (1/1/2027–12/31/2028)  
**Option Period:** $80,000 (1/1/2029–12/31/2030)

**Labor:**
- Dr. John Park (PI): 450 hours Year 1 @ $77.23/hr; 420 hours Year 2 @ $82.00/hr
- Graduate Research Assistant: 195 hours Year 2 @ $29.97/hr; 195 hours Year 4 @ $31.80/hr
- 3% annual salary increases projected

**Travel:** $500 per trip × 2 domestic trips per year for DOD/program reviews in Washington DC area (airfare ~$162, lodging ~$180, meals, ground transport)

**Indirect Cost Rate:** 77% of Modified Total Direct Costs (MTDC) per ONR negotiation agreement dated July 3, 2025, effective 7/1/25–6/30/26 for DOD organized research on-campus

## Notable Details & Context

### Principal Investigator Background
Dr. Hyoshin (John) Park is an Associate Professor at ODU (Fall 2023–present) with extensive expertise in:
- Physics-informed, data-driven machine learning for complex ocean/environmental systems
- Temporal Multimodal Multivariate Learning (TMML) and adaptive AI
- Information-theoretic path planning and multi-agent autonomy
- Previous appointments: Visiting Professor AFRL (2025), NASA JPL (2018–2022), North Carolina A&T (2017–2023)
- **125 peer-reviewed publications** (25 journal, 100 conference) and **41 technical reports**
- **35 grants** totaling **$46.4M** ($2.4M personal PI share) from NSF, DOE, NASA JPL, USDA, USDOT, ONR, AFRL, etc.
- **4 issued U.S. patents** (2020–2025) in transportation autonomy and robotic navigation
- Outstanding Young Investigator Award (NCA&T 2022)

### Prior Relevant Funded Work
- **ONR 2025–2026:** Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions via sUAS (this proposal is Phase II)
- **NSF 2019–2025:** IMPACT—Information-theoretic Multiagent Paths for Anticipatory Control of Tasks
- **NASA JPL 2018–2022:** Ground/Air Adaptive Edge Mars Multimodal Autonomy
- **AFRL 2025:** Cooperative Tactics and Staging for Heterogeneous Teams

### Subcontractor Role
ODURF is a subrecipient to Black Swift Technologies (prime contractor). The proposal must comply with:
- ONR Consortium policy on inter-organizational agreements
- DFARS 252.204-700(a)(3) Fundamental Research determination (requested from DOD Contracting Office)
- OMB Uniform Guidance (2 CFR Part 200) cost principles
- ONR negotiated fringe benefit rates (32% full-time, 4.9% part