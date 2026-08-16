
"""
Dashboard
---------
Executive overview of customer churn risk,
customer value, and revenue exposure.
"""

from pathlib import Path
import sys

import pandas as pd
import streamlit as st


# ============================================================
# PROJECT PATH SETUP
# ============================================================

APP_DIR = Path(__file__).resolve().parents[1]

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))


# ============================================================
# CONFIGURATION
# ============================================================

from config.settings import AI_READY_DATA_PATH
from utils.data_loader import load_ai_ready_dataset


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Retention Dashboard",
    page_icon="🎯",
    layout="wide",
)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_dashboard_data():
    """
    Load the validated AI-ready customer dataset
    using the centralized application data loader.
    """
    return load_ai_ready_dataset(
        AI_READY_DATA_PATH
    )


df = load_dashboard_data()


# ============================================================
# DATA FILE VALIDATION
# ============================================================

if df is None:

    st.error(
        "AI-ready dataset could not be loaded."
    )

    st.info(
        f"Expected file location:\n\n"
        f"{AI_READY_DATA_PATH}"
    )

    st.stop()


# ============================================================
# REQUIRED COLUMN VALIDATION
# ============================================================

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


if missing_columns:

    st.error(
        "The AI-ready dataset is missing required columns."
    )

    st.write("Missing columns:")

    for column in missing_columns:
        st.write(f"- {column}")

    st.stop()


# ============================================================
# DATA TYPE STANDARDIZATION
# ============================================================

numeric_columns = [
    "Frequency",
    "Monetary",
    "average_order_value",
    "average_review_score",
    "Risk_Probability",
]


for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce",
    )


# ============================================================
# CUSTOMER VALUE STANDARDIZATION
# ============================================================

df["Customer_Value"] = (
    df["Customer_Value"]
    .astype(str)
    .str.strip()
)


# ============================================================
# REMOVE INVALID RECORDS
# ============================================================

df = df.dropna(
    subset=[
        "customer_unique_id",
        "Risk_Probability",
        "Monetary",
    ]
).copy()


# ============================================================
# REVENUE AT RISK
# ============================================================

df["Revenue_at_Risk"] = (
    df["Monetary"]
    * df["Risk_Probability"]
)


# ============================================================
# APPLICATION HEADER
# ============================================================

st.title(
    "🎯 Customer Retention Dashboard"
)

st.markdown(
    """
    ### Executive Overview

    Monitor customer churn risk, customer value,
    and potential revenue exposure.
    """
)

st.divider()


# ============================================================
# DATASET STATUS
# ============================================================

with st.expander(
    "Dataset Information",
    expanded=False,
):

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Records",
            f"{len(df):,}",
        )

    with col2:

        st.metric(
            "Columns",
            f"{len(df.columns):,}",
        )

    with col3:

        st.success(
            "AI Dataset Loaded"
        )


# ============================================================
# DASHBOARD FILTERS
# ============================================================

st.subheader(
    "Dashboard Filters"
)


filter_col1, filter_col2, filter_col3 = (
    st.columns(3)
)


# ------------------------------------------------------------
# Risk Filter
# ------------------------------------------------------------

