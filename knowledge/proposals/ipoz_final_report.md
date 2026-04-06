# IPOZ Photogrammetry System Final Report

## Document Metadata
- Type: Final Report (technical system documentation)
- Client/Agency: IPOZ
- Program/Solicitation: Not specified
- Date: 2019-01-30 (created), 2019-02-05 (last modified)
- BST Products/Systems Referenced: IPOZ Photogrammetry System (custom embedded imaging system)
- Key Personnel: Not named in document

## Executive Summary
This report documents the design, performance, and operation of a custom photogrammetry system developed by Black Swift Technologies for IPOZ. The system consists of a Ximea camera with a TX2 compute module, synchronized timing systems including an IMU with PPS signal, and a web-based user interface for image acquisition, camera control, and data management. The system captures high-resolution images (~9 MB each in JPEG format) at approximately 1.07 Hz with full-resolution storage and 1080p live video streaming at 20 FPS.

## Technical Approach

### Core Hardware
- **Compute Platform**: NVIDIA TX2 with GPU acceleration
- **Imaging Sensor**: Ximea camera (4112 x 3008 resolution, 8-bit Bayer format)
- **Storage**: 1TB SSD with zeroconf networking capability
- **Timing Reference**: Inertial Measurement Unit (IMU) with PPS (Pulse Per Second) signal
- **Network**: Wired Ethernet (max 125 MB/s transfer), accessible via fixed IP (192.168.50.42:8000) or zeroconf (bst-tx2-spacely.local)

### Software Architecture
- Asynchronous, multithreaded embedded system written with independent thread domains:
  - Ximea camera clock domain (ns precision, tags start of exposure)
  - TX2 Monotonic clock (high precision, independent of leap second corrections)
  - IMU clock domain (1 PPS signal + RS232 serial messages)
- Web-based GUI (HTTP server on port 8000) for user control and live streaming
- Image acquisition rate: Fixed at ~1.07 Hz (17 frames at 20 FPS camera rate, accounting for GPU frame drops)
- Maximum sustainable acquisition: 4-5 Hz with stable performance

### Timing Synchronization
- Three independent clock domains with cross-calibration:
  - Ximea-to-TX2: Conversion computed at start of acquisition using 100 averaged timestamp requests with latency estimation
  - TX2-to-IMU: Conversion factor derived from PPS timestamps and IMU serial messages
  - PPS signal: Conditioned from 5V (IMU) to 3.3V (TX2 compatible) via voltage step-down (ns-level delay)
- Kernel module for PPS detection: Mean response time 22 µs ±10 µs (16,000 test pulses, zero dropped)
- Pulse widths tested down to 8 µs

### Image Processing
- Color space conversion (Bayer to RGB) and white balance via TX2 GPU
- Wide standard deviation in GPU processing leads to ~1 frame drop per 10 frames
- JPEG encoding at quality level 100 with floating-point IDCT to minimize compression loss
- Video stream: H.264 encoded 1080p at 20 FPS (~4 Mbits/sec or ~4000 kbits/sec)
- Typical image file size: ~9 MB on disk

### Data Storage & Transfer
- **Recording Capacity**: ~57,000 images on 512 GB reserved space (other 512 GB reserved for zip downloads); 15.8 hours continuous at 1.07 Hz
- **Data Format**: Full-resolution JPEG images + master CSV with timing metadata per acquisition folder
- **Download**: Data zipped on SSD during transfer; video feed pauses to maximize Ethernet bandwidth (max 125 MB/s; ~30 sec recording = ~300 MB transfers in ~2.4 seconds)
- **CSV Metadata**: Records image filename, image timestamp (Ximea clock domain converted to TX2 domain), last PPS timestamp, last IMU timestamp

### Clock Domain Conversion
Timing conversion calculated as:
```
Ximea_TX2_conversion = (TX2_timestamp_after - TX2_timestamp_before) / (Ximea_timestamp_response - Ximea_timestamp_request)
```
Communication latency corrected by averaging over 100 requests at acquisition start.

### Known Serial Communication Issue
- IMU RS232 messages corrupted ~13% in test data provided, less frequently in actual operation but still significant
- PPS signals extremely reliable (no missed detections during testing)
- Serial message corruption causes conversion factor jumps (~1 second intervals); post-processing can identify dropped messages by detecting jumps >0.5 seconds

## Products & Capabilities Described

### IPOZ Photogrammetry System
**What it is**: A complete embedded imaging and data acquisition platform integrating a high-resolution camera, TX2 compute module, precise timing via IMU/PPS, and web-based control interface.

**Key Specifications**:
- Camera resolution: 4112 x 3008 pixels (8-bit)
- Acquisition rate: ~1.07 Hz (nominal), up to 4-5 Hz max
- Live video: 1080p @ 20 FPS
- Storage: 1TB SSD (512 GB usable for acquisition)
- Network: Ethernet 125 MB/s, zeroconf-capable
- Timing precision: Microsecond-level synchronization across three independent clock domains
- Power: Operates continuously for 15.8+ hours per acquisition session

**Proposed Use**: Image acquisition for photogrammetry applications with precise timestamping for post-processing alignment and 3D reconstruction.

