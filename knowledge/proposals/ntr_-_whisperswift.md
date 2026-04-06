# WhisperSwift Aircraft (NTR)

## Document Metadata
- **Type:** New Technology Report (NTR)
- **Client/Agency:** NASA Goddard Space Flight Center
- **Program/Solicitation:** NASA SBIR Phase II-E; Contract NNX14CG09C; WBS 939869.03.06.02 (S3.05-8971 Soil Moisture Mapping sUAS)
- **Date:** Submitted January 2017 (document created/modified Jan 8-9, 2017; development completed Dec 2016)
- **BST Products/Systems Referenced:** WhisperSwift, SuperSwift, Tempest (predecessor aircraft)
- **Key Personnel:** Maciej Stachura (overall design, EMI cases, aircraft shielding), Cory Dixon (aerodynamic design and new propeller), Jack Elston (mechanical design), Geoff Bland (NASA COTR, initial planning and feedback)

## Executive Summary
The WhisperSwift is a radio-quiet modification of the SuperSwift small unmanned aircraft system (sUAS) designed to enable accurate L-band radiometer measurements for soil moisture mapping. The innovation systematically shields all RF-emitting components (motor, battery, speed controller, wiring) and houses payloads in lightweight Faraday-cage-style containers, creating a clean RF environment necessary for sensitive radiometer operations without the electromagnetic interference that plagued earlier electric-powered sUAS platforms.

## Technical Approach

### Core Problem Addressed
Electric-powered sUAS generate significant RF noise at L-band frequencies, interfering with L-band radiometer operation for soil moisture mapping. Prior ad-hoc shielding approaches (Tempest and early SuperSwift) worked but were heavy, unreliable, and difficult to reproduce.

### Two-Part Shielding Strategy

**1. Payload Shielding ("Shoebox" Design)**
- Lightweight, modular pressure-fit sheet metal containers housing radiometer, computer boards, and data loggers
- Manufactured via waterjet cutting and bending (scalable, accessible fabrication)
- Single-piece walls bent 90° at three corners, soldered at fourth
- Spring-loaded lids with 0.3" tabs and 0.075" gaps between tabs (~1 cm periodicity) designed to block radiation up to ~4 GHz (lambda/8 spacing) and prevent sidelobe interference
- Weight reduction: ~2 lbs (from 5 lbs to 3 lbs for SMM payload)
- Enables easy board access, field swapping of cases, and modular stacking

**2. Aircraft RF Emission Mitigation**
- **Battery/Fuselage:** Copper mesh (rather than solid sheet) bonded to fiberglass fuselage with epoxy; mesh improves airflow for cooling while reducing weight vs. Phase II solid shielding
- **Motor (primary EMI source):** Cowling with interior copper mesh glued to ground; motor opening < 1" in all dimensions to eliminate L-band noise escape; copper backplane fully encloses motor except propeller shaft opening
- **Wiring:** All ESC and power system connections wrapped with shielded copper braid (also improves cable durability and appearance vs. unshielded braid)

### Design Rationale
The shoebox design uses proven radio fabrication principles (standard for decades) based on Faraday cage principles with optimized gap spacing. Copper mesh over solid shielding reduces weight while maintaining effectiveness through proper grounding and epoxy sealing.

## Products & Capabilities Described

### WhisperSwift Aircraft
- **What it is:** Radio-quiet 10-foot wingspan electric-powered small unmanned aircraft system based on the SuperSwift platform
- **Key specifications:**
  - 10 foot wingspan
  - Electric propulsion
  - Modular airframe with removable nose cone for payload accommodation
  - Designed for operation in unimproved areas
  - All electronic components shielded and grounded
- **Use in this context:** Primary platform for L-band radiometer soil moisture mapping; RF environment clean enough for accurate L-band measurements
- **Unique capability:** Removable nose cone allows field-swappable payloads and easy external tuning/maintenance of instruments

### SuperSwift (Base Platform)
- Parent airframe providing modular architecture; this NTR documents its modification to WhisperSwift

## Use Cases & Applications

### Primary Mission
- **Soil Moisture Mapping:** L-band radiometer measurements for hydrological and agricultural monitoring; enables detection of water-soil saturation for flood prediction

### Commercial Applications
- **Precision Agriculture:** Working with agronomists to reduce water usage in agriculture using soil moisture data
- **Water-Soil Saturation Mapping:** Flood prediction applications
- **Soil Integrity Assessment:** Combined with other sensing technologies
- **Other Radiometer/Radar Missions:** Any application requiring a radio-quiet aircraft platform for sensitive RF-based sensors
- **Wireless Communication Research:** Clean RF environment useful for communication system testing

## Key Results

### Development Timeline
- **03/01/2016:** Initial discussions and planning
- **03/15/2015:** Phase II-E proposal writing with implementation plan
- **06/15/2016:** First modifications and EMI testing
- **10/01/2016:** Payload cases for EMI shielding completed
- **11/10/2016:** Aircraft EMI mitigation completed
- **12/12/2016:** Lab testing of EMI completed (successful operational test at CET)

### Verification
- Prototype design and testing completed; first successful operational test conducted November 2016
- EMI shielding effectiveness validated through lab testing

### Weight Performance
- SMM payload weight reduction of ~2 lbs (40% reduction from 5 lbs to 3 lbs)

## Notable Details

### Design Innovation
- Shoebox containers represent a more manufacturable, scalable approach than previous ad-hoc shielding; uses standard machine shop capabilities (waterjet cutting, bending, soldering)
- Copper mesh approach selected over solid shielding for weight, bonding ease, airflow, and protective epoxy covering
- Tab/gap spacing design (0.3" + 0.075" = ~1 cm) uses proven RF design principles to eliminate sidelobe interference up to 4 GHz

### Technology Readiness Level
- **State:** Modification and Used in Current Work (prototype stage completed; operational testing successful)
- **Significance:** Substantial Advancement in the Art (systematic, repeatable RF shielding solution vs. previous ad-hoc approach)

### Partnership & Stakeholder Involvement
- **NASA COTR:** Geoff Bland (Goddard Space Flight Center)
- **BST Technical Rep:** Jack Elston
- Commercial collaboration with agronomists for precision agriculture applications

### Competitive Advantage
- Enables reliable, reproducible soil moisture measurements with electric sUAS (previously difficult due to RF noise)
- Modular design allows field swapping and easy payload reconfiguration
- More lightweight and manufacturable than previous shielding approaches
- Opens door to other clean-RF applications (radar, radiometer, communications research)

### Patent Status
No prior patents or patent applications listed.