# Data Quality Summary

## Objective

The purpose of this phase is to assess the overall quality and structure of the datasets before performing data cleaning and feature engineering.

---

## Dataset Summary

| Dataset | Rows | Columns | Memory (MB) |
|----------|-----:|--------:|------------:|
| Customers | 99,441 | 5 | 11.03 |
| Orders | 99,441 | 8 | 21.95 |
| Order Items | 112,650 | 7 | 17.40 |
| Payments | 103,886 | 5 | 8.11 |
| Products | 32,951 | 9 | 3.73 |
| Reviews | 99,224 | 7 | 17.84 |
| Sellers | 3,095 | 4 | 0.22 |
| Geolocation | 1,000,163 | 5 | 50.12 |
| Translation | 71 | 2 | 0.00 |

---

## Key Observations

- The project contains **9 datasets**.
- The Geolocation dataset is the largest, containing over **1 million records**.
- The Sellers dataset is the smallest.
- Orders and Customers have an equal number of records, indicating a one-to-one relationship.
- The dataset sizes are manageable for in-memory processing using Pandas.

---

## Business Interpretation

The dataset summary provides an overview of the scale and complexity of the available data. Understanding dataset size and memory usage helps estimate computational requirements, identify large datasets that may require optimization, and prepare for downstream data quality assessment, feature engineering, and machine learning.

---

## Status

✅ Dataset Summary Completed