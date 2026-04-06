# SwiftFlow™ 3D Multi-Hole Probe Datasheet

## Document Metadata
- Type: Product datasheet
- Client/Agency: BAE Systems (via DARPA Albatross subcontract RFP)
- Program/Solicitation: DARPA Albatross
- Date: 2024 (created/modified December 10, 2024)
- BST Products/Systems Referenced: SwiftFlow™ 3D wind probe
- Key Personnel: Beck Cotter (last editor)

## Executive Summary
The SwiftFlow™ is a tightly integrated 3D multi-hole probe and wind velocity measurement device designed specifically for UAS deployments. It combines differential pressure measurements with magnetometer and IMU data processed through fusion algorithms to deliver comprehensive wind vector solutions, measuring air speed, altitude, angle-of-attack, side-slip, temperature, and humidity.

## Technical Approach
The SwiftFlow integrates three core sensor types with fusion algorithms:
- **Multi-hole pressure ports**: Barometric (10-1200 hPa), side port differential (-249 to +249 Pa), and center port absolute (0-1244 Pa) pressure measurements
- **Inertial Measurement Unit (IMU)**: 3-axis rotation rates, 3-axis accelerations
- **Magnetometer**: 3-axis magnetic field measurement
- **GNSS**: GPS position and velocity data with separate sensor module

Data fusion across these sensors produces derived wind parameters (true airspeed, indicated airspeed, angle-of-attack, side-slip).

## Products & Capabilities Described

### SwiftFlow™ 3D Wind Probe
**What it is**: A compact, integrated aerodynamic measurement probe for small aircraft and UAS platforms.

**Specifications**:
- **Data Interface**: 5V TTL UART at 921,600 baud
- **Power**: 5-8.4V input
- **Operating Temperature**: -20°C to +60°C
- **Data Rate**: 100 Hz
- **Weight**: 144 g (probe), 37 g (GNSS module)
- **Size**: 0.515m × 0.051m × 0.04m (probe); 0.016m × 0.054m × 0.054m (GNSS)

**Performance Specifications**:
| Parameter | Range | Resolution | Accuracy |
|-----------|-------|-----------|----------|
| Barometric Pressure | 10-1200 hPa | 0.012 hPa | ±1.5 hPa |
| Side Port Pressure | -249 to +249 Pa | 0.03038 Pa | ±2.49 Pa |
| Center Port Pressure | 0-1244 Pa | 0.07594 Pa | ±6.22 Pa |
| Temperature | -40°C to +85°C | 0.1°C | ±0.3°C |
| Relative Humidity | 0-100% | 0.1% | ±3% @ 21°C |
| Rotation Rate | -250 to +250 °/sec | 0.008 °/sec | ±0.006 °/sec |
| Acceleration | -8 to +8 g | 0.0002 g | ±0.16 g |
| Magnetic Field | -1100 to +1100 µT | 0.013 µT | ±0.015 µT |
| Time | — | 0.2 sec | ±3.00E-08 sec |
| Horizontal Position | — | 0.00001 m | ±2.5 m |
| Vertical Position | — | 0.003 m | ±2.5 m |
| Velocity | 0-514 m/s | 0.01 m/s | ±0.05 m/s |
| IAS (Indicated Airspeed) | 0-45 m/s | — | ±0.06 m/s |
| TAS (True Airspeed) | 0-45 m/s | — | ±0.14 m/s |
| Dynamic Pressure (Q) | 0-1244 Pa | — | ±2.78 Pa |
| Angle of Attack (α) | -15° to +15° | — | ±0.25° |
| Side-Slip (β) | -15° to +15° | — | ±0.25° |

**Data Output**: Raw sensor streams for all pressure ports, temperature, humidity, IMU (rotation rates and accelerations), magnetometer, GPS time/position/velocity.

## Use Cases & Applications
- UAS wind environment characterization
- Aircraft performance evaluation
- Atmospheric profiling missions
- High-altitude and extreme-environment operations (design for -40°C minimum operating point suggests cold-weather/Arctic capability)

## Notable Details
- **UAS-Optimized Design**: Explicitly designed for unmanned aircraft systems with compact footprint and low weight
- **Modular GNSS**: Separate GNSS sensor module allows flexible integration
- **Comprehensive Fusion Approach**: Combines pressure, inertial, and magnetic data to derive wind vectors rather than relying on pressure measurement alone
- **High Data Rate**: 100 Hz output supports dynamic flight regimes
- **Low Power**: 5-8.4V operational range suitable for battery-powered UAS