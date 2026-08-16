from pathlib import Path

import joblib
import streamlit as st


@st.cache_resource
def load_model(model_path):
    """
    Load and cache the trained churn prediction model.

    Streamlit's cache_resource is used because the model
    is a reusable application resource rather than data
    that should be copied for every session.

    Parameters
    ----------
    model_path : str or Path
        Location of the saved model.

    Returns
    -------
    model
        Loaded scikit-learn model/pipeline.

    Raises
    ------
    FileNotFoundError
        If the model file does not exist.

    RuntimeError
        If the model cannot be loaded.
    """

    model_path = Path(model_path)

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found: {model_path}"
        )

    try:

        model = joblib.load(model_path)

    except Exception as exc:

        raise RuntimeError(
            f"Unable to load churn prediction model: "
            f"{model_path}"
        ) from exc

    if not hasattr(model, "predict"):
        raise RuntimeError(
            "Loaded model does not provide a "
            "'predict' method."
        )

    if not hasattr(model, "predict_proba"):
        raise RuntimeError(
            "Loaded model does not provide a "
            "'predict_proba' method."
        )

    return model


def model_exists(model_path):
    """
    Check whether the trained model exists.
    """

    return Path(model_path).exists()