with filter_col1:

    risk_options = [
        "All"
    ] + sorted(
        df["Risk_Level"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_risk = st.selectbox(
        "Risk Level",
        risk_options,
    )


# ------------------------------------------------------------
# Customer Value Filter
# ------------------------------------------------------------

with filter_col2:

    value_options = [
        "All"
    ] + sorted(
        df["Customer_Value"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_value = st.selectbox(
        "Customer Value",
        value_options,
    )


# ------------------------------------------------------------
# Priority Filter
# ------------------------------------------------------------

with filter_col3:

    priority_options = [
        "All"
    ] + sorted(
        df["Priority"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_priority = st.selectbox(
        "Priority",
        priority_options,
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_risk != "All":

    filtered_df = filtered_df[
        filtered_df["Risk_Level"]
        .astype(str)
        .eq(selected_risk)
    ]


if selected_value != "All":

    filtered_df = filtered_df[
        filtered_df["Customer_Value"]
        .astype(str)
        .eq(selected_value)
    ]


if selected_priority != "All":

    filtered_df = filtered_df[
        filtered_df["Priority"]
        .astype(str)
        .eq(selected_priority)
    ]


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_customers = len(
    filtered_df
)


at_risk_customers = filtered_df[
    filtered_df["Risk_Level"]
    .astype(str)
    .str.lower()
    .isin(
        [
            "medium",
            "high",
            "critical",
        ]
    )
].shape[0]


high_critical_customers = filtered_df[
    filtered_df["Risk_Level"]
    .astype(str)
    .str.lower()
    .isin(
        [
            "high",
            "critical",
        ]
    )
].shape[0]


revenue_at_risk = (
    filtered_df["Revenue_at_Risk"]
    .sum()
)


total_customer_value = (
    filtered_df["Monetary"]
    .sum()
)


average_churn_probability = (
    filtered_df["Risk_Probability"]
    .mean()
)


average_order_value = (
    filtered_df["average_order_value"]
    .mean()
)


# ============================================================
# EXECUTIVE KPIs
# ============================================================

st.subheader(
    "Executive KPIs"
)


kpi1, kpi2, kpi3, kpi4 = (
    st.columns(4)
)


with kpi1:

    st.metric(
        "Total Customers",
        f"{total_customers:,}",
    )


with kpi2:

    st.metric(
        "At-Risk Customers",
        f"{at_risk_customers:,}",
    )


with kpi3:

    st.metric(
        "High / Critical",
        f"{high_critical_customers:,}",
    )


with kpi4:

    st.metric(
        "Revenue at Risk",
        f"₹ {revenue_at_risk:,.2f}",
    )


# ============================================================
# SECONDARY KPIs
# ============================================================

secondary1, secondary2, secondary3 = (
    st.columns(3)
)


with secondary1:

    st.metric(
        "Customer Value",
        f"₹ {total_customer_value:,.2f}",
    )


with secondary2:

    st.metric(
        "Average Churn Probability",
        f"{average_churn_probability:.2%}",
    )


with secondary3:

    st.metric(
        "Average Order Value",
        f"₹ {average_order_value:,.2f}",
    )


st.divider()


# ============================================================
# RISK DISTRIBUTION
# ============================================================

st.subheader(
    "Customer Risk Distribution"
)


risk_distribution = (
    filtered_df["Risk_Level"]
    .value_counts()
    .reindex(
        [
            "Low",
            "Medium",
            "High",
            "Critical",
        ],
        fill_value=0,
    )
)


chart_col1, chart_col2 = (
    st.columns(2)
)


with chart_col1:

    st.markdown(
        "#### Customers by Risk Level"
    )

    st.bar_chart(
        risk_distribution
    )


with chart_col2:

    st.markdown(
        "#### Risk Distribution (%)"
    )

    total_risk_customers = (
        risk_distribution.sum()
    )

    if total_risk_customers > 0:

        risk_percentage = (
            risk_distribution
            / total_risk_customers
            * 100
        )

    else:

        risk_percentage = (
            risk_distribution
        )

    st.bar_chart(
        risk_percentage
    )


st.divider()


# ============================================================
# REVENUE AT RISK
# ============================================================

st.subheader(
    "Revenue at Risk by Risk Level"
)


revenue_risk = (
    filtered_df
    .groupby("Risk_Level")["Revenue_at_Risk"]
    .sum()
    .reindex(
        [
            "Low",
            "Medium",
            "High",
            "Critical",
        ],
        fill_value=0,
    )
)


st.bar_chart(
    revenue_risk
)


st.divider()


# ============================================================
# CUSTOMER VALUE ANALYSIS
# ============================================================

st.subheader(
    "Customer Value vs Risk"
)


value_risk = (
    filtered_df
    .groupby("Customer_Value")
    .agg(
        Customers=(
            "customer_unique_id",
            "count",
        ),
        Revenue_at_Risk=(
            "Revenue_at_Risk",
            "sum",
        ),
        Average_Risk=(
            "Risk_Probability",
            "mean",
        ),
    )
    .reset_index()
)


st.dataframe(
    value_risk,
    width="stretch",
    hide_index=True,
)


st.divider()


# ============================================================
# HIGH-PRIORITY CUSTOMERS
# ============================================================

st.subheader(
    "High-Priority Customers"
)


priority_customers = (
    filtered_df[
        filtered_df["Risk_Level"]
        .astype(str)
        .str.lower()
        .isin(
            [
                "high",
                "critical",
            ]
        )
    ]
    .sort_values(
        "Revenue_at_Risk",
        ascending=False,
    )
)


display_columns = [
    "customer_unique_id",
    "Risk_Probability",
    "Risk_Level",
    "Priority",
    "Customer_Value",
    "Monetary",
    "Revenue_at_Risk",
    "Recommendation",
]


priority_display = (
    priority_customers[
        display_columns
    ]
    .head(20)
    .copy()
)


priority_display[
    "Risk_Probability"
] = (
    priority_display[
        "Risk_Probability"
    ].round(4)
)


priority_display[
    "Revenue_at_Risk"
] = (
    priority_display[
        "Revenue_at_Risk"
    ].round(2)
)


st.dataframe(
    priority_display,
    width="stretch",
    hide_index=True,
)


# ============================================================
# KEY BUSINESS INSIGHTS
# ============================================================

st.divider()

st.subheader(
    "Key Business Insights"
)


# ============================================================
# INSIGHT CALCULATIONS
# ============================================================

if total_customers > 0:

    at_risk_percentage = (
        at_risk_customers
        / total_customers
        * 100
    )

else:

    at_risk_percentage = 0


high_critical_revenue = (
    filtered_df[
        filtered_df["Risk_Level"]
        .astype(str)
        .str.lower()
        .isin(
            [
                "high",
                "critical",
            ]
        )
    ]["Revenue_at_Risk"]
    .sum()
)


high_value_at_risk = filtered_df[
    (
        filtered_df["Customer_Value"]
        .astype(str)
        .str.lower()
        .isin(
            [
                "high",
                "high value",
                "high-value",
            ]
        )
    )
    &
    (
        filtered_df["Risk_Level"]
        .astype(str)
        .str.lower()
        .isin(
            [
                "high",
                "critical",
            ]
        )
    )
].shape[0]


# ============================================================
# INSIGHT COLUMNS
# ============================================================

insight1, insight2, insight3 = (
    st.columns(3)
)


# ============================================================
# CUSTOMER RISK INSIGHT
# ============================================================

with insight1:

    st.info(
        "⚠️ Customer Risk"
    )

    st.metric(
        "At-Risk Customers",
        f"{at_risk_customers:,}",
    )

    st.write(
        f"{at_risk_percentage:.1f}% of the "
        "selected customer population is "
        "classified as medium, high, or "
        "critical risk."
    )

    st.markdown(
        "**Business Insight:** "
        "The customer base requires proactive "
        "retention monitoring rather than "
        "reactive churn management."
    )


# ============================================================
# REVENUE EXPOSURE INSIGHT
# ============================================================

with insight2:

    st.warning(
        "💰 Revenue Exposure"
    )

    st.metric(
        "Revenue at Risk",
        f"₹ {revenue_at_risk:,.2f}",
    )

    st.write(
        "High and critical-risk customers "
        "account for approximately "
        f"₹ {high_critical_revenue:,.2f} "
        "in risk-weighted revenue exposure."
    )

    st.markdown(
        "**Business Insight:** "
        "Retention campaigns should focus "
        "first on customers with the greatest "
        "revenue exposure."
    )


# ============================================================
# RETENTION STRATEGY INSIGHT
# ============================================================

with insight3:

    st.success(
        "🎯 Retention Strategy"
    )

    st.metric(
        "High-Value At-Risk Customers",
        f"{high_value_at_risk:,}",
    )

    st.write(
        "These customers represent the "
        "strongest opportunity for targeted "
        "retention intervention."
    )

    st.markdown(
        "**Business Insight:** "
        "Prioritize personalized offers, "
        "loyalty incentives, and proactive "
        "engagement."
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()


st.caption(
    "AI-Powered Customer Retention Intelligence Platform"
)


st.caption(
    f"Dashboard powered by {len(df):,} customer records."
)

