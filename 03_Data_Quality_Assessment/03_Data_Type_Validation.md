# 03 — Data Type Validation Report

## Phase 3.3 — Data Quality Assessment

**Project:** AI-Powered Customer Retention Intelligence Platform
**Dataset:** Brazilian E-Commerce (Olist) Dataset
**Assessment:** Data Type Validation
**Status:** Completed

---

## 1. Objective

The objective of this assessment is to validate the data types of all columns across the Olist datasets and determine whether the detected data types are appropriate for their respective business meanings and future analytical use.

Data type validation is important because incorrect data types can affect:

* Data transformations
* SQL analysis
* Aggregations
* Date calculations
* Feature engineering
* Machine learning
* Business reporting
* Data visualization

The assessment was performed using the automated `data_type_report()` profiling function.

---

## 2. Validation Scope

The assessment covered the following datasets:

* Customers
* Orders
* Order Items
* Payments
* Products
* Reviews
* Sellers
* Geolocation
* Translation

A total of **52 columns** were profiled.

---

## 3. Overall Findings

The majority of columns have technically appropriate data types based on their business purpose.

The main issue identified is that several **date and timestamp columns are currently stored as strings (`str`) rather than datetime values**.

Other observations include:

* Identifier fields are appropriately stored as strings.
* Financial fields are appropriately stored as floating-point numbers.
* Categorical fields are appropriately stored as strings.
* Review scores and other count-based fields are represented using integer types.
* Several product attributes are represented as `float64`, which may be appropriate because of missing values.

---

# 4. Detailed Data Type Assessment

## 4.1 Customer Dataset

| Column                     | Data Type | Assessment  |
| -------------------------- | --------- | ----------- |
| `customer_id`              | `str`     | Appropriate |
| `customer_unique_id`       | `str`     | Appropriate |
| `customer_zip_code_prefix` | `int64`   | Appropriate |
| `customer_city`            | `str`     | Appropriate |
| `customer_state`           | `str`     | Appropriate |

### Observation

Customer identifiers are stored as strings, which is appropriate because they represent unique identifiers rather than numerical measurements.

The ZIP code prefix is stored as an integer. Although technically valid, it should be treated as a categorical/geographical identifier during analysis rather than as a continuous numerical variable.

**Status: ✅ Acceptable**

---

# 5. Orders Dataset

| Column                          | Data Type | Assessment             |
| ------------------------------- | --------- | ---------------------- |
| `order_id`                      | `str`     | Appropriate            |
| `customer_id`                   | `str`     | Appropriate            |
| `order_status`                  | `str`     | Appropriate            |
| `order_purchase_timestamp`      | `str`     | ⚠️ Requires conversion |
| `order_approved_at`             | `str`     | ⚠️ Requires conversion |
| `order_delivered_carrier_date`  | `str`     | ⚠️ Requires conversion |
| `order_delivered_customer_date` | `str`     | ⚠️ Requires conversion |
| `order_estimated_delivery_date` | `str`     | ⚠️ Requires conversion |

### Observation

The identifier and categorical fields have appropriate data types.

However, the five temporal fields are currently stored as strings.

These fields should ultimately be represented as datetime values because they will be required for:

* Customer tenure
* Recency
* Purchase frequency
* Delivery time
* Delivery delay
* Churn definition
* Observation windows
* Time-based feature engineering

**Status: 🟨 Requires correction during Data Cleaning**

---

# 6. Order Items Dataset

| Column                | Data Type | Assessment             |
| --------------------- | --------- | ---------------------- |
| `order_id`            | `str`     | Appropriate            |
| `order_item_id`       | `int64`   | Appropriate            |
| `product_id`          | `str`     | Appropriate            |
| `seller_id`           | `str`     | Appropriate            |
| `shipping_limit_date` | `str`     | ⚠️ Requires conversion |
| `price`               | `float64` | Appropriate            |
| `freight_value`       | `float64` | Appropriate            |

### Observation

The financial fields `price` and `freight_value` are correctly represented as floating-point values because monetary values may contain decimals.

