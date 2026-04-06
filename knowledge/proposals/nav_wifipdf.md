# Signals of Opportunity Navigation Using Wi-Fi Signals

## Document Metadata
- Type: Thesis (Master of Science in Electrical Engineering)
- Client/Agency: Air Force Institute of Technology (AFIT) / U.S. Air Force
- Program/Solicitation: Academic thesis research (not a BST proposal or product document)
- Date: March 2011
- BST Products/Systems Referenced: None
- Key Personnel: Wilfred E. Noel, Captain USAF (author); Maj Fisher (advisor); Dr. Temple

## Executive Summary
This thesis presents a method for navigation using IEEE 802.11a/g (Wi-Fi) signals as "Signals of Opportunity" (SoOP) rather than GPS. The research develops a technique using Time Difference of Arrival (TDOA) calculations and cross-correlation of Wi-Fi signals to determine position in three-dimensional space, with testing on real-world collected Wi-Fi data demonstrating the viability of the approach under varying noise and signal strength conditions.

## Technical Approach
The thesis explores SoOP navigation by:
1. **Signal Acquisition**: Recording IEEE 802.11a/g signals in real-world environments (anechoic chamber and three outdoor locations)
2. **TDOA Calculation**: Using cross-correlation of received Wi-Fi signals from multiple stations to compute timing offsets between stations
3. **Position Solution**: Solving nonlinear TDOA equations using least squares approximation to determine 3D position
4. **Correlation Method**: Extracting "Unique Identifiers" (UI) from Wi-Fi OFDM symbols using statistical representations (mean value method and scaled differential method) to enable correlation without synchronized transmissions

## Products & Capabilities Described

### IEEE 802.11a/g Wi-Fi Signals
- **What it is**: Wireless networking signals operating at 2.4 GHz and 5 GHz bands per IEEE 802.11 standards, using OFDM (Orthogonal Frequency Division Multiplexing) modulation
- **How used**: Signals received at multiple ground stations; cross-correlation of these signals produces timing differences between stations
- **Advantages**: Widely available, non-synchronization required, already present in urban/indoor environments

### TDOA (Time Difference of Arrival) Method
- **What it is**: Navigation technique that calculates position based on time differences of signal arrival at multiple receivers
- **How used**: Measurements from 4+ Wi-Fi broadcast stations with known positions enable 3D position solution plus clock bias calculation
- **Key capability**: Does not require knowledge of signal transmission time or synchronized clocks between receivers

## Use Cases & Applications

### Primary Use Cases
1. **Indoor/Urban Navigation**: Where GPS is unavailable due to building obstruction or urban canyon effects
2. **Military Operations**: Urban and "urban-esque" environments where personnel need navigation inside structures
3. **GPS-Denied Environments**: Areas where clear sky view is impossible

### Environmental Testing
- Anechoic chamber testing (IEEE 802.11a data collection)
- Three real-world outdoor locations (IEEE 802.11g data collection)
- Simulated noise environments and degraded signal conditions

## Key Results

### Experimental Findings
1. **Window Size Impact**: Optimal performance achieved with window sizes of 50-100 symbols; larger windows reduced accuracy
2. **Noise Robustness**: Wi-Fi correlation achieved zero errors in the correlation algorithm across wide range of noise strengths (signal-to-noise variations)
3. **Signal Degradation**: System maintained accurate timing offset detection even when signal magnitude was reduced to 5-10% of original strength
4. **Position Accuracy**: TDOA position estimation demonstrated feasibility with multiple broadcast stations

### Detailed Performance Data
- **IEEE 802.11a (Anechoic Chamber)**: Tested with varying window sizes (20-500) and noise levels; percent error remained near 0% for moderate window sizes
- **IEEE 802.11g (Three Locations)**: Tested under realistic multipath conditions; showed robustness across 100% signal strength down to 5% magnitude with window size 50

### Correlation Methods Tested
- **Mean Value Method (MVM)**: Used statistical mean of OFDM symbols
- **Scaled Differential Method (SDM)**: Used differential representation scaled appropriately
- Both methods achieved reliable correlation performance

## Notable Details

1. **No Synchronization Required**: Unlike Loran-C or some SoOP methods, does not require synchronized broadcast stations or known transmission times—critical for exploiting non-navigation signals

2. **Multipath Robustness**: Successfully operated in environments with significant multipath (urban locations) where GPS would fail

3. **Scalability**: Method works with minimum 4 broadcast stations for 3D solution; performance improves with more stations (overdetermined systems solved via least squares approximation)

4. **Comparison to Prior Work**: 
   - FM radio SoOP by Kim: Similar correlation-based approach but different signal type
   - DVB-T research by Eggert: Achieved 1-meter minimum error in some cases
   - CDMA cellular by Mizusawa: Used synchronized towers; this approach exploits unsynchronized signals

5. **Theoretical Basis**: Thesis cites prior SOOP research by Velotta and Martin on general OFDM signals, showing Wi-Fi OFDM structure is suitable for TDOA exploitation

6. **Practical Implications**: 
   - No need for custom transmitters (unlike Vegni/Ciurana Wi-Fi TOA methods)
   - More practical than IP-address-based localization (Brown, Bowen) which only provides neighborhood-level accuracy
   - Exploits existing Wi-Fi infrastructure without modification

7. **Limitations Acknowledged**:
   - Multipath effects still present challenge in dense urban environments
   - Requires known positions of broadcast stations
   - Method dependent on availability of 4+ detectable Wi-Fi transmitters in area

8. **Future Work Recommendations**: Thesis suggests improvement areas including refinement of multipath handling, testing with fewer stations, and integration with other navigation sources

---

**Note**: This is an academic research thesis, not a Black Swift Technologies document or proposal. It appears to be stored in BST's reference library for background research on Wi-Fi-based navigation techniques, which may be relevant to BST's work on signal exploitation and navigation alternatives. The document contains comprehensive technical background on TDOA methods and OFDM signal analysis that could inform BST's own SoOP or alternative navigation research.