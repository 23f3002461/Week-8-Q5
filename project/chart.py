import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Styling ---
sns.set_style("whitegrid")
sns.set_context("talk")

# --- Generate synthetic customer engagement data ---
np.random.seed(42)

data = pd.DataFrame({
    "Customer_Satisfaction": np.random.normal(8, 1.2, 300),
    "Purchase_Frequency": np.random.normal(5, 1.5, 300),
    "Time_On_App": np.random.normal(20, 6, 300),
    "Referral_Rate": np.random.normal(3, 1.1, 300),
    "Support_Interactions": np.random.normal(2, 0.8, 300),
})

# --- Compute correlation matrix ---
corr_matrix = data.corr()

# --- Create heatmap ---
plt.figure(figsize=(8, 8))  # Creates 512x512 with dpi=64
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="RdYlGn",
    linewidths=0.5,
    square=True,
    cbar=True
)

plt.title("Customer Engagement Correlation Matrix", fontsize=18)
plt.tight_layout()

# --- Export exactly 512x512 px ---
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
