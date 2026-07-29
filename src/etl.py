import pandas as pd

# =====================================
# Read Cleaned Dataset
# =====================================

file_path = r"D:\RetailAnalytics\data\processed\cleaned_retail_data.csv"

df = pd.read_csv(file_path)

print("=" * 50)
print("RETAIL ANALYTICS ETL PIPELINE")
print("=" * 50)

print("\nDataset Shape:", df.shape)
print(df.head())

# =====================================
# Extract Customers Table
# =====================================

customers = (
    df[["Customer ID", "Country"]]
    .drop_duplicates(subset=["Customer ID"], keep="first")
    .sort_values("Customer ID")
)

# Convert Customer ID to integer
customers["Customer ID"] = customers["Customer ID"].astype(int)

# Rename columns to match MySQL table
customers = customers.rename(columns={
    "Customer ID": "customer_id",
    "Country": "country"
})

print("\n" + "=" * 50)
print("CUSTOMERS TABLE")
print("=" * 50)
print(customers.head())
print("\nTotal Customers:", len(customers))

# =====================================
# Extract Products Table
# =====================================

products = (
    df[["StockCode", "Description", "Price"]]
    .drop_duplicates(subset=["StockCode"], keep="first")
    .sort_values("StockCode")
)

products = products.rename(columns={
    "StockCode": "product_id",
    "Description": "product_name",
    "Price": "unit_price"
})

print("\n" + "=" * 50)
print("PRODUCTS TABLE")
print("=" * 50)
print(products.head())
print("\nTotal Products:", len(products))

# =====================================
# Extract Orders Table
# =====================================

orders = (
    df[["Invoice", "Customer ID", "InvoiceDate"]]
    .drop_duplicates(subset=["Invoice"], keep="first")
    .sort_values("Invoice")
)

orders["Customer ID"] = orders["Customer ID"].astype(int)

orders = orders.rename(columns={
    "Invoice": "order_id",
    "Customer ID": "customer_id",
    "InvoiceDate": "order_date"
})

print("\n" + "=" * 50)
print("ORDERS TABLE")
print("=" * 50)
print(orders.head())
print("\nTotal Orders:", len(orders))

# =====================================
# Extract Order Items Table
# =====================================

order_items = df[["Invoice", "StockCode", "Quantity", "Price"]].copy()

# Generate unique Order Item ID
order_items.insert(
    0,
    "order_item_id",
    range(1, len(order_items) + 1)
)

order_items = order_items.rename(columns={
    "Invoice": "order_id",
    "StockCode": "product_id",
    "Quantity": "quantity",
    "Price": "unit_price"
})

print("\n" + "=" * 50)
print("ORDER ITEMS TABLE")
print("=" * 50)
print(order_items.head())
print("\nTotal Order Items:", len(order_items))

# =====================================
# ETL SUMMARY
# =====================================

print("\n" + "=" * 50)
print("ETL SUMMARY")
print("=" * 50)

print(f"Customers   : {len(customers)}")
print(f"Products    : {len(products)}")
print(f"Orders      : {len(orders)}")
print(f"Order Items : {len(order_items)}")

# =====================================
# Data Validation
# =====================================

print("\nRunning Data Validation...")

print("Duplicate Customer IDs:",
      customers["customer_id"].duplicated().sum())

print("Duplicate Product IDs:",
      products["product_id"].duplicated().sum())

print("Duplicate Order IDs:",
      orders["order_id"].duplicated().sum())

print("Duplicate Order Item IDs:",
      order_items["order_item_id"].duplicated().sum())

print("\nETL Transformation Completed Successfully!")

# =====================================
# Save Processed Tables
# =====================================

customers.to_csv(
    r"D:\RetailAnalytics\data\processed\customers.csv",
    index=False
)

products.to_csv(
    r"D:\RetailAnalytics\data\processed\products.csv",
    index=False
)

orders.to_csv(
    r"D:\RetailAnalytics\data\processed\orders.csv",
    index=False
)

order_items.to_csv(
    r"D:\RetailAnalytics\data\processed\order_items.csv",
    index=False
)

print("\nCSV files created successfully!")