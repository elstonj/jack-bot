# Variable Winds on Venus Mapped in Three Dimensions

## Document Metadata
- Type: Peer-reviewed scientific journal article
- Publication: Geophysical Research Letters, Vol. 35, L13204
- Date: Published July 10, 2008 (received February 29, 2008; accepted June 2, 2008)
- Instrument/Mission: VIRTIS (Visible and InfraRed Thermal Imaging Spectrometer) on Venus Express (VEX)
- Lead Author: A. Sánchez-Lavega (Universidad del País Vasco, Bilbao, Spain)
- BST Connection: Referenced in 2018 NASA SBIR Phase I Venus proposal materials (Jack Elston added to library)

## Executive Summary
This paper presents the first comprehensive three-dimensional wind measurements of Venus's cloud layers using cloud tracking analysis of VIRTIS images from Venus Express, obtained between April 2006 and June 2007. The study maps zonal and meridional wind velocities at three altitude levels within the cloud layers and identifies key wind structure characteristics, including super-rotation at low latitudes, vertical wind shear patterns, poleward meridional circulation consistent with Hadley cell dynamics, and solar tide effects at high latitudes.

## Observational Data & Methodology

### Instrument & Orbital Parameters
- **Venus Express**: Highly elliptical polar orbit (apocenter 60,000 km over South Pole; pericenter 250 km over North Pole); 24-hour orbital period
- **VIRTIS Observations**: April 2006–June 2007
- **Cloud Tracking Method**: Identified cloud features across 20–74 minute image pairs
- **Total Cloud Elements Tracked**: 625 at 380 nm; 662 at 980 nm; 932 at 1.74 μm

### Three-Altitude Measurement Levels
1. **Upper Cloud (Dayside, 380 nm UV)**: 62–70 km altitude (~66 km nominal)
2. **Upper Cloud Base (Dayside, 980 nm near-infrared)**: 58–64 km altitude (~61 km nominal)
3. **Lower Cloud (Nightside, 1.74–2.3 μm infrared)**: 44–48 km altitude (~47 km nominal)

### Measurement Uncertainty
- Polar and mid-latitudes (30°S–90°S): ±4–12 m/s systematic uncertainty per tracked feature
- Equatorial latitudes (30°S–0°): ±13–20 m/s systematic uncertainty
- Mean RMS scatter: ±9 m/s for meridional velocity measurements
- Error bars in figures: ±10 m/s (standard deviation within each 2° latitude bin)

## Key Findings

### Zonal Winds (Westward Super-Rotation)

**Low Latitudes (0°–55°S):**
- Nearly constant with latitude
- Upper cloud (66 km): mean velocity ⟨u⟩ = 102 ± 10 m/s
- Upper cloud base (61 km): ⟨u⟩ = 62 ± 10 m/s (showing possible temporal variation; earlier April 2006 showed ~75 m/s closer to Galileo measurements)
- Lower cloud (47 km): ⟨u⟩ = 60 ± 10 m/s

**High Latitudes (55°S–90°S):**
- Wind speeds decrease linearly toward pole
- Drop to zero velocity at pole
- Meridional shear: ∂⟨u⟩/∂y = 0.026 m/s per km (upper cloud), 0.021 m/s per km (lower cloud)
- Indicates vertically coherent vortex structure with minimal vertical wind shear (∂⟨u⟩/∂z ~ 2 m/s per km or lower)

### Vertical Wind Shear
- **Equatorial/mid-latitudes (0°–55°S)**: ∂⟨u⟩/∂z = 8 ± 2 m/s per km between 61 and 66 km; <1 m/s per km between 47 and 61 km
- **Subpolar latitudes (50°S–60°S to pole)**: ∂⟨u⟩/∂z ≤ 2 m/s per km (weak or no shear)

### Meridional Winds (Poleward Motion)
- **Upper cloud (66 km)**: Increases from 0 m/s at equator to ~10 m/s peak at 55°S, then decreases to 0 m/s poleward
  - Interpreted as upper branch of Hadley circulation
  - Peak speed and rapid decrease toward pole related to polar vortex structure
- **Upper cloud base (61 km) and lower cloud (47 km)**: Mean values <5 m/s with no conclusive latitudinal trend due to measurement uncertainty

### Solar Tide Effect
- **Detection**: Present at high latitudes (50°S–75°S) in zonal wind at upper cloud level (66 km)
- **Magnitude**: ~2.5 ± 0.5 m/s/hr wind speed increase from morning (9 hr local time) to afternoon (15 hr)
- **Wave amplitude**: ~10 m/s
- **Altitude Confinement**: Confined to near cloud tops; not detected at 61 km level or on nightside at 47 km
- **Latitude Distribution**: Stronger at high latitudes than at equator (differs from some previous reports)

## Consistency with Previous Missions

The study compares results with:
- **Pioneer Venus** (1979–1985, 1990): Cloud tracking and in situ entry probe data
- **Galileo** (1990 Flyby): Cloud tracking northern hemisphere and equatorial measurements
- **Vega Balloons**: Middle-cloud drift measurements
- **Mariner 10**: Flyby cloud tracking

Finding: VIRTIS zonal wind profiles (2006–07) are broadly consistent with measurements from 1979–85, 1990, and earlier 2006 Galileo comparisons, within measurement uncertainties. Tentative detection of ~10 m/s decrease in mean equatorial speed at 61 km from April 2006 to later observations requires confirmation.

## Structural Conclusions

1. **Latitudinal Transition at ~55°S**: Sharp change in wind circulation character
   - Equatorward: Nearly constant zonal winds with strong vertical shear
   - Poleward: Linear decrease to pole with minimal vertical shear and vertically coherent vortex structure

2. **Polar Dipole Feature**: Vortex structure extends to poles forming dipolar feature observed at cloud tops

3. **Hadley Cell Dynamics**: Meridional wind pattern at upper cloud level consistent with upper branch of Hadley circulation; lower return branch not clearly detected at lower cloud level (may be below measurement sensitivity or weaker than 5 m/s)

## Notable Technical Details

- **Spatial Resolution**: Variable 15–105 km/pixel due to orbital characteristics and instrument constraints
- **Image Processing**: Defect correction, contrast enhancement, navigation, cylindrical and polar map projections
- **Homogeneous Dataset**: First study using same instrument with consistent methodology to retrieve winds at three wavelengths/altitudes
- **Temporal Coverage**: 14-month span allowed identification of both mean wind structure and temporal variability

## Relevance to Black Swift

This paper was included in BST's 2018 NASA SBIR Phase I Venus proposal reference materials, indicating its relevance to BST's proposed Venus atmospheric science mission. The three-dimensional wind mapping and cloud-tracking methodology documented here establishes baseline atmospheric characterization for Venus that would inform aerial platform operations and sensor design for BST systems proposed for Venus science missions.