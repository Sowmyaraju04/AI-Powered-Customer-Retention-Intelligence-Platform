# Model Selection

## AI-Powered Customer Retention Intelligence Platform

---

## 1. Objective

Multiple machine learning classification algorithms were evaluated to identify the most suitable model for customer churn-risk prediction.

The objective was not simply to maximize accuracy but to identify a model that provides useful risk discrimination for customer retention activities.

---

## 2. Models Evaluated

Four classification algorithms were tested.

### 1. Logistic Regression

Used as a baseline model because it is simple, interpretable, and provides a strong reference point.

### 2. Decision Tree

Selected because of its interpretability and ability to capture nonlinear relationships.

### 3. Random Forest

Selected as an ensemble method capable of modeling nonlinear relationships while reducing the instability of individual decision trees.

### 4. Gradient Boosting

Selected because boosting methods can capture complex nonlinear relationships and interactions between features.

---

## 3. Initial Model Comparison

The initial model comparison based on accuracy was:

| Model | Accuracy |
|---|---:|
| Gradient Boosting | 71.39% |
| Random Forest | 71.27% |
| Logistic Regression | 71.14% |
| Decision Tree | 71.13% |

Gradient Boosting achieved the highest initial accuracy.

However, the differences between the four models were relatively small.

---

## 4. Why Accuracy Was Not Used Alone

The target variable is imbalanced:

- Active / Retained: 28.87%
- Churn-Risk: 71.13%

A model that predicts a large proportion of customers as Churn-Risk can achieve relatively high accuracy without providing strong discrimination.

Therefore, model selection also considered:

- Precision
- Recall
- F1-Score
- ROC-AUC
- PR-AUC
- Confusion Matrix

---

## 5. Final Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Gradient Boosting | 71.39% | 71.49% | 99.41% | 83.17% | 60.01% |
| Random Forest | 71.27% | 71.43% | 99.35% | 83.11% | 59.05% |
| Logistic Regression | 71.14% | 71.42% | 99.09% | 83.01% | 55.59% |
| Decision Tree | 71.13% | 71.37% | 99.23% | 83.02% | 55.47% |

---

## 6. Selected Model

### Gradient Boosting

Gradient Boosting was selected as the current champion model because it achieved the strongest overall results across the evaluated models.

It achieved:

- Accuracy: 71.39%
- Precision: 71.49%
- Recall: 99.41%
- F1-Score: 83.17%
- ROC-AUC: 60.01%
- PR-AUC: 77.70%

---

## 7. Model Limitation

Although Gradient Boosting was the strongest model among the tested algorithms, its ROC-AUC of approximately 0.60 indicates limited class discrimination.

The model also produced a high number of false positives at the default 0.50 threshold.

Therefore, the model should be treated as a **risk-ranking and prioritization tool**, rather than a definitive churn prediction system.

---

## 8. Business Selection Rationale

Gradient Boosting provides the strongest overall performance among the evaluated models and can produce probability-based customer risk scores.

These probabilities can subsequently be converted into business risk categories and used by the retention recommendation engine.

---

## 9. Conclusion

Gradient Boosting was selected as the champion model for the current project.

However, its limitations are explicitly documented, and risk thresholds will be used to support more targeted retention actions.