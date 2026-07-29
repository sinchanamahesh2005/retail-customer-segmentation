import pandas as pd

# Path to the dataset
file_path = r"D:\RetailAnalytics\data\raw\online_retail_II.xlsx"

# Read the first worksheet
df = pd.read_excel(file_path, sheet_name="Year 2009-2010")

# Display the first 5 rows
print(df.head())

# Find the dataset size
print("Shape of dataset:", df.shape)

# Display column names
print("\nColumns:")
print(df.columns)

# Display information
print("\nDataset Information:")
df.info()

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumber of Unique Customers:")
print(df["Customer ID"].nunique())

print("\nNumber of Unique Products:")
print(df["StockCode"].nunique())

print("\nNumber of Unique Invoices:")
print(df["Invoice"].nunique())

print("\nSummary Statistics:")
print(df.describe())