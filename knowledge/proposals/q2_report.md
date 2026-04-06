# Q2 Report: NASA SBIR Phase II - Internal Intelligence Project

## Document Metadata
- **Type:** Quarterly Progress Report (Q2)
- **Client/Agency:** NASA
- **Program/Solicitation:** NASA SBIR Phase II - Internal Intelligence
- **Date:** October 2018 (covering Q2 activities; report created 2018-10-08, modified 2018-12-20)
- **BST Products/Systems Referenced:** S1, S2, Node Core, actuator nodes, battery management nodes
- **Key Personnel:** Multiple PI and engineering staff (names redacted); Dan Connors (consultant)

## Executive Summary

This Q2 report documents Black Swift Technologies' progress on a Phase II NASA SBIR project focused on developing hardware failure detection, autonomous diagnostics, and safe landing zone identification for small UAS. The team developed relational and time series databases for historical flight data (12 GB backlog spanning 2016-2018), created accelerated post-processing tools (100x speedup), and designed a hierarchical vision system for obstacle detection and safe landing identification. Total cumulative costs through October 13, 2018 were $156,318.58 with 25% physical completion estimated.

## Technical Approach

### Hardware & Firmware Development
- Worked with manufacturers (electronic speed controller and servo suppliers) to develop UART-based communication interfaces with updated hardware
- Enables higher-fidelity control and telemetry gathering for proper system monitoring
- Node Core firmware updated with these interfaces for bench testing

### Data Management Infrastructure
**Relational Database (PostgreSQL):**
- Consolidated historical flight notes metadata (aircraft type, pilots, flight parameters, failures, hardware config)
- Replaced cumbersome manual text file processing with standardized SQL queries
- Analyzed 243 flight logs; key finding: aircraft with most flight time (S1) also experienced most failures

**Time Series Database (InfluxDB):**
- Stores millions of high-rate flight messages per flight (typically 35-70 distinct message types at 100 msgs/sec)
- Schemaless field structure accommodates variability from 3 years of avionics upgrades and sensor additions
- Uploaded 12 GB of 3-year backlog (243 logs) into raw and resampled measurements
- Raw measurement: 299M points (12GB), 2,871 series; Resampled (10 Hz): 4.5M points (850MB), 239 series
- Access rates: 42k points/sec (raw), 20k points/sec (resampled)
- Demonstrated queries for RSSI vs. range correlation, link quality estimation, and failure pattern analysis

**Processing Tools:**
- Developed C++ post-processing tools wrapped in Python (100x speedup over stock Python tools)
- Handles 20 different messaging protocol versions across historical data
- Standardized tool generation based on protocol definitions enables rapid adaptation to new versions
- Processes entire 12GB backlog in minutes (vs. many hours)

### Vision System for Safe Landing Identification

**Hierarchical Two-Stage Approach:**
1. **Stage 1:** Generalized semantic classification of image tiles (coarse-grained)
2. **Stage 2:** Object segmentation for precise obstacle localization (computationally intensive, applied selectively based on Stage 1 results)

**Semantic Categories for Detection:**
Road/street, building structures, tracks/trails, vehicles, humans, water towers, powerlines, rock/mountain outcrops, tree formations, waterways, standing water, open land, vegetation/agriculture

**Training Data Sources Identified:**

*External:*
- Stanford Drone Dataset
- Mini-drone video dataset (EPFL)
- AID (Aerial Image Dataset) - benchmark for scene classification
- Inria Aerial Image Labeling Dataset
- Kaggle satellite datasets (Dstl, Draper chronology)

*Internal:*
- 16,191 images (24MP resolution) collected across 16 flight campaigns (2016-2018)
- Image sets include farmland, golf courses, construction sites, urban neighborhoods, mountains, oil fields, sand dunes
- Metadata includes aircraft state information and standard camera tags
- Images documented with obstacle inventories (powerlines, vehicles, people, structures, etc.)

### Customer Portal Development

**Web-Based Log Parsing Interface:**
- Updated from Phase I prototype to support binary log file parsing and directory generation
- Integrated automated post-processing tools for field population
- Under development: direct hooks to relational/time series databases and report generation
- Login system implemented; cybersecurity being integrated

**Command-Line Helper Tool:**
- Auto-populates standard fields in flight note entries using protocol-aware processing
- Returns formatted directories for direct addition to legacy archives

**Planned Cloud Migration:**
- Archive migration to cloud platform (from local server)
- Web tools updated for cloud storage, relational DB, and time series DB interaction
- Quick-look plots of uploaded flights with PDF download option

## Products & Capabilities Described

### S1 and S2 Aircraft
- Historical flight data analyzed; S1 has most logged flight time (>12 years of records) and most failures
- S2 equipped with monopole antenna (55° offset) showing periodic RSSI variation correlated with aircraft yaw during mapping missions

### Node Core (Actuator Instrumentation)
- Firmware development for UART-based servo and ESC control
- Telemetry gathering for system monitoring
- Bench testing planned for Q3

