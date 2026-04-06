# Airborne in situ Sampling of Volcanic Emissions: Progress and Plans

## Document Metadata
- **Type:** Technical presentation/report
- **Authors:** David Pieri (Jet Propulsion Laboratory, NASA) and Jorge Andres Diaz (CICANUM GasLab, Universidad de Costa Rica)
- **Date:** October 29, 2014 (presentation date); references work from March 2013 and ongoing through 2015
- **Related Program:** NASA SBIR Program (mentioned for related UAV development)
- **Key Collaborators:** Simon Carn (Michigan Tech), Fred Prata (NILU), multiple NASA centers (ARC, GSFC/Wallops, GRC), University of Costa Rica
- **Study Sites:** Turrialba Volcano (Costa Rica), Arenal Volcano (Costa Rica), Sakurajima/Kagoshima (Japan), Mt. Etna (Italy), various others

## Executive Summary
This presentation documents JPL/NASA efforts to develop unmanned aircraft systems (UAV) and related instrumentation for in situ sampling and measurement of volcanic ash and gas emissions. The work addresses both aviation safety hazards from volcanic ash and scientific understanding of volcanic plume composition and transport. The document describes two main operational regimes: low-altitude passive persistent emissions (accessible to small UAVs) and high-altitude explosive eruption clouds (requiring larger platforms or high-altitude capabilities).

## Technical Approach

### Problem Framing
**Proximal Hazards:**
- Airborne ash on instrument landing system (ILS) approaches at airports near volcanoes (Kagoshima, SFO, Portland, Clark AFB Philippines, Manila)
- Ash fallout on airport surfaces
- Mid-air collisions with eruption macro-products (clasts)

