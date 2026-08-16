# Duplicate Records Report

## Objective

The objective of this analysis is to identify duplicate records across all datasets before performing data cleaning and feature engineering. Duplicate records can lead to inaccurate reporting, incorrect business insights, and biased machine learning models if not properly handled.

---

# Duplicate Summary

| Dataset | Total Rows | Duplicate Rows | Duplicate % |
|----------|-----------:|---------------:|------------:|
| Customers | 99,441 | 0 | 0.00% |
| Orders | 99,441 | 0 | 0.00% |
| Order Items | 112,650 | 0 | 0.00% |
| Payments | 103,886 | 0 | 0.00% |
| Products | 32,951 | 0 | 0.00% |
| Reviews | 99,224 | 0 | 0.00% |
| Sellers | 3,095 | 0 | 0.00% |
| Geolocation | 1,000,163 | 261,831 | 26.18% |
| Translation | 71 | 0 | 0.00% |

---

# Key Observations

- Eight datasets contain no duplicate records.
- The Geolocation dataset contains **261,831 duplicate records (26.18%)**.
- These duplicates are expected because multiple postal codes can share identical latitude and longitude coordinates.
- Duplicate records in the Geolocation dataset should be evaluated carefully before removal, as they may represent valid business information rather than data quality issues.

---

# Business Interpretation

Duplicate records do not always indicate poor data quality. In the Olist dataset, duplicate geographical coordinates are a consequence of the data collection process and may legitimately correspond to multiple zip code prefixes.

Therefore, duplicate removal should be based on business understanding rather than performed automatically.

---

# Initial Recommendations

- Retain duplicates in transactional datasets unless business rules indicate otherwise.
- Investigate Geolocation duplicates during the Data Cleaning phase to determine the appropriate deduplication strategy.
- Document all duplicate handling decisions to maintain transparency and reproducibility.

---

## Status

✅ Duplicate Analysis Completed