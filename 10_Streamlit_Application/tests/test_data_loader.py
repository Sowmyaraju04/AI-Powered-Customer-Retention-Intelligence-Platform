import sys
from pathlib import Path

import pandas as pd


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

STREAMLIT_APP = (
    PROJECT_ROOT / "10_Streamlit_Application"
)

if str(STREAMLIT_APP) not in sys.path:
    sys.path.insert(0, str(STREAMLIT_APP))


from config.settings import AI_READY_DATA_PATH
from utils.data_loader import load_ai_ready_data


# ============================================================
# TEST AI DATASET EXISTS
# ============================================================

def test_ai_ready_dataset_exists():

    assert AI_READY_DATA_PATH.exists(), (
        f"AI-ready dataset not found: "
        f"{AI_READY_DATA_PATH}"
    )


# ============================================================
# TEST DATA LOADING
# ============================================================

def test_ai_ready_data_loading():

    df = load_ai_ready_data()

    assert isinstance(
        df,
        pd.DataFrame
    )

    assert not df.empty


# ============================================================
# TEST EXPECTED COLUMNS
# ============================================================

def test_ai_ready_required_columns():

    df = load_ai_ready_data()

    required_columns = [
        "customer_unique_id",
        "Frequency",
        "Monetary",
        "average_order_value",
        "average_review_score",
        "Risk_Probability",
        "Risk_Level",
        "Priority",
        "Customer_Value",
        "Recommendation",
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    assert not missing_columns, (
        f"Missing required columns: "
        f"{missing_columns}"
    )


# ============================================================
# TEST CUSTOMER RECORD COUNT
# ============================================================

def test_customer_record_count():

    df = load_ai_ready_data()

    assert len(df) > 0