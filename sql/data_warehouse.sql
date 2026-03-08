SET FOREIGN_KEY_CHECKS = 0;

TRUNCATE TABLE fact_sales;
TRUNCATE TABLE dim_customer;
TRUNCATE TABLE dim_product;
TRUNCATE TABLE dim_date;

SET FOREIGN_KEY_CHECKS = 1;

-- =====================================
-- DATA WAREHOUSE STRUCTURE
-- Star Schema for Ecommerce Analytics
-- =====================================

-- Dimension table: Customers
CREATE TABLE IF NOT EXISTS dim_customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100),
    signup_date DATE
);

-- Dimension table: Products
CREATE TABLE IF NOT EXISTS dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- Dimension table: Date
CREATE TABLE IF NOT EXISTS dim_date (
    date_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    year INT,
    month INT,
    day INT
);

-- Fact table: Sales
CREATE TABLE IF NOT EXISTS fact_sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    date_id INT,
    quantity INT,
    revenue DECIMAL(10,2),

    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);


-- =====================================
-- ELT: LOAD CUSTOMER DIMENSION
-- Loads customer data from OLTP database
-- =====================================

INSERT INTO dim_customer (customer_id, name, city, signup_date)
SELECT
    customer_id,
    name,
    city,
    signup_date
FROM ecommerce_analytics.customers;

-- =====================================
-- ELT: LOAD PRODUCT DIMENSION
-- =====================================

INSERT INTO dim_product (product_id, product_name, category, price)
SELECT
    product_id,
    product_name,
    category,
    price
FROM ecommerce_analytics.products;

-- =====================================
-- ELT: LOAD DATE DIMENSION
-- Extract dates from orders
-- =====================================

INSERT INTO dim_date (date, year, month, day)
SELECT DISTINCT
    order_date,
    YEAR(order_date),
    MONTH(order_date),
    DAY(order_date)
FROM ecommerce_analytics.orders;

-- =====================================
-- ELT: LOAD FACT SALES
-- Combines orders and order_items
-- =====================================

INSERT INTO fact_sales (customer_id, product_id, date_id, quantity, revenue)
SELECT
    o.customer_id,
    oi.product_id,
    d.date_id,
    oi.quantity,
    oi.quantity * p.price AS revenue

FROM ecommerce_analytics.orders o

JOIN ecommerce_analytics.order_items oi
ON o.order_id = oi.order_id

JOIN ecommerce_analytics.products p
ON oi.product_id = p.product_id

JOIN dim_date d
ON d.date = o.order_date;

