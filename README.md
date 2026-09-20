# Anomaly Detection with Z-Scores

A Python script that detects unusual (anomalous) transactions in a dataset using Z-score statistical analysis.

## How it works
- Calculates the mean and standard deviation of a list of transaction amounts
- Computes the Z-score for each transaction (how many standard deviations it is from the mean)
- Flags any transaction whose Z-score exceeds a threshold (default: 3) as an anomaly

## How to run
```bash
python zscore_anomaly_detection.py
```

## What I learned
- Using NumPy (`np.mean`, `np.std`) for quick statistical calculations on an array
- Understanding Z-scores as a way to measure how unusual a data point is relative to the rest of the dataset
- Using a threshold-based approach to flag outliers, a common technique in fraud/anomaly detection

## Dependencies
Requires NumPy:
```bash
pip install numpy
```
