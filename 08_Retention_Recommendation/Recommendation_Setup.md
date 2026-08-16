# Recommendation Setup

## Objective

The objective of this notebook is to transform the machine learning model predictions into a business-ready recommendation dataset.

## Activities Performed

- Loaded the trained Gradient Boosting model.
- Loaded the customer retention modeling dataset.
- Generated churn-risk probabilities.
- Classified customers into High, Medium, and Low risk groups.
- Assigned business priorities based on predicted risk.
- Prepared the recommendation dataset for downstream business decision-making.

## Output

Generated:

- customer_recommendation_data.csv

New Features Created:

- Risk_Probability
- Risk_Level
- Priority

## Business Value

This notebook bridges the gap between predictive analytics and business action by converting model predictions into structured customer risk information that can be used by marketing and customer success teams.