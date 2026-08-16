"""
Data Loader Module

Project:
AI-Powered Customer Retention Intelligence Platform

Purpose:
Load all raw datasets.
"""

import pandas as pd

from src.config.config import RAW_DATA_PATH


def load_all_data():
    """
    Loads all raw Olist datasets.

    Returns
    -------
    dict
        Dictionary of pandas DataFrames.
    """

    datasets = {
        "customers": pd.read_csv(RAW_DATA_PATH / "olist_customers_dataset.csv"),
        "orders": pd.read_csv(RAW_DATA_PATH / "olist_orders_dataset.csv"),
        "order_items": pd.read_csv(RAW_DATA_PATH / "olist_order_items_dataset.csv"),
        "payments": pd.read_csv(RAW_DATA_PATH / "olist_order_payments_dataset.csv"),
        "products": pd.read_csv(RAW_DATA_PATH / "olist_products_dataset.csv"),
        "reviews": pd.read_csv(RAW_DATA_PATH / "olist_order_reviews_dataset.csv"),
        "sellers": pd.read_csv(RAW_DATA_PATH / "olist_sellers_dataset.csv"),
        "geolocation": pd.read_csv(RAW_DATA_PATH / "olist_geolocation_dataset.csv"),
        "translation": pd.read_csv(
            RAW_DATA_PATH / "product_category_name_translation.csv"
        ),
    }

    return datasets