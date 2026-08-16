import sys
from pathlib import Path

import pandas as pd


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

STREAMLIT_APP = (
    PROJECT_ROOT / "10_Streamlit_Application"
)

if str(STREAMLIT_APP) not in sys.path:
    sys.path.insert(0, str(STREAMLIT_APP))


from config.settings import MODEL_PATH
from utils.model_loader import load_model
from utils.prediction import (
    MODEL_FEATURES,
    generate_predictions,
    validate_prediction_features,
)


# ============================================================
# SAMPLE DATA
# ============================================================

SAMPLE_FILE = (
    STREAMLIT_APP
    / "data"
    / "sample"
    / "customer_prediction_sample.csv"
)


# ============================================================
# TEST MODEL EXISTS
# ============================================================

def test_model_exists():

    assert MODEL_PATH.exists(), (
        f"Model not found: {MODEL_PATH}"
    )


# ============================================================
# TEST MODEL LOADING
# ============================================================

def test_model_loading():

    model = load_model(
        MODEL_PATH
    )

    assert model is not None


# ============================================================
# TEST SAMPLE DATA
# ============================================================

def test_sample_dataset():

    df = pd.read_csv(
        SAMPLE_FILE
    )

    assert not df.empty

    assert len(df) == 10


# ============================================================
# TEST FEATURE VALIDATION
# ============================================================

def test_prediction_features():

    df = pd.read_csv(
        SAMPLE_FILE
    )

    is_valid, missing_features = (
        validate_prediction_features(
            df
        )
    )

    assert is_valid is True

    assert missing_features == []


# ============================================================
# TEST PREDICTION GENERATION
# ============================================================

def test_prediction_generation():

    df = pd.read_csv(
        SAMPLE_FILE
    )

    model = load_model(
        MODEL_PATH
    )

    result = generate_predictions(
        model,
        df
    )

    assert isinstance(
        result,
        pd.DataFrame
    )

    assert len(result) == len(df)

    assert "Risk_Probability" in result.columns

    assert "Risk_Level" in result.columns

    assert "Prediction" in result.columns


# ============================================================
# TEST RISK PROBABILITY RANGE
# ============================================================

def test_risk_probability_range():

    df = pd.read_csv(
        SAMPLE_FILE
    )

    model = load_model(
        MODEL_PATH
    )

    result = generate_predictions(
        model,
        df
    )

    assert (
        result["Risk_Probability"]
        .between(0, 1)
        .all()
    )