import streamlit as st


def render_sidebar():
    """
    Render the global application sidebar navigation.
    """

    with st.sidebar:

        # =====================================================
        # SIDEBAR HEADING
        # =====================================================

        st.markdown(
            """
            <div class="sidebar-title">
                RETENTION PLATFORM
            </div>
            """,
            unsafe_allow_html=True,
        )

        # =====================================================
        # APPLICATION PAGES
        # =====================================================

        st.page_link(
            "app.py",
            label="🏠 App",
        )

        st.page_link(
            "pages/01_Dashboard.py",
            label="📊 Dashboard",
        )

        st.page_link(
            "pages/02_Customer_Prediction.py",
            label="🎯 Customer Prediction",
        )

        st.page_link(
            "pages/03_AI_Insights.py",
            label="🤖 AI Insights",
        )

        st.page_link(
            "pages/04_Executive_Report.py",
            label="📋 Executive Report",
        )