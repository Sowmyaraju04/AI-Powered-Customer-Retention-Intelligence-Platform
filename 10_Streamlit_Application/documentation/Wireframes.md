# Wireframes

## AI-Powered Customer Retention Intelligence Platform

**Phase:** 10 — Streamlit Web Application  
**Document Type:** Low-Fidelity UI Wireframe Specification  
**Status:** Design

---

# 1. Purpose

This document defines the low-fidelity user interface structure of the AI-Powered Customer Retention Intelligence Platform.

The wireframes provide the blueprint for the Streamlit application before implementation begins.

The purpose is to determine:

- What users see
- Where information appears
- How users navigate
- Which business questions each page answers
- Which actions users can perform
- Which visualizations are required
- Where filters and downloads should appear

The application will contain four primary pages:

1. Dashboard
2. Customer Prediction
3. AI Insights
4. Executive Report

---

# 2. Global Application Layout

All application pages should follow a consistent structure.

┌────────────────────────────────────────────────────────────────────┐
│                         APPLICATION HEADER                         │
│       AI-Powered Customer Retention Intelligence Platform          │
├────────────────┬───────────────────────────────────────────────────┤
│                │                                                   │
│   SIDEBAR      │                    PAGE CONTENT                   │
│                │                                                   │
│  🏠 Dashboard  │                                                   │
│                │                                                   │
│  🎯 Prediction │                                                   │
│                │                                                   │
│  🤖 AI Insights│                                                   │
│                │                                                   │
│  📊 Exec Report│                                                   
│                │                                                   │
│                │                                                   │
│                │                                                   │
├────────────────┴───────────────────────────────────────────────────┤
│                         FOOTER / STATUS                            │
└────────────────────────────────────────────────────────────────────┘


┌──────────────────────────┐
│   RETENTION INTELLIGENCE │
│        PLATFORM          │
├──────────────────────────┤
│                          │
│  🏠 Dashboard            │
│                          │
│  🎯 Customer Prediction  │
│                          │
│  🤖 AI Insights          │
│                          │
│  📊 Executive Report     │
│                          │
├──────────────────────────┤
│                          │
│  MODEL STATUS            │
│  ● Model Available       │
│                          │
│  DATA STATUS             │
│  ● Data Available        │
│                          │
└──────────────────────────┘

┌────────────────────────────────────────────────────────────────────┐
│                    CUSTOMER RETENTION OVERVIEW                     │
│                                                                    │
│ Monitor customer churn risk, customer exposure and revenue risk. │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│ ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌─────────────────┐ │
│ │   TOTAL    │ │  AT-RISK   │ │ HIGH /     │ │ REVENUE AT RISK │ │
│ │ CUSTOMERS  │ │ CUSTOMERS  │ │ CRITICAL   │ │                 │ │
│ │            │ │            │ │ CUSTOMERS  │ │      VALUE      │ │
│ │   VALUE    │ │   VALUE    │ │   VALUE    │ │                 │ │
│ └────────────┘ └────────────┘ └────────────┘ └─────────────────┘ │
│                                                                    │
├────────────────────────────────┬───────────────────────────────────┤
│                                │                                   │
│       RISK DISTRIBUTION        │       CUSTOMER RISK PROFILE       │
│                                │                                   │
│           [CHART]              │             [CHART]               │
│                                │                                   │
├────────────────────────────────┴───────────────────────────────────┤
│                                                                    │
│                       REVENUE AT RISK                              │
│                                                                    │
│                            [CHART]                                 │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│                      KEY BUSINESS INSIGHTS                         │
│                                                                    │
│ ┌──────────────────┐ ┌──────────────────┐ ┌─────────────────────┐ │
│ │ Insight 1        │ │ Insight 2        │ │ Insight 3           │ │
│ │                  │ │                  │ │                     │ │
│ └──────────────────┘ └──────────────────┘ └─────────────────────┘ │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

