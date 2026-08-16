# Machine Learning Setup

## AI-Powered Customer Retention Intelligence Platform

---

## 1. Objective

The objective of the machine learning phase is to develop a predictive customer-risk model that identifies customers who exhibit behavioral patterns associated with inactivity.

The model is designed to support customer retention by providing:

- Customer churn-risk probability
- Customer risk classification
- Risk prioritization
- Explainable predictions
- Inputs for the retention recommendation engine

The machine learning model is not intended to claim certain future churn. Instead, it estimates the likelihood that a customer belongs to the inactivity-based risk group defined during feature engineering.

---

## 2. Modeling Dataset

The machine learning model uses the processed customer-level dataset:

`data/processed/customer_retention_model_data.csv`

The dataset contains customer-level behavioral, transactional, satisfaction, and payment-related features.

---

## 3. Target Variable

The target variable is:

`churn_label`

The target was created during feature engineering using an inactivity-based business rule.

| Value | Meaning |
|---|---|
| 0 | Active / Retained |
| 1 | Churn-Risk |

The churn definition is based on customer inactivity beyond the predefined business threshold.

Therefore, the model should be interpreted as an **inactivity-risk prediction model** rather than a confirmed future churn prediction model.

---

## 4. Target Distribution

The modeling dataset contains:

| Customer Segment | Count | Percentage |
|---|---:|---:|
| Active / Retained | 27,744 | 28.87% |
| Churn-Risk | 68,352 | 71.13% |

The target is therefore imbalanced, with the Churn-Risk class representing approximately 71% of the dataset.

This imbalance was considered during model evaluation.

---

## 5. Selected Predictive Features

The following features were selected for modeling:

- Frequency
- Monetary
- Average Review Score
- Preferred Payment Method
- Average Order Value

These features represent different dimensions of customer behavior:

### Frequency
Measures the number of purchases associated with a customer.

### Monetary
Measures total customer spending.

### Average Review Score
Represents customer satisfaction based on available review scores.

### Preferred Payment Method
Represents the customer's most frequently used payment method.

### Average Order Value
Measures the average monetary value of customer orders.

---

## 6. Excluded Features

Several variables were intentionally excluded.

### Customer ID

`customer_unique_id`

This is an identifier and does not contain predictive behavioral information.

### Recency

`Recency` was excluded because the churn target was defined using customer inactivity.

Including Recency directly would introduce target leakage because the feature would contain information directly related to how the target was created.

### Customer Risk

`Customer_Risk` was excluded because it is a derived risk classification and would introduce information from the target-generation process.

### Customer Lifetime Value

`customer_lifetime_value` was excluded because in the current feature-engineering implementation it duplicates the information contained in `Monetary`.

Including both would introduce redundant information.

---

## 7. Data Splitting

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

The split used:

- `random_state = 42`
- `stratify = y`

Stratification was used to preserve the target-class distribution across training and testing datasets.

---

## 8. Preprocessing

Numerical features were processed using median imputation.

Categorical variables were processed using:

- Most-frequent imputation
- One-Hot Encoding

The preprocessing steps were integrated into Scikit-learn pipelines to ensure consistent transformation during training and prediction.

---

## 9. Modeling Strategy

Multiple classification algorithms were evaluated:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Gradient Boosting

The models were evaluated using multiple performance metrics rather than relying solely on accuracy.

---

## 10. Evaluation Metrics

The following metrics were used:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- PR-AUC
- Confusion Matrix

Because the dataset contains class imbalance, special attention was given to Recall, F1-Score, ROC-AUC, PR-AUC, and false-positive behavior.

---

## 11. Conclusion

The ML setup establishes a controlled and leakage-aware predictive modeling environment.

The selected features capture customer spending, satisfaction, purchasing behavior, and payment preferences while avoiding direct leakage from the inactivity-based target definition.