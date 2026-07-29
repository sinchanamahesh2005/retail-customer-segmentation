import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ==========================================================
# CUSTOMER SEGMENTATION USING RFM + K-MEANS
# ==========================================================

print("=" * 60)
print("CUSTOMER SEGMENTATION")
print("=" * 60)

# ==========================================================
# Load RFM Dataset
# ==========================================================

file_path = r"D:\RetailAnalytics\data\processed\rfm.csv"

rfm = pd.read_csv(
    file_path,
    index_col=0
)

print("\nFirst 5 Customers")
print(rfm.head())

print("\nDataset Shape:")
print(rfm.shape)

# ==========================================================
# Feature Scaling
# ==========================================================

print("\n" + "=" * 60)
print("FEATURE SCALING")
print("=" * 60)

rfm_features = rfm[["Recency", "Frequency", "Monetary"]]

scaler = StandardScaler()

rfm_scaled = scaler.fit_transform(rfm_features)

print("\nScaled Data Shape:")
print(rfm_scaled.shape)

print("\nFirst 5 Scaled Rows:")
print(rfm_scaled[:5])

# ==========================================================
# Elbow Method
# ==========================================================

print("\n" + "=" * 60)
print("ELBOW METHOD")
print("=" * 60)

wcss = []

for k in range(1, 11):

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    kmeans.fit(rfm_scaled)

    wcss.append(kmeans.inertia_)

print("\nWCSS Values")

for i, value in enumerate(wcss, start=1):
    print(f"K = {i} : {value:.2f}")

# Plot Elbow Graph

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, 11),
    wcss,
    marker="o",
    linewidth=2
)

plt.title("Elbow Method")

plt.xlabel("Number of Clusters (K)")

plt.ylabel("WCSS")

plt.grid(True)

plt.savefig(
    r"D:\RetailAnalytics\report\elbow_method.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nElbow graph saved successfully!")

# ==========================================================
# Final K-Means Model
# ==========================================================

print("\n" + "=" * 60)
print("FINAL K-MEANS MODEL")
print("=" * 60)

optimal_clusters = 4

kmeans = KMeans(
    n_clusters=optimal_clusters,
    random_state=42,
    n_init=10
)

rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

print("\nCluster Counts")

print(
    rfm["Cluster"]
    .value_counts()
    .sort_index()
)

# ==========================================================
# Cluster Summary
# ==========================================================

cluster_summary = (
    rfm
    .groupby("Cluster")
    .agg({
        "Recency": "mean",
        "Frequency": "mean",
        "Monetary": "mean"
    })
    .round(2)
)

print("\n" + "=" * 60)
print("CLUSTER SUMMARY")
print("=" * 60)

print(cluster_summary)

cluster_summary.to_csv(
    r"D:\RetailAnalytics\data\processed\cluster_summary.csv"
)

print("\nCluster Summary saved successfully!")

# ==========================================================
# Assign Business Labels
# ==========================================================

cluster_names = {

    0: "Regular Customers",

    1: "Lost Customers",

    2: "VIP Customers",

    3: "Loyal Customers"

}

rfm["Customer_Segment"] = rfm["Cluster"].map(cluster_names)

print("\n" + "=" * 60)
print("CUSTOMER SEGMENTS")
print("=" * 60)

print(
    rfm[
        [
            "Cluster",
            "Customer_Segment"
        ]
    ].head()
)

# ==========================================================
# Save Final Dataset
# ==========================================================

rfm.to_csv(
    r"D:\RetailAnalytics\data\processed\customer_segments.csv",
    index=True
)

print("\nCustomer Segments saved successfully!")

# ==========================================================
# Final Summary
# ==========================================================

print("\n" + "=" * 60)
print("PROJECT SUMMARY")
print("=" * 60)

print(f"Customers Processed : {len(rfm)}")
print(f"Clusters Created    : {rfm['Cluster'].nunique()}")

print("\nGenerated Files")

print("-----------------------------------")

print("customer_segments.csv")

print("cluster_summary.csv")

print("elbow_method.png")

print("\nCustomer Segmentation Completed Successfully!")

print("=" * 60)