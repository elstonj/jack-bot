# Monitoring and Measuring Volcanoes with Unmanned Aerial Systems (UAS)

## Document Metadata
- Type: NASA proposal/capability brief
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR program (mentioned); appears to be a disaster response proposal
- Date: Created 2018-06-07; Modified 2018-06-20
- BST Products/Systems Referenced: S2 XT UAS, SwiftCore Flight Management System (FMS)
- Key Personnel: Jack Elston (last editor); Dr. Ryan Perry (University of Hawaii at Hilo); Jorge Diaz (University of Costa Rica); reference to pilot with 1000+ UAS hours

## Executive Summary
This proposal describes a comprehensive UAS-based system for monitoring and measuring volcanic eruptions, combining multirotor and fixed-wing aircraft to provide both rapid-response capabilities and extended-duration scientific measurements. Black Swift Technologies' S2 XT system is presented as the primary fixed-wing platform, offering superior payload capacity and endurance compared to traditional manned aircraft while avoiding risks from sulfur dioxide, intense heat, and ash plumes.

## Technical Approach

**System Architecture:**
- Hybrid approach combining multirotor quad-copters (rapid deployment, hovering capability, 30-min endurance, limited payload) with fixed-wing UAS (1.5-hour endurance, 5-8 lb payload capacity, low-altitude capability)
- Electric propulsion for fixed-wing systems to avoid anoxic environment problems (sulfur dioxide robs oxygen-dependent engines)
- Real-time data relay to ground operators for adaptive mission planning
- Multiple simultaneous UAS operations for spatially diverse data collection

**S2 XT UAS Specifications:**
- **Airframe:** 3.0 m (10.0 ft) wingspan, 5.2 kg (11.5 lbs) nominal weight, 6.6 kg max
- **Flight Performance:** 12 m/s (24 kts) stall speed, 18 m/s (35 kts) cruise; 110 min maximum endurance, 90 min nominal; 110 km (60 nm) max range, 92 km (50 nm) nominal
- **Ceiling:** 6,000 m (20,000 ft)
- **Payload Capacity:** 2.3 kg (5 lbs)
- **Environmental:** IP42 ingress protection; withstands 15 m/s (30 kts) winds
- **Assembly:** <30 minutes pre-flight setup
- **Automation:** Custom flight plan menus reduce pilot input and human error
- **Proven Field History:** Successfully operated at Turrialba Volcano, Costa Rica at ~9,000 ft MSL; flown by NASA for multiple scientific campaigns

**SwiftCore Flight Management System:**
- Simplified user interface and flight planning menus
- Supports multiple mission profiles including volcano plume monitoring menu
- Based on commercially-available, proven platform

## Products & Capabilities Described

### S2 XT UAS
The primary platform, specifically designed for extreme environments and scientific sensing. Offers unrivaled payload capability for volcano monitoring in its class with field-proven performance in ash clouds and volcanic emissions (CO2, H2O sampling demonstrated).

### Payloads (Field-Swappable)

**3D Wind Sensor (BST-developed)**
- Measures turbulence, updrafts, and atmospheric movement in-situ
- Described as critical for plume characterization
- Addresses airspeed as largest source of flux measurement error

**Multi-Gas Sensor (NCR Mini-Gas)**
- Developed by Jorge Diaz (University of Costa Rica) for small UAS
- Electrochemical gas sensors with PTH (pressure-temperature-humidity) integration
- Measures: SO2, H2S, CO2
- Day/night capable; useful for volcanic unrest monitoring

**Particle Counter**
- Six channels, user-selectable size bins: 0.3, 0.5, 1.0, 2.5, 5.0, 10.0 µm
- Real-time ground station visibility
- Characterizes aerosol and particulate movement within plume

**Particulate Sampler**
- Multi-stage filter system with on-demand sampling
- Samples collected based on real-time sensor data
- Tagged with time, location, air volume, and all sensor metadata

**Calibrated Infrared Imager (BESST - Ball Experimental Sea Surface Temperature Radiometer)**
- Microbolometer-based system with two black bodies for 2-point calibration (one ambient, one cooled to 12°C below ambient)
- Samples at 3 Hz; calibration cycle ~7 seconds (85% data collection efficiency)
- TRL6+ (previously flown on ScanEagle UAS, 2013 Arctic Marginal Ice Zone study)
- Corrects for sky radiation reflected off surfaces
- Can retrieve actual temperatures (not just radiances)

**Synthetic Aperture Radar (SAR) - X-band (BYU System)**
- Operates at 10 GHz for all-weather, day/night imaging
- Enables interferometric processing (InSAR) for vertical deformation measurements
- Compact: 7"×9"×10", 6 lbs, 46W power consumption
- Includes integral IMU with GPS and gyros for precise positioning
- 1TB solid-state disk enables 10 days continuous operation
- TRL6+ (flown on multiple missions)
- Ground processing via time-domain back projection for motion/range compensation and georectification
- Backscatter sensitive to dielectric constant and surface roughness

**Geo-Stabilized Thermal/Visible Camera (FLIR M625CS)**
- Pan/tilt capability with 2X e-zoom
- Geo-stabilized platform independent of aircraft attitude
- Automatic window heater for ice/condensation prevention
- Day/night navigation capability
- Ethernet connectivity for data download

