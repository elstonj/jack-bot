# Atmospheric Sounding AF Pitch Day Proposal - Phase II

## Document Metadata
- **Type**: SBIR Phase II Proposal
- **Client/Agency**: U.S. Air Force
- **Program/Solicitation**: SBIR Topic AF192-005
- **Proposal Number**: F2-12711
- **Date**: Submitted December 2019
- **BST Products/Systems Referenced**: S0 UAS, S0-AD (Air Deployed variant), Multi-hole Probe (MHP), SwiftCore Flight Management System, SwiftTab software
- **Key Personnel**: Dr. Jack Elston (Principal Investigator, CEO), Josh Fromm (Lead Engineer), Dr. Maciej Stachura (Aerospace Engineer)

## Executive Summary
Black Swift Technologies proposes to develop the S0 UAS (Unmanned Aircraft System) as a purpose-built atmospheric sounding platform for the U.S. Air Force and commercial users. Based on the successful S0-AD (air-deployed variant used by NOAA for hurricane sampling), this Phase II effort will create a hand-launched system capable of providing vertical wind profiles up to 15,000 feet in under 20 minutes with autonomous operation and precise landing accuracy (within 10 feet). The system will integrate BST's proven Multi-hole Probe (MHP) sensor for 3D wind measurement and provide data in formats compatible with Air Force weather systems.

## Technical Approach

### Core Design Modifications
The S0 will be modified from the S0-AD platform (originally designed for air deployment from manned aircraft into hurricanes) to enable:

1. **Airframe Optimization**: 
   - Different wing/tail design for hand-launch capability
   - Optimized for fast climb rate (15,000 ft in under 20 minutes = ~4 m/s or 787 ft/min vertical rate)
   - Deep-stall landing capability enabling near-vertical descent with landing precision within 10 feet
   - Compact form factor suitable for field transport

2. **Flight Control & Wind Estimation**:
   - Novel onboard algorithms for rapid profiling while maintaining 3D wind accuracy at fast climb rates
   - Aircraft maintains constant angle of attack (~1.5°) and zero sideslip during climb to maximize wind estimation accuracy
   - Unique tail design enabling precise autoland capability

3. **Sensor Integration**:
   - Uses BST's Multi-hole Probe (MHP) as primary sensor (50 grams, $2000, 100 Hz sampling rate)
   - Measures 3D wind velocity, pressure, temperature, humidity with specifications:
     - Wind velocity resolution: 0.03 m/s
     - Wind velocity accuracy: ±0.29 m/s
     - Temperature range: -40° to 85°C (±0.3°C accuracy)
     - Pressure accuracy: ±1.5 mbar
     - Humidity accuracy: ±1.3% RH
   - Temperature range: -40° to 85°C
   - Sensor rate: 100 Hz sampling

4. **Communications & Data**:
   - Dual-mode operation: fully autonomous (no wireless) OR secure real-time wind data downlink to operator
   - Data formatted for integration with Air Force standard systems and upload to Air Force Data Centers
   - Supports multiple radio configurations: AVAPS, iMet base station, ISM 900MHz frequency-hopping, cellular network, or radio-silent mode
   - One-way legacy communication system capability (inherited from S0-AD hurricane work)
   - Ground system interface via web browser (no specialized software installation required)

5. **Operational Parameters**:
   - Hand-launch capable (deployable by single AF Weather operator)
   - Cruise speed: 35-40 mph (optimized for efficiency)
   - Endurance: 60+ minutes flight duration
   - Recovery radius: 10 feet maximum error
   - Setup/deployment time: under 5 minutes for trained operator
   - Total system cost target: ~$5,000 per aircraft (matching S0-AD pricing)

### Aerodynamic Design (Phase I Results)
- XFRL5 computational analysis completed showing:
  - Pitching moment coefficient zero at 1.5° angle of attack (natural cruise angle)
  - CL/CD ratio at maximum efficiency with flat curve allowing wider speed range (35-40 mph) without significant endurance loss
  - Stable design with tail providing negative lift at cruise conditions (tail incidence: 2° down)

