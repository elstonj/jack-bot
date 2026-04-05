# #sbir-hurricane

## Overview
The #sbir-hurricane channel is the primary workspace for Black Swift Technologies' SBIR Hurricane project, focused on developing the S0 unmanned aircraft system for hurricane reconnaissance missions. The channel is highly active with extensive technical discussions, operational updates, and mission planning covering 2020-2024. Key participants include Joshua Fromm, Jack Elston, Maciej, Danny Troke, and Dan Prendergast.

## Key Decisions

**Aircraft Design & Configuration:**
- User panel positioned on bottom of NOAA S0 for easier access through outer tube (June 2020)
- Selected T-Motor F60 for propulsion due to discontinued KDE motor (September 2020)
- Switched from Castle ESC to 36A version for improved reliability (November 2020)
- Spring steel antenna wrapped around fuselage confirmed as optimal design (November 2020)
- Wing pivot system designed to "fall away" after deployment to save weight (December 2020)
- Deployment timing set at 5 seconds (parachute flap) and 10 seconds (tube release) (April 2021)

**Sensor & Electronics:**
- Selected SF20 laser altimeter over SF22 due to Ardupilot/PX4 integration issues (January 2021)
- Eliminated datalogging requirement after presentation feedback (April 2021)
- Selected MLX90614ESF-DCH thermal sensor per Terry's recommendation (December 2021)
- Direct soldering battery/ESC to AP due to space constraints (November 2021)
- Dual USB-A ports on front panel instead of USB-C for GCS (May 2022)

**Manufacturing & Components:**
- 50/50 cost split between Air Force and Hurricane for KMac tubes (June 2020)
- Lee selected for deployment tube machining at $700 NRE, $95 per additional tube (March 2022)
- Aluminum caps chosen over 3D printed ones after high-Q deployment failure (May 2022)
- Switched to Samsung INR21700-50S cells replacing Panasonic NCR18650GA (February 2024)
- Decision to use 76gsm wing skins instead of 160gsm for 50g weight savings (October 2024)

## Projects & Initiatives

**S0 Hurricane Aircraft System:**
- Primary deliverable: 16-18 complete S0 systems for NOAA hurricane reconnaissance
- Specifications: 2.6 lbs GTOW, 32.8" wingspan, 22.5 m/s cruise speed, 2+ hour endurance
- Sensors: Vaisala RSS421, MLX90614ESF thermal sensor, 9-hole pressure system
- Communication: 400MHz licensed band with 150+ nautical mile range demonstrated

**Hurricane Flight Controllers:**
- Dan Prendergast developed eyewall tracking algorithms with left/right turn capabilities
- Inflow controller for spiral trajectory patterns
- Center fix controller for eye navigation (first successful automated center fix achieved)
- Controllers tested extensively in X-Plane simulation and live hurricane flights

**Ground Control Station (GCS):**
- Rack-mounted system with HDMI output, powered USB hub
- 400MHz radio integration with tablet interface
- Real-time telemetry and flight plan generation capabilities

## Action Items & Commitments

**Manufacturing & Delivery (2024-2025):**
- 25-30 additional aircraft for NOAA 2025 hurricane season
- Combined NOAA and Air Force contracts requiring ~400 units
- Long-lead item ordering: 90 days for latches, 6 weeks for phenolic tubes
- Component costs: $7k latches, ~$25k wings, $20k deployment tubes, ~$5k fuselage tubes

**Technical Development:**
- Complete radar altimeter testing (Innosent unit) as laser replacement
- Address humidity sensor saturation issues in extreme weather
- Investigate communication failures in >98% relative humidity conditions
- Implement improved ESC re-arming capability after engine disable events

## Client & External References

**Primary Client - NOAA:**
- Joe (project lead), Akshar and Rebecca (P3 requirements), Nick, Dana Naeher
- AOC (Aircraft Operations Center) - receiving deliveries and operations
- Hurricane Reconnaissance missions from P3 aircraft (NOAA42, NOAA43)
- National Hurricane Center using S0 data in forecast models

**Partners & Vendors:**
- Area-I: MHP integration and nose cone development
- FirstRF (Ken): Antenna design and integration
- Lee: Wing and deployment tube manufacturing
- Vaisala: RSS421 sensor supplier and support
- Lightware: Laser altimeter supplier (SF20, SF22)

**External Validation:**
- 53rd Weather Reconnaissance Squadron presentation opportunity
- National Security Council visitor made White House call during mission
- NHC and NWS considering S0 data in operational forecasts

## Recurring Topics & Themes

**Weekly Technical Meetings:**
- Regular Thursday update meetings for project status
- Integration testing coordination between team members
- QC checklist reviews and aircraft certification processes

**Hurricane Season Operations:**
- 2024 season: 19 flights, 20.5 total hours, 11/12 successful launches in first deployment
- Record achievements: 169 mile communication range, 106+ minute endurance
- Operations from Lakeland, Barbados, Bermuda, and Texas bases

**Performance Optimization:**
- Continuous weight reduction efforts (achieved 30g reduction in 2024)
- Power consumption optimization: 58W average (enabling 2+ hour missions)
- Wind measurement accuracy: ±3 m/s average error vs reference data

## Important Resources

**Technical Documentation:**
- Hurricane Controllers Operator's Manual (Dan Prendergast)
- NetCDF file generation scripts for NOAA data delivery
- S0 parameter files and firmware repositories
- QC checklists and assembly procedures

**Data Products:**
- Real-time hurricane data: winds, pressure, temperature, humidity
- WMO-formatted netCDF files for operational use
- Flight summaries and telemetry analysis
- Sea surface temperature measurements

**External Links:**
- NOAA article: https://www.aoml.noaa.gov/black-swift-drone/
- ARM NetCDF guidance: https://www.arm.gov/guidance/datause/formatting-and-file-naming-protocols
- Hurricane field program data: aoml.noaa.gov

## Recent Activity

**2024 Hurricane Season Success:**
- Achieved unprecedented 6/6 successful full-duration missions initially
- S0 aircraft successfully flew through Category 5 Hurricane Milton (240 mph winds)
- First automated hurricane center fix accomplished
- Maximum recorded winds: 240 mph gusts, 2.8g acceleration loads

**Business Growth:**
- NOAA secured funding for 25-30 additional aircraft for 2025 season
- Air Force contract secured requiring NDAA compliance
- Company projected growth to 30 people
- Cost optimization: Single S0 system estimated at $6,300 (airframe $4,200 + tube $2,100)

**Technical Achievements:**
- 169 nautical mile communication range record
- 106+ minute flight endurance records
- Successful operations in extreme weather (>98% humidity, heavy rain)
- Real-time data integration with National Hurricane Center forecasting