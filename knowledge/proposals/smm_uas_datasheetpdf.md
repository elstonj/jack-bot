# Soil Moisture Mapping sUAS Datasheet

## Document Metadata
- Type: Product/capability datasheet
- Client/Agency: Center for Environmental Technology (CET); Colorado Advanced Industries
- Program/Solicitation: NASA SBIR (sUAS integration phase)
- Date: March 2, 2015
- BST Products/Systems Referenced: SwiftCore, SwiftPilot, SwiftStation, SwiftTab, SuperSwift aircraft platform
- Key Personnel: Dr. Al Gasiewski (collaboration partner mentioned); team with 30+ years sUAS experience noted

## Executive Summary
Black Swift Technologies offers an integrated soil moisture mapping sUAS combining a passive L-band microwave radiometer with their SwiftCore avionics system to provide volumetric soil moisture measurements at 15m resolution and 5-20cm depth. The hand-launched system covers 1-2 km² per hour and is available as a turnkey solution with existing FAA and NASA approvals for U.S. operations.

## Technical Approach
The system integrates a calibrated passive L-band microwave radiometer sensor with:
- Precision GPS (10 Hz, raw measurements, <1m accuracy)
- High-rate IMU (100 Hz attitude updates, 9 DOF, 1 kHz sampling)
- Differential and static pressure sensing
- NDVI sensor (near-infrared and red wavelength, nadir and zenith)
- Thermal imaging (surface temperature)

Flight control via SwiftCore avionics provides real-time telemetry (10 Hz) through tablet/mobile interface (Swift Tab), enabling precision low-altitude operations for accurate soil moisture mapping.

## Products & Capabilities Described

### SwiftCore™ Flight Management System
- Integrated avionics solution consisting of SwiftPilot, SwiftStation, and SwiftTab
- Designed specifically for small UAS (<50 lbs)
- Fully customizable and field-tested in FAA-approved operations
- Includes guide for FAA COA applications

### SwiftPilot™
- 50-gram flight management autopilot
- Dimensions: 6.7 × 4.0 × 1.8 cm
- Dual 168 MHz Cortex-M4 processors with FPU
- Multiple interfaces: CAN, UART, I2C, SPI, Ethernet, USB, GPIO
- Gumstix Overo (1 GHz Cortex-A8) onboard payload computer for customer use
- Included software SDK

### SwiftTab™
- Mobile ground control station (tablet/phone form factor)
- Android-based with gesture and multi-touch interface
- 10 Hz telemetry reception

### SuperSwift™ Aircraft Platform
- Empty weight: 3.4 kg
- Nominal payload capacity: 1.4 kg (maximum 2 kg)
- Cruise speed: 18 m/s
- Maximum speed: 25 m/s
- Endurance: 90 minutes with payload
- Range: 100 km maximum; 10 km standard communication range
- Features: Hand-launch, laser-guided autoland, operations from unimproved surfaces
- Full autonomous capability
- Custom nose cone available up to 65 cm length for payload accommodation
- Field-swappable payload nose cone

### Soil Moisture Sensor Suite
- **L-band Microwave Radiometer**: Passive measurement at 15m resolution from 15m altitude; penetration depth 5-20 cm
- **NDVI Sensor**: Nadir and zenith measurement of near-infrared and red wavelengths
- **Thermal Imaging**: Surface temperature measurement

## Use Cases & Applications
- Agricultural soil moisture mapping without infrastructure requirements
- Scientific Cal/Val (calibration/validation) bridge between manned aviation and in situ sensors
- Data collection over difficult terrain and high-variance areas
- Agricultural plot-scale operations

## Coverage Performance
- **15m resolution**: 1 km² (247 acres) per hour
- **30m resolution**: 2 km² (494 acres) per hour

## Operational Status & Availability
- Existing FAA and NASA approvals for U.S. operations
- Data collection service available through experienced team (30+ years sUAS experience as of April 2015)
- Turnkey system availability planned for Fall 2015
- Sole-source acquisition available through existing contract mechanism

## Notable Details
- **Heritage**: Initial development funded by NASA fellowship; sUAS integration funded by NASA SBIR with collaboration from Dr. Al Gasiewski
- **Competitive positioning**: Described as "small, accurate, mission-focused" solution
- **Operational experience**: Team had existing FAA and NASA approvals at time of publication
- **Software**: Includes Swift Pilot™ software SDK for customization
- Company address: 3080 Valmont Rd, Ste 259, Boulder, CO 80301
- Document notes this as a complete, integrated ecosystem (system/sensor/service/approvals/product)