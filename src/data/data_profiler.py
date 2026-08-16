"""
Data Profiler Module

Project:
AI-Powered Customer Retention Intelligence Platform

Purpose:
Generate summary statistics for all datasets.
"""

import pandas as pd

from src.data.data_loader import load_all_data


def dataset_summary():
    """
    Generate a summary of all datasets.

    Returns
    -------
    pandas.DataFrame
        Summary table containing dataset name,
        rows, columns and memory usage.
    """

    datasets = load_all_data()

    summary = []

    for name, df in datasets.items():

        summary.append({
            "Dataset": name,
            "Rows": df.shape[0],
            "Columns": df.shape[1],
            "Memory_MB": round(
                df.memory_usage(deep=True).sum() / (1024 * 1024), 2
            )
        })

    return pd.DataFrame(summary)

def missing_value_report():
    """
    Generate a missing value report for all datasets.

    Returns
    -------
    pandas.DataFrame
        Missing value summary.
    """

    datasets = load_all_data()

    report = []

    for dataset_name, df in datasets.items():

        total_rows = len(df)

        for column in df.columns:

            missing_count = df[column].isnull().sum()

            if missing_count > 0:

                report.append({
                    "Dataset": dataset_name,
                    "Column": column,
                    "Missing_Count": missing_count,
                    "Missing_Percentage": round(
                        (missing_count / total_rows) * 100,
                        2
                    )
                })

    return pd.DataFrame(report)


def duplicate_report():
    """
    Generate duplicate record report for all datasets.

    Returns
    -------
    pandas.DataFrame
        Duplicate summary for all datasets.
    """

    datasets = load_all_data()

    report = []

    for dataset_name, df in datasets.items():

        duplicate_count = df.duplicated().sum()

        report.append({
            "Dataset": dataset_name,
            "Total_Rows": len(df),
            "Duplicate_Rows": duplicate_count,
            "Duplicate_Percentage": round(
                (duplicate_count / len(df)) * 100,
                2
            )
        })

    return pd.DataFrame(report)


def data_type_report():
    """
    Generate data type report for all datasets.

    Returns
    -------
    pandas.DataFrame
        Data type summary.
    """

    datasets = load_all_data()

    report = []

    for dataset_name, df in datasets.items():

        for column in df.columns:

            report.append({
                "Dataset": dataset_name,
                "Column": column,
                "Data_Type": str(df[column].dtype)
            })

    return pd.DataFrame(report)

def outlier_report():
    """
    Generate an IQR-based outlier report for numerical columns
    across all datasets.

    Returns
    -------
    pandas.DataFrame
        Outlier summary containing dataset name, column,
        quartiles, IQR, bounds, outlier count, and percentage.
    """

    datasets = load_all_data()

    report = []

    for dataset_name, df in datasets.items():

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        for column in numeric_columns:

            series = df[column].dropna()

            # Skip columns with no usable numerical values
            if series.empty:
                continue

            q1 = series.quantile(0.25)
            q3 = series.quantile(0.75)

            iqr = q3 - q1

            lower_bound = q1 - (1.5 * iqr)
            upper_bound = q3 + (1.5 * iqr)

            outlier_mask = (
                (series < lower_bound)
                | (series > upper_bound)
            )

            outlier_count = outlier_mask.sum()

            report.append({
                "Dataset": dataset_name,
                "Column": column,
                "Q1": round(q1, 2),
                "Q3": round(q3, 2),
                "IQR": round(iqr, 2),
                "Lower_Bound": round(lower_bound, 2),
                "Upper_Bound": round(upper_bound, 2),
                "Outlier_Count": int(outlier_count),
                "Outlier_Percentage": round(
                    (outlier_count / len(series)) * 100,
                    2
                ),
                "Minimum": round(series.min(), 2),
                "Maximum": round(series.max(), 2)
            })

    return pd.DataFrame(report)
