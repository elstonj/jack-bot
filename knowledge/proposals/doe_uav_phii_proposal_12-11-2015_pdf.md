# A Highly Miniaturized Cloud and Aerosol Instrument Package for Small UAV's

## Document Metadata
- Type: SBIR Phase II Proposal
- Client/Agency: U.S. Department of Energy (DOE)
- Program/Solicitation: DOE SBIR Topic 19 (Atmospheric Measurement Technology), Subtopic a (Aerosol and Hydrometer Size Distributions from UAV Platforms)
- Date: December 11, 2015
- Company: SPEC Inc.
- BST Products/Systems Referenced: None directly; document is from SPEC Inc., not Black Swift Technologies
- Key Personnel: Dr. R. Paul Lawson (PI), Dr. Chris Roden, Nick Krause, Dr. Colin Gurganus, Dr. Sarah Woods, Qixu Mo, Dr. Sebastian Schmidt (subcontractor, University of Colorado)

## Executive Summary
SPEC Inc. proposes to design, fabricate, and flight-test a miniaturized cloud and aerosol instrument package (micro-COPP) for small electric UAVs, combining optical particle imaging with aerosol sensors weighing 7 kg total and consuming 70 W. Phase I successfully demonstrated feasibility through laboratory and field tests; Phase II will integrate the package into a Vanilla Aircraft VA-002 UAV and conduct a three-week pilot field deployment in the Arctic (Oliktok Point, Alaska or Ny-Ålesund, Svalbard) to characterize mixed-phase clouds critical to understanding Arctic climate change.

## Technical Approach

### Micro-COPP Design
The miniaturized Combination Optical Particle Probe integrates three optical systems into a 3 kg package:
- **Fast Cloud Droplet Probe (FCDP)**: Forward scattering probe measuring particles 1–50 µm
- **Optical Array Probe (OAP)**: 128-photodiode array with 25 µm pixel resolution, images particles up to 3.2 mm
- **Cloud Particle Imager (CPI)**: Digital camera with 256 gray levels and 2 µm pixel resolution (submicron version: 0.7 µm resolution using Mitutoyo microscope objective)

The design uses:
- Carbon fiber and rapid-prototype components replacing heavy aluminum
- FPGAs and system-on-module/system-on-chip electronics
- Integrated optical paths where FCDP and OAP trigger the pulsed CPI laser
- Three laser beams intersecting in sample volume for simultaneous measurement

### Integration into UAV Instrument Package
Complete 7 kg package includes:
- Micro-COPP (3 kg)
- Miniaturized CCN counter (Cloud Condensation Nuclei, Dr. Greg Roberts design)
- Haltech CW-HPC300 optical particle counter (0.3–25 µm aerosols)
- Ice nuclei (IN) filter system with electrostatically-deposited samples
- Meteorological package: pressure, temperature, humidity, heading, GPS
- UAV telemetry: airspeed, altitude, pitch, roll, yaw, vertical acceleration, heading

**Total power consumption**: 70 W. **VA-002 performance with 7 kg load**: 10,000 ft MSL ceiling, 2-hour duration.

### Field Deployment Strategy
- **TBS (Tethered Balloon System)**: Vertical profiles from surface to 7,000 ft MSL with 15 kg payload including cryogenic frost-point hygrometer and new six-channel 4-π radiometer (measuring actinic flux at 440, 670, 940, 1020, 1240, 1640 nm)
- **VA-002 UAV**: Horizontal ascending/descending slants around balloon to create 3D microphysical volume
- **Operating envelope**: 10-minute dips into supercooled clouds; flights between/below/above cloud layers when possible
- **Location**: Oliktok Point, Alaska or Ny-Ålesund, Svalbard; 3-week pilot program

## Products & Capabilities Described

### Micro-COPP
**What it is**: Integrated optical cloud particle probe combining forward scattering, array imaging, and high-resolution digital imaging in a lightweight package.

