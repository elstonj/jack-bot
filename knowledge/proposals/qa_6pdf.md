# NOAA SBIR 2018-1 Questions and Answers #6

## Document Metadata
- Type: Q&A Clarification Document
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration)
- Program/Solicitation: SBIR 2018-1 (Small Business Innovation Research)
- Date: December 7, 2017
- BST Products/Systems Referenced: None explicitly mentioned
- Key Personnel: Jack Elston (last editor)

## Executive Summary
This is a compendium of clarifying questions and answers issued by NOAA regarding their SBIR 2018-1 solicitation. The document addresses technical requirements, specifications, and application guidance for multiple subtopics spanning marine monitoring, environmental sensing, autonomous systems, and aquaculture disease detection. No further questions were permitted after this release.

## Technical Approach & Requirements by Subtopic

### Subtopic 8.1.2: Fish Spawning Data Collection Device
**Challenge:** Develop a device to collect data from fish during spawning and retrieve it remotely.
- **Data Retrieval:** Satellite transmission (popup satellite tag technology) preferred
- **Size/Weight Constraints:** Must fit inside/through fish oviduct; reference smallest acoustic tags (~1 cm × 0.5 cm)
- **Power Requirements:** Minimum 6-month continuous operation
- **Cost Target:** ≤$3,000/device
- **Deployment Duration:** 6+ months

### Subtopic 8.2.1: Real-Time Phytoplankton Characterization
**Challenge:** Develop instrument to characterize phytoplankton species in field conditions.
- **Throughput:** Acquire statistically representative sample data within minutes
- **Processing:** Delayed analysis acceptable; local or remote processing both acceptable
- **Species Focus:** Common coastal and inland water algae species initially
- **Approach:** Acceptable to focus on transferable methods using representative species examples that can expand library as system develops
- **Size:** Lower detection limit desired; no specific minimum mandated

### Subtopic 8.2.5: Low-Cost Subsurface Mooring Beacon
**Challenge:** Develop beacon to locate/track moorings that surface unexpectedly during deployment.
- **Communication:** Satellite, cellular, or AIS acceptable; subscription fees assumed
- **Data Transmission:** Location 3× daily sufficient
- **Cost Target:** Reduce below current ~$3,000 baseline by reducing capabilities (depth, autonomy, data volume)
- **Operation:** Subsurface standby mode; transmit location when surfaced
- **Depth Rating:** ≤500 m for coastal applications
- **Temperature Range:** All conditions (arctic to tropical) required
- **Battery Life:** Minimum 10 months (deployments 6-8 months; recovery delays up to 1 month)
- **Active Beaconing Duration:** 1-2 months desired for recovery assistance
- **Transmission Frequency:** 1-2 times daily acceptable; missing locations 1-2 days during extreme weather acceptable
- **Interfaces:** No specific hardware/software/communication interfaces required

### Subtopic 8.2.8: Under Keel Clearance (UKC) Software Solution
**Challenge:** Develop software for ship under-keel management using existing data streams.
- **Approach:** Software-only solution incorporating existing bathymetry, surface current data (S-129 standard)
- **Integration:** Incorporate ship parameters to visualize go/no-go areas based on UKC calculations
- **Platforms:** ECDIS (Electronic Chart Display and Information System), ECS, Portable Pilot Units
- **Implementation:** Could be cloud-based to serve dataset to various navigation systems
- **Flexibility:** Each manufacturer uses different operating systems

### Subtopic 8.2.9: Cost-Effective ROV Survey System
**Challenge:** Develop low-cost ROV-integrated system for shallow-water bathymetric survey.
- **Maximum Depth:** ~10 feet (vessel grounding response); potential expansion to harbor clearing post-hurricane
- **Offshore Range:** 8-10 nautical miles (RTK not viable)
- **Cost Target:** ~$15,000 (current approach baseline); preference for integrated package over component-only proposals
- **Instruments:** No specific package mandated; awareness of smaller, lower-cost survey-grade GPS options exists
- **Preference:** Complete integrated ROV+instrument package; component-only proposals would require target ROV platform identification and size/weight/power specifications

### Subtopic 8.2.10: Self-Positioning Water Level Monitoring Station
**Challenge:** Automate position verification and data collection for water level systems.
- **Accuracy Requirement:** Self-position within 0.1-cm sphere (all directions) relative to national/state spatial reference systems
- **Functionality:** Monitor vertical displacement and motion continuously
- **Phase I Scope:** Develop concept, design, and first article addressing automation of data collection, processing, QA/QC
- **GNSS Requirements:** Yes, continuous GNSS observations required

### Subtopic 8.2.11: Clean Energy Generation for Coastal Monitoring Networks
**Challenge:** Develop clean, low-cost, small-footprint power generation/storage for remote observation networks.

