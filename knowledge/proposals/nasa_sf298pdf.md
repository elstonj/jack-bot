# NASA SBIR Phase I Final Report: Adaptive and Secure Autonomy for UAS

## Document Metadata
- **Type:** Final Report (SBIR Phase I)
- **Client/Agency:** NASA / Shared Services Center (Stennis Space Center)
- **Program/Solicitation:** SBIR Phase I, Topic: Adaptive and Secure Autonomy for UAS
- **Contract Number:** 80NSSC25C0155
- **Award Date:** 09/29/2025
- **Report Date:** 03/27/2026
- **Period Covered:** 09/29/2025 - 03/27/2026
- **BST Products/Systems Referenced:** SwiftCore
- **Key Personnel:** Mr. Daniel Prendergast, Dr. Jack Elston, Dr. Maciej Stachura
- **Last Editor:** Beck Cotter
- **Document Classification:** Unclassified (U)

## Executive Summary
Black Swift Technologies developed and demonstrated a modular autonomy architecture built on SwiftCore, a flight-proven NDAA-compliant avionics platform. The Phase I work successfully integrated deterministic embedded flight control with sandboxed, higher-level autonomy modules while maintaining strict safety guarantees—addressing NASA's CAS (Cybersecurity, Assurance, and Safety) objectives for reconfigurable UAS solutions.

## Technical Approach

### SwiftCore Architecture
SwiftCore employs a **two-tier modular design:**

**MCU Tier (Microcontroller Unit):**
- STM32-based hardware nodes
- Provides deterministic flight control
- Nodes interconnected via CAN bus
- Publisher-subscriber messaging paradigm
- Handles sensor-actuator interfaces

**SBC Tier (Single-Board Computer):**
- NixOS on Linux
- Hosts containerized autonomy services
- WebAssembly (WASM) sandbox environment for experimental modules
- Isolated execution prevents third-party algorithms from compromising flight safety
- Enables rapid technology integration

**Inter-Tier Communication:**
- Lightweight binary protocol
- Measured latencies: <10ms
- Standardized message types across hierarchical control layers

**Safety Enforcement:**
- Supervisor service enforces safety envelopes
- Automatic override of experimental commands exceeding validated limits
- Maintains strict control boundaries between deterministic flight control and experimental autonomy

## Products & Capabilities Described

### SwiftCore
- **What it is:** A modular, flight-proven UAS avionics platform with NDAA compliance
- **Key differentiation:** Addresses limitations of monolithic designs where sensors, actuators, and control algorithms are tightly coupled
- **Proposed use in this context:** Foundation for integrating ML-based vision, multi-vehicle coordination, and experimental autonomy algorithms while maintaining deterministic flight control
- **Architecture:** Two-tier system (MCU + SBC) with CAN bus communication and WASM sandboxing
- **Safety features:** Hierarchical control layers with supervisor-enforced safety envelopes
- **Performance:** Inter-tier communication latency <10ms

## Use Cases & Applications

- **Multi-vehicle coordination** (autonomous fleet management)
- **ML-based vision autonomy** (perception and decision-making)
- **Experimental autonomy module integration** (third-party algorithm testing)
- **Rapid technology integration** for UAS platforms
- **NDAA-compliant autonomous systems** (defense/government applications)

## Key Results

The Phase I effort **successfully demonstrated the feasibility** of:
1. Combining deterministic embedded control (MCU tier) with higher-level autonomy (SBC tier) without safety compromise
2. Sandboxing experimental autonomy modules in WebAssembly while maintaining flight-critical guarantees
3. Implementing hierarchical control layers with standardized messaging, enabling independent module replacement
4. Creating a supervisor-enforced safety framework that automatically validates experimental commands

**Phase I Deliverable:** Complete definition and implementation of the modular autonomy architecture meeting NASA CAS 2024 objectives.

## Notable Details

- **NDAA Compliance:** SwiftCore explicitly engineered to meet NDAA requirements for government/defense use
- **20-Year SBIR Protection:** Government use limited to internal purposes for 20 years from award date; third-party disclosure prohibited during this period
- **Prior Art References:** Document cites Elston 2011 and Argrow 2015, indicating prior research foundation by BST personnel
- **Modular Philosophy:** The architecture directly addresses the document's stated problem—that monolithic UAS designs "hinder innovation by requiring extensive modifications and revalidation when adding new capabilities"
- **Direct NASA Alignment:** Solution framed explicitly around NASA CAS 2024 priorities for modular, reconfigurable autonomy systems
- **50-page Final Report:** Suggests substantial technical depth (not reflected in this cover page)