**Technical specifications**:
- FCDP: 1–50 µm particles
- OAP: 25 µm resolution, up to 3.2 mm particles fully imaged
- CPI: 2 µm pixel resolution (standard), 0.7 µm submicron version
- Weight: 3 kg
- Power: <30 W

**Performance achievements**:
- Phase I laboratory tests confirmed optical integration and functionality
- October 2015 field test on SPEC TBS at Ft. Carson demonstrated successful operation in mixed-phase clouds
- Successfully imaged supercooled water drops and ice particles
- Submicron CPI version tested and confirmed ability to resolve 0.78 µm line pairs (1951 USAF test reticle)

**Capabilities**:
- Distinguishes particle phase (water vs. ice) through high-resolution imaging
- Identifies ice crystal habit and surface roughness
- Provides particle size distributions across three size ranges
- Suitable for both TBS and small UAV platforms

### SPEC Tethered Balloon System (TBS)
**What it is**: Proven unmanned tethered platform capable of extended vertical profiling in remote regions.

**Applications in proposal**:
- Extended observation periods (>24 hours)
- Vertical profiles from surface to 2 km altitude (covers full Arctic boundary layer)
- Carries larger (15 kg) payload including radiometer
- Slow aspiration speed (~10 m/s) minimizes ice crystal shattering artifact

**Prior deployments cited**:
- Ny-Ålesund, Svalbard (May 2008): Mixed-phase cloud microphysics and radiative properties
- South Pole (January–February 2009): Aerosol and supercooled liquid water measurements at temperatures to -32°C

### Vanilla Aircraft VA-002 UAV
**What it is**: Electric, runway-independent unmanned aircraft developed under NASA SBIR.

**Specifications**:
- Largest payload capacity of electric runway-independent UAS
- Bungee-launched, belly-landed
- Man-portable, modular construction (carbon-composite fuselage, EPP foam)
- Brushless DC motors, rechargeable lithium-ion batteries
- With 7 kg instrument payload: 10,000 ft MSL ceiling, 2-hour duration
- Generic payload mount in free airstream

**Role in proposal**: Primary platform for micro-COPP deployment; capable of slow flight (20–30 m/s) to minimize particle shattering

### Supporting Sensors
- **CCN Counter (miniaturized)**: Designed/built by Dr. Greg Roberts (Scripps); successfully flight-tested on SPEC TBS at Ft. Carson
- **Haltech CW-HPC300 OPC**: Off-the-shelf particle counter, 0.3–25 µm, USB interface
- **Ice Nuclei Filter System**: Electrostatically deposits aerosols on silicon wafer; deployed South Pole and Ft. Carson
- **4-π Radiometer**: Six-channel actinic flux measurement (440–1640 nm); measures hemispherical irradiance on six faces for platform-independence
- **Cryogenic Frost-Point Hygrometer**: High-precision water vapor measurement on TBS
- **Ground-based Spectrometer**: Supplied by CU LASP; measures zenith radiance and downwelling irradiance for radiative closure

## Use Cases & Applications

### Primary: Arctic Climate Research
- **Mixed-phase cloud characterization**: Study supercooled liquid water and ice particle coexistence in Arctic stratus clouds (cloud tops typically <2 km)
- **Radiative closure**: Combine microphysical and radiative measurements to constrain cloud radiative effects on surface energy budget
- **Climate model validation**: Provide in situ data to improve parameterizations in global climate models for polar regions
- **Ice-albedo feedback**: Understand net warming from mixed-phase clouds and its role in Arctic sea ice melt

### Secondary Applications (Noted in Proposal)
- **Volcanic ash monitoring**: NASA interest in measuring volcanic ash plumes affecting air traffic
- **Methane emissions**: Monitor wellhead emissions from oil operations (e.g., Prudhoe Bay)
- **Urban air quality**: Monitor aerosols and gases in urban environments for EPA compliance
- **Wildfire smoke**: Profile aerosols from forest fires in unsafe airspace
- **Offshore weather**: Improve fog forecasting for helicopter operations to offshore oil rigs
- **Marine stratus breakup**: Better forecasting of marine boundary layer clouds for aviation

