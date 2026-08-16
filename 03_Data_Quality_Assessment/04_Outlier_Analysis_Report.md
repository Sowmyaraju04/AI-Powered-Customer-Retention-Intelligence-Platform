# 03.4 — Outlier Analysis Report

## Phase 3.4 — Data Quality Assessment

**Project:** AI-Powered Customer Retention Intelligence Platform
**Dataset:** Brazilian E-Commerce (Olist) Dataset
**Assessment:** Outlier Analysis
**Method:** Interquartile Range (IQR)
**Status:** Completed

---

# 1. Objective

The objective of this analysis is to identify unusually high or low numerical observations across the Olist datasets and determine whether they represent:

* Genuine business behavior
* Legitimate extreme transactions
* Statistical anomalies
* Potential data quality issues
* Variables that require domain-specific validation

The analysis is intended to support the upcoming Data Cleaning phase.

Importantly, **statistical outliers are not automatically considered data errors**.

---

# 2. Methodology

The Interquartile Range (IQR) method was used as the initial statistical screening technique.

The IQR is calculated as:

```text
IQR = Q3 - Q1
```

The lower and upper bounds are calculated as:

```text
Lower Bound = Q1 - 1.5 × IQR

Upper Bound = Q3 + 1.5 × IQR
```

Any non-null observation below the lower bound or above the upper bound is classified as an IQR-based statistical outlier.

The analysis was implemented through the reusable `outlier_report()` function in:

```text
src/data/data_profiler.py
```

---

# 3. Important Interpretation Principle

An observation being classified as an IQR outlier does **not** automatically mean it is incorrect.

For an e-commerce dataset, extreme values can represent legitimate business events.

Examples include:

* High-value products
* Large shipments
* Expensive orders
* Customers purchasing multiple products
* Low customer review scores
* Large physical products

Therefore, the analysis combines:

**Statistical Detection + Business Interpretation + Domain Validation**

before any data-cleaning decision is made.

---

# 4. Outlier Detection Results

| Dataset     | Column                        | Outlier Count | Outlier % | Minimum |   Maximum |
| ----------- | ----------------------------- | ------------: | --------: | ------: | --------: |
| customers   | `customer_zip_code_prefix`    |             0 |     0.00% |   1,003 |    99,990 |
| order_items | `order_item_id`               |        13,984 |    12.41% |       1 |        21 |
| order_items | `price`                       |         8,427 |     7.48% |    0.85 |  6,735.00 |
| order_items | `freight_value`               |        12,134 |    10.77% |    0.00 |    409.68 |
| payments    | `payment_sequential`          |         4,526 |     4.36% |       1 |        29 |
| payments    | `payment_installments`        |         6,313 |     6.08% |       0 |        24 |
| payments    | `payment_value`               |         7,981 |     7.68% |    0.00 | 13,664.08 |
| products    | `product_name_lenght`         |           290 |     0.90% |       5 |        76 |
| products    | `product_description_lenght`  |         2,078 |     6.43% |       4 |     3,992 |
| products    | `product_photos_qty`          |           849 |     2.63% |       1 |        20 |
| products    | `product_weight_g`            |         4,551 |    13.81% |       0 |    40,425 |
| products    | `product_length_cm`           |         1,380 |     4.19% |       7 |       105 |
| products    | `product_height_cm`           |         1,892 |     5.74% |       2 |       105 |
| products    | `product_width_cm`            |           912 |     2.77% |       6 |       118 |
| reviews     | `review_score`                |        14,575 |    14.69% |       1 |         5 |
| sellers     | `seller_zip_code_prefix`      |             0 |     0.00% |   1,001 |    99,730 |
| geolocation | `geolocation_zip_code_prefix` |             0 |     0.00% |   1,001 |    99,990 |
| geolocation | `geolocation_lat`             |       168,240 |    16.82% |  -36.61 |     45.07 |
| geolocation | `geolocation_lng`             |        42,348 |     4.23% | -101.47 |    121.11 |

---

# 5. Identifier and Sequence Variables

## 5.1 `order_item_id`

The IQR method identifies **13,984 observations (12.41%)** as outliers.

However, the reason is that:

```text
Q1 = 1
Q3 = 1
IQR = 0
```

Since most orders contain an item with sequence number 1, values greater than 1 are classified as outliers by the mathematical rule.

However, `order_item_id` represents the sequence of an item within an order.

Therefore, values from 1 to 21 can be legitimate.

### Decision

**Retain.**

This variable should not be treated as a continuous business metric for outlier removal.

---

# 6. Payment Sequence Variable

## `payment_sequential`

The IQR method identifies **4,526 observations (4.36%)** as outliers.

The variable represents the sequence of payments associated with an order.

A value greater than 1 can occur when an order has multiple payment records.

### Decision

**Retain.**

This is a sequence variable rather than a continuous measurement requiring statistical outlier treatment.

---

# 7. Product Price

## `order_items.price`

Results:

* Q1: 39.90
* Q3: 134.90
* IQR: 95.00
* Upper Bound: 277.40
* Outliers: 8,427
* Outlier Percentage: 7.48%
* Maximum: 6,735.00

