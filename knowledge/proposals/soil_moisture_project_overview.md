# Soil Moisture Project Overview

## Document Metadata
- Type: Project overview presentation
- Client/Agency: U.S. Air Force, Air Force Research Laboratory (AFRL)
- Program/Solicitation: AFWERX SBIR Phase II (Topic: Soil Moisture Mapping)
- Date: Created May 28, 2024; Last modified January 28, 2025
- BST Products/Systems Referenced: L-band radiometer, E2 Group 1 Quadrotor UAS
- Key Personnel: Daniel Prendergast (last editor)

## Executive Summary
Black Swift Technologies, in partnership with CU Technology Transfer Company (CET) and Operational Management Services (OMS), is developing a UAS-based L-band radiometer system to map soil integrity via soil moisture measurements for the U.S. Air Force. The system will enable rapid assessment of landing zones for C-130 aircraft operations by computing cone index (a measure of soil strength) from remotely sensed soil moisture data, replacing time-consuming manual field surveys.

## Technical Approach

**Core Technology:**
- L-band radiometer originally developed under NASA SBIR for SMAP (Soil Moisture Active Passive) Cal/Val
- Patented technology penetrates vegetation and measures volumetric soil moisture (VSM) in top soil layer
- Integrated onto E2 Group 1 Quadrotor UAS for high-resolution mapping

**Key Technical Elements:**
- Radiometer modifications for DAF requirements (refined instrument, auxiliary sensors)
- UAS modifications including surface temperature and NDVI (Normalized Difference Vegetation Index) sensors for real-time soil moisture calculation
- Soil Integrity Algorithm: Cone Index (CI) calculated from VSM and soil type using formula: **CI = a + b × mg**, where a and b are coefficients specific to USCS soil types
- Integration of geophysical sensing methods (EMI, CRI, GPR, tTEM) for subsurface characterization
- Survey capability: 1 km² per hour mapping rate

**Performance Specifications:**
- Soil moisture measurement accuracy: within 3% of true volumetric soil moisture
- Validated at test sites with NASA, USGS, and NOAA

## Products & Capabilities Described

**L-Band Radiometer**
- What: Patented remote sensing instrument measuring soil moisture through vegetation
- Use case: Primary sensor for computing soil integrity/cone index on unimproved landing zones
- Development history: Originally developed for NASA SBIR SMAP Cal/Val project; validated across multiple agencies

**E2 Group 1 Quadrotor UAS**
- What: Small unmanned aircraft system developed and validated for soil moisture mapping
- Capabilities: Carries radiometer and auxiliary sensors (thermal, NDVI, DEM generation, orthorectified imagery)
- Operational history: 6 field campaigns (golf courses, high-altitude alpine, grasslands) for NOAA and commercial users
- Use case: Platform for C-130 landing zone assessment; operates in demanding environments

**Soil Moisture-to-Integrity Conversion**
- Converts volumetric soil moisture (VSM) percentage to cone index via empirical relationship
- Leverages soil type database to tailor coefficients

## Use Cases & Applications

**Primary Use Case:**
- Mapping landing areas for C-130 operations on unimproved landing zones
- Rapid airfield evaluation to provide forward air controllers decision-critical data on soil integrity for landing operations

**Operational Context:**
- Replaces inefficient manual approaches (local point measurements with Dynamic Cone Penetrometer) and automated approaches (Rapid Assault Zone Terminal Evaluation Kit)
- Enables "on the move" measurements for global rather than local soil strength characterization
- Intended for field campaigns at locations including Tyndall Air Force Base

## Project Milestones & Deliverables

| Milestone | Timeline | Deliverable |
|-----------|----------|-------------|
| 01 | Award + 1 month | DAF requirements analysis and customer specifications |
| 02 | Award + 6 months | Radiometer modifications for sensing system |
| 03 | Award + 8 months | UAS modifications (surface temp, NDVI sensors) |
| 04 | Award + 12 months | Cone index algorithms and code development |
| 05 | Award + 14 months | Local field testing with in situ validation data |
| 06 | Award + 17 months | Soil integrity model refinement based on field results |
| 07 | Award + 18 months | Flight campaign at Tyndall AFB or customer-defined locations |
| 08 | Award + 21 months | Additional reporting and documentation |

## Key Results (Preliminary)
- Weekly soil moisture collections conducted at BST test site during development
- Early results show promise in applying soil integrity calculations to collected data
- System validation progressing with ongoing field campaigns

## Notable Details

**Team Composition:**
- **Black Swift Technologies**: UAS development, integration, field operations
- **CU Technology Transfer Company (CET)**: Radiometer instrument development, processing software, expertise in remote sensing concepts
- **Operational Management Services (OMS)**: Project management/support role (limited detail provided)
- **AFRL Partnership**: Long history using UAS for remote sensing; primary customer and technical collaborator

**Complementary Geophysical Methods Under Investigation:**
- Electromagnetic Induction (EMI): Multi-frequency, commercially available
- Capacitive Resistivity Imaging (CRI): Evaluated at University of Rouen calibrated test site
- Ground Penetrating Radar (GPR): Modified for water content monitoring; planned testing at University of Rouen
- Towed Time-Domain Electromagnetic (tTEM): 3D subsurface mapping (0-80 m depth); co-funded through EOARD for A-RAM applications

**Competitive Advantages:**
- Patented radiometer technology with 3-year NASA/USGS/NOAA validation history
- Non-contact geophysical approach vs. invasive point-measurement methods
- Integration of multiple data products (DEM, thermal, orthorectified imagery) on single platform
- Demonstrated field campaign experience across diverse environments

**Open Questions/Decisions Noted:**
- Meeting frequency and preferred scheduling
- Procurement of Dynamic Cone Penetrometer for ground truth calibration
- Flight permissions for local testing and Tyndall AFB operations
- Additional calibration tool requirements