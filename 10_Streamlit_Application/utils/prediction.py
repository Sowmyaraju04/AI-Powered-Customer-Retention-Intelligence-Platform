import pandas as pd


# ============================================================
# MODEL FEATURES
# ============================================================

MODEL_FEATURES = [
    "Frequency",
    "Monetary",
    "average_review_score",
    "preferred_payment_method",
    "average_order_value",
]


# ============================================================
# VALIDATE INPUT FEATURES
# ============================================================

def validate_prediction_features(
    df: pd.DataFrame
) -> tuple[bool, list[str]]:
    """
    Validate that all features required by the trained
    churn model are present in the input dataset.
    """

    missing_columns = [
        column
        for column in MODEL_FEATURES
        if column not in df.columns
    ]

    return len(missing_columns) == 0, missing_columns


# ============================================================
# PREPARE MODEL INPUT
# ============================================================

def prepare_model_input(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Select model features in the exact order expected
    by the trained pipeline.
    """

    is_valid, missing_columns = validate_prediction_features(df)

    if not is_valid:
        raise ValueError(
            "Missing required model features: "
            + ", ".join(missing_columns)
        )

    return df[MODEL_FEATURES].copy()


# ============================================================
# GENERATE CHURN PROBABILITY
# ============================================================

def generate_churn_probability(
    model,
    df: pd.DataFrame
) -> pd.Series:
    """
    Generate churn-risk probability for each customer.
    """

    model_input = prepare_model_input(df)

    probabilities = model.predict_proba(model_input)

    return pd.Series(
        probabilities[:, 1],
        index=df.index,
        name="Risk_Probability",
    )


# ============================================================
# ASSIGN RISK LEVEL
# ============================================================

def assign_risk_level(
    probability: pd.Series
) -> pd.Series:
    """
    Convert churn probability into business-friendly
    risk categories.

    Thresholds:
        < 0.25  -> Low
        < 0.50  -> Medium
        < 0.75  -> High
        >= 0.75 -> Critical
    """

    return pd.cut(
        probability,
        bins=[-float("inf"), 0.25, 0.50, 0.75, float("inf")],
        labels=[
            "Low",
            "Medium",
            "High",
            "Critical",
        ],
        right=False,
    ).astype(str)


# ============================================================
# GENERATE PREDICTIONS
# ============================================================

def generate_predictions(
    model,
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Generate churn predictions and business-friendly
    risk information.
    """

    result = df.copy()

    model_input = prepare_model_input(df)

    predictions = model.predict(model_input)

    probabilities = model.predict_proba(model_input)

    result["Prediction"] = predictions

    result["Risk_Probability"] = probabilities[:, 1]

    result["Risk_Level"] = assign_risk_level(
        result["Risk_Probability"]
    )

    return result


# ============================================================
# FORMAT PREDICTION RESULTS
# ============================================================

def format_prediction_results(
    df: pd.DataFrame
) -> pd.DataFrame:
    """
    Format prediction results for display in Streamlit.
    """

    result = df.copy()

    if "Risk_Probability" in result.columns:

        result["Risk_Probability"] = (
            result["Risk_Probability"]
            .astype(float)
            .round(4)
        )

    return result