## Key Results (Phase I Achievements)

### Task 1: Micro-COPP Design
- Completed Solidworks solid models of integrated micro-COPP
- Zemax optical ray-trace demonstrating feasibility of three-probe integration
- Weight target met: 3 kg vs. 27 kg for earlier Hawkeye probe
- Power requirement: <30 W

### Task 2: Laboratory Tests
- Prototype micro-COPP assembled on optical bench
- Glass beads and water drops projected through sample volume
- Confirmed feasibility of integrated three-probe operation
- FCDP, OAP, and CPI subsystems functionally validated

### Task 3: Submicron CPI Development
- Successfully tested submicron-resolution CPI with Mitutoyo 20 mm working-distance objective
- Confirmed 0.78 µm line-pair resolution (1951 USAF test reticle)
- Demonstrated superior imaging of small ice particles, water droplets, and aerosol particles
- Showed clear diffraction patterns suitable for droplet sizing without holographic reconstruction

### Task 4: UAV Integration Design
- Solidworks models developed showing integration into Vanilla Aircraft VA-002 and Scaneagle UAVs
- Complete power and data flow block diagram created
- UAV instrument package designed: 7 kg total, 70 W power consumption

### Bonus: Field Testing (Beyond Phase I Scope)
- October 29, 2015 deployment on SPEC TBS at Ft. Carson
- Successfully imaged supercooled water drops and ice particles in mixed-phase clouds
- FCDP and OAP size distributions obtained
- CPI particle habit images collected and validated

## Notable Details

### Technical Innovation
- **Miniaturization strategy**: Replaced massive aluminum housing with carbon fiber, FPGAs with SOM/SOC, enabling 3 kg vs. 27 kg for previous generation
- **Submicron imaging**: 0.7 µm pixel resolution enables detection of surface roughness effects on radiative properties, small ice crystal habit identification
- **Integrated optical triggering**: Three probes share sample volume; FCDP and OAP trigger CPI laser, enabling simultaneous measurement across size ranges
- **Depth-of-field exploitation**: Submicron resolution improves retrieval of small droplet sizes from diffraction patterns without computationally-intensive holographic reconstruction

### Partnerships & Subcontracts
- **Vanilla Aircraft LLC**: VA-002 UAV platform, integration support, flight operations
- **Dr. Greg Roberts (Scripps Institute)**: CCN counter design and calibration
- **Dr. Sebastian Schmidt (University of Colorado)**: Radiative transfer modeling and retrievals
- **Prof. Knut Stamnes (Stevens Institute of Technology)**: 4-π radiometer design direction
- **Dr. Heinz Bingemer (Goethe University)**: Ice nuclei filter system development
- **Norwegian Institute of Air Research (NILU)**: 4-π radiometer manufacturing

### Prior Experience
- **SPEC ATTREX Project**: Hawkeye probe operated on NASA Global Hawk at 60,000 ft
- **Arctic TBS deployments**: Ny-Ålesund (2008), South Pole (2009) with proven data quality
- **DOE ERASMUS Program**: Referenced successful 163-flight campaign with small DataHawk UAVs at Oliktok Point (August 2015)

### Climate Significance
Document emphasizes Arctic as region warming at ~2× global average rate:
- September sea ice extent declining 9.4–13.6% per decade
- Models predict ice-free Arctic summers by mid-21st century
- Mixed-phase clouds have net warming effect on Arctic surface energy budget
- Current uncertainty in satellite retrievals of cloud microphysics requires in situ validation

### Operational Advantages of TBS + UAV Approach
- **TBS**: Extended duration, full vertical profiles (surface to 7 km