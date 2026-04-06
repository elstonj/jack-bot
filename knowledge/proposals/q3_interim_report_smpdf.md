# The S/zero.pnum UAS: An Air-Deployed Solution for Boundary Layer Observations in Turbulent Environments – Q3 Interim Report

## Document Metadata
- **Type:** NOAA SBIR Phase II Interim Report
- **Client/Agency:** National Oceanic and Atmospheric Administration (NOAA)
- **Program/Solicitation:** NOAA SBIR Phase II
- **Contract Number:** 1305M219CNRMW0030 (Phase II) / 1305M218CNRMW0059 (referenced)
- **Date:** June 23, 2020
- **BST Products/Systems Referenced:** S0 UAS, SwiftCore Flight Management System, SwiftTab UI, Multi-Hole Probe (MHP), Coyote UAS, Aerosonde UAS, S2 aircraft
- **Key Personnel:** Jack Elston (PI, elstonj@blackswifttech.com), Dr. Stachura, Mr. Fromm
- **Company Address:** 3200 Valmont Rd Ste 7, Boulder, CO 80301

## Executive Summary
Black Swift Technologies is developing the S0, a low-cost, air-deployed unmanned aircraft system (UAS) designed specifically for sampling the lower boundary layer of tropical storms and hurricanes. Building on successful platforms like the Coyote and Aerosonde, the S0 aims to reduce aircraft cost by an order of magnitude (target: ~$5,000 per unit) while maintaining endurance and measurement quality, with the goal of enabling increased frequency of in situ observations for improved tropical cyclone forecasting.

## Technical Approach

**Overall Design Philosophy:**
- Purpose-built system focusing only on boundary layer observation, avoiding ISR and other mission requirements that increase complexity and cost
- Single swiveling wing design to reduce moving parts and manufacturing complexity
- Air-deployed from manned aircraft (P3) via tube and parachute system, mimicking existing radiosonde operational concepts (CONOPS)
- Lightweight construction enabled by BST's proprietary toolset: certified autopilot, ground station, and integrated thermodynamic/kinematic sensors

**Key Design Innovations:**
1. **Consolidated avionics:** BST's SwiftCore autopilot, custom ground station, and sensor suite integrated into compact design, avoiding third-party integrations
2. **Simplified structure:** Single-piece composite wings, 3D-printed tail and components, minimized wiring
3. **Modular sensor approach:** SD card storage and CAN bus for future payload expansion
4. **Integrated wind sensing:** Multi-hole probe (MHP) directly integrated into fuselage nose for 3D wind measurement

**Deployment System:**
- Aircraft housed in protective tube with parachute compartment above
- Plastic flap (instead of drogue chute) deploys main parachute after drop
- Aircraft deploys motor-first, then flips to nose-first descent before achieving level flight via elevator control
- Autopilot capable of full flight regime estimation and control during unconventional deployment sequence

## Products & Capabilities Described

### S0 UAS
**What it is:**
- Low-cost, air-deployed fixed-wing UAS optimized for atmospheric boundary layer sampling in severe weather
- Single swiveling wing design
- Tube diameter constrained fuselage (~cylindrical cross-section for aerodynamic stability during tube deployment)

**Performance specifications/goals:**
- **Endurance:** 1-2 hours cruise flight
- **Cost target:** ~$5,000 per unit (order of magnitude reduction vs. existing platforms)
- **Cruise altitude capability:** Demonstrated ~60 minutes at 5,500' MSL in Phase I; Phase II targeting 90 minutes
- **Wind capability:** Can operate in winds exceeding 60 mph
- **Precipitation tolerance:** Designed to fly during heavy rain
- **Sea surface observation altitude:** Operates at lower altitudes to measure sea surface temperature and height

**Sensing Package:**
1. **3D Wind measurement:** Multi-hole probe (5-hole integrated probe, not external)
   - Measures angle of attack (α), angle of sideslip (β), and dynamic pressure (q)
   - Wind tunnel validation completed: RMS errors (filtered) α = 0.1°, β = 0.25°, vTAS = 0.06 m/s
   - 9th-order polynomial calibration fit from 900+ wind tunnel points
   - Automated calibration software developed

