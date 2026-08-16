# User Journey

## AI-Powered Customer Retention Intelligence Platform

**Phase:** 10 — Streamlit Web Application
**Document Type:** User Journey Specification
**Status:** Design

---

# 1. Purpose

This document defines how users interact with the AI-Powered Customer Retention Intelligence Platform from application entry to business decision-making.

The purpose of the user journey is to ensure that the application is designed around **business decisions and user needs**, rather than simply displaying technical model outputs.

The primary journey is:


Access Application
        ↓
Understand Business Situation
        ↓
Analyze Customer Risk
        ↓
Predict Churn
        ↓
Understand Customer Risk
        ↓
Determine Retention Action
        ↓
Assess Business Impact
        ↓
Download Results


---

# 2. Overall User Journey

The platform follows a decision-support workflow:

                    USER
                     │
                     ▼
             Open Application
                     │
                     ▼
               Dashboard
                     │
                     ▼
          Understand Retention Health
                     │
                     ▼
          Customer Prediction Page
                     │
                     ▼
              Upload CSV
                     │
                     ▼
             Validate Dataset
                │         │
             Valid       Invalid
                │         │
                ▼         ▼
        Run Prediction   Fix Input
                │
                ▼
         Churn Probability
                │
                ▼
           Risk Score
                │
                ▼
        Risk Categorization
                │
                ▼
          AI Insights
                │
        ┌───────┴────────┐
        ▼                ▼
 Risk Explanation   Recommendation
        │                │
        └───────┬────────┘
                ▼
        Executive Report
                │
                ▼
         Revenue at Risk
                │
                ▼
        Business Priorities
                │
                ▼
         Download Results


---

# 3. Primary User Journey

## Stage 1 — Application Entry

### User Goal

Understand what the application does and quickly access the most important retention information.

### User Action

The user opens the Streamlit application.

### System Response

The application displays:

* Application name
* Application purpose
* Executive KPIs
* Customer risk overview
* Navigation menu

### Expected Outcome

The user immediately understands the current customer retention situation.

---

# 4. Stage 2 — Dashboard Exploration

## User Goal

Understand the overall health of the customer base.

### User Actions

The user reviews:

* Total customers
* Churn rate
* At-risk customers
* High-risk customers
* Critical-risk customers
* Revenue at risk

The user may also review charts showing:

* Risk distribution
* Customer segments
* Revenue exposure
* Key business insights

### System Response

The dashboard converts analytical outputs into executive-level information.

### Decision

The user determines whether customer retention requires immediate attention.

---

# 5. Stage 3 — Customer Data Upload

## User Goal

Analyze a new customer dataset.

### User Action

The user navigates to:

**Customer Prediction**

and uploads a CSV file.

### System Response

The system:

1. Accepts the uploaded file.
2. Reads the dataset.
3. Checks the file format.
4. Validates required columns.
5. Checks data quality.
6. Displays validation results.

### Decision Point


Is the dataset valid?
       │
   ┌───┴───┐
   │       │
  YES      NO
   │       │
   ▼       ▼
Proceed   Display
         Validation
           Errors




# 6. Stage 4 — Data Validation

## Valid Dataset

If the dataset satisfies all critical requirements:

The system displays:

**Dataset validated successfully.**

The user can proceed to prediction.

## Invalid Dataset

If validation fails:

The system displays:

* Error description
* Missing columns
* Invalid fields
* Required corrections

The user must correct the dataset before continuing.

### Business Benefit

Validation prevents unreliable predictions caused by incompatible input data.

---

# 7. Stage 5 — Churn Prediction

## User Goal

Identify customers who are likely to churn.

### User Action

The user selects:

**Run Prediction**

### System Process


Uploaded Data
      ↓
Preprocessing
      ↓
Feature Preparation
      ↓
Machine Learning Model
      ↓
Churn Probability
      ↓
Risk Score
      ↓
Risk Category


### System Output

For each customer:

* Customer ID
* Churn probability
* Risk score
* Risk category

---

# 8. Stage 6 — Risk Analysis

## User Goal

Identify which customers require attention.

### User Actions

The user reviews:

* Low-risk customers
* Medium-risk customers
* High-risk customers
* Critical-risk customers

The user may filter or sort customers based on:

* Risk score
* Churn probability
* Customer value
* Revenue exposure

### Decision

The user identifies priority customers.

---

# 9. Stage 7 — Customer Explanation

## User Goal

Understand why a customer is considered at risk.

### User Action

The user selects a customer or customer segment.

### System Response

The AI Insights page displays:

* Customer risk level
* Churn probability
* Major risk factors
* Behavioral indicators
* Business interpretation

Example structure:


Customer
   ↓
Critical Risk
   ↓
High Recency
   ↓
Low Purchase Frequency
   ↓
Poor Delivery Experience
   ↓
Retention Intervention Recommended


### Business Benefit

Users can move beyond:

> "The model says this customer is risky."

to:

> "The customer is risky because of specific observable behaviors."

---

# 10. Stage 8 — Retention Recommendation

## User Goal

Determine what action should be taken.

### System Response

The recommendation engine evaluates factors such as:

* Churn risk
* Customer value
* Purchase history
* Review behavior
* Delivery experience
* Product preferences

It produces an appropriate retention recommendation.

Potential recommendations include:

* Loyalty reward
* Personalized offer
* Discount campaign
* Customer support outreach
* Service recovery
* Cross-sell
* Upsell

### Decision

The business user determines whether the recommendation is appropriate for the customer.

---