## Products & Capabilities Described

### S0 UAS (Modified Atmospheric Sounding Variant)
**What it is**: Hand-launched, fixed-wing unmanned aircraft system purpose-built for atmospheric vertical profiling with integrated meteorological sensors

**Specifications**:
- Weight: 2 lbs
- Price: $5,000
- Wingspan: 31 in
- Cruise time: 60 minutes
- Propulsion: Electric
- Launch type: Hand-deployed
- Comm range: 100 miles (one-way)
- Sensing: Winds (3D), pressure, temperature, humidity
- Performance target: 15,000 ft altitude in <20 minutes, landing accuracy within 10 ft

**Use in this context**: Primary platform for Air Force rapid atmospheric sounding capability providing tactical upper air measurements to support weather forecasting and modeling for Army and Special Operations Forces operations

**Unique capabilities**: 
- Only currently available U.S.-made system specifically designed for vertical wind profiling
- Reusable vs. balloon-borne disposable systems
- Sensor-reactive control algorithms enabling adaptive sampling patterns
- Capability to operate autonomously with no wireless communications (important for undetected operations)

### S0-AD (Air Deployed Variant)
**What it is**: Predecessor system designed for air deployment from manned aircraft into hurricanes

**Specifications**:
- Weight: 2 lbs
- Price: $5,000
- Wingspan: 31 in
- Cruise time: 60 minutes
- Comm range: 100 miles (one-way)
- Current user: NOAA (5 aircraft on contract through mid-2021)

**Use in this context**: Commercial proof-of-concept demonstrating market viability; technology foundation for Phase II S0 development

### Multi-Hole Probe (MHP)
**What it is**: Advanced sensor for measuring 3D wind velocity plus atmospheric properties; uses additive manufacturing (3D printing) to reduce cost by factor of 10 versus traditional instruments

**Specifications**:
- Weight: 1.8 oz (50 g)
- Price: $2,000
- Wind velocity resolution: 0.03 m/s
- Wind velocity accuracy: ±0.29 m/s
- Temperature range: -40° to 85°C
- Temperature accuracy: ±0.3°C
- Pressure resolution: 0.012 mbar
- Pressure accuracy: ±1.5 mbar
- Relative humidity: 0-100% RH
- Humidity accuracy: ±1.3% RH
- Sensor rate: 100 Hz

**Previous sales**: 9 units sold to NOAA, NCAR, University of Colorado Boulder, and others for atmospheric research (~$9,000 revenue with minimal marketing)

**Use in this context**: Core sensing payload for S0; provides all critical measurements for atmospheric profiling; already flight-proven with established customer base

### SwiftCore Flight Management System
**What it is**: BST's proprietary autopilot system providing advanced flight control

**Use in this context**: Enables autonomous profiling, sensor-reactive control algorithms, and precise autoland capability; supports complex mission profiles including adaptive sampling

### SwiftTab Software
**What it is**: Ground station software for mission planning and vehicle operation

**Use in this context**: Tablet-based version being developed for S0 operations; allows operators to script complex atmospheric sampling patterns in intuitive manner; provides real-time data visualization compatible with weather balloon operational concepts

## Use Cases & Applications

### Air Force Primary Applications
1. **Tactical Upper Air Measurements**: Rapid wind field knowledge for precision drops (primary requirement)
2. **Army Support**: ~50% of USAF weather activity supports Army operations
3. **Special Operations Forces (SOF)**: Weather data for tactical operations
4. **Weather Nowcasting & Forecasting**: Real-time atmospheric profile data for 557th Weather Wing and Air Force Weather Directorate

