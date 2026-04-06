# MALIBU - Multi Angle Imaging Bidirectional Reflectance Distribution Function Unmanned Aerial Vehicle

## Document Metadata
- **Type:** Mid-year progress report (presentation)
- **Client/Agency:** NASA Goddard Space Flight Center (GSFC), Code 619
- **Program/Solicitation:** IRAD (Internal Research and Development), FY15
- **Date:** September 22, 2015
- **BST Products/Systems Referenced:** Tempest UAS platform (leased)
- **Key Personnel:** 
  - M. Román (PI, GSFC)
  - N. Pahlevan (Instrument PI, SSAI/Code 619)
  - Jack Elston (Black Swift) – listed as collaborator
  - Other collaborators: Geoff Bland, Joel McCorkel, Zhuosen Wang, Ed Masuoka, R. Wolfe, Eric Vermote, John Augustine (NOAA), Ivan Csiszar (NOAA), Chris Justice (UMD), Crystal Schaaf (UMB), Gabriela Schaepman-Strub (U. Zurich), Nigel Fox (NPL), Jan-Peter Muller (UCL)

## Executive Summary
MALIBU is a NASA/GSFC effort to deploy an unmanned aircraft vehicle (UAV) capable of high spatial and angular resolution mapping of global land essential climate variables (ECVs) for Earth observation and climate data record validation. The project aims to make GSFC a global facility for land product validation and multi-angle reference data by integrating multispectral imaging sensors on an airborne platform.

## Technical Approach
MALIBU employs a dual-camera multispectral imaging system mounted on a Tempest UAS platform to achieve multi-angular bidirectional reflectance distribution function (BRDF) measurements. The technical strategy includes:

- **Multi-angle sampling via flight geometry:** Overlapping stereo acquisition along-track (~90% overlap) and cross-track (~70% overlap) enables each pixel to be viewed approximately 15 times along-track and at least 6 times across-track
- **Payload integration:** Two Tetracam Mini MCA6 multispectral cameras with custom filter sets mounted for off-nadir imaging
- **Geolocation approach:** All-of-the-above strategy combining onboard IMU (0.1° uncertainty), onboard GPS (<1m uncertainty), and image-based ground control points
- **Radiative transfer modeling:** MODTRAN5 simulations for Level 2 atmospheric correction and product processing
- **Synthetic validation:** DIRSIG (Digital Imaging and Remote Sensing Image Generation) model at RIT for pre-deployment BRDF imagery generation

## Products & Capabilities Described

### Tempest UAS Platform
- **What it is:** Unmanned aircraft system leased for MALIBU payload integration
- **How used:** Primary airborne platform for sensor deployment
- **Specifications:** Operational altitude ~200m; cruise speed ~20 m/s; 5-hour flight endurance capability
- **Cost:** Tempest lease, integration, and D-GPS upgrade estimated at ~$38K (as of mid-2015)

### Tetracam Mini MCA6 Multispectral Cameras (2 units)
- **What it is:** 2D-array CMOS multispectral imaging system
- **How used:** Mounted off-nadir on Tempest platform in dual configuration; one unit points Unit #1, the other Unit #2 (imaging geometry shown with specific mounting arrangements)
- **Specifications:**
  - Dimensions: 87H × 134L × 78W (mm); Weight: 1.4 kg (700g per camera)
  - 6 spectral channels: 442nm, 488nm, 531nm, 560nm, 650nm, 861nm (FWHM ~25nm)
  - Custom filter sets: [531nm±5nm, 861nm±30nm]
  - Frame size: 1280 × 1024 pixels
  - Field of View (FOV): 35° per camera; Combined FOV ~100° (50° per camera with wider lenses)
  - Pixel pitch: 5.2 micron
  - Angular scan samples: 0.542°
  - Ground Sampling Distance (GSD): 5-25 cm (un-aggregated); 10m (onboard aggregation)
  - **Signal-to-Noise Ratio:** >300
  - **Radiometric uncertainty:** <5% (achieved through frequent GSFC in-house calibration)
  - **Geometric accuracy:** sub-pixel
  - **Geolocation accuracy:** <0.7 pixel
- **Performance claims:** Combined system achieves <10m GIFOV; radiometric uncertainty <5% attained through frequent GSFC RCF (Reference Calibration Facility) calibration using SIRCUS portable calibration unit

### GeoSnap VN-TC Navigation Units (2 units)
- **What it is:** Navigation/geolocation support system
- **Specifications:** PO#NNG15HA47P; Procured cost: $16,700
- **How used:** Supports onboard geolocation via GPS and attitude measurement