# 11. Stage 9 — Revenue-at-Risk Analysis

## User Goal

Understand the financial impact of customer churn risk.

### User Action

The user navigates to the Executive Report.

### System Response

The application summarizes:

* Total revenue at risk
* Revenue from high-risk customers
* Revenue from critical-risk customers
* High-value customers at risk

### Business Question

The system should help answer:

> "How much business could potentially be affected if high-risk customers are not retained?"

---

# 12. Stage 10 — Executive Decision

## User Goal

Translate analytics into strategic action.

### Executive reviews:

* Customer retention KPIs
* Risk distribution
* Revenue at risk
* High-value at-risk customers
* Major risk drivers
* Recommended actions

### Executive Decision

Possible decisions include:

* Increase retention investment.
* Prioritize high-value customers.
* Launch targeted campaigns.
* Improve customer support.
* Investigate delivery issues.
* Develop loyalty initiatives.

---

# 13. Stage 11 — Download Results

## User Goal

Take analytical outputs outside the application.

### Available Downloads

Depending on the workflow, users may download:

* Customer predictions
* Risk scores
* Customer explanations
* Retention recommendations
* Executive summary
* Business report data

### Final Outcome

The user receives an actionable dataset that can be used for:

* CRM analysis
* Marketing campaigns
* Customer Success outreach
* Management reporting
* Further analysis

---

# 14. Executive User Journey

The executive journey should be intentionally short.


Open Application
       ↓
Dashboard
       ↓
Review KPIs
       ↓
Review Risk Distribution
       ↓
Review Revenue at Risk
       ↓
Review Key Insights
       ↓
Executive Report
       ↓
Make Strategic Decision


Executives should not need to interact with technical model details unless required.

---

# 15. Customer Success User Journey


Open Application
       ↓
Dashboard
       ↓
Customer Prediction
       ↓
Review High/Critical Risk Customers
       ↓
Select Customer
       ↓
View Risk Explanation
       ↓
View Recommended Action
       ↓
Prioritize Outreach
       ↓
Download Customer List


The primary objective is **customer-level intervention**.

---

# 16. Marketing / CRM User Journey


Open Application
       ↓
Dashboard
       ↓
Customer Prediction
       ↓
Segment At-Risk Customers
       ↓
Analyze Customer Value
       ↓
Review Risk Drivers
       ↓
Review Recommendations
       ↓
Prioritize Campaign Audience
       ↓
Download Customer Segment


The primary objective is **targeted retention campaigns**.

---

# 17. Business Analyst Journey


Open Application
       ↓
Customer Prediction
       ↓
Upload Dataset
       ↓
Validate Dataset
       ↓
Run Prediction
       ↓
Review Results
       ↓
Analyze AI Insights
       ↓
Review Revenue Impact
       ↓
Download Results


The primary objective is **analysis and decision support**.

---

# 18. Error Journey

The application must also support unsuccessful journeys.

## Scenario 1 — Invalid File


Upload File
     ↓
Validation
     ↓
Invalid
     ↓
Display Error
     ↓
User Corrects File
     ↓
Upload Again


---

## Scenario 2 — Missing Required Columns


Upload Dataset
     ↓
Schema Validation
     ↓
Required Column Missing
     ↓
Display Missing Column
     ↓
User Corrects Dataset


---

## Scenario 3 — Empty Dataset


Upload CSV
     ↓
Dataset Empty
     ↓
Display Warning
     ↓
Request Valid Dataset


---

## Scenario 4 — Model Unavailable


Run Prediction
     ↓
Model Loading Failure
     ↓
Display User-Friendly Error
     ↓
Prevent Prediction


Technical stack traces should not be exposed directly to business users.

---

# 19. User Decision Points

The major decision points in the application are:

| Stage            | Decision                                        |
| ---------------- | ----------------------------------------------- |
| Dashboard        | Is retention risk significant?                  |
| Upload           | Is the dataset valid?                           |
| Prediction       | Which customers are at risk?                    |
| Risk Analysis    | Which customers should be prioritized?          |
| AI Insights      | Why are they at risk?                           |
| Recommendations  | What action should be taken?                    |
| Revenue Analysis | What is the potential business impact?          |
| Executive Report | What strategic action should the business take? |

---

# 20. User Journey Success Criteria

The journey is successful when a user can move from:

DATA
 ↓
RISK
 ↓
EXPLANATION
 ↓
ACTION
 ↓
BUSINESS IMPACT


without requiring technical knowledge of:

* Python
* Machine learning
* SQL
* Feature engineering
* Model internals

The application should hide technical complexity while exposing the information required for business decisions.

---

# 21. Core Product Journey

The most important product journey can be summarized as:


                 CUSTOMER DATA
                       │
                       ▼
                CHURN PREDICTION
                       │
                       ▼
                 RISK SCORE
                       │
                       ▼
               WHY AT RISK?
                       │
                       ▼
             WHAT SHOULD WE DO?
                       │
                       ▼
               REVENUE IMPACT
                       │
                       ▼
               BUSINESS ACTION


This represents the central value proposition of the platform:

> **Identify → Explain → Prioritize → Act → Measure**

---

# 22. Final User Experience Principle

The application should never force users to interpret raw machine learning outputs.

Instead, the platform should progressively translate technical outputs into business decisions:

Model Output
     ↓
Risk Score
     ↓
Business Interpretation
     ↓
Recommended Action
     ↓
Financial Impact

The final user experience should therefore feel like a **customer retention decision-support platform**, rather than a machine learning demonstration.
