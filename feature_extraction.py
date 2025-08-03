"""
feature_extraction.py

This script implements functional brain connectivity feature extraction
based on the Phase Locking Index (PLI) from EEG signals.
"""

import numpy as np

def compute_phase(signal):
    """
    Compute the instantaneous phase of a signal using FFT.

    Parameters:
        signal : numpy array (1D)

    Returns:
        phase : numpy array (1D)
    """
    fft_result = np.fft.fft(signal)
    phase = np.angle(fft_result)
    return phase


def compute_pli_matrix(eeg_data):
    """
    Calculate the Phase Locking Index (PLI) matrix for each trial.

    Parameters:
        eeg_data : numpy array (trials × channels × samples)

    Returns:
        pli_features : numpy array (trials × features) - upper triangle of PLI matrices
    """
    n_trials, n_channels, n_samples = eeg_data.shape
    pli_features = []

    for trial in range(n_trials):
        pli_matrix = np.zeros((n_channels, n_channels))
        for i in range(n_channels):
            phase_i = compute_phase(eeg_data[trial, i])
            for j in range(i + 1, n_channels):
                phase_j = compute_phase(eeg_data[trial, j])
                phase_diff = phase_i - phase_j
                pli = np.abs(np.mean(np.sign(np.sin(phase_diff))))
                pli_matrix[i, j] = pli
                pli_matrix[j, i] = pli  # symmetry
        # Flatten upper triangle (excluding diagonal) as feature vector
        upper_triangle = pli_matrix[np.triu_indices(n_channels, k=1)]
        pli_features.append(upper_triangle)

    return np.array(pli_features)
