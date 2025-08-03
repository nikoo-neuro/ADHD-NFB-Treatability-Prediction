
import numpy as np
from scipy.io import loadmat

from preprocessing import preprocess_eeg_data
from feature_extraction import compute_pli_matrix
from classification import evaluate_model

mat = loadmat('data/eeg_dataset.mat')
eeg_data_raw = mat['eeg_data']
labels = mat['labels'].flatten()

eeg_data_filtered = preprocess_eeg_data(eeg_data_raw)
pli_features = compute_pli_matrix(eeg_data_filtered)

scores = evaluate_model(pli_features, labels)
mean_acc = np.mean(scores)

print(f"Accuracy: {mean_acc * 100:.2f}%")
