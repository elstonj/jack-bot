# Weather Stream xTech Whitepaper - Soil Moisture Mapping

## Document Metadata
- Type: White paper / SBIR proposal
- Client/Agency: U.S. Army (xTech Overwatch program)
- Program/Solicitation: xTech Overwatch competition
- Date: May 21, 2025 (submission deadline)
- BST Products/Systems Referenced: Black Swift Technologies UAV platforms
- Key Personnel: 
  - Michael Hurowitz (Principal Investigator, Weather Stream)
  - Dr. Eryan Dai (Senior Soil Moisture Scientist)
  - Prof. Albin Gasiewski (Chief Scientist)
  - Dr. Maciej Stachura (CTO, Black Swift Technologies)
  - Ben Andre (Lead Embedded Software Engineer)

## Executive Summary
Weather Stream, in partnership with the University of Colorado Center for Environmental Technology (CET) and Black Swift Technologies, has developed innovative remote sensing technology for measuring soil moisture and soil integrity from UAV, UGV, handheld, and stationary platforms. The system combines a novel L-band microwave radiometer with commercial off-the-shelf vegetation and thermal sensors plus a patented retrieval algorithm, and is nearing full commercial readiness for adaptation to U.S. Army platforms. This technology addresses a JROC Category A meteorological data gap and fills a critical operational need for high-resolution soil moisture mapping that current satellite and ground-based methods cannot provide.

## Technical Approach

**Core Technology Architecture:**
- Novel L-band microwave radiometer (patented)
- Commercial off-the-shelf (COTS) vegetation sensor
- COTS thermal sensor
- Proprietary physics and machine learning-based retrieval algorithms for inverting microwave thermal signals into soil moisture and soil integrity assessments

**Key Technical Capabilities:**
- Produces high-resolution soil moisture maps at meter scale (significant improvement over 50 km satellite resolution)
- Performs sensor fusion from multiple sensor observations to achieve improved data products
- Can assess soil integrity and soil moisture characteristics
- Operates from multiple platform types: UAV, UGV, handheld, stationary

**Prior Development & Validation:**
- Previously funded by NASA for scientific research
- Funded by United States Air Force (USAF) for assessing unimproved runway integrity
- Field testing completed with USAF through runway soil integrity SBIR program
- Multiple operational deployments funded by NOAA and U.S. Geological Survey (USGS)
- Published research; Dr. Eryan Dai's Ph.D. thesis addressed radiometer payload development
- Patent issued; presentations/posters at multiple conferences over 8 years (planned IGARSS 2025 presentation)

**Technical Feasibility Grounding:**
- Team built on world-leading microwave remote sensing sensor developers with experience on programs costing >$100M
- Extensive expertise in radiometer architecture, calibration, system losses, amplifier noise, EMI mitigation, drift, and calibration stability
- Team expertise in physics-based and machine learning retrieval algorithms

## Products & Capabilities Described

**Soil Moisture Radiometer Payload**
- What it is: L-band microwave radiometer combined with multi-sensor fusion (vegetation, thermal)
- How proposed for use: Mounted on Army UAV/UGV platforms to provide real-time, high-resolution soil moisture and soil integrity data products
- Specifications/Performance: Meter-scale spatial resolution (vs. 50 km from satellites); high accuracy through sensor fusion; currently at pre-TRL 8 maturity
- Integration needs: Environmental hardening, relevant interface/software, UAV/UGV platform adaptation

## Use Cases & Applications

**Military/Defense Applications:**
- Trafficability assessments for military operations
- Water resource management in forward operating environments
- Runway soil integrity assessment for aircraft operations
- Support for US Army planners and operators in field decision-making
- Contested environments where satellite/manned aircraft are unreliable

**Commercial Applications:**
- **Agriculture:** Water resource management, crop production optimization, irrigation system design, agricultural operations optimization
- **Golf courses:** Water resource management
- **Mining:** Dust suppression, ore transportation operations
- **Horse racing:** Track condition optimization for competitive fairness
- **Land management:** Wildfire mitigation applications
- **General environmental monitoring:** Scales potential for multi-frequency band deployment to improve vertical resolution and penetration depth

## Notable Details

**Competitive Advantages:**
- Patented IP previously developed with partial support from other U.S. Government partners (NASA, USAF)
- Only technology from U.S.-based vendor; competitors exist from Canada, Switzerland, Spain
- Unique multi-sensor fusion approach vs. international competitors using L-band radiometers alone
- Addresses JROC Category A meteorological data gap
- Significant cost savings from using non-radiation hardened components vs. satellite instruments
- Low-cost platform approach scalable for production in quantity with simple user-friendly software

**Technical Risks Identified & Mitigation:**
- Environmental hardening of sensor
- EMI degradation of sensor performance → potential adaptive spectrum techniques to find quiet spectrum regions
- Enhancing radiometer antenna operating bandwidth
- Adaptation for ground-based platforms
- On-board processing and sensor fusion acceleration
- Each identified as key Phase II development task

**Team Credentials (Combined >100 years experience):**
- Michael Hurowitz: 18 years leading radiometer development (DoD, NASA, NOAA); PI with technology transfer and commercialization expertise; mentor at University of Colorado Research2Market program; experience raising >$100M private investment capital
- Dr. Eryan Dai: 10 years soil moisture radiometer and algorithm development
- Prof. Albin Gasiewski: 40 years microwave radiometer design and calibration (world-respected expertise)
- Dr. Maciej Stachura (BST CTO): 15 years UAV platform development for scientific remote sensing
- Ben Andre: 25 years embedded software development

**Commercialization Track Record:**
- Weather Stream: 100% success rate transitioning Phase I to Phase II SBIR
- >$1M follow-on commercialization dollars on all completed Phase II programs
- Multiple customer discovery interviews across federal civil and defense agencies generated enthusiastic response
- Secured multiple funded pilot programs with commercial customers
- Partnership with Black Swift Technologies provides UAV production capability and experience with harsh environment/scientific research platforms (aircraft considered for Venus operations)

**Production & Transition Readiness:**
- Weather Stream operates 9,500 sq ft facilities suitable for instrument production, calibration/validation, maintenance
- Subcontractor partnerships available for PCB assembly and testing to accelerate production
- Black Swift Technologies supplies aircraft to multiple federal customers
- Clear path identified to produce and deliver capability for Army UAV/UGV platform integration

**Army Customer Validation:**
- Weather Stream participated in U.S. Air Force Catalyst accelerator program for "Terrestrial Weather Technology for the US Warfighter"
- Interest from U.S. Army Corps of Engineers (USACE) members
- Multiple contracts/purchase orders generated from customer discovery efforts