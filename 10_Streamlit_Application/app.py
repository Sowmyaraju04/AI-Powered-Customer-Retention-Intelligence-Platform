
"""
Main Streamlit Application
--------------------------
AI-Powered Customer Retention Intelligence Platform
"""

from pathlib import Path

import streamlit as st

from config.settings import (
    APP_TITLE,
    PAGE_ICON,
    LAYOUT,
)


# ============================================================
# PROJECT PATH
# ============================================================

APP_DIR = Path(__file__).resolve().parent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT,
)


# ============================================================
# GLOBAL STYLING
# ============================================================

CSS_PATH = APP_DIR / "assets" / "styles.css"

if CSS_PATH.exists():

    with open(
        CSS_PATH,
        "r",
        encoding="utf-8",
    ) as css_file:

        st.markdown(
            f"""
            <style>
            {css_file.read()}
            </style>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# APP / HOME PAGE
# ============================================================

def render_home():

    # ========================================================
    # CENTERED PLATFORM HEADER
    # ========================================================

    header_left, header_center, header_right = st.columns(
        [1, 4, 1]
    )

    with header_center:

        st.markdown(
            """
            # 🎯 AI-Powered Customer Retention Intelligence Platform
            """,
            text_alignment="center",
        )

        st.markdown(
            """
            **Identify churn risk. Understand why.
            Take proactive retention actions.**
            """,
            text_alignment="center",
        )

    st.divider()


    # ========================================================
    # APPLICATION OVERVIEW
    # ========================================================

    st.markdown(
        """
        ### Welcome to the Customer Retention Intelligence Platform

        This application transforms customer-level analytics
        and machine learning predictions into actionable
        retention intelligence.

        Use the platform to:
        """
    )


    overview_col1, overview_col2, overview_col3, overview_col4 = (
        st.columns(4)
    )


    with overview_col1:

        st.markdown(
            """
            ### 📊 Monitor

            Track customer churn risk, customer value,
            and revenue exposure.
            """
        )


    with overview_col2:

        st.markdown(
            """
            ### 🎯 Predict

            Generate customer-level churn probabilities
            and risk classifications.
            """
        )


    with overview_col3:

        st.markdown(
            """
            ### 🤖 Understand

            Identify the business factors contributing
            to customer churn risk.
            """
        )


    with overview_col4:

        st.markdown(
            """
            ### 📋 Act

            Prioritize retention campaigns based on
            customer risk and business value.
            """
        )


    st.divider()


    # ========================================================
    # PLATFORM WORKFLOW
    # ========================================================

    st.subheader(
        "Platform Workflow"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.markdown(
            """
            ### 1️⃣ Identify

            Detect customers with elevated churn risk.
            """
        )


    with col2:

        st.markdown(
            """
            ### 2️⃣ Understand

            Identify the factors contributing to customer risk.
            """
        )


    with col3:

        st.markdown(
            """
            ### 3️⃣ Act

            Generate targeted retention recommendations.
            """
        )


    with col4:

        st.markdown(
            """
            ### 4️⃣ Prioritize

            Focus retention efforts on customers with
            the highest business impact.
            """
        )


    st.divider()


    # ========================================================
    # PLATFORM CAPABILITIES
    # ========================================================

    st.subheader(
        "Platform Capabilities"
    )


    capability_col1, capability_col2 = st.columns(2)


    with capability_col1:

        st.markdown(
            """
            **Customer Analytics**

            - Customer risk segmentation
            - Churn probability
            - Customer value analysis
            - Revenue exposure analysis
            """
        )


    with capability_col2:

        st.markdown(
            """
            **AI-Powered Retention**

            - Explainable customer risk
            - Business risk drivers
            - Retention recommendations
            - Campaign prioritization
            """
        )


    st.divider()


    # ========================================================
    # FOOTER
    # ========================================================

    st.caption(
        "AI-Powered Customer Retention Intelligence Platform"
    )


# ============================================================
# APPLICATION NAVIGATION
# ============================================================

pages = [

    st.Page(
        render_home,
        title="App",
        icon="🏠",
        default=True,
    ),

    st.Page(
        "pages/01_Dashboard.py",
        title="Dashboard",
        icon="📊",
    ),

    st.Page(
        "pages/02_Customer_Prediction.py",
        title="Customer Prediction",
        icon="🎯",
    ),

    st.Page(
        "pages/03_AI_Insights.py",
        title="AI Insights",
        icon="🤖",
    ),

    st.Page(
        "pages/04_Executive_Report.py",
        title="Executive Report",
        icon="📋",
    ),
]


# ============================================================
# RUN APPLICATION
# ============================================================

pg = st.navigation(
    {
        "RETENTION PLATFORM": pages
    }
)

pg.run()

