
# Model Interpretation

## AI-Powered Customer Retention Intelligence Platform

---

## 1. Objective

The objective of model interpretation is to understand which customer attributes influence churn-risk predictions and provide transparent explanations for individual customer predictions.

Explainability is important because business users should understand why a customer has been classified as high-risk.

---

## 2. Global Feature Importance

Gradient Boosting feature importance produced the following ranking:

| Feature | Importance |
|---|---:|
| Monetary | 36.77% |
| Average Order Value | 32.75% |
| Average Review Score | 16.53% |
| Debit Card | 11.22% |
| Credit Card | 1.33% |
| Boleto | 0.63% |
| Frequency | 0.55% |
| Voucher | 0.21% |
| Not Defined | 0.00% |

The model primarily relies on spending-related and customer-satisfaction features.

---

## 3. SHAP Global Interpretation

SHAP analysis was used to understand the average contribution of features to model predictions.

| Feature | Mean Absolute SHAP |
|---|---:|
| Average Review Score | 0.123803 |
| Average Order Value | 0.120126 |
| Monetary | 0.104626 |
| Debit Card | 0.027837 |
| Credit Card | 0.023082 |
| Boleto | 0.006626 |
| Frequency | 0.002796 |
| Voucher | 0.001148 |
| Not Defined | 0.000000 |

Average Review Score, Average Order Value, and Monetary value were the strongest contributors to model predictions.

---

## 4. Frequency Finding

Frequency had very low model importance.

This is consistent with the underlying dataset:

| Segment | Average Frequency |
|---|---:|
| Active / Retained | 1.04 |
| Churn-Risk | 1.03 |

The extremely small difference indicates that purchase frequency provides limited discriminatory information in this dataset.

This is an important dataset-level finding rather than a modeling error.

---

## 5. Individual Customer Explanation

A high-risk customer was selected for individual explanation.

### Customer Profile

| Feature | Value |
|---|---:|
| Frequency | 1 |
| Monetary | 77.57 |
| Average Review Score | 1.0 |
| Preferred Payment | Boleto |
| Average Order Value | 77.57 |

### Predicted Risk

`89.91%`

---

## 6. SHAP Explanation for the High-Risk Customer

The strongest positive SHAP contributions were:

| Feature | SHAP Contribution |
|---|---:|
| Monetary | +0.770635 |
| Average Review Score | +0.351590 |
| Average Order Value | +0.054546 |
| Boleto | +0.041683 |

These features pushed the prediction toward the Churn-Risk class.

---

## 7. Global vs Individual Explainability

Global feature importance explains:

> Which features generally matter most across the customer population?

Individual SHAP explanations answer:

> Which features contributed most to this specific customer's prediction?

Therefore, a feature can have high global importance while not being the strongest driver for every individual customer.

---

## 8. Business Interpretation

The explainability layer enables the retention platform to provide both:

- A customer risk score
- The behavioral factors associated with that risk

For example, a customer with a very low review score may receive a service-recovery recommendation rather than a generic promotional offer.

---

## 9. Important Limitation

SHAP explains the behavior of the trained model. It does not prove that a feature causally causes churn.

Therefore, explanations should be interpreted as:

> "Factors contributing to the model's risk prediction."

They should not be interpreted as:

> "Factors that definitively caused the customer to churn."

---

## 10. Conclusion

The explainability analysis demonstrates that the model's predictions can be translated into understandable customer-level risk drivers.

This creates the foundation for the next phase: a retention recommendation engine that converts customer risk and behavioral signals into actionable business interventions.