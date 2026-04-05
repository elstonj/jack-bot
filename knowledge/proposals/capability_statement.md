# NOAA Capability Statement

## Document Metadata
- Type: Capability Statement
- Client/Agency: NOAA (National Oceanic and Atmospheric Research Administration)
- Program/Solicitation: NOAA Sources Sought (not a formal proposal response, but an unsolicited capability statement for potential opportunities)
- Date: January 28, 2026
- BST Products/Systems Referenced: S0 Air-Deployed (S0-AD), S0 VTOL, S2 Fixed-Wing, S3 VTOL, E2 Multirotor
- Key Personnel: Dr. Jack Elston (CEO)

## Executive Summary
Black Swift Technologies is a small business UAS designer and manufacturer (founded 2011, Boulder CO) specializing in purpose-built unmanned aircraft systems for scientific payloads in extreme environments. This capability statement presents BST's five-platform portfolio—S0-AD (air-deployed), S0 VTOL, S2 fixed-wing, S3 VTOL, and E2 multirotor—each tailored to address specific NOAA mission gaps across hurricane boundary-layer sampling, coastal profiling, atmospheric research, wildfire monitoring, and localized sensing. The statement emphasizes BST's vertically integrated design-manufacture-operate model, proprietary SwiftCore™ flight management system, and extensive operational heritage in severe weather and remote environments.

---

## Technical Approach

### Core Philosophy
BST's technical approach centers on **purpose-built design for harsh environments** rather than adaptation of commercial platforms. Key design principles include:
- **Expendability as an enabling feature** (particularly S0-AD): allows placement of sensors in hazardous regions without risk to personnel or high-value crewed assets
- **Autonomy-first architecture**: systems designed to operate independent of continuous command-and-control links, essential for storm penetration
- **Integrated design**: airframe, avionics, communications, and payload are co-designed as a unified system
- **Environmental robustness**: platforms validated for hurricane-force winds, extreme turbulence, heavy precipitation, icing, salt spray, and extreme cold

### Proprietary Systems
- **SwiftCore™ Flight Management System**: end-to-end avionics and autonomy stack (in-house developed) integrating state estimation, guidance, navigation, control, communications, and payload management. Supports fully autonomous flight, adaptive mission execution, sensor-informed control, and real-time telemetry.
- **SwiftTab™**: custom ground control software optimized for scientific and operational missions (not hobbyist workflows). Supports complex survey geometries, stacked profiling, adaptive retasking, and sensor-driven behaviors.
- **Modular payload architectures**: designed for rapid field reconfiguration and open integration with external sensors

---

## Products & Capabilities Described

### 1. **S0 Air-Deployed (S0-AD) UAS**

**What it is:**
- Tube-launched, fixed-wing, air-deployed, attritable UAS
- Purpose-built to be expendable; designed to sustain operations in conditions exceeding conventional UAS design envelopes
- Deployable from crewed aircraft (e.g., NOAA WP-3D)

**Key Specifications:**
| Attribute | Specification |
|-----------|---------------|
| Flight endurance | ~60–90 minutes nominal; extended endurance demonstrated in recent hurricane ops |
| Cruise/dash speed | Cruise ~20–22 m/s; dash >40 m/s for storm-relative maneuvering |
| Ceiling/altitude regime | Deployed from crewed aircraft; operational profiling from several km AGL down to ~30–50 ft above ocean surface |
| Low-altitude capability | Sustained low-altitude flight over ocean with laser altimeter for wave clearance |
| Environmental limits | Designed for hurricane-force winds, extreme turbulence, heavy precipitation, icing |
| Thermal envelope | Validated for extreme cold (~−65 °F) |
| Core sensor suite | Pressure, temperature, humidity; 3D winds via multi-hole probe; turbulence metrics derivable at high rate |
| Sampling rates | 10–100 Hz (mission dependent) |
| Comms | Long-range UHF link optimized for air-deployed ops; autonomous execution tolerant of intermittent comms |
| Data products | Real-time telemetry; automated QC; near-real-time NetCDF outputs compatible with NOAA workflows |

