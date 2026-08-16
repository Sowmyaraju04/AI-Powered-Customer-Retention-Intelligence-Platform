"""
Test Data Profiler

Project:
AI-Powered Customer Retention Intelligence Platform

Purpose:
Test data type validation and outlier analysis.
"""

from src.data.data_profiler import data_type_report, outlier_report


print("=" * 60)
print("DATA TYPE REPORT")
print("=" * 60)

type_report = data_type_report()

print(type_report.to_string(index=False))


print("\n")
print("=" * 60)
print("OUTLIER REPORT")
print("=" * 60)

outlier_report_data = outlier_report()

print(outlier_report_data.to_string(index=False))