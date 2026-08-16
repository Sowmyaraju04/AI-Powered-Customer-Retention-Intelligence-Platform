# Application Requirements Document (ARD)

## AI-Powered Customer Retention Intelligence Platform

**Phase:** 10 — Streamlit Web Application
**Document Type:** Application Requirements Document
**Status:** Design
**Application:** AI-Powered Customer Retention Intelligence Platform

---

# 1. Application Overview

The AI-Powered Customer Retention Intelligence Platform is an interactive analytics and AI application designed to help business users identify customers at risk of churn, understand the reasons behind customer risk, prioritize customers based on business value, and determine appropriate retention actions.

The application transforms the outputs of the existing customer analytics, machine learning, retention recommendation, and AI business intelligence pipeline into an accessible business-facing web application.

The platform will provide a centralized interface for:

* Customer churn prediction
* Customer risk scoring
* Explainable AI insights
* Retention recommendations
* Revenue-at-risk analysis
* Executive KPIs
* Business insights
* Report generation and downloads

The application is intended to demonstrate how an end-to-end machine learning and analytics solution can be converted into a practical business decision-support product.

---

# 2. Business Problem

Organizations often identify customer churn only after customers have stopped purchasing.

Traditional reporting primarily answers historical questions such as:

* How many customers purchased?
* How much revenue was generated?
* Which products performed well?
* Which customers have already stopped purchasing?

However, historical reporting alone does not provide sufficient information for proactive retention.

The business requires a system that can identify customers who are likely to churn before the business loses the opportunity to intervene.

The application therefore needs to connect:

**Customer Data → Churn Prediction → Risk Explanation → Customer Prioritization → Retention Action**

---

# 3. Business Objectives

The application should help business stakeholders:

1. Identify customers who are likely to churn.
2. Quantify the probability and severity of customer risk.
3. Understand the major factors contributing to customer risk.
4. Prioritize high-risk customers based on both churn risk and customer value.
5. Recommend appropriate retention actions.
6. Estimate revenue associated with high-risk customers.
7. Provide executives with a concise view of customer retention health.
8. Allow users to download prediction and reporting outputs.
9. Reduce dependence on manual analysis.
10. Demonstrate an end-to-end AI-driven customer retention workflow.

---

# 4. Target Users

The application is designed for multiple business stakeholders.

## 4.1 Executive Leadership

### Primary Needs

* Overall retention health
* Customer risk distribution
* Revenue at risk
* High-level business insights
* Strategic recommendations

### Expected Application Usage

Executives should primarily use the Dashboard and Executive Report pages.

---

## 4.2 Customer Success Team

### Primary Needs

* Identify high-risk customers
* Understand customer-specific risk factors
* Review recommended retention actions
* Prioritize customer outreach

### Expected Application Usage

Customer Success users should primarily use Customer Prediction and AI Insights.

---

## 4.3 Marketing / CRM Team

### Primary Needs

* Identify customer segments requiring intervention
* Understand customer behavior
* Design targeted retention campaigns
* Prioritize high-value customers

### Expected Application Usage

Marketing users should use Customer Prediction, AI Insights, and Executive Report.

---

## 4.4 Business Analysts

### Primary Needs

* Upload customer data
* Run predictions
* Analyze model outputs
* Download results
* Generate business reports

### Expected Application Usage

Business Analysts may use all application sections.

---

# 5. Application Scope

## 5.1 In Scope

The application will include:

* Executive dashboard
* Customer data upload
* Data validation
* Churn prediction
* Churn probability
* Customer risk score
* Risk categorization
* Customer-level explanations
* Retention recommendations
* Revenue-at-risk analysis
* Executive insights
* Downloadable results
* Error handling
* Modular application architecture

---

## 5.2 Out of Scope

The initial version will not include:

* Real-time CRM integration
* Automated email campaigns
* Real-time customer communication
* Online model retraining
* Automated marketing campaign execution
* Production database integration
* Authentication and role-based access control
* Automated cloud infrastructure management

These may be considered future enhancements.

---

# 6. Application Workflow

The primary application workflow is:

```text
User Opens Application
        ↓
Executive Dashboard
        ↓
Upload Customer Data
        ↓
Validate Input
        ↓
Preprocess Data
        ↓
Generate Churn Predictions
        ↓
Calculate Risk Scores
        ↓
Generate Customer Explanations
        ↓
Generate Retention Recommendations
        ↓
Calculate Revenue at Risk
        ↓
Display Business Insights
        ↓
Download Results / Reports
```