**How Proposed to be Used:**
- Deploy from NOAA WP-3D aircraft into targeted regions of tropical cyclones identified in real time by onboard radar
- Execute autonomous profiles from deployment altitude down to 30–50 ft above ocean surface
- Collect high-rate thermodynamic and wind measurements enabling estimation of turbulence statistics and boundary-layer structure
- Support hurricane intensity forecasting via air–sea interaction and turbulent flux characterization
- Real-time data assimilation and operational situational awareness for National Hurricane Center

**Unique Design Features:**
- Fixed-wing airframe compact and aerodynamically stable across wide range of Reynolds numbers and angles of attack
- Control authority maintained in high turbulence and strong vertical shear
- Propulsion and control layout minimize sensitivity to precipitation, icing, and debris ingestion
- Avionics emphasize reliability and graceful degradation
- Core flight control, navigation, sensing functions designed for autonomous operation without continuous C2 links
- Heated nose and conformal-coated electronics for extreme environments

**Operational Heritage:**
- Repeated flights in 2024 hurricanes
- Demonstrated sustained flight in hurricane-force winds, extreme turbulence, heavy precipitation, icing
- Iterative design refinements based on deployment lessons learned

---

### 2. **S0 VTOL UAS**

**What it is:**
- Hybrid VTOL–fixed-wing atmospheric profiling UAS
- Extends S0 severe-weather measurement capability to missions where launch/recovery flexibility is critical
- Enables persistent profiling from locations without conventional aviation infrastructure

**Key Specifications:**
| Attribute | Specification |
|-----------|---------------|
| Platform type | Hybrid VTOL–fixed-wing atmospheric profiling UAS |
| Endurance | ~60–90 minutes depending on profile and payload |
| Cruise speed | ~17–20 m/s |
| Ceiling | Profiling to ~15,000 ft AGL |
| Gross takeoff weight | ~1.6–1.8 kg class |
| Payload capacity | ~100–150 g (science sensor suite) |
| Core measurements | Pressure, temperature, humidity; 3D winds via miniaturized multi-hole probe |
| VTOL capability | Autonomous vertical launch and recovery in confined areas and from vessels |
| Environmental robustness | Designed for high-wind launch/recovery, precipitation, turbulent boundary layers |

**How Proposed to be Used:**
- Rapid deployment of atmospheric profiling from coastal sites, research vessels, and remote field positions during severe weather events
- Autonomous vertical launch and recovery in confined areas
- Pre-, during-, and post-landfall atmospheric profiles during landfalling hurricanes
- Repeated vertical profiles and boundary-layer transects over days or weeks from same location
- Support for diurnal variability studies and land–sea interactions

**Design Approach:**
- Hybrid configuration preserves environmental performance of baseline S0 airframe while adding VTOL capability with minimal compromise
- Avionics and autonomy stack shared with S0-AD, ensuring consistency in flight behavior, data products, and operational procedures
- Control laws and state estimation algorithms tuned specifically for gusty, turbulent environments
- Maintains control authority during high-wind vertical operations (typical challenge for VTOL UAS)

---

### 3. **S2 Fixed-Wing UAS**

**What it is:**
- Reusable, science-grade fixed-wing atmospheric profiling and remote sensing UAS
- Emphasizes flexibility, sensor interoperability, and operational maturity
- Designed for stable, low-noise flight essential for accurate atmospheric measurements

**Key Specifications:**
| Attribute | Specification |
|-----------|---------------|
| Platform type | Fixed-wing, reusable, science-grade UAS |
| Endurance | ~90 minutes nominal; up to ~110 minutes maximum |
| Range | ~50–60 nm |
| Ceiling | ~20,000 ft |
| Max winds endured | ~15 m/s (30 kt) sustained; higher gust tolerance in complex terrain |
| Payload capacity | Up to ~2.3 kg (5 lb) |
| Payload bay | Modular nose cone; ~50 W payload power |
| Launch/recovery | Catapult or rail launch; autonomous belly landing or net recovery |

