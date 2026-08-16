# Feature Engineering Report

## Project

**AI-Powered Customer Retention Intelligence Platform**

---

## Objective

The objective of the Feature Engineering phase was to transform cleaned e-commerce transaction data into meaningful customer-level features suitable for customer retention analysis and machine learning.

Rather than using raw transactional variables directly, business-oriented features were created to represent customer activity, purchasing behavior, monetary value, satisfaction, and retention risk.

---

# Feature Engineering Approach

The feature engineering process followed these major steps:

1. Created transaction-level behavioral features.
2. Aggregated transactional information to the customer level.
3. Used `customer_unique_id` to represent individual customers.
4. Created RFM features.
5. Created customer value and satisfaction features.
6. Created customer risk segments.
7. Created a churn-risk proxy target.
8. Consolidated the features into a final modeling dataset.
9. Validated the final customer-level dataset.

---

# Features Created

## Transaction and Customer Behavior

The following features were engineered:

- Delivery Days
- Order Value
- Total Customer Spend
- Total Orders
- Average Order Value
- Average Review Score
- Preferred Payment Method

These features capture customer purchasing behavior, transaction value, satisfaction, and operational experience.

---

# RFM Features

Three standard customer analytics features were created:

### Recency

Measures the number of days since the customer's latest purchase.

### Frequency

Measures the number of purchases made by the customer.

### Monetary

Measures the total amount spent by the customer.

RFM provides an interpretable framework for understanding customer engagement and value.

---

# Customer Value

## Average Order Value

Average Order Value was calculated as:

```text
Average Order Value =
Total Customer Spend / Total Orders
```

This measures the average monetary value of a customer's transactions.

---

## Customer Lifetime Value

For this project, historical customer monetary value was used as a transparent representation of Customer Lifetime Value.

This approach avoids introducing unsupported assumptions about future customer behavior.

---

# Customer Risk Segmentation

Customers were categorized into three business-oriented risk groups:

| Risk Segment | General Interpretation |
|---|---|
| Low | Recently active with stronger engagement |
| Medium | Moderate customer engagement |
| High | Longer period of inactivity |

The risk segmentation provides a practical framework for prioritizing retention activities.

---

# Target Variable

Because the Olist dataset does not contain an explicit churn label, a churn proxy was created.

The rule used was:

```text
Recency > 180 days
        ↓
Churn-Risk = 1

Recency <= 180 days
        ↓
Active / Retained = 0
```

The target variable is:

```text
churn_label
```

### Important Limitation

This is a **churn-risk proxy based on inactivity**, not a confirmed customer churn event.

Therefore, the machine learning model should be interpreted as predicting **inactivity-based churn risk**.

---

# Target Leakage Consideration

Since the target variable is directly derived from Recency, `Recency` must not be used as a predictive input when training the churn model.

Otherwise, the model would have direct access to the information used to construct the target.

Therefore:

```text
Target:
churn_label

Excluded from model predictors:
Recency
```

Recency remains useful for business analysis and retention recommendations.

---

# Final Customer-Level Dataset

All relevant customer features were consolidated into a single modeling dataset.

The final dataset contains customer-level information including:

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
churn_label
```

The final modeling dataset is stored at:

```text
data/processed/customer_retention_model_data.csv
```

---

# Business Value

The engineered dataset provides a structured view of customer behavior and enables the organization to:

- Identify potentially disengaged customers.
- Identify high-value customers.
- Understand purchasing behavior.
- Measure customer satisfaction.
- Segment customers according to retention risk.
- Prioritize retention campaigns.
- Build predictive customer-risk models.
- Support personalized customer recommendations.

---

# Machine Learning Readiness

The final customer-level dataset provides the foundation for the next stage of the project.

The Machine Learning phase will use these engineered variables to develop a model capable of identifying customers with elevated inactivity-based retention risk.

The modeling workflow will include:

- Feature selection
- Train-test splitting
- Categorical encoding
- Feature scaling where required
- Model training
- Model comparison
- Evaluation
- Probability-based risk scoring
- Explainability

---

# Data Quality and Validation

The final feature dataset was validated for:

- Missing values
- Duplicate customer records
- Target consistency
- Feature availability
- Customer-level granularity
- Modeling readiness

The final dataset is structured around `customer_unique_id`, ensuring that the modeling unit represents the customer rather than an individual transaction.

---

# Key Outcome

The Feature Engineering phase transformed the cleaned Olist e-commerce data into a customer-centric analytical dataset.

This phase established the behavioral foundation required for the project's core objective:

> **Identify customers at risk of disengagement and support data-driven customer retention strategies.**

---

## Phase Status

**Phase 6 – Feature Engineering**

**Status: ✅ COMPLETED**

---

# Next Phase

**Phase 7 – Machine Learning**

The next phase will focus on developing and evaluating machine learning models for inactivity-based customer churn-risk prediction.