---

# 7. Functional Requirements

## FR-01 — Application Launch

The application shall provide a centralized landing/dashboard experience when launched.

The landing experience should communicate:

* Application name
* Business purpose
* Key retention metrics
* Navigation options
* Current analytical context

---

## FR-02 — Dashboard

The Dashboard shall provide an executive-level overview of customer retention.

It should display relevant KPIs such as:

* Total Customers
* Customers at Risk
* High/Critical Risk Customers
* Churn Rate
* Revenue at Risk
* Average Customer Value

The dashboard should also provide visual summaries of:

* Risk distribution
* Customer segments
* Revenue exposure
* Key business insights

---

## FR-03 — Customer Data Upload

The application shall allow authorized users to upload customer-level CSV data.

The upload workflow should:

1. Accept CSV files.
2. Read the uploaded dataset.
3. Validate required columns.
4. Check data types where applicable.
5. Identify missing or invalid values.
6. Provide user-friendly validation messages.

---

## FR-04 — Data Validation

The application shall validate uploaded data before running predictions.

Validation should check:

* File format
* Required columns
* Column names
* Data types
* Missing values
* Invalid values
* Empty datasets
* Duplicate customer records where applicable

Prediction should not proceed when critical validation requirements are not satisfied.

---

## FR-05 — Customer Churn Prediction

The application shall use the trained machine learning model to generate customer churn predictions.

For each customer, the system should generate:

* Predicted churn class
* Churn probability
* Business risk score
* Risk category

---

## FR-06 — Risk Score

The application shall convert model churn probability into a business-friendly risk score.

The risk score should use a standardized 0–100 scale.

Example interpretation:

| Risk Score | Category |
| ---------: | -------- |
|       0–24 | Low      |
|      25–49 | Medium   |
|      50–74 | High     |
|     75–100 | Critical |

The exact thresholds should remain configurable.

---

## FR-07 — Customer-Level Explanation

The application shall provide explanations for customer-level predictions.

The explanation should communicate:

* Customer risk level
* Main contributing factors
* Important behavioral indicators
* Business interpretation

Where available, explanations should be derived from the existing explainable AI outputs rather than generated independently by the UI.

---

## FR-08 — Retention Recommendations

The application shall provide recommended retention actions based on customer characteristics and risk.

Recommendations may include:

* Loyalty incentives
* Personalized offers
* Customer support outreach
* Discount campaigns
* Cross-sell opportunities
* Upsell opportunities
* Service recovery actions

Recommendations should be presented as actionable business decisions rather than raw model outputs.

---

## FR-09 — Customer Prioritization

The application shall allow users to identify customers requiring immediate attention.

Prioritization should consider both:

* Churn risk
* Customer/business value

This prevents the business from treating every high-risk customer as equally important.

---

## FR-10 — Revenue at Risk

The application shall estimate the revenue associated with customers who are at elevated churn risk.

The system should provide:

* Total revenue at risk
* High-risk customer value
* Critical-risk customer value
* Customer-level revenue exposure where available

---

## FR-11 — AI Insights

The application shall display business insights derived from the existing AI Business Intelligence outputs.

Insights should focus on:

* Customer risk
* Revenue exposure
* Customer behavior
* Retention opportunities
* Business priorities

The application should distinguish between analytical findings and recommendations.

---

## FR-12 — Executive Report

The application shall provide an executive reporting interface.

The report should summarize:

* Customer base
* Churn exposure
* Risk distribution
* Revenue at risk
* Key insights
* Recommended business actions

---

## FR-13 — Download Results

Users shall be able to download relevant analytical outputs.

Potential downloadable outputs include:

* Customer prediction results
* Risk scores
* Customer explanations
* Retention recommendations
* Executive summary
* Business report data

---

# 8. Input Requirements

The primary input is a customer-level CSV dataset compatible with the existing machine learning pipeline.

The expected dataset should contain the features required by the trained model.

Potential examples include:

* Customer identifier
* Recency
* Frequency
* Monetary value
* Customer tenure
* Average order value
* Review-related features
* Delivery-related features
* Product behavior
* Payment behavior
* Other engineered customer-level features

The exact required schema must be aligned with the feature set used during model training.

---

# 9. Existing AI Outputs

