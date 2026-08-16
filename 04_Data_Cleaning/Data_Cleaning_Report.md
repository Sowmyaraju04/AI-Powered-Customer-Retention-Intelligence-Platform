# Data Cleaning Report

## 1. Objective

The objective of this phase was to transform the raw Brazilian E-Commerce (Olist) datasets into clean, consistent, and analysis-ready datasets while preserving meaningful business information.

The cleaning process focused on:

- Data type consistency
- Missing value treatment
- Duplicate handling
- Invalid value validation
- Text standardization
- Creation of cleaned datasets

---

# 2. Data Cleaning Activities

## 2.1 Data Type Conversion

Timestamp columns across the Orders and Reviews datasets were converted from string/object formats into datetime formats.

### Key Columns

**Orders**

- `order_purchase_timestamp`
- `order_approved_at`
- `order_delivered_carrier_date`
- `order_delivered_customer_date`
- `order_estimated_delivery_date`

**Reviews**

- `review_creation_date`
- `review_answer_timestamp`

### Business Value

Datetime conversion enables:

- Time-based analysis
- Delivery duration calculations
- Customer recency calculations
- Seasonal analysis
- Feature engineering

**Status:** Completed

---

# 3. Missing Value Treatment

Missing values were evaluated based on their business meaning rather than applying a single blanket treatment.

### Orders

Missing delivery-related timestamps were retained because they can represent cancelled or undelivered orders.

### Products

Missing `product_category_name` values were replaced with:

`Unknown`

This preserves the records while allowing category-based analysis.

### Reviews

Missing review titles were replaced with:

`No Title`

Missing review messages were replaced with:

`No Comment`

This reflects the fact that customers may provide a rating without providing written feedback.

### Business Value

The approach preserves meaningful records while preparing important fields for downstream analysis.

**Status:** Completed

---

# 4. Duplicate Handling

Duplicate records were evaluated across all datasets.

The Geolocation dataset contained:

- Total records before cleaning: **1,000,163**
- Duplicate records: **261,831**
- Records after cleaning: **738,332**

Exact duplicate rows were removed from the Geolocation dataset.

No duplicate rows were identified in the remaining datasets.

### Business Value

Removing exact duplicates reduces unnecessary storage and prevents redundant geographic records from affecting downstream processing.

**Status:** Completed

---

# 5. Invalid Value Validation

Business validation rules were applied to important numeric fields.

### Validation Rules

| Dataset | Field | Rule |
|---|---|---|
| Order Items | `price` | Must be greater than 0 |
| Order Items | `freight_value` | Must be ≥ 0 |
| Payments | `payment_value` | Must not be negative |
| Reviews | `review_score` | Must be between 1 and 5 |
| Products | Weight | Must not be negative |
| Products | Dimensions | Must not be negative |

### Validation Results

- Invalid price values: **0**
- Invalid freight values: **0**
- Invalid payment values: **9 zero-value records**
- Invalid review scores: **0**
- Invalid product weights: **0**
- Invalid product lengths: **0**
- Invalid product heights: **0**
- Invalid product widths: **0**

The 9 payment records with a value of zero were retained because zero-value transactions can represent valid business scenarios and are not necessarily data errors.

### Business Value

Business-rule validation prevents incorrect values from influencing revenue calculations, KPIs, dashboards, and machine learning models.

**Status:** Completed

---

# 6. Text Standardization

Important categorical and text fields were standardized.

### Transformations

- Removed leading and trailing whitespace.
- Standardized order status to lowercase.
- Standardized product categories to lowercase.
- Standardized customer cities to lowercase.
- Standardized customer state codes to uppercase.

### Business Value

Text standardization improves:

- Grouping
- Filtering
- Joins
- Category consistency
- Feature engineering
- Dashboard reporting

**Status:** Completed

---

# 7. Cleaned Dataset Generation

All nine datasets were successfully processed and saved into:

`data/cleaned/`

### Generated Files

- `customers_cleaned.csv`
- `orders_cleaned.csv`
- `order_items_cleaned.csv`
- `payments_cleaned.csv`
- `products_cleaned.csv`
- `reviews_cleaned.csv`
- `sellers_cleaned.csv`
- `geolocation_cleaned.csv`
- `translation_cleaned.csv`

---

# 8. Data Integrity

The raw datasets were preserved without modification.

The cleaning pipeline generates separate cleaned datasets for downstream analysis.

This creates a clear separation between:

**Raw Data → Cleaned Data → Analysis → Feature Engineering → Modeling**

---

# 9. Overall Outcome

The Phase 4 data cleaning process successfully transformed the raw Olist datasets into standardized datasets suitable for downstream analytics.

The process addressed:

- Data type consistency
- Missing values
- Duplicate records
- Invalid business values
- Text consistency
- Clean dataset generation

The cleaned datasets will serve as the trusted input for the next stages of the project.

---

## Phase Status

**Phase 4 – Data Cleaning: COMPLETED ✅**