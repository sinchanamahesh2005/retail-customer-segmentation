import pandas as pd

# Load Cleaned Dataset
file_path = r"D:\RetailAnalytics\data\processed\cleaned_retail_data.csv"

df = pd.read_csv(file_path)

print("RFM ANALYSIS")

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
print(df.dtypes)

df["TotalAmount"] = df["Quantity"] * df["Price"]
print(df[["Quantity", "Price", "TotalAmount"]].head())

reference_date = df["InvoiceDate"].max()

print("\nReference Date:")
print(reference_date)

# =====================================
# Calculate RFM Metrics
# =====================================

rfm = df.groupby("Customer ID").agg({
    "InvoiceDate": lambda x: (reference_date - x.max()).days,
    "Invoice": "nunique",
    "TotalAmount": "sum"
})

# Rename columns
rfm.columns = ["Recency", "Frequency", "Monetary"]

# Convert Customer ID to integer
rfm.index = rfm.index.astype(int)

print("\n" + "=" * 60)
print("RFM TABLE")
print("=" * 60)

print(rfm.head())

print("\nTotal Customers:", len(rfm))

# Save RFM Table

rfm.to_csv(
    r"D:\RetailAnalytics\data\processed\rfm.csv"
)

print("\nRFM table saved successfully!")