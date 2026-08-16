"""
Recommendation Engine
---------------------
Rule-based customer retention recommendation engine.

This module converts customer risk and behavioral attributes
into actionable retention strategies.

Business logic is aligned with:
08_Retention_Recommendation/Recommendation_Logic.md
"""

from __future__ import annotations

from typing import Dict

import pandas as pd


# ============================================================
# REQUIRED INPUT COLUMNS
# ============================================================

REQUIRED_COLUMNS = [
    "Risk_Level",
    "Customer_Value",
    "average_review_score",
    "Frequency",
]


# ============================================================
# RISK NORMALIZATION
# ============================================================

def normalize_risk_level(value) -> str:
    """
    Normalize customer risk level.

    Parameters
    ----------
    value : Any
        Risk level value.

    Returns
    -------
    str
        Low / Medium / High / Critical / Unknown
    """

    value = str(value).strip().lower()

    if "critical" in value:
        return "Critical"

    if "high" in value:
        return "High"

    if "medium" in value:
        return "Medium"

    if "low" in value:
        return "Low"

    return "Unknown"


# ============================================================
# CUSTOMER VALUE NORMALIZATION
# ============================================================

def normalize_customer_value(value) -> str:
    """
    Normalize customer value segment.
    """

    if pd.isna(value):
        return "Unknown"

    value = str(value).strip().lower()

    if "high" in value:
        return "High"

    if "medium" in value:
        return "Medium"

    if "low" in value:
        return "Low"

    if "vip" in value:
        return "VIP"

    return str(value).title()


# ============================================================
# SAFE NUMERIC CONVERSION
# ============================================================

def safe_float(value, default: float = 0.0) -> float:
    """
    Safely convert a value to float.
    """

    try:
        if pd.isna(value):
            return default

        return float(value)

    except (TypeError, ValueError):
        return default


# ============================================================
# SINGLE CUSTOMER RECOMMENDATION
# ============================================================

