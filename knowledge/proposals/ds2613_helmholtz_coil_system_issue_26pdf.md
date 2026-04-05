# DS2613 Helmholtz Coil System Issue 26

## Document Metadata
- Type: Product brochure/technical specification sheet
- Manufacturer: Bartington Instruments Ltd (Witney, Oxford, England)
- Document Code: DS2613/26
- BST Context: Referenced in Navy SBIR Phase II proposal on Magnetometer project (Bartington supplier)
- Last Editor: Beck Cotter
- Date: 2026-03-19

## Executive Summary
This is a technical specification brochure for Bartington Instruments' Helmholtz Coil Systems (HC1®, HC2®, and HC16 models), used for calibrating magnetic field sensors and creating controlled magnetic environments. The document details three coil sizes with supporting amplifier and control electronics, applicable to Black Swift's Navy SBIR magnetometer development work.

## Products & Capabilities Described

### HC1® Helmholtz Coils
- **Specification**: 500mm nominal diameter, 3-axis coil system
- **Performance**:
  - Maximum DC field (X-axis): 706 μT continuous
  - Homogeneous area: 8 cm diameter sphere (<0.1% error); 15 cm diameter sphere (<1% error)
  - Orthogonality error: <0.1° (adjustable to <0.05° with PA1)
  - Parallelism: <1°
- **Electrical**: 10 turns per coil, Field/Current Ratios: 35.3 μT/A (X), 32.2 μT/A (Y), 29.1 μT/A (Z)
- **Coil resistance**: <0.2Ω per axis
- **Operating temperature**: +15°C to +30°C
- **Weight**: 43 kg
- **Connectors**: Neutrik Speakon 8-Way NL-8-FC

### HC2® Helmholtz Coils
- **Specification**: 1000mm nominal diameter, square profile, 3-axis, flat-pack assembly
- **Performance**:
  - Maximum DC field (Y-axis): 446 μT continuous
  - Homogeneous area: 13.6 cm cube (<0.1% error); 24 cm cube (<1% error)
  - Orthogonality error: <0.1° (adjustable to <0.05° with PA1)
  - Parallelism: <±1°
- **Electrical**: 14 turns per coil, Field/Current Ratios: 20.5 μT/A (X), 22.3 μT/A (Y), 19 μT/A (Z)
- **Coil resistance**: 0.36–0.44Ω per axis
- **Operating temperature**: +15°C to +30°C
- **Weight**: 130 kg
- **Connectors**: Neutrik Speakon 4-Way NL-4-MP (coils), 8-Way NL-8-FC (harness)

### HC16 Helmholtz Coils
- **Specification**: 270–370mm nominal diameter, 3-axis, compact plastic coil former
- **Performance**:
  - Maximum DC field (Z-axis): 2.8 mT continuous (highest field capability)
  - Homogeneous area: 40 mm diameter sphere (<0.1% error); 65 mm diameter sphere (<1% error); 100 mm diameter sphere (<5% error)
  - Orthogonality error: <0.1° (adjustable to <0.05° with PA1)
  - Parallelism: <±1°
- **Electrical**: 22 turns per coil, Field/Current Ratios: 106 μT/A (X), 122 μT/A (Y), 144 μT/A (Z)
- **Coil resistance**: 0.114–0.158Ω per axis
- **Operating temperature**: +15°C to +50°C (wider range than HC1/HC2)
- **Weight**: 10 kg
- **Connectors**: 4 mm sockets (coils), Neutrik Speakon 8-Way NL-8-FC + 4 mm plugs (harness)

### PA1 Power Amplifier
- **Function**: Supplies current to Helmholtz coil assemblies; applies DC offset to cancel ambient magnetic field
- **Electrical**:
  - Input: 100–240V AC, 50/60Hz
  - Maximum power consumed: 1.5 kW
  - Control input: ±10V
  - Coil drive output: ±25V (no load)
  - Maximum total output current: 29A (max 20A per axis)
  - Output impedance per axis: 1.35Ω
  - Current monitor output: ±15V
- **Mechanical**: 6U 19-inch rack mount, 27 cm H × 51 cm W × 60 cm D, 50 kg
- **Environmental**: +15°C to +30°C operating; fan-cooled with self-resetting thermal shutdown; indoor only, max 2000 m altitude
- **Features**: Electronic adjustment of scaling and orthogonality; DC offset current capability

### CU1 Control Unit
- **Function**: Interface between PA1 and National Instruments–based control systems
- **Inputs**:
  - Two magnetometer/auxiliary sensor inputs (compatible with Bartington sensors, ±10V differential/single-ended)
  - Current sense inputs (up to three axes, ±10V differential)