The upper tail contains a meaningful number of high-priced products.

However, an expensive product is not necessarily invalid.

Potential explanations include:

* Premium products
* High-value categories
* Specialty products
* Legitimate large transactions

### Decision

**Retain for now.**

Extreme values should be investigated during Data Cleaning before considering any transformation or removal.

This variable is particularly important for:

* Customer spending
* Average Order Value
* Customer value
* Revenue-at-risk analysis

---

# 8. Freight Value

## `order_items.freight_value`

Results:

* Q1: 13.08
* Q3: 21.15
* IQR: 8.07
* Upper Bound: 33.25
* Outliers: 12,134
* Outlier Percentage: 10.77%
* Maximum: 409.68

The relatively high outlier percentage suggests a long-tailed freight distribution.

Potential business explanations include:

* Large or heavy products
* Long-distance shipments
* High logistics costs
* Remote delivery destinations
* Seller-specific shipping behavior

The minimum value is 0.00, which should also be reviewed because previous data-quality analysis identified zero-freight records.

### Decision

**Retain initially and investigate during Data Cleaning.**

---

# 9. Payment Value

## `payments.payment_value`

Results:

* Q1: 56.79
* Q3: 171.84
* IQR: 115.05
* Upper Bound: 344.41
* Outliers: 7,981
* Outlier Percentage: 7.68%
* Maximum: 13,664.08

High payment values may represent legitimate high-value transactions or orders containing multiple products.

### Decision

**Retain.**

The extreme values should be investigated against their associated orders before any cleaning decision is made.

This variable is important for customer-value and revenue-at-risk analysis.

---

# 10. Payment Installments

## `payments.payment_installments`

Results:

* Q1: 1
* Q3: 4
* IQR: 3
* Upper Bound: 8.50
* Outliers: 6,313
* Outlier Percentage: 6.08%
* Maximum: 24

Values above 8.5 installments are classified as IQR outliers.

However, installment values up to 24 may represent legitimate payment behavior.

The minimum value of 0 also requires validation because installment behavior should be interpreted in combination with payment type.

### Decision

**Retain and investigate during Data Cleaning.**

---

# 11. Review Score

## `reviews.review_score`

Results:

* Q1: 4
* Q3: 5
* IQR: 1
* Lower Bound: 2.50
* Upper Bound: 6.50
* Outliers: 14,575
* Outlier Percentage: 14.69%
* Minimum: 1
* Maximum: 5

The IQR method classifies scores of 1 and 2 as statistical outliers.

However, the valid review-score scale is 1–5.

Therefore, scores of 1 and 2 are **legitimate customer feedback**, not erroneous observations.

In fact, low review scores may provide valuable predictive information for customer retention modeling.

### Decision

**Retain all valid review scores.**

No review scores should be removed based on IQR.

---

# 12. Product Attributes

## 12.1 `product_weight_g`

* Outliers: 4,551
* Outlier Percentage: 13.81%
* Maximum: 40,425 g

The extreme values may represent legitimately heavy products.

### Decision

**Retain initially and investigate physical plausibility.**

---

## 12.2 `product_length_cm`

* Outliers: 1,380
* Outlier Percentage: 4.19%
* Maximum: 105 cm

Large product dimensions may represent legitimate products.

### Decision

**Retain and validate during cleaning.**

---

## 12.3 `product_height_cm`

* Outliers: 1,892
* Outlier Percentage: 5.74%
* Maximum: 105 cm

### Decision

**Retain and validate during cleaning.**

---

## 12.4 `product_width_cm`

* Outliers: 912
* Outlier Percentage: 2.77%
* Maximum: 118 cm

### Decision

**Retain and validate during cleaning.**

---

# 13. Product Catalog Attributes

## `product_name_lenght`

Only **0.90%** of records were classified as outliers.

The maximum value is 76 characters.

Long product names are not inherently invalid.

### Decision

**Retain.**

---

## `product_description_lenght`

Approximately **6.43%** of observations were classified as outliers.

The maximum description length is 3,992 characters.

Long descriptions can be legitimate catalog behavior.

### Decision

**Retain.**

---

## `product_photos_qty`

Approximately **2.63%** of observations were classified as outliers.

The maximum number of photos is 20.

A product containing many photos is not inherently a data-quality issue.

### Decision

**Retain.**

---

# 14. Geographic Variables

## 14.1 ZIP Code Prefixes

The following fields produced no IQR outliers:

* `customer_zip_code_prefix`
* `seller_zip_code_prefix`
* `geolocation_zip_code_prefix`

However, ZIP code prefixes are identifiers rather than continuous numerical variables.

Therefore, IQR is not the appropriate primary validation method for these fields.

### Decision

**Retain and treat as geographical identifiers.**

---

# 15. Geographic Coordinates

## 15.1 Latitude

Results:

* Outliers: 168,240
* Outlier Percentage: 16.82%
* Minimum: -36.61
* Maximum: 45.07

The high IQR outlier percentage does not necessarily indicate erroneous data because geographic coordinates do not follow a conventional business-value distribution.

