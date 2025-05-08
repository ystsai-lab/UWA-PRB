# UWA-PRB

## Abstract

Underwater imaging faces challenges such as light attenuation, scattering, and water turbidity, which degrade image quality and hinder accurate organism recognition. The Detecting Underwater Objects dataset, with resolutions from 586×482 to 3840×2160 pixels, highlights significant object scale variation, including a high proportion of small objects (27.38%).

This study introduces the **Under Water Attention-Parallel Residual Bi-Fusion Feature Pyramid Network** model, which improves detection accuracy for small and medium-sized objects in complex underwater environments.

The proposed model incorporates a **Spatial Pyramid Pooling** module with attention mechanisms to enhance multi-scale feature representation and integrates the **Normalized Wasserstein Distance** into the loss function for better detection flexibility.

Experimental results demonstrate that the model outperforms state-of-the-art methods, achieving:
- A **mean average precision (mAP) at IoU = 0.5** of **88.8%**
- A **mAP at IoU = 0.5:0.95** of **68.3%**, representing a **2.5–9%** improvement over baseline models
- A **precision** of **85.5%**, **recall** of **82.9%**, and an **F1-score** of **0.8417**

These results highlight the model’s robustness and effectiveness, offering significant contributions to:
- Underwater biodiversity studies
- Environmental assessments
- Marine ecosystem management

By addressing scale variability and achieving high accuracy even for rare species such as **scallops**, the proposed model supports practical applications in **underwater monitoring and conservation**.


## Installation

Make sure you are using **Python 3.8 or later**. Install all required dependencies using the following command:

```bash
pip install -r requirements.txt
```

If you are using an NVIDIA GPU, ensure that the appropriate CUDA drivers are installed for compatibility with the prebuilt versions of torch, torchvision, and torchaudio (e.g., +cu117).

## Training

To train the UWA-PRB model from scratch using the provided dataset and configuration file:

```bash
--workers
8
--device
0
--batch-size
4
--data
YOUR_DATAPATH_HERE.yaml
--epochs
300
--img
640
640
--cfg
/UWA-PRB-OwOb/cfg/UWA-PRB.yaml
--weights
weights/yolov7.pt
--name
uwa-prb-test
--hyp
data/hyp.scratch.p5.yaml
```

## Dataset

The following datasets are used to train and evaluate the model:
- **[Detecting Underwater Objects (DUO)](https://paperswithcode.com/dataset/duo)** 
- **[Rethinking general underwater object detection (RUOD)](https://universe.roboflow.com/cttlab/ruod-copy)** 

## Citation
Tsai, Y. S., Tsai, C. T., & Huang, J. H. (2025). Multi-scale detection of underwater objects using attention mechanisms and normalized Wasserstein distance loss. The Journal of Supercomputing, 81(6), 1-33.

