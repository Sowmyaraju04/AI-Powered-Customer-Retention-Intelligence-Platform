# Table Relationships

## Overview

The Brazilian Olist E-Commerce Dataset is a relational dataset where each table represents a different business entity within the e-commerce ecosystem. These entities are connected through primary keys and foreign keys, allowing analysts to combine customer, order, payment, product, seller, and review information into a unified analytical dataset.

Understanding these relationships is essential before performing SQL joins, Python merges, feature engineering, or machine learning.

---

# Relationship Summary

| Parent Table | Child Table | Relationship | Join Key |
|---------------|-------------|--------------|----------|
| customers | orders | One-to-Many | customer_id |
| orders | order_items | One-to-Many | order_id |
| orders | order_payments | One-to-Many | order_id |
| orders | order_reviews | One-to-One (Mostly) | order_id |
| products | order_items | One-to-Many | product_id |
| sellers | order_items | One-to-Many | seller_id |
| product_category_name_translation | products | One-to-Many | product_category_name |

---

# Relationship Details

## 1. Customers → Orders

### Relationship

One Customer → Many Orders

### Join Key

customer_id

### Business Meaning

A single customer can place multiple orders over time.

This relationship enables the calculation of:

- Purchase Frequency
- Customer Recency
- Customer Tenure
- Total Orders
- Repeat Purchase Behaviour

These are among the most important features for churn prediction.

---

## 2. Orders → Order Items

### Relationship

One Order → Many Order Items

### Join Key

order_id

### Business Meaning

A single order may contain multiple products.

This relationship supports:

- Basket Size
- Product Diversity
- Revenue Calculation
- Preferred Product Categories

---

## 3. Orders → Payments

### Relationship

One Order → One or More Payment Records

### Join Key

order_id

### Business Meaning

Some orders are paid using multiple payment methods or installment records.

This table helps analyze:

- Payment Preference
- Installment Behaviour
- Payment Value
- Spending Patterns

---

## 4. Orders → Reviews

### Relationship

One Order → One Review (Generally)

### Join Key

order_id

### Business Meaning

Customers may leave a review after receiving their order.

This table provides customer satisfaction information and is useful for engineering behavioural features.

---

## 5. Products → Order Items

### Relationship

One Product → Many Order Items

### Join Key

product_id

### Business Meaning

A product can be purchased many times by different customers.

This relationship helps identify:

- Popular Products
- Product Diversity
- Preferred Categories

---

## 6. Sellers → Order Items

### Relationship

One Seller → Many Order Items

### Join Key

seller_id

### Business Meaning

A seller can fulfill many order items.

Although seller information is not a primary driver of churn, it provides useful operational insights.

---

## 7. Product Category Translation → Products

### Relationship

One Category → Many Products

### Join Key

product_category_name

### Business Meaning

The translation table converts Portuguese category names into English, making reports easier to understand.

---

# Join Flow

The recommended join sequence for this project is:

customers
↓
orders
↓
order_items
↓
products
↓
payments
↓
reviews
↓
translation

This sequence preserves customer-level relationships while enabling comprehensive feature engineering.

---

# Important Notes

- Always understand table granularity before joining datasets.
- Avoid joining many-to-many relationships without aggregation.
- Use LEFT JOIN when preserving customer records is important.
- Aggregate transactional tables before creating customer-level datasets.
- Validate row counts after every merge.

---

# Common Join Mistakes

- Joining tables without checking granularity.
- Creating duplicate customer records.
- Ignoring missing foreign keys.
- Using INNER JOIN where LEFT JOIN is more appropriate.
- Aggregating after joining instead of before.

---

# Business Importance

Correct table relationships ensure that customer behaviour is accurately represented. They form the foundation for data cleaning, customer-level feature engineering, churn prediction, explainable AI, and executive reporting.

Incorrect joins can lead to duplicated transactions, inflated revenue calculations, inaccurate customer metrics, and unreliable machine learning models.