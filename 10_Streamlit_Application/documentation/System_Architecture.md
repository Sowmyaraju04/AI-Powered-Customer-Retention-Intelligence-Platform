# System Architecture

## AI-Powered Customer Retention Intelligence Platform

**Phase:** 10 — Streamlit Web Application  
**Document Type:** System Architecture Specification  
**Status:** Design

---

# 1. Architecture Overview

The AI-Powered Customer Retention Intelligence Platform is an end-to-end analytics application designed to transform customer transaction data into actionable churn predictions, customer-level explanations, retention recommendations, and executive business insights.

The application follows a modular layered architecture:

```text
                    ┌──────────────────────────────┐
                    │        USER / BUSINESS       │
                    │          STAKEHOLDERS        │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │       STREAMLIT WEB APP       │
                    │                              │
                    │  Dashboard                   │
                    │  Customer Prediction         │
                    │  AI Insights                 │
                    │  Executive Report            │
                    └──────────────┬───────────────┘
                                   │
                                   ▼
                    ┌──────────────────────────────┐
                    │       APPLICATION LOGIC       │
                    │                              │
                    │  Data Validation             │
                    │  Preprocessing               │
                    │  Prediction                  │
                    │  Risk Scoring                │
                    │  Recommendation Engine        │
                    └──────────────┬───────────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
          ┌────────────────┐ ┌────────────┐ ┌──────────────────┐
          │  ML MODEL      │ │ AI OUTPUTS │ │ BUSINESS LOGIC   │
          │                │ │            │ │                  │
          │ Churn Model    │ │ SHAP /     │ │ Recommendations  │
          │                │ │ Customer   │ │ Revenue at Risk  │
          │ churn_model.pkl│ │ Explanations│ │ Risk Categories │
          └────────┬───────┘ └─────┬──────┘ └────────┬─────────┘
                   │               │                  │
                   └───────────────┼──────────────────┘
                                   ▼
                    ┌──────────────────────────────┐
                    │       FINAL AI DATA          │
                    │                              │
                    │ ai_ready_dataset.csv         │
                    │ ai_customer_explanations.csv │
                    │ executive_summary.csv        │
                    │ business_report_data.csv     │
                    └──────────────────────────────┘

Presentation Layer
        ↓
Application Layer
        ↓
Business Intelligence Layer
        ↓
Machine Learning Layer
        ↓
Data Layer

Components
app.py
pages/
    01_Dashboard.py
    02_Customer_Prediction.py
    03_AI_Insights.py
    04_Executive_Report.py
components/
    sidebar.py
    metrics.py
    charts.py
    cards.py

Components
utils/
    model_loader.py
    prediction.py
    recommendation.py
    preprocessing.py
    helpers.py

The machine learning layer contains the trained churn prediction model developed during the Machine Learning phase.

models/
    churn_model.pkl

The model receives customer-level analytical features and produces churn probability.

Customer Features
       ↓
Preprocessing
       ↓
Trained Churn Model
       ↓
Churn Probability
       ↓
Risk Score
       ↓
Risk Category

The Explainable AI layer provides customer-level explanations for model predictions.

The system uses previously generated AI explanation outputs where available.

Customer Prediction
        ↓
Risk Score
        ↓
Important Risk Drivers
        ↓
Customer Explanation
        ↓
Business Interpretation

Primary output:

ai_customer_explanations.csv

he recommendation engine converts customer risk and behavioral information into actionable retention strategies.

Churn Risk
     +
Customer Value
     +
Customer Behavior
     +
Experience Signals
     ↓
Recommendation Engine
     ↓
Retention Recommendation
     ↓
Business Action

The application consumes processed customer-level data and previously generated AI business outputs.

Primary data sources
data/final/


ai_ready_dataset.csv
ai_customer_explanations.csv
executive_summary.csv
business_report_data.csv

Application-wide configuration is maintained separately.

config/
    settings.py

Application Navigation

The application follows a business decision journey:

Dashboard
    ↓
Customer Prediction
    ↓
AI Insights
    ↓
Executive Report

Each page answers a different business question.

Dashboard
"What is happening?"


        ↓


Customer Prediction
"Who is at risk?"


        ↓


AI Insights
"Why are they at risk?"


        ↓


Executive Report
"What should the business prioritize?"

End-to-End Architecture Flow
Raw / Processed Data
        ↓
Customer-Level Features
        ↓
Machine Learning Model
        ↓
Churn Probability
        ↓
Risk Score
        ↓
Risk Category
        ↓
Customer Explanation
        ↓
Retention Recommendation
        ↓
Revenue at Risk
        ↓
Executive Insights
        ↓
Streamlit Application
        ↓
Business Decision

The application is designed to support local development and future cloud deployment.

Developer Environment
        ↓
GitHub Repository
        ↓
Streamlit Application
        ↓
Production / Cloud Deployment

The architecture connects data engineering, machine learning, explainable AI, recommendation logic, and business intelligence into a single application.

The final system transforms:

Customer Data
      ↓
Risk Prediction
      ↓
Risk Explanation
      ↓
Retention Recommendation
      ↓
Revenue Impact
      ↓
Business Decision