### Additional Optical Components
- Wider FOV lenses (6.0-8.0 mm focal length) to achieve ~100° combined FOV
- Irradiance sensor (with Tetracam units)

## Use Cases & Applications

### Primary Mission
- **Global land product validation:** Statistically rigorous validation of MODIS and other space-based land climate data products across multiple locations, time periods, and global conditions
- **Climate Data Record (CDR) assessment:** Direct support for global challenges in assessing Land CDRs
- **Fiducial reference data:** GSFC as global source of reference data for Land Essential Climate Variables (ECVs)

### Specific Applications & Related Missions
- Support for NASA Earth Science initiatives: ABoVE (Arctic-Boreal Vulnerability Experiment), EV (Earth Venture), and Earth Science Decadal missions
- Test bed for multi-angle optical missions and field campaigns
- JPSS-1 Intensive Cal/Val (calibration/validation) efforts

### Specific Field Deployment Sites
- NOAA-BSRN Table Mountain Site (for scaling assessment)

### Multi-angle Science Applications (noted in document)
- Canopy structure parameter retrieval (vegetation cover, forest canopy height, clumping index)
- Snow bidirectional reflectance, fractional cover, and grain size derivation

## Key Results (as of mid-2015 reporting)

### Completed Accomplishments
1. **Sensor suite procurement finalized:**
   - 2× Tetracam-Mini MCA6 with irradiance sensor and custom filter sets (PO#NNG15HC33P; $42,500)
   - Wider FOV lenses 6.0-8.0 mm (Estimated cost: $2,500)
   - 2× GeoSnap VN-TC navigation units (PO#NNG15HA47P; $16,700)
   - **Total procurement: $55.13K**

2. **Platform feasibility studies completed:**
   - Assessed along-track (~90% overlap) and cross-track (~70% overlap) BRDF sampling scenarios
   - Characterized overlapping regions and impact of aircraft altitude changes and geolocation accuracy variations

3. **Radiative transfer modeling initiated:**
   - MODTRAN5 simulations started for Level 2 product processing (atmospheric correction)

### Budget Status (FY15)
- **Procurement:** All IRAD tech equipment and funds expended; remaining costs (~$60K) to be covered by NOAA FY15 Reimbursable funds for JPSS-1 Intensive Cal/Val efforts
- **Manpower:** 0.7 FTE allocated (1,460 hours total); labor burn rate ~640 hours (0.3 FTE) at time of report—well on track

### Remaining Milestones (at time of report)
- Platform lease and integration services: 04/2015
- Sensor characterization: 05/2015
- Integration: 06/2015
- Airworthiness and Flight Safety Review: 06/2015
- FAA Certificate of Authorization: 06/2015
- Test flights and data collection: 07/2015
- Post-deployment calibration: 08/2015
- Data processing: 09/2015

## Notable Details

### Strategic Vision & Sustainability
- GSFC intends to position itself as the global facility for land product validation and multi-angle reference data (modeled on AERONET approach)
- Stakeholders anticipated to seek their own MALIBU platforms
- Plan leverages small business/tech-transfer portfolio: GSFC provides algorithms and calibration expertise; aircraft vendors (implied including BST) provide hardware and support post-baseline

### International Coordination
- Integrated into CEOS (Committee on Earth Observation Satellites) WGCV (Working Group on Calibration and Validation) framework
- Addresses ESA Copernicus and multi-agency satellite validation needs
- Response to 2015 Aqua Senior Review Panel question on MODIS error classification

### Clarifications on Project Scope
- Document explicitly notes MALIBU **is not** "a series of UAVs flying in formation" despite multi-platform future potential
- Current design focuses on single-platform, multi-angle imaging through flight geometry and frequent overlapping stereo acquisition

### Flight Characteristics (at ~200m altitude)
- Coverage: ~600m width (cross-track); 5km flight lines
- Flight time: ~4 min per 5km flight line at 20 m/s cruise speed
- GSD: 18cm near-nadir; 50cm at 70° viewing angle
- Projected full campaign duration: ~5 hours (67 adjacent flight lines + 30 min overhead)
- Each pixel viewed ~15 times along-track, ≥6 times across-track

### Black Swift Connection
Jack Elston of Black Swift Technologies is listed as a key collaborator on the team, suggesting BST's potential role in platform provision or future commercialization of MALIBU systems.