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
