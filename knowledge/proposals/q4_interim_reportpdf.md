# S/0 UAS: An Air Deployed Solution for Boundary Layer Observations in Turbulent Environments - Phase II Interim Report

## Document Metadata
- **Type:** Phase II Interim Report (NOAA SBIR)
- **Client/Agency:** National Oceanic and Atmospheric Administration (NOAA)
- **Program/Solicitation:** NOAA SBIR Phase II
- **Contract Number:** 1305M219CNRMW0030 (also referenced as 1305M218CNRMW0059)
- **Date:** December 23, 2020
- **BST Products/Systems Referenced:** S/0 UAS, SwiftCore firmware/autopilot, MultiScat (multi-hole probe), AVAPS integration, SwiftTab UI
- **Key Personnel:** Jack Elston (PI), Dr. Maciej Stachura, Mr. Fromm

## Executive Summary
This interim report documents Black Swift Technologies' Phase II SBIR work to develop the S/0, a low-cost, air-deployed UAS designed for boundary layer observations in tropical cyclones and severe weather. The report covers technical progress through Q4 2020, including antenna design refinement, firmware development, wind sensor testing, deployment tube design, and automated guidance algorithm advancement. As of the report date, approximately 75% of the work was completed with cumulative costs of $315,662.46.

## Technical Approach

