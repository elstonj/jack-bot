# Quarter 7 Report: Soil Moisture Mapping sUAS Phase II

## Document Metadata
- Type: Phase II Interim Report (SBIR)
- Client/Agency: NASA
- Program/Solicitation: NASA SBIR Phase II, Topic not specified
- Contract Number: NNX14CG09C
- Date: January 2015 (Quarter 7 of Phase II)
- BST Products/Systems Referenced: SuperSwift, Spirit of SuperSwift (S3), Tempest UAS, LDCR (L-band Digital Correlator Radiometer)
- Key Personnel: Stachura (contact: stachura@blackswifttech.com)
- Location: Black Swift Technologies LLC, Boulder, CO

## Executive Summary
Quarter 7 focused on completing three major work streams for the soil moisture mapping Phase II: (1) processing and analyzing radiometer flight data from Canton test site deployments, validating LDCR brightness temperature measurements against in-situ soil moisture sensors with favorable agreement; (2) finalizing SuperSwift aircraft designs including fuselage molds, v-tail stabilizers, and structural components ready for manufacturing; and (3) completing power board redesigns and fabricating additional LDCR receiver board assemblies for flight systems.

## Technical Approach

### Data Processing & Soil Moisture Analysis
BST developed and refined brightness temperature mapping methodologies using two complementary approaches:

1. **N-Sample Grid-Cell Averaging Method**: Spatial averaging of antenna temperature (TA) measurements within discrete grid cells corresponding to flight line separation (~29 m). Two-stage averaging: first within each calibration cycle (N1=6 samples), then across multiple calibration cycles within each grid cell (N2~31 cycles). Calculated combined averaging of N=186 samples per pixel, yielding antenna temperature standard deviation of ~0.9 K.

2. **Unbiased Linear Minimum Mean Square Error (LMMSE) / Kriging Method**: Optimal antenna temperature estimation using radially-symmetric covariance functions to map irregularly sampled flight data onto regular grids. Applied unbiased constraint (Equation 7) using Lagrange multipliers to ensure mean values were properly preserved.

**Covariance Model**: Exponential radial covariance with characteristic length a=58 m (approximately twice the flight line separation).

**Key Performance Metrics**:
- LDCR antenna temperature sensitivity to volumetric soil moisture (VSM): 0.87-0.82 K/% (slope of best-fit lines)
- LDCR measurements showed excellent agreement with in-situ soil moisture sensor data
- Repeatably detected ~40 K warming in NW quadrant and ~40 K cooling in SW corner of mapping area across two consecutive flight days