2. **Thermodynamic sensing:** Temperature, humidity, pressure (RD-41 sonde board)
   - Modified sonde board with reduced footprint (removed battery, GPS, parachute deployment components)
   - MMCX antenna connection for simplified external antenna integration

3. **Additional sensors:**
   - Laser altimeter (for sea surface height measurement)
   - Thermal IR sensor (sea surface temperature)
   - Magnetometer
   - GPS

**Avionics:**
- Two 6-layer PCBs accommodating all subsystems within tight fuselage constraints
- Individual heaters for pressure sensors and IMU to maintain operating temperatures
- Magnetometer positioned at fuselage forward point (distance from battery to avoid strong magnetic field interference)
- GPS and radio positioned to minimize interference
- Clam-shell mounting with GPS antenna ground plane on one side, static pressure chamber on other
- Ports optimized for minimal wiring; positive-lock connectors for interface reliability

**Control Systems:**
- SwiftCore Flight Management System (proprietary BST autopilot)
- ESC and servo control
- Firmware updated for new avionics board and external interfaces
- Detection algorithms for release from P3
- Intelligent autonomous sampling: aircraft can make navigation decisions based on atmospheric sensor data

**User Interface:**
- USB port for programming via Android phone/tablet
- Charge port (optimized for 20V input, 4A max)
- Status LEDs
- Waterproof design
- Integration with KARMA radar interface (can display radar returns and sonde data simultaneously with mission design on tablet)
- SwiftTab UI adapted for streamlined air-deployment setup
- Simple mission programming via web interface or file transfer

**Data Transmission:**
- AVAPS integration for real-time data streaming to NOAA aircraft
- Modified RD-41 sonde board with simplified GPS interface for protocol injection
- Post-processing software development underway for interleaved sensor data streams

**Weight and Manufacturing:**
- Avionics PCB came in 50 grams under predicted weight margin
- 3D printing used extensively for low-cost, lightweight, iterative components
- Composite wings manufactured via vacuum-bagged carbon fiber on aluminum molds (array production on single mold to reduce labor costs)
- Custom cable harnesses being designed for manufacture

### SwiftCore Flight Management System
- BST proprietary certified autopilot
- Adapted for S0 avionics design
- Firmware modified for new interfaces and operational requirements
- STM32 microcontroller with HAL/LL drivers for latest board support packages
- Full flight regime estimation and control capability
- CAN bus for future payload expansion

### Multi-Hole Probe (MHP)
- 5-hole configuration integrated directly into S0 nose
- Based on BST's commercial multi-hole probe offering
- Wind tunnel calibration completed (3 hours, 900+ orientation points tested)
- Generates α, β, q measurements from 5 differential pressure ports
- Filtered performance: α RMS 0.1°, β RMS 0.25°, vTAS RMS 0.06 m/s

## Use Cases & Applications

1. **Tropical Cyclone Intensity Forecasting:** Targeted in situ measurements of lower boundary layer winds, thermodynamics in hurricanes/tropical cyclones
   - Overcomes regulatory and distance limitations of land-based UAS
   - Air deployment from P3 hurricane hunters enables rapid storm intercept
   - Low per-unit cost enables multiple flights per storm (moving from single-digit to many flights per event)

2. **Boundary Layer Profiling:** Spatial and temporal sampling of kinematic and thermodynamic processes in convective storms

3. **Sea Surface Observations:** Laser altimetry and thermal IR for SST and surface height measurements during storm events

4. **Autonomous Environmental Sampling:** Aircraft can self-position within storm features based on atmospheric data

5. **Potential Formation Flight Applications:** Reduced cost enables future innovations like coordinated multi-aircraft observations to measure atmospheric gradients

## Key Results (Q3 2020 Status Report)

