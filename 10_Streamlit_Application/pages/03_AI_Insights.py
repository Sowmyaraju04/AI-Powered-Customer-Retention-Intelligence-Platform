"""
AI Insights
-----------
Explainable AI view of customer churn risk,
business drivers, and recommended retention actions.
"""

from pathlib import Path
import sys

import pandas as pd
import plotly.express as px
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

from config.settings import AI_CUSTOMER_EXPLANATIONS_PATH


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Retention Intelligence",
    page_icon="🤖",
    layout="wide",
)


# ============================================================
# REQUIRED COLUMNS
# ============================================================

REQUIRED_COLUMNS = [
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
    "AI_Customer_Explanation",
]


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_ai_explanation_data():

    if not AI_CUSTOMER_EXPLANATIONS_PATH.exists():
        return None

    return pd.read_csv(
        AI_CUSTOMER_EXPLANATIONS_PATH
    )


df = load_ai_explanation_data()


# ============================================================
# DATASET VALIDATION
# ============================================================

if df is None:

    st.error(
        "AI customer explanation dataset could not be found."
    )

    st.info(
        f"Expected file:\n\n"
        f"{AI_CUSTOMER_EXPLANATIONS_PATH}"
    )

    st.stop()


missing_columns = [
    column
    for column in REQUIRED_COLUMNS
    if column not in df.columns
]


if missing_columns:

    st.error(
        "The AI explanation dataset is missing required columns."
    )

    st.write("Missing columns:")

    for column in missing_columns:
        st.write(f"- {column}")

    st.stop()


# ============================================================
# DATA PREPARATION
# ============================================================

df = df.copy()


# ------------------------------------------------------------
# Numeric columns
# ------------------------------------------------------------

NUMERIC_COLUMNS = [
    "Frequency",
    "Monetary",
    "average_order_value",
    "average_review_score",
    "Risk_Probability",
]


for column in NUMERIC_COLUMNS:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce",
    )


# ------------------------------------------------------------
# Risk probability validation
# ------------------------------------------------------------

df["Risk_Probability"] = (
    df["Risk_Probability"]
    .clip(
        lower=0,
        upper=1,
    )
)


# ------------------------------------------------------------
# Text columns
# ------------------------------------------------------------

TEXT_COLUMNS = [
    "Risk_Level",
    "Priority",
    "Customer_Value",
    "Recommendation",
    "Campaign_Type",
    "Business_Reason",
    "Expected_Outcome",
    "AI_Insight_Tags",
    "AI_Customer_Explanation",
]


for column in TEXT_COLUMNS:

    df[column] = (
        df[column]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
    )


# ============================================================
# NORMALIZE RISK LEVEL
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
# REMOVE INVALID CORE RECORDS
# ============================================================

df = df.dropna(
    subset=[
        "customer_unique_id",
        "Risk_Probability",
        "Monetary",
    ]
)


if df.empty:

    st.error(
        "No valid customer records are available."
    )

    st.stop()


# ============================================================
# PAGE HEADER
# ============================================================

st.title(
    "🤖 AI Retention Intelligence"
)

