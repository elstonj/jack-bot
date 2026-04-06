# Atmospheric Sounding UAS - SBIR Phase I Proposal

## Document Metadata
- Type: SBIR Phase I Proposal (presentation format)
- Client/Agency: U.S. Air Force
- Program/Solicitation: AF192-005 (Air Force UAS Pitch Day)
- Proposal Number: F192-006-1526
- Date: July 24, 2019
- BST Products/Systems Referenced: S0 (Hurricane Sampler), S2 UAS, 3D Wind Probe, Atmospheric Sensor Suite, SwiftCore avionics
- Key Personnel: Dr. Jack Elston (PI, Lead Avionics Developer)

## Executive Summary
Black Swift Technologies proposed developing an Atmospheric Sounding UAS based on their heritage S0 Hurricane Sampler platform to provide the U.S. Air Force with a low-cost, fully autonomous, fixed-wing UAS for high-resolution atmospheric boundary layer profiling. The system would deliver real-time in situ meteorological data (winds, temperature, pressure, humidity) to augment weather models, operate in extreme conditions, and cost approximately $5,000 per aircraft.

## Technical Approach

**Core System Design:**
- Small, fixed-wing recoverable UAS (under 2 lbs) derived from S0 Hurricane Sampler heritage
- 2-hour endurance cruise time
- Vertical profiling capability to 15,000+ ft AGL
- Operations in wind regimes up to 20 m/s (wider tolerance than equivalent multirotor systems)
- Fully automated operation with scripting-based UI for custom sampling plans

**Sensor Suite:**
- 3D Wind Probe (BST-designed):
  - 100 Hz measurement rate
  - Accuracy: ±0.5 m/s winds, ±1 degree
  - Co-located IMU, magnetometer, GPS
  - Rugged design using 3D printing techniques
  - Validated in wind tunnels and operationally
- Thermodynamic sensors: pressure, temperature, humidity
- Modular payload architecture for future trace gas and particulate sensors

**Data & Control Systems:**
- Automated profiling with fully scripted sampling patterns
- "Throw and forget" simplified UI for basic operations
- BST Atmospheric Toolkit for complex pattern design
- Standardized data format for easy assimilation into Air Force systems
- Future expansion to feature tracking and model-based sampling
- Future expansion to swarm-based operations

**Deployment Options:**
- Air-launched from manned aircraft
- Balloon-deployed (future variant) for controlled sampling on descent vs. wind-driven drift
- Integration with standard balloon sonde base stations

## Products & Capabilities Described

**S0 Hurricane Sampler (Predecessor):**
- Air-launched UAS for low-level hurricane and sea-surface observations
- Reliable, advanced capabilities at low price point
- 1+ hour endurance for targeted observations
- Accurate, well-calibrated data
- Automated eyewall boundary tracking based on simplified hurricane model and local measurements
- Integration with legacy AVAPS radio system

**3D Wind Probe:**
- Designed for accuracy and ruggedness
- Used on both manned and unmanned aircraft
- Low cost through 3D printing
- 100 Hz, ±0.5 m/s and ±1 degree accuracy
- Full sensor suite with co-located IMU, magnetometer, GPS
- Operational heritage in Arctic, tornadic thunderstorms, hurricanes
- Validated in wind tunnels and against meteorological towers

**S2 UAS:**
- Mentioned as successfully commercialized product
- Applications: soil moisture measurement, volcano observations, Greenland atmospheric sampling, wildland fire monitoring

**Avionics, UI, GCS (Ground Control Station):**
- Developed in-house by BST
- Critical for robust modular solutions
- Fully autonomous capability
- Minimal training required (< half day)

## Use Cases & Applications

**Primary - Vertical Atmospheric Profiling:**
- Atmospheric boundary layer sampling for Air Force weather operations
- Data assimilation into WRF (Weather Research and Forecasting) models
- Fills data gap between surface observations, satellites, and balloon-borne radiosondes
- Operations up to 15,000 ft AGL
- Icing and fog predictions
- Small-scale turbulence measurement

**Secondary - Balloon-Deployed Variant:**
- High-altitude sampling with controlled descent sampling (vs. wind-drift radiosondes)
- Compatibility with Air Force ground station radios
- Simplified recovery

**Civilian/Commercial Applications:**
- National weather centers: NOAA, NSSL, NCAR
- Universities and national laboratories
- Commodity/crop health analytics
- Replacement for 800+ weather stations worldwide using twice-daily balloon radiosondes
- Reusable platform provides cost savings over consumable sondes

**Historical Operational Heritage:**
- 20+ major scientific deployments (Arctic, tornadoes, hurricanes, volcanoes, wildfires)
- 150+ FAA-approved flight operations
- 2,500+ legal flight hours
- 8 NASA Flight Safety Reviews

## Key Technical Specifications

| Parameter | Value |
|-----------|-------|
| Profiling Altitude | Up to 15,000+ ft AGL |
| Endurance | 2 hours cruise |
| Wind Tolerance | Up to 20 m/s operations |
| Weight | Under 2 lbs |
| Target Unit Cost | $5,000 per aircraft |
| Wind Measurement Accuracy | ±0.5 m/s, ±1 degree |
| Wind Probe Sample Rate | 100 Hz |
| Training Required | < 0.5 day |

## Notable Details

**BST Heritage & Credibility:**
- Established 2011, initially selling U.S.-made avionics
- 100+ peer-reviewed publications on UAS
- All-in-house development: avionics, UI, GCS, aircraft
- No Chinese components; entirely U.S. made
- Approved for flight by multiple federal institutions

**PI Qualifications:**
- Dr. Jack Elston, Ph.D. University of Colorado Aerospace Engineering (2011)
- Dissertation: UAS for tornadic thunderstorm research
- Postdoctoral work: accurate wind measurement from small UAS
- Lead avionics developer at BST
- Missions: COCONUE, VORTEX2, ELEVATE, ISARRA
- Invited speaker at WMO Workshop on UAVs for Operational Meteorology
- PI for upper atmospheric sampling of Venus using gliders

**Past Commercialization Success:**
- Soil Moisture Mapping UAS (NASA SBIR)
- S2 UAS (2 NASA SBIRs, evolved and improved)
- Multiple Hole Probe (NASA SBIR) - 10+ units sold
- Machine Vision technology (NASA SBIR) - transferred to underwater tech with commercial customer
- Predictive maintenance technology (NASA SBIR) - cloud-based portal for customer use

**Competitive Advantages:**
- Significantly lower cost than competitors
- Fully autonomous "launch and forget" operations
- Wider wind tolerance than equivalent multirotors
- Modular design for rapid sensor integration
- Proven accuracy validated in extreme conditions
- Integration with existing Air Force systems and radio protocols (balloon variant)
- Reusable vs. consumable radiosondes

**Proposed Phase I Objectives:**
- Interface and modify S0 system for Air Force use
- Focus on data interface and collection pipeline
- Automate data ingestion into Air Force systems to minimize personnel time
- Identify and target Air Force use cases

**Future Expansion Capabilities:**
- Trace gas sensors (unspecified types)
- Particulate size and distribution measurement
- Sea surface temperature
- Swarm-based operations
- Data-driven automated control
- Directed descent sampling (balloon variant)
- Direct radio integration with Air Force ground stations