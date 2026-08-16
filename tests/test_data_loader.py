"""
Test Data Loader

Purpose:
Verify that all Olist datasets load successfully.
"""

from src.data.data_loader import load_all_data


def main():
    """
    Test the data loader.
    """

    datasets = load_all_data()

    print("=" * 60)
    print("DATA LOADER TEST")
    print("=" * 60)

    print("\nDatasets Loaded Successfully\n")

    for name, df in datasets.items():
        print(f"{name:<15} Shape: {df.shape}")

    print("\nOrders Dataset Preview")
    print("-" * 60)
    print(datasets["orders"].head())


if __name__ == "__main__":
    main()