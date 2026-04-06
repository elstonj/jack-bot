# Improved Fire Weather Forecasting with Continuous and Efficient Monitoring

## Document Metadata
- **Type:** NASA Grant Proposal (Draft)
- **Client/Agency:** NASA - Science Mission Directorate, Earth Science Division
- **Program/Solicitation:** NASA ROSES 2024, Announcement NNH24ZDA001N-WF (A.47 Earth Action: Wildland Fires)
- **Date:** Submitted May 24, 2024
- **Proposed Period:** December 2, 2024 – December 1, 2027 (3 years)
- **BST Products/Systems Referenced:** S2 UAS, SwiftCore flight management system, SwiftTab app
- **Key Personnel:**
  - Jack Elston (PI, Black Swift Technologies)
  - Maciej Stachura (Co-I, Black Swift Technologies)
  - Weile Wang (Co-I/Science PI, NASA Ames)
  - Jeremy Benik (Co-I, NASA Ames)
  - Matthew Fladeland (Collaborator, NASA Ames)
  - Joshua Schwarz (Collaborator, NOAA)
  - Troy Thornberry (Collaborator, NOAA)
  - Joey Taylor (Collaborator, NOAA/University of Colorado)

## Executive Summary
Black Swift Technologies proposes a three-year project to enhance wildfire monitoring and forecasting by deploying small, fixed-wing uncrewed aircraft systems (S2 UAS) equipped with advanced infrared sensors to provide persistent, high-resolution observations over active fires and controlled burns. The collected data will be assimilated into the WRF-SFIRE fire-weather model to improve operational fire forecasting and support incident command decisions, demonstrating a scalable, cost-effective alternative to larger crewed and uncrewed aircraft for wildfire management.

## Technical Approach

**Core System:** Multiple Black Swift S2 UAS deployed serially to provide continuous infrared (IR) imagery and fire perimeter data over 24–48-hour periods.

**Key Technical Components:**

1. **Remote Sensing Payload (NOAA NightFOX):** NOAA-developed prototype payload providing:
   - Dual visible/thermal wide-angle camera for full ground coverage
   - Custom-built shortwave infrared (SWIR) camera for fire perimeter measurements
   - Two custom-built narrow-band IR telescopes (~1.6 µm and ~4 µm) with 1° field of view scanning ±30° from nadir
   - Spatial resolution: ~20 m at 1000 m altitude, 1 Hz scan rate
   - Embedded inertial navigation system (VectorNav-200) for precise geolocation
   - Onboard data storage and removable media for rapid post-flight access
   - Field-proven to withstand precipitation and winds >50 kt

2. **Fire-Weather Model:** WRF-SFIRE
   - Two-way coupled fire-atmosphere model combining Weather Research and Forecasting (WRF) model with fire spread model (SFIRE)
   - SFIRE uses level set method with semi-empirical Rothermel Rate of Spread (ROS) model
   - Operates on dual meshes: coarser atmospheric mesh + finer fire mesh near surface
   - Ingests IR fire perimeters to initialize and validate model predictions

3. **Flight Management & Autonomy:**
   - **SwiftCore:** Advanced autonomous flight management system enabling precise control and coordination of multiple UAS
   - **SwiftTab:** User-friendly mobile app (Android) for mission planning, execution, and monitoring
   - Integration with **ATAK** (Android Team Awareness Kit) for joint operations with crewed aircraft and sharing real-time situational awareness (fire location, spread patterns, weather)

4. **Data Telemetry & Real-Time Capabilities:**
   - Near-real-time payload data streaming back to ground station at range up to 10 km (prioritized: dual MWIR scanners first, then SWIR camera)
   - Demonstrated capability: telemetry and live video at 25 km range (BST/USGS Makushin volcano, Alaska); science data link >200 km (BST/NOAA partnership)
   - Onboard computing hardware supports data selection and prioritization for bandwidth-constrained operations

## Products & Capabilities Described

### Black Swift S2 UAS
- **What it is:** High TRL (Technology Readiness Level) fixed-wing small UAS developed by BST under NASA SBIR program
- **Specifications:** Can operate beyond visual line of sight (BVLOS) in mountainous terrain; endures precipitation and winds >50 kt; demonstrated operational use by USGS and NASA Ames
- **Use in this context:** Serial deployment (fleet of 2 minimum) to provide persistent 24–48-hour continuous IR coverage over fires via seamless handoff between aircraft. Designed for challenging Earth Science missions including controlled burn monitoring.

### NightFOX Payload (NOAA-developed, integrated onto S2)
- **What it is:** Complete remote sensing system combining visible, thermal, SWIR, and narrow-band IR sensors with precision navigation
- **Specifications:**
  - Wavelengths chosen to match MODIS and VIIRS fire detection bands for direct satellite-UAS comparison
  - ~20 m spatial resolution; continuous 1 Hz scan at altitude
  - Robust design; demonstrated on multiple field campaigns
- **Use in this context:** Provides primary data stream for fire perimeter mapping, hotspot detection, and fire radiative power (FRP) measurement during active fires. Data fed into WRF-SFIRE and compared against satellite data (MODIS, VIIRS, GOES, Tempo).

### SwiftCore Flight Management System & SwiftTab App
- **What it is:** Integrated autonomous flight control and user interface system for multi-UAS operations
- **Capabilities:** Autonomous precision control, multi-aircraft coordination, handoff sequencing, intuitive mission planning and monitoring
- **Use in this context:** Enables single operator to manage multiple S2 aircraft simultaneously, reducing crew overhead while enhancing safety and operational efficiency. Allows seamless transition between aircraft to maintain continuous coverage.