### Core Design Philosophy
The S/0 is purpose-built for air deployment from manned aircraft (specifically NOAA's P-3), designed to reduce complexity and weight compared to existing platforms (Aerosonde, Coyote) while maintaining performance. Key design principles:
- Single swiveling wing architecture to minimize moving parts and manufacturing complexity
- Lightweight, compact design based on proprietary avionics and sensing suite
- Heritage from radio dropsonde operations to maintain current CONOPS
- Target unit cost near $5,000 to enable expanded observations and formation flying

### Key Technical Subsystems

**Avionics & Autopilot:**
- Custom SwiftCore autopilot based on new STM32 microprocessor
- Distributed implementation consolidated to single processor for S/0's complexity
- USB bootloader for firmware updates and data retrieval
- CAN bus implementation for future expansion
- Integration with NCAR/Vaisala AVAPS system for wireless data transmission

**Sensing Package:**
- **Wind Measurement:** 5-hole multi-hole probe (MHP) integrated directly into fuselage nose for accurate 3D wind measurement
- **Thermodynamic Sensors:** Temperature, humidity, pressure, sea surface temperature
- **Altitude/Oceanographic:** Laser altimeter, thermal IR sensor for sea surface observations
- **Attitude/Orientation:** IMU with high-frequency sampling synchronized with wind probe data

**Propulsion:**
- Battery: 3S3P Sanyo 18650GA cells (primary candidate); Sony Murata VTC6 cells as secondary option for dash power
- Motor: T-Motor F60 Pro (~600W class) in 2000-2500 Kv range
- Propeller: Custom forward-folding pusher propeller with adapter for storage in deployment tube
- Electronic Speed Controller: Lumenier 35A (upgraded from initial selection due to thermal issues)
- Target Endurance: 1-2 hours cruise flight

**Antenna Design:**
Multiple configurations tested and evaluated:
- Spring dipole (deployable) - final selected design, based on NCAR dropwindsonde heritage
- Straight, folded, Z-shaped, and U-shaped dipoles evaluated as alternatives
- Operating frequency range: 400-410 MHz (AVAPS radio system)
- Voltage Standing Wave Ratio (VSWR) testing confirmed spring dipole performance maintained after coiling/deployment cycles
- Materials: Spring steel blade elements, FR4 substrate, MMCX connectors

**Air Deployment System:**
- Deployment tube: ~4.875" OD, 4.785" ID, 36" length, ~18-22 lbs
- LE Linen Phenolic construction for dimensional stability
- Compatible with existing free-fall chute (heritage from AXBT deployments)
- Parachute sizing and ballast configuration still under development
- Aircraft release mechanism under design

## Products & Capabilities Described

### S/0 UAS
**What it is:** A compact, air-deployed fixed-wing UAS specifically designed for boundary layer sampling in severe weather and tropical cyclones.

**Proposed use:** Rapid deployment from NOAA P-3 aircraft into hurricane eyewalls and boundary layers to provide 3D wind, temperature, humidity, pressure, and sea surface measurements. Designed to replace or supplement expensive single-use platforms.

**Specifications:**
- **Dimensions:** Compact enough to fit in ~36" x 4.875" OD deployment tube
- **Endurance:** 1-2 hours cruise flight
- **Sensors:** 3D wind (MHP), temperature, humidity, pressure, SST, laser altimeter, thermal IR
- **Communication:** AVAPS wireless system (one-way data link from S/0 to P-3)
- **Guidance:** Autonomous flight with onboard decision-making based on atmospheric data
- **Target Cost:** ~$5,000 per unit (order of magnitude reduction vs. existing platforms)

### SwiftCore Autopilot/Firmware
Custom flight management system being upgraded for S/0's integration requirements. Handles real-time sensor fusion, wind calculations, navigation, and deployment detection.

### Multi-Hole Probe (MHP)
5-hole probe integrated into S/0 fuselage nose. Validated in kite-based testing for accurate 3D wind measurement in highly turbulent atmospheres. Real-time algorithms compute:
- Angle of attack (α) and angle of sideslip (β)
- Indicated airspeed (IAS) → True airspeed (TAS) conversion
- Attitude computation from IMU/GPS
- Airspeed vector rotation to inertial frame
- 3D inertial wind computation with sensor lag compensation via Kalman filtering

Testing showed good agreement with IMU measurements and demonstrated accurate post-processing validation.

## Use Cases & Applications

**Primary Mission:** Boundary layer observations in tropical cyclones
- Enhanced eyewall penetration sampling
- Lower boundary layer kinematics and thermodynamics
- Sea surface temperature and height measurements
- Improved tropical cyclone intensity forecasting through increased sampling density

**Secondary Potential Uses:**
- Severe convective storm sampling
- Formation flight operations for instantaneous atmospheric gradient measurement
- Descending transects within storm structures
- Extended spatial and temporal sampling per storm event

**Geographic Focus:** Tropical and subtropical environments; initial validation testing planned for Florida

## Key Results (Current Status)

### Completed/In-Progress Technical Activities

**Antenna Development (75% program completion milestone):**
- Tested four alternative dipole configurations plus spring dipole design
- Roll-cut radiation pattern measurements at 400-410 MHz frequency range
- Validated spring dipole performance after deployment cycle testing
- Confirmed VSWR performance maintained after coiling (critical for deployment reliability)
- Selected spring dipole as final design with construction specifications

**Firmware Development:**
- STM32 hardware abstraction layer (HAL) drivers implemented
- All sensor interfaces integrated and verified (IMU, pressure, magnetometer, GPS, laser, SD card)
- Servo control (S.Bus) and PWM outputs validated
- USB bootloader completed for field firmware updates
- User interface completed (power switch, charging port, status LED)
- Remaining: autopilot stack integration, AVAPS/Vaisala interface completion, battery management

**Wind Sensor (MHP) Validation:**
- First kite-based flight test conducted in highly turbulent atmosphere
- Real-time wind algorithm development completed (5-step process from probe pressures to inertial winds)
- Sensor lag compensation and Kalman filtering implemented
- 1 Hz wind vector trajectory data successfully processed from 100 Hz measurements
- Temperature and humidity data validated during flight

**Propulsion System:**
- Motor/propeller combination testing ongoing; T-Motor F60 Pro selected
- Identified ESC thermal issues; upgraded to Lumenier 35A controller
- Custom forward-folding propeller adapter designed for deployment tube storage
- Battery pack options validated (Sanyo 18650GA primary, Sony Murata VTC6 alternative)

**Deployment System:**
- Deployment tube design finalized (phenolic construction, AXBT-heritage sizing)
- Mass model preparation underway
- Parachute timing and aircraft release mechanism concepts under development
- Preliminary design review planned with all stakeholders

**Autonomous Guidance:**
- NetCDF weather model import integrated into JSBSim simulation environment
- Hurricane model data pipeline established for atmospheric property injection (temperature, density, wind)
- Setup for 1000+ Monte Carlo simulations to validate 99% eyewall intercept success rate
- Pressure-based eyewall tracking algorithm development in progress

### Resource Status
- **Cumulative costs (as of Dec 23, 2020):** $315,662.46
- **Work completion estimate:** 75%

### Current Problems/Risks
- Flight testing may extend beyond original final report date due to P-3 availability and pandemic travel restrictions
- ESC supply chain concerns at higher production volumes (workaround: multiple suppliers identified)
- Battery management board complexity still under development

## Notable Details

**Partnerships & Collaboration:**
- Positive working relationship established with NCAR and Vaisala (AVAPS protocol support)
- Successful wireless data transmission over AVAPS system during Phase I
- Plans for close coordination on post-processing software for interleaved sensor data
- Integration planned with actual AVAPS ground station at NCAR facility
- Support from Northwind Composites for wing mold design and composite manufacturing
- Local PCB board shop for custom electronics manufacturing

**Unique BST Capabilities Leveraged:**
- Proprietary certified autopilot and ground station
- Full thermodynamic and kinematic sensing suite
- Experience building and operating severe convective storm platforms (Tempest, Coyote heritage)
- Strong background in UAS wind observation methodology
- In-house 3D printing capabilities for rapid iteration on aircraft internals and deployment mechanisms

**Commercialization Path:**
- Detailed build procedures and QC processes being developed for production readiness
- Custom UI development for ruggedized Android tablet (minimal version of SwiftTab)
- Online documentation planned for BST support website
- Design prioritizes manufacturability and cost reduction for potential expanded NOAA/commercial use

**Test Plan Remaining:**
- Severe weather testing in Colorado (high winds >60 mph, heavy precipitation)
- Indoor deployment tube release tests (nets, then tethered balloon)
- Tethered balloon system tests at BST sod farm (up to 400')
- Full P-3 air deployment flights from Florida (primary Phase II milestone)
- Complete system validation including airframe, sensors, avionics, and communication

**Design Innovations:**
- Single swiveling wing reduces complexity vs. Aerosonde/Coyote multi-surface designs
- Purpose-built avionics integration eliminates third-party autopilot/air probe integration overhead
- Deployment tube design mimics operational CONOPS of existing radio dropsondes, reducing operator workload
- Formation flight capability enabled by low unit cost and autonomous guidance
- Sensor lag compensation via Kalman filtering provides accurate wind estimates even with asynchronous measurements