**Distal Hazards (Prompt: >2000μg/m³):**
- Compressor stall failure and engine flameouts
- Abrasion of windscreens, internal engine parts, leading edges
- Carbon deposition on fuel injectors
- Ungrounded static charges (St. Elmo's Fire)
- Example: December 15, 1989 Redoubt Volcano encounter with Boeing 747-400 resulted in 4-engine flameout; windscreen scoured to 98% opacity

**Distal Hazards (Latent: <2000μg/m³):**
- Blade cooling problems
- Bleed air passages clogged, causing thermal stresses outside design envelope
- Electronics over-insulation and heating damage
- Example: NASA DC-8 encounter with Hekla eruption (February 2000) caused $3.5M minimum economic damage through "silent damage"—shortened maintenance life via erosion of leading edges, plugged cooling holes, blistered thermal coating, ash buildup in passages

### Pre-2010 Response
- ICAO "zero tolerance—zero risk" approach
- Volcanic Ash Advisory Centers (VAACs) operated by national weather services to assimilate eruption data and predict trajectories
- Strategy: avoid all ash-contaminated airspace
- Result: limited academic interest in actual solid aerosol and gas concentrations within contaminated airspace

### Post-2010 Paradigm Shift
- **Game changer:** Eyjafjallajokull 2010 eruption demonstrated impracticality of global "zero tolerance" approach
- New approach: more "risk-tolerant," requiring increased accuracy/precision of ash concentration retrievals, mass loadings, and trajectory predictions
- Manufacturers need to understand effects of turbine ash ingestion
- Challenge: need to fly into contaminated airspace to obtain concentration data
  - Manned aircraft can only probe periphery and dilute plume sections
  - Unmanned platforms required for thickest plume areas (recommended by Germany, UK, US)

### Solutions Described

**1. Understanding Turbine Tolerance Limits**
- Key finding (Grindle and Burcham 2002): blade with blocked cooling operates at sufficiently higher temperature that its life may be as little as 150 hours

**2. In Situ Measurements of Ash and Gas Environment**
- Provide operational data to airlines and manufacturers
- Improve calibration and validation of remote sensing retrievals and models
- Approach: heavily instrumented manned aircraft for dilute plumes + small, capable robotic (UAV) platforms
- Recognition: "No dedicated platforms/micro-instruments exist operationally today, specifically for volcanic plumes"
- Assessment: "Electric UAVs are perhaps the most promising"

## Products & Capabilities Described

### UAV Platforms

**Dragon Eye (µUAV, NASA ARC/JPL, built by AeroVironment)**
- 5-piece modular airframe (Kevlar, fiberglass, carbon fiber, foam composite); no-tool field assembly
- Inventory: ~90 aircraft (95 planned)
- Fits into 15" × 15" × 7" backpack
- Twin brushless DC electric motors
- NiMH rechargeable & LiSO₂ primary batteries
- **Payload capacity:** ~0.5 kg total (250g SO₂ sensor, <250g OPC, camera, electronics)
- **Endurance:** 45-60 minutes
- **Range:** 6 km
- **Specifications:** Wingspan 3.75 ft (1.14 m), empty weight 5 lb (2.25 kg)
- **Ceiling:** daylight limited (no altitude specification given)
- **Sensors:** TIR imager, daylight, lowlight, SO₂ sensor, ash sampler, nephelometer, T/P/%H₂O sensors, optional CO₂ sensor
- **Autonomy:** autonomous capable autopilot with GPS navigator
- **Development:** Built for DoD 2001-2003; now no ITAR restrictions
- **Key capability:** Deployed March 2013 to Turrialba; intercepted SO₂ plume with 6-8 ppmv concentration

**NASA SIERRA (Medium UAV, NASA ARC)**
- ~100 lb payload capacity
- 500 km range
- 6-8 hours endurance
- ~12-15 kft ceiling
- Satcomm link; direct download capability
- Proposed deployment with ICAMS (In situ Compact Airborne Mass Spectrometer) payload

**Viking 400C Tigershark (Small UAV)**
- Comparable to SIERRA
- Under discussion for deployment to Turrialba and/or Salton Sea, CA
- Proposed payload: ICAMS/ULISSES mini-mass spectrometer + other sensors

**University of Costa Rica (UCR) Vector Wing 100 UAV**
- Maryland Aerospace aircraft, highly modified
- Modified motor: 1800W (vs. original 400W)
- **Ceiling:** flights to 13 kft ASL with 1 kg payloads
- Real-time telemetry link for video and data + in-flight GPS geolocation
- Variety of gas and particle micro-sensors built at UCR
- Collaboration with JPL & NASA ARC (Prof. Andres Diaz, UCR School of Physics)
- **Performance at Turrialba:** reached 11,258-11,500 ft ASL with SO₂ measurements up to 12.4 ppmv

**UCR VANTAR (Small UAV, New)**
- Deployed March 2014 and planned for March 2015
- Capability to carry multiple mini-sensors

**NASA ARC "Swift" Electric Sailplane UAV (Under Development)**
- **Operating ceiling:** 30-40 kft ASL
- **Payload:** 220 lbs possible
- **Wingspan:** 41 ft
- **Lift/drag ratio:** ~25:1+
- **Design:** Stanford University
- **Purpose:** Potential to sample high-altitude volcanic plumes

**Other Platforms Discussed**

**Steerable Dropsonde (Latitude Engineering, Tucson, AZ)**
- SBIR Phase II under active development
- Features: ash sampler, camera, electrochemical sensors
- Drop from balloon or aircraft at standoff distance or above ash
- Recoverable
- Up to 10:1 glide ratio possible
- Prototype flight-tested

**Lighter-Than-Air Platforms (Aerostats)**
- Tethered balloons (JPL-UCR, deployed Feb-March 2013 at Turrialba)
- Kites (where helium unavailable, e.g., delta kites, "Into the Wind" 9 ft delta over Chesapeake Bay)
- Helikites (where helium available)
- **Turrialba balloon flight Feb 2013:** max altitude 3,475 m (11,300 ft ASL), max SO₂ ~5 ppmv
- **Turrialba balloon flight Feb 2012:** max altitude 3,464 m (11,258 ft ASL), max SO₂ ~10.5 ppmv

### Instrumentation/Sensors

**SO₂ Measurement:**
- Compact SO₂ sensor package (<250g) with SO₂-temperature-pressure-humidity suite (NASA GSFC/WFF)
- SO₂ sample capture bottle (1 deciliter)
- Electrochemical SO₂ sensors
- DOAS (Differential Optical Absorption Spectroscopy) for near-field remote sensing
- COSPEC for near-field remote sensing
- FTIR for near-field remote sensing

**Aerosol/Particle Measurement:**
- Basic Optical Particle Counter (OPC) (<250g)
- IDI Twin Laser Nephelometer (SBIR-funded)
  - Balloon-borne test: measured 10 μm diameter liquid aerosols in stratus clouds
  - New installation in Dragon Eye nose
  - Can detect solid aerosols, liquid aerosols, and distinguish ice particulates
- Nano-particle (≤20 nm) collectors

**Gas Measurement:**
- Compact Sulfur Dioxide sensor packages
- Miniature CO₂ sensor (Makel Engineering LLC; SBIR collaboration with NASA GRC, Cleveland, OH)
- OEM CO₂ sensors
- Electrochemical multi-gas sensor suites

**Mass Spectrometry:**
- In situ Compact Airborne Mass Spectrometer (ICAMS)
  - Proposed for SIERRA and Viking 400C deployment
  - 40 kg payload capacity planned for Salton Sea deployment

**Other Sensors:**
- Thermal infrared (TIR) cameras
- Visible light cameras (normal and low-light)
- GoPro cameras
- Met instruments (temperature, pressure, humidity)
- Autonomous capable autopilots with GPS navigation

### Computational Support
- Computational Fluid Dynamics (CFD) windfield solutions at ~100 m scale for sUAV operations (NASA ARC, Corey Ippolito)

## Use Cases & Applications

### Volcanological Regimes Addressed

**Regime 1: Passive Persistent Low-Altitude Emissions (<10-15 kft ASL)**
- Examples: Turrialba, Arenal (Costa Rica)
- Characteristics: 
  - Accessible natural labs for simultaneous orbital/airborne/ground truth campaigns
  - Distances typically few tens of km from vent
  - Detecting changes in steady state beneficial for mitigating proximal and distal hazards
- Operational requirements:
  - Day/night, all-weather capabilities over hazardous terrain
  - Airspace accessibility under local civil aviation authorities critical limiting factor
  - Aerostats useful where helium available (balloons, helikites) or pure kites without helium
  - Near-field remote sensing (COSPEC, DOAS, FTIR) helpful
- Scientific application: Low-altitude ash and gas plumes rarely factor in aviation unless volcano near airfield (e.g., Kagoshima/Sakurajima, Catania/Mt. Etna)

**Regime 2: Syn- and Post-Eruptive High-Altitude Cloud Monitoring**
- Characteristics:
  - Explosive eruption emissions 100-1000 km lengths, continental spatial scales
  - Up to 150 kft ASL
  - Poorly accessible by ground remote sensing
- Approach:
  - Orbital or high-altitude airborne remote sensing (multi/hyperspectral, LIDAR) for initial detection/monitoring
  - Manned aircraft sampling in low-risk dilute plumes within operational limits
  - Electric UAV penetration, sampling, measurement within high-risk high-concentration zones