**Hyperspectral Imager (HSI)**
- Visible to near-infrared pushbroom system (NASA Glenn Research Center development)
- Produces 3D hyperspectral data cube with spectral signature per location
- Calibrated to wavelength (Hg/Ar reference lamp) and radiance (NIST-traceable Labsphere source)
- Georeferenced via inertial navigation and GPS
- TRL6+ (multiple iterations for manned and unmanned aircraft)
- HSI4 variant optimized for small UAS: 55° FOV yields ~1,040 ft swath at 1,000 ft altitude (~0.305 m/pixel cross-track, ~0.85 m/pixel along-track at 92 km/hr speed)

**High-Resolution EO Camera**
- 25 MP color camera, downward-facing
- Post-processing: mosaics, data overlays, change detection, structure-from-motion 3D rendering

**Forward-Looking Real-Time Video**
- Navigation to areas of interest, hazard avoidance, outreach

## Use Cases & Applications

**Volcanic Eruption Monitoring:**
- Real-time observation of active fissures and lava flows
- Thermal mapping of active volcanic features
- Detection of ground deformation via repeat SAR imaging and InSAR processing
- Monitoring of volcanic unrest in suspected eruption zones (surface temperature + vertical deformation)
- SO2, H2S, CO2 flux characterization in volcanic plumes
- Ash plume characterization (3D wind patterns, particle size distribution, altitude determination)
- Particulate sampling from ash and steam/smoke plumes
- Rapid thermal and visible documentation of eruption progression

**Observed Operations (Kilauea 2018):**
- Monitoring Fissure 6 eruption at Kilauea with thermal and visible time series
- Documenting active fissures and ground cracks in Leilani Estates
- Thermal imaging of pavement cracks along Highway 130
- Night-time lava flow monitoring near Puna Geothermal Venture power plant
- Civil Defense hazard mapping and public webpage integration

**Ground-Aerial Integration:**
- Fusion of ground-based observations with aerial perspective
- Real-time guidance from ground crews to airborne sensors
- Objective measurement (eliminates subjective interpretation between ground and airborne observers)

## Key Results

**Field Demonstrations (Turrialba Volcano, Costa Rica):**
- S2 XT successfully overflew vents at ~9,000 ft MSL
- Confirmed operation in ash clouds
- Demonstrated accurate CO2 and water vapor sampling capability
- Launched and recovered from small clearing on volcano slope (confirmed versatility and ruggedness)

**Kilauea 2018 Campaign (UH Hilo operations):**
- Time series thermal and visible imagery of active fissures
- High-resolution low-altitude visible and thermal data (captured 5/8/18)
- Data integration into Civil Defense public webpage maps
- Night-time documentation of lava flow approach to critical infrastructure

**BESST Radiometer (Arctic MIZ, 2013):**
- Comparison with MODIS SST measurements validated instrument
- Wavenumber spectral analysis showed uniform slope of -2 (wavelengths 25 m to 25 km), consistent with submesoscale oceanographic processes
- Confirmed submesoscale temperature variability detection capability

## Notable Details

**Safety & Regulatory Advantages:**
- UAS eliminate risk to personnel from volcanic hazards (toxic gases, heat, ash)
- Can be lost without endangering human life (unlike manned aircraft)
- Cleared for operations by 4 different NASA flight safety review boards
- FAA Part 107 compliant operations within sight-line, single-system, daylight/twilight, 400 ft AGL, 100 mph max speed
- Operated within NPS guidelines and local regulations
- Requires NASA Flight Release and extensive flight test plan
- Pilot certification: Remote pilot airman certificate with small UAS rating; 1,000+ UAS hours including Arctic freezing temperatures, tornadic supercells, altitudes >14,000 ft

**Competitive Advantages:**
- Swappable payload design for mission versatility
- Real-time data relay enables adaptive mission planning
- Electric propulsion avoids anoxic environment engine failures
- 2-hour endurance (60-mile coverage) without measurement gas contamination
- Rapid 24/7 deployment (<30 min assembly)
- Intuitive user interface reduces operator training burden
- Payload capability "unmatched" in class
- Combines capabilities of prior research (NSF-RAPID funding for quad-copter observations) with extended-range fixed-wing platform

**Funding Model:**
- NASA provides 100% funding Year 1, declining to 40% by Year 4
- Cost share expectations: Year 1 $0, Year 2 20%, Year 3 40%, Year 4 60%
- Estimated Year 1 request: $400-500k (with $80k requested for quad-copter operations portion)

**Partnerships:**
- University of Hawaii at Hilo (Dr. Ryan Perry, quad-copter operations)
- University of Costa Rica (Jorge Diaz, Mini-Gas sensor)
- NASA Glenn Research Center (HSI development)
- BYU (SAR system)
- Hawaiian Volcano Observatory (HVO) – intended data user for modeling
- Italian COSMOSKYmed satellite program (existing HVO SAR data source)

**Document Status:**
This appears to be a draft proposal with editorial notes and incomplete sections ("Ryan, I need you to add in some text here..."), suggesting it was not finalized before being archived in the "Completed/Inactive/Unsubmitted Projects" folder.