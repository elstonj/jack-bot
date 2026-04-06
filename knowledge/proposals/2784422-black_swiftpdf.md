# Enabling BLOS UAS Operations through a Diverse-Source Global Positioning System

## Document Metadata
- Type: SBIR Phase I Proposal with Reviewer Evaluations
- Client/Agency: NOAA (National Oceanic and Atmospheric Administration)
- Program/Solicitation: NOAA SBIR 2019, Subtopic 9.5.01
- Date: Submitted 2019 (Application ID: 2784422); Reviews dated around 2019-2020
- BST Products/Systems Referenced: sUAS (small Unmanned Aerial Systems)
- Key Personnel: Jack Elston (last editor of review document)

## Executive Summary
Black Swift Technologies proposed developing a diverse-source global positioning system (DS-GPS) to enable safe Beyond Line-of-Sight (BLOS) autonomous UAS operations in GPS-denied or GPS-degraded environments. The 8-month Phase I effort ($116,095 federal funding) would integrate multiple navigation methods including SLAM, optical flow, machine learning, and land-based navigation aids to provide navigation redundancy when GPS is unavailable due to jamming, spoofing, or terrain obstruction.

## Technical Approach
The proposed solution combines multiple complementary navigation technologies:
- **SLAM (Simultaneous Localization and Mapping)**: For visual-based position estimation
- **Optical Flow**: Machine vision algorithms for motion-from-vision position determination on embedded hardware
- **Coastline Following**: Navigation aid for coastal operations
- **Land-Based Navigation Aids and Transmitters**: Secondary positioning sources for diverse-source GPS
- **Machine Learning**: Algorithms to identify suitable emergency landing zones in the event of GPS loss

The approach addresses GPS failure modes including jamming, spoofing, and signal blockage from terrain. The innovation lies in combining multiple methods to provide greater reliability than any single approach.

## Products & Capabilities Described

**sUAS (Small Unmanned Aerial Systems)**
- Application domain: Small UAS platforms for autonomous operations
- Proposed enhancement: Navigation redundancy for GPS-denied environments
- Capability goal: Safe BLOS autonomous flight without reliance on GPS
- Safety feature: Machine learning-based automated safe landing zone identification

## Use Cases & Applications

### NOAA/Government Applications:
- Hurricane tracking UAS operations (specifically mentioned by proposal as potential NOAA use)
- Federal government UAS navigation in GPS-denied areas
- Safe BLOS operations for NOAA missions

### Commercial Applications (identified by reviewers):
- Rail inspection without need for multiple visual observers along flight path
- Pipeline inspection in BLOS operations
- Power line inspection
- General NAS (National Airspace System) UAS operations requiring navigation redundancy
- Future BVLOS (Beyond Visual Line-of-Sight) operations requiring navigation backup

## Key Review Findings

**Technical Merit:** All three reviewers found the approach technically sound and appropriate. Reviewers noted innovation in combining SLAM, optical flow, and coastline-following methods.

**Innovation Assessment:** 
- Reviewer 1: "Significant innovation" through method combination
- Reviewer 2: "Highly innovative approach" including optical flow sensors, land-based navigation aids, and "motion from vision" machine vision algorithms
- Reviewer 3: Reasonable technical approach with commercial potential

**Relevance to NOAA Goals:**
- Directly supports NOAA's goal of safe and efficient BLOS operations
- Important step toward NOAA's future BLOS transition
- Addresses critical safety risk of GPS signal loss
- Mitigates risks to life and property during GPS failure events

**Commercial Potential:**
- Reviewers uniformly rated high commercial potential
- Market need for navigation redundancy in NAS operations
- Broad applicability across multiple infrastructure inspection domains
- Expected requirement for future BVLOS operations

**Applicant Qualifications:**
- Reviewer 1: "Past experience working with BlackSwift Technologies has been exceptional"
- Reviewer 2: "BST's staff qualifications, and UAS experience is outstanding"
- Reviewer 3: "Principal investigators are well qualified" with "extensive experience with UAS platforms and integration"

## Notable Details
- Project Period: 07/01/2019 - 02/29/2020 (8 months)
- Total Proposal: $116,095 (all federal funding)
- No reviewer comments on how BLOS flight would avoid other aircraft (Reviewer 2 noted this gap)
- One reviewer noted GPS denial is not currently a high-priority requirement for NOAA, though proposal suggested hurricane tracking application
- Strong emphasis on navigation redundancy as critical requirement for safe autonomous UAS operations in National Airspace System