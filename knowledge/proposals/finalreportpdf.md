# Data Acquisition System for MultiSpectral Remote Sensing

## Document Metadata
- Type: Master's thesis / technical report
- Client/Agency: Colorado State University (CSU) - Soil and Irrigation Department / CSU Extension Service
- Program/Solicitation: Not applicable (academic project)
- Date: May 4, 2015
- BST Products/Systems Referenced: Tempest UAV (manufactured by UASUSA, not BST)
- Key Personnel: Anshuman Rajwar (author); Advisors: Prof. Dr. Anura Jayasumana, Prof. Dr. J. Rockey Luo; Committee: Prof. Dr. Indrajit Ray; Contributors: Amandeep Vashisht, Jeff Hathaway, Emily Kullberg, Cody Remington, Alex Kenyon (UASUSA), Del Nantt (Cropscan Inc.), Dr. Stefan Thamke (TE-AX)

## Executive Summary
This master's thesis documents the design and implementation of a lightweight, power-efficient data acquisition system (DAS) for airborne multispectral remote sensing. The DAS was designed to operate on the Tempest UAV and integrates multiple sensors (multispectral radiometer, thermal camera, digital camera, temperature sensor, GPS) with a Beaglebone Black single-board computer as the control hub. The system was successfully deployed and used by CSU's Soil and Irrigation Department to monitor water consumption in crops.

## Technical Approach

### Hardware Architecture
- **Central Controller**: Beaglebone Black (1 GHz ARM Cortex A8, 512 MB RAM, 4 GB storage, expandable to 32 GB via SD card; cost ~$55)
  - 46 GPIO pins, USB 2.0, 4 UART buses, 1 SPI, 1 I2C, 8 PWM outputs
  - Provides 5V power distribution to connected devices

### Sensor Integration & Signal Conditioning
- **MSR5 Multispectral Radiometer** (Cropscan): Measures reflectance at five wavelengths (485, 560, 660, 830, 1650 nm); outputs 11 analog voltages (upward and downward sensors for each wavelength plus internal temperature)
  - Interfaced via custom ADC circuit: AD7490 16-channel ADC (12.5 mW max power, 1 MSPS throughput, 16 clock cycles per conversion)
  - AD780 precision voltage reference (2.5V) with decoupling capacitors (0.01 µF and 0.1 µF)
  - SPI0 communication with Beaglebone Black

- **IRt/c Temperature Sensor** (Exergen IRt/c.5): Measures –40°C to 120°C; outputs 0–1.511 mV
  - Amplification required due to low output voltage; implemented LMP2021 zero-drift, low-noise EMI-hardened amplifier
  - Non-inverting amplifier configuration with gain of 1001 (resistors: 1 kΩ and 1 MΩ)
  - Single 5V supply; output fed to ADC channel 4

- **FLIR Tau2 640 Thermal Camera** (uncooled thermal imaging core) + ThermalCapture module (TE-AX)
  - Mini-USB power and configuration
  - Snapshot triggered by grounding pin 2
  - On-board storage with integrated GPS data logging capability
  - Powered by separate battery; Beaglebone provides trigger signal only

- **ADCSnap Multispectral Camera**: Lightweight with on-board storage
  - Triggered via LOW-true SHUTTER pin connected to Beaglebone GPIO pin 30 (header 9)

- **Sony Alpha A6000 Digital Camera** (50 mm lens): Mirrorless camera
  - Powered by internal battery
  - IR remote shutter trigger controlled by Beaglebone PWM (pin 14, header P9)

- **GPS Module** (Adafruit Ultimate GPS Breakout Board): 5V supply, UART4 communication
  - Provides GPGGA and GPRMC NMEA sentences
  - Used to set Beaglebone system clock on startup

### Circuit Design
- Power management: All devices powered from Beaglebone 5V pins (capable of 2A; actual draw <10mA)
- ADC configuration: AD7490 with VDrive (3.3V from Beaglebone) and Vref (2.5V from AD780)
- Analog signal path: MSR5 and IRt/c → AD7490 (16 channels total, 12 used)
- MSR-to-ADC pin mapping provided via DB25 connector and 26-pin header
- Additional trigger outputs: GPIO pins P9_30 and P8_10 for ADCSnap and ThermalCapture

## Products & Capabilities Described

### Beaglebone Black Single-Board Computer
- **Function**: Central control and data logging platform
- **Specifications**: 1 GHz ARM Cortex A8, 512 MB RAM, 4 GB onboard storage (expandable to 32 GB)
- **Use in DAS**: Orchestrates all sensor timing, manages multithreaded data acquisition, controls analog-to-digital conversion via SPI, sets system time from GPS, triggers camera shutters via PWM and GPIO
- **Advantages cited**: Low power consumption, versatility, reasonable cost ($55)

### AD7490 16-Channel ADC
- **Specifications**: 12-bit resolution (1.2 mV per step), 1 MSPS throughput, 16 clock cycles per conversion, 12.5 mW max power
- **Use**: Digitizes 11 MSR5 analog outputs and 1 IRt/c amplified output; SPI interface (SPI0)
- **Performance**: Max conversion rate determined by SPI clock frequency (no fixed sampling requirement for MSR5)

### AD780 Precision Voltage Reference
- **Specifications**: 2.5V output, provides stable reference for AD7490; requires 0.01 µF and 0.1 µF decoupling capacitors
- **Use**: Establishes measurement range and accuracy for ADC

