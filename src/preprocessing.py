"""
preprocessing.py

Preprocessing stage of EEG signal for ADHD neurofeedback prediction.
Includes Butterworth bandpass filter to isolate relevant brainwave frequencies.
"""

import numpy as np
from scipy.signal import butter, filtfilt

def bandpass_filter(signal, lowcut=0.5, highcut=45.0, fs=500, order=5):
    """
    Apply a bandpass filter (0.5–45 Hz) to a 1D EEG signal.

    Parameters:
        signal : numpy array (1D)
        lowcut : float (Hz) - lower bound of the filter
        highcut: float (Hz) - upper bound of the filter
        fs     : int - sampling frequency in Hz
        order  : int - order of the Butterworth filter

    Returns:
        filtered_signal : numpy array
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist

    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, signal)


def preprocess_eeg_data(eeg_data, fs=500):
    """
    Apply bandpass filtering to all channels of all EEG trials.

    Parameters:
        eeg_data : numpy array (shape: trials × channels × samples)
        fs       : sampling frequency (Hz)

    Returns:
        eeg_data_filtered : numpy array of the same shape
    """
    n_trials, n_channels, n_samples = eeg_data.shape
    eeg_data_filtered = np.zeros_like(eeg_data)

    for trial in range(n_trials):
        for channel in range(n_channels):
            eeg_data_filtered[trial, channel] = bandpass_filter(
                eeg_data[trial, channel], fs=fs
            )

    return eeg_data_filtered
