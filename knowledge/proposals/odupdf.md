# ODU STTR Phase II Proposal: Expendable Air-Sea Profiling Observations in Hazardous Weather Conditions

## Document Metadata
- **Type:** STTR Phase II Subcontract Proposal
- **Client/Agency:** Office of Naval Research (ONR)
- **Program/Solicitation:** ONR STTR N25A-T025; Topic N2-9533
- **Date:** February 17-18, 2026
- **Period of Performance:** 1/1/2027 – 12/31/2030 (4 years)
- **BST Products/Systems Referenced:** S0 sUAS (small Unmanned Aerial System), JSBSim framework
- **Key Personnel:** Dr. Hyoshin (John) Park (PI, ODU); Beck Cotter (BST contact)
- **Subcontractor:** Old Dominion University Research Foundation (ODURF)
- **Prime Contractor:** Black Swift Technologies
- **Proposal Number:** ODURF 260784
- **Submission Date:** February 25, 2026 (via email to Beck Cotter)
- **Pricing Validity:** 120 days from February 17, 2026

## Executive Summary
Old Dominion University proposes a four-year STTR Phase II effort to develop autonomous adaptive sampling algorithms for small unmanned aerial systems (sUAS) operating in hazardous weather conditions (tropical cyclones). The work integrates high-fidelity simulation, information-theoretic path planning, AI-based data compression, and onboard autonomy to enable the BST S0 platform to dynamically target regions of high uncertainty in storm environments while managing communication constraints and safety limits.

## Technical Approach

### Core Tasks (ODU Scope of Work)

**Task 1: Simulation Environment Development (JSBSim Integration)**
- Develop research code with Python wrapper executable in BST's JSBSim framework
- **Weather Library Expansion:** Integrate external weather server data based on realistic Tropical Cyclone (TC) structures (wind gradients, turbulence, pressure fields)
- **Virtual Sensors:** Model sUAS sensor noise and errors consistent with historical data

**Task 2: Onboard Path Planning Implementation (IT-RRT*)**
- Re-develop Information-Theoretic Rapidly-Exploring Random Tree (IT-RRT*) algorithm for operation in S0-P3 environments with realistic data
- **Algorithm Architecture:** Address previous dimension issues by optimizing path growing step size and trajectory optimization
- **Cost Function Tuning:** Implement specific cost functions balancing information gain vs. wind/risk constraints (from Phase I)

**Task 3: Trajectory Tracking and Smoothing**
- Convert RRT*-generated paths into realistic flight trajectories respecting sUAS physical constraints and limits

**Task 4: AI-Based Data Compression (Generative Superobbing)**
- **Uncertainty Quantification:** Based on previously developed methods integrated with manifold algorithms
- **TMML Encoder Development:** Create inference-based Temporal Multimodal Multivariate (TMML) encoder as manifold of belief state; convert output to cost function for path planner integration
- **Latent Space Integration:** Feed spatiotemporal correlation output directly into Path Planner to inform trajectory decisions

**Task 5: Model Integration (Software-in-the-Loop Training)**
- **Offline Training:** Models trained using historical NOAA/P-3 hurricane data
- **Onboard Inference:** Run lightweight model on sUAS at low resolution for short-term environmental prediction (e.g., wind vector changes)
- **Model Refinement:** Refine to high resolution with data imputation for realistic flight simulation
- **RRT* Optimization:** Optimize RRT* planner to run online; balance high-performance cloud computing with limited onboard computing and communication
- **Testing:** Evaluate various resolution settings, communication scenarios, and RRT* parameters

**Task 6: Hardware-in-the-Loop (HITL) Validation**
- Verify computational load of RRT* planner and AI inference on actual mission hardware
- Validate safety constraints (geofencing, minimum altitude, max turbulence tolerance)

**Task 7: AI-Based Autonomy in Active Storm**
- Execute adaptive sampling algorithms onboard S0 sUAS during active storm deployments
- **Closed Loop Strategy:** IT-RRT* dynamically generates waypoints targeting high-uncertainty regions (inflow/outflow boundaries) based on real-time sensing
- **Open Loop Comparison:** Fly rule-based sorties alongside AI-driven sorties to quantify information gain increase

**Task 8: Post-Mission Analysis & Validation**
- **Trajectory Analysis:** Compare flown trajectories against pre-planned optimal paths; assess planner responsiveness to unpredicted wind shifts
- **Data Quality Assessment:** Evaluate "Superobs" transmitted by sUAS against full-resolution onboard data to validate compression efficiency and accuracy
- **Reporting:** Generate reports detailing autonomous system performance in operational environments with flight logs and information gain metrics

## Products & Capabilities Described

### BST S0 sUAS
- **What it is:** Small unmanned aerial system serving as primary platform for hazardous weather sampling
- **Proposed use:** Autonomous deployment in tropical cyclone environments with onboard path planning, AI inference, and adaptive sampling
- **Capabilities required:** 
  - Onboard computing capable of running RRT* path planner and lightweight AI models
  - Real-time sensor suite for environmental data collection
  - Data transmission capability (with communication constraints acknowledged)
  - Flight envelope suitable for hazardous weather operations
  - Safety constraint implementation (geofencing, altitude/turbulence limits)

### BST JSBSim Framework
- **What it is:** Flight dynamics simulation framework developed by Black Swift Technologies
- **Proposed use:** Host for high-fidelity simulation environment with weather integration and virtual sensor modeling
- **Technical integration:** Python wrapper enables integration with external weather servers and AI/ML tools

## Use Cases & Applications

