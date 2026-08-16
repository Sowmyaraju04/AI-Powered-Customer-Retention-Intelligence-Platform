# RFM Features

## Objective

RFM analysis was performed to understand customer purchasing behavior using three key dimensions:

- Recency
- Frequency
- Monetary

RFM is a widely used customer analytics technique for identifying valuable, active, and potentially inactive customers.

---

## Customer Identifier

RFM analysis is performed using:

`customer_unique_id`

This allows multiple orders belonging to the same customer to be analyzed together.

---

# 1. Recency

## Definition

Recency measures how recently a customer made a purchase.

It is calculated as the number of days between the customer's most recent purchase and the analysis reference date.

### Formula

```text
Recency = Reference Date - Last Purchase Date
```

### Interpretation

| Recency | Customer Behavior |
|---|---|
| Low | Recently active |
| Medium | Moderately inactive |
| High | Long period since purchase |

### Business Value

Customers with high recency values may represent potential retention risks.

These customers can be prioritized for:

- Re-engagement campaigns
- Personalized offers
- Promotional communication
- Retention campaigns

---

# 2. Frequency

## Definition

Frequency measures how many orders a customer has placed.

### Formula

```text
Frequency = Number of Customer Orders
```

### Interpretation

| Frequency | Customer Behavior |
|---|---|
| Low | Occasional customer |
| High | Repeat customer |

### Business Value

High-frequency customers demonstrate stronger purchasing engagement and may have greater long-term value.

---

# 3. Monetary

## Definition

Monetary measures the total amount spent by a customer.

### Formula

```text
Monetary = Total Customer Payment Value
```

### Interpretation

| Monetary Value | Customer Value |
|---|---|
| Low | Lower-value customer |
| High | Higher-value customer |

### Business Value

Monetary value helps identify high-value customers who should receive greater retention attention.

---

# RFM Summary

| Metric | Measures | Business Meaning |
|---|---|---|
| Recency | Time since last purchase | Customer activity |
| Frequency | Number of purchases | Customer engagement |
| Monetary | Total spending | Customer value |

---

# Why RFM Was Selected

RFM was selected because it provides a simple and interpretable representation of customer behavior.

Instead of relying only on demographic information, RFM captures actual purchasing behavior.

This makes it useful for:

- Customer segmentation
- Retention analysis
- Customer value analysis
- Churn-risk identification
- Marketing prioritization
- Machine learning feature engineering

---

# Relationship With Customer Retention

RFM features provide strong behavioral signals for retention modeling.

For example:

- **High Recency + Low Frequency** → Potentially disengaged customer
- **Low Recency + High Frequency** → Highly engaged customer
- **Low Recency + High Monetary** → Valuable active customer
- **High Recency + High Monetary** → Potential high-value retention opportunity

These behavioral patterns can be used to prioritize retention actions.

---

# Final RFM Dataset

The RFM features are included in the customer-level modeling dataset:

`data/processed/customer_retention_model_data.csv`

The main RFM fields are:

```text
Recency
Frequency
Monetary
```

---

## Status

**RFM Feature Engineering: Completed**