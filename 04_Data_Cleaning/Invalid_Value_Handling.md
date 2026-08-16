# Invalid Value Handling

## Objective

Validate important business rules to ensure that numeric fields contain realistic and acceptable values before analysis and machine learning.

---

## Validation Rules

| Dataset | Validation Rule |
|---------|-----------------|
| Order Items | Price must be greater than 0 |
| Order Items | Freight value must be greater than or equal to 0 |
| Payments | Payment value must be greater than 0 |
| Reviews | Review score must be between 1 and 5 |
| Products | Product dimensions and weight must not be negative |

---

## Validation Results

- No invalid prices detected.
- No invalid freight values detected.
- No invalid payment values detected.
- No invalid review scores detected.
- No negative product dimensions or weights detected.

---

## Business Justification

Validating business rules before analysis prevents inaccurate KPIs, misleading dashboards, and unreliable machine learning models. This step ensures that the cleaned dataset is trustworthy for downstream analytics.

---

## Status

✅ Completed