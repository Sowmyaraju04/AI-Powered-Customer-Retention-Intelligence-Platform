"""
EDA Data Loader

Project:
AI-Powered Customer Retention Intelligence Platform

Purpose:
Load cleaned datasets for Exploratory Data Analysis.
"""

import pandas as pd

from src.config.config import CLEANED_DATA_PATH


def load_cleaned_data():
    """
    Load all cleaned datasets.

    Returns
    -------
    dict
        Dictionary containing cleaned pandas DataFrames.
    """

    datasets = {
        "customers": pd.read_csv(
            CLEANED_DATA_PATH / "customers_cleaned.csv"
        ),

        "orders": pd.read_csv(
            CLEANED_DATA_PATH / "orders_cleaned.csv"
        ),

        "order_items": pd.read_csv(
            CLEANED_DATA_PATH / "order_items_cleaned.csv"
        ),

        "payments": pd.read_csv(
            CLEANED_DATA_PATH / "payments_cleaned.csv"
        ),

        "products": pd.read_csv(
            CLEANED_DATA_PATH / "products_cleaned.csv"
        ),

        "reviews": pd.read_csv(
            CLEANED_DATA_PATH / "reviews_cleaned.csv"
        ),

        "sellers": pd.read_csv(
            CLEANED_DATA_PATH / "sellers_cleaned.csv"
        ),

        "geolocation": pd.read_csv(
            CLEANED_DATA_PATH / "geolocation_cleaned.csv"
        ),

        "translation": pd.read_csv(
            CLEANED_DATA_PATH / "translation_cleaned.csv"
        ),
    }

    return datasets