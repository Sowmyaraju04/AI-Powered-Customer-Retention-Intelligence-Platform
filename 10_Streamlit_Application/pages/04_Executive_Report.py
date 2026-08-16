"""
Executive Report
----------------
Management-ready summary of customer retention risk,
revenue exposure, churn drivers, and recommended actions.
"""

import sys
from pathlib import Path

import pandas as pd
import streamlit as st


# ============================================================
# PROJECT PATH SETUP
# ============================================================

APP_DIR = Path(__file__).resolve().parents[1]

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))


# ============================================================
# APPLICATION IMPORTS
# ============================================================

from config.settings import AI_READY_DATA_PATH


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Executive Retention Report",
    page_icon="📊",
    layout="wide",
)


# ============================================================
# DATA LOADING
# ============================================================

@st.cache_data
def load_data():

    if not AI_READY_DATA_PATH.exists():
        return None

    return pd.read_csv(AI_READY_DATA_PATH)


df = load_data()


# ============================================================
# DATA VALIDATION
# ============================================================

if df is None:

    st.error(
        "AI-ready dataset could not be found."
    )

    st.info(
        f"Expected file location:\n\n"
        f"{AI_READY_DATA_PATH}"
    )

    st.stop()


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


if missing_columns:

    st.error(
        "Required columns are missing from the AI-ready dataset."
    )

    st.write(
        "Missing columns:"
    )

    for column in missing_columns:

        st.write(
            f"- {column}"
        )

    st.stop()


# ============================================================
# DATA PREPARATION
# ============================================================

df = df.copy()


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


df["Risk_Probability"] = (
    df["Risk_Probability"]
    .clip(
        lower=0,
        upper=1,
    )
)


text_columns = [
    "Risk_Level",
    "Priority",
    "Customer_Value",
    "Recommendation",
    "Campaign_Type",
    "Business_Reason",
    "Expected_Outcome",
    "AI_Insight_Tags",
]


for column in text_columns:

    df[column] = (
        df[column]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
    )


# ============================================================
# RISK STANDARDIZATION
# ============================================================

def normalize_risk(value):

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


df["Risk_Level_Display"] = (
    df["Risk_Level"]
    .apply(normalize_risk)
)


# ============================================================
# REVENUE AT RISK
# ============================================================

df["Revenue_at_Risk"] = (
    df["Monetary"]
    * df["Risk_Probability"]
)


# ============================================================
# HEADER
# ============================================================

st.title(
    "📊 Executive Retention Report"
)

st.markdown(
    """
    ### Management Summary

    This report summarizes customer churn exposure,
    revenue at risk, major retention drivers, and
    recommended business actions.
    """
)

st.divider()


# ============================================================
# EXECUTIVE KPI CALCULATIONS
# ============================================================

total_customers = len(df)


at_risk_df = df[
    df["Risk_Level_Display"].isin(
        [
            "Medium",
            "High",
            "Critical",
        ]
    )
]


high_critical_df = df[
    df["Risk_Level_Display"].isin(
        [
            "High",
            "Critical",
        ]
    )
]


at_risk_customers = len(
    at_risk_df
)


high_critical_customers = len(
    high_critical_df
)


at_risk_percentage = (
    at_risk_customers
    / total_customers
    if total_customers > 0
    else 0
)


high_critical_percentage = (
    high_critical_customers
    / total_customers
    if total_customers > 0
    else 0
)


total_revenue = (
    df["Monetary"]
    .sum()
)


revenue_at_risk = (
    df["Revenue_at_Risk"]
    .sum()
)


high_critical_revenue = (
    high_critical_df["Monetary"]
    .sum()
)


average_risk = (
    df["Risk_Probability"]
    .mean()
)


# ============================================================
# EXECUTIVE KPIs
# ============================================================

st.subheader(
    "Executive KPIs"
)


kpi1, kpi2, kpi3, kpi4 = st.columns(4)


with kpi1:

    st.metric(
        "Total Customers",
        f"{total_customers:,}",
    )


