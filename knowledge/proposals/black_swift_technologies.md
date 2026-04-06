# Black Swift Technologies — Company Overview & ONR LRUAV Alignment Document

## Document Metadata
- **Type:** Company overview with capability alignment analysis
- **Client/Agency:** Office of Naval Research (ONR)
- **Program/Solicitation:** ONR LRUAV (Long-Range Unmanned Aerial Vehicle) opportunity
- **Date:** August 3, 2025 (document creation/modification)
- **BST Products/Systems Referenced:** S2 Research Platform, SØ VTOL, SwiftCore™ FMS, SwiftPilot™, SwiftTab™, SwiftStation™
- **Key Personnel:** Beck Cotter (last editor); Ed Dumas (NOAA/ATDD testimonial); Daniel Hesselius (CU Boulder Flight Operations Director)

---

## Executive Summary
Black Swift Technologies designs and manufactures purpose-built unmanned aircraft systems for scientific research in extreme atmospheric environments. This document establishes BST's company background, core capabilities, and detailed alignment with ONR's LRUAV requirements, demonstrating field-proven modularity, autonomy, rapid deployment, and integration with government agencies (NASA, NOAA).

---

## Technical Approach

### Core Philosophy
- **Integrated End-to-End Design:** BST designs complete UAS systems in-house (airframe, avionics, control systems, UI), rather than integrating off-the-shelf components.
- **Sensor-Driven Architecture:** Platform design begins with sensor integration and is optimized for precise scientific data collection.
- **Autonomous Flight Management:** Proprietary SwiftCore™ FMS enables autonomous flight paths adjusted in real-time based on sensor input, enhancing data quality and reducing operator workload.
- **Modular Payload Integration:** Standard 5V/12V power, common data/mechanical interfaces enable tool-free field swapping and rapid reconfiguration without specialized equipment.

### SwiftCore™ Flight Management System Architecture
**SwiftPilot™ (autopilot core):**
- 9-DOF IMU, dual pressure sensors (differential barometry)
- 10 Hz GPS, 1 kHz altitude sampling rate
- Compact form factor: 6.7 × 4.0 × 1.8 cm, 50 g
- Multiple interface options: CAN, UART, I2C, SPI, USB, Ethernet, GPIO
- 1 GHz Cortex A8 processor (Gumstix Overo)
- Embedded machine learning for inflight failure detection and prognostics
- Enables fault detection, anomaly management, and predictive maintenance

**SwiftTab™ (mission control interface):**
- Android-based touchscreen with gesture-based multi-touch control
- Intuitive mission planning and execution
- Real-time telemetry display
- Minimal operator training required

**SwiftStation™ (ground station):**
- Tripod-mounted, compact (15 × 30 × 35 cm, 0.9 kg)
- Modular radio options (900 MHz) with GPS antenna
- Integrates with autopilot for fully autonomous launch-to-landing missions
- Supports multi-mission interoperability

### Operational Autonomy Features
- Fully autonomous launch, flight, and landing
- Sensor-based flight control: autopilot autonomously navigates based on real-time sensor input to optimize sampling
- Real-time telemetry and high-accuracy tracking
- Predictive maintenance: regression and classification-based diagnostics for subsystem and component failure anticipation
- Supports BVLOS (beyond visual line of sight) operations and flights over people (with FAA approval pathway)

---

## Products & Capabilities Described

### **Black Swift S2™ Research Platform**

**Design & Purpose:**
- Fixed-wing UAS engineered for high-payload, high-endurance atmospheric and environmental research missions
- Purpose-built for harsh volcanic environments (strong winds, particulate-laden air, turbulence)
- Modular, field-swappable payload interface with standard power, data, and maintenance access
- Tool-free payload swapping in laboratory or field environments
- Supports rapid redeployment with different sensor suites using the same airframe

**Performance Specifications:**
| Parameter | Value |
|-----------|-------|
| **Ingress Protection** | IP42 |
| **Payload Capacity** | Up to 2.3 kg (5 lbs) hand-launch / 1.4 kg (3 lbs) rail-launch |
| **Flight Ceiling** | 6,000 m (20,000 ft) |
| **Maximum Wind** | 15 m/s (30 knots) |
| **Stall Speed** | 12 m/s (24 knots) |
| **Cruise Speed** | 18 m/s (35 knots) |
| **Endurance** | 110 min max / 90 min nominal |
| **Max/Nominal Range** | 110/92 km (60/50 nm) |
| **Max GTOW** | 9.5 kg (20.8 lbs) |
| **Wingspan** | 3.0 m (10.0 ft) |
| **Sensor Bay** | 20.3 cm dia × 63.2 cm length |
| **Payload Power** | 50 W total |
| **Geotag Accuracy** | <4 m all directions |
| **Telemetry Data Rate** | 9500 bps serial |
| **Launch Methods** | Hand-launch or rail-launchable |

**Payload Integration:**
- Rugged, field-swappable modular nose cone with contamination-free design
- Standard electrical interface: 5V & 12V power, common data/mechanical interface
- Common payloads supported:
  - **Soil Moisture Mapping:** L-band radiometer
  - **Wildfire Monitoring:** CO2, CO, aerosol, RH, P, T, trace gas sensors, multispectral camera
  - **Multi-Angular Remote Sensing:** 531 nm band monitor, Tetracam mini-MCA, multispectral camera
  - **Volcano Monitoring:** CO2, nephelometer, T, P, H, and wind sensors