**Performance Claims**:
- PPS timing: No dropped pulses over 16,000 test cycles; mean detection latency 22 µs ±10 µs
- Camera settings adjustable: Exposure (500 µs increments to ~30 sec), analog gain (0-24 dB in 1 dB steps), digital gain (0-24 dB), white balance (0.0-2.0 per channel)
- Depth of field control via fixed focal length lens with manual aperture and focus adjustment
- Frame drop rate: ~1 per 10 frames due to GPU processing variance

## Use Cases & Applications
- Photogrammetry with precise multi-modal timing (camera, IMU, PPS)
- High-resolution image mapping and reconstruction requiring microsecond-level synchronization
- Long-duration autonomous image acquisition (15+ hour sessions)
- Environments requiring stable clock reference (IMU PPS provides external timing anchor)

## Key Results (Testing & Performance)

### Timing Validation
- PPS kernel module latency: 22 µs ±10 µs (nearly Gaussian distribution)
- Voltage step-down delay: ~ns (below precision of major clock domains)
- No PPS signal dropouts across all testing

### Image Acquisition Performance
- Sustainable frame rate: ~1.07 Hz (17 frames @ 20 FPS nominal camera rate)
- GPU processing variability causes ~10% frame drops
- Maximum tested rate: 4-5 Hz with stable performance
- Video bitrate: ~4000 kbits/sec (measured 3824 kbits/sec nominal)

### Storage & Transfer Performance
- Data transfer rate: Max 125 MB/s (30 sec recording ~300 MB takes ~2.4 sec)
- Usable storage: 512 GB (57,000 images at ~9 MB/image)
- Continuous recording duration: 15.8 hours @ 1.07 Hz

### IMU Serial Communication
- RS232 message corruption: ~13% in test data, lower but present in operational use
- Mitigation: PPS signal remained 100% reliable; post-processing can detect dropped messages by spike detection (>0.5 sec jumps in conversion factor)

## Notable Details

### Networking & Access
- Fixed IP: 192.168.50.42:8000
- Zeroconf name: bst-tx2-spacely.local:8000
- Zero-configuration networking support (Avahi on Linux, Bonjour on Windows/Mac)
- API documentation accessible at server address /documentation endpoint

### User Interface Features
- Web-based GUI (HTTP)
- Live 1080p video preview with frame rate display
- Camera settings menu: Exposure, gains (analog/digital), white balance per-channel
- Folder naming (alphanumeric only; auto-timestamp fallback)
- One-click image capture start/stop (capture button changes red circle → red square)
- Data download options: Current acquisition folder or entire drive
- Drive firmware update capability via encrypted files (data.zip.enc + key.bin.enc)
- Full-screen mode for immersive viewing

### Data Organization
- Each acquisition session generates acquisition folder with:
  - Master CSV (metadata for all images in session)
  - Full-resolution JPEG images with naming convention based on TX2 monotonic clock (Unix epoch conversion)
  - Timing columns: image_filename, image_timestamp (Ximea→TX2 converted), last_pps_timestamp, last_imu_timestamp

### Camera Optics
- Fixed focal length lens with manual focus and aperture rings
- Set screws lock adjustments (but do not tune)
- Recommended setup procedure: aperture → focus → gain/exposure iteration
- Optimal exposure: as short as possible for global shutter performance
- Recommended gains: +6 dB (low-noise floor), +10-12 dB (max before decolor/noise)

### Known Issues & Workarounds
1. **Initial camera settings**: First slider adjustment may not register; repeat by sliding off and back to desired value
2. **Camera settings feedback**: No real-time feedback; settings GUI values may not reflect current state; recommend re-setting on new stream
3. **Drive clear**: Must restart stream after clearing; bug fixed in Version 1.0.1
4. **Application exit**: Must explicitly hit "Stop Stream" and wait for status change before closing browser; improper exit causes background persistence
5. **Chrome compatibility**: Older Chrome versions show stream start delays and occasional stream persistence after stop; closing/reopening tab resolves
6. **Multiple users**: WiFi access allows viewing by multiple users, but acquisition shows count collisions (0, -1); only single user should acquire
7. **IMU serial messages**: After 1-2 days of continuous operation, RS232 messages stop (PPS still works); power cycle IMU resolves
8. **Kernel watchdog**: Two lockups observed during testing; second occurred during download with poor grounding (likely ESD); power cycle recovers
9. **SSD UUID issue**: Observed once on backup TX2 where SSD UUID changed, preventing mount on boot; requires BST physical access to resolve

### Focusing Guidance
- Global shutter benefits from shortest practical exposure
- Wider aperture increases light but reduces depth of field; narrower aperture increases depth but requires longer exposure or higher gain
- Recommended iteration: Set gain → adjust exposure → optimize aperture → focus → lock → iterate if needed
- Outdoor lighting significantly better for image quality than office environment

### Related Documentation
- System interconnect diagrams: IPOZ_Interconnect.PDF (referenced but not included)
- API documentation: API_Documentation.pdf (referenced but not included)
- Ximea CamTool software available for focus verification via mouse scroll zoom
- Ximea Windows software package: https://www.ximea.com/support/wiki/apis/XIMEA_Windows_Software_Package
- CamTool instructions: https://www.ximea.com/support/wiki/allprod/XIMEA_CamTool

### Cost & Budget Note
Report explicitly excludes component costs, budgets, and bill of materials (found in separate email exchanges with IPOZ).