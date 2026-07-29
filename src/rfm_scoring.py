import pandas as pd

# =====================================
# Load RFM Dataset
# =====================================

rfm = pd.read_csv(
    r"D:\RetailAnalytics\data\processed\rfm.csv",
    index_col=0
)

print("=" * 60)
print("RFM SCORING")
print("=" * 60)

print(rfm.head())

print("\nSummary Statistics")
print(rfm.describe())

# =====================================
# Calculate RFM Scores
# =====================================

# Recency
rfm["R_Score"] = pd.qcut(
    rfm["Recency"],
    q=5,
    labels=[5, 4, 3, 2, 1]
)

# Frequency
rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    q=5,
    labels=[1, 2, 3, 4, 5]
)

# Monetary
rfm["M_Score"] = pd.qcut(
    rfm["Monetary"],
    q=5,
    labels=[1, 2, 3, 4, 5]
)

print("\nRFM Scores")
print(rfm.head())

print("\nR Score Distribution")
print(rfm["R_Score"].value_counts().sort_index())

print("\nF Score Distribution")
print(rfm["F_Score"].value_counts().sort_index())

print("\nM Score Distribution")
print(rfm["M_Score"].value_counts().sort_index())

_, bins = pd.qcut(
    rfm["Recency"],
    q=5,
    retbins=True,
    duplicates="drop"
)

print("Recency Bin Edges:")
print(bins)