The application will leverage existing outputs generated during previous project phases.

Current available datasets include:

```text
data/final/

├── ai_ready_dataset.csv
├── ai_customer_explanations.csv
├── executive_summary.csv
└── business_report_data.csv
```

These outputs will serve different application purposes.

### ai_ready_dataset.csv

Used for customer-level AI and prediction-related analysis.

### ai_customer_explanations.csv

Used for customer-level explainability and risk interpretation.

### executive_summary.csv

Used for executive KPIs and high-level reporting.

### business_report_data.csv

Used for business insights, reporting, and downloadable outputs.

---

# 10. Output Requirements

For each processed customer, the application should be capable of presenting:

```text
Customer ID
       ↓
Churn Probability
       ↓
Risk Score
       ↓
Risk Category
       ↓
Key Risk Factors
       ↓
Recommended Retention Action
       ↓
Customer Value / Revenue Exposure
```

At the aggregate level, the application should provide:

* Customer counts
* Risk distribution
* Churn metrics
* Revenue at risk
* Customer segments
* Business insights
* Retention priorities

---

# 11. Risk Categories

The application will use business-friendly risk categories.

| Category | Business Meaning                                      |
| -------- | ----------------------------------------------------- |
| Low      | Customer currently presents relatively low churn risk |
| Medium   | Customer should be monitored                          |
| High     | Customer requires proactive retention attention       |
| Critical | Customer represents significant retention priority    |

Risk thresholds should be configurable rather than hardcoded throughout the application.

---

# 12. Non-Functional Requirements

## NFR-01 — Usability

The application should be understandable to non-technical business users.

Users should not need Python, SQL, or machine learning knowledge to operate the application.

---

## NFR-02 — Performance

The application should minimize unnecessary computation.

Expensive operations such as model loading should be cached where appropriate.

---

## NFR-03 — Reliability

The application should gracefully handle:

* Invalid uploads
* Missing columns
* Incorrect file formats
* Empty datasets
* Prediction failures
* Missing model files

---

## NFR-04 — Maintainability

The application should use modular architecture.

UI components, prediction logic, preprocessing, model loading, and recommendation logic should remain separated.

---

## NFR-05 — Scalability

The application architecture should allow future integration with:

* Databases
* APIs
* Cloud storage
* CRM platforms
* Real-time prediction services

---

## NFR-06 — Explainability

Predictions should be accompanied by understandable explanations whenever explainability data is available.

The system should avoid presenting model predictions as unquestionable business decisions.

---

## NFR-07 — Consistency

The preprocessing applied during prediction must remain consistent with the preprocessing used during model training.

This is critical for avoiding training-serving skew.

---

# 13. Business KPIs

The application should monitor metrics relevant to customer retention.

Primary KPIs include:

* Total Customers
* Total At-Risk Customers
* High-Risk Customers
* Critical-Risk Customers
* Churn Rate
* Revenue at Risk
* Average Customer Value
* High-Value At-Risk Customers
* Retention Opportunity

Secondary metrics may include:

* Average Order Value
* Customer Frequency
* Customer Recency
* Customer Tenure
* Average Review Score

---

# 14. Success Criteria

The application will be considered successful when a business user can:

1. Open the application.
2. Understand the current retention situation.
3. Upload compatible customer data.
4. Validate the uploaded dataset.
5. Generate churn predictions.
6. Identify high-risk customers.
7. Understand why customers are at risk.
8. View recommended retention actions.
9. Understand potential revenue exposure.
10. Download actionable results.

The application should accomplish these tasks without requiring the user to interact directly with Python code or machine learning infrastructure.

---

# 15. Assumptions

The application assumes:

* The trained churn model is available.
* Required model features are known.
* Uploaded data follows the expected schema.
* Existing AI outputs are generated correctly.
* The customer-level analytical dataset represents the required modeling granularity.
* The model is used for decision support rather than fully automated decision-making.

---

# 16. Constraints

Current project constraints include:

* The application is built using Streamlit.
* The primary data source is the Brazilian E-Commerce Olist dataset.
* The initial version uses prepared CSV-based outputs.
* The machine learning model has already been trained.
* No real-time CRM integration is currently available.
* No production database is currently required.
* The application is primarily a portfolio demonstration of an enterprise analytics product.

---

# 17. Risks

## Risk 1 — Input Schema Mismatch

Uploaded files may not contain the features required by the model.

