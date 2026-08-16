# Machine Learning Report

## AI-Powered Customer Retention Intelligence Platform

---

# 1. Executive Summary

The machine learning phase focused on developing a customer-level risk prediction model capable of identifying customers associated with an inactivity-based churn definition.

The modeling pipeline included:

- Target definition
- Feature selection
- Leakage prevention
- Train/test splitting
- Preprocessing
- Multiple classification algorithms
- Model evaluation
- Threshold analysis
- Feature importance
- SHAP-based explainability

Four machine learning models were evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting

Gradient Boosting was selected as the current champion model based on its overall performance across the evaluated metrics.

However, evaluation revealed significant class imbalance and limited discrimination. Therefore, the model is positioned as a **customer risk-scoring and prioritization tool**, not a definitive churn prediction system.

---

# 2. Business Objective

The business objective is to identify customers who exhibit patterns associated with inactivity so that retention teams can prioritize intervention.

The machine learning system is designed to provide:

- Customer churn-risk probability
- Risk classification
- Customer prioritization
- Explainable risk drivers
- Inputs for personalized retention recommendations

---

# 3. Modeling Dataset

The model uses:

`data/processed/customer_retention_model_data.csv`

The dataset represents customer-level transactional, behavioral, satisfaction, and payment information.

---

# 4. Target Definition

The target variable is:

`churn_label`

| Value | Meaning |
|---|---|
| 0 | Active / Retained |
| 1 | Churn-Risk |

The target is based on a predefined inactivity threshold.

Because the target is derived from historical inactivity, the model should be described as predicting **inactivity-associated customer risk** rather than guaranteed future churn.

---

# 5. Target Distribution

| Segment | Customers | Percentage |
|---|---:|---:|
| Active / Retained | 27,744 | 28.87% |
| Churn-Risk | 68,352 | 71.13% |

The target is significantly imbalanced toward the Churn-Risk class.

---

# 6. Predictive Features

The final model uses:

- Frequency
- Monetary
- Average Review Score
- Preferred Payment Method
- Average Order Value

These features capture:

- Purchase behavior
- Customer spending
- Customer satisfaction
- Payment preferences
- Order value

---

# 7. Leakage Prevention

The following features were excluded:

### Recency

Excluded because the target itself is based on inactivity and using Recency would create target leakage.

### Customer Risk

Excluded because it is derived from customer-risk logic.

### Customer Unique ID

Excluded because it is an identifier rather than a behavioral predictor.

### Customer Lifetime Value

Excluded because it duplicates Monetary in the current implementation.

---

# 8. Modeling Approach

Four classification algorithms were trained:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

The models used a common preprocessing pipeline.

Numerical variables were median-imputed.

Categorical payment variables were one-hot encoded.

The dataset was divided into:

- 80% training
- 20% testing

Stratified sampling was used to maintain target proportions.

---

# 9. Initial Model Comparison

| Model | Accuracy |
|---|---:|
| Gradient Boosting | 71.39% |
| Random Forest | 71.27% |
| Logistic Regression | 71.14% |
| Decision Tree | 71.13% |

Gradient Boosting achieved the highest accuracy.

---

# 10. Final Model Evaluation

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Gradient Boosting | 71.39% | 71.49% | 99.41% | 83.17% | 60.01% |
| Random Forest | 71.27% | 71.43% | 99.35% | 83.11% | 59.05% |
| Logistic Regression | 71.14% | 71.42% | 99.09% | 83.01% | 55.59% |
| Decision Tree | 71.13% | 71.37% | 99.23% | 83.02% | 55.47% |

---

# 11. Champion Model

## Gradient Boosting

Gradient Boosting was selected as the champion model because it achieved the strongest overall results among the evaluated models.

Performance:

- Accuracy: 71.39%
- Precision: 71.49%
- Recall: 99.41%
- F1-Score: 83.17%
- ROC-AUC: 60.01%
- PR-AUC: 77.70%

---

# 12. Model Limitations

The evaluation identified several limitations.

### Class Imbalance

