import pandas as pd
import mysql.connector

# =====================================
# Connect to MySQL
# =====================================

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Sinc@2005",
    database="retail_analytics"
)

cursor = connection.cursor()

print("=" * 60)
print("CONNECTED TO MYSQL")
print("=" * 60)

# =====================================
# LOAD CUSTOMERS
# =====================================

customers = pd.read_csv(
    r"D:\RetailAnalytics\data\processed\customers.csv"
)

customer_query = """
INSERT INTO customers(customer_id, country)
VALUES(%s, %s)
"""

customer_data = list(
    customers[["customer_id", "country"]]
    .itertuples(index=False, name=None)
)

cursor.executemany(customer_query, customer_data)

print(f"Customers Loaded : {cursor.rowcount}")

connection.commit()

# =====================================
# LOAD PRODUCTS
# =====================================

products = pd.read_csv(
    r"D:\RetailAnalytics\data\processed\products.csv"
)

# Add empty category column
products["category"] = None

product_query = """
INSERT INTO products(product_id,
                     product_name,
                     category,
                     unit_price)
VALUES(%s,%s,%s,%s)
"""

product_data = list(
    products[
        ["product_id",
         "product_name",
         "category",
         "unit_price"]
    ].itertuples(index=False, name=None)
)

cursor.executemany(product_query, product_data)

print(f"Products Loaded : {cursor.rowcount}")

connection.commit()

# =====================================
# LOAD ORDERS
# =====================================

orders = pd.read_csv(
    r"D:\RetailAnalytics\data\processed\orders.csv"
)

orders["order_id"] = orders["order_id"].astype(str)

order_query = """
INSERT INTO orders(order_id,
                   customer_id,
                   order_date)
VALUES(%s,%s,%s)
"""

order_data = list(
    orders[
        ["order_id",
         "customer_id",
         "order_date"]
    ].itertuples(index=False, name=None)
)

cursor.executemany(order_query, order_data)

print(f"Orders Loaded : {cursor.rowcount}")

connection.commit()

# =====================================
# LOAD ORDER ITEMS
# =====================================

order_items = pd.read_csv(
    r"D:\RetailAnalytics\data\processed\order_items.csv"
)

order_items["order_id"] = order_items["order_id"].astype(str)
order_items["product_id"] = order_items["product_id"].astype(str)

order_item_query = """
INSERT INTO order_items(order_item_id,
                        order_id,
                        product_id,
                        quantity,
                        unit_price)
VALUES(%s,%s,%s,%s,%s)
"""

order_item_data = list(
    order_items[
        [
            "order_item_id",
            "order_id",
            "product_id",
            "quantity",
            "unit_price"
        ]
    ].itertuples(index=False, name=None)
)

cursor.executemany(order_item_query, order_item_data)

print(f"Order Items Loaded : {cursor.rowcount}")

connection.commit()

# =====================================
# FINISH
# =====================================

cursor.close()
connection.close()

print("\n" + "=" * 60)
print("ALL DATA LOADED SUCCESSFULLY!")
print("=" * 60)