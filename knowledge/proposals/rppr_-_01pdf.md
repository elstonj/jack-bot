# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- Type: Research Performance Progress Report (RPPR)
- Client/Agency: NOAA (Department of Commerce)
- Program/Solicitation: NOAA SBIR Phase II
- Federal Award Number: NA21OAR0210110
- Date: Reporting period 02/01/2021 - 01/31/2023 (Report submitted 03/31/2021)
- Award Period: 02/01/2021 - 01/31/2023
- BST Products/Systems Referenced: UAS (uncrewed aerial systems)
- Key Personnel: Jack Elston (Principal Investigator), Maciej Stachura

## Executive Summary
Black Swift Technologies received NOAA SBIR Phase II funding to develop a GPS-independent positioning system for beyond-line-of-sight (BLOS) UAS operations. The system combines high-rate inertial navigation with lower-rate absolute position solutions to provide 20Hz position updates with error bounds, functioning as a direct replacement for standard GPS units. This progress report documents the early Phase II efforts focused on project management and initial technical planning.

## Technical Approach
The system architecture comprises two integrated technologies:

1. **High-Rate Inertial Navigation Solution** - Provides rapid position updates independent of external signals
2. **Lower-Rate Absolute Position Solution** - Supplies periodic ground-truth positioning data
3. **Fusion Algorithm** - Combines both sources to deliver 20Hz position estimates with error bounds

Key technical components under development:
- GPS spoofing and jamming detection firmware
- Spoofed GPS signal generation capability for testing
- Dense labeled datasets from photogrammetry data
- RGB-D onboard sensing capabilities
- VCN (Vision-based Convolutional Neural) network training pipeline
- CDMA signal-based localization
- Localization filter development
- Single integrated hardware package designed to replace standard GPS units

## Products & Capabilities Described

**GPS-Independent Positioning System**
- What it is: A unified hardware package providing positioning without GPS
- Proposed use: Enable BLOS UAS operations in GPS-denied or GPS-contested environments
- Key specifications: 20Hz update rate, includes error bounds, GPS jamming/spoofing detection
- Performance: Designed as drop-in replacement for standard GPS units

## Use Cases & Applications
- **Primary:** Beyond-line-of-sight (BLOS) unmanned aerial systems operations
- **Government/Commercial Applications:**
  - Environmental research (coastline monitoring)
  - Powerline and pipeline inspections
  - Law enforcement and military applications
  - Medical and aid delivery
  - Severe weather prediction and environmental monitoring

## Key Results (for reports)
**Phase II Status (Early Stage):** This is an interim progress report from early Phase II (first ~2 months of activity).

Completed activities:
- Project management and kick-off meetings
- Requirements document review and modification
- Test site review
- Risk review and update

In-progress/planned work:
- Addition of spoofing and jamming detection to GPS firmware
- Bench testing of full system
- Generation of dense labeled datasets from photogrammetry
- RGB-D onboard sensing development
- VCN network training pipeline
- CDMA signal data collection
- Localization filter development

**Outputs to date:**
- No publications yet
- No new technologies or techniques finalized
- No patent applications or licenses
- Hands-on team experience gained with GPS jamming technologies
- Training database developed for cross-team training

## Notable Details

**Team Impact:**
- Staff size unchanged, but project required additional man-hours from existing team members
- Project provided hands-on training opportunities on GPS jamming and spoofing detection
- Team cross-training on diverse technology segments

**Infrastructure Developed:**
- Information-sharing database for GPS and flight data collection
- Training database for team capability enhancement

**Regulatory/Societal Context:**
- Project aims to improve relationships with regulatory agencies
- Potential to enable cost-effective UAS deployment for critical missions
- Emphasizes transition from research to viable commercial system (building on Phase I success)

**No foreign budget expenditure:** 0% of award spent in foreign countries

**Performance:** Project tracking with no reported delays, problems, or approach changes at time of this early interim report.