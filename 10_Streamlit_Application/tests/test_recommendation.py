import sys
from pathlib import Path

import pandas as pd
import pytest


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

STREAMLIT_APP = (
    PROJECT_ROOT
    / "10_Streamlit_Application"
)

if str(STREAMLIT_APP) not in sys.path:
    sys.path.insert(
        0,
        str(STREAMLIT_APP)
    )


from utils.recommendation import (
    generate_recommendation,
    generate_recommendations,
    normalize_risk_level,
)


# ============================================================
# TEST RISK NORMALIZATION
# ============================================================

def test_risk_normalization():

    assert normalize_risk_level(
        "critical"
    ) == "Critical"

    assert normalize_risk_level(
        "HIGH"
    ) == "High"

    assert normalize_risk_level(
        "Medium"
    ) == "Medium"

    assert normalize_risk_level(
        "low"
    ) == "Low"


# ============================================================
# TEST CRITICAL CUSTOMER
# ============================================================

def test_critical_customer_recommendation():

    result = generate_recommendation(
        risk_level="Critical",
        customer_value="High",
        average_review_score=4.0,
        frequency=3,
    )

    assert isinstance(
        result,
        dict
    )

    assert result["Recommendation"] == (
        "VIP Service Recovery"
    )

    assert result["Campaign_Type"] == (
        "Priority Customer Recovery"
    )


# ============================================================
# TEST HIGH RISK
# ============================================================

def test_high_risk_recommendation():

    result = generate_recommendation(
        risk_level="High",
        customer_value="Medium",
        average_review_score=4.0,
        frequency=1,
    )

    assert result["Recommendation"] == (
        "Re-engagement Email"
    )


# ============================================================
# TEST LOW REVIEW SCORE
# ============================================================

def test_low_review_recommendation():

    result = generate_recommendation(
        risk_level="High",
        customer_value="Medium",
        average_review_score=2.0,
        frequency=3,
    )

    assert result["Recommendation"] == (
        "Customer Support Follow-Up"
    )


# ============================================================
# TEST LOW RISK FREQUENT CUSTOMER
# ============================================================

def test_low_risk_frequent_customer():

    result = generate_recommendation(
        risk_level="Low",
        customer_value="Medium",
        average_review_score=4.5,
        frequency=4,
    )

    assert result["Recommendation"] == (
        "Cross-Sell Recommendation"
    )


# ============================================================
# TEST DATAFRAME RECOMMENDATIONS
# ============================================================

def test_generate_recommendations():

    df = pd.DataFrame(
        {
            "customer_unique_id": [
                "customer_001",
                "customer_002",
                "customer_003",
            ],
            "Risk_Level": [
                "Critical",
                "High",
                "Low",
            ],
            "Customer_Value": [
                "High",
                "Medium",
                "Medium",
            ],
            "average_review_score": [
                4.0,
                2.0,
                4.5,
            ],
            "Frequency": [
                3,
                2,
                4,
            ],
        }
    )

    result = generate_recommendations(
        df
    )

    assert isinstance(
        result,
        pd.DataFrame
    )

    assert len(result) == 3

    required_outputs = [
        "Recommendation",
        "Campaign_Type",
        "Business_Reason",
        "Expected_Outcome",
    ]

    for column in required_outputs:

        assert column in result.columns

        assert (
            result[column]
            .notna()
            .all()
        )


# ============================================================
# TEST MISSING COLUMNS
# ============================================================

def test_missing_required_columns():

    df = pd.DataFrame(
        {
            "Risk_Level": ["High"],
        }
    )

    with pytest.raises(
        ValueError
    ):

        generate_recommendations(
            df
        )


# ============================================================
# TEST INVALID INPUT TYPE
# ============================================================

def test_invalid_dataframe_input():

    with pytest.raises(
        TypeError
    ):

        generate_recommendations(
            ["invalid"]
        )