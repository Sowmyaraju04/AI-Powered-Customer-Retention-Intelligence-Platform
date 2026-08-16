"""
Customer Prediction
-------------------
Generate customer-level churn predictions using the trained
machine learning model.
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
# APPLICATION IMPORTS
# ============================================================

from config.settings import (
    MODEL_PATH,
    SAMPLE_DATA_DIR,
)

from utils.model_loader import load_model

from utils.prediction import (
    MODEL_FEATURES,
    generate_predictions,
    validate_prediction_features,
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🎯",
    layout="wide",
)


# ============================================================
# PAGE-SPECIFIC STYLES
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       ACTION BUTTONS
       ====================================================== */

    div.stButton > button[kind="primary"] {
        background-color: #0B5ED7 !important;
        color: white !important;
        border: 1px solid #084298 !important;
        border-radius: 9px !important;
        min-height: 52px !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        box-shadow: 0 3px 8px rgba(11, 94, 215, 0.20) !important;
        transition: all 0.15s ease-in-out !important;
    }

    div.stButton > button[kind="primary"]:hover {
        background-color: #084298 !important;
        border-color: #052C65 !important;
        color: white !important;
        box-shadow: 0 5px 12px rgba(11, 94, 215, 0.28) !important;
    }

    div.stButton > button[kind="primary"]:focus {
        color: white !important;
        border-color: #052C65 !important;
    }


    /* ======================================================
       DOWNLOAD BUTTONS
       ====================================================== */

    div[data-testid="stDownloadButton"] > button {
        background-color: #0B5ED7 !important;
        color: white !important;
        border: 1px solid #084298 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        min-height: 46px !important;
        box-shadow: 0 2px 7px rgba(11, 94, 215, 0.18) !important;
    }

    div[data-testid="stDownloadButton"] > button:hover {
        background-color: #084298 !important;
        color: white !important;
        border-color: #052C65 !important;
    }


    /* ======================================================
       IMPORTANT ACTION AREAS
       ====================================================== */

    .prediction-action-card {
        background: #F0F6FF;
        border: 1px solid #B8D4F5;
        border-left: 5px solid #0B5ED7;
        border-radius: 10px;
        padding: 18px 20px 16px 20px;
        margin: 10px 0 18px 0;
    }

    .prediction-action-title {
        color: #12355B;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .prediction-action-description {
        color: #4A5A6A;
        font-size: 14px;
        margin-bottom: 0;
    }


    .download-action-card {
        background: #F4F8FC;
        border: 1px solid #C7D7E8;
        border-left: 5px solid #0B5ED7;
        border-radius: 10px;
        padding: 16px 20px 14px 20px;
        margin: 10px 0 15px 0;
    }

    .download-action-title {
        color: #12355B;
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .download-action-description {
        color: #566575;
        font-size: 14px;
        margin-bottom: 0;
    }


    /* ======================================================
       KPI EMPHASIS
       ====================================================== */

    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #D8E2EC;
        border-radius: 10px;
        padding: 14px;
        box-shadow: 0 2px 7px rgba(31, 55, 80, 0.06);
    }


    /* ======================================================
       SECTION HEADINGS
       ====================================================== */

    .section-label {
        color: #12355B;
        font-size: 20px;
        font-weight: 700;
        margin-top: 4px;
        margin-bottom: 8px;
    }


    /* ======================================================
       RESULT AREA
       ====================================================== */

    .results-header {
        background: #F7FAFD;
        border: 1px solid #D8E2EC;
        border-radius: 9px;
        padding: 13px 16px;
        margin-bottom: 12px;
    }

    .results-header-title {
        color: #12355B;
        font-weight: 700;
        font-size: 16px;
    }

    .results-header-text {
        color: #607080;
        font-size: 13px;
        margin-top: 2px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# PAGE HEADER
# ============================================================

st.title("🎯 Customer Churn Prediction")

st.markdown(
    """
    Upload customer-level data or use the provided sample dataset
    to generate **churn probability, risk classification,
    and retention priorities**.

    The prediction engine uses the trained churn model developed
    in the AI/ML phase of the platform.
    """
)

st.divider()


# ============================================================
# MODEL STATUS
# ============================================================

st.subheader("🤖 Model Status")

try:

    model = load_model(MODEL_PATH)

except Exception as e:

    st.error(
        "❌ The churn prediction model could not be loaded."
    )

    st.code(
        str(e),
        language="text",
    )

    st.info(
        f"Expected model location:\n\n{MODEL_PATH}"
    )

    st.stop()

else:

    st.success(
        "✅ Churn prediction model loaded successfully."
    )


# ============================================================
# REQUIRED MODEL FEATURES
# ============================================================

with st.expander(
    "📋 Required Customer Features",
    expanded=False,
):

    st.write(
        "The customer dataset must contain these "
        "features required by the trained model:"
    )

    for feature in MODEL_FEATURES:
        st.code(feature)


# ============================================================
# SAMPLE DATASET
# ============================================================

st.subheader("🧪 Sample Dataset")

sample_files = sorted(
    SAMPLE_DATA_DIR.glob("*.csv")
)

selected_sample = None
sample_preview = None


if sample_files:

    sample_options = [
        file.name
        for file in sample_files
    ]

    selected_sample_name = st.selectbox(
        "Select a sample customer dataset",
        sample_options,
    )

    selected_sample = (
        SAMPLE_DATA_DIR
        / selected_sample_name
    )

    try:

        sample_preview = pd.read_csv(
            selected_sample
        )

        sample_col1, sample_col2, sample_col3 = (
            st.columns(3)
        )

        with sample_col1:

            st.metric(
                "Rows",
                f"{len(sample_preview):,}",
            )

        with sample_col2:

            st.metric(
                "Columns",
                f"{len(sample_preview.columns):,}",
            )

        with sample_col3:

            features_valid, missing_features = (
                validate_prediction_features(
                    sample_preview
                )
            )

            if features_valid:

                st.success(
                    "Features Valid"
                )

            else:

                st.error(
                    "Features Missing"
                )

        if not features_valid:

            st.warning(
                "The selected sample dataset does not contain "
                "all required model features."
            )

            st.write(
                "Missing features:"
            )

            for feature in missing_features:

                st.write(
                    f"- {feature}"
                )

        sample_csv = (
            sample_preview
            .to_csv(index=False)
            .encode("utf-8")
        )

        st.download_button(
            label="⬇️ Download Sample CSV",
            data=sample_csv,
            file_name=selected_sample_name,
            mime="text/csv",
        )

    except Exception as e:

        st.warning(
            f"Unable to read sample dataset: {e}"
        )

else:

    st.warning(
        "No sample CSV files were found."
    )

    st.info(
        f"Expected directory:\n\n{SAMPLE_DATA_DIR}"
    )


st.divider()


# ============================================================
# DATA SOURCE SELECTION
# ============================================================

st.subheader("📂 Customer Data")

data_source = st.radio(
    "Choose data source",
    [
        "Use Sample Dataset",
        "Upload CSV",
    ],
    horizontal=True,
)


# ============================================================
# INITIALIZE DATAFRAME
# ============================================================

df = None


# ============================================================
# USE SAMPLE DATASET
# ============================================================

if data_source == "Use Sample Dataset":

    if selected_sample is None:

        st.error(
            "No sample dataset is available."
        )

        st.stop()

    try:

        df = pd.read_csv(
            selected_sample
        )

    except Exception as e:

        st.error(
            "❌ The sample dataset could not be loaded."
        )

        st.code(
            str(e),
            language="text",
        )

        st.stop()


# ============================================================
# UPLOAD CSV
# ============================================================

else:

    uploaded_file = st.file_uploader(
        "Upload a customer-level CSV file",
        type=["csv"],
        help=(
            "The CSV must contain all required model features."
        ),
    )

    if uploaded_file is None:

        st.info(
            "👆 Upload a customer CSV file to begin prediction."
        )

        st.stop()

    try:

        df = pd.read_csv(
            uploaded_file
        )

    except Exception as e:

        st.error(
            "❌ The uploaded CSV could not be read."
        )

        st.code(
            str(e),
            language="text",
        )

        st.stop()


# ============================================================
# EMPTY DATA VALIDATION
# ============================================================

if df is None or df.empty:

    st.error(
        "❌ The selected dataset is empty."
    )

    st.stop()


# ============================================================
# DATASET INFORMATION
# ============================================================

st.subheader("📊 Dataset Information")

info_col1, info_col2, info_col3 = (
    st.columns(3)
)

with info_col1:

    st.metric(
        "Rows",
        f"{len(df):,}",
    )

with info_col2:

    st.metric(
        "Columns",
        f"{len(df.columns):,}",
    )

with info_col3:

    st.metric(
        "Model Features",
        f"{len(MODEL_FEATURES)}",
    )


# ============================================================
# FEATURE VALIDATION
# ============================================================

is_valid, missing_features = (
    validate_prediction_features(df)
)


if not is_valid:

    st.error(
        "❌ Dataset validation failed."
    )

    st.markdown(
        "The following required model features are missing:"
    )

    for feature in missing_features:

        st.code(
            feature
        )

    st.stop()


st.success(
    "✅ Dataset validation successful. "
    "All required model features are available."
)


# ============================================================
# DATA PREVIEW
# ============================================================

st.subheader("👀 Data Preview")

st.dataframe(
    df.head(10),
    width="stretch",
    hide_index=True,
)


# ============================================================
# RUN PREDICTION
# ============================================================

st.divider()

st.markdown(
    """
    <div class="prediction-action-card">
        <div class="prediction-action-title">
            🚀 Generate Churn Predictions
        </div>
        <div class="prediction-action-description">
            Run the trained machine learning model to calculate
            customer churn probability and risk level.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

