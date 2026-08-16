# Customer Features

## Objective

The objective of customer-level feature engineering is to transform transaction-level e-commerce data into a single customer-level representation.

These features capture customer purchasing behavior, monetary value, satisfaction, and engagement and will serve as inputs for the customer retention modeling process.

---

## Customer Identifier

The primary customer identifier used for customer-level analysis is:

`customer_unique_id`

This identifier allows multiple orders belonging to the same actual customer to be grouped together.

---

## Customer-Level Features

### 1. Recency

**Definition:**  
Number of days since the customer's most recent purchase.

**Business Interpretation:**

- Lower Recency → More recently active customer
- Higher Recency → Customer has been inactive for longer

**Business Value:**  
Recency is an important indicator of customer engagement and potential retention risk.

---

### 2. Frequency

**Definition:**  
Number of orders placed by the customer.

**Business Interpretation:**

- Low Frequency → Occasional customer
- High Frequency → Repeat customer

**Business Value:**  
Helps identify customers with stronger purchasing engagement.

---

### 3. Monetary

**Definition:**  
Total amount spent by the customer across purchases.

**Business Interpretation:**

- Low Monetary → Lower-value customer
- High Monetary → Higher-value customer

**Business Value:**  
Helps identify valuable customers and prioritize retention efforts.

---

### 4. Average Order Value

**Definition:**

`Average Order Value = Monetary / Frequency`

**Business Interpretation:**  
Measures the average amount a customer spends per order.

**Business Value:**  
Helps understand individual purchasing strength and customer spending behavior.

---

### 5. Average Review Score

**Definition:**  
Average review score associated with the customer's orders.

**Business Interpretation:**

- Higher score → Stronger customer satisfaction
- Lower score → Potential dissatisfaction

**Business Value:**  
Customer satisfaction can be used as an indicator when prioritizing retention strategies.

---

### 6. Preferred Payment Method

**Definition:**  
The payment method most frequently used by the customer.

**Business Interpretation:**  
Represents the customer's dominant payment preference.

**Business Value:**  
Can support personalized promotions and payment-related customer experiences.

---

### 7. Customer Lifetime Value

**Definition:**  
For this project, Customer Lifetime Value is represented using the customer's cumulative historical monetary value.

**Business Value:**  
Provides a transparent measure of historical customer value and helps prioritize high-value customers.

---

### 8. Customer Risk

Customers are assigned a business-oriented risk segment based primarily on recency and purchasing activity.

The segments are:

| Risk Segment | Interpretation |
|---|---|
| Low | Recently active and showing repeat purchasing behavior |
| Medium | Moderate engagement |
| High | Long period of inactivity |

**Business Value:**  
Enables the business to prioritize customers for retention campaigns.

---

## Final Customer Feature Table

The final customer-level dataset combines the engineered features into a single analytical structure.

The main fields include:

```text
customer_unique_id
Recency
Frequency
Monetary
average_review_score
preferred_payment_method
average_order_value
customer_lifetime_value
Customer_Risk
```

The customer-level dataset provides a consolidated view of customer behavior and value.

---

## Modeling Readiness

These customer-level features provide the foundation for:

- Customer retention prediction
- Customer risk classification
- Customer segmentation
- Retention campaign prioritization
- Business recommendation generation

The final modeling dataset is stored as:

`data/processed/customer_retention_model_data.csv`

---

## Status

**Customer Feature Engineering: Completed**