# TX2_datasheet.pdf

## Document Metadata
- Type: Technical datasheet / Product specification
- Client/Agency: NVIDIA (Jetson product line documentation)
- Program/Solicitation: NASA 2017 SBIR Phase II (internal reference)
- Date: February 2020 (version 1.5.1, latest revision)
- BST Products/Systems Referenced: None explicitly; document is third-party component specification
- Key Personnel: None named

## Executive Summary
This is the NVIDIA Jetson TX2 Series System-on-Module datasheet detailing hardware specifications and technical characteristics. The TX2 is an embedded computing platform combining a Pascal GPU, ARMv8 CPU complex, video codecs, and rich I/O in a small-form-factor module. This appears in BST's 2017 NASA SBIR Phase II Vision Node deliverables, suggesting it may have been considered or integrated as a processing component for an airborne platform.

## Technical Approach
**Module Architecture:**
- **SoC:** Tegra X2 (Parker Series) System-on-Chip
- **Processing:** 
  - 256-core NVIDIA Pascal GPU (1.12 GHz max, 1.3 GHz boost)
  - ARMv8 64-bit heterogeneous multi-processor CPU: NVIDIA Denver 2 (dual-core, 2.0 GHz) + ARM Cortex-A57 (quad-core, 2.0 GHz)
  - 6 total processor cores with coherent high-performance interconnect fabric
- **Memory:** 128-bit LPDDR4 interface supporting up to 3732 MT/s (TX2), delivering 59.7 GB/s peak bandwidth
  - 8GB or 4GB LPDDR4 DRAM options
  - 32GB or 16GB eMMC 5.1 storage
- **Power:** 
  - 7.5W (Max-Q) / 15W (Max-P) for TX2
  - 10W (Max-Q) / 20W (Max-P) for TX2i
  - Input voltage: 5.5–19.6V (TX2), 9.0–19.6V (TX2i/4GB)
- **Operating temperature:** -25°C to 80°C (TX2), -40°C to 85°C (TX2i)

## Products & Capabilities Described

### GPU (Pascal Architecture)
- 256 CUDA cores with unified shaders
- Full support for modern graphics APIs: OpenGL 4.6, OpenGL ES 3.2, Vulkan 1.0, DirectX 12
- CUDA compute capability for general-purpose compute workloads
- End-to-end lossless compression, tile caching
- Early-z reject and multiple power-gating levels for efficiency
- Video protection region for DRM content

### Video Processing
**Decoder:**
- H.265 (Main 10, Main 8, Main 444)
- H.264 (Baseline, Main, High, MVC Stereo)
- VP9 (Profiles 0, 2), VP8, MPEG-1/2, MPEG-4, VC-1
- 4K (2160p) at 60fps decode capability
- Multiple simultaneous streams supported

**Encoder:**
- H.265, H.264 (Baseline/Main/High), VP8/VP9 MVC
- 4K (2160p) at 60fps encoding
- Multi-stream simultaneous encoding with frame-boundary context switch
- Scalable performance (resolution/frame rate)
- CBR and VBR rate control, error resiliency

**JPEG:** 600 MP/sec (decode & encode)

**Video Image Compositor (VIC):**
- De-interlacing, temporal noise reduction, scaling, color conversion, rotation, 2D BLIT operations

### Image Signal Processing
- 1.4 Gpix/s RAW-to-YUV processing engine
- Hardware-accelerated still image and video capture
- MIPI CSI 2.0 up to 2.5 Gbps per lane (up to 3 x4-lane or 6 x2-lane cameras supported)
- Bayer histogram statistics, auto-exposure/white-balance/focus support
- CSI Virtual Channel support (4 VCs per CSI x4)

### Display Controller
- Dual multi-mode outputs supporting eDP/DP/HDMI
- HDMI 2.0a/b: 4K @ 60Hz, 8/10/12 bpc RGB and YUV support
- DisplayPort 1.2a: 4K @ 60Hz, HBR2 5.4 Gbps
- eDP 1.4: up to 3840×2160 @ 60Hz, enhanced framing, power sequencing
- MIPI DSI: 2×4-lane support, 2560×1600 @ 60Hz max
- Multi-channel audio (up to 8 channels, 192 kHz, 24-bit) to HDMI

### Audio Processing Engine (APE)
- 96 KB dedicated audio RAM
- 4×I2S stereo/TDM I/O channels
- Digital audio mixer (10-in/5-out)
- Up to 8 channels, 192 kHz, 32-bit samples
- Multi-band dynamic range compression (DRC), parametric EQ, sample rate conversion

### Memory Controller
- Integrated ARM SMMU v2 (SMMU-500) with two-stage translation
- DRAM ECC (TX2i, software-enabled): Single-bit correction, double-bit detection
- AES-XTS encryption for carveout regions (TrustZone, GSC, VPR)
- Dual CKE signals for dynamic power-down per device