71.13% of customers belong to the Churn-Risk class.

### High False Positives

At the 0.50 threshold, the model classified many Active / Retained customers as Churn-Risk.

### Limited Discrimination

The ROC-AUC of 0.6001 indicates limited separation between the two target classes.

### Weak Behavioral Separation

The average feature values between the two classes are relatively similar.

For example:

Frequency:

- Active / Retained: 1.04
- Churn-Risk: 1.03

This indicates that the available dataset contains limited behavioral differentiation between the target groups.

---

# 13. Threshold Analysis

| Threshold | Precision | Recall | F1 | Predicted Risk |
|---:|---:|---:|---:|---:|
| 0.30 | 71.17% | 99.96% | 83.14% | 19,200 |
| 0.40 | 71.21% | 99.90% | 83.15% | 19,180 |
| 0.50 | 71.49% | 99.41% | 83.17% | 19,010 |
| 0.60 | 71.82% | 98.32% | 83.00% | 18,716 |
| 0.70 | 75.42% | 64.88% | 69.75% | 11,761 |
| 0.80 | 85.19% | 3.36% | 6.47% | 540 |

A threshold of 0.70 provides a more targeted high-risk segment.

---

# 14. Risk Segmentation

The application can convert probability scores into business risk groups.

| Risk Probability | Risk Level |
|---:|---|
| < 0.40 | Low Risk |
| 0.40 – 0.69 | Medium Risk |
| ≥ 0.70 | High Risk |

The continuous probability score should also be retained for customer ranking.

---

# 15. Explainability

Gradient Boosting feature importance showed that:

- Monetary
- Average Order Value
- Average Review Score

were among the strongest predictors.

SHAP analysis identified:

1. Average Review Score
2. Average Order Value
3. Monetary

as the strongest contributors at the global level.

---

# 16. Customer-Level Explanation

A selected high-risk customer received:

`89.91%`

predicted churn-risk probability.

Customer characteristics included:

- Frequency: 1
- Monetary: 77.57
- Average Review Score: 1.0
- Preferred Payment: Boleto
- Average Order Value: 77.57

The strongest positive SHAP contributors were:

- Monetary
- Average Review Score
- Average Order Value

This demonstrates how the platform can explain individual risk predictions.

---

# 17. Business Application

The model can support:

### Customer Prioritization

Rank customers based on estimated risk probability.

### Retention Campaigns

Segment customers into low, medium, and high-risk groups.

### Service Recovery

Customers with poor review scores can be prioritized for customer-service interventions.

### Targeted Re-engagement

High-risk customers can receive personalized reactivation campaigns.

### Retention Recommendation Engine

Model outputs can serve as inputs to a recommendation layer that determines the most appropriate retention action.

---

# 18. Key Business Insights

### Spending Behavior Matters

Monetary value and Average Order Value are major contributors to model predictions.

### Customer Satisfaction Matters

Review scores provide meaningful predictive information.

### Purchase Frequency Has Limited Signal

Frequency contributes very little because most customers have very similar purchase frequency.

### Risk Scoring Is More Useful Than a Binary Label

Probability scores provide a ranking mechanism that can support different intervention strategies.

---

# 19. Model Governance and Responsible Interpretation

The model should not be interpreted as proving that a customer will churn.

Predictions represent patterns learned from historical data.

SHAP explanations describe model behavior and should not be interpreted as causal relationships.

Retention decisions should therefore combine model predictions with business rules and customer context.

---

# 20. Final Conclusion

The machine learning phase successfully established an end-to-end customer-risk prediction pipeline.

The solution:

- Prevents target leakage
- Uses customer-level behavioral features
- Compares multiple machine learning algorithms
- Evaluates models using multiple metrics
- Addresses class imbalance through diagnostic analysis
- Generates probability-based risk scores
- Supports threshold-based segmentation
- Provides global and individual explainability

Gradient Boosting is retained as the champion model for the current project.

The next phase will transform these predictions into actionable business recommendations through the **Retention Recommendation Engine**.