┌────────────────┐
│ TOTAL CUSTOMERS│
│                │
│     VALUE      │
└────────────────┘

┌────────────────┐
│ AT-RISK        │
│ CUSTOMERS      │
│                │
│     VALUE      │
└────────────────┘

┌────────────────┐
│ HIGH / CRITICAL│
│ CUSTOMERS      │
│                │
│     VALUE      │
└────────────────┘

┌────────────────┐
│ REVENUE AT RISK│
│                │
│     VALUE      │
└────────────────┘

Customer Risk Distribution

Low       ███████████████████
Medium    ███████████
High      ███████
Critical  ████

Customer Risk
      ↓
Customer Value
      ↓
Revenue Exposure

Revenue at Risk by Risk Category

Low        ███
Medium     █████
High       █████████
Critical   █████████████

Finding
   ↓
Business Meaning
   ↓
Potential Action
Example:
┌──────────────────────────────────────────────┐
│ HIGH-VALUE CUSTOMERS AT RISK                 │
│                                              │
│ High-value customers represent significant   │
│ revenue exposure.                            │
│                                              │
│ Action: Prioritize proactive retention.      │
└──────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────┐
│                       CUSTOMER PREDICTION                          │
│                                                                    │
│ Upload customer data and generate churn risk predictions.        │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│                         DATA UPLOAD                                │
│                                                                    │
│       ┌──────────────────────────────────────────┐                 │
│       │                                          │                 │
│       │          Drag & Drop CSV File            │                 │
│       │                                          │                 │
│       │             [ Browse Files ]             │                 │
│       │                                          │                 │
│       └──────────────────────────────────────────┘                 │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                       DATA VALIDATION                              │
│                                                                    │
│ Records: XXXX     Columns: XX     Status: ✓ Valid                 │
│                                                                    │
│                  [ View Validation Details ]                       │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                         PREDICTION                                 │
│                                                                    │
│                     [ RUN PREDICTION ]                             │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                     PREDICTION SUMMARY                             │
│                                                                    │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐│
│ │ TOTAL    │ │ LOW      │ │ MEDIUM   │ │ HIGH     │ │ CRITICAL ││
│ │ CUSTOMERS│ │ RISK     │ │ RISK     │ │ RISK     │ │ RISK     ││
│ │          │ │          │ │          │ │          │ │          ││
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘│
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                       CUSTOMER RESULTS                             │
│                                                                    │
│ Risk: [All ▼]   Value: [All ▼]   Search: [____________]           │
│                                                                    │
│ ┌─────────┬──────────┬──────────┬──────────┬────────────────────┐ │
│ │Customer │ Churn    │ Risk     │ Risk     │ Recommendation     │ │
│ │ID       │Probability│ Score   │ Category │                    │ │
│ ├─────────┼──────────┼──────────┼──────────┼────────────────────┤ │
│ │ ...     │ ...      │ ...      │ ...      │ ...                │ │
│ └─────────┴──────────┴──────────┴──────────┴────────────────────┘ │
│                                                                    │
│                    [ DOWNLOAD RESULTS ]                            │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘


Upload CSV
     ↓
Validate File
     ↓
Validate Schema
     ↓
Preview Data
     ↓
Run Prediction
     ↓
Generate Churn Probability
     ↓
Calculate Risk Score
     ↓
Assign Risk Category
     ↓
Generate Recommendation
     ↓
Display Results
     ↓
Download Results

Risk Category

[ All ▼ ]

Low
Medium
High
Critical

Customer Value
[ All ▼ ]


Low Value
Medium Value
High Value

Customer Search
Search Customer ID: [________________]

[ DOWNLOAD PREDICTION RESULTS ]

