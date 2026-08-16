import streamlit as st


def display_kpi_card(
    title: str,
    value: str,
    description: str = "",
):
    """
    Display a reusable KPI metric card.

    Parameters
    ----------
    title : str
        KPI name.

    value : str
        KPI value to display.

    description : str, optional
        Supporting information shown below the KPI.
    """

    with st.container(border=True):

        st.markdown(f"**{title}**")

        st.markdown(
            f"<h2>{value}</h2>",
            unsafe_allow_html=True,
        )

        if description:
            st.caption(description)