### LMP2021 Amplifier
- **Specifications**: Zero-drift, low-noise, EMI-hardened; input offset drift 0.004 µV/°C (max) / 0.02 µV/°C (typical); input bias current 25 pA; SOIC package
- **Use**: Amplifies low-voltage IRt/c output (0–1.511 mV) to range compatible with ADC; gain = 1001
- **Configuration**: Single 5V supply, non-inverting amplifier topology

## Software Architecture

### Programming Languages & Tools
- **Python**: Main control logic, multithreading for concurrent sensor management
- **C**: Fast SPI-based data acquisition (msr_spi.c) for time-critical ADC communication
- **SWIG**: Tool to wrap C code as Python library
- **Libraries**: Adafruit BBIO (GPIO/PWM/UART control), BBBio lib (C library for Beaglebone GPIO)

### Software Modules

**Main.py** (Initialization & Control)
- GPS initialization: Reads GPGGA and GPRMC NMEA sentences, waits for GPS fix
- System clock synchronization using GPS data via `date` command
- 900-second pre-flight delay before sensor activation
- Spawns and manages sensor threads (MSRThread, ADCSnap, A6000, FLIR, GPSLog)
- Monitors user input for graceful shutdown; joins all threads on exit
- Sets GPIO pin P8_10 as control flag for msr_spi.c polling loop

**msr_python.py** (MSR5 Control Thread Class)
- Wraps msr_spi.c C module via SWIG
- Calls getVolt() method repeatedly to acquire MSR5 data

**msr_spi.c** (Core ADC Driver - C Module)
- **transfer()**: Low-level SPI communication; sends 16-bit values to AD7490, receives digitized results via ioctl
- **createFile()**: Opens timestamped file for data logging at experiment start
- **getReading()**: Retrieves ADC values, calculates channel number and voltage; writes comma-separated CSV data with timestamp at end of each channel cycle
- **getVolt()**: High-level API for Python; handles SPI and AD7490 initialization (requires 2 dummy 16-bit reads before control register setup and sequencer configuration), then loops polling until P8_10 pin goes LOW
- Output format: DAT file compatible with existing MSR processing software

**GPSLog.py** (GPS Logging Thread Class)
- Sets up UART4 communication at 9600 baud
- Logs all GPGGA and GPRMC sentences to GPSLOG.txt (append mode)
- Runs until join() is called

**A6000.py** (Sony Camera Control Thread Class)
- Uses Adafruit BBIO.PWM on pin P9_14
- IR trigger pulse width: 2 ms (snapshot) / 1.5 ms (idle)
- PWM frequency: 50 Hz, 10% duty cycle
- Logs snapshot timestamps to A6000Log.txt for later correlation with captured images
- Runs until join() is called (stops PWM signal)

**ADCSnap.py** (Tetracam Control Thread Class)
- Controls GPIO pin P8_14 connected to SHUTTER (LOW-active trigger)
- Generates snapshot trigger pulses
- Runs until join() is called

**FLIR.py** (Thermal Camera Control Thread Class)
- Controls GPIO pin for trigger input (LOW-active)
- Keeps trigger grounded for continuous video recording
- Runs until join() is called

### Data Output Formats
- **MSR5 data**: CSV file (channel, voltage, timestamp) created with current time as filename; compatible with legacy MSR processing software
- **GPS**: NMEA sentences logged to GPSLOG.txt
- **Camera timestamps**: A6000Log.txt contains snapshot trigger times for post-flight correlation

## Use Cases & Applications

### Primary Application: Precision Agriculture - Water Management
- **Objective**: Accurate estimation of crop water consumption and irrigation efficiency over large areas
- **Methodology**: Airborne multispectral remote sensing to measure crop reflectance at multiple wavelengths; temperature measurements to infer water stress
- **Deployment**: Installed on Tempest UAV for flights over agricultural fields
- **Client**: Colorado State University Soil and Irrigation Department (successful operational deployment)

### Sensors Enable:
- Multispectral vegetation indices (NDVI, etc.) via 5-wavelength radiometer
- Thermal imaging for crop canopy temperature and water stress detection
- High-resolution RGB imagery (via A6000)
- Tetracam multispectral camera imagery
- Precise geolocation via GPS for data correlation

## Key Results

The thesis is a technical design and implementation report rather than an experimental results paper. However, it notes:
- **Successful deployment**: "The whole system was mounted on the UAV and used by Soil and Irrigation Department of Colorado State University with success."
- **System validation**: All hardware interfaces verified and functional; software integration achieved seamless multithreaded operation
- **Operational parameters achieved**:
  - Lightweight design suitable for UAV payload constraints
  - Power-efficient operation from single 5V source
  - Synchronized data logging from 6 independent sensors
  - A6000 snapshot rate maximized (continuous PWM trigger at 50 Hz)
  - FLIR thermal video recording capability (extended from initial 80–90 second limit to longer duration after firmware update)

## Notable Details

### Technical Challenges Addressed
1. **SPI word size limitation**: Adafruit BBIO.SPI library does not support 16-bit word size required by AD7490; solution: wrote SPI driver in C with SWIG wrapper
2. **Low-voltage sensor amplification**: IRt/c output (0–1.511 mV) below ADC resolution; solved with LMP2021 amplifier (gain 1001)
3. **FLIR Thermal Capture firmware**: Initial firmware limited recording to 80–90 seconds; resolved via firmware update from TE-AX (TCFWUP.BIN file)
4. **