# NAVY Magnetometer Working Document

## Document Metadata
- Type: Internal working document / technical planning notes
- Client/Agency: U.S. Navy
- Program/Solicitation: Navy SBIR Phase I (Magnetometer topic)
- Date: Created 2025-08-15, Modified 2025-08-21
- BST Products/Systems Referenced: S0-VTOL
- Key Personnel: Alex Lomis (last editor)

## Executive Summary
Internal working document outlining component selection and integration planning for a Navy SBIR Phase I magnetometer payload system. Document focuses on determining optimal component configurations, reducing size/weight/power (SWaP), and minimizing magnetic interference while maintaining operational capability for ocean-based deployment.

## Technical Approach
The proposed system integrates multiple third-party sensors and computing components onto what appears to be a BST VTOL platform (S0-VTOL):

**Integration Strategy:**
- Minimize and customize commercial magnetometer and hydrophone systems to fit airframe constraints
- Evaluate alternative single-board computer (SBC) options to replace oversized default configuration
- Manage power budget with specialized battery cells to reduce magnetic interference and save internal volume
- Design for waterproofing and buoyancy to support post-landing ocean operations
- CAD-based validation before full airframe development

## Products & Capabilities Described

**S0-VTOL**
- BST's vertical takeoff and landing platform being used as the host vehicle
- Preliminary payload mounting location identified near nose, behind "AP" (likely autopilot or antenna pod)
- Sufficient internal volume to accommodate integrated sensor package and compute systems

## Use Cases & Applications
- Naval sensing operations involving magnetometry and hydrophone (underwater acoustic) data collection
- Deployment scenarios requiring ocean landing and post-landing data transmission/buoyancy
- Likely anti-submarine warfare (ASW) or maritime domain awareness applications given magnetometer + hydrophone combination

## Key Design Considerations
1. **Sensor Integration:** QuSpin magnetometer needs custom integration; determining minimal viable configuration and removal of unnecessary components
2. **Hydrophone Operations:** Cetacean Systems hydrophone requires cable routing, floating/waterproofing support for post-landing operations
3. **Computing:** Strong preference to downsize NVIDIA Jetson Orin SBC; document notes it is "massive and overkill" and recommends exploring smaller SOM (System-on-Module) alternatives
4. **Power & EMI:** Amprius pouch cells selected to reduce magnetic interference and save space; boxed configuration for SBC/battery assembly proposed
5. **Development Path:** S0-VTOL QuSpin mount to be created for initial evaluation using CAD validation before committing to full airframe development (AD)

## Notable Details
- Emphasis on minimizing SWaP and magnetic signature (critical for magnetometer-based sensing)
- Post-landing waterproofing and buoyancy requirement suggests ocean recovery/continued operation scenario
- Fiber-optic hydrophone cable under consideration (likely for EMI reduction)
- Preference for rapid CAD-based prototyping and validation before hardware build