`shipping_limit_date` is stored as a string and should be converted to datetime during Data Cleaning.

**Status: 🟨 Requires correction for temporal field**

---

# 7. Payments Dataset

| Column                 | Data Type | Assessment  |
| ---------------------- | --------- | ----------- |
| `order_id`             | `str`     | Appropriate |
| `payment_sequential`   | `int64`   | Appropriate |
| `payment_type`         | `str`     | Appropriate |
| `payment_installments` | `int64`   | Appropriate |
| `payment_value`        | `float64` | Appropriate |

### Observation

The payment fields have appropriate data types.

`payment_value` is correctly represented as a floating-point value because it represents a monetary amount.

`payment_type` is appropriately represented as a categorical/string field.

**Status: ✅ Acceptable**

---

# 8. Products Dataset

| Column                       | Data Type | Assessment  |
| ---------------------------- | --------- | ----------- |
| `product_id`                 | `str`     | Appropriate |
| `product_category_name`      | `str`     | Appropriate |
| `product_name_lenght`        | `float64` | Review      |
| `product_description_lenght` | `float64` | Review      |
| `product_photos_qty`         | `float64` | Review      |
| `product_weight_g`           | `float64` | Appropriate |
| `product_length_cm`          | `float64` | Appropriate |
| `product_height_cm`          | `float64` | Appropriate |
| `product_width_cm`           | `float64` | Appropriate |

### Observation

The physical product measurements are appropriately represented as floating-point values.

The count-like fields such as:

* `product_name_lenght`
* `product_description_lenght`
* `product_photos_qty`

are also represented as `float64`.

This does not automatically indicate a data quality problem because missing values can cause Pandas to represent otherwise integer-like variables as floating-point values.

These fields will therefore be investigated further during Data Cleaning rather than being converted blindly.

**Status: 🟨 Requires validation during cleaning**

---

# 9. Reviews Dataset

| Column                    | Data Type | Assessment             |
| ------------------------- | --------- | ---------------------- |
| `review_id`               | `str`     | Appropriate            |
| `order_id`                | `str`     | Appropriate            |
| `review_score`            | `int64`   | Appropriate            |
| `review_comment_title`    | `str`     | Appropriate            |
| `review_comment_message`  | `str`     | Appropriate            |
| `review_creation_date`    | `str`     | ⚠️ Requires conversion |
| `review_answer_timestamp` | `str`     | ⚠️ Requires conversion |

### Observation

The review score is correctly represented as an integer.

The review text fields are appropriately represented as strings.

The two review timestamp fields are currently stored as strings and should be converted to datetime values during Data Cleaning.

**Status: 🟨 Requires correction for temporal fields**

---

# 10. Sellers Dataset

| Column                   | Data Type | Assessment  |
| ------------------------ | --------- | ----------- |
| `seller_id`              | `str`     | Appropriate |
| `seller_zip_code_prefix` | `int64`   | Appropriate |
| `seller_city`            | `str`     | Appropriate |
| `seller_state`           | `str`     | Appropriate |

### Observation

Seller identifiers and categorical geographical fields have appropriate data types.

The ZIP code prefix should be treated as a geographical identifier rather than a continuous numerical measure.

**Status: ✅ Acceptable**

---

# 11. Geolocation Dataset

| Column                        | Data Type | Assessment  |
| ----------------------------- | --------- | ----------- |
| `geolocation_zip_code_prefix` | `int64`   | Appropriate |
| `geolocation_lat`             | `float64` | Appropriate |
| `geolocation_lng`             | `float64` | Appropriate |
| `geolocation_city`            | `str`     | Appropriate |
| `geolocation_state`           | `str`     | Appropriate |

### Observation

Latitude and longitude are correctly represented as floating-point values.

The geographical and categorical fields also have appropriate representations.

**Status: ✅ Acceptable**

---

# 12. Translation Dataset