IQR is therefore not sufficient to determine whether a coordinate is valid.

### Decision

**Do not remove based on IQR.**

Geographic validation should instead be performed using domain-specific coordinate boundaries.

---

## 15.2 Longitude

Results:

* Outliers: 42,348
* Outlier Percentage: 4.23%
* Minimum: -101.47
* Maximum: 121.11

The extreme longitude values warrant further investigation because the project primarily represents Brazilian e-commerce activity.

However, records should not be deleted solely based on the IQR result.

### Decision

**Flag for domain-specific validation during Data Cleaning.**

---

# 16. Outlier Classification

| Variable                | Statistical Finding | Business Interpretation                   | Action            |
| ----------------------- | ------------------- | ----------------------------------------- | ----------------- |
| `order_item_id`         | High outlier count  | Sequence values are legitimate            | Retain            |
| `price`                 | 7.48%               | Potential high-value products             | Investigate       |
| `freight_value`         | 10.77%              | Potential legitimate logistics extremes   | Investigate       |
| `payment_sequential`    | 4.36%               | Payment sequence                          | Retain            |
| `payment_installments`  | 6.08%               | Potential legitimate installment behavior | Investigate       |
| `payment_value`         | 7.68%               | Potential high-value transactions         | Investigate       |
| `review_score`          | 14.69%              | Low ratings are valid customer feedback   | Retain            |
| Product dimensions      | 2.77–13.81%         | Potential legitimate physical extremes    | Investigate       |
| Product text attributes | 0.90–6.43%          | Legitimate catalog variation              | Retain            |
| ZIP prefixes            | 0%                  | Identifier fields                         | Retain            |
| `geolocation_lat`       | 16.82%              | IQR unsuitable for coordinates            | Domain validation |
| `geolocation_lng`       | 4.23%               | Potential geographic anomalies            | Domain validation |

---

# 17. Key Findings

### Finding 1 — Financial Variables Have Long-Tailed Distributions

`price`, `freight_value`, and `payment_value` contain meaningful numbers of statistical outliers.

This indicates that the e-commerce data contains a long tail of high-value transactions.

These observations should be investigated rather than automatically removed.

---

### Finding 2 — Review Score Outliers Are Legitimate

The IQR method flags 14.69% of review scores, primarily because the distribution is concentrated around scores of 4 and 5.

Low scores represent genuine customer dissatisfaction and are potentially valuable for retention modeling.

They should therefore be retained.

---

### Finding 3 — Sequence Variables Produce False Statistical Outliers

`order_item_id` and `payment_sequential` produce outliers because their distributions are heavily concentrated at 1.

This demonstrates that automated outlier detection must account for variable semantics.

---

### Finding 4 — Product Attributes Contain Legitimate Extremes

Product weight and dimensions contain statistical outliers that may represent large or heavy products.

These should be validated using business and physical plausibility rules.

---

### Finding 5 — Geographic Coordinates Require Domain Validation

Latitude and longitude should not be judged solely using IQR.

Geographic coordinates require location-specific validation.

---

# 18. Data Cleaning Recommendations

The following actions are recommended for Phase 4:

### Financial variables

Investigate extreme:

* `price`
* `freight_value`
* `payment_value`

values against their associated orders and products.

### Payment behavior

Validate:

* `payment_installments`
* Zero-value payments
* Multiple payment records

### Product dimensions

Check:

* Zero weights
* Extreme dimensions
* Missing physical attributes
* Physically implausible combinations

### Geographic coordinates

Validate latitude and longitude using appropriate geographical rules rather than IQR.

### Review scores

Retain valid scores from 1 to 5.

Do not remove low review scores simply because they are statistical outliers.

---

# 19. Important Data Quality Principle

This analysis demonstrates a critical principle:

> **A statistical outlier is not automatically a data-quality error.**

A production-quality data pipeline should combine:

```text
Statistical Detection
        +
Business Rules
        +
Domain Knowledge
        =
Reliable Data Quality Decision
```

This prevents legitimate business observations from being incorrectly removed.

---

# 20. Phase 3.4 Conclusion

The IQR-based analysis successfully identified unusual numerical observations across the Olist datasets.

However, the results demonstrate that different variable types require different validation strategies.

Financial variables require transaction-level investigation.

Review scores should be retained because low ratings represent legitimate customer feedback.

Sequence and identifier variables should not be treated as continuous numerical measures.

Geographic coordinates require domain-specific validation rather than relying solely on statistical methods.

Therefore, **no observations will be automatically removed as a result of this analysis**.

The identified variables will be investigated and addressed during the Data Cleaning phase where appropriate.

---

## Phase Status

**Phase 3.4 — Outlier Analysis: ✅ COMPLETED**

### Primary Method

**Interquartile Range (IQR)**

### Key Principle

> **Outlier detection is a screening mechanism, not an automatic data-removal mechanism.**

### Next Phase

**Phase 5 — Data Cleaning**

The Data Cleaning phase will address the issues identified throughout the Data Quality Assessment, including missing values, duplicate considerations, data type corrections, temporal validation, and domain-specific outlier investigation.
