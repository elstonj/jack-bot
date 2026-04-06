# Internal Intelligence Report #1: Image Segmentation Techniques Overview

## Document Metadata
- Type: Internal research report / technical investigation
- Client/Agency: NASA (SBIR program)
- Program/Solicitation: 2017 SBIR Phase II
- Date: 2019-12-26 (created); 2020-06-10 (last modified)
- BST Products/Systems Referenced: NVIDIA Tx2 (aerial platform), BST aerial imagery datasets
- Key Personnel: Not named in document

## Executive Summary
This internal intelligence report documents BST's investigation into semantic image segmentation techniques for aerial imagery analysis, with focus on deployment to the NVIDIA Tx2 embedded platform. The report evaluates three semantic segmentation frameworks (Deeplab, SegNet, and alternative approaches), establishes development environments on local machines and AWS, and tests aerial-specific semantic segmentation toolsets (Raster-Vision, DeepNetsForEO, RoboSat) on BST imagery data.

## Technical Approach

### Semantic Segmentation Frameworks Evaluated:

**Deeplab v3**
- Built on TensorFlow framework
- Uses Google's MobileNet v2 neural network backbone for edge device deployment
- Key architecture features: depth-wise separable convolutions and learned data compression
- Pre-trained models available (tested on PASCAL VOC 2012 dataset with 20 terrestrial classes)
- Strong scale invariance built into architecture

**SegNet**
- Built on Caffe framework (competing framework to TensorFlow)
- Pre-trained demo available via website
- Different approach than Deeplab: attempts to classify everything into known classes vs. allowing "background" class
- Default NVIDIA Tx2 implementation available

**Tiramisu**
- Noted as alternative but not investigated in depth

### Development & Deployment Environments:

**Local Lab Machine Setup**
- NVIDIA GPU acceleration (driver, CUDA, cuDNN)
- Titan V GPU utilized for training (12GB VRAM)
- Batch size adjustments necessary (8→4) for memory constraints

**AWS Deep Learning Instance**
- p3.2xlarge instances (16GB GPU RAM)
- Pre-configured conda environments for TensorFlow (python 3.6, 2.7) and PyTorch
- Jupyter notebook integration
- 85GB+ storage required for Potsdam dataset

**NVIDIA Tx2 Embedded Platform**
- Jetpack 3.3 deployment
- Docker containers (NVIDIA-Docker) for encapsulation
- DIGITS training environment
- TensorRT optimization on device (computationally intensive, ~30 minutes at max speed)
- jetson_clocks.sh required to achieve full performance

### Framework Conversion & Interoperability
- Models and architectures convertible between TensorFlow and Caffe using Microsoft's open-source converter and other tools
- Pre-trained models available in multiple formats

## Products & Capabilities Described

### NVIDIA Tx2 Embedded Platform
- Used for aerial platform deployment
- Performance: ~2 TOPS (tera operations per second)
- Semantic segmentation framerates: 1 FPS (with live overlay), up to 5 FPS (optimized, without overlay)
- Performance ratio: ~2.5 FPS/TOPS (comparable to iPhone XS at ~2.4 FPS/TOPS)
- Console inference time observed: 322ms per image processing
- Docker support for containerized deployments
- DIGITS native training environment

### BST Aerial Imagery Datasets
- Custom aerial image dataset used for testing and training
- Requires georeference data for processing
- RGB color space (vs. IR|R|G alternatives)
- Multiple geographical locations tested (Boulder, CO reference)

## Use Cases & Applications

**Primary Application: Aerial Landing Zone Detection**
- Semantic segmentation for runway/landing area identification
- Classes of interest: impervious surfaces (primary), low vegetation (secondary)
- Height-above-ground variations for different flight conditions

**Tested Datasets (Public):**
1. **Vaihingen, Germany** - IR|R|G multispectral data
2. **Potsdam, Germany** - IR|R|G multispectral data with 6 semantic classes (impervious, building, low vegetation, tree, car, clutter)
3. **SpaceNet, Las Vegas, US** - RGB data

**Aerial-Specific Semantic Segmentation Toolsets:**

**Raster-Vision** (Azavea)
- Default: Deeplab + MobileNet v2
- Modular architecture supporting alternative networks
- IR|R|G training by default, modified to RGB for BST testing
- Georeference data required
- AWS batch job automation (p3.2xlarge instances)
- Tested on Potsdam dataset with BST images
- Results showed correct category prediction despite errors from IR|R|G→R|G|B channel mapping and dummy georeferencing

**DeepNetsForEO** (Lighter-weight alternative)
- Default: SegNet with PyTorch
- Simpler setup than Raster-Vision
- Uses same datasets (Potsdam, Vaihingen)
- Jupyter notebook-based workflow
- IR|R|G data preference; successfully modified for RGB
- PyTorch 1.0+ compatible (original codebase used 0.3.1)
- Tested on BST images with scale sensitivity noted
- AWS deployment capability with pre-trained RGB model available
- Automatic inference capability on image datasets

