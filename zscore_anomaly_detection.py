import numpy as np

# Step 1: Sample transaction data
transaction_amounts = np.array([50, 45, 60, 55, 48, 52, 47, 5000, 58, 51, -2000])

# Step 2: Calculate statistics
mean_amount = np.mean(transaction_amounts)
std_amount = np.std(transaction_amounts)

# Step 3: Calculate Z-score for each transaction, one at a time
z_scores = []
for amount in transaction_amounts:
    z = float((amount - mean_amount) / std_amount)  # convert to plain Python float
    z_scores.append(z)

# Step 4: Check each Z-score against the threshold
threshold = 3
flagged_transactions = []

for i in range(len(transaction_amounts)):
    if abs(z_scores[i]) > threshold:
        flagged_transactions.append(transaction_amounts[i])

# Step 5: Print results
print(f"Mean: {mean_amount:.2f}")
print(f"Std Dev: {std_amount:.2f}")
print(f"Z-scores: {[round(z, 2) for z in z_scores]}")
print(f"🚩 Flagged transactions: {flagged_transactions}")