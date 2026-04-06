# KDE Direct KDEXF-UAS20LV 20A+ Electronic Speed Controller Product Sheet

## Document Metadata
- Type: Product specification sheet / vendor datasheet
- Source: KDE Direct website (kdedirect.com)
- Date: 1/31/2018
- Context: Found in BST NOAA SBIR Phase II budget justification supporting materials
- BST Products/Systems Referenced: None directly (this is a third-party component)

## Executive Summary
This is a product specification sheet for a KDE Direct electronic speed controller (ESC) designed for small unmanned aerial systems (sUAS) and multi-rotor applications. The document was included in Black Swift Technologies' NOAA SBIR Phase II proposal supporting materials, likely as justification for a component procurement or system integration choice.

## Product Description: KDEXF-UAS20LV 20A+ ESC

### Specifications
- **Type:** Electronic Speed Controller for electric multi-rotor UAS
- **Current Rating:** 20A+
- **Power Compatibility:** 2S LiPo - 6S LiHV (26.5V maximum)
- **Price:** $40.95 (as of 1/31/2018)
- **Connectors:** ф 3.5mm (KDEXF-BC35) 24K matching bullet connectors
- **Wire Specifications:** 
  - Power leads: 200°C, 16 AWG silicone
  - Motor leads: 18 AWG silicone

### Key Features & Technologies
- **Regenerative Braking:** Active braking during motor deceleration with instantaneous response
- **Temperature-Controlled Synchronous Rectification:** Proprietary algorithm for smooth low-throttle operation and improved response under high-peak loads; reduces operating temperatures
- **Dynamic Timing and Startup Power:** Optimized startup across full range of brushless motors (no hesitation/stuttering)
- **Increased Drive and Throttle Frequency Resolution:** High-accuracy linear throttle response
- **Motor Synchronization:** Factory-calibrated for consistent throttle control
- **Signal Compatibility:** Auto-recognition of OneShot125, PWMSync500, and standard PWM throttle-control signals; no hardware modifications required
- **Programming:** Compatible with KDE Direct Device Manager Adapter; supports manual-throttle and direct-range calibration for common racing controllers (Naze32, SPRacing, CC3D)

### Optimization
- Specifically designed and optimized for KDE Direct UAS Multi-Rotor Brushless Motor Series
- Tuned for near-instantaneous reaction to flight control commands

## Notable Details
- Patent pending on the design
- Pre-loaded with latest production firmware
- Marketed for "competition-level FPV racing" applications as well as general sUAS use
- Includes several related higher-capacity ESC models in product line (35A through 125A options)

## Why This Document Was Retained by BST
This component specification appears in BST's NOAA SBIR Phase II budget justification materials, suggesting the KDE Direct ESC was either:
1. A proposed component for integration into a BST system
2. A reference for performance specifications or cost estimation
3. Part of a bill of materials for a proposed multi-rotor platform

The document itself contains no BST-specific information and no indication of how or whether BST ultimately used this component.