### Laser Range Finder (Altitude Above Ground Level sensor)
- Nominal range: 120m
- Data shows regular use starting summer 2018
- January 2018 volcanic mission in Costa Rica showed degraded performance (50m range vs. 120m expected)

### Battery and Actuator Management Nodes
- Smart battery sensor integration with Dynexus Technology for health monitoring under load
- Instrumented actuators for long-term failure mode data collection
- New servos from Hacker Motors with integrated actuator node technology

## Use Cases & Applications

**Current Testing/Development:**
- Mapping missions with S2 aircraft (straight-line passes, RSSI monitoring for link quality)
- Volcanic plume characterization missions (Costa Rica)
- Arctic operations (referenced as historical precedent)
- RC field development flights at local field (<750 m range)
- Oil field and ranch land monitoring (Oklahoma)
- Urban and suburban mapping

**Proposed Future Applications:**
- Arctic operations with improved reliability
- Volcano monitoring with extended mission capability
- Hurricane sampling (referenced in commercialization section)
- Extended operations beyond visual line of sight (BVLOS)
- GPS RTK and scanning LIDAR payload operations (cost-prohibitive today due to accident risk)
- 3D mapping in vegetation-dense areas (where photogrammetry fails)
- Fully autonomous flight without direct human oversight
- FAA safety case development for new mission types

## Key Results

### Database Implementation Results
- **Relational DB Query Speed:** 2 short SQL queries replaces custom Python script requiring file system traversal
- **Failure Analysis:** Communications failures clustered at high RSSI/range values; analysis revealed software error (not link quality) in one case via cross-referencing with flight notes
- **Antenna Pattern Validation:** Aircraft yaw-correlated RSSI variation confirmed for S2 monopole antenna, explaining periodic fluctuations in straight-line mapping flight

### Time Series Database Performance
| Parameter | Raw Measurement | Resampled Measurement |
|-----------|-----------------|----------------------|
| Points | 299M | 4.5M |
| Disk Size | 12GB | 850MB |
| Shards | 1 | 224 |
| Series | 2,871 | 239 |
| Access Rate | 42k pts/sec | 20k pts/sec |

### Processing & Data Insights
- 243 flight logs processed and uploaded (3.5 hours total upload)
- 100x speedup in log processing (from ~1 MB/s to ~100 MB/s with C++ implementation)
- Historical AGL sensor data showed usage concentrated at 75-105m AGL; limited use before summer 2018; degraded performance on volcanic mission

### Image Dataset
- 16,191 internal training images catalogued across diverse terrain types
- High resolution (24MP) requiring tile subdivision for processing tractability
- Ready for manual semantic labeling (major Q3 focus)

## Notable Details

### Commercialization & Partnerships
- **Hacker Motors:** Integrating BST's actuator node technology into new Ditex servo motors; planning custom version as premium offering
- **Dynexus Technology:** Smart battery sensor for health monitoring under load; BST providing machine learning integration for improved battery monitoring

### Flight Permission Resolution
- Original plan required NASA AFSRB review (~9 month wait, ~$8,000 cost, unbudgeted)
- Determined AFSRB not required for this SBIR since: (1) no NASA-owned aircraft/sensors, (2) no NASA personnel performing mission, (3) no NASA personnel directing mission location/timing
- Data gathered may not be flown by BST personnel (customer aircraft integration)

### Hardware Failure Testing Plan (Q3)
- Bench-level testing to point of failure for servos, batteries, ESCs, motors, propellers
- Long-term data collection for preventative maintenance algorithm development

### Cost Status
- Q1: $71,763.45 (labor, overhead, G&A, web hosting, PCB manufacturing materials)
- Q2: $84,555.13 (labor, hardware components: servos $990, batteries $1,310, ESCs $565, motors $740, PCB $3,897, hosting)
- **Total through Q2:** $156,318.58
- **Estimated Physical Completion:** 25%

### Quality Assurance on Historical Data
- 20 protocol version updates discovered across 3-year backlog; each isolated and data relabeled with correct version
- GPS time correction applied with nanosecond precision posix timestamps; correction varies by ~few milliseconds over flight

### Database Design Decisions
- **InfluxDB Tag vs. Field Structure:** Tags indexed for performance (static flight metadata, dynamic flight mode); Fields schemaless but unindexed (sensor data, GPS, accelerometer)
- **Shard Configuration:** Single 10-year shard for raw data performs better than multiple shards for full-backlog queries; performance depends on query design
- **Data Resampling:** 10Hz fixed-rate resampling using mode aggregation and zero-order/linear interpolation preserves sensor variability while enabling dense queries

### Vision System Development
- Pre-trained deep learning classifiers identified for testing on internal images
- Planned retraining on external satellite + internal datasets
- Hierarchical approach addresses embedded processor constraints by using Stage 1 (fast, coarse classification) to guide Stage 2 (slower, precise segmentation)