# Enterprise Data Dictionary

## Overview

The Brazilian Olist E-Commerce Dataset is a relational dataset consisting of multiple interconnected tables. Each table represents a different business entity within the e-commerce ecosystem.

This document provides a high-level data dictionary describing the purpose, business meaning, primary keys, foreign keys, granularity, and analytical importance of each table used in the AI-Powered Customer Retention Intelligence Platform.

---

# Dataset Summary

| Table | Business Entity | Primary Key | Importance |
|--------|-----------------|-------------|------------|
| customers | Customers | customer_id | ⭐⭐⭐⭐⭐ |
| orders | Orders | order_id | ⭐⭐⭐⭐⭐ |
| order_items | Order Items | order_id + order_item_id | ⭐⭐⭐⭐⭐ |
| order_payments | Payments | order_id + payment_sequential | ⭐⭐⭐⭐☆ |
| order_reviews | Reviews | review_id | ⭐⭐⭐⭐☆ |
| products | Products | product_id | ⭐⭐⭐⭐☆ |
| sellers | Sellers | seller_id | ⭐⭐⭐☆☆ |
| geolocation | Locations | No Unique PK | ⭐⭐☆☆☆ |
| product_category_name_translation | Category Translation | product_category_name | ⭐⭐☆☆☆ |

---

# Table Details

---

## 1. Customers Table

**Table Name**

customers

**Business Purpose**

Stores customer identification and location information.

**Primary Key**

customer_id

**Business Entity**

Customer

**Granularity**

One row represents one customer record.

**Key Columns**

- customer_id
- customer_unique_id
- customer_zip_code_prefix
- customer_city
- customer_state

**Business Importance**

This table identifies customers and enables customer-level analytics.

**Importance for Churn Prediction**

⭐⭐⭐⭐⭐

---

## 2. Orders Table

**Table Name**

orders

**Business Purpose**

Stores every order placed by customers.

**Primary Key**

order_id

**Foreign Key**

customer_id

**Granularity**

One row represents one order.

**Key Columns**

- order_id
- customer_id
- order_status
- order_purchase_timestamp
- order_delivered_customer_date

**Business Importance**

This is the core transactional table.

Most customer behavior features originate from this dataset.

**Importance for Churn Prediction**

⭐⭐⭐⭐⭐

---

## 3. Order Items Table

**Table Name**

order_items

**Business Purpose**

Stores individual products purchased within each order.

**Primary Key**

(order_id, order_item_id)

**Foreign Keys**

- order_id
- product_id
- seller_id

**Granularity**

One row represents one product within one order.

**Business Importance**

Used to calculate:

- Revenue
- Product diversity
- Basket size
- Preferred product categories

**Importance for Churn Prediction**

⭐⭐⭐⭐⭐

---

## 4. Order Payments Table

**Business Purpose**

Stores payment information for each order.

**Primary Key**

(order_id, payment_sequential)

**Foreign Key**

order_id

**Granularity**

One row represents one payment transaction.

**Business Importance**

Used to analyze:

- Payment methods
- Installments
- Customer spending patterns

**Importance for Churn Prediction**

⭐⭐⭐⭐☆

---

## 5. Order Reviews Table

**Business Purpose**

Stores customer feedback after purchases.

**Primary Key**

review_id

**Foreign Key**

order_id

**Granularity**

One row represents one review.

**Business Importance**

Provides customer satisfaction indicators.

**Importance for Churn Prediction**

⭐⭐⭐⭐☆

---

## 6. Products Table

**Business Purpose**

Contains product attributes.

**Primary Key**

product_id

**Granularity**

One row represents one product.

**Business Importance**

Supports:

- Category analysis
- Product diversity
- Product preferences

**Importance for Churn Prediction**

⭐⭐⭐⭐☆

---

## 7. Sellers Table

**Business Purpose**

Stores seller information.

**Primary Key**

seller_id

**Granularity**

One row represents one seller.

**Business Importance**

Supports marketplace and seller performance analysis.

**Importance for Churn Prediction**

⭐⭐⭐☆☆

---

## 8. Geolocation Table

**Business Purpose**

Maps ZIP code prefixes to geographical locations.

**Primary Key**

No unique primary key.

**Granularity**

One row represents one ZIP code observation.

**Business Importance**

Supports regional analytics.

**Importance for Churn Prediction**

⭐⭐☆☆☆

---

## 9. Product Category Translation Table

**Business Purpose**

Translates Portuguese product categories into English.

**Primary Key**

product_category_name

**Granularity**

One row represents one product category.

**Business Importance**

Improves readability and reporting.

**Importance for Churn Prediction**

⭐⭐☆☆☆

---

# Key Observations

- The Orders table is the central transactional table.
- Customer-level modelling will require integrating multiple tables.
- Some tables contain transactional data, while others contain reference data.
- Different tables have different levels of granularity and must not be joined without careful aggregation.
- The dataset is well suited for customer analytics, retention modelling, and business intelligence applications.