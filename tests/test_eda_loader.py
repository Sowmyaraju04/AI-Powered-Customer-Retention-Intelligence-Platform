"""
Test EDA Data Loader
"""

from src.analysis.eda_loader import load_cleaned_data


print("=" * 70)
print("EDA DATA LOADER TEST")
print("=" * 70)


datasets = load_cleaned_data()


for name, df in datasets.items():

    print(
        f"{name:<15} "
        f"Rows: {df.shape[0]:<10} "
        f"Columns: {df.shape[1]}"
    )


print("=" * 70)
print("All cleaned datasets loaded successfully.")
print("=" * 70)