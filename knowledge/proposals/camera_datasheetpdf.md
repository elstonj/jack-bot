# See3CAM_CU135 Camera Datasheet

## Document Metadata
- Type: Technical datasheet/product specification
- Manufacturer: e-con Systems India Pvt Ltd
- Date: 26 December 2017 (Revision 1.3)
- BST Products/Systems Referenced: Vision Node (NASA 2017 SBIR Phase II project)
- Document Location: NASA 2017 SBIR Phase II Deliverables archive

## Executive Summary
The See3CAM_CU135 is a 13-megapixel USB 3.0/2.0 camera module with USB Type-C connector from e-con Systems. It features a 1/3.2" AR1335 CMOS sensor, plug-and-play UVC compliance, and supports resolutions up to 4K at various frame rates with both uncompressed (UYVY) and compressed (MJPEG) formats. The camera is designed for integration into embedded imaging applications with minimal development effort.

## Technical Approach & Product Description

### Core Specifications
- **Sensor**: 1/3.2" optical format CMOS image sensor (ON Semiconductor AR1335)
- **Resolution**: 4208 x 3120 pixels (13 MP native)
- **Size**: 30 x 30 x 30.2 mm (compact two-board solution)
- **Interface**: USB 3.0 SuperSpeed with Type-C reversible connector (backward compatible with USB 2.0)
- **Lens Mount**: Standard M12 (S-mount) board lens holder

### Supported Formats & Frame Rates

**USB 3.0 Uncompressed (UYVY):**
- VGA (640×480): 120 fps / 60 fps
- 720P (1280×720): 60 fps / 30 fps
- 960P (1280×960): 60 fps / 30 fps
- 1080P (1920×1080): 60 fps / 30 fps
- 1440P (1920×1440): 45 fps / 22.5 fps
- 4K UHD (3840×2160): 15 fps / 7.5 fps
- 2.8K (2880×2160): 20 fps / 10 fps
- 4K Cinema (4096×2160): 15 fps / 7.5 fps
- 13MP (4208×3120): 9 fps / 4.5 fps

**USB 3.0 Compressed (MJPEG):**
- VGA: 120 fps
- 720P through 1440P: 60 fps
- 4K UHD, 2.8K, 4K Cinema: 30 fps
- 13MP: 20 fps

**USB 2.0** supports significantly reduced frame rates (e.g., VGA 60/30 fps, 720P 16/8 fps, 13MP 1 fps)

### Image Sensor Specifications
- **Pixel Size**: 1.1 µm × 1.1 µm
- **Sensor Type**: Colour CMOS rolling shutter with Bayer RGB
- **Signal-to-Noise Ratio**: 37 dB
- **Dynamic Range**: 69 dB
- **Responsivity**: 0.76 V/lux-sec
- **Field of View**: 67° (full resolution with e-con lens)
- **Interlaced HDR (iHDR)**: Supported

## Connectivity & GPIO Features

### USB Type-C Connector
- Standard USB 3.1 Type-C connector supporting SuperSpeed differential pairs and Hi-Speed pairs
- Fully reversible plug interface
- Compatible with standard USB 3.0 Type-A to Type-C cables

### GPIO Header (10-pin)
- **Pin 1-3**: VCC_5V power supply for external flash circuits (can source up to 300mA on USB 3.0 only)
- **Pins 4, 5, 8**: Ground
- **Pin 6**: I2C Serial Clock (400 kHz)
- **Pin 7**: I2C Serial Data (pulled up to 1.8V)
- **Pin 9**: NC (not connected)
- **Pin 10**: External trigger signal for still image capture and sensor trigger

## Power Consumption & Electrical Specifications

### Operating Voltage
- 5V ± 5% (5V ± 250mV typical)

### Typical Current Draw (USB 3.0)
- **Idle**: 95 mA (0.475 W)
- **Maximum streaming** (3840×2160 @ 30 fps MJPEG): 370 mA (1.850 W)
- **Minimum streaming** (640×480 @ 120 fps MJPEG): 282 mA (1.410 W)
- Range across operating modes: 212–403 mA

### GPIO Voltage Levels
- Input LOW: 0.45V max
- Input HIGH: 1.4V min
- Output LOW: 0.18V typical
- Output HIGH: 1.62V typical
- Output drive strength: 9 mA (source), 100 µA (sink)
- Maximum input voltage: 2.1V

### Operating Temperature
- **Range**: -30°C to +70°C
- **Note**: Image quality degrades significantly above 50°C with thermal flickering noise; continuous operation at 70°C causes irreparable damage

## Software & Compatibility

### Operating Systems
- **Windows**: 7, 8, 8.1, 10 (32-bit and 64-bit) — native UVC drivers, no additional installation required
- **Linux**: Native UVC driver support with V4L2 API access

### Driver Support
- **UVC Compliant**: Yes (USB Video Class Version 1.0)
- **Plug-and-Play**: No special drivers required
- **Product ID (PID)**: 0xC1D1
- **Vendor ID (VID)**: 0x2560

### Application Integration
- Exposed as DirectShow capture source on Windows
- Exposed as V4L2 camera on Linux
- Compatible with any DirectShow-compliant application (e.g., Skype)
- e-con provides sample PC applications demonstrating features
- Customers can develop customized applications using standard APIs

## Mechanical Details
- **Module Board Dimensions**: 30×30 mm footprint with multiple layers
- **Total Height**: 30.2 mm (without lens)
- **Two-board design**: Separate camera sensor module board and USB3.0 interface board
- **Mounting**: Standard M12 lens holder for optical customization
- **Connectors**: Molex USB Type-C connector (105450-0101), Hirose GPIO FPC header (FH34SRJ-10S-0.5SH(50)), Molex flex cable (0152660095)

## Notable Features & Applications

### Key Capabilities
- Lightweight, portable, versatile design enabling rapid integration
- Ready-to-manufacture with built-in firmware
- Supports still image capture in both UYVY and MJPEG formats
- iHDR (Interlaced High Dynamic Range) support for enhanced dynamic range
- Customizable lens mount (M12) for application-specific optics
- GPIO header enables external flash circuits and sensor triggering
- Bulk transport USB streaming (no isochronous support)

### Application Suitability
- Embedded imaging systems requiring compact, low-power operation
- Industrial machine vision
- Security and surveillance
- Medical imaging
- Research and scientific applications (implied by NASA SBIR context)
- Applications requiring multiple resolution/frame rate combinations with dynamic switching

## Operating Notes & Limitations

- **Frame Rate Dependency**: Maximum frame rates assume exclusive USB port access; sharing with other devices reduces bandwidth and frame rates
- **Auto-Exposure Impact**: Ambient light levels affect frame rates in auto-exposure mode; manual exposure provides consistent maximum frame rates
- **Exposure Considerations**: Exposure values above -6 cause frame rate reduction as exposure time exceeds frame period
- **USB 2.0 Limitation**: No load connections to VCC_5V pins when using USB 2.0 connectivity
- **Trigger Input**: TRIG pin requires debouncing circuitry and push-button switch for reliable operation
- **Field of View Variation**: FOV differs across resolutions (0-28.88% vertical crop depending on resolution selected)

## Context & Integration
This datasheet documents a third-party camera module (See3CAM_CU135 from e-con Systems) evaluated or integrated into Black Swift Technologies' Vision Node project under a NASA 2017 SBIR Phase II contract. The compact form factor, UVC compliance, and flexible USB interface make it suitable for embedded autonomous systems, particularly aircraft-mounted imaging platforms requiring minimal size, weight, and power (SWaP) penalties.