with kpi2:

    st.metric(
        "Customers at Risk",
        f"{at_risk_customers:,}",
        f"{at_risk_percentage:.1%} of customers",
    )


with kpi3:

    st.metric(
        "High / Critical",
        f"{high_critical_customers:,}",
        f"{high_critical_percentage:.1%} of customers",
    )


with kpi4:

    st.metric(
        "Revenue at Risk",
        f"₹ {revenue_at_risk:,.2f}",
    )


st.divider()


# ============================================================
# EXECUTIVE SUMMARY
# ============================================================

st.subheader(
    "Executive Summary"
)


if high_critical_percentage >= 0.50:

    severity = "very high"

elif high_critical_percentage >= 0.25:

    severity = "high"

elif high_critical_percentage >= 0.10:

    severity = "moderate"

else:

    severity = "relatively contained"


summary_text = f"""
The customer portfolio contains **{total_customers:,} customers**,
of which **{at_risk_customers:,} ({at_risk_percentage:.1%})**
are classified as Medium, High, or Critical risk.

There are **{high_critical_customers:,} High or Critical-risk
customers**, representing **{high_critical_percentage:.1%}**
of the customer base.

The estimated revenue exposure associated with predicted churn
risk is **₹ {revenue_at_risk:,.2f}**.

Overall, the portfolio shows a **{severity} level of high-risk
customer exposure**. Retention efforts should prioritize customers
where churn probability and monetary customer value are both high.
"""


st.info(
    summary_text
)


# ============================================================
# REVENUE EXPOSURE
# ============================================================

st.subheader(
    "Revenue Exposure"
)


revenue_col1, revenue_col2, revenue_col3 = (
    st.columns(3)
)


with revenue_col1:

    st.metric(
        "Total Customer Value",
        f"₹ {total_revenue:,.2f}",
    )


with revenue_col2:

    st.metric(
        "Estimated Revenue at Risk",
        f"₹ {revenue_at_risk:,.2f}",
    )


with revenue_col3:

    st.metric(
        "High / Critical Customer Value",
        f"₹ {high_critical_revenue:,.2f}",
    )


st.divider()


# ============================================================
# RISK DISTRIBUTION
# ============================================================

st.subheader(
    "Customer Risk Distribution"
)


risk_order = [
    "Low",
    "Medium",
    "High",
    "Critical",
]


risk_distribution = (
    df["Risk_Level_Display"]
    .value_counts()
    .reindex(
        risk_order,
        fill_value=0,
    )
)


risk_report = pd.DataFrame(
    {
        "Risk Level": risk_distribution.index,
        "Customers": risk_distribution.values,
    }
)


risk_report["Share (%)"] = (
    risk_report["Customers"]
    / total_customers
    * 100
)


st.dataframe(
    risk_report.style.format(
        {
            "Share (%)": "{:.2f}",
        }
    ),
    width="stretch",
    hide_index=True,
)


st.divider()


# ============================================================
# TOP BUSINESS REASONS
# ============================================================

st.subheader(
    "Top Customer Risk Drivers"
)


reason_data = (
    high_critical_df[
        "Business_Reason"
    ]
    .value_counts()
    .head(10)
    .reset_index()
)


reason_data.columns = [
    "Business Reason",
    "Customers",
]


if not reason_data.empty:

    st.dataframe(
        reason_data,
        width="stretch",
        hide_index=True,
    )

else:

    st.info(
        "No business reason data is available."
    )


st.divider()


# ============================================================
# RETENTION CAMPAIGN STRATEGY
# ============================================================

st.subheader(
    "Recommended Retention Campaigns"
)


campaign_data = (
    high_critical_df[
        "Campaign_Type"
    ]
    .value_counts()
    .reset_index()
)


campaign_data.columns = [
    "Campaign Type",
    "Customers",
]


if not campaign_data.empty:

    st.dataframe(
        campaign_data,
        width="stretch",
        hide_index=True,
    )

else:

    st.info(
        "No campaign recommendations are available."
    )


st.divider()


