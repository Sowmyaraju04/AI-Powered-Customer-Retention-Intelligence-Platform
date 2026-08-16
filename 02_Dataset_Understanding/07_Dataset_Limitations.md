# Dataset Limitations

## Overview

Although the Brazilian Olist E-Commerce Dataset is one of the most comprehensive public e-commerce datasets available, it was not originally designed for customer churn prediction.

As with any real-world dataset, it contains several business and technical limitations that must be acknowledged before building analytical models.

Understanding these limitations helps ensure that business decisions, feature engineering, and machine learning models are interpreted correctly.

---

# Business Limitations

## 1. No Explicit Churn Label

The dataset does not contain a column indicating whether a customer has churned.

### Impact

A business definition of churn must be created using historical purchasing behaviour.

### Mitigation

A churn definition based on customer inactivity (for example, no repeat purchase within a defined observation window) will be developed in Phase 6.

---

## 2. Limited Customer Demographics

The dataset contains only basic customer location information.

Missing attributes include:

- Age
- Gender
- Income
- Occupation
- Loyalty Membership

### Impact

Customer segmentation is limited to behavioural and geographic characteristics.

### Mitigation

Behavioral features such as recency, frequency, monetary value (RFM), and purchasing patterns will be used instead.

---

## 3. No Marketing Campaign Information

The dataset does not record:

- Promotional campaigns
- Coupons
- Email marketing
- Loyalty programs
- Customer support interactions

### Impact

The influence of marketing activities on customer retention cannot be measured directly.

### Mitigation

The recommendation engine will be rule-based and derived from observed customer behaviour rather than campaign history.

---

## 4. Limited Customer Journey Information

The dataset begins when an order is placed.

It does not include:

- Website visits
- Product views
- Search behaviour
- Cart abandonment
- Browsing sessions

### Impact

Pre-purchase customer behaviour cannot be analysed.

### Mitigation

The analysis will focus on post-purchase customer behaviour.

---

# Technical Limitations

## 1. Historical Snapshot

The dataset represents historical transactions rather than a continuously updated production database.

### Impact

Real-time churn prediction cannot be demonstrated.

### Mitigation

The project will simulate a production workflow using historical data.

---

## 2. Missing Values

Some tables contain missing values, particularly in delivery and review-related fields.

### Impact

Missing information may affect feature engineering and model quality.

### Mitigation

A comprehensive Data Quality Assessment and Data Cleaning phase will address missing values using documented business rules.

---

## 3. Multiple Granularity Levels

Different tables represent different levels of detail.

Examples include:

- Customer Level
- Order Level
- Order Item Level
- Payment Level

### Impact

Improper joins may create duplicate records and incorrect business metrics.

### Mitigation

A customer-level analytical data mart will be created before machine learning.

---

## 4. Limited Time Coverage

The dataset represents a fixed historical period.

### Impact

Long-term customer lifecycle analysis is limited.

### Mitigation

Churn analysis will be restricted to the available observation period.

---

# Analytical Assumptions

To build a meaningful customer retention platform, the following assumptions will be made:

- Customer inactivity is a reasonable proxy for churn.
- Historical purchasing behaviour reflects future purchasing tendencies.
- Customer satisfaction influences retention.
- Delivery performance affects customer loyalty.
- Purchase frequency and recency are strong predictors of churn.

These assumptions are commonly adopted in customer analytics when explicit churn labels are unavailable.

---

# Risks

Potential risks include:

- Incorrect churn definition.
- Class imbalance after target creation.
- Feature leakage.
- Duplicate records during table joins.
- Overfitting due to limited behavioural history.

These risks will be evaluated and addressed in later project phases.

---

# Business Impact

Despite these limitations, the dataset provides sufficient transactional, behavioural, operational, and customer satisfaction information to build an enterprise-grade Customer Retention Intelligence Platform.

By acknowledging these constraints and applying appropriate analytical techniques, meaningful business insights and reliable predictive models can still be developed.