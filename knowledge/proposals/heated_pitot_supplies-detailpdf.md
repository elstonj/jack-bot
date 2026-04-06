# Heated Pitot / ADS-B Supplies Detail

## Document Metadata
- Type: Budget justification / component sourcing detail
- Client/Agency: NASA (NOAA/ATDD)
- Program/Solicitation: 2016 SBIR Phase III - Volcano monitoring
- Date: December 2021 - January 2022
- BST Products/Systems Referenced: S2 UAS, SwiftStation Ground Station, Air Data Board (Pitot board)
- Key Personnel: Jack Elston (last editor), Joshua Fromm (BST purchasing contact), Edward Dumas (NOAA recipient)

## Executive Summary
This document details the component-level bill of materials and sourcing for a heated pitot tube and ADS-B (Automatic Dependent Surveillance-Broadcast) receiver system, likely for integration into BST's S2 UAS platform for the NASA volcano monitoring project. The total component cost was $801.00 for the assembled system.

## Technical Approach
The heated pitot system was assembled from off-the-shelf and custom components:
- **3D-printed housing** (Shapeways): Custom enclosure for the pitot assembly
- **Metal pitot tip** (Shapeways): 3D-printed aluminum heated tip with TPU insert for thermal management
- **BST MHP (Air Data Board)**: Custom PCB-based airspeed/air data sensing board ($181.00)
- **EE03 Humidity/Temperature Sensor** ($130.00): E+E Elektronik EE03-M1C1 with M1C1 sensor coating, 4 units ordered
- **Voltage regulator and power switch**: Support components
- **uAvionix ADS-B receiver** ($350.00): For transponder data integration

## Products & Capabilities Described

### BST Air Data Board (MHP - Pitot Board)
- Type: Custom avionics PCB for airspeed and air data measurement
- Application: Integrated into S2 UAS for accurate airspeed sensing
- Cost: $181.00 per unit (Invoice 1479)
- Associated services: Installation/replacement labor charged at $125/hour

### S2 UAS Platform
- Referenced in context of maintenance and upgrades (servo replacement, diagnostics)
- Equipped with Hacker DITEX 0606 servos in wings/tails
- Supported by SwiftStation ground control system

### SwiftStation Ground Station
- GCS control board and face plate mentioned
- Warranty coverage for replacement components noted

## Use Cases & Applications

**Primary Application:** Volcano monitoring mission under NASA 2016 SBIR Phase III contract
- Heated pitot tube enables airspeed measurement in volcanic ash and challenging atmospheric conditions
- ADS-B receiver integration for air traffic awareness/coordination
- Potential for measurement of atmospheric parameters (temperature, humidity) in harsh environments

## Notable Details

1. **Component sourcing approach**: BST utilized both custom 3D-printed parts (Shapeways) and commercial off-the-shelf avionics (uAvionix ADS-B, E+E Elektronik sensors)

2. **Multi-unit ordering**: EE03 temperature/humidity sensors ordered in quantity of 4 ($555.00 total from supplier), suggesting system redundancy or multiple platform deployment

3. **BST manufacturing capability**: Document shows BST performs in-house maintenance, refurbishment, diagnostics, and installation services

4. **Invoice details** (Invoice 1479 from 12/30/2021):
   - Servo replacement labor on S2 airframe (S20007)
   - Pitot board replacement (0.5 hours labor)
   - GCS repairs and component replacement
   - Warranty coverage applied to most line items; customer charged $263.92 net after discount

5. **Timing**: Equipment ordered and shipped January 2022 for what appears to be Phase III volcano monitoring project completion/delivery

6. **Thermal design consideration**: TPU (thermoplastic polyurethane) insert in pitot tip suggests thermal isolation/protection for heated sensing elements