### Security
- Secure boot with RSA 2048-bit PKC support
- Hardware acceleration for AES-128/192/256 (encryption/decryption)
- SHA-1, SHA-256, SHA-384, SHA-512 hardware support
- RSA (512 to 4096-bit), ECC (160 to 521-bit)
- TrustZone technology for DRAM/peripherals
- TSEC (Tegra Security Controller) with Falcon engine for DRM
- Side-channel attack prevention

### Connectivity
**TX2 only:**
- IEEE 802.11a/b/g/n/ac dual-band 2×2 MIMO WLAN (866.7 Mbps max)
- Bluetooth 4.1 (3 MB/s, A2DP audio profile, HIDP)

**All variants:**
- Gigabit Ethernet (10/100/1000 BASE-T)
- USB: 3×USB 3.0, 3×USB 2.0 (XHCI host controller, USB 3.0 device controller)
- PCIe: 2×x1 and 1×x4 controllers (5-lane total)
- SATA (1 port)
- SD/MMC controller: eMMC 5.1, SD 4.0, SDIO 3.0 support

### Peripheral Interfaces
- 5×UART
- 3×SPI
- 8×I2C
- 2×CAN
- 4×I2S
- GPIOs (quantity not specified in datasheet excerpt)
- JTAG for debugging

### Thermal Management
- On-chip thermal sensors across die
- Thermal throttling controller (SOC_THERM) with:
  - Multiple software-configurable temperature thresholds per sensor
  - Hardware throttling response capability
  - Over-current detection support
  - Throttle prioritization

## Use Cases & Applications
Listed in datasheet:
- Intelligent Video Analytics (IVA)
- Drones
- Robotics
- Industrial automation
- Gaming
- Virtual/Augmented Reality
- Portable medical devices
- Intelligent embedded systems

*Inferred from BST context: The presence of this datasheet in the Vision Node deliverables suggests potential use in airborne platforms requiring real-time image processing, video encoding/decoding, and autonomous decision-making.*

## Key Technical Specifications
| Specification | TX2 | TX2 4GB | TX2i |
|---|---|---|---|
| GPU | 256-core Pascal @ 1.12 GHz | 256-core Pascal @ 1.12 GHz | 256-core Pascal @ 1.12 GHz |
| CPU | Denver 2 (2c) + Cortex-A57 (4c) | Denver 2 (2c) + Cortex-A57 (4c) | Denver 2 (2c) + Cortex-A57 (4c) |
| RAM | 8 GB LPDDR4 @ 1866 MHz | 4 GB LPDDR4 @ 1600 MHz | 8 GB LPDDR4 @ 1600 MHz |
| Storage | 32 GB eMMC 5.1 | 16 GB eMMC 5.1 | 32 GB eMMC 5.1 |
| Power (Max-P) | 15W | 15W | 20W |
| Peak Memory BW | 59.7 GB/s | 51.2 GB/s | 51.2 GB/s |
| Temp Range | -25°C to 80°C | -25°C to 80°C | -40°C to 85°C |
| Input Voltage | 5.5–19.6V | 9.0–19.6V | 9.0–19.6V |

## Notable Details
- **Form Factor:** Small system-on-module (SOM) with 400-pin board-to-board connector, single Thermal Transfer Plate (TTP) for thermal interface
- **Heterogeneous Computing:** Denver 2 optimized for single-thread performance; Cortex-A57 for multi-threaded loads; coherent interconnect enables task migration without cache-flushing overhead
- **Power Efficiency:** Dynamic frequency scaling, multiple clock-gating levels, support for sleep modes (OFF, ON, SLEEP states with wake events)
- **Three TX2 Variants:** Standard TX2 (with integrated WLAN/BT), TX2 4GB (low-memory variant), TX2i (industrial grade, wider temp range, ECC support, higher power)
- **Revision History:** Document version 1.5.1 (Feb 2020) with iterative updates since initial Mar 2018 release; latest changes include extended VDD_IN range (5.5–19.6V for TX2)
- **OEM Support:** Comprehensive design guides referenced (OEM Product Design Guide, Thermal Design Guide, Parker Series SoC Technical Reference Manual) indicate mature ecosystem for system integration
- **Security Focus:** Multiple layers including secure boot, hardware crypto acceleration, DRM support via TSEC, encrypted DRAM regions, TrustZone support

**Document Quality Note:** This is a comprehensive, well-structured technical datasheet with detailed specifications, block diagrams, pin definitions, electrical characteristics, and revision history. It serves as a reference for systems integrators and OEMs incorporating the TX2 module into embedded applications.