┌────────────────────────────────────────────────────────────────────┐
│                         AI INSIGHTS                                │
│                                                                    │
│ Understand customer risk, drivers and recommended actions.       │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│ Customer ID: [____________________]       [ SEARCH ]              │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                       CUSTOMER PROFILE                             │
│                                                                    │
│ ┌─────────────────┐ ┌─────────────────┐ ┌────────────────────────┐│
│ │ CUSTOMER ID     │ │ RISK SCORE      │ │ RISK CATEGORY          ││
│ │                 │ │                 │ │                        ││
│ └─────────────────┘ └─────────────────┘ └────────────────────────┘│
│                                                                    │
├────────────────────────────────┬───────────────────────────────────┤
│                                │                                   │
│          WHY AT RISK?          │       CUSTOMER BEHAVIOR           │
│                                │                                   │
│ • Risk Factor 1                │             [CHART]               │
│ • Risk Factor 2                │                                   │
│ • Risk Factor 3                │                                   │
│                                │                                   │
├────────────────────────────────┴───────────────────────────────────┤
│                                                                    │
│                    RETENTION RECOMMENDATION                        │
│                                                                    │
│ ┌────────────────────────────────────────────────────────────────┐ │
│ │ Recommended Action                                             │ │
│ │                                                                │ │
│ │ Business Reasoning                                             │ │
│ │                                                                │ │
│ │ Priority: HIGH                                                │ │
│ └────────────────────────────────────────────────────────────────┘ │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                       CUSTOMER VALUE                               │
│                                                                    │
│ Customer Value: XXXXX                                             │
│ Revenue Exposure: XXXXX                                           │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘

Customer ID

[________________________]

       [ SEARCH ]

       The recommendation section should communicate:

Recommended Action
        ↓
Business Reason
        ↓
Priority

Example:

┌──────────────────────────────────────────────┐
│ RECOMMENDED ACTION                           │
│                                              │
│ Customer Support Outreach                    │
│                                              │
│ Reason: Customer shows elevated churn risk   │
│ combined with negative experience signals.   │
│                                              │
│ Priority: HIGH                               │
└──────────────────────────────────────────────┘



┌────────────────────────────────────────────────────────────────────┐
│                        EXECUTIVE REPORT                            │
│                                                                    │
│                  Customer Retention Summary                       │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│ ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌──────────────────────┐│
│ │ CUSTOMERS│ │ CHURN    │ │ REVENUE    │ │ HIGH-VALUE CUSTOMERS ││
│ │          │ │ RISK     │ │ AT RISK    │ │ AT RISK              ││
│ │          │ │          │ │            │ │                      ││
│ └──────────┘ └──────────┘ └────────────┘ └──────────────────────┘│
│                                                                    │
├────────────────────────────────┬───────────────────────────────────┤
│                                │                                   │
│        RISK OVERVIEW           │       REVENUE EXPOSURE            │
│                                │                                   │
│           [CHART]              │             [CHART]               │
│                                │                                   │
├────────────────────────────────┴───────────────────────────────────┤
│                                                                    │
│                     KEY BUSINESS INSIGHTS                          │
│                                                                    │
│  1. Insight                                                        │
│  2. Insight                                                        │
│  3. Insight                                                        │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│                     RETENTION PRIORITIES                           │
│                                                                    │
│  Priority 1 → Action                                               │
│  Priority 2 → Action                                               │
│  Priority 3 → Action                                               │
│                                                                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│                         REPORT DOWNLOADS                           │
│                                                                    │
│ [ DOWNLOAD EXECUTIVE SUMMARY ]                                     │
│                                                                    │
│ [ DOWNLOAD BUSINESS REPORT ]                                       │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘


Executive Insights

Executive insights should follow:

Finding
   ↓
Business Meaning
   ↓
Recommended Action

Example:

Finding:
High-value customers are concentrated within elevated-risk groups.


Business Meaning:
Churn among these customers may have a disproportionate financial impact.


Action:
Prioritize high-value, high-risk customers for proactive retention.

Retention Priorities

The Executive Report should identify the most important retention priorities.

