import pandas as pd

file_path = r"D:\RetailAnalytics\data\raw\online_retail_II.xlsx"

df = pd.read_excel(file_path, sheet_name="Year 2009-2010")

print("Original dataset shape:", df.shape)

# craete a copy
clean_df = df.copy()

# count missing customer IDs
print("\nMissing customer IDs:")
print(clean_df["Customer ID"].isnull().sum())

# remove missing cuatomer IDs
clean_df = clean_df.dropna(subset=["Customer ID"])

# verify
print("\nAfter removing missing customer IDs:")
print(clean_df.shape)

rows_removed = len(df) - len(clean_df)

print("\nRows removed:", rows_removed)
print("\nRows remaining:", len(clean_df))

cancelled_orders = clean_df["Invoice"].astype(str).str.startswith("C").sum()
print("\nCancelled invoices:", cancelled_orders)

# remove cancelled invoices
clean_df = clean_df[~clean_df["Invoice"].astype(str).str.startswith("C")]
print("\nAfter removing cancelled invoices:")
print(clean_df.shape)

# verify
print("\nRows after removing cancelled invoices:", len(clean_df))

# count rows with non-positive quantity
negative_quantity = (clean_df["Quantity"]<=0).sum()
print("\nRows with quantity <= 0:")
print(negative_quantity)

# count rows with non-positive price
negative_price = (clean_df["Price"]<=0).sum()
print("\nRows with price <= 0:")
print(negative_price)

print("\nRows with Price <= 0")
# Display all columns
pd.set_option("display.max_columns", None)

# Display full width
pd.set_option("display.width", None)

"""
# Display complete rows
print("\nRows with Price <= 0")

print(clean_df[clean_df["Price"] <= 0])
print(
    clean_df[clean_df["Price"] <= 0]
)
"""

# Remove rows with Price <= 0
clean_df = clean_df[clean_df["Price"] > 0]

print("\nAfter removing Price <= 0:")
print(clean_df.shape)

# verify
print("\nRemaining rows with Price <= 0:")
print((clean_df["Price"] <= 0).sum())

# save to processed
clean_df.to_csv(
    r"D:\RetailAnalytics\data\processed\cleaned_retail_data.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")