
---

## `Data_Flow.md`


# Data Flow

## AI-Powered Customer Retention Intelligence Platform

**Phase:** 10 — Streamlit Web Application  
**Document Type:** Data Flow Specification  
**Status:** Design

---

# 1. Data Flow Overview

The platform transforms customer transaction data into predictive and prescriptive business outputs.

The overall data flow is:


Raw Data
   ↓
Processed Data
   ↓
Customer-Level Feature Dataset
   ↓
Machine Learning
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


2. Historical Data Flow

The project began with the Brazilian E-Commerce Dataset.

Customers
Orders
Order Items
Payments
Products
Reviews
Sellers
Geolocation
Translation
        ↓
Data Cleaning
        ↓
Exploratory Analysis
        ↓
Feature Engineering
        ↓
Customer-Level Dataset


3. Data Preparation Flow
Raw Dataset
      ↓
Data Validation
      ↓
Missing Value Treatment
      ↓
Duplicate Handling
      ↓
Invalid Value Handling
      ↓
Data Type Conversion
      ↓
Text Standardization
      ↓
Cleaned Dataset

4. Feature Engineering Flow

Transactional information is transformed into customer-level analytical features.

Orders
   +
Payments
   +
Reviews
   +
Order Items
   +
Products
        ↓
Customer-Level Aggregation
        ↓
Behavioral Features
        ↓
Transaction Features
        ↓
Experience Features
        ↓
Customer Feature Dataset


5. Machine Learning Data Flow
Customer Feature Dataset
        ↓
Feature Selection
        ↓
Train/Test Processing
        ↓
Preprocessing
        ↓
Trained Churn Model
        ↓
Churn Probability

The trained model is stored as:

models/churn_model.pkl



6. Risk Scoring Flow

Churn probability is transformed into a business-friendly risk score.

Churn Probability
        ↓
Risk Score Calculation
        ↓
0–100 Risk Score
        ↓
Risk Category

Risk categories:

Low
Medium
High
Critical

7. Explainable AI Flow
Customer Features
        ↓
Churn Prediction
        ↓
Model Explanation
        ↓
Important Risk Drivers
        ↓
Customer-Level Explanation

The resulting explanations are available through:

data/final/ai_customer_explanations.csv


8. Recommendation Flow
Customer Risk
       +
Customer Value
       +
Purchase Behavior
       +
Review Behavior
       +
Delivery Experience
       +
Product Preferences
       ↓
Recommendation Rules
       ↓
Retention Action
       ↓
Priority

Example:

High Churn Risk
        +
High Customer Value
        ↓
Immediate Retention Outreach


9. Revenue at Risk Flow
Customer Value
        +
Churn Probability
        ↓
Revenue Exposure
        ↓
Revenue at Risk
        ↓
Risk Prioritization

Customers are prioritized using both:

Risk
  +
Value

rather than churn probability alone.

10. Streamlit Input Flow

When a user uploads a customer dataset:

Upload CSV
    ↓
File Format Validation
    ↓
Schema Validation
    ↓
Required Column Validation
    ↓
Data Preview
    ↓
Preprocessing
    ↓
Prediction

If validation fails:

Invalid File
    ↓
Validation Error
    ↓
User Notification
    ↓
Correct File

11. Streamlit Prediction Flow
Customer Data
      ↓
Preprocessing
      ↓
Churn Model
      ↓
Churn Probability
      ↓
Risk Score
      ↓
Risk Category
      ↓
Retention Recommendation
      ↓
Prediction Results

12. Dashboard Data Flow

The Dashboard consumes prepared AI business intelligence data.

AI Outputs
    ↓
KPI Calculation
    ↓
Risk Aggregation
    ↓
Revenue Aggregation
    ↓
Business Insights
    ↓
Dashboard

Dashboard outputs include:

Total Customers
At-Risk Customers
High/Critical Customers
Revenue at Risk
Risk Distribution
Customer Risk Profile
Business Insights

13. Customer Prediction Data Flow
Uploaded Customer Data
        ↓
Validation
        ↓
Preprocessing
        ↓
Churn Prediction
        ↓
Risk Scoring
        ↓
Risk Categorization
        ↓
Recommendation Generation
        ↓
Prediction Table
        ↓
Download Results


14. AI Insights Data Flow
Customer ID
     ↓
Customer Lookup
     ↓
Prediction
     ↓
Risk Drivers
     ↓
Customer Explanation
     ↓
Customer Behavior
     ↓
Retention Recommendation
     ↓
Business Action


15. Executive Report Data Flow
Prediction Results
        +
Customer Explanations
        +
Revenue Exposure
        +
Business Insights
        ↓
Executive Aggregation
        ↓
Executive KPIs
        ↓
Risk Overview
        ↓
Revenue Exposure
        ↓
Retention Priorities
        ↓
Executive Report


16. Existing Final Data Outputs

The AI layer currently produces:

data/final/


ai_ready_dataset.csv
ai_customer_explanations.csv
executive_summary.csv
business_report_data.csv

These datasets provide the foundation for the Streamlit application.


17. Application Output Flow

The application produces downloadable outputs.

Prediction Results
        ↓
CSV Output
        ↓
data/outputs/
        ↓
User Download

Executive reporting:

Executive Summary
        ↓
Business Report
        ↓
Download



18. Complete End-to-End Data Flow
                    ┌──────────────────┐
                    │    RAW DATA      │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ DATA CLEANING    │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ FEATURE          │
                    │ ENGINEERING      │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ CUSTOMER-LEVEL   │
                    │ DATASET          │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ CHURN MODEL      │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ CHURN            │
                    │ PROBABILITY      │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ RISK SCORE       │
                    └────────┬─────────┘
                             ↓
                    ┌──────────────────┐
                    │ RISK CATEGORY    │
                    └────────┬─────────┘
                             ↓
              ┌──────────────┴──────────────┐
              ↓                             ↓
    ┌──────────────────┐          ┌──────────────────┐
    │ EXPLAINABLE AI   │          │ RECOMMENDATION   │
    └────────┬─────────┘          └────────┬─────────┘
             └──────────────┬──────────────┘
                            ↓
                  ┌──────────────────┐
                  │ BUSINESS IMPACT  │
                  │ & REVENUE RISK   │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │ STREAMLIT APP    │
                  └────────┬─────────┘
                           ↓
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
        Dashboard     AI Insights   Executive Report
             │             │             │
             └─────────────┼─────────────┘
                           ↓
                  Business Decisions


19. Data Governance Considerations

The application should maintain:

Consistent feature definitions
Validated input schemas
Reproducible preprocessing
Consistent model inputs
Clear output definitions
Traceable prediction results
Separation between raw and processed data


20. Data Flow Summary

The platform converts raw transactional information into actionable customer retention intelligence.

Data
 ↓
Features
 ↓
Prediction
 ↓
Risk
 ↓
Explanation
 ↓
Recommendation
 ↓
Business Impact
 ↓
Decision