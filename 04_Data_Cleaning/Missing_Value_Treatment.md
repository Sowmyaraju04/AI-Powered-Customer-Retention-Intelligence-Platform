# Missing Value Treatment

## Objective

Handle missing values using business-driven rules while preserving meaningful business information.

---

# Strategy

## Orders

- Delivery-related timestamps were left unchanged.
- Missing values represent cancelled or undelivered orders.

## Products

- Missing product categories were replaced with **"Unknown"**.
- This preserves records for downstream analysis.

## Reviews

- Missing review titles were replaced with **"No Title"**.
- Missing review messages were replaced with **"No Comment"**.
- Customers can legitimately provide only a rating without text.

---

# Business Justification

Missing values should not always be removed or imputed with arbitrary values. Each treatment decision should reflect the underlying business process to maintain data quality and analytical integrity.

---

## Status

✅ Completed

## Validation Results

### Products Dataset

- Successfully replaced missing values in `product_category_name`.
- Remaining missing values were intentionally retained for later business-driven evaluation.

### Reviews Dataset

- Successfully replaced missing review titles with **"No Title"**.
- Successfully replaced missing review messages with **"No Comment"**.

### Result

The cleaning strategy preserved business meaning while preparing key fields for downstream analysis and machine learning.