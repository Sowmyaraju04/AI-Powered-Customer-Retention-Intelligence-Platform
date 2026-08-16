import pandas as pd
import streamlit as st


def display_risk_distribution(data: pd.DataFrame):
    """
    Display customer distribution across risk levels.
    """

    risk_counts = (
        data["Risk_Level"]
        .value_counts()
        .reindex(
            ["Low", "Medium", "High", "Critical"],
            fill_value=0,
        )
    )

    st.bar_chart(risk_counts)


def display_revenue_at_risk(data: pd.DataFrame):
    """
    Display estimated revenue exposure by risk level.

    Revenue at risk is calculated as:

        Monetary × Risk Probability

    This represents a probability-weighted revenue exposure
    rather than guaranteed future revenue loss.
    """

    revenue_risk = (
        data.groupby("Risk_Level")["Estimated_Revenue_At_Risk"]
        .sum()
        .reindex(
            ["Low", "Medium", "High", "Critical"],
            fill_value=0,
        )
    )

    st.bar_chart(revenue_risk)


def display_customer_value_profile(data: pd.DataFrame):
    """
    Display customer distribution by customer value segment.
    """

    value_counts = data["Customer_Value"].value_counts()

    st.bar_chart(value_counts)