def generate_recommendation(
    risk_level,
    customer_value,
    average_review_score,
    frequency,
) -> Dict[str, str]:
    """
    Generate a retention recommendation for one customer.

    Parameters
    ----------
    risk_level : str
        Customer churn risk level.

    customer_value : str
        Customer value segment.

    average_review_score : float
        Average customer review score.

    frequency : float
        Customer purchase frequency.

    Returns
    -------
    dict
        Recommendation business outputs.
    """

    risk = normalize_risk_level(risk_level)

    value = normalize_customer_value(customer_value)

    review_score = safe_float(
        average_review_score
    )

    purchase_frequency = safe_float(
        frequency
    )

    # ========================================================
    # CRITICAL RISK
    # ========================================================

    if risk == "Critical":

        if value in {"VIP", "High"}:

            return {
                "Recommendation": "VIP Service Recovery",
                "Campaign_Type": "Priority Customer Recovery",
                "Business_Reason": (
                    "High-value customer has critical churn risk."
                ),
                "Expected_Outcome": (
                    "Protect high-value revenue and prevent customer loss."
                ),
            }

        if review_score < 3:

            return {
                "Recommendation": "Customer Support Follow-Up",
                "Campaign_Type": "Service Recovery",
                "Business_Reason": (
                    "Critical-risk customer shows signs of "
                    "customer dissatisfaction."
                ),
                "Expected_Outcome": (
                    "Resolve customer concerns and reduce churn probability."
                ),
            }

        return {
            "Recommendation": "Personalized Discount",
            "Campaign_Type": "Win-Back Campaign",
            "Business_Reason": (
                "Customer has critical churn risk and requires "
                "an immediate retention intervention."
            ),
            "Expected_Outcome": (
                "Re-engage the customer and encourage another purchase."
            ),
        }

    # ========================================================
    # HIGH RISK
    # ========================================================

    if risk == "High":

        if value in {"VIP", "High"}:

            return {
                "Recommendation": "Exclusive Loyalty Offer",
                "Campaign_Type": "VIP Loyalty Campaign",
                "Business_Reason": (
                    "High-value customer has elevated churn risk."
                ),
                "Expected_Outcome": (
                    "Increase loyalty and protect future customer value."
                ),
            }

        if review_score < 3:

            return {
                "Recommendation": "Customer Support Follow-Up",
                "Campaign_Type": "Customer Recovery Campaign",
                "Business_Reason": (
                    "High-risk customer has a low review score."
                ),
                "Expected_Outcome": (
                    "Improve customer satisfaction and reduce churn risk."
                ),
            }

        if purchase_frequency <= 1:

            return {
                "Recommendation": "Re-engagement Email",
                "Campaign_Type": "Re-engagement Campaign",
                "Business_Reason": (
                    "High-risk customer has limited purchase frequency."
                ),
                "Expected_Outcome": (
                    "Encourage repeat purchasing and restore engagement."
                ),
            }

        return {
            "Recommendation": "Personalized Promotion",
            "Campaign_Type": "Targeted Promotion",
            "Business_Reason": (
                "Customer shows elevated churn risk and requires "
                "targeted engagement."
            ),
            "Expected_Outcome": (
                "Increase engagement and encourage another purchase."
            ),
        }

    # ========================================================
    # MEDIUM RISK
    # ========================================================

    if risk == "Medium":

        if value in {"VIP", "High"}:

            return {
                "Recommendation": "VIP Appreciation",
                "Campaign_Type": "Loyalty Campaign",
                "Business_Reason": (
                    "High-value customer shows moderate churn risk."
                ),
                "Expected_Outcome": (
                    "Strengthen loyalty and maintain customer engagement."
                ),
            }

        if purchase_frequency <= 1:

            return {
                "Recommendation": "Re-engagement Email",
                "Campaign_Type": "Re-engagement Campaign",
                "Business_Reason": (
                    "Moderate-risk customer has limited purchase activity."
                ),
                "Expected_Outcome": (
                    "Encourage the customer to return and purchase again."
                ),
            }

        return {
            "Recommendation": "Loyalty Reward",
            "Campaign_Type": "Customer Loyalty Campaign",
            "Business_Reason": (
                "Customer has moderate churn risk and can be "
                "retained through loyalty incentives."
            ),
            "Expected_Outcome": (
                "Increase repeat purchases and strengthen loyalty."
            ),
        }

    # ========================================================
    # LOW RISK
    # ========================================================

    if risk == "Low":

        if value in {"VIP", "High"}:

            return {
                "Recommendation": "VIP Appreciation",
                "Campaign_Type": "VIP Loyalty Campaign",
                "Business_Reason": (
                    "High-value customer currently has low churn risk."
                ),
                "Expected_Outcome": (
                    "Maintain loyalty and maximize long-term customer value."
                ),
            }

        if purchase_frequency >= 3:

            return {
                "Recommendation": "Cross-Sell Recommendation",
                "Campaign_Type": "Cross-Sell Campaign",
                "Business_Reason": (
                    "Frequent customer presents an opportunity "
                    "for additional product engagement."
                ),
                "Expected_Outcome": (
                    "Increase customer lifetime value through cross-selling."
                ),
            }

        return {
            "Recommendation": "Personalized Promotion",
            "Campaign_Type": "Engagement Campaign",
            "Business_Reason": (
                "Customer is currently low risk and suitable "
                "for continued engagement."
            ),
            "Expected_Outcome": (
                "Maintain engagement and encourage future purchases."
            ),
        }

    # ========================================================
    # UNKNOWN / FALLBACK
    # ========================================================

    return {
        "Recommendation": "Personalized Promotion",
        "Campaign_Type": "General Engagement Campaign",
        "Business_Reason": (
            "Customer risk information is insufficient for "
            "a more specific intervention."
        ),
        "Expected_Outcome": (
            "Maintain customer engagement while additional "
            "behavioral information becomes available."
        ),
    }


# ============================================================
# DATAFRAME RECOMMENDATIONS
# ============================================================

def generate_recommendations(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Generate retention recommendations for every customer
    in a DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Customer-level dataset.

    Returns
    -------
    pandas.DataFrame
        Original dataset with recommendation fields added.
    """

    if not isinstance(df, pd.DataFrame):

        raise TypeError(
            "df must be a pandas DataFrame."
        )

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:

        raise ValueError(
            "Missing required columns: "
            f"{missing_columns}"
        )

    result = df.copy()

    recommendations = result.apply(
        lambda row: generate_recommendation(
            risk_level=row["Risk_Level"],
            customer_value=row["Customer_Value"],
            average_review_score=row[
                "average_review_score"
            ],
            frequency=row["Frequency"],
        ),
        axis=1,
    )

    recommendation_df = pd.DataFrame(
        recommendations.tolist(),
        index=result.index,
    )

    result[
        [
            "Recommendation",
            "Campaign_Type",
            "Business_Reason",
            "Expected_Outcome",
        ]
    ] = recommendation_df[
        [
            "Recommendation",
            "Campaign_Type",
            "Business_Reason",
            "Expected_Outcome",
        ]
    ]

    return result