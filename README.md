# Neurofeedback Treatment Prediction in ADHD Patients

This project implements a full pipeline to predict whether a child with ADHD will respond to neurofeedback therapy, based on EEG data recorded before treatment.

The pipeline includes:

- EEG preprocessing with a bandpass filter (0.5–45 Hz)
- Feature extraction using Phase Locking Index (PLI) between brain regions
- Feature selection via electrode filtering
- Classification using an ensemble of SVM, KNN, and Decision Tree models
- Evaluation using 5-fold cross-validation

The model was trained and evaluated on a real EEG dataset containing recordings from 1200 trials (600 treatable, 600 non-treatable).

**Achieved average accuracy:** 90.6%

##  Project Structure

src/  
 preprocessing.py          # Filters EEG signals using Butterworth bandpass filter  
 feature_extraction.py     # Computes PLI-based connectivity features  
 classification.py         # Ensemble classifier (SVM + KNN + DecisionTree)  
 main.py                   # Runs the full pipeline  

##  Dataset

The EEG data was recorded from 32 channels, 550 samples per trial, at 500 Hz.  
Labels: 1 = treatable, 0 = non-treatable

Data format: `data/eeg_dataset.mat`  
Variables expected: `eeg_data`, `labels`

##  Reference

Based on the article:  
**Prediction of Success in Neurofeedback Treatment for ADHD Before Starting Treatment**  
Authors: Nikoo Khanahmadi, Mohammad Reza Yousefi  
*Journal of Intelligent Procedures in Electrical Technology (2025)*

##  Requirements

- Python 3.8+
- numpy
- scipy
- scikit-learn

Install dependencies with:

pip install -r requirements.txt

##  Contact

If you have questions or want to collaborate, feel free to reach out:  
nikoo.ahmadi92@gmail.com

