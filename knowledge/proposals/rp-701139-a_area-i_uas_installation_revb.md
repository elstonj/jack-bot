# Area-I Altius UAS Installation – WP-3D Structural Substantiation

## Document Metadata
- **Type:** Technical Report (Structural Analysis & Substantiation)
- **Client/Agency:** NOAA Aircraft Operations Center, Science & Engineering Branch
- **Program:** Area-I UAS Installation on WP-3D Orion Aircraft
- **Date:** January 8, 2021 (Revision B; initial release December 17, 2019)
- **Aircraft:** NOAA WP-3D Orion (tail numbers N42 and N43)
- **BST Products/Systems Referenced:** Altius UAS (Area-I)
- **Key Personnel:** 
  - Akshar Patel (Author)
  - J. Hartberger (Reviewer)

## Executive Summary
This report provides structural substantiation for installing and launching the Altius UAS (Area-I) via the free fall chute assembly on NOAA's WP-3D Orion aircraft to obtain research data during hurricanes. The analysis evaluates loads applied to the drop chute, adapter bracket, antenna installation, and fasteners using emergency crash and flight load factors consistent with FAR 25.561 requirements. All hardware maintains positive design margins and is acceptable for installation.

## Technical Approach

### Load Analysis Framework
- Applied emergency crash load factors from original aircraft certification (Lockheed Aircraft Corporation)
- Evaluated margins of safety for all affected components
- Used load factors similar to FAR 25.561 but referenced to original aircraft certification basis

### Ultimate Crash Load Factors Applied:
| Load | Direction | Notes |
|------|-----------|-------|
| -7.1 g | Down (normal to longitudinal axis) | |
| +4.2 g | Up (normal to longitudinal axis) | |
| ±1.9 g | Lateral (normal to longitudinal axis) | |
| -10 g | Forward (parallel to longitudinal axis) | |
| 450 lb | Axial | Along free fall tube (controlling load) |

The **450 lb axial launch tube load** was identified as the most severe ultimate load condition.

## Products & Capabilities Described

### Altius UAS (Area-I)
- **What it is:** Unmanned Aircraft System developed for NOAA hurricane research missions
- **Proposed use:** Loaded and launched from the free fall chute on WP-3D Orion to obtain research data during hurricanes
- **Launch method:** Free fall chute assembly with 450 lb axial ejection load

## Structural Components Analyzed

### 1. Free Fall Chute Tube
- **Material:** AL 6061-T6 (0.125" thickness)
- **Length:** ~64.0 inches
- **Attachment:** 32 MS 20246DD6 rivets to aircraft skin and longeron (AL 2024-T4, 100° countersunk)
- **Load Analysis:** 450 lb axial load decomposed into:
  - Fx (bending component): 335 lbs at 42° angle
  - Fy: 301.1 lbs
  - Resulting bending moment: 15,086.6 in-lb
  - Bending stress: 3.1 ksi (acceptable by inspection)
- **FEA performed:** Confirmed structural adequacy

### 2. Chute End Collar & T-Section Attachment
- **Chute End Collar to Skin:** 16 MS 20246DD rivets (single shear)
- **T-Section to Skin & Chute Collar:** 17 MS 20246DD rivets (double shear)
- **Maximum stress found:** 4.3 ksi at critical point (acceptable)

### 3. Clamp Ring
- **Material:** 6061-T6 Al Plate
- **Load:** 450 lb applied
- **Failure Theory:** Bending
- **Minimum Margin of Safety:** +0.02 (positive margin)
- **Torque specification:** No more than 50 in-lb
- **Analysis:** Completed by Pagnotta Engineering (Report P2073-18A-AR-01_Rev)

### 4. Antennas (Communication)
Two prototype antennas manufactured by Hascall-Denke mounted on lower radiometer cover:
- **AVDP1785 blade antenna**
- **AVDP430 rod antenna**
- **Fastening:** Four Hi-Lok 21-6 fasteners per antenna

#### Antenna Load Testing:
- **Design gust:** FAR 25.415 (65-knot gust at sea level = 109 ft/sec)
- **Calculated dynamic pressure:** 4.1 psf
- **Conservative test load:** 50 lb lateral pull applied at mid-point height (~3.5" from base)
- **Test result:** Antenna passed static load test with no deformation or damage
- **Status:** Acceptable by inspection

### 5. Radio Equipment Tray (Station 7)
- **Equipment:** Tellisware radio and Raveon radio receiver
- **Mounting:** 4 NAS bolts on aircraft rail
- **Tray weight:** 8.9 lbs
- **Analysis:** Loading acceptable by inspection

### 6. Installation Hardware (Free Fall Chute Assembly)
- 2× Clamp bars (6061-T6)
- 1× Dog bone link
- 2× 3/8" pins
- Bolts AN10-33-2x
- 2× Threaded rod NAS1454-5-0802
- 1× Turn buckle (6061-T6)
- 2× Nut MS 21042-4
- 2× Locking pin MS 24665-446
- Cargo strap (prevents ejection of components during deployment, secured to front face of Altius and outboard seat track)

## Key Results

### Structural Adequacy
- **All hardware maintains positive design margins** in all load factors
- **Equipment is acceptable by inspection** for installation on WP-3D Orion aircraft
- **No structural modifications required** to aircraft

### Critical Findings by Component:
1. **Free fall chute bending stress:** 3.1 ksi (acceptable)
2. **T-section maximum stress:** 4.3 ksi (acceptable)
3. **Clamp ring:** Positive margin of safety (+0.02)
4. **Antenna:** Passed 50 lb lateral pull test without deformation
5. **Radio tray:** Acceptable by inspection

## Installation Details

### Free Fall Chute Installation
- Drawing: DWG 938478 (CHUTE INSTL – FREE FALL, SONOBUOY)
- Clamp torque specification: ≤50 in-lb
- Cargo strap required to secure assembly during deployment

### Antenna Installation
- Blade antenna per drawing 1Y46400-ODD
- Rod antenna per drawing 1Y46450-ODD and installation video 1Y46450 AVMP430 INSTALLATION INSTRUCTIONS
- Mounting certified per previous analysis (Pagnotta Engineering P1894-04_Radiometer_Port_Cover_Summary_01 and drawing 1894-04-200)

## Notable Details

### Aircraft Compatibility
- Substantiation applies to **both NOAA WP-3D Orion aircraft** (tail numbers N42 and N43)
- Structural analysis incorporates aircraft-specific stress reports and original certification basis from Lockheed Aircraft Corporation
- Load factors taken from NOAA Stress Analysis Worksheets (1975)

### Regulatory Alignment
- Analysis approach parallels FAA FAR 25.561 emergency landing conditions
- Meets FAR 25.415 gust load requirements for antenna design

### Third-Party Engineering
- Clamp ring analysis: Pagnotta Engineering (P2073-18A-AR-01_Rev)
- Radiometer port cover analysis: Pagnotta Engineering (P1894-04)
- Antenna design: Hascall-Denke (manufacturer)

### Approval Chain
- Report authored by Akshar Patel
- Reviewed and approved by J. Hartberger (NOAA Science & Engineering Branch)
- Document classification: NOAA property (proprietary)