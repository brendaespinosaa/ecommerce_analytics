import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# -------------------
# CUSTOMERS
# -------------------

customers = []

for i in range(500):
    customers.append({
        "customer_id": i + 1,
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "signup_date": fake.date_between(start_date='-2y', end_date='today')
    })

customers_df = pd.DataFrame(customers)


# -------------------
# PRODUCTS
# -------------------

categories = ["Electronics", "Clothing", "Home", "Sports", "Beauty"]

products = []

for i in range(50):
    products.append({
        "product_id": i + 1,
        "product_name": fake.word().capitalize(),
        "category": random.choice(categories),
        "price": round(random.uniform(10, 500), 2)
    })

products_df = pd.DataFrame(products)


# -------------------
# ORDERS
# -------------------

orders = []

for i in range(2000):
    orders.append({
        "order_id": i + 1,
        "customer_id": random.randint(1, 500),
        "order_date": fake.date_between(start_date='-1y', end_date='today'),
        "total_amount": round(random.uniform(20, 1000), 2)
    })

orders_df = pd.DataFrame(orders)


# -------------------
# ORDER ITEMS
# -------------------

order_items = []

for i in range(3000):
    order_items.append({
        "order_item_id": i + 1,
        "order_id": random.randint(1, 2000),
        "product_id": random.randint(1, 50),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(10, 500), 2)
    })

order_items_df = pd.DataFrame(order_items)


# -------------------
# PAYMENTS
# -------------------

methods = ["Credit Card", "Debit Card", "Pix", "Boleto"]

payments = []

for i in range(2000):
    payments.append({
        "payment_id": i + 1,
        "order_id": random.randint(1, 2000),
        "payment_method": random.choice(methods),
        "payment_value": round(random.uniform(20, 1000), 2)
    })

payments_df = pd.DataFrame(payments)


# -------------------
# SAVE CSV
# -------------------

customers_df.to_csv("customers.csv", index=False)
products_df.to_csv("products.csv", index=False)
orders_df.to_csv("orders.csv", index=False)
order_items_df.to_csv("order_items.csv", index=False)
payments_df.to_csv("payments.csv", index=False)

print("Datasets gerados com sucesso!")