Example:

Priority 1
High-value + High-risk customers


        ↓


Immediate proactive retention outreach
Priority 2
Medium-value + High-risk customers


        ↓


Targeted retention campaign
Priority 3
Low-risk customers


        ↓


Maintain relationship and monitor behavior

                         CUSTOMER VALUE
                    LOW                HIGH
               ┌────────────────┬────────────────┐
HIGH RISK      │    MONITOR     │   PRIORITIZE   │
               │                │   IMMEDIATELY  │
               ├────────────────┼────────────────┤
LOW RISK       │   LOW PRIORITY │    MAINTAIN    │
               │                │   RELATIONSHIP │
               └────────────────┴────────────────┘
┌──────────────────────────┐
│ KPI TITLE                │
│                          │
│       KPI VALUE          │
│                          │
│ Optional comparison      │
└──────────────────────────┘

┌──────────────────────────────────────┐
│ INSIGHT TITLE                        │
│                                      │
│ Business Finding                     │
│                                      │
│ Recommended Action                   │
└──────────────────────────────────────┘

┌──────────────────────────────────────┐
│ RETENTION RECOMMENDATION             │
│                                      │
│ Recommended Action                   │
│                                      │
│ Reason                               │
│                                      │
│ Priority: HIGH                       │
└──────────────────────────────────────┘


                     APPLICATION
                          │
                          ▼
                    DASHBOARD
                          │
                          ▼
              Understand Overall Risk
                          │
                          ▼
               CUSTOMER PREDICTION
                          │
                          ▼
                 Upload Customer Data
                          │
                          ▼
                    Validate Data
                          │
                          ▼
                 Generate Prediction
                          │
                          ▼
                  Review Risk Scores
                          │
                          ▼
                    AI INSIGHTS
                          │
                          ▼
                Select Customer
                          │
                          ▼
                 Understand Risk
                          │
                          ▼
               Review Explanation
                          │
                          ▼
             Review Recommendation
                          │
                          ▼
                EXECUTIVE REPORT
                          │
                          ▼
              Understand Business Impact
                          │
                          ▼
                 Prioritize Actions


┌─────────────────────────────────────────────┐
│                                             │
│   AI-POWERED CUSTOMER RETENTION PLATFORM    │
│                                             │
│   Identify churn risk. Understand why.      │
│   Take proactive retention actions.         │
│                                             │
│              [ GET STARTED ]                │
│                                             │
└─────────────────────────────────────────────┘

Processing customer data...

✓ Validating input
✓ Preparing features
⏳ Generating predictions
○ Calculating recommendations
○ Preparing results

✓ Prediction completed successfully

Customers processed: XXXX

Risk distribution available.

[ VIEW RESULTS ]

[ DOWNLOAD RESULTS ]

⚠ DATA VALIDATION FAILED

The uploaded file is missing required information.

Please review the required columns and upload
a valid customer-level dataset.

Customer Data
      ↓
Prediction
      ↓
Risk Score
      ↓
Recommendation
      ↓
[ DOWNLOAD CSV ]

Customer
    ↓
Prediction
    ↓
Explanation
    ↓
Recommendation
    ↓
[ DOWNLOAD ]

Executive KPIs
      ↓
Business Insights
      ↓
Revenue Exposure
      ↓
Retention Priorities
      ↓
[ DOWNLOAD EXECUTIVE SUMMARY ]

┌──────────────────────────────────────────┐
│               DASHBOARD                  │
│                                          │
│        What is happening?                │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────┐
│          CUSTOMER PREDICTION             │
│                                          │
│        Who is at risk?                   │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────┐
│              AI INSIGHTS                 │
│                                          │
│        Why are they at risk?             │
│        What should we do?                │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────┐
│           EXECUTIVE REPORT               │
│                                          │
│        What is the business impact?      │
│        What should leadership prioritize?│
└──────────────────────────────────────────┘