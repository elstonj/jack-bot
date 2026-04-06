# Surveying and Mapping with Fixed Wing UAS: A Fly-Off Between Leading UAS Providers

## Document Metadata
- **Type:** White Paper / Marketing Material
- **Client/Agency:** CH2MHill (conducted fly-off)
- **Program/Solicitation:** N/A
- **Date:** May 15, 2018
- **BST Products/Systems Referenced:** SwiftTrainer™, SwiftCore™ (Flight Management System), SwiftPilot™, SwiftStation™, SwiftTab™
- **Key Personnel:** Jack Elston (last editor)

## Executive Summary
This white paper presents a direct technical comparison of three fixed-wing UAS mapping platforms tested in an independent fly-off near Elbert, Colorado: Black Swift Technologies' SwiftTrainer™, SenseFly's Ebee, and Trimble's UX5 HP. The SwiftTrainer™ demonstrated superior performance in data quality, accuracy, and cost-effectiveness, particularly in maintaining uniform image overlap, achieving lower reprojection errors, and producing cleaner 3D elevation models without artifacts.

## Technical Approach
The comparison was conducted using:
- **Testing Protocol:** Independent contractors (not manufacturers) flew identical survey missions over the same area of interest on the same day
- **Processing:** OneButton software (Icaros) with identical settings for all three datasets
- **Evaluation Metrics:** Orthomosaic quality, elevation map accuracy, image overlap patterns, geo-tag accuracy, reprojection errors, and connection density

**Key Technical Findings:**
- **SwiftTrainer™** maintained uniform, high-density (10+ image) overlap in a regular grid pattern
- **Ebee and UX5 HP** produced irregular overlap patterns with gaps, leading to artifacts in 3D data
- SwiftTrainer™ geo-tags were highly accurate (estimated vs. calculated positions nearly identical)
- Ebee and UX5 HP showed significant deviation between autopilot-estimated and corrected image positions

## Products & Capabilities Described

### SwiftTrainer™ UAS
**What it is:** Fully autonomous fixed-wing survey and mapping platform, ready-to-fly out of box

**Specifications:**
- Area coverage: 25–600 acres per flight
- Maximum flight time: 60 minutes
- Cruise speed: 33 mph
- Weight: 6 lbs
- Wingspan: 5.5 ft
- Ground sample distance: 1 inch/pixel at 400 ft
- Mapping camera: 24MP resolution
- Image trigger rate: <1 second per image
- Maximum operational ceiling: 14,000 ft (demonstrated in Colorado)
- Launch: Hand launch
- Landing: Autonomous belly landing with advanced algorithm
- Propulsion: Electric motor

**Key Performance Advantages:**
- Time between photos: 0.9s (vs. 3.8s for Ebee, unknown for UX5)
- Mean reprojection error: 7.1cm (vs. 19.4cm for Ebee, 9.4cm for UX5)
- Photos used in processing: 99.7% (vs. 88.1% for Ebee, 95.5% for UX5)
- Average connections per image pair: 190.11 (vs. 52.17 for Ebee, 72.62 for UX5)
- Price: $ (lowest tier; Ebee $$, UX5 HP $$$$)

**Included in Package:**
- Aircraft, batteries, ground station with tripod
- Tablet computer, field toolbox, carrying case
- RC handset
- No additional computers or support equipment required

**Operations:**
- Ready-to-fly out of box
- ~5 minute pre-flight checklist
- Training requirement: ~half day for new operators
- Training included: 2 hours at BST test site near Boulder, CO (on-site training available)

### SwiftCore™ Flight Management System
**Components:**
- SwiftPilot™ (autopilot)
- SwiftStation™ (ground station)
- SwiftTab™ (user interface/tablet)
- Support electronics

**Characteristics:**
- Designed and manufactured by BST (entirely made in USA)
- Enables accurate flight tracking even in high winds
- Proprietary avionics (not open-source)
- Used and approved by NASA and NOAA
- Growing adoption by commercial survey companies

## Use Cases & Applications
- Survey and mapping operations
- Land management
- Crop damage assessment
- Large area ecological studies
- High-altitude mapping (tested up to 14,000 ft)

## Key Results (Fly-Off Comparison)

### Data Quality Comparison:
**SwiftTrainer™ Performance:**
- Produced uniform, connected elevation maps without artifacts
- 3D solution clearly showed terrain and dam structure
- 99.7% of captured images used in final product

**Ebee Performance:**
- Significant artifacts in elevation maps (middle area of data)
- Gaps in image connectivity around perimeter
- Irregular overlap patterns; only 88.1% of photos used
- Larger reprojection errors (19.4cm mean)

**UX5 HP Performance:**
- Better elevation map quality than Ebee but not as clean as SwiftTrainer™
- Gaps in perimeter connectivity
- Irregular overlap patterns
- 95.5% of photos used
- Higher reprojection error than SwiftTrainer™ (9.4cm)

### Coverage & Efficiency:
| Metric | SwiftTrainer™ | Ebee | UX5 HP |
|--------|---|---|---|
| Mission time | 29.3 min | 31.7 min | 25.8 min |
| Number of photos | 693 | 312 | 621 |
| Coverage at 120m | 600 acres | 500 acres | 250 acres |
| GSD at 120m | 2.9 cm/px | 4.4 cm/px | 1.7 cm/px |
| Maximum flight time | 60 min | 50 min | 35 min |

### Root Cause Analysis:
The SwiftTrainer™'s superior performance stemmed from three critical factors:
1. **Accurate ground tracks** – maintains strict grid spacing; deviations can cause image overlap loss
2. **Accurate geo-tags** – critical for rapid orthomosaic generation
3. **Fast image acquisition** (<1s vs. 3.8s for Ebee) – essential for 60%+ overlap at low altitudes

## Notable Details

### Competitive Positioning
- SwiftTrainer™ achieved "industry leading orthomosaics and point clouds" at the lowest price point
- Document emphasizes cost-benefit: superior data quality with significant cost savings
- Competing systems' errors can necessitate costly mission re-flights

### Regulatory & Operational Advantages
- BST has 8 years of FAA flight approval experience
- Responsible for hundreds of flight approvals, including unique/difficult missions
- SwiftTrainer™ compliant with Part 107 regulations
- Operator certification achievable in ~1 day of study
- Simple user interface enables multiple trained staff without full-time pilot requirement

### Market Differentiation
- BST manufactures proprietary avionics (vs. open-source competitors)
- Full control over electronics design, software, mechanical assembly, and QC
- Combined avionics expertise with consulting services
- ApprovedFlight.com consulting service for FAA airspace access

### Process Simplification
Four-step simplified workflow:
1. Planning and Simulation (pre-deployment planning with high-fidelity simulation)
2. Flight (~5 min setup, up to 60 min flight time)
3. In-Field Check (automatic geo-tagging, data completeness verification)
4. Data Processing (compatible with third-party software)

### Company Background
- **Location:** Boulder, CO
- **Founded:** 2011
- **Clients:** NASA, NOAA, universities, commercial survey companies, aircraft integrators
- **Services:** Product sales + consulting for FAA airspace access and certificates of authorization