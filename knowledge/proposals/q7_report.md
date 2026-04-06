# Q7 Report: A Ruggedized UAS for Scientific Data Gathering in Harsh Environments

## Document Metadata
- **Type:** Quarterly Report (Phase II, Q7)
- **Client/Agency:** NASA
- **Program/Solicitation:** 2016 SBIR Phase II, Topic: Volcano Monitoring
- **Contract Number:** NNX17CP13C
- **Date:** March 2019
- **BST Products/Systems Referenced:** SuperSwift XT, SwiftCore FMS, SwiftPilot, SwiftTab, Multi-Hole Probe (MHP), S2 XT
- **Key Personnel:** Jack S. Elston (PI), Lois J. Wardell (Senior Personnel), Maciej Stachura (Aircraft Design & Flight Authorization), David Pieri (NASA Technical Monitor)

## Executive Summary
Black Swift Technologies is developing the SuperSwift XT, a ruggedized small unmanned aircraft system (sUAS) specifically designed to collect in situ scientific data from volcanic plumes and other harsh atmospheric environments. Phase II focuses on building a commercially viable, turn-key system capable of measuring volcanic gases (SO₂, CO₂, H₂S, CH₄), ash characteristics, and atmospheric parameters (pressure, temperature, humidity, 3D winds) through integrated sensor packages and advanced flight planning software. As of Q7 (March 2019), the project was 87.5% complete with cumulative costs of $602,677, with planned volcanic test deployments to Turrialba Volcano (Costa Rica) or Volcanoes National Park.

## Technical Approach

The SuperSwift XT development follows a "test early, test often" philosophy with validation at every key step:

1. **Airframe Design:** Modified SuperSwift airframe enhanced for harsh environment operations including high altitude (20,000+ ft), strong turbulence, corrosive volcanic ash particles, and difficult mountainous terrain. Design improvements include custom motor cowl for ash protection, sealed hatches/openings (IP 63 rating), ruggedized components.

2. **Flight Management System:** Leverages BST's SwiftCore FMS with SwiftPilot autopilot and SwiftTab tablet-based operator interface. Phase II adds automatic volcanic plume mission profile generation capabilities and custom mission plan language for scientists with minimal UAS training.

3. **Wind Measurement:** Custom-designed Multi-Hole Probe (MHP) for 3D wind measurement—lighter weight and significantly lower cost than commercial alternatives. Integrated with vehicle sensors and state estimation algorithms for inertial wind calculation.

4. **Sensor Integration:** Field-swappable payload system with common power/data/mechanical interface enabling rapid sensor suite changes. Modular nose cone design for clean, uncontaminated atmospheric measurements with sensor protection.

5. **Flight Testing Approach:** Three primary test sites:
   - Pawnee National Grasslands (PNG): Low-altitude validation, sensor characterization
   - San Luis Valley (SLV): High-altitude (14,000 ft), turbulent, mountainous terrain validation
   - Turrialba Volcano (Costa Rica) or Volcanoes National Park: Final operational deployment

## Products & Capabilities Described

### SuperSwift XT
- **What it is:** Hand-launchable fixed-wing sUAS purpose-built for scientific payloads in harsh environments
- **Specifications:** 
  - Ceiling: 20,000+ ft above mean sea level (AMSL)
  - Endurance: Extended (specific duration not stated in Q7)
  - Payload capacity: Larger than Dragon Eye, comparable to or exceeding Vector Wing
  - Range: Longer than Vector Wing
  - Ruggedness: IP 63 rated sealing, ash particle protection, structural robustness for turbulence
- **Integration advantages:** Hand-launchable, field-maintainable, rapid payload swapping without specialized tools
- **Comparison:** Superior endurance and altitude capability vs. multi-rotor systems; more robust than typical small fixed-wing platforms; superior sensor integration vs. standard commercial airframes

### SwiftCore Flight Management System
- SwiftPilot (autopilot firmware and control algorithms)
- SwiftTab (tablet-based operator interface)
- **Phase II enhancements:** Automatic mission plan generation for volcanic profiling; terrain-following capability in mountainous areas; custom mission plan language for scientist-friendly flight definition

### Multi-Hole Probe (MHP)
- **What it is:** Custom-designed 3D wind sensor measuring aircraft-relative winds
- **Technical approach:** Combined with SwiftPilot sensors and state estimation algorithms to compute inertial winds
- **Advantages:** Much lower cost than existing commercial systems; lighter weight; validated through wind tunnel testing (Phase I and II)
- **Commercial partnership:** Being integrated into iMet XF sensor suite as commercial product

### Volcanic Profiling Payload
- **Gas sensors:** SO₂, CO₂, H₂S, CH₄ measurement capability
- **Particulate sensors:** Nephelometer for ash particle size and concentration; ash sampling capability
- **Atmospheric sensors:** Pressure, temperature, humidity (PTH); 3D wind via MHP
- **Ancillary:** EO and thermal imagery, forward video feed
- **Integration:** All sensors integrated into modular nose cone with field-swappable payload bay; synchronized data logging with autopilot telemetry and system time tagging

## Use Cases & Applications