run_prediction = st.button(
    "🚀 Run Churn Prediction",
    type="primary",
    width="stretch",
)


# ============================================================
# PREDICTION ENGINE
# ============================================================

if run_prediction:

    with st.spinner(
        "Generating customer churn predictions..."
    ):

        try:

            result = generate_predictions(
                model,
                df,
            )

        except Exception as e:

            st.error(
                "❌ Prediction generation failed."
            )

            st.code(
                str(e),
                language="text",
            )

            st.stop()


    st.success(
        "✅ Churn predictions generated successfully."
    )


    # ========================================================
    # PREDICTION SUMMARY
    # ========================================================

    st.divider()

    st.markdown(
        '<div class="section-label">📈 Prediction Summary</div>',
        unsafe_allow_html=True,
    )

    total_customers = len(result)

    average_probability = (
        result["Risk_Probability"]
        .mean()
    )

    high_risk_count = (
        result["Risk_Level"]
        == "High"
    ).sum()

    critical_risk_count = (
        result["Risk_Level"]
        == "Critical"
    ).sum()

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
            "Average Churn Probability",
            f"{average_probability:.2%}",
        )

    with kpi3:

        st.metric(
            "High Risk Customers",
            f"{high_risk_count:,}",
        )

    with kpi4:

        st.metric(
            "Critical Risk Customers",
            f"{critical_risk_count:,}",
        )


    # ========================================================
    # HIGH / CRITICAL RISK
    # ========================================================

    high_critical_count = (
        result["Risk_Level"]
        .isin(
            [
                "High",
                "Critical",
            ]
        )
        .sum()
    )

    high_critical_percentage = (
        high_critical_count
        / total_customers
        if total_customers > 0
        else 0
    )


    # ========================================================
    # RISK DISTRIBUTION
    # ========================================================

    st.divider()

    st.subheader("🚨 Customer Risk Distribution")

    risk_order = [
        "Low",
        "Medium",
        "High",
        "Critical",
    ]

    risk_counts = (
        result["Risk_Level"]
        .value_counts()
        .reindex(
            risk_order,
            fill_value=0,
        )
        .reset_index()
    )

    risk_counts.columns = [
        "Risk Level",
        "Customers",
    ]

    chart_col, table_col = (
        st.columns(
            [1.6, 1]
        )
    )

    with chart_col:

        fig_risk = px.bar(
            risk_counts,
            x="Risk Level",
            y="Customers",
            text="Customers",
            category_orders={
                "Risk Level": risk_order,
            },
            title="Customer Distribution by Churn Risk",
            color="Risk Level",
            color_discrete_map={
                "Low": "#198754",
                "Medium": "#F0AD4E",
                "High": "#DC3545",
                "Critical": "#8B0000",
            },
        )

        fig_risk.update_traces(
            textposition="outside"
        )

        fig_risk.update_layout(
            height=420,
            showlegend=False,
            xaxis_title="Risk Level",
            yaxis_title="Customers",
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20,
            ),
        )

        st.plotly_chart(
            fig_risk,
            width="stretch",
        )

    with table_col:

        risk_table = risk_counts.copy()

        risk_table["Share (%)"] = (
            risk_table["Customers"]
            / total_customers
            * 100
        ).round(2)

        st.dataframe(
            risk_table,
            width="stretch",
            hide_index=True,
        )


    # ========================================================
    # BUSINESS INTERPRETATION
    # ========================================================

    st.divider()

    st.subheader("💡 Retention Interpretation")

    if high_critical_percentage >= 0.50:

        st.error(
            f"""
            **High Retention Urgency**

            {high_critical_count:,} customers
            ({high_critical_percentage:.1%}) are classified
            as High or Critical risk.

            A significant portion of the analyzed customer
            base requires proactive retention intervention.
            """
        )

    elif high_critical_percentage >= 0.25:

        st.warning(
            f"""
            **Moderate Retention Urgency**

            {high_critical_count:,} customers
            ({high_critical_percentage:.1%}) are classified
            as High or Critical risk.

            Retention campaigns should prioritize high-value
            customers within these risk segments.
            """
        )

    else:

        st.success(
            f"""
            **Targeted Retention Opportunity**

            {high_critical_count:,} customers
            ({high_critical_percentage:.1%}) are classified
            as High or Critical risk.

            Retention efforts can focus on the highest-value
            customers while maintaining engagement with the
            remaining customer base.
            """
        )


    # ========================================================
    # CUSTOMER RESULTS
    # ========================================================

    st.divider()

    st.subheader("👥 Customer Prediction Results")

    st.markdown(
        """
        <div class="results-header">
            <div class="results-header-title">
                Customer-Level Churn Intelligence
            </div>
            <div class="results-header-text">
                Filter the prediction output by risk level or
                search for a specific customer.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    display_columns = [
        column
        for column in [
            "customer_unique_id",
            "Frequency",
            "Monetary",
            "average_order_value",
            "average_review_score",
            "preferred_payment_method",
            "Prediction",
            "Risk_Probability",
            "Risk_Level",
        ]
        if column in result.columns
    ]

    display_result = (
        result[
            display_columns
        ]
        .copy()
    )

    if "Risk_Probability" in display_result.columns:

        display_result[
            "Risk_Probability"
        ] = (
            display_result[
                "Risk_Probability"
            ]
            .astype(float)
            .round(4)
        )


    # ========================================================
    # RESULT FILTERS
    # ========================================================

    filter_col1, filter_col2 = (
        st.columns(2)
    )

    with filter_col1:

        selected_risk = st.selectbox(
            "Filter by Risk Level",
            [
                "All",
                "Low",
                "Medium",
                "High",
                "Critical",
            ],
            key="prediction_risk_filter",
        )

    with filter_col2:

        search_customer = st.text_input(
            "Search Customer ID",
            key="prediction_customer_search",
        )


    filtered_result = (
        display_result.copy()
    )


    if selected_risk != "All":

        filtered_result = (
            filtered_result[
                filtered_result[
                    "Risk_Level"
                ]
                == selected_risk
            ]
        )


    if search_customer:

        if (
            "customer_unique_id"
            in filtered_result.columns
        ):

            filtered_result = (
                filtered_result[
                    filtered_result[
                        "customer_unique_id"
                    ]
                    .astype(str)
                    .str.contains(
                        search_customer,
                        case=False,
                        na=False,
                    )
                ]
            )


    if filtered_result.empty:

        st.warning(
            "No customers match the selected filters."
        )

    else:

        st.dataframe(
            filtered_result,
            width="stretch",
            height=450,
            hide_index=True,
        )


    # ========================================================
    # DOWNLOAD RESULTS
    # ========================================================

    st.divider()

    st.markdown(
        """
        <div class="download-action-card">
            <div class="download-action-title">
                ⬇️ Download Prediction Results
            </div>
            <div class="download-action-description">
                Export the complete customer-level prediction
                dataset for further analysis or retention action.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    csv_data = (
        result
        .to_csv(index=False)
        .encode("utf-8")
    )

    st.download_button(
        label="⬇️ Download Prediction Results",
        data=csv_data,
        file_name="customer_churn_predictions.csv",
        mime="text/csv",
        width="stretch",
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI-Powered Customer Retention Intelligence Platform | "
    "Customer Churn Prediction"
)