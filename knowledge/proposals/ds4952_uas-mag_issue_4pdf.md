# UAS-Mag™ High Performance DroneCAN Magnetometer

## Document Metadata
- Type: Product specification/datasheet
- Manufacturer: Bartington Instruments Ltd
- Document ID: DS4952/4
- Date: 2026-03-19
- BST Context: Referenced in Navy SBIR Phase II proposal on magnetometer systems (folder: [550] Navy/[550-1] Navy SBIR: Magnetometer/Phase II proposal)
- Last Editor: Beck Cotter

## Executive Summary
The UAS-Mag™ is a three-axis fluxgate magnetic field sensor designed for unmanned aircraft systems (UAS) with a DroneCAN digital communication interface. It provides high-performance magnetic field measurement in a lightweight, unpackaged form factor suitable for drone integration and payload applications.

## Product Description

### What It Is
- **Type:** 3-axis fluxgate magnetometer
- **Communication:** DroneCAN (UAVCAN) v1 protocol
- **Form Factor:** Unpackaged for system integration
- **Weight:** 25g
- **Dimensions:** 110 x 29 x 24mm
- **Connector:** JST-GH-4P

### Key Performance Specifications
- **Measuring Range:** ±105µT (±1.05 Gauss) ±5µT
- **Noise Floor:** ≤20pTrms√Hz @ 1Hz
- **Calibration Error:** <±0.5%
- **Linearity Error:** <0.02%
- **Zero Field Offset:** <±200nT
- **Perming (Magnetization Hysteresis):** <2nT at 1 x full-scale when powered
- **Orthogonality:** <±0.1°
- **Start-up/Settling Time:** <150ms
- **Warm-up Drift Time:** 15 minutes
- **Bandwidth at -3dB:** >300Hz

### Digital Output Capabilities
- **Data Rate:** 1 to 200 samples/second on all 3 axes simultaneously (50 samples/second default)
- **ADC:** 24-bit AD7767BRUZ-2
- **ADC Sample Rate:** 1MHz
- **ADC Output Rate:** 31.25kSPS
- **DroneCAN Data Types:** MagneticFieldStrength, MagneticFieldStrength2

### Electrical Specifications
- **Supply Voltage:** +4.5V to +15V DC
- **Current Consumption:** 60mA typical @ 5V
- **Analog Output Scaling:** 3V balanced differential (0.15 – 3.15V) / 100µT

## Axis Orientation
- **X-Axis:** +ve forward (Roll)
- **Y-Axis:** +ve starboard (Pitch)
- **Z-axis:** +ve down (Yaw)
- **Polarity:** +ve output when pointing North
- **Coordinate System:** Right Hand XYZ

## Environmental & Compliance
- **Operating Temperature:** -40°C to +85°C
- **Storage Temperature:** -40°C to +85°C
- **Compliance Standards:** BS EN 61326 & RoHS
- **Military Classification:** Dual-use (6a006a3)
- **ITAR:** No ITAR components

## Typical Applications
- Unmanned aircraft system navigation
- Compass functionality
- Payload magnetic field measurements

## Notable Details
- **Unpackaged Design:** Intended for direct integration into UAS platforms rather than standalone use
- **Adjustable Output Rate:** Selectable data rates from 1-200 samples/second accommodate different mission requirements
- **Low Power Consumption:** 60mA enables extended flight operations
- **Military Certification:** Dual-use classification and no ITAR components enable broader deployment
- **High Precision:** Sub-nanotesla zero-field offset and very low perming error indicate suitability for precision navigation