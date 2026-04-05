# Hurricane R&D Funding Breakdown (2025 OMAO)

## Document Metadata
- Type: Budget/Funding breakdown document
- Client/Agency: NOAA OMAO (Office of Marine and Aviation Operations)
- Program/Solicitation: 2025 OMAO funding cycle
- Date: November 21, 2025
- BST Products/Systems Referenced: S0 (tube-launched), AirOps, deployment tube, aircraft platform
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
This is a detailed budget breakdown for a multi-year (Years 1-3) hurricane research and development program funded through NOAA OMAO. The document outlines engineering tasks, aircraft modifications, operational flight costs, and platform development, with total project budget of $327,952 distributed across three years ($132,333 Y1, $135,619 Y2, $60,000 Y3).

## Technical Approach
BST is proposing a series of engineering improvements and operational deployments for unmanned aircraft systems in hurricane environments:

**Year 1 Focus (NRE Engineering):**
- Optimize laser configuration for rain operation
- Implement dual GPS with moving baseline RTK for improved heading estimation and velocity/position accuracy (addressing magnetometer finickiness)
- Upgrade to 10Hz meteorological data collection
- Firmware/comms/UI customization for automation and operational capability
- Battery optimization for extended endurance (potential +30 min additional flight time)
- Manufacturability improvements
- Data buffering and re-transmission for communications loss
- Clear air testing (2025) and initial hurricane flight operations (4 flights × $4,000)

**Year 2 Focus:**
- USB-based firmware update system for deployment tube and aircraft (eliminates need to remove aircraft from tube)
- Wind tunnel testing to characterize wing effects
- Automated NetCDF file creation at P3 ground station
- Skyfora sensor integration (in addition to Vaisala)
- Hurricane flights (4 flights, $16,000)

**Year 3 Focus:**
- Laser-relative flight capability
- Hurricane flights (4 flights, $16,000)
- Documentation and training materials

## Products & Capabilities Described

### S0 (Tube-Launched Aircraft)
- Primary unmanned platform for hurricane deployment
- Deployed from aircraft tube launcher
- Budget allocation: $720,000 for tube-launched S0 (cost line item suggests vehicle procurement/development)
- Modifications include: laser configuration optimization, dual GPS heading system, extended endurance batteries, automated firmware updating capability

### AirOps (Flight Control/Data Management System)
- Software system managing aircraft operations
- Proposed enhancements: addition of laser altitude, radio signal quality, and time-since-last-comms fields for situational awareness
- Integration with meteorological data collection (10Hz met data)
- Firmware customization for automation and scientist-controlled flight adaptation

### Deployment Tube
- Launch vehicle for S0
- Proposed USB-based firmware update capability
- CAD launching option under consideration (avoids depressurization, simplifies AVAPS integration)

## Use Cases & Applications

**Hurricane Operations:**
- Deployment from P3 aircraft into hurricane environments
- Wind measurement and meteorological data collection
- 12 total hurricane flights planned across 3 years (4 flights per year at $4,000/flight)
- Clear air testing preceding operational deployments (2025)

**Operational Requirements:**
- Real-time situational awareness for flight engineers
- Autonomous operation with scientist-adaptable parameters
- Communications redundancy and data buffering for harsh environments
- Ground station integration at P3 (NOAA aircraft platform)

## Budget Summary
| Category | Y1 | Y2 | Y3 | Total |
|----------|----|----|-------|-------|
| Engineering Tasks (NRE) | $132,333 | $135,619 | $60,000 | $327,952 |
| Aircraft/Platform Development | Included | Included | Included | $720,000 (S0) |
| **Total Identified** | **$132,333** | **$135,619** | **$60,000** | **$1,047,952+** |

*Note: Document shows engineering NRE totaling $327,952 with separate S0 vehicle line item of $720,000*

## Notable Details

**Key Technical Improvements:**
- Magnetometer limitation acknowledged as major wind measurement error source; dual GPS RTK moving baseline proposed as solution
- Extended 30-minute additional endurance potential through battery optimization
- Communications resilience critical for hurricane operations (data buffering, re-transmission, USB firmware updates eliminate field maintenance requirements)

**Platform Flexibility:**
- MHTP integration to new platforms under consideration (Dragoon or Strato Solutions mentioned in cost line)
- Optional enhancements: onboard video ($18,000), CAD launching ($34,000)
- Suggests future platform evolution beyond current S0

**Operational Integration:**
- Ground station integration with P3 aircraft (NOAA's primary hurricane research platform)
- Automated data processing (NetCDF file creation) reducing post-mission QC time
- Multi-sensor integration (Vaisala primary, Skyfora as alternative)

**Rebudgeting Detail:**
- Document filename references "de minimis" rebudgeting with Years 2-3 funding adjustments, suggesting flexibility in execution timing