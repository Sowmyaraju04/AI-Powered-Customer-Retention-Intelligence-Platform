# Cleaning Decisions

## Objective

Document the rationale behind every data cleaning decision made during Phase 4.

---

## 1. DateTime Conversion

**Decision:**
Converted all timestamp columns to datetime format.

**Reason:**
Required for delivery analysis, customer recency calculations, and time-based feature engineering.

---

## 2. Missing Values

### Orders

**Decision:**
Retained missing delivery-related dates.

**Reason:**
Cancelled and unavailable orders naturally do not have delivery timestamps.

---

### Products

**Decision:**
Replaced missing `product_category_name` with **"Unknown"**.

**Reason:**
Preserves records while allowing category-based analysis.

---

### Reviews

**Decision:**
Replaced missing review titles with **"No Title"** and review messages with **"No Comment"**.

**Reason:**
Many customers provide only a rating without textual feedback.

---

## 3. Duplicate Records

**Decision:**
Removed exact duplicate rows from the Geolocation dataset.

**Reason:**
Duplicate geographic coordinates increase storage and processing without adding analytical value.

---

## 4. Invalid Values

**Decision:**
Validated numeric business rules.

**Reason:**
No negative prices, freight values, review scores, or product dimensions were found.

Payment values equal to **0** were retained because they can represent valid business scenarios such as fully discounted or voucher-based transactions.

---

## 5. Text Standardization

**Decision:**
Standardized important text columns.

**Reason:**
Improves grouping, filtering, joins, dashboard consistency, and machine learning feature quality.

---

## Final Outcome

The cleaned datasets preserve business meaning while improving consistency, quality, and usability for downstream analytics and machine learning.