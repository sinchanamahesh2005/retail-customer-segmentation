import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# CUSTOMER SEGMENT VISUALIZATION
# ==========================================================

print("=" * 60)
print("CUSTOMER SEGMENT VISUALIZATION")
print("=" * 60)

# ==========================================================
# Load Customer Segments
# ==========================================================

rfm = pd.read_csv(
    r"D:\RetailAnalytics\data\processed\customer_segments.csv",
    index_col=0
)

print("\nFirst 5 Customers")

print(rfm.head())

print("\nDataset Shape:")

print(rfm.shape)

# ==========================================================
# Customer Distribution
# ==========================================================

print("\n" + "=" * 60)
print("CUSTOMER DISTRIBUTION")
print("=" * 60)

segment_counts = (
    rfm["Customer_Segment"]
    .value_counts()
)

print(segment_counts)

plt.figure(figsize=(9,5))

segment_counts.plot(
    kind="bar",
    edgecolor="black"
)

plt.title(
    "Customer Distribution by Segment",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Customer Segment")

plt.ylabel("Number of Customers")

plt.xticks(rotation=15)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    r"D:\RetailAnalytics\report\customer_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("\nCustomer Distribution chart saved successfully!")

# ==========================================================
# Average RFM Values
# ==========================================================

print("\n" + "=" * 60)
print("AVERAGE RFM VALUES")
print("=" * 60)

average_rfm = (
    rfm
    .groupby("Customer_Segment")[
        ["Recency","Frequency","Monetary"]
    ]
    .mean()
)

print(average_rfm.round(2))

# ==========================================================
# Average Recency
# ==========================================================

plt.figure(figsize=(8,5))

average_rfm["Recency"].sort_values().plot(
    kind="bar",
    edgecolor="black"
)

plt.title(
    "Average Recency by Customer Segment",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Customer Segment")

plt.ylabel("Average Recency (Days)")

plt.xticks(rotation=15)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    r"D:\RetailAnalytics\report\average_recency.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Average Recency chart saved successfully!")

# ==========================================================
# Average Frequency
# ==========================================================

plt.figure(figsize=(8,5))

average_rfm["Frequency"].sort_values().plot(
    kind="bar",
    edgecolor="black"
)

plt.title(
    "Average Purchase Frequency by Customer Segment",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Customer Segment")

plt.ylabel("Average Frequency")

plt.xticks(rotation=15)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    r"D:\RetailAnalytics\report\average_frequency.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Average Frequency chart saved successfully!")

# ==========================================================
# Average Monetary
# ==========================================================

plt.figure(figsize=(8,5))

average_rfm["Monetary"].sort_values().plot(
    kind="bar",
    edgecolor="black"
)

plt.title(
    "Average Monetary Value by Customer Segment",
    fontsize=15,
    fontweight="bold"
)

plt.xlabel("Customer Segment")

plt.ylabel("Average Monetary Value")

plt.xticks(rotation=15)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.5
)

plt.tight_layout()

plt.savefig(
    r"D:\RetailAnalytics\report\average_monetary.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Average Monetary chart saved successfully!")

# ==========================================================
# Summary
# ==========================================================

print("\n" + "=" * 60)
print("VISUALIZATION SUMMARY")
print("=" * 60)

print("Generated Charts:")

print("--------------------------------")

print("customer_distribution.png")

print("average_recency.png")

print("average_frequency.png")

print("average_monetary.png")

print("\nVisualization Completed Successfully!")

# ==========================================================
# Customer Segments Scatter Plot
# ==========================================================

print("\n" + "=" * 60)
print("CUSTOMER SEGMENTS SCATTER PLOT")
print("=" * 60)

plt.figure(figsize=(10, 7))

colors = {
    "Regular Customers": "blue",
    "Lost Customers": "red",
    "VIP Customers": "gold",
    "Loyal Customers": "green"
}

for segment in rfm["Customer_Segment"].unique():

    data = rfm[rfm["Customer_Segment"] == segment]

    plt.scatter(
        data["Monetary"],
        data["Frequency"],
        label=segment,
        alpha=0.7,
        s=60,
        color=colors[segment]
    )

plt.title(
    "Customer Segmentation using K-Means",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Monetary Value")

plt.ylabel("Purchase Frequency")

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    r"D:\RetailAnalytics\report\customer_segments_scatter.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Customer Segments Scatter Plot saved successfully!")

# ==========================================================
# Revenue Contribution by Segment
# ==========================================================

print("\n" + "=" * 60)
print("REVENUE CONTRIBUTION")
print("=" * 60)

segment_revenue = (
    rfm.groupby("Customer_Segment")["Monetary"]
    .sum()
    .sort_values(ascending=False)
)

print(segment_revenue.round(2))

plt.figure(figsize=(9,5))

segment_revenue.plot(
    kind="bar",
    edgecolor="black"
)

plt.title(
    "Total Revenue by Customer Segment",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Customer Segment")

plt.ylabel("Total Revenue")

plt.xticks(rotation=15)

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    r"D:\RetailAnalytics\report\revenue_by_segment.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Revenue Contribution chart saved successfully!")