### Primary Use Case: Tropical Cyclone (Hurricane) Sampling
- **Mission:** Adaptive sampling of hurricane inflow/outflow boundaries and high-uncertainty regions
- **Operational context:** Hazardous weather deployments requiring real-time autonomy and communication-constrained operations
- **Comparison methodology:** Closed-loop (AI-driven) vs. open-loop (rule-based) sorties to quantify information gain improvements
- **Data collection:** Multi-modal environmental observations (wind pressure, thermal structure)
- **Output products:** 
  - Compressed "Superobs" transmitted in real-time
  - Full-resolution data archived onboard

### Operational Framework
- Integration with existing NOAA/P-3 (manned hurricane research aircraft) data and operational practices
- Field deployments during active hurricane season
- Comparison against historical P-3 hurricane mission data for validation

## Budget & Resource Allocation

### Total Contract Value: $160,000 (ODURF Subcontract Portion)
- **Base Period (Years 1-2):** $80,000/year
- **Option Period (Years 3-4):** $80,000/year
- **Direct Costs:** $90,396
- **Indirect Costs (77% MTDC):** $69,604

### Annual Breakdown
| Category | Year 1 | Year 2 | Year 3 | Year 4 | Total |
|----------|--------|--------|--------|--------|-------|
| Salaries & Wages | $20,454 | $20,149 | $19,251 | $21,376 | $81,230 |
| Fringe Benefits | $1,734 | $1,861 | $1,636 | $1,934 | $7,165 |
| Travel | $500 | $500 | $500 | $500 | $2,000 |
| Direct Costs Subtotal | $22,688 | $22,510 | $21,388 | $23,810 | $90,396 |
| Indirect Costs (77%) | $17,469 | $17,333 | $16,468 | $18,334 | $69,604 |
| **Project Total** | **$40,157** | **$39,843** | **$37,856** | **$42,144** | **$160,000** |

### Personnel Cost Detail

**Dr. Hyoshin (John) Park (PI)**
- Base salary: $119,033 (9-month); 3% annual increase budgeted
- Year 1: 1.55 months summer effort @ $77.23/hr = $20,454
- Year 2: 1.05 months summer effort @ $82.00/hr = $14,304
- Year 3: 1.37 months summer effort = $19,251
- Year 4: 1.05 months summer effort = $15,175
- **Total PI salary:** $69,184

**Graduate Research Assistant (TBN)**
- Starting wage: $38,968 (Year 2); 3% annual increases budgeted
- Year 2: 1.13 months academic effort @ $29.97/hr = $5,845
- Year 4: 1.13 months academic effort @ $31.80/hr = $6,201
- **Total GRA salary:** $12,046

### Fringe Benefits (ONR Negotiated Rate, May 15, 2025)
- **Faculty summer:** FICA (7.65%), workers' compensation (0.435%), unemployment insurance (1%)
- **GRA:** Workers' compensation (0.435%), health insurance ($600/spring semester)
- **Total fringe:** $7,165

### Travel: $2,000 Total
- $500 per trip (4 trips total), domestic travel to DoD visits/exercises/conferences
- Estimated costs per trip:
  - Airfare: $162
  - Lodging (1 night @ $180): $180
  - Meals (2 days @ $79/day): $158
  - Ground transport (2 days @ $50/day): $100
  - **Subtotal per trip: $500**

### Indirect Cost Rate
- **ONR Predetermined Rate (July 3, 2025):** 77% on Modified Total Direct Costs (MTDC)
- **Effective Period:** 7/1/2025 – 6/30/2026
- **Applicable to:** Organized Research, On-Campus DOD contracts awarded on or after November 30, 1993 (per DFARS 231.303(2), uncapped)

## Key Technical Concepts & Innovations

### Information-Theoretic Path Planning (IT-RRT*)
- Algorithm designed to balance information gain (sampling high-uncertainty regions) with operational constraints (wind avoidance, energy limits, risk tolerance)
- Closed-loop execution: Real-time sensor feedback drives dynamic waypoint generation rather than pre-planned routes
- Previous Phase I work identified dimension and resolution issues; Phase II focuses on architectural improvements and realistic data integration

### Temporal Multimodal Multivariate Learning (TMML)
- Dr. Park's research focus integrates acoustic, visual, and flow-field data to predict environmental evolution
- Applied to adaptive sampling: manifold-based representation of belief state informs path planner
- Converts uncertainty quantification into cost functions for path optimization

### Adaptive Data Compression (Generative Superobbing)
- AI-based method to compress high-resolution observations into "Superobs" for transmission over communication-constrained channels
- Maintains fidelity assessed against full-resolution onboard data archive
- Enables real-time data downlink and cloud-based model refinement during mission

### Software-in-the-Loop to Hardware-in-the-Loop Progression
- **SIL Phase:** Offline training on historical NOAA/P-3 data; dual-resolution onboard inference (lightweight for immediate planning; high-resolution for accuracy)
- **HIL Phase:** Validation on actual S0 hardware before operational deployment
- **Operational Phase:** Live execution in active hurricane conditions with closed-loop vs. open-loop comparison flights

## Notable Details

### Principal Investigator Background
**Dr. Hyoshin (John) Park**, Associate Professor, Old Dominion University (Fall 2023–)

**Personal Details:**
- **US Citizenship:** Since 2024
- **Contact:** h1park@odu.edu; 2101F Engineering Systems Building, Norfolk, VA 23529
- **Website:** fs.wp.odu.edu/h1park

**Key Research Focus:**
- Physics-informed, data-driven self-learning integrating real-time sensor data with hydrodynamic models to map uncertainty in multimodal complex ocean environments
- Temporal Multimodal Multiva