st.markdown(
    """
    ### Explainable Customer Risk & Retention Intelligence

    Understand **why customers are at risk**, identify the
    strongest risk drivers, and determine **what retention
    action should be taken next**.
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

    info_col1, info_col2, info_col3 = st.columns(3)

    with info_col1:

        st.metric(
            "Customers",
            f"{len(df):,}",
        )

    with info_col2:

        st.metric(
            "Features",
            f"{len(df.columns):,}",
        )

    with info_col3:

        st.success(
            "AI Explanation Dataset Loaded"
        )


# ============================================================
# FILTERS
# ============================================================

st.subheader(
    "🎛️ Insight Filters"
)


filter_col1, filter_col2, filter_col3 = (
    st.columns(3)
)


# ------------------------------------------------------------
# Risk filter
# ------------------------------------------------------------

with filter_col1:

    risk_options = [
        "All",
        "Low",
        "Medium",
        "High",
        "Critical",
    ]

    selected_risk = st.selectbox(
        "Risk Level",
        risk_options,
    )


# ------------------------------------------------------------
# Priority filter
# ------------------------------------------------------------

with filter_col2:

    priority_options = (
        ["All"]
        + sorted(
            df["Priority"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )
    )

    selected_priority = st.selectbox(
        "Priority",
        priority_options,
    )


# ------------------------------------------------------------
# Campaign filter
# ------------------------------------------------------------

with filter_col3:

    campaign_options = (
        ["All"]
        + sorted(
            df["Campaign_Type"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )
    )

    selected_campaign = st.selectbox(
        "Campaign Type",
        campaign_options,
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_risk != "All":

    filtered_df = filtered_df[
        filtered_df["Risk_Level_Display"]
        == selected_risk
    ]


if selected_priority != "All":

    filtered_df = filtered_df[
        filtered_df["Priority"]
        == selected_priority
    ]


if selected_campaign != "All":

    filtered_df = filtered_df[
        filtered_df["Campaign_Type"]
        == selected_campaign
    ]


# ============================================================
# EMPTY FILTER RESULT
# ============================================================

if filtered_df.empty:

    st.warning(
        "No customers match the selected filters."
    )

    st.stop()


# ============================================================
# AI RISK SUMMARY
# ============================================================

st.subheader(
    "📊 AI Risk Intelligence"
)


total_customers = len(
    filtered_df
)


high_critical_df = filtered_df[
    filtered_df["Risk_Level_Display"].isin(
        [
            "High",
            "Critical",
        ]
    )
]


high_critical_count = len(
    high_critical_df
)


average_risk = (
    filtered_df["Risk_Probability"]
    .mean()
)


customer_value_at_risk = (
    high_critical_df["Monetary"]
    .sum()
)


# ============================================================
# KPI CARDS
# ============================================================

kpi1, kpi2, kpi3, kpi4 = (
    st.columns(4)
)


with kpi1:

    st.metric(
        "Customers Analyzed",
        f"{total_customers:,}",
    )


with kpi2:

    st.metric(
        "High / Critical Risk",
        f"{high_critical_count:,}",
    )


with kpi3:

    st.metric(
        "Average Churn Probability",
        f"{average_risk:.2%}",
    )


with kpi4:

    st.metric(
        "Customer Value at Risk",
        f"₹ {customer_value_at_risk:,.2f}",
    )


st.divider()


# ============================================================
# RISK DISTRIBUTION
# ============================================================

st.subheader(
    "🚨 Customer Risk Distribution"
)


RISK_ORDER = [
    "Low",
    "Medium",
    "High",
    "Critical",
]


risk_distribution = (
    filtered_df["Risk_Level_Display"]
    .value_counts()
    .reindex(
        RISK_ORDER,
        fill_value=0,
    )
    .reset_index()
)


risk_distribution.columns = [
    "Risk Level",
    "Customers",
]


risk_distribution["Share (%)"] = (
    risk_distribution["Customers"]
    / total_customers
    * 100
)


chart_col, table_col = st.columns(
    [1.5, 1]
)


with chart_col:

    fig_risk = px.bar(
        risk_distribution,
        x="Risk Level",
        y="Customers",
        text="Customers",
        category_orders={
            "Risk Level": RISK_ORDER,
        },
        title="Customer Risk Distribution",
    )

    fig_risk.update_traces(
        textposition="outside",
    )

    fig_risk.update_layout(
        height=420,
        showlegend=False,
        xaxis_title="Risk Level",
        yaxis_title="Customers",
    )

    st.plotly_chart(
        fig_risk,
        width="stretch",
    )


with table_col:

    display_risk = (
        risk_distribution.copy()
    )

    display_risk["Share (%)"] = (
        display_risk["Share (%)"]
        .round(2)
    )

    st.dataframe(
        display_risk,
        width="stretch",
        hide_index=True,
    )


st.divider()


# ============================================================
# BUSINESS REASONS
# ============================================================

st.subheader(
    "🔍 Why Customers Are At Risk"
)


reason_data = (
    filtered_df["Business_Reason"]
    .value_counts()
    .head(10)
    .reset_index()
)


reason_data.columns = [
    "Business Reason",
    "Customers",
]


if not reason_data.empty:

    fig_reason = px.bar(
        reason_data.sort_values(
            "Customers"
        ),
        x="Customers",
        y="Business Reason",
        orientation="h",
        text="Customers",
        title="Top Business Reasons Behind Customer Risk",
    )

    fig_reason.update_traces(
        textposition="outside",
    )

    fig_reason.update_layout(
        height=450,
        showlegend=False,
        xaxis_title="Customers",
        yaxis_title="",
    )

    st.plotly_chart(
        fig_reason,
        width="stretch",
    )


st.caption(
    "Business reasons are derived from the customer-level "
    "AI explanation dataset."
)


st.divider()


# ============================================================
# AI INSIGHT TAGS
# ============================================================

st.subheader(
    "🏷️ Leading AI Insight Drivers"
)


def split_tags(value):

    if pd.isna(value):
        return []

    value = str(value)

    for separator in [
        ";",
        "|",
        ",",
    ]:

        if separator in value:

            return [
                item.strip()
                for item in value.split(separator)
                if item.strip()
            ]

    return [value.strip()]


tag_rows = []


for value in filtered_df[
    "AI_Insight_Tags"
].dropna():

    for tag in split_tags(value):

        if tag:
            tag_rows.append(tag)


if tag_rows:

    tag_data = (
        pd.Series(tag_rows)
        .value_counts()
        .head(10)
        .reset_index()
    )

    tag_data.columns = [
        "Insight Tag",
        "Customers",
    ]

    fig_tags = px.bar(
        tag_data.sort_values(
            "Customers"
        ),
        x="Customers",
        y="Insight Tag",
        orientation="h",
        text="Customers",
        title="Top AI-Identified Customer Risk Drivers",
    )

    fig_tags.update_traces(
        textposition="outside",
    )

    fig_tags.update_layout(
        height=450,
        showlegend=False,
        xaxis_title="Customers",
        yaxis_title="",
    )

    st.plotly_chart(
        fig_tags,
        width="stretch",
    )

else:

    st.info(
        "No AI insight tags are available."
    )


st.divider()


# ============================================================
# RETENTION CAMPAIGNS
# ============================================================

st.subheader(
    "🎯 Recommended Retention Actions"
)


campaign_data = (
    filtered_df["Campaign_Type"]
    .value_counts()
    .reset_index()
)


campaign_data.columns = [
    "Campaign Type",
    "Customers",
]


campaign_col1, campaign_col2 = (
    st.columns([1.5, 1])
)


with campaign_col1:

    fig_campaign = px.bar(
        campaign_data.sort_values(
            "Customers"
        ),
        x="Customers",
        y="Campaign Type",
        orientation="h",
        text="Customers",
        title="Recommended Campaign Strategy",
    )

    fig_campaign.update_traces(
        textposition="outside",
    )

    fig_campaign.update_layout(
        height=420,
        showlegend=False,
        xaxis_title="Customers",
        yaxis_title="",
    )

    st.plotly_chart(
        fig_campaign,
        width="stretch",
    )


with campaign_col2:

    st.markdown(
        "### Campaign Mix"
    )

    st.dataframe(
        campaign_data,
        width="stretch",
        hide_index=True,
    )


st.divider()


# ============================================================
# CUSTOMER-LEVEL EXPLANATION
# ============================================================

st.subheader(
    "🧠 Customer-Level AI Explanation"
)


customer_ids = (
    filtered_df[
        "customer_unique_id"
    ]
    .dropna()
    .astype(str)
    .unique()
    .tolist()
)


selected_customer = st.selectbox(
    "Select a customer",
    customer_ids,
)


customer_row = (
    filtered_df[
        filtered_df[
            "customer_unique_id"
        ]
        .astype(str)
        == selected_customer
    ]
    .iloc[0]
)


# ============================================================
# CUSTOMER RISK SUMMARY
# ============================================================

risk_probability = float(
    customer_row["Risk_Probability"]
)


risk_level = (
    customer_row["Risk_Level_Display"]
)


priority = (
    customer_row["Priority"]
)


profile_col1, profile_col2, profile_col3 = (
    st.columns(3)
)


with profile_col1:

    st.metric(
        "Risk Probability",
        f"{risk_probability:.2%}",
    )


with profile_col2:

    st.metric(
        "Risk Level",
        risk_level,
    )


with profile_col3:

    st.metric(
        "Priority",
        priority,
    )


# ============================================================
# AI EXPLANATION
# ============================================================

st.markdown(
    "### 🧠 Why This Customer Is At Risk"
)


st.info(
    customer_row[
        "AI_Customer_Explanation"
    ]
)


reason_col, action_col = (
    st.columns(2)
)


with reason_col:

    st.markdown(
        "### 📌 Business Reason"
    )

    st.write(
        customer_row[
            "Business_Reason"
        ]
    )

    st.markdown(
        "### 🏷️ AI Insight Tags"
    )

    st.write(
        customer_row[
            "AI_Insight_Tags"
        ]
    )


with action_col:

    st.markdown(
        "### 🎯 Recommended Action"
    )

    st.success(
        customer_row[
            "Recommendation"
        ]
    )

    st.markdown(
        "### 📣 Campaign Type"
    )

    st.write(
        customer_row[
            "Campaign_Type"
        ]
    )


# ============================================================
# EXPECTED BUSINESS OUTCOME
# ============================================================

st.markdown(
    "### 📈 Expected Business Outcome"
)


st.write(
    customer_row[
        "Expected_Outcome"
    ]
)


# ============================================================
# CUSTOMER PROFILE
# ============================================================

st.markdown(
    "### 📊 Customer Profile"
)


profile1, profile2, profile3, profile4 = (
    st.columns(4)
)


with profile1:

    st.metric(
        "Frequency",
        f"{customer_row['Frequency']:.0f}",
    )


with profile2:

    st.metric(
        "Monetary Value",
        f"₹ {customer_row['Monetary']:,.2f}",
    )


with profile3:

    st.metric(
        "Average Order Value",
        f"₹ {customer_row['average_order_value']:,.2f}",
    )


with profile4:

    st.metric(
        "Review Score",
        f"{customer_row['average_review_score']:.1f}",
    )


st.divider()


# ============================================================
# EXECUTIVE INTERPRETATION
# ============================================================

st.subheader(
    "💡 Executive Interpretation"
)


risk_percentage = (
    high_critical_count
    / total_customers
    if total_customers > 0
    else 0
)


if risk_percentage >= 0.50:

    interpretation = (
        f"More than half of the analyzed customers "
        f"({risk_percentage:.1%}) are classified as High "
        f"or Critical risk. This represents a significant "
        f"retention opportunity. Retention campaigns should "
        f"prioritize customers using both churn probability "
        f"and monetary value."
    )

elif risk_percentage >= 0.25:

    interpretation = (
        f"{risk_percentage:.1%} of analyzed customers are "
        f"High or Critical risk. The business should focus "
        f"retention efforts on high-value customers while "
        f"using targeted re-engagement strategies for "
        f"medium-risk customers."
    )

else:

    interpretation = (
        f"{risk_percentage:.1%} of analyzed customers are "
        f"High or Critical risk. Retention activity can "
        f"focus on targeted interventions while maintaining "
        f"engagement with lower-risk customers."
    )


st.info(
    interpretation
)


# ============================================================
# DOWNLOAD FILTERED AI INSIGHTS
# ============================================================

st.divider()

st.subheader(
    "📥 Export AI Insights"
)


download_df = filtered_df.drop(
    columns=[
        "Risk_Level_Display",
    ],
    errors="ignore",
)


csv_data = (
    download_df
    .to_csv(index=False)
    .encode("utf-8")
)


st.download_button(
    label="Download Filtered AI Insights",
    data=csv_data,
    file_name="ai_retention_insights.csv",
    mime="text/csv",
    width="stretch",
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Retention Intelligence | "
    "Customer churn prediction + explainable AI + "
    "retention recommendations"
)

st.caption(
    f"AI insights powered by {len(df):,} customer records."
)