| Column                          | Data Type | Assessment  |
| ------------------------------- | --------- | ----------- |
| `product_category_name`         | `str`     | Appropriate |
| `product_category_name_english` | `str`     | Appropriate |

### Observation

Both fields contain category names and are correctly represented as strings.

**Status: ✅ Acceptable**

---

# 13. Critical Data Type Issues Identified

The following **8 temporal columns** require conversion from string to datetime:

| Dataset     | Column                          |
| ----------- | ------------------------------- |
| Orders      | `order_purchase_timestamp`      |
| Orders      | `order_approved_at`             |
| Orders      | `order_delivered_carrier_date`  |
| Orders      | `order_delivered_customer_date` |
| Orders      | `order_estimated_delivery_date` |
| Order Items | `shipping_limit_date`           |
| Reviews     | `review_creation_date`          |
| Reviews     | `review_answer_timestamp`       |

These fields should not remain as strings for downstream temporal analytics.

---

# 14. Business Impact

The identified datetime issue is particularly important for the Customer Retention Intelligence Platform.

Several core features depend directly on accurate dates.

### Customer Recency

```text
Recency = Analysis Date − Last Purchase Date
```

### Customer Tenure

```text
Tenure = Analysis Date − First Purchase Date
```

### Delivery Delay

```text
Delivery Delay =
Actual Delivery Date − Estimated Delivery Date
```

### Purchase Frequency

```text
Purchase Frequency =
Number of Orders / Customer Observation Period
```

If the underlying dates remain strings, these calculations cannot be performed reliably.

Therefore, correcting these data types is a prerequisite for subsequent feature engineering and churn modeling.

---

# 15. Data Type Validation Principles Applied

The assessment follows an important data engineering principle:

> **A technically valid data type is not necessarily a business-appropriate data type.**

For example:

```text
order_purchase_timestamp → str
```

is technically valid from a Pandas perspective.

However, because the column represents a timestamp, the business-appropriate type is:

```text
datetime
```

Therefore, validation considers both:

**Technical Representation + Business Meaning**

---

# 16. Recommended Actions

The following actions will be performed during the Data Cleaning phase:

### 1. Convert date columns

Convert all identified timestamp fields from strings to datetime.

### 2. Validate conversion

Check for values that fail during datetime parsing.

### 3. Investigate missing timestamps

Determine whether missing values are legitimate based on order status or represent data quality problems.

### 4. Validate chronological relationships

Check logical relationships such as:

```text
Purchase Date
      ≤
Approval Date
      ≤
Carrier Delivery Date
      ≤
Customer Delivery Date
```

where applicable.

### 5. Re-run validation

Run the data type profiling function after cleaning to confirm that the expected data types have been achieved.

---

# 17. Final Assessment

| Assessment Area             | Result                 |
| --------------------------- | ---------------------- |
| Identifier data types       | ✅ Appropriate          |
| Categorical data types      | ✅ Appropriate          |
| Financial data types        | ✅ Appropriate          |
| Geographic numerical fields | ✅ Appropriate          |
| Product numerical fields    | 🟨 Requires validation |
| Temporal data types         | 🟨 Requires correction |
| Overall Data Type Quality   | 🟨 Needs Attention     |

---

# 18. Conclusion

The Data Type Validation assessment confirms that the majority of the Olist datasets have technically appropriate data types.

The primary issue identified is that **8 temporal columns are stored as strings instead of datetime values**.

These fields will be corrected during the Data Cleaning phase because they are essential for customer-level behavioral analysis, churn definition, feature engineering, and predictive modeling.

No data has been removed or modified as part of this profiling activity.

The findings from this assessment will be carried forward into the Data Cleaning plan.

---

## Phase 3.3 Status

**Data Type Validation: ✅ COMPLETED**

### Key Finding

> **Eight temporal fields require conversion from string to datetime before temporal analysis and customer-level feature engineering.**

### Next Phase

**Phase 3.4 — Outlier Analysis**

The next phase will identify statistically unusual observations in key numerical business variables and determine whether those observations represent genuine business behavior or potential data quality issues.
