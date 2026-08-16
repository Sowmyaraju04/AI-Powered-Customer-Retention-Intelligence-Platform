# Table Granularity

## Overview

Table granularity defines what a single row represents within a dataset. It is one of the most important concepts in data analytics because it determines how tables should be joined, aggregated, and analyzed.

Before combining multiple tables, analysts must understand the granularity of each dataset to avoid duplicate records, incorrect calculations, and misleading business insights.

For the AI-Powered Customer Retention Intelligence Platform, understanding table granularity is essential because the final machine learning model requires a customer-level analytical dataset where each row represents exactly one customer.

---

# What is Granularity?

Granularity refers to the level of detail stored in a table.

For example:

- One row may represent one customer.
- One row may represent one order.
- One row may represent one product within an order.
- One row may represent one payment transaction.

Although these tables belong to the same business process, they describe different levels of information.

---

# Granularity of Each Table

| Table | One Row Represents | Granularity Type |
|--------|--------------------|------------------|
| customers | One customer record | Customer Level |
| orders | One customer order | Order Level |
| order_items | One product within one order | Order Item Level |
| order_payments | One payment transaction for an order | Payment Level |
| order_reviews | One customer review | Review Level |
| products | One product | Product Level |
| sellers | One seller | Seller Level |
| geolocation | One ZIP code observation | Geographic Level |
| product_category_name_translation | One product category translation | Reference Level |

---

# Why Granularity Matters

Different tables cannot be joined blindly because they represent different levels of detail.

For example:

- One customer can place many orders.
- One order can contain many products.
- One order can have multiple payment records.

If these tables are joined without understanding their granularity, a single customer may appear multiple times, leading to inflated metrics and incorrect model inputs.

---

# Example

Suppose:

Customer A placed 2 orders.

Order 1 contains 3 products.

Order 2 contains 2 products.

The data would look like this:

| Table | Number of Rows |
|--------|---------------:|
| customers | 1 |
| orders | 2 |
| order_items | 5 |

If we directly join `customers`, `orders`, and `order_items`, Customer A will appear **5 times**, not once.

This duplication can inflate:

- Total Revenue
- Order Count
- Average Order Value
- Purchase Frequency

---

# Customer-Level Analytical Dataset

Machine learning models require a fixed structure where each row represents one observation.

In this project:

**One row = One customer**

To achieve this, transactional tables must be aggregated before they are merged into the customer-level dataset.

Examples include:

- Total Orders
- Total Spend
- Average Order Value
- Purchase Frequency
- Average Review Score
- Total Products Purchased

These aggregated features accurately describe customer behavior without introducing duplicate records.

---

# Transactional vs Reference Tables

## Transactional Tables

These tables record business events.

- orders
- order_items
- order_payments
- order_reviews

Their row counts increase as business activity grows.

---

## Master / Dimension Tables

These tables describe business entities.

- customers
- products
- sellers

They provide descriptive information used to enrich transactional data.

---

## Reference Tables

These tables provide lookup information.

- product_category_name_translation
- geolocation

They improve reporting and data interpretation but do not represent business transactions.

---

# Best Practices

- Always identify table granularity before joining datasets.
- Aggregate transactional tables before creating customer-level features.
- Validate row counts after every merge.
- Keep the analytical grain consistent throughout the project.
- Clearly document the analytical grain of the final dataset.

---

# Common Mistakes

- Joining tables without checking granularity.
- Counting duplicated rows as unique customers.
- Calculating revenue after duplicate joins.
- Building machine learning models on transactional-level data instead of customer-level data.
- Ignoring aggregation before feature engineering.

---

# Business Importance

Understanding table granularity ensures that customer behavior is represented accurately.

It enables reliable KPI calculations, prevents duplicate records, supports meaningful feature engineering, and provides a strong foundation for customer churn prediction and business intelligence reporting.