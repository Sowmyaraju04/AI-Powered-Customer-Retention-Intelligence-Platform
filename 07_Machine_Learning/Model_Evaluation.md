# Model Evaluation

## AI-Powered Customer Retention Intelligence Platform

---

## 1. Evaluation Objective

The objective of model evaluation is to determine how effectively the trained machine learning models distinguish between Active / Retained customers and customers classified as Churn-Risk.

Because the target is imbalanced, multiple evaluation metrics were considered.

---

## 2. Evaluation Metrics

### Accuracy

Measures the overall proportion of correctly classified customers.

### Precision

Measures the proportion of customers predicted as Churn-Risk who were actually classified as Churn-Risk.

### Recall

Measures the proportion of actual Churn-Risk customers successfully identified by the model.

### F1-Score

Provides a balance between Precision and Recall.

### ROC-AUC

Measures the model's ability to distinguish between the two classes across classification thresholds.

### PR-AUC

Provides additional evaluation of precision-recall behavior, which is useful for imbalanced classification problems.

---

## 3. Model Performance

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Gradient Boosting | 71.39% | 71.49% | 99.41% | 83.17% | 60.01% |
| Random Forest | 71.27% | 71.43% | 99.35% | 83.11% | 59.05% |
| Logistic Regression | 71.14% | 71.42% | 99.09% | 83.01% | 55.59% |
| Decision Tree | 71.13% | 71.37% | 99.23% | 83.02% | 55.47% |

---

## 4. Gradient Boosting Confusion Matrix

At the default classification threshold of 0.50:

```text
[[130, 5419],
 [ 80, 13591]]