**CO2/H2O Payload (LI-840 sensor):**
- **H2O Range:** 0–60 mmol mol⁻¹, <1.5% accuracy, drift <0.003 mmol mol⁻¹/°C
- **CO2 Range:** 0–20,000 ppm, <1.5% accuracy, drift <0.15 ppm/°C (zero), LOD: 1.5 ppm
- Designed for close-to-surface atmospheric measurement above forest canopy and at/near vent/fumarole height
- Supports rapid field recalibration at altitude

**Field Deployment:**
- Entire system fits in carry-on baggage
- Setup time: <5 min
- Fully autonomous operations with SwiftTab™ interface
- Minimal operator training required

---

### **Black Swift SØ™ VTOL UAS**

**Design & Purpose:**
- Lightweight, all-electric, fully portable VTOL system for rapid atmospheric profiling
- Designed for remote, minimal-infrastructure operation in arctic, alpine, and harsh weather environments
- Hand-off/hand-catch launch and recovery

**Performance Specifications:**
| Parameter | Value |
|-----------|-------|
| **Vehicle Type** | VTOL, fully electric |
| **Ingress Protection** | IP54 |
| **Launch/Land Mode** | Hand-off/hand-catch VTOL |
| **Endurance** | 30–40 min |
| **Max Altitude** | 5,000 m (16,404 ft) AMSL |
| **Payload Capacity** | 200 g (7 oz) with negligible performance impact |
| **Max Takeoff Weight** | 1.4 kg (3.1 lbs) |
| **Max Sustained Wind** | 10 m/s (20 knots) |
| **Max Flight Speed** | 13 m/s (25 knots) |
| **Telemetry Link** | 900 MHz, up to 115 kbps |
| **GNSS Geotagging** | <2 m accuracy |
| **Operating Temperature** | -15 to +45 °C |
| **All-Weather Capability** | Light rain, snow, fog |

**Payload Integration:**
- Modular nose cone accepts default or user-provided sensors (trace gas, particulate, miniature camera)
- Payload power: 5V, 12V, up to 10 W
- Rapid field swap and sensor calibration capability

**Field Deployment:**
- Entire system fits in carry-on case
- Setup in <5 min
- Fully autonomous launch, flight, landing
- SwiftTab™ mission interface (Android, gesture-based)
- Minimal operator training required

---

## Use Cases & Applications

### Primary Mission Areas
1. **Volcanic Monitoring:**
   - Gas sampling (CO2, H2O) from active vents and fumaroles
   - Environmental monitoring in harsh, particulate-laden conditions
   - Proven use by NASA and NOAA

2. **Wildfire Assessment:**
   - CO2, CO, aerosol, trace gas, and environmental measurement
   - Multispectral camera-based fire monitoring
   - High-altitude, long-endurance operations

3. **Severe Weather Research:**
   - Tornado and hurricane field campaigns
   - Atmospheric profiling in extreme wind and turbulence
   - Proven partnerships with NOAA/ATDD

4. **Arctic & Polar Operations:**
   - High-altitude operations at extreme latitudes
   - Permafrost and cryospheric research
   - Rugged performance in ice, wind, and cold

5. **Environmental & Atmospheric Research:**
   - Soil moisture mapping via radiometer
   - Multi-angular remote sensing campaigns
   - High-altitude atmospheric studies (20,000 ft ceiling)

6. **Industrial & Inspection Missions:**
   - Precision agronomy
   - Industrial inspections
   - Remote environmental assessments

### Key Mission Partners
- NASA (planetary aerial vehicles, Venus atmospheric exploration, arctic research)
- NOAA (volcanic, arctic, permafrost campaigns)
- University of Colorado (atmospheric science, flight operations)
- UTSI (University of Tennessee Space Institute)

---

## Notable Details

### Awards & Recognition
- **AUVSI XCELLENCE Award (2022):** Humanitarian and Public Safety category
- **SBIR Contracts:** Awarded for advanced vehicle innovations, including planetary aerial vehicles
- **NASA Innovation Recognition:** Funded work on Venus atmospheric exploration concepts

### Competitive Differentiators
1. **Integrated System Design:** In-house design of airframe, avionics, control systems, and UI (not OEM/COTS integration)
2. **Modular Open Architecture:** Standard payload interfaces with no specialized tools required for field reconfiguration
3. **Autonomous Capability:** SwiftCore™ FMS enables routine autonomous operations with minimal training
4. **Field Proven:** Documented use by NASA, NOAA, and academic institutions in demanding research environments
5. **Sensor-Optimized Design:** Platforms engineered around payload requirements, not adapted to existing platforms
6. **Rapid Deployment:** <5 min setup, carry-on portability, fully autonomous flight planning via SwiftTab™

### ONR LRUAV Alignment Analysis
The document includes a comprehensive alignment table mapping ONR LRUAV requirements to BST capabilities:

| ONR Requirement | BST Capability | Evidence |
|-----------------|----------------|----------|
| Distributed, persistent, modular ISR | Modular field-swappable payloads, rapid reconfiguration | S2 tool-free payload swap, standard 5V/12V power interface |
| Open architecture, standard interfaces | Standard payload/data interfaces, no tools required | Common mechanical/electrical interface specification |
| ISR in harsh maritime/adverse environments | Proven volcanic, arctic, remote, high-wind operations | 30 kt max wind, IP42 protection, field-proven by NASA/NOAA |
| Rapid field deployment | <5 min setup, carry-on portable, autonomous ops | Fully autonomous launch/flight/landing, SwiftTab™ interface |
| End-to-end avionics/autonomy | SwiftCore™ FMS with real-time telemetry, GCS integration | SwiftPilot™ + SwiftStation™ + SwiftTab™ integrated system |
|