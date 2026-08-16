"""
Data Validator Module

Purpose:
Validate all loaded datasets.
"""

from src.data.data_loader import load_all_data


def validate_datasets():
    """
    Validate all datasets and print summary information.
    """

    datasets = load_all_data()

    print("=" * 60)
    print("DATA VALIDATION REPORT")
    print("=" * 60)

    for name, df in datasets.items():
        print(f"\nDataset: {name}")
        print(f"Rows: {df.shape[0]}")
        print(f"Columns: {df.shape[1]}")
        print(f"Duplicate Rows: {df.duplicated().sum()}")
        print("Missing Values:")
        print(df.isnull().sum())
        print("-" * 60)


if __name__ == "__main__":
    validate_datasets()