- **Outputs**:
  - PA1 drive signal (±10V differential)
  - Two NI DAQ interfaces (2 × 68-way Harting connectors)
- **Filters**: Butterworth 2-pole 12 dB/octave low-pass, software-selectable at 10 kHz, 1 kHz, 100 Hz, 10 Hz
- **Power supply**: 0 to ±20V programmable magnetometer supply (100 mA max); ±15V auxiliary (50 mA per channel)
- **Mechanical**: 1U 19-inch rack mount, 2.4 kg
- **Environmental**: +10°C to +30°C operating; indoor only, max 2000 m altitude
- **Cable limits**: 10 m (sensor), 3 m (current sense & PA1 output)

### CU2 Closed-Loop Module (with Reference Magnetometer)
- **Function**: Active compensation for external DC and AC magnetic field variations
- **Performance**:
  - DC disturbance field attenuation: -46 dB ±1 dB
  - Zero field DC drift over 6 hours: <100 nT
  - System noise: <3 nT peak-to-peak
  - Bandwidth: DC to 12 Hz (-3 dB) for HC1/HC2/HC16; DC to 4 Hz for BH1300 series
  - Reference magnetometer range: ±500 μT
  - Reference magnetometer scaling: 20 mV/μT (±10V full scale)
- **Adjustments**:
  - Orthogonality error: ±1° nominal
  - Gain: ±10% nominal
  - Offset: ±800 nT nominal
- **Environmental**: +10°C to +50°C operating; warm-up time 30 min; IP20 rating
- **Mechanical**: 
  - CU2 Module: 106.1 × 57.6 × 143.8 mm, 430 g
  - Reference Magnetometer: 25 × 23.4 × 73 mm (excluding cable), 320 g
  - Mounting: 4 × M2.5 tapped holes on reference magnetometer; mounting accuracy <±10° to Helmholtz coils
- **Compatibility**: Only works with 3-axis coils; powered by CU1 auxiliary ±15V supply

## System Compatibility & Performance

**HC1® + PA1 Compatibility**:
- Maximum DC field (single axis): >±500 μT
- Maximum AC field (single axis): >±100 μT at 3 kHz
- DC field compensation: >±80 μT
- Corner frequency: 100 Hz

**HC2® + PA1 Compatibility**:
- Maximum DC field (single axis): >±250 μT
- Maximum AC field (single axis): >±100 μT at 300 Hz
- DC field compensation: >±45 μT
- Corner frequency: 20 Hz

**HC16 + PA1 Compatibility**:
- Maximum DC field (single axis): >±1 mT
- Maximum AC field (single axis): >±100 μT at 5 kHz
- DC field compensation: >±80 μT
- Corner frequency: >100 Hz
- All axes driven simultaneously: 1 mT DC target; 1 mT peak <440 Hz AC target
- Maximum frequency: 5 kHz
- Field at max frequency (largest diameter axis, all driven): 110 μT peak

## Typical Applications
- Calibration of three-axis magnetic field sensors
- Creation of known magnetic environments for testing

## Accessories
- **Sensor for Setup/Recalibration**: Bartington Mag-13MS recommended for final verification and periodic calibration
- **Sensor Mounting Accessories**: Tables (HC1®, HC2®) or pillars (HC16) to position sensors at homogeneous volume center
- **Helmholtz Coil Breakout Box**: Real-time voltage and current monitoring between coils and PA1 on each axis

## Notable Details

1. **Regulatory Compliance**: All units compliant with FCC and CE approvals; cable length limits specified to maintain compliance
2. **National Instruments Integration**: Full software control capability via NI DAQ cards (USB-6363 mentioned as standalone option)
3. **Flat-Pack HC2®**: Delivered in flat-pack form for freight efficiency and customer assembly convenience
4. **Extended Range HC16**: Smallest coil (10 kg) produces highest field (2.8 mT) and operates at widest temperature range (+15°C to +50°C), making it suitable for diverse applications
5. **Ferronato Compatibility**: Larger third-party Helmholtz coils (1.3 m, 2 m diameters) also compatible with described control system
6. **Thermal Protection**: PA1 includes self-resetting thermal shutdown
7. **Manufacturing**: Bartington Instruments, Witney, Oxford (UK); established supplier with registered trademarks in 20+ territories

## Context for Black Swift Technologies
This specification document supports BST's Navy SBIR Phase II proposal on magnetometer development. The Helmholtz coil systems provide essential test and calibration infrastructure for magnetometer sensor development, validation, and qualification—likely critical to demonstration and verification activities for Navy magnetometer applications.