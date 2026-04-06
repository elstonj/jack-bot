# RAVEN: Rover–Aerial Vehicle Exploration and Navigation

## Document Metadata
- **Type:** PSTAR (Planetary Science and Technology Through Analog Research) proposal
- **Client/Agency:** NASA
- **Program/Solicitation:** Planetary Science and Technology Through Analog Research NNH17ZDA001N-PSTAR
- **Date:** September 27, 2017 (submitted)
- **BST Products/Systems Referenced:** None directly; Jack Elston listed as collaborator
- **Key Personnel:** Jack Elston (Black Swift Technologies, listed as collaborator); PI Christopher W. Hamilton (University of Arizona); multiple co-investigators from JPL, University of Tennessee, University of Arizona, and other institutions

## Executive Summary
RAVEN proposes to develop and field-test integrated rover-aerial vehicle exploration systems using Iceland's 2014–2015 Holuhraun lava flow as a Mars analog. The project will compare rover-only mission architectures against two sUAS-enhanced approaches: one using a multi-rotor system with a deployable sample-acquisition device (RavenClaw) and another using a VTOL fixed-wing sUAS for reconnaissance. Field deployments in 2019–2020 will validate whether combined rover and sUAS operations improve scientific return and operational efficiency over traditional rover-only designs.

## Technical Approach

### Task 1: Physical and Chemical Characterization
- Develop 1:800-scale facies maps of entire Holuhraun lava flow; 1:200-scale maps of three focused study sites
- Use sUAS surveys, remote sensing, and ground-truth observations to characterize lava flow emplacement processes and surface textures
- Perform in situ chemical analyses using ASD field spectrometer (400–2500 nm) to identify silica and sulfate deposits indicating hydrothermal alteration
- Map lava–water interactions including hot springs, fumarolic activity, and hydrothermal precipitates
- Conduct biological sampling of hot springs and water characterization

### Task 2: Technology Development
**Terrain Relative Navigation (TRN) System:**
- Adapt JPL's TRN software from Lander Vision System (LVS) heritage for rover localization
- Use sUAS-derived digital terrain models (DTMs) via multi-view stereo-photogrammetry (MSVP) to create coregistered orthomosaics equivalent to LVS maps
- Expected to improve rover 3D positional estimates to ±5–20 cm (versus ~10 m cumulative uncertainty after 100 m with odometer/optical flow)
- Allows rovers to safely traverse "over the horizon," reducing manual position updates via triangulation
- Run on separate laptop to avoid major modification to rover control software; only requires wireless image transmission protocol from rover's navigation camera

**RavenClaw System:**
- Fabricated by Honeybee Robotics (Co-I Zacny)
- Integrated into DJI Matrice 600 frame with 6 kg payload capacity
- Deployable claw suspended from vertical standoff distance of 2 m, capable of capturing unconsolidated surface material from rough terrain (boulder fields, ʻaʻā lava)
- Spool system retrieves claw with sample; fail-safe quick-release mechanism if sample becomes lodged
- Equipped with gimbal and camera (DJI Zenmuse Z15-A7 3-Axis Gimbal with Sony Alpha 7R)
- Navigation via DJI D-RTK GNSS-G Flight Control system with Trimble R10 GNSS DGPS base station
- Autonomous take-off, landing, image acquisition; manual piloting for sampling operations

### Task 3: Field-Testing Rover-Only vs. RAVEN Mission Designs
- **Year 2 (2019):** Team A conducts rover-only baseline mission at Location 1 (Holuhraun flow margin with former fumarole and hot springs deposits) using HiRISE-scale imagery (25 cm/pixel) and 1 m/pixel DTMs. Simultaneously, Team B (Group 3) operates RavenClaw and VTOL sUAS at other locations and trains for Year 3; Group 1 conducts science investigations.
- **Year 3 (2020):** Team B conducts rover + VTOL sUAS mission at same Location 1, using high-resolution sUAS-derived DTMs (4–20 cm/pixel) and orthomosaics (1–4 cm/pixel). Team A members sequestered to prevent bias.
- Field seasons: July 31–August 23, 2019 and July 30–August 22, 2020; 24-day deployments with 16 full operational days planned
- Field team: 12 people, 5 4×4 vehicles, 2 covered trailers
- Integration tests at CSA Headquarters in Montréal during February each year (2 weeks, 3 U.S. team members)

## Products & Capabilities Described

### Mars Exploration Science Rover (MESR)
- Canadian Space Agency prototype Mars science-class rover
- Comparable trafficability to flight-design rovers (MSL, Mars 2020, ExoMars)
- Features: mast-mounted cameras, robotic manipulator arm, autonomous path planning using LIDAR, visual odometry, IMU-corrected odometry
- Operational modes: remote and autonomous (can navigate beyond sensing horizon using embedded autonomy)
- Equipped with simplified science payload (Table 3):
  - Stereo imaging (MESR integrated cameras, comparable to MastCam/PanCam)
  - Handheld ASD field spectrometer (400–2500 nm, comparable to ChemCam/SuperCam)
  - Tripod-mounted Sony α7R camera with zoom lens (context imaging)
  - Handheld analog instrument with simulated reachability rules (comparable to SHERLOC)
  - High-resolution handheld imaging with macro lens (comparable to MAHLI/CLUPI)
- Can be operated with realistic communications delays, power budgets, data volume constraints, and sol-based planning cycles

### Small Unmanned Aerial Systems (sUAS)
Two architectures evaluated:

**1. Multi-rotor with RavenClaw (Group 3A lead: Co-I Moersch)**
- DJI Matrice 600 base with deployable sample-acquisition device
- Optimized for remote sample collection and retrieval
- Manual piloting for sampling; autonomous for navigation/imaging

