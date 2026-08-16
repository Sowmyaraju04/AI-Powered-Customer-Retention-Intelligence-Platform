"""
Data Loader
-----------
Centralized loading utilities for the Streamlit application.
"""

from pathlib import Path

import pandas as pd


# ============================================================
# PROJECT PATH
# ============================================================

APP_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP_DIR.parent


# ============================================================
# DATA PATH
# ============================================================

AI_READY_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "final"
    / "ai_ready_dataset.csv"
)


# ============================================================
# AI-READY DATA LOADER
# ============================================================

def load_ai_ready_data(
    file_path: Path = AI_READY_DATA_PATH,
) -> pd.DataFrame:
    """
    Load the final AI-ready customer dataset.

    Parameters
    ----------
    file_path : Path
        Location of the AI-ready CSV file.

    Returns
    -------
    pandas.DataFrame
        Customer-level AI-ready dataset.

    Raises
    ------
    FileNotFoundError
        If the dataset does not exist.
    ValueError
        If the loaded dataset is empty.
    """

    file_path = Path(file_path)

    if not file_path.exists():

        raise FileNotFoundError(
            f"AI-ready dataset not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    if df.empty:

        raise ValueError(
            "AI-ready dataset is empty."
        )

    return df


# ============================================================
# DATA VALIDATION
# ============================================================

def validate_ai_ready_data(
    df: pd.DataFrame,
) -> bool:
    """
    Validate the basic structure of the AI-ready dataset.
    """

    required_columns = [
        "customer_unique_id",
        "Frequency",
        "Monetary",
        "average_order_value",
        "average_review_score",
        "preferred_payment_method",
        "Risk_Probability",
        "Risk_Level",
        "Priority",
        "Customer_Value",
        "Recommendation",
        "Campaign_Type",
        "Business_Reason",
        "Expected_Outcome",
        "AI_Insight_Tags",
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    return len(missing_columns) == 0


# ============================================================
# DATA SUMMARY
# ============================================================

def get_data_summary(
    df: pd.DataFrame,
) -> dict:
    """
    Return basic information about the dataset.
    """

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
    }


# ============================================================
# BACKWARD-COMPATIBILITY LOADER
# ============================================================

def load_ai_ready_dataset(file_path=None):
    """
    Load the AI-ready customer dataset.

    Supports both:
        load_ai_ready_dataset()
        load_ai_ready_dataset(custom_path)

    This wrapper maintains compatibility with dashboard code
    while preserving the existing load_ai_ready_data() function.
    """

    if file_path is None:
        return load_ai_ready_data()

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"AI-ready dataset not found: {file_path}"
        )

    return pd.read_csv(file_path)