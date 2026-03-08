# ============================================
# LOAD CSV DATA INTO MYSQL DATABASE
# ============================================
# This script loads the generated CSV datasets
# into the OLTP MySQL database.
#
# Tables loaded:
# customers
# products
# orders
# order_items
# payments
# ============================================

import pandas as pd
import mysql.connector

# --------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

print("Connected to MySQL")

# --------------------------------------------
# CLEAN TABLES BEFORE INSERTING DATA
# --------------------------------------------

cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

cursor.execute("TRUNCATE TABLE order_items")
cursor.execute("TRUNCATE TABLE orders")
cursor.execute("TRUNCATE TABLE customers")
cursor.execute("TRUNCATE TABLE products")
cursor.execute("TRUNCATE TABLE payments")

cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

connection.commit()

print("Tables cleaned successfully")

# --------------------------------------------
# FUNCTION TO LOAD DATAFRAME INTO MYSQL TABLE
# --------------------------------------------
def insert_dataframe(df, table_name):
    """
    Inserts rows from a pandas dataframe
    into a MySQL table.
    """

    columns = ",".join(df.columns)
    placeholders = ",".join(["%s"] * len(df.columns))

    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row))

    connection.commit()
    print(f"{table_name} loaded successfully")


# --------------------------------------------
# LOAD CSV FILES
# --------------------------------------------

customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")
orders = pd.read_csv("data/orders.csv")
order_items = pd.read_csv("data/order_items.csv")
payments = pd.read_csv("data/payments.csv")


# --------------------------------------------
# INSERT DATA INTO MYSQL
# --------------------------------------------

insert_dataframe(customers, "customers")
insert_dataframe(products, "products")
insert_dataframe(orders, "orders")
insert_dataframe(order_items, "order_items")
insert_dataframe(payments, "payments")


cursor.close()
connection.close()

print("All datasets loaded successfully!")