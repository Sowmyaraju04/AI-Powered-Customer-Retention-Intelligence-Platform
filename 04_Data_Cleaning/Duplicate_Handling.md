# Duplicate Handling

## Objective

Remove duplicate records while preserving valid business information.

---

## Cleaning Strategy

All datasets were evaluated for duplicate records.

Only the **Geolocation** dataset contained exact duplicate rows.

These duplicates were removed using the `drop_duplicates()` method.

No duplicate records were found in the remaining datasets.

---

## Business Justification

The Geolocation dataset contains repeated latitude and longitude combinations. Removing exact duplicate rows reduces storage requirements and improves processing efficiency without affecting analytical results.

Transactional datasets such as Orders, Payments, Customers, Reviews, and Order Items were left unchanged because they contained no duplicate records.

---

## Validation

- Duplicate records successfully removed from the Geolocation dataset.
- All remaining datasets contain zero duplicate rows.

---

## Status

✅ Completed


## Validation Results

### Before Cleaning

- Total Records: 1,000,163
- Duplicate Records: 261,831

### After Cleaning

- Remaining Records: 738,332
- Duplicate Records: 0

### Result

Duplicate records were successfully removed from the Geolocation dataset while preserving all transactional datasets. This improves storage efficiency and prevents redundant geographic records from affecting downstream analysis.