# Business Use of Each Table

## Overview

Each table in the Brazilian Olist E-Commerce Dataset contributes unique business information that supports customer analytics, retention modeling, and executive decision-making.

Rather than viewing the tables as isolated datasets, they should be understood as interconnected business entities that collectively describe the complete customer purchase lifecycle.

This document explains how each table contributes to solving the customer retention problem and identifies its role in feature engineering, business intelligence, and machine learning.

---

# Business Contribution Summary

| Table | Primary Business Purpose | Importance for Churn Prediction |
|--------|--------------------------|---------------------------------|
| customers | Identify and segment customers | ⭐⭐⭐⭐⭐ |
| orders | Analyze purchasing behaviour | ⭐⭐⭐⭐⭐ |
| order_items | Understand products purchased | ⭐⭐⭐⭐⭐ |
| order_payments | Analyze payment behaviour | ⭐⭐⭐⭐☆ |
| order_reviews | Measure customer satisfaction | ⭐⭐⭐⭐☆ |
| products | Understand product characteristics | ⭐⭐⭐⭐☆ |
| sellers | Analyze seller performance | ⭐⭐⭐☆☆ |
| geolocation | Perform regional analysis | ⭐⭐☆☆☆ |
| product_category_name_translation | Improve reporting readability | ⭐⭐☆☆☆ |

---

# 1. Customers Table

## Business Questions Answered

- Who are our customers?
- Where are they located?
- How many unique customers do we have?

## Business Value

This table forms the foundation of the customer-level analytical dataset. It provides customer identity and geographic information used for segmentation and regional analysis.

## Planned Features

- Customer State
- Customer City
- Geographic Segmentation

---

# 2. Orders Table

## Business Questions Answered

- When did customers place orders?
- How frequently do they purchase?
- What is their most recent purchase?
- What is the order status?

## Business Value

The Orders table is the core transactional dataset. It captures customer purchasing behaviour over time and will be the primary source for defining churn.

## Planned Features

- Purchase Frequency
- Customer Recency
- Customer Tenure
- Total Orders
- Days Since Last Purchase

---

# 3. Order Items Table

## Business Questions Answered

- What products were purchased?
- How much revenue was generated?
- How many products were purchased per order?

## Business Value

This table enables revenue analysis and product-level behavioural insights.

## Planned Features

- Total Spend
- Average Order Value
- Basket Size
- Product Diversity
- Preferred Product Category

---

# 4. Order Payments Table

## Business Questions Answered

- Which payment methods are preferred?
- How many installments are used?
- What is the payment value?

## Business Value

Payment behaviour often reflects customer purchasing habits and spending patterns.

## Planned Features

- Preferred Payment Method
- Average Installments
- Total Payment Value

---

# 5. Order Reviews Table

## Business Questions Answered

- Are customers satisfied?
- How consistent are review scores?
- Do poor experiences influence churn?

## Business Value

Review data provides an indirect measure of customer satisfaction and post-purchase experience.

## Planned Features

- Average Review Score
- Review Consistency
- Low Review Count

---

# 6. Products Table

## Business Questions Answered

- Which product categories are popular?
- Which categories does each customer prefer?

## Business Value

Product information helps identify customer interests and purchasing preferences.

## Planned Features

- Preferred Product Category
- Product Diversity
- Category Count

---

# 7. Sellers Table

## Business Questions Answered

- Which sellers fulfill customer orders?
- Are there operational patterns associated with sellers?

## Business Value

Seller information supports operational and marketplace analysis. While it is not a primary driver of churn, it can provide additional business context.

## Planned Features

- Number of Unique Sellers
- Seller Diversity

---

# 8. Geolocation Table

## Business Questions Answered

- Where are customers and sellers located?
- Which regions generate the most business?

## Business Value

Geographical information supports regional reporting and customer segmentation.

## Planned Features

- Regional Sales Analysis
- Geographic Segmentation

---

# 9. Product Category Translation Table

## Business Questions Answered

- How can category names be presented in English?

## Business Value

This lookup table improves report readability and stakeholder communication.

## Planned Features

- English Product Category

---

# Overall Contribution to the AI Platform

The combined information from all tables enables the platform to:

- Build customer-level behavioural profiles.
- Measure purchasing behaviour over time.
- Estimate customer value.
- Identify customers at risk of churn.
- Generate personalized retention recommendations.
- Estimate revenue at risk.
- Support executive decision-making through interactive dashboards.

---

# Business Perspective

Each dataset contributes a different perspective of customer behaviour:

- Customers identify **who** the customer is.
- Orders show **when** purchases occur.
- Order Items reveal **what** customers buy.
- Payments explain **how** they pay.
- Reviews indicate **how they feel** about their experience.
- Products describe **what was purchased**.
- Sellers explain **who fulfilled the order**.
- Geolocation shows **where transactions occur**.

When integrated, these datasets provide a complete view of the customer journey and enable data-driven retention strategies.