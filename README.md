# Ecommerce Analytics Data Pipeline

## Overview

This project implements an **end-to-end data pipeline for ecommerce analytics**.
It simulates transactional ecommerce data, loads it into a relational database, and builds a **star-schema Data Warehouse** for analytical queries.

The goal of the project is to demonstrate key **Data Engineering and Analytics Engineering concepts**, including:

* Synthetic data generation
* ETL pipeline development
* OLTP database modeling
* Data Warehouse design (Star Schema)
* Analytical SQL queries

This project mimics a simplified **modern analytics data workflow used in real companies**.

---

# Architecture

The pipeline follows this architecture:

```
Synthetic Data Generation
        ↓
Python ETL Pipeline
        ↓
MySQL OLTP Database
        ↓
Star Schema Data Warehouse
        ↓
Business Analytics Queries
```

Pipeline flow:

```
generate_data.py
        ↓
load_data.py
        ↓
run_pipeline.py
```

---

# Tech Stack

Main technologies used in the project:

* Python
* SQL
* MySQL
* Pandas
* Data Warehouse Modeling
* ETL Pipelines

Python libraries:

* pandas
* mysql-connector-python
* faker

---

# Project Structure

```
ecommerce-analytics-project
│
├── data
│   ├── customers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── payments.csv
│   └── products.csv
│
├── python
│   ├── generate_data.py
│   ├── load_data.py
│   └── run_pipeline.py
│
├── sql
│   ├── create_tables.sql
│   └── data_warehouse.sql
│
├── analytics
│   └── kpi_queries.sql
│
├── requirements.txt
└── README.md
```

---

# Data Pipeline

## 1. Synthetic Data Generation

`generate_data.py` creates realistic ecommerce datasets using the **Faker** library.

Generated datasets:

* customers
* products
* orders
* order_items
* payments

These datasets simulate an **OLTP transactional system**.

---

## 2. OLTP Database Loading

`load_data.py` loads CSV datasets into a **MySQL relational database**.

Tables created:

* customers
* products
* orders
* order_items
* payments

Key features of the loader:

* automated table cleanup
* idempotent pipeline execution
* batch insertion using pandas

---

## 3. Data Warehouse Construction

The `data_warehouse.sql` script builds a **Star Schema Data Warehouse** optimized for analytics.

Star schema structure:

Fact table:

* `fact_sales`

Dimension tables:

* `dim_customer`
* `dim_product`
* `dim_date`

This structure enables **fast analytical queries and KPI calculations**.

---

# Example Analytical Queries

The `analytics/kpi_queries.sql` file contains queries used for business analysis.

Examples include:

* Monthly revenue
* Top selling products
* Customer purchase behavior
* Average order value
* Sales trends

These queries simulate **typical BI and analytics workloads**.

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/ecommerce-analytics-project.git
cd ecommerce-analytics-project
```

Install Python dependencies:

```
pip install -r requirements.txt
```

---

# Running the Pipeline

Run the full ETL pipeline:

```
python python/run_pipeline.py
```

Pipeline steps executed:

1. Generate synthetic datasets
2. Load data into MySQL OLTP tables
3. Build the analytics Data Warehouse

Successful output example:

```
Starting Ecommerce Data Pipeline

Step 1: Generating datasets...
Datasets generated successfully

Step 2: Loading data into MySQL...
All datasets loaded successfully

Step 3: Building Data Warehouse...
Data Warehouse built successfully

Pipeline finished successfully
```

---

# Key Data Engineering Concepts Demonstrated

This project demonstrates several important data engineering principles:

* ETL pipeline development
* OLTP vs OLAP data modeling
* Star Schema data warehouse design
* Synthetic dataset generation
* Automated pipeline execution
* Data cleaning and idempotent pipelines

---

# Future Improvements

Planned improvements for this project include:

* Business Intelligence dashboard integration
* Pipeline orchestration
* Containerized deployment
* Advanced analytics queries

---

# Author

Created as part of a **Data Engineering / Data Analytics portfolio project** to demonstrate practical skills in:

* Python data pipelines
* SQL analytics
* Data warehouse modeling
* end-to-end data workflows

---
Create by Brenda Espinosa