### Air Force Operational Requirements Identified
From customer discovery:
- **Altitude**: 10,000 ft minimum (15,000 ft preferred for some missions)
- **Flight Duration**: 40+ minutes (shorter timescale preferred for rapid information dissemination)
- **Recovery Area**: 10 ft accuracy
- **Data Downlink**: Post-landing collection acceptable; <15 min recovery/processing desired
- **Deployment**: Hand-launched by AF Weather operators
- **Key Parameters**: Wind speed/direction (most critical), temperature, pressure, humidity, dewpoint
- **Autonomy**: Desired; ability to retask in-flight
- **Data Format**: Compatible with AF standard desktop systems and Air Force Data Centers; support for BUFR, GRIB, netCDF, and text formats

### Commercial & Research Applications
1. **Supercell Thunderstorm Research**: Already demonstrated with Tempest UAS precursor
2. **Arctic Campaigns**: Atmospheric profiling in remote regions
3. **Weather Balloon Augmentation/Replacement**: At 92 NWS Weather Forecasting Offices (current cost: $325/radiosonde launch, $21.8M annual expenditure)
4. **Severe Weather Support**: Rapid deployment for special soundings
5. **Specialized Research**:
   - Cloud physics (liquid/ice water content)
   - Aerosol characterization (size, type, optical properties)
   - Trace gas detection (ozone, SO2, NOx, methane)
   - Volcanic monitoring
   - Red tide/HAB detection via multispectral imaging
   - Soil moisture assessment
   - Snow cover/sea ice properties measurement
   - Solar radiation measurement

### High-Altitude/Remote Applications (from customer feedback)
- Arctic research (balloon tube-launch from altitude capability desired by some researchers)
- High-altitude research (some customers requested 100,000-120,000 ft capability)
- Ship-based deployment for remote ocean research

## Key Results (Phase I Feasibility Study)

### Airframe Design Validation
- Completed aerodynamic analysis using XFRL5 showing stable, efficient design
- Flow field and lift distribution analysis confirms optimal design at 1.5° angle of attack
- CL/CD maximum allows efficient flight across 35-40 mph speed range with flat efficiency curve

### Prototype Construction & Flight Testing
- Successfully built and flight-tested initial S0 prototype
- Two test flights completed in gusty conditions (5 kts sustained, gusts to 13 kts)
- Demonstrated feasible hand-launch and flight characteristics
- Qualitatively validated ease of launch capability

### Customer Discovery & Requirements Gathering
**Government Contacts**:
- Total Federal Government contacts attempted/reached: 58/5
- Federal organizations contacted/reached: 9/4 (including NOAA, NASA, NCAR)
- USAF organizations contacted/reached: 2/1

**Key Air Force Stakeholder Engagement**:
- Major Andrew Travis (Hanscom AFB, Staff Meteorologist/Deputy Branch Chief): Primary AF requirements provider; participated in bi-weekly status calls throughout Phase I
- Received MOU from Bruce A. Lambert (DAF Chief Engineer, Weather Systems Branch, AFLCMC, Hanscom AFB) stating: "The Upper Air UAS solution proposed by Black Swift is of interest to AFLCMC/HBAW, and can assist Air Force Weather in developing a tactical upper air measurement tool to support Air Force, Army, and SOF operations, which is a current unfunded requirement for ACC/A5W"

**Commercial/Research Customer Alignment**:
- Phase I identified consensus customer requirements spanning military and civilian markets
- Letters of support secured from NOAA, NASA, and NCAR researchers
- Identified significant overlap between AF needs and commercial/research requirements, validating dual-use potential

### Market Analysis
- Global weather forecasting systems market: $2.51B (2016) → $4.63B projected (2025, 7.1% CAGR)
- U.S. market represents ~25% of global market
- Weather instruments market: $322.86M (2018) → $496.78M projected (2025, 6.33% CAGR)
- Global UAS market: $18.14B (2017) → $52.30B projected (2025, 14.15% CAGR)
- Current competitor cost baseline: $325 per weather balloon radiosonde launch; 92 NWS sites launching