### Canton Test Site Deployment
- **Location**: Canton Soilscape, Kansas (36.00375°N, -98.63125°W)
- **Mapping Area**: ~41 acres rectangular grid
- **Flight Platform**: Tempest UAS
- **Flight Altitude**: h=35 m
- **LDCR Antenna 3dB Beam Width**: ~45° (from HFSS simulations), corresponding to ~28 m surface pixel size
- **In-Situ Validation**: 12 wireless soil moisture sensor nodes at 5 cm, 15 cm, and 30 cm depths; 9 nodes within mapping area
- **September 8 Flight**: 11:35 AM start, ~60% cloud cover, 27°C ambient, dry grass (~7" height), ~16 min duration
- **September 9 Flight**: 8:00 AM start, ~100% cloud cover, 20°C ambient, dew-moistened grass, ~16 min duration

**Data Characteristics**:
- LDCR sampling: 1 ms A/D interval, 1.5 ms time constant low-pass filter
- 44 ms calibration cycle period
- Upwelling TA measurement noise (single-sample σ): ~7.5 K
- After filtering and averaging: σTA ~0.9 K per grid cell

### SuperSwift Aircraft Development

**Fuselage Design & Manufacturing**:
- Finalized outer fuselage geometry with smooth blending and optimized radius of curvature (≥0.26" where possible) to reduce manufacturing difficulty and interference drag
- Wing joiner extended to 8" to match fuselage diameter, enabling top hatch for dual propulsion batteries and improved access
- Internal load-carrying structure: composite core flat-plate interlocking assembly with longitudinal stringers for battery and thrust load distribution
- Manufacturing method: Two-half construction (starboard/port) using outer female molds
- Material/Process: Epoxy resin + 3 plies 7781 E-glass fiberglass per half, wet layup under vacuum; halves joined with 3.5" wide ply bands, open cure (non-vacuum)

**V-Tail Stabilizer Design**:
- Airfoil selection: NACA 0014 (changed from NACA 0008 to accommodate internal servo/antenna mounting and increase volume; aerodynamic impact minimal as tail functions as flying wing)
- Area increase: ~12% in both stabilizer and control surface to improve elevator authority at low speed (landing)
- Internal structure: Laser-cut/CNC-machined composite sandwich-core fiberglass flat stock with interlocking design
- Materials: Vacuum-formed high-impact polystyrene (HIPS) shells OR standard fiberglass shell (both manufacturing paths being pursued to reduce risk)
- Removable design: Carbon fiber joiner rods + blind-mate MPX electrical connectors for tool-free field assembly
- **Unique Feature**: Symmetric airfoil means left/right tail surfaces are aerodynamically identical; BST design uses single interchangeable surface for both sides, reducing molds and spares requirements

**Center Joiner Piece**:
- 3D printed from DuraForm HST (fiber-reinforced engineering plastic with low thermal expansion, cold-temperature toughness, suitable for Arctic deployment)
- Mechanical interface: Inner lip aligns to hexagonal tail tube; secured with two screws; hexagonal tube partially cut away to distribute tail surface loads
- Electrical interface: Embedded MPX connectors for blind-mate connection to v-tail surfaces
- Modular design enables rapid customization for mission-specific antenna mounting

**Thrust Analysis**:
- Static thrust testing of 5 propeller configurations at full throttle with 5-cell LiPo (21V):
  - 12x12: Insufficient thrust for hand launch
  - 14x8.5: ~27.6 N thrust
  - 14x10: ~27.8 N thrust (original design baseline)
  - 14x14: Stalled condition (6870 RPM, 900+ W, insufficient thrust)
  - **14x9 three-bladed (selected)**: 34.6 N thrust (+6.8 N / +24.5% vs. 14x10), 142 W additional power consumption (+24.6%)
- Analysis software predicted 90-minute flight time achievable with three-bladed propeller (to be verified)

### Spirit of SuperSwift (S3) Flight Testing
S3 is a commercial prototype built with external Colorado State investment and initial customer downpayment; operates under BST Section 333 FAA exemption. Aerodynamically identical to Phase II SuperSwift design.

**Initial Manual Flight Test**:
- Duration: ~2 minutes
- Conditions: 5-6 m/s headwind
- Results:
  - Qualitative handling: Excellent control response; control surface sizing appropriate
  - Structural: Wings showed slight bending (resolved by increasing joiner rod thickness 50%)
  - Propulsion: System sufficient but felt underpowered (as designed for efficiency)
  - Hand launch: Successful; throw acceleration = 6 m/s; aircraft released at 11 m/s airspeed
  - Pitot sensor reading at release: 5 m/s (wind speed) + 6 m/s (throw) = 11 m/s IAS

**Failed Launch Attempt (Low Wind)**: 
- Conditions: 2 m/s wind
- Result: Aircraft accelerated from 2 m/s to 8 m/s after throw but could not climb; landed after couple seconds
- Root cause: Combined insufficient elevator effectiveness at low airspeed + insufficient static thrust
- Led to thrust analysis and three-bladed propeller selection (Section 3.3)

**Autonomous Flight Test (with 3-bladed propeller)**:
- Total flight duration: 17.4 minutes
- Phases: Manual takeoff, autopilot tuning, autonomous waypoint following
- Autopilot performance: Good tracking during tuning; roll/pitch/IAS well-controlled
- Wind aloft: ~6 m/s (measured from GPS ground speed difference vs. IAS)
- Status: Further zero-wind testing required to confirm hand-launch capability

## Products & Capabilities Described

### LDCR (L-band Digital Correlator Radiometer)
- **Purpose**: Passive L-band radiometry for soil moisture remote sensing
- **Operational Principle**: Brightness temperature measurement of upwelling thermal radiation at L-band frequencies
- **Sensor Components**: 
  - Antenna (MiCo antenna, 45° 3dB beam width)
  - Low-pass video filter (τ=1.5 ms time constant)
  - Calibration system with multiple states
  - Thermistor temperature monitors (8 units; 2.7 V excitation)
  - TEC heaters/coolers for thermal stability
- **Data Processing**: Integrates with custom software for brightness temperature mapping and soil moisture estimation
- **Performance**: Excellent correlation with in-situ soil moisture sensors (K/% sensitivity coefficients of 0.82-0.87)
- **Integration**: Mounted on Tempest UAS; boards being fabricated for SuperSwift integration

### SuperSwift sUAS
- **Classification**: Hand-launchable, long-endurance small unmanned aircraft system
- **Endurance Target**: 90+ minutes (1.5 hours goal)
- **Power System**: 5-cell or 6-cell lithium polymer battery; three-bladed 14x9 propeller; efficiency-optimized motor
- **Payload Capacity**: Radiometer systems (LDCR), antennas, sensors
- **Field Deployment**: Tool-free assembly with slip-on wing/tail connectors; designed for rapid Arctic deployment
- **Launch Method**: Hand launch (no launcher required, though launcher-compatible)
- **Manufacturing Readiness**: Designs finalized and ready for tooling; dual manufacturing paths (vacuum-formed plastic and fiberglass) to reduce schedule risk
- **Structural Features**: Composite fuselage, removable wings and v-tail, modular avionics

### Tempest UAS
- **Role**: Baseline platform used for Canton soil moisture mapping flights
- **Flight Characteristics**: Capable of 35 m altitude operations, ~16 minute endurance in test configuration

## Use Cases & Applications

### Primary Mission: Soil Moisture Mapping
- **Application**: Passive microwave remote sensing of surface and near-surface soil moisture
- **Test Case**: Soilscape project at Canton, Kansas
- **Use**: Validation of LDCR radiometer system and brightness temperature mapping algorithms
- **Operational Concept**: Low-altitude (~35 m) serpentine flight patterns over ~41-acre study areas; dual flights for diurnal variation assessment

### Secondary/Planned Missions
- **Arctic Operations**: SuperSwift designed for tool-free field deployment in cold environments (DuraForm HST plastic for low thermal expansion, cold-temperature toughness)
- **Commercial Applications**: S3 prototype being developed for broader sUAS market beyond soil moisture (specific applications not detailed in this report)

## Key Results

### Soil Moisture Mapping Validation

**Brightness Temperature Mapping**:
- Successful deployment of LDCR radiometer system on Tempest UAS over Canton site
- Two consecutive flight days (Sept 8-9, 2014) generated high-resolution brightness temperature maps
- Methodology validated: upwelling antenna temperature directly correlates with in-situ measured volumetric soil moisture

**Quantitative Results**:
- September 8 (11:35 AM): Mean surface physical temperature 29.91°C (σ=0.79°C); upwelling TA maps show ~20 K higher values than September 9
- September 9 (8:00 AM): Mean surface physical temperature 19.87°C (σ=0.16°C); overcast conditions with dew
- Spatial Patterns: Repeatable ~40 K