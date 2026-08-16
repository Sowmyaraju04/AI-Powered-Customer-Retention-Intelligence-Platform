# Feature Creation

## Objective

The objective of feature creation was to transform cleaned e-commerce data into meaningful customer-level variables that can support customer behavior analysis, retention prediction, and machine learning.

The engineered features were designed based on business logic rather than creating variables arbitrarily.

---

## Features Created

### 1. Delivery Days

Measures the number of days between order purchase and customer delivery.

**Business Purpose:**  
Helps evaluate logistics performance and understand whether delivery experience may influence customer satisfaction and retention.

---

### 2. Order Value

Represents the total product value associated with an individual order.

**Business Purpose:**  
Helps measure transaction-level purchasing behavior.

---

### 3. Total Customer Spend

Represents the total monetary value spent by a customer across their purchases.

**Business Purpose:**  
Identifies high-value and low-value customers and supports customer value analysis.

---

### 4. Total Orders

Measures the number of orders associated with a customer.

**Business Purpose:**  
Provides an indicator of customer purchasing activity.

---

### 5. Average Order Value

Calculated as:

`Total Customer Spend / Total Orders`

**Business Purpose:**  
Measures the average amount a customer spends per transaction.

---

### 6. Average Review Score

Represents the average review score associated with a customer's orders.

**Business Purpose:**  
Acts as a customer satisfaction indicator and can help identify customers who may require retention attention.

---

### 7. Preferred Payment Method

Identifies the payment method most frequently used by each customer.

**Business Purpose:**  
Captures customer purchasing and payment behavior.

---

### 8. Recency

Measures the number of days since a customer's most recent purchase.

**Business Purpose:**  
Lower recency indicates more recent engagement, while higher recency may indicate declining customer activity.

---

### 9. Frequency

Measures the number of purchases made by a customer.

**Business Purpose:**  
Helps distinguish occasional customers from repeat customers.

---

### 10. Monetary

Represents the total amount spent by a customer.

**Business Purpose:**  
Measures customer monetary value and supports customer segmentation.

---

### 11. Customer Lifetime Value

For this project, Customer Lifetime Value is represented using the customer's cumulative monetary value.

**Business Purpose:**  
Provides a transparent measure of historical customer value.

---

### 12. Customer Risk Segment

Customers were categorized into business-oriented risk groups using customer recency and purchase frequency.

The segments are:

- **Low Risk**
- **Medium Risk**
- **High Risk**

**Business Purpose:**  
Helps prioritize customers for retention activities.

---

### 13. Churn Label

A proxy churn label was created because the Olist dataset does not contain an explicit churn indicator.

Customers with more than 180 days since their last purchase are classified as:

`1 = Churn Risk`

Customers with 180 days or fewer since their last purchase are classified as:

`0 = Active / Retained`

**Business Purpose:**  
Provides a target variable for supervised machine learning.

---

## Customer Identifier

For customer-level analysis, `customer_unique_id` is used as the primary customer identifier.

This is important because the Olist dataset's `customer_id` can represent individual order-level customer records, while `customer_unique_id` allows multiple purchases belonging to the same actual customer to be grouped together.

---

## Final Output

The engineered features were consolidated into:

`customer_retention_model_data.csv`

This dataset represents the final customer-level modeling dataset and will be used in the Machine Learning phase.

---

## Status

**Feature Creation: Completed**