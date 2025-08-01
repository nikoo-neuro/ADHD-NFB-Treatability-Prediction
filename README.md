# ADHD-NFB-Treatability-Prediction
 EEG-based prediction of neurofeedback responsiveness in ADHD using functional connectivity features.

This repository contains the methodology, explanation, and article PDF for our research titled:

 **"Prediction of Success in Neurofeedback Treatment for Attention-Deficit Hyperactivity Disorder before Starting Treatment"**  
 *By: Nikoo Khanahmadi, M.Sc.*  
 *Supervised by: Dr. Mohammad Reza Yousefi*  
 *Islamic Azad University, Najafabad Branch*


##  Abstract

In this research, we propose a method to **predict the responsiveness of ADHD patients to neurofeedback therapy before treatment starts**, using EEG signal analysis and functional connectivity features.

We analyzed EEG data from **60 children aged 7–14 years**, extracted coherence-based features (specifically alpha and beta bands), and classified patients as **treatable or non-treatable** using **Linear Discriminant Analysis (LDA)**.



##  Methodology Overview

- **Data**: EEG recordings during 5-minute neurofeedback stimulation (F3, F4, C3, C4, P3, P4, O1, O2)
- **Preprocessing**: Filtering (0.5–45 Hz), artifact removal, segmentation
- **Feature Extraction**: Coherence-based Functional Connectivity Index (FCI)
- **Classification**: LDA model trained on extracted FCI values
- **Outcome**: Predicts treatability before therapy starts


##  Results

| Metric        | Value  |
|---------------|--------|
| Accuracy      | 83.3%  |
| Sensitivity   | 85.7%  |
| Specificity   | 80.0%  |
| AUC           | 0.87   |

##  Repository Contents

 data/ → EEG data samples (simulated or anonymized)
 preprocessing/ → MATLAB scripts for signal cleaning
 features/ → FCI computation code
 classifier/ → LDA training and evaluation
 Article.pdf → Full-text PDF of the research


##  Citation

If you use this code or methodology, please cite our work:

  title={Prediction of Success in Neurofeedback Treatment for ADHD Before Starting Therapy},
  author={Nikoo Khanahmadi and Mohammad Reza Yousefi},
  year={2025},
  affiliation={Islamic Azad University, Najafabad}

 Contact
For collaborations, questions, or code access, feel free to reach out:

 nikoo.ahmadi92@gmail.com
 
 GitHub: nikoo-neuro