**Mitigation:** Implement strict schema validation before prediction.

---

## Risk 2 — Training/Serving Data Mismatch

The preprocessing applied to uploaded data may differ from training preprocessing.

**Mitigation:** Centralize preprocessing logic and reuse the same transformations.

---

## Risk 3 — Model Interpretability

Business users may misunderstand probability as certainty.

**Mitigation:** Present predictions as risk estimates and provide explanations.

---

## Risk 4 — Over-Reliance on Recommendations

Users may treat automated recommendations as guaranteed outcomes.

**Mitigation:** Present recommendations as decision-support suggestions.

---

## Risk 5 — Model Performance Degradation

Model performance may change when applied to future data.

**Mitigation:** Future versions should include model monitoring and periodic retraining.

---

# 18. Future Enhancements

Potential future versions may include:

* User authentication
* Role-based access control
* Database integration
* CRM integration
* Real-time predictions
* Automated campaign triggering
* Customer communication workflows
* Model monitoring
* Drift detection
* Automated model retraining
* A/B testing of retention strategies
* Customer lifetime value modeling
* Real-time dashboards
* Cloud deployment
* API-based prediction service

---

# 19. Application Modules

The Streamlit application will contain four primary user-facing modules.

## Module 1 — Dashboard

Purpose:

Provide an executive-level overview of customer retention health.

---

## Module 2 — Customer Prediction

Purpose:

Allow users to upload customer data and generate churn predictions.

---

## Module 3 — AI Insights

Purpose:

Explain customer risk and provide retention recommendations.

---

## Module 4 — Executive Report

Purpose:

Translate analytical outputs into executive-level business reporting.

---

# 20. High-Level Application Architecture

```text
                    BUSINESS USER
                         │
                         ▼
                STREAMLIT APPLICATION
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
    Dashboard       Prediction       AI Insights
        │                │                │
        │                ▼                │
        │          Preprocessing         │
        │                │                │
        │                ▼                │
        │          ML Model              │
        │                │                │
        │                ▼                │
        │          Risk Score            │
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼
                Recommendation Engine
                         │
                         ▼
                  Executive Reporting
                         │
                         ▼
                    Downloads
```

---

# 21. Design Principles

The application should follow these principles:

### Business First

Every feature must support a real business decision.

### Explainability

Predictions should be understandable.

### Actionability

Insights should lead to possible actions.

### Simplicity

Complex machine learning processes should be hidden behind a simple user interface.

### Modularity

Each technical responsibility should remain isolated.

### Maintainability

The application should be easy to modify and extend.

### Enterprise Thinking

The architecture should be designed with future integration and scalability in mind.

---

# 22. Hiring Manager Perspective

A strong implementation of these requirements demonstrates more than Streamlit knowledge.

It demonstrates the ability to:

* Translate business requirements into technical requirements.
* Design a user-oriented analytics product.
* Integrate machine learning into an application.
* Communicate model outputs to non-technical stakeholders.
* Connect predictive analytics with business actions.
* Design modular software architecture.
* Think about production risks and scalability.

This is the difference between demonstrating:

> "I built a churn model."

and demonstrating:

> "I designed and implemented an AI-powered customer retention decision-support platform."

---

# 23. Requirement Traceability

The major requirements map to the application as follows:

| Requirement               | Application Component         |
| ------------------------- | ----------------------------- |
| Executive KPIs            | Dashboard                     |
| Risk distribution         | Dashboard                     |
| Customer upload           | Customer Prediction           |
| Data validation           | Prediction utilities          |
| Churn prediction          | Prediction utilities          |
| Risk scoring              | Prediction utilities          |
| Customer explanations     | AI Insights                   |
| Retention recommendations | AI Insights                   |
| Revenue at risk           | Executive Report              |
| Business insights         | Executive Report              |
| Downloads                 | Prediction / Executive Report |

---

# 24. Final Product Definition

The AI-Powered Customer Retention Intelligence Platform will serve as a business decision-support application that connects historical customer analytics, predictive machine learning, explainable AI, and prescriptive retention recommendations.

The final product should enable a business user to move from:

**"Which customers are at risk?"**

to:

**"Why are they at risk?"**

and ultimately:

**"What should we do about it?"**

This represents the transition from:

**Descriptive Analytics → Diagnostic Analytics → Predictive Analytics → Prescriptive Analytics**

and forms the core product objective of Phase 10.