# ============================================================
# HIGH-VALUE HIGH-RISK CUSTOMERS
# ============================================================

st.subheader(
    "Priority Retention Customers"
)


priority_customers = (
    high_critical_df
    .sort_values(
        [
            "Revenue_at_Risk",
            "Risk_Probability",
        ],
        ascending=False,
    )
)


priority_columns = [
    "customer_unique_id",
    "Risk_Probability",
    "Risk_Level_Display",
    "Priority",
    "Customer_Value",
    "Monetary",
    "Revenue_at_Risk",
    "Recommendation",
]


priority_display = (
    priority_customers[
        priority_columns
    ]
    .head(20)
    .copy()
)


priority_display = (
    priority_display.rename(
        columns={
            "Risk_Level_Display": "Risk Level",
            "Risk_Probability": "Risk Probability",
        }
    )
)


priority_display[
    "Risk Probability"
] = (
    priority_display[
        "Risk Probability"
    ].round(4)
)


priority_display[
    "Monetary"
] = (
    priority_display[
        "Monetary"
    ].round(2)
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


st.divider()


# ============================================================
# BUSINESS ACTION PLAN
# ============================================================

st.subheader(
    "Recommended Business Action Plan"
)


action_col1, action_col2, action_col3 = st.columns(3)


with action_col1:

    st.error(
        """
        ### 🔴 Immediate Action

        Focus on **High and Critical-risk customers**.

        Prioritize customers with:

        - High churn probability
        - High monetary value
        - Critical retention priority
        """
    )


with action_col2:

    st.warning(
        """
        ### 🟠 Targeted Retention

        Use personalized campaigns based on:

        - Customer value
        - Risk level
        - Business reason
        - Recommended campaign type
        """
    )


with action_col3:

    st.success(
        """
        ### 🟢 Continuous Engagement

        Maintain engagement with Low and Medium-risk
        customers to prevent future movement into
        higher-risk segments.
        """
    )


st.divider()


# ============================================================
# EXPECTED BUSINESS OUTCOMES
# ============================================================

st.subheader(
    "Expected Business Outcomes"
)


outcome_data = (
    high_critical_df[
        "Expected_Outcome"
    ]
    .value_counts()
    .head(10)
    .reset_index()
)


outcome_data.columns = [
    "Expected Outcome",
    "Customers",
]


if not outcome_data.empty:

    st.dataframe(
        outcome_data,
        width="stretch",
        hide_index=True,
    )

else:

    st.info(
        "Expected outcome information is not available."
    )


st.divider()


# ============================================================
# MANAGEMENT RECOMMENDATION
# ============================================================

st.subheader(
    "Management Recommendation"
)


recommendation_text = f"""
### Retention Priority

The business should immediately focus retention resources on the
**{high_critical_customers:,} High/Critical-risk customers**.

These customers represent approximately
**₹ {high_critical_revenue:,.2f} in customer monetary value**.

The most effective strategy is not to contact every at-risk customer
with the same campaign. Instead, retention actions should be
**risk-based, value-based, and reason-based**.

Customers with high monetary value and high churn probability should
receive the strongest intervention, while lower-value customers can
be managed through automated or lower-cost campaigns.

This approach helps the business allocate retention resources where
they have the highest potential financial impact.
"""


st.info(
    recommendation_text
)


# ============================================================
# DOWNLOAD REPORT DATA
# ============================================================

st.subheader(
    "Download Executive Report Data"
)


report_columns = [
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
    "Campaign_Type",
    "Business_Reason",
    "Expected_Outcome",
    "AI_Insight_Tags",
    "Revenue_at_Risk",
]


report_data = df[
    report_columns
].copy()


csv_data = (
    report_data
    .to_csv(index=False)
    .encode("utf-8")
)


st.download_button(
    label="⬇️ Download Executive Report CSV",
    data=csv_data,
    file_name="executive_retention_report.csv",
    mime="text/csv",
    width="stretch",
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI-Powered Customer Retention Intelligence Platform"
)

st.caption(
    f"Executive report generated from {len(df):,} customer records."
)