### Progress Metrics
- **Contract Status:** 60% work completed as of June 23, 2020
- **Cumulative Costs:** $236,746.84 incurred

### Technical Achievements

**Design & Component Development:**
- Antenna design finalized (flexible metal band, deployed after wing swivel, stowed configuration allows pre-deployment testing on P3)
- Wing production molds designed and manufactured via Northwind Composites; first composite wing parts successfully pulled
- User interface panel design completed (charge port, USB, LEDs, switch, waterproof)
- Avionics PCBs fabricated (2 six-layer boards, all peripherals assembled and tested)
- Aircraft internals designed in CAD; removable nosecone and tail interface for serviceable design
- Tail design finalized for manufacturability
- Wire harnesses designed with custom cable vendors for production

**Multi-Hole Probe Validation:**
- 3-hour wind tunnel test session completed by NOAA team
- 900+ orientation points tested (α: -15° to +15° in 1° steps; β: -15° to +15° at each α)
- Over 1 million individual measurements collected
- Excellent calibration results achieved with 9th-order polynomial fit
- Filtered wind measurements show strong agreement with true airspeed (α 0.1° RMS, β 0.25° RMS, vTAS 0.06 m/s)
- Symmetrical, non-linear response data indicates good sensor manufacturing tolerances

**Firmware Development:**
- Migrated from CMSIS to STM32 HAL/LL drivers for latest board support packages
- All sensors tested and running at desired rates
- USB interface partially implemented; FAT file system integrated
- Radio confirmed functional; driver development ongoing
- Low-level driver development required due to new microcontroller

**Tube & Deployment System:**
- Preliminary tube design completed featuring:
  - Plastic flap (drag device) to deploy main parachute
  - Separate parachute compartment to prevent tangling
  - Hole in tube bottom for access to S0 user interface panel
  - Open back end with removable cap for storage protection
  - Motor-first deployment sequence with flip to nose-first descent

**Aerodynamic Testing:**
- Production wing molds completed and first composite wing parts successfully manufactured
- Initial testing planned with rigid wing mount to validate design while swivel mechanism under iteration

**Integration Testing:**
- Successful integration of PCBs with mechanical components
- Minor GPS cradle modification required; overall fit validated
- Test equipment under construction for droplet mitigation validation (supports future precipitation-flight testing)

### Parallel Work - DOE ARM SGP Site Testing
- Permissions received for operations at DOE ARM (Atmospheric Radiation Measurement) Southern Great Plains tower site
- Flights planned August 3-7 around instrumented tower
- Collaboration with University of Nebraska-Lincoln (UNL) team bringing:
  - Ground-based instrumented vehicles
  - Two hexrotors with simultaneous sampling capability
  - Comparative measurement validation
- Additional instrumentation and balloon soundings requested to accompany S0 flights

### Design Review Progress
- In contact with NOAA Federal and NOAA Aircraft Operations Center (AOC)
- Pursuing Concept Design Review (CDR) with AOC to validate design meets P3 launch requirements
- CDR targeted for next quarter

## Notable Details

1. **Regulatory & Operational Philosophy:** Design intentionally mimics existing radiosonde CONOPS to reduce operator workload and integrate smoothly with current NOAA hurricane reconnaissance procedures

2. **Cost-Reduction Strategy:** Avoids integration of third-party autopilots and air data probes; leverages BST's proprietary SwiftCore and sensor suite. Purpose-built for single mission (boundary layer observation) rather than multi-mission ISR platform

3. **Manufacturing Partnerships:**
   - Northwind Composites: Wing mold design and composite layup
   - First RF: Antenna design and sonde board modifications
   - NCAR: Sonde board modifications and AVAPS protocol integration
   - Local cable vendors: Custom wiring harness fabrication
   - Local PCB shops: Electronics manufacturing and assembly

4. **Sensor Integration Advantages:**
   - Multi-hole probe integrated into nose eliminates need for external air data probe
   - RD-41 sonde board simplified for S0 mounting with external antenna
   - Consolidated avionics reduce