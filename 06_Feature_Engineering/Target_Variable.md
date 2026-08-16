# Target Variable

## Objective

The objective of target variable engineering is to define a measurable customer retention outcome that can be used by the machine learning model.

The original Olist dataset does not contain an explicit customer churn or retention label. Therefore, a **churn proxy** was created using customer inactivity.

---

# Churn Definition

A customer is considered a potential churn-risk customer when they have not made a purchase for more than **180 days**.

The target variable is named:

`churn_label`

---

## Target Definition

| churn_label | Definition |
|---:|---|
| 0 | Active / Retained Customer |
| 1 | Churn-Risk Customer |

### Business Rule

```text
If Recency > 180 days
    → churn_label = 1

If Recency <= 180 days
    → churn_label = 0
```

---

# Why 180 Days?

A six-month inactivity threshold was selected as a practical business rule for identifying customers who may have become disengaged.

The threshold is not an observed value from the dataset. It is a **business-defined proxy** created because the dataset does not provide an actual churn event.

This distinction is important when interpreting model results.

---

# Target Variable Creation

The target was created using:

```python
CHURN_THRESHOLD_DAYS = 180

model_data["churn_label"] = (
    model_data["Recency"] > CHURN_THRESHOLD_DAYS
).astype(int)
```

---

# Target Interpretation

### `churn_label = 0`

Represents a customer who has purchased within the defined 180-day activity window.

These customers are considered:

**Active / Retained**

---

### `churn_label = 1`

Represents a customer whose last purchase occurred more than 180 days before the analysis reference date.

These customers are considered:

**Churn-Risk**

---

# Target Distribution

The target distribution was validated after creation.

The validation checks included:

- Unique target values
- Number of active customers
- Number of churn-risk customers
- Percentage distribution
- Missing target values
- Consistency with the Recency rule

The final target validation confirmed that the target values are generated consistently from the defined business rule.

---

# Important Modeling Consideration: Target Leakage

Because the target variable is directly derived from `Recency`, **Recency must not be used as an input feature when training a model to predict this exact target**.

Otherwise, the model would receive the same information used to create the target, resulting in target leakage.

Therefore:

```text
Target:
churn_label

Excluded predictive feature:
Recency
```

Recency can still be retained for:

- Business analysis
- Customer risk interpretation
- Retention recommendations
- Customer segmentation

---

# Business Purpose

The churn proxy allows the platform to identify customers who may require retention intervention.

Potential actions include:

- Personalized offers
- Re-engagement campaigns
- Loyalty incentives
- Product recommendations
- Targeted communication
- High-value customer recovery campaigns

---

# Limitation

This target variable represents **predicted inactivity risk**, not confirmed customer churn.

The dataset does not provide:

- Customer cancellation of membership
- Account closure
- Explicit churn date
- Customer-declared reason for leaving
- Confirmed permanent customer loss

Therefore, model results should be interpreted as:

> **Churn-risk prediction based on customer inactivity**

rather than definitive proof that a customer has permanently churned.

This limitation will be clearly communicated in the final project documentation and interviews.

---

# Final Target Variable

The final modeling target is:

```text
churn_label
```

with:

```text
0 → Active / Retained
1 → Churn-Risk
```

The target is included in:

`data/processed/customer_retention_model_data.csv`

---

## Status

**Target Variable Engineering: Completed**