### WRF-SFIRE Integration
- **What it is:** Coupled fire-atmosphere model capable of ingesting IR perimeters and hotspot data
- **Workflow:** UAS-derived fire perimeters → WRF-SFIRE initialization → fire behavior prediction → forecast outputs for incident command
- **Use in this context:** Post-fire assimilation of UAS perimeter data to refine fire spread predictions; comparison with satellite hotspots; support for controlled burn planning and real-time fire forecasting.

## Use Cases & Applications

1. **Active Wildfire Monitoring & Incident Command Support**
   - Real-time fire perimeter and hotspot detection transmitted to incident commanders via ATAK
   - Continuous coverage (24+ hours) over fire line to augment daily satellite overpasses
   - High spatial/temporal resolution data not available from MODIS/VIIRS

2. **Prescribed/Controlled Burn Operations**
   - Pre-burn WRF-SFIRE simulations using prescribed ignition patterns to predict fire spread
   - UAS fire perimeter capture during burn to validate model predictions
   - Post-burn model validation to improve fire spread algorithms
   - Safer, more efficient burn planning and execution

3. **Fire-Weather Model Improvement & Operational Forecasting**
   - Assimilation of high-resolution UAS perimeter data into WRF-SFIRE
   - Comparison of UAS-derived measurements with satellite data (MODIS, VIIRS, GOES, Tempo)
   - Validation of fire radiative power measurements
   - Support for next-generation WRFx operational fire forecasting system

4. **Airspace Integration & Mixed Operations**
   - Demonstration of UAS-crewed aircraft coordination over active fires
   - Development of operational concepts for NASA ACERO project and FAA next-generation airspace management
   - Support for Federal Emergency Management operations in disaster zones

5. **Interagency Coordination**
   - Collaboration with U.S. Forest Service (USFS) for integration into operational wildfire response
   - Data sharing and coordination with FAA, NASA, NOAA, USGS
   - Contribution to long-term wildfire observation system development

## Project Objectives & Deliverables

### Year 1: Sensor Integration & Controlled Burn Flight
- **Y1-1:** Kickoff, planning, timeline updates, flight deployment planning
- **Y1-2:** Improve payload for real-time data telemetry (10 km+ range)
- **Y1-3:** Complete Airworthiness and Flight Safety Review Board (AFSRB) and Flight Readiness Review Board (FRRB) approvals
- **Y1-4:** Single S2 flight over controlled burn to validate sensors and live data telemetry
- **Deliverable:** Validated sensor package and real-time telemetry capability

### Year 2: Multi-Aircraft Operations & ATAK Integration
- **Y2-1:** Processing Y1 controlled burn flight data; evaluate UAS data contribution to WRF-SFIRE vs. idealized runs
- **Y2-2:** Integrate UAS telemetry and science data into ATAK for active wildfire operations
- **Y2-3:** Coordinated flight campaign with BST and NASA Ames pilots at local test site demonstrating handoff procedures and 12–24 hour continuous coverage CONOPS (Concept of Operations)
- **Y2-4:** Lessons learned report with recommendations for persistent coverage missions
- **Deliverable:** Validated multi-UAS handoff procedures and ATAK integration; minimum 12-hour continuous flight demonstration

### Year 3: Operational Wildfire/Large Burn Flight & Data Assimilation
- **Y3-1:** Updates to S2, sensor, UI, and data pipeline based on Y2 findings
- **Y3-2:** Updated flight permissions from USFS, NASA, and FAA for active fire or large controlled burn
- **Y3-3:** Two S2 UAS flight campaign over active fire (or large controlled burn) providing minimum 12 hours of continuous coverage
- **Y3-4:** Fire perimeter and hotspot data processed and delivered in 1-hour intervals through common operating picture (COP)
- **Y3-5:** Post-campaign data assimilation into WRF-SFIRE; comparison with satellite data; analysis of utility for operational forecasting
- **Deliverable:** Operational demonstration of persistent UAS coverage; processed fire perimeter/hotspot data; WRF-SFIRE assimilation results; final technical report

## Budget & Funding

**Total Project Budget:** $896,539.76 (3 years)
- **Year 1 (FY2025):** $299,542.25
- **Year 2 (FY2026):** $298,245.14
- **Year 3 (FY2027):** $298,752.37

**Key Budget Elements:**
- Direct Labor (Key Personnel): $581,082.80 (PI Elston, Co-I Stachura, Co-Is Wang & Benik; NASA civil servants Benik & Wang receiving $59,373 + $71,985 = $131,358 total)
- Direct Labor (Other Personnel): $125,300.40 (deployment engineers, pilots, NASA support staff)
- Travel: $43,269.86 (domestic field deployments)
- Other Direct Costs: $32,577.32 (NASA technical support, shipping, publication)
- Indirect Costs: $114,309.38

**Application Readiness Level (ARL):**
- Start: ARL 3 (Technology demonstrated in relevant environment)
- End: ARL 6 (Technology demonstrated in operational environment)

## Risk Mitigation

| Risk | Mitigation Strategy |
|------|---------------------|
| Payload/Aircraft failure during landing | Spare parts, spare aircraft, 4 instrumented payloads (2 active, 1 in prep, 1 spare); careful landing site selection |
| Flight permissions (FAA/NASA/fire agencies) | Partnership with USFS; Dr. Stachura's extensive AFSRB/FRRB/COA experience; coordination with NASA ACERO project |
| Lack of wildfire community buy-in | Focus on ATAK integration (growing use by fire agencies); successful prescribed burn participation to build operational credibility |
| Crew fatigue (long-duration missions) | Adherence to NASA crew rest requirements; adequate staffing (3 shifts for critical roles: pilot, GCS pilot, instrument controller, safety observer) |
| Competing operational vs. modeling requirements | Prioritize fire perimeter and hotspot delivery; model improvements as secondary objective