**Power Requirements:**
- Peak: 1.5 kW for 2 hours/day
- Low-power mode: 40 watts for other instruments/sensors and standby
- Minimum duty: 6 months continuous operation with no maintenance; 1-year target
- Arctic to tropical operation required

**Cost Targets:**
- Laboratory prototype/demonstration: <$200,000
- Commercialization/production scale: <$50,000

**Footprint:** Fit onto typical NOAA buoy (1.5-meter diameter)

**Technology Scope:**
- "Traditional battery technology" = disposable single-use batteries (environmentally harmful)
- "Clean battery" = rechargeable batteries powered by renewable sources (solar, wind, thermal)
- Temperature-gradient power generation explicitly mentioned but innovative alternative technologies encouraged
- Unacceptable: Nuclear power, radioisotope fuel sources
- Data/Cost drivers: Environmental concern is battery leakage of toxic materials into marine environment

### Subtopic 8.2.13: Air-Deployed Hurricane Observation UAS
**Challenge:** Develop autonomous UAS for in-situ hurricane measurement via P3 mothership deployment.

**Flight Environment:**
- Operating altitude: <1 km preferred
- Average vertical wind: ±1 m/s typical
- Extreme vertical winds: Short bursts of ±20 m/s recorded (rare, uncommon)
- Downdraft risk greatest below 500 m altitude
- Wind feature scale: 1-3 km horizontal
- Flight strategy: Harness prevailing winds (20-30° deviations acceptable)

**Flight Profiles:**
- Circumnavigate hurricane eyewall (launched from P3 in calm eye; fly counterclockwise in high-wind region)
- Track spiral currents away from center converging to eyewall/eye
- Reference: Past successful missions with Aerosonde (2005 Ophelia, 2007 Noel) and Coyote (Edouard, Maria)

**Launch & Control Requirements:**
- Launch method: GPS or Sonobuoy launch sleeve from NOAA P3
- Communication: One-way data retrieval only via AVAPS (Atmospheric Vertical Atmospheric Profiling System)
- Critical Requirement: Onboard autonomous AI system for GPS/sensor-based autonomous operation (no realtime telemetry control post-deployment)
- Range: ~200 nautical miles (AVAPS system capability)
- Data Management: Onboard data logger/hard drive required for loss-of-link data preservation
- Telemetry: Collected via AVAPS on mothership P3
- No active UAS operator on P3 or ground during flight

### Subtopic 8.3.1: Coral Nursery Efficiency
**Challenge:** Increase efficiency of coral restoration techniques.
- **Species Flexibility:** Acropora palmata specified for Caribbean; alternate species acceptable if solution scales/adapts to A. palmata
- **Geographic Flexibility:** Alternative regions (Indo-Pacific, Hawaii, West Coast) acceptable for demonstration if solution scales to Caribbean
- **Design Preference:** Solutions with flexibility across regions and environments encouraged

### Subtopic 8.3.6: Real-Time Aquaculture Pathogen Detection
**Challenge:** Develop instrument for accurate, real-time pathogen identification in aquaculture.

**Throughput:** Varies by organism biology and state regulations

**Processing:** Near-real-time preferred with accuracy to minimize false positives; local or remote processing acceptable

**Vibrio Detection:**
- Target concentration levels: Must meet Interstate Shellfish Sanitation Commission and state health department thresholds
- Multiple species of Vibrio with varying thresholds across states and species

**Scope of Pathogens:**
- Primary focus: Pathogens causing aquaculture area closure, trade impacts, or animal/human health effects
- Beyond Vibrio: Animal health and human health pathogens of concern
- Transferability: System may be species- or region-specific; multiple common pathogen detection acceptable

**Approach:** General multi-pathogen system framework acceptable, demonstrated on specific example pathogens

## Notable Details

1. **Formatting Flexibility:** No line-spacing preference specified (single, double, or 1.5 acceptable)

2. **AVAPS Integration (Subtopic 8.2.13):** Critical requirement to use existing NOAA AVAPS dropsonde system; applicants strongly encouraged to review system documentation and contact AVAPS design engineers for compatibility understanding

3. **Environmental Concerns:** Battery leakage into marine environments is driver for Subtopic 8.2.11 clean energy requirement

4. **Recovery Logistics (Subtopic 8.2.5):** Beacon intended to assist drift recovery operations; location transmitted to recovery crews for field search, not for real-time directional finding via remote crew

5. **Technology Maturity:** Phase I addresses concept/design/first article; Phase II addresses cost refinement and demonstration

6. **Geographic/Species Flexibility Encouraged:** Multiple subtopics (8.3.1, 8.3.6) explicitly encourage demonstrations in non-specified geographies/species if solutions demonstrate scalability to specified baseline

---

**Note:** This document contains no references to Black Swift Technologies products or personnel. It is a NOAA solicitation clarification document of archival value to BST for understanding the technical requirements and customer expectations of the 2018 SBIR program.