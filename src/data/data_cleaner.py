"""
Data Cleaner Module

Project:
AI-Powered Customer Retention Intelligence Platform

Purpose:
Perform data cleaning and preprocessing.
"""

import pandas as pd

from src.data.data_loader import load_all_data


def convert_datetime_columns():
    """
    Convert timestamp columns to datetime format.

    Returns
    -------
    dict
        Dictionary of cleaned DataFrames.
    """

    datasets = load_all_data()

    orders = datasets["orders"]

    datetime_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for column in datetime_columns:
        orders[column] = pd.to_datetime(
            orders[column],
            errors="coerce"
        )

    reviews = datasets["reviews"]

    reviews["review_creation_date"] = pd.to_datetime(
        reviews["review_creation_date"],
        errors="coerce"
    )

    reviews["review_answer_timestamp"] = pd.to_datetime(
        reviews["review_answer_timestamp"],
        errors="coerce"
    )

    datasets["orders"] = orders
    datasets["reviews"] = reviews

    return datasets


def handle_missing_values():
    """
    Handle missing values using business-driven rules.

    Returns
    -------
    dict
        Dictionary of cleaned DataFrames.
    """

    datasets = convert_datetime_columns()

    # -------------------------
    # Orders Dataset
    # -------------------------

    orders = datasets["orders"]

    # Keep missing delivery-related dates.
    # These are valid for cancelled or unavailable orders.

    datasets["orders"] = orders

    # -------------------------
    # Products Dataset
    # -------------------------

    products = datasets["products"]

    products["product_category_name"] = (
        products["product_category_name"]
        .fillna("Unknown")
    )

    datasets["products"] = products

    # -------------------------
    # Reviews Dataset
    # -------------------------

    reviews = datasets["reviews"]

    reviews["review_comment_title"] = (
        reviews["review_comment_title"]
        .fillna("No Title")
    )

    reviews["review_comment_message"] = (
        reviews["review_comment_message"]
        .fillna("No Comment")
    )

    datasets["reviews"] = reviews

    return datasets

def handle_duplicates():
    """
    Remove duplicate records where appropriate.

    Returns
    -------
    dict
        Dictionary of cleaned DataFrames.
    """

    datasets = handle_missing_values()

    geolocation = datasets["geolocation"]

    before = len(geolocation)

    geolocation = geolocation.drop_duplicates()

    after = len(geolocation)

    removed = before - after

    print("=" * 60)
    print("DUPLICATE HANDLING")
    print("=" * 60)
    print(f"Duplicates Removed : {removed}")
    print(f"Remaining Records  : {after}")

    datasets["geolocation"] = geolocation

    return datasets


def handle_invalid_values():
    """
    Validate business rules for important numeric columns.

    Returns
    -------
    dict
        Dictionary of validated DataFrames.
    """

    datasets = handle_duplicates()

    order_items = datasets["order_items"]
    payments = datasets["payments"]
    reviews = datasets["reviews"]
    products = datasets["products"]

    print("=" * 60)
    print("INVALID VALUE VALIDATION")
    print("=" * 60)

    # Order Items
    invalid_price = (order_items["price"] <= 0).sum()
    invalid_freight = (order_items["freight_value"] < 0).sum()

    # Payments
    invalid_payment = (payments["payment_value"] <= 0).sum()

    # Reviews
    invalid_review = (
        (~reviews["review_score"].between(1, 5))
    ).sum()

    # Products
    invalid_weight = (products["product_weight_g"] < 0).sum()
    invalid_length = (products["product_length_cm"] < 0).sum()
    invalid_height = (products["product_height_cm"] < 0).sum()
    invalid_width = (products["product_width_cm"] < 0).sum()

    print(f"Invalid Price Values        : {invalid_price}")
    print(f"Invalid Freight Values      : {invalid_freight}")
    print(f"Invalid Payment Values      : {invalid_payment}")
    print(f"Invalid Review Scores       : {invalid_review}")
    print(f"Invalid Product Weights     : {invalid_weight}")
    print(f"Invalid Product Lengths     : {invalid_length}")
    print(f"Invalid Product Heights     : {invalid_height}")
    print(f"Invalid Product Widths      : {invalid_width}")

    return datasets


def standardize_text():
    """
    Standardize text columns.

    Returns
    -------
    dict
        Dictionary of cleaned DataFrames.
    """

    datasets = handle_invalid_values()

    # Orders
    datasets["orders"]["order_status"] = (
        datasets["orders"]["order_status"]
        .str.strip()
        .str.lower()
    )

    # Products
    datasets["products"]["product_category_name"] = (
        datasets["products"]["product_category_name"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    # Customers
    datasets["customers"]["customer_city"] = (
        datasets["customers"]["customer_city"]
        .str.strip()
        .str.lower()
    )

    datasets["customers"]["customer_state"] = (
        datasets["customers"]["customer_state"]
        .str.strip()
        .str.upper()
    )

    print("=" * 60)
    print("TEXT STANDARDIZATION COMPLETED")
    print("=" * 60)

    return datasets


from src.config.config import CLEANED_DATA_PATH


def save_cleaned_datasets():
    """
    Save all cleaned datasets to the cleaned data folder.

    Returns
    -------
    dict
        Dictionary of cleaned DataFrames.
    """

    datasets = standardize_text()

    CLEANED_DATA_PATH.mkdir(parents=True, exist_ok=True)

    for name, df in datasets.items():

        file_path = CLEANED_DATA_PATH / f"{name}_cleaned.csv"

        df.to_csv(file_path, index=False)

        print(f"Saved: {file_path.name}")

    return datasets