### Primary Mission
**Volcanic Plume Monitoring:** In situ measurement of volcanic emissions for:
- Aviation safety (Volcanic Ash Advisory Centers support, VATD model validation)
- Volcano research (magmatic system dynamics, eruption forecasting)
- Environmental monitoring (ash dispersion, toxic gas concentration)

### NASA Potential Customers
- Tropospheric Chemistry Program (TCP)
- Applied Sciences Air Quality Program
- CALIPSO, Aura, CATS, OCO-2/3, Earth Ventures missions
- Atmospheric Composition, Carbon Cycle & Ecosystems, Weather focus areas

### Non-NASA Commercial/Government Applications
- **NOAA Wildfire Meteorology:** Incident Meteorologist (IMET) support; portable weather station replacement/augmentation for fire crew safety
- **NOAA Hurricane Meteorology:** Enhanced wind measurement for Coyote UAS; higher accuracy/resolution than Piccolo autopilot-only wind estimation
- **DOE, NSF, UCAR, NCAR:** Atmospheric research partnerships
- **National Weather Service:** Operational weather forecasting

## Key Results (Q7 Status)

### Physical Completion
- **Overall Progress:** 87.5% complete
- **Cumulative Costs:** $602,677.00 (as of March 19, 2019)

### Recent Technical Achievements

**Flight Certification (Task 2.0):**
- Volcanoes National Park: Flight Test Plan (FTP) submitted; awaiting AFSRB scheduling

**SuperSwift XT Aircraft (Task 3.0):**
- Ground testing validated critical S2 XT sealing against volcanic ash
- Final mechanical part completed: video camera wing pod design and build (sealed for ash protection)
- San Luis Valley flight campaign (ISARRA) data fully analyzed; converted to NetCDF format for shared access
- BST developed full toolkit for evaluating vehicle-borne wind sensor accuracy
- 2nd SuperSwift XT aircraft delivery pending

**Multi-Hole Probe (Task 4.0):**
- Wind tunnel testing completed for MHP validation
- Integration into modular nose cone designed based on Phase I CFD analysis
- Further wind tunnel testing planned for nose cone + MHP combination

**Sensor Integration (Task 5.0):**
- Lab testing and calibration of integrated sensor system
- Data analysis software development underway
- Data management plan in development

**Flight Testing Progress:**
- Pawnee National Grasslands: Aircraft validation flights completed; sensor validation flights conducted
- San Luis Valley: High-altitude and turbulent environment testing completed; data analysis finished
- Data quality validation in progress; sensors performing within expected parameters

### Quarterly Milestones Met (per Q7 report structure)
Quarters 1-6 milestones reportedly completed:
- Requirements finalized
- FAA/NASA flight approvals submitted
- SuperSwift XT CAD designs finalized
- Prototype ready for flight testing
- Sensor package integrated and validated
- SwiftTab operator interface finalized
- High-altitude flight testing completed at SLV
- 2nd SuperSwift XT ordered for manufacturing

## Notable Details

### Technical Innovations
- **MHP Design:** Custom 3D wind probe developed by BST; represents significant cost reduction vs. commercial alternatives; being commercialized through iMet partnership
- **Field-Swappable Payload Architecture:** Enables rapid sensor suite changes and mission flexibility without specialized tools
- **Terrain-Following Capability:** Advanced flight planning for difficult mountainous volcanic terrain
- **Sealed Airframe Design:** Purpose-built protection against corrosive volcanic ash (IP 63 rating)

### Regulatory/Approval Strategy
- Early engagement with NASA AFSRB/FRRB in Phase I; documentation ready for Phase II
- BST has successfully completed AFSRB/FRRB six times in two years
- First company to receive National Park flight approval under new FAA rules (Great Sand Dunes NP)
- Multi-site approval strategy: Pawnee National Grasslands → San Luis Valley → Turrialba/Volcanoes NP

### Operational Readiness
- Hand-launch capability enables deployment from remote volcanic sites
- Repair/replacement costs reasonable for high-risk applications
- Multiple aircraft deployment feasible with low-cost sUAS approach
- Rapid response capability for post-eruption data collection

### Commercialization Progress
- MHP integration into iMet XF sensor suite (commercial product)
- Design for Manufacturability (DFM) underway for cost reduction
- System positioned as turn-key solution for NASA and non-NASA customers
- Multiple organizations engaged for post-Phase II deployment

### Project Status Indicators
- On track for Turrialba Volcano (Costa Rica) deployment in Q7-Q8
- Backup site option: Volcanoes National Park (Hawaii)
- All flight test sites secured or in final approval stages
- Integration with subcontractors proceeding; no reported schedule conflicts
- Technical monitor: Dr. David Pieri (JPL volcanology expert)

### Data Management
- Flight data converted to NetCDF standard format
- Shared server infrastructure established for multi-team access
- Data analysis software toolkit developed for wind sensor validation
- Emphasis on proper data cataloging and archival for future use

This Q7 report documents a mature Phase II effort nearing completion with functional prototype systems ready for operational volcanic field deployment, establishing SuperSwift XT as a novel capability for NASA airborne science missions.