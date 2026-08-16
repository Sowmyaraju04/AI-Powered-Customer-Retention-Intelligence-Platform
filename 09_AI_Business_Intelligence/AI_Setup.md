# AI Setup

## Objective

The objective of this notebook is to prepare a business-ready dataset for the AI Business Intelligence layer. This dataset combines customer behavior, churn predictions, business recommendations, and key business attributes into a single structured dataset that can be consumed by downstream AI components.

## Activities Performed

- Loaded the customer retention recommendation dataset.
- Selected relevant business and machine learning features.
- Created AI insight tags based on customer behavior.
- Validated dataset completeness.
- Generated an AI-ready dataset.
- Saved the final dataset for AI processing.

## Input

- customer_retention_recommendations.csv

## Output

- ai_ready_dataset.csv

## Key Features

- Customer Unique ID
- Frequency
- Monetary Value
- Average Order Value
- Average Review Score
- Preferred Payment Method
- Risk Probability
- Risk Level
- Customer Value
- Recommendation
- Campaign Type
- Business Reason
- Expected Outcome
- AI Insight Tags

## Business Value

This notebook prepares a structured dataset that enables AI-powered customer explanations, executive summaries, and business reporting. Instead of relying on raw customer data, the AI layer receives clean and business-contextual information for consistent decision-making.