**2. VTOL Fixed-wing (Group 3B lead: Co-I Farber)**
- Optimized for reconnaissance scouting
- High-resolution imagery collection for DTM generation (1–4 cm/pixel orthomosaics)
- Provides data for TRN and rover path planning

### Data Products
- sUAS-derived orthomosaics: 1–4 cm/pixel resolution
- Digital terrain models: 4–20 cm/pixel resolution (derived via MSVP)
- High-resolution mapping coverage: >25% of Holuhraun lava flow at 1–4 cm/pixel

## Use Cases & Applications

### Primary Use Case: Lava-Induced Hydrothermal Systems as Mars Analog
- **Study Site:** Holuhraun lava flow, Iceland (August 2014–February 2015 eruption; 1.5 km³ lava, 83.3 km² coverage)
- **Mars Analog Target:** Athabasca Valles flood lava (250,000 km², <50 Ma; potentially 1.5–20 Ma), containing Volcanic Rootless Cones (VRCs) indicating lava–water interactions
- **Scientific Question:** Can ephemeral hydrothermal systems preserve biosignatures on Mars and within buried deposits that might be excavated by rootless eruptions?
- **Astrobiological Interest:** Salts from hydrothermal fluids can preserve microorganisms for >250 Ma; comparable salt deposits observed by Spirit rover at Gusev Crater on Mars

### Operational Applications
- **Rover Trafficability Improvements:** sUAS reconnaissance reduces safe traverse distance limitations (~100 m/sol for direct line-of-sight) by providing advance terrain mapping
- **Sample Acquisition:** RavenClaw enables collection from terrain inaccessible to rovers (rough lava flows, boulder fields)
- **Rapid Sampling for Sample Return Missions:** RavenClaw could support caching samples for future Mars sample return missions
- **Enhanced Rover Localization:** TRN-enabled rovers can navigate "over the horizon" without line-of-sight constraints, dramatically improving traversing efficiency
- **Mission Planning Efficiency:** High-resolution sUAS imagery allows mission planners to identify safe paths and science targets with greater confidence than orbital imagery

### Mars Mission Implications
- Direct contribution to Mars2020 Helicopter technology validation (approved for $15M funding)
- Results inform design of next-generation sUAS for Mars (helicopters, gliders, airplanes)
- Demonstrates feasibility of integrated rover + sUAS mission architectures for future Mars exploration

## Key Results (Proposal Stage)

Not yet a report; this is a proposal. However, the document includes pre-proposal field investigations at Holuhraun (2014–2017) with preliminary findings:

### Prior Field Campaign Findings
- **Temperature monitoring:** Hot springs region cooled from 48°C (July–August 2015) to 17°C (July–August 2017), indicating hydrothermal system waning
- **Thermophile isolation:** Water samples (2016) yielded three thermophile strains:
  - *Geobacillus stearothermophilus* (well-characterized endospore-forming thermophile)
  - *Paenibacillus cisolokensis* (well-characterized endospore-forming thermophile)
  - Novel strain with 96% genetic match to *Pseudorhodoplanes sinuspersici*, isolated at 50°C showing strong growth at 40–70°C (unusual, as species typically cannot survive >35°C); represents previously undocumented thermophile species of genus *Pseudorhodoplanes*
- **Remote sensing coverage:** sUAS surveys acquired >25% of flow at 1–4 cm/pixel resolution; 80+ terrestrial laser scans completed; >20 km of flow margin mapped using DGPS; geodetic network established with Differential GPS
- **Biological sampling:** Comprehensive water characterization (temperature, velocity, conductivity, turbidity, pH, chlorophyll fluorescence, dissolved oxygen, nutrient concentrations)

### Expected Deliverables (from Proposal)
- **Manuscript 1 (Year 2):** Physical and chemical characteristics of Holuhraun lava flow, detailed facies maps
- **Manuscript 2 (Year 3):** Synthesis of physical, chemical, and biological aspects of ephemeral hydrothermal system; analogy to Athabasca Valles on Mars
- **Manuscript 3 (Year 3):** New advances in rover localization using TRN and sUAS-derived DTMs; engineering specifications of two RAVEN architectures
- **Manuscript 4 (Year 3):** Critical assessment of RAVEN versus rover-only mission architectures; trade-offs in complexity, trafficability, and scientific return

## Notable Details

### BST Connection
Jack Elston of Black Swift Technologies is listed as a collaborator, though his specific role is not detailed in the proposal sections provided. Given BST's expertise in small UAS systems, his involvement likely relates to sUAS operations planning or technical consultation.

### Team Structure
- 4 research groups with dedicated group leads reporting to PI Hamilton
- Monthly virtual coordination meetings
- Interdisciplinary team: geologists, engineers, astrobiologists, mission operations specialists
- Previous MESR experience: Co-Is Osinski and Francis conducted three prior multi-week analog deployments (including Mars Sample Return Analogue Deployment in Hanksville, Utah, 2015–2016)

### Field Logistics & Risk Mitigation
- **Weather margin:** 50% operational efficiency built into plan (8 of 16 days minimum) based on 30-year average weather data from Icelandic and Norwegian meteorological offices
- **Power:** Two Honda EU3000is generators in long-term Iceland storage (3 kW each)
- **Communications:** 4G cellular coverage (Vodafone), TETRA radios as backup (115.2 kbit/s at 25 kHz)
- **Data transfer:** Physical USB transport from field to Drekagill campsite (12 km, ~20 min drive) to ensure reliability
- **Hardware redundancy:** Two identical Raven