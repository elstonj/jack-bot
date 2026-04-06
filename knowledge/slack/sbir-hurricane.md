# #sbir-hurricane

## Overview
The #sbir-hurricane channel is the primary workspace for Black Swift Technologies' SBIR Hurricane project, focused on developing the S0 unmanned aircraft system for hurricane reconnaissance missions. The channel is highly active with extensive technical discussions, operational updates, and mission planning spanning 2020-2026. Key participants include Joshua Fromm, Jack Elston, Maciej, Danny Troke, Dan Prendergast, Alex Lomis, and Nate.

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

**Ground Control Station Operations (April 2026):**
- Single operator per aircraft confirmed as acceptable by NOAA operational rules (April 2026)
- GCS firmware updates for dual-channel radio control implemented (April 2026)
- Use of Channel 1 designated for flight operations over Avon Park (April 2026)

## Projects & Initiatives

**S0 Hurricane Aircraft System:**
- Primary deliverable: 16-18 complete S0 systems for NOAA hurricane reconnaissance (expanded to 25-30 additional for 2025 season)
- Specifications: 2.6 lbs GTOW, 32.8" wingspan, 22.5 m/s cruise speed, 2+ hour endurance
- Sensors: Vaisala RSS421, MLX90614ESF thermal sensor, 9-hole pressure system
- Communication: 400MHz licensed band with 150+ nautical mile range demonstrated

**Multi-UAS Operations:**
- Developing dual-aircraft capability for simultaneous operations with single operator
- GCS infrastructure expansion to support multiple aircraft from NOAA P3 platform
- Testing and validation of coordinated flight operations (April 2026)

**Hurricane Flight Controllers:**
- Dan Prendergast developed eyewall tracking algorithms with left/right turn capabilities
- Inflow controller for spiral trajectory patterns
- Center fix controller for eye navigation (first successful automated center fix achieved)
- Controllers tested extensively in X-Plane simulation and live hurricane flights

**Ground Control Station (GCS):**
- Dual Swift Station systems (SwiftStation-400001 "top" and SwiftStation-400002 "bottom") for multi-channel operations
- Rack-mounted system with HDMI output, powered USB hub
- 400MHz radio integration with tablet interface and hot-swappable USB radio modules
- Real-time telemetry and flight plan generation capabilities
- Channel 1 and Channel 2 radio configuration with dynamic switching capability

## Action Items & Commitments

**Manufacturing & Delivery (2025-2026):**
- 25-30 additional aircraft for NOAA 2025 hurricane season
- Combined NOAA and Air Force contracts requiring ~400 units
- Long-lead item ordering: 90 days for latches, 6 weeks for phenolic tubes
- Component costs: $7k latches, ~$25k wings, $20k deployment tubes, ~$5k fuselage tubes
- Single S0 system estimated at $6,300 (airframe $4,200 + tube $2,100)

**Technical Development:**
- Complete radar altimeter testing (Innosent unit) as laser replacement
- Address humidity sensor saturation issues in extreme weather
- Investigate communication failures in >98% relative humidity conditions
- Implement improved ESC re-arming capability after engine disable events
- GCS firmware updates requiring aircraft code updates (pending implementation, April 2026)
- Funding approval for additional GCS units for dual-aircraft capability (in progress with Nick P, April 2026)
- Landing site preparation: 450m sand/smooth road strip near Avon Park for SW-NE approach alignment (April 2026)

## Client & External References

**Primary Client - NOAA:**
- Joe (project lead), Akshar and Rebecca (P3 requirements), Nick, Nick P (funding authorization), Dana Naeher
- AOC (Aircraft Operations Center) at Flightline Drive, Lakeland, FL 33811-2836 - receiving deliveries and operations
- Hurricane Reconnaissance missions from P3 aircraft (NOAA42, NOAA43)
- National Hurricane Center using S0 data in forecast models
- Mark (operational planning and logistics support)

**Partners & Vendors:**
- Area-I: MHP integration and nose cone development
- FirstRF (Ken): Antenna design and integration
- Lee: Wing and deployment tube manufacturing
- Vaisala: RSS421 sensor supplier and support
- Lightware: Laser altimeter supplier (SF20, SF22)
- FedEx: Expedited delivery logistics

**External Validation:**
- 53rd Weather Reconnaissance Squadron presentation opportunity
- National Security Council visitor made White House call during mission
- NHC and NWS considering S0 data in operational forecasts

## Recurring Topics & Themes

**Weekly Technical Meetings:**
- Regular Thursday update meetings for project status
- Integration testing coordination between team members
- QC checklist reviews and aircraft certification processes

**GCS Infrastructure Management (April 2026):**
- Swift Station hardware maintenance and power cycle sequencing
- Antenna cable characterization and signal strength diagnostics
- Radio channel configuration testing and verification procedures
- Firmware deployment coordination between ground control and aircraft systems

**Hurricane Season Operations:**
- 2024 season: 19 flights, 20.5 total hours, 11/12 successful launches in first deployment
- Record achievements: 169 mile communication range, 106+ minute endurance
- Operations from Lakeland, Barbados, Bermuda, and Texas bases
- 2026 season: Preparing for ocean flights from P3 platform with multi-UAS capability

**Performance Optimization:**
- Continuous weight reduction efforts (achieved 30g reduction in 2024)
- Power consumption optimization: 58W average (enabling 2+ hour missions)
- Wind measurement accuracy: ±3 m/s average error vs reference data
- GCS shutdown timing optimization (30-second difference between stations due to wiring)

## Important Resources

**Technical Documentation:**
- Hurricane Controllers Operator's Manual (Dan Prendergast)
- NetCDF file generation scripts for NOAA data delivery
- S0 parameter files and firmware repositories
- QC checklists and assembly procedures
- GCS firmware update procedures and installation commands
- Google Earth document for landing site planning and recommendations

**Data Products:**
- Real-time hurricane data: winds, pressure, temperature, humidity
- WMO-formatted netCDF files for operational use
- Flight summaries and telemetry analysis
- Sea surface temperature measurements

**Operational Resources:**
- NOAA AOC contact: Flight Operations Office, 3450 Flightline Drive, Lakeland, FL 33811-2836
- FedEx tracking capability for equipment delivery (example tracking: 870349069283)
- GCS radio channel configuration utility