**RoboSat** (Not fully investigated)
- OpenStreetMap-based automatic training data generation
- Larger/more mature toolset
- Potential for bootstrapping ground-truth data
- Recommended for future investigation

## Key Results

### Pre-trained Model Testing:
- **Deeplab on PASCAL VOC 2012**: Successfully segmented terrestrial objects; performed poorly on aerial imagery (e.g., tracked shadow rather than person when viewed from above)
- **SegNet baseline**: Different approach than Deeplab; qualitatively demonstrated different classification strategies
- **Tx2 SegNet**: Poor accuracy on both aerial and terrestrial pre-trained models; detected only 1 FPS (5 FPS without overlay)

### Custom Aerial Dataset Training:

**Raster-Vision on Potsdam RGB data:**
- Training time: ~7 hours on Titan V (0.22 seconds/step)
- Inference on BST test image showed reasonable category predictions
- "Tiling effect" observed (attributed to dummy georeferencing)
- Performance improved when training on matching color space (RGB vs. IR|R|G mismatch)

**DeepNetsForEO on Potsdam RGB data:**
- Successfully executed training and inference pipeline
- Lower accuracy identifying runway vs. Raster-Vision on same dataset
- Scale sensitivity demonstrated: rescaling BST image improved results but still underperformed vs. Raster-Vision

### Key Findings:

1. **Scale Dependency**: 
   - DeepNetsForEO and Raster-Vision show heavy scale dependency despite using scale-invariant neural networks
   - Caused by training on fixed-scale data; can be mitigated by training on variable-scale datasets
   - Deeplab and SegNet architected for scale invariance

2. **Geographic Specificity**:
   - Models trained on Potsdam, Germany dataset showed significant accuracy loss when applied to BST imagery from different geography (Boulder, CO)
   - Recommendation: As few as 10-20 labeled images representative of target geographic area would substantially improve accuracy over generic models
   - Suggested: 15 labeled images covering BST target flight area at various altitudes

3. **Multispectral Data Advantage**:
   - IR|R|G (infrared + red + green) data provides superior discrimination for vegetation classification
   - Normalized Difference Vegetation Index (NDVI) utilized by default in toolsets
   - IR and R channels better correlate object color to object type, reducing ambiguities
   - Most existing public datasets and aircraft instruments use RGB; both frameworks adapted to RGB successfully

4. **Model Quality from Pre-trained Demos**:
   - Default models from semantic segmentation demos often poorly trained
   - Example: Apple Object Detection demo "effectively unusable" even on friendly datasets
   - Recommendation: Rigorously retrained models (e.g., TensorFlow/Keras) show "worlds better" accuracy than defaults

5. **Tx2 Performance Observations**:
   - Current SegNet Tx2 implementation likely represents optimized code near theoretical device limits
   - Framerate/inference time efficiency comparable to high-end mobile processors (iPhone XS)
   - Pre-trained models likely not well-trained rather than platform limitation

## Notable Details

### AWS & Cloud Infrastructure
- AWS p3.2xlarge instance configured with complete deep learning stack
- Access credentials provided for team use (credentials in document; likely rotated since)
- Automatic instance start/stop capability for cost management
- Jupyter notebook remote access over HTTPS with custom password
- Pre-trained RGB DeepNetsForEO model available on AWS instance for immediate inference

### Data & Georeference Conversion
- VOC (Visual Object Classes) XML format widely used for semantic segmentation ground truth
- Simple RGB-value color scheme sufficient for ground-truth labeling (e.g., exact RGB for each class)
- Existing conversion scripts available for format transformation
- Photoshop or similar tools viable for manual labeling
- **Recommendation**: Write converter script for BST georeference data format to Raster-Vision format

### Labeling Tools for Ground Truth Generation
- **Labelbox**: Most promising; Photoshop-like intelligent assist features (tested auto-fill for clouds)
- **labelme**: Standard option
- **PixelAnnotationTool**: Standard option

### Docker & Containerization
- nvidia-docker v2 essential for GPU acceleration pass-through to containers
- NVIDIA pre-built Docker images significantly reduce setup burden vs. building from source
- Jetpack installer streamlines Tx2 deployment vs. manual setup on other platforms

### Future Work Recommendations (Priority-ordered in document)
1. Convert BST georeference data format to Raster-Vision expectations
2. Investigate removing georeference data requirement or real-time georeferencing in-flight
3. Script automated testing of BST datasets with DeepNetsForEO and Raster-Vision
4. Host Raster-Vision on AWS with split setup for easier data manipulation
5. Investigate training via NVIDIA DIGITS platform (native Tx2 compatibility advantage)
6. Investigate model conversion process for Raster-Vision and DeepNetsForEO to Tx2 execution
7. Investigate alternate embedded platforms (e.g., NCS2 running Deeplab at 4-5 FPS)

### Technical Debt/Known Issues
- Batch size constraints on local hardware vs. cloud instances
- Checkpoint incompatibility when changing batch sizes during training
- Georeference data handling in inference pipeline incomplete
- RGB/IR|R|G channel mismatch in initial testing
- Scale-dependent model behavior in post-processing-oriented toolsets