**Typical Payloads:**
- Multispectral and RGB cameras
- Thermal IR
- Trace gas sensors (CO₂, CH₄, SO₂)
- Aerosol instruments
- Multi-hole wind probes for 3D winds
- Radiometers (e.g., L-band soil moisture)
- Small LiDAR

**How Proposed to be Used:**
- Boundary-layer and mesoscale observations, turbulence/flux studies
- Smoke and plume sampling; model validation; repeatable field campaigns
- Wildfire monitoring with combined thermodynamic sensors, aerosol instruments, and thermal/multispectral imagers
- Volcanic plume characterization (CO₂ measurements, 3D terrain mapping via photogrammetry)
- Soil moisture mapping (radiometry)
- Coastal surveys and air quality mapping
- Validation of satellite-derived products
- Pre- and post-event surveys

**Historical Examples:**
- 2018 Hawaii volcanic eruption observations
- NASA CRATER project in Costa Rica (CO₂ measurements near volcanic vents)
- Coordination with surface towers, lidar, and radar systems for flux/turbulence studies
- Wildfire plume thermodynamics paired with thermal fire mapping

---

### 4. **S3 VTOL UAS**

**What it is:**
- VTOL-capable, modular fixed-wing UAS designed to scale S2 capabilities into infrastructure-limited environments
- Combines vertical takeoff/landing with efficient fixed-wing cruise
- Enables science-grade payload deployment from ships, confined coastal sites, remote locations

**Key Specifications:**
| Attribute | Specification |
|-----------|---------------|
| Platform type | VTOL-capable, modular fixed-wing UAS |
| Payload capacity | Multi-payload capable; designed to exceed S2-class single-payload configs |
| Endurance | Mission dependent; designed to preserve fixed-wing endurance while enabling VTOL |
| Launch/recovery | Autonomous VTOL launch and recovery |
| Typical payloads | Imaging (RGB/multispectral/thermal), atmospheric sensor suites, combined payload stacks |
| Autonomy | Shared autonomy lineage with S2/S0; repeatable survey and profiling missions |

**How Proposed to be Used:**
- Shipboard operations in coastal and marine environments
- Multi-sensor missions combining atmospheric profiling, imaging, and surface characterization
- Infrastructure-limited environments (no runways required)
- Rapid repositioning and VTOL recovery reduce operational risk and crew workload
- Support for NOS and OAR missions focused on coastal processes, air–sea interaction, marine meteorology

**Design Emphasis:**
- Modularity and mission flexibility (payloads swappable in field)
- Single platform supporting imaging, atmospheric sensing, or combined missions in same campaign
- Adaptive to changing priorities or environmental conditions

---

### 5. **E2 Multirotor UAS**

**What it is:**
- Autonomous multirotor UAS designed for precise positioning, hovering, and detailed local observations
- Complements fixed-wing platforms for close-in measurement and inspection

**Key Specifications:**
| Attribute | Specification |
|-----------|---------------|
| Platform type | Autonomous multirotor UAS |
| Maximum payload | ~2.0 kg class (configuration dependent) |
| Typical endurance | ~25–35 minutes depending on payload |
| Wind tolerance | Designed for stable operation in elevated winds (vs. commercial multirotors) |
| Payload interfaces | Quick-change mounts for RGB/zoom, thermal IR, small LiDAR, specialty sensors |
| Operational concept | Precision hover, automated inspection paths, repeatable local surveys |

**Typical Payloads & Measurements:**
- High-resolution RGB, thermal cameras
- Soil moisture sensors (L-band radiometers)
- Small LiDAR (dense point clouds for 3D mapping)
- Air quality sensors
- Surface condition instruments

**How Proposed to be Used:**
- Facility inspection (weather infrastructure, coastal facilities)
- Localized mapping and 3D surveying
- Station-keeping measurements at specific