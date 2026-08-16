# Missing Values Report

## Objective

The objective of this analysis is to identify missing values across all datasets before data cleaning and feature engineering. Missing values can impact data quality, statistical analysis, machine learning model performance, and business decision-making.

---

# Missing Value Summary

| Dataset | Column | Missing Count | Missing % |
|---------|--------|--------------:|----------:|
| Orders | order_approved_at | 160 | 0.16% |
| Orders | order_delivered_carrier_date | 1,783 | 1.79% |
| Orders | order_delivered_customer_date | 2,965 | 2.98% |
| Products | product_category_name | 610 | 1.85% |
| Products | product_name_lenght | 610 | 1.85% |
| Products | product_description_lenght | 610 | 1.85% |
| Products | product_photos_qty | 610 | 1.85% |
| Products | product_weight_g | 2 | 0.01% |
| Products | product_length_cm | 2 | 0.01% |
| Products | product_height_cm | 2 | 0.01% |
| Products | product_width_cm | 2 | 0.01% |
| Reviews | review_comment_title | 87,656 | 88.34% |
| Reviews | review_comment_message | 58,247 | 58.70% |

---

# Key Observations

- Missing values are concentrated in the **Orders**, **Products**, and **Reviews** datasets.
- The **Reviews** dataset has the highest percentage of missing values.
- More than **88%** of review titles are missing.
- Approximately **59%** of review messages are missing.
- Product information has only a small proportion of missing values (approximately **1.85%**).
- Missing delivery dates in the Orders dataset are expected for canceled or undelivered orders and should be investigated before deciding on a treatment strategy.

---

# Business Interpretation

Not all missing values indicate poor data quality. Some missing values occur naturally due to business processes.

Examples include:

- Delivery dates may be unavailable for canceled orders.
- Customers often submit only a rating without writing a review title or review message.

Therefore, each missing value must be evaluated based on its business context before applying any cleaning strategy.

---

# Initial Recommendations

- Investigate business reasons before imputing or deleting missing values.
- Preserve business-related missing values that carry useful information.
- Remove or impute only when justified.
- Document every cleaning decision during the Data Cleaning phase.

---

## Status

✅ Missing Value Analysis Completed