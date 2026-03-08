# ============================================
# ECOMMERCE DATA PIPELINE
# ============================================
# This script orchestrates the full pipeline:
#
# 1. Generate synthetic ecommerce data
# 2. Load CSV data into MySQL OLTP database
# 3. Run SQL scripts to build the Data Warehouse
#
# Author: Brenda Espinosa
# ============================================

import subprocess
import mysql.connector


print("Starting Ecommerce Data Pipeline\n")


# --------------------------------------------
# STEP 1: GENERATE DATA
# --------------------------------------------
print("Step 1: Generating datasets...")

subprocess.run(["python3", "python/generate_data.py"])

print("Datasets generated successfully\n")


# --------------------------------------------
# STEP 2: LOAD DATA INTO MYSQL
# --------------------------------------------
print("Step 2: Loading data into MySQL...")

subprocess.run(["python3", "python/load_data.py"])

print("Data loaded into OLTP database\n")


# --------------------------------------------
# STEP 3: RUN DATA WAREHOUSE SQL
# --------------------------------------------
print("Step 3: Building Data Warehouse...")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce_analytics"
)

cursor = connection.cursor()

with open("sql/data_warehouse.sql", "r") as file:
    sql_script = file.read()

for statement in sql_script.split(";"):
    if statement.strip():
        cursor.execute(statement)

connection.commit()

cursor.close()
connection.close()

print("Data Warehouse built successfully\n")


print("Pipeline finished successfully 🚀")