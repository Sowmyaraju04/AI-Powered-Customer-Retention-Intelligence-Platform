# AI-Powered Customer Retention Intelligence Platform

An end-to-end **AI-powered customer retention and churn intelligence platform** built using the Brazilian E-Commerce (Olist) dataset.

The platform combines **data analytics, customer segmentation, feature engineering, machine learning, explainable AI, retention recommendations, and an interactive Streamlit application** to transform raw e-commerce transaction data into actionable customer retention intelligence.

> **🚀 Live Demo:** https://ai-powered-customer-retention-intelligence-platform-xbk5vzn4kd.streamlit.app/

---

## 📌 Project Overview

Customer churn is one of the major challenges faced by e-commerce businesses. Identifying customers who are likely to disengage is not enough — businesses also need to understand **why customers are at risk and what action should be taken**.

This project addresses that problem by building an end-to-end customer retention intelligence platform.

The solution follows the complete analytics lifecycle:

```text
Raw E-Commerce Data
        ↓
Data Quality Assessment
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Customer Behavior Analysis
        ↓
Churn Prediction
        ↓
Model Interpretation
        ↓
Retention Recommendations
        ↓
AI-Powered Business Insights
        ↓
Interactive Streamlit Application
```

---

## 🎯 Business Problem

E-commerce businesses generate large amounts of customer, order, payment, product, seller, delivery, and review data.

However, raw transactional data does not directly answer critical business questions such as:

* Which customers are at high risk of churn?
* Which customer behaviors indicate potential disengagement?
* What factors contribute to customer churn?
* Which customers should the business prioritize?
* What retention action should be taken for different customer segments?
* How can customer-level predictions be converted into business decisions?

The objective of this project is to build a system that answers these questions using data-driven methods.

---

## 💡 Solution

The platform provides a complete customer retention intelligence workflow.

### 1. Customer Analytics

Customer purchasing behavior is analyzed using:

* Recency
* Frequency
* Monetary value
* Order history
* Average order value
* Review behavior
* Delivery experience
* Payment behavior
* Geographic information

### 2. Churn Prediction

Machine learning is used to estimate customer churn risk based on engineered customer-level behavioral features.

The model produces a customer-level risk prediction that can be used to prioritize retention activities.

### 3. Explainable AI

Model predictions are interpreted to identify the factors contributing to customer risk.

This improves transparency and helps business users understand that the system is not simply producing a prediction — it is providing a reason behind the prediction.

### 4. Retention Recommendations

A rule-based recommendation engine converts customer behavior and risk information into actionable retention strategies.

Examples include:

* Re-engagement campaigns
* Personalized offers
* High-value customer retention
* Service recovery
* Delivery experience improvement
* Review-driven intervention

### 5. AI Business Intelligence

The final outputs transform analytical results into business-oriented insights, including:

* Customer risk analysis
* Customer explanations
* Executive summaries
* Business reports
* Retention opportunities

---

# 🏗️ Project Architecture

```text
                         ┌─────────────────────┐
                         │   Olist Dataset     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Data Quality        │
                         │ Assessment          │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Data Cleaning       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Exploratory         │
                         │ Data Analysis       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Feature Engineering │
                         │ & RFM Analysis      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │ Machine Learning    │
                         │ Churn Prediction    │
                         └──────────┬──────────┘
                                    │
                       ┌────────────┴────────────┐
                       ▼                         ▼
             ┌─────────────────┐       ┌────────────────────┐
             │ Explainable AI  │       │ Retention          │
             │ & Risk Drivers  │       │ Recommendations    │
             └────────┬────────┘       └─────────┬──────────┘
                      │                          │
                      └────────────┬─────────────┘
                                   ▼
                       ┌────────────────────────┐
                       │ AI Business            │
                       │ Intelligence           │
                       └────────────┬───────────┘
                                    │
                                    ▼
                       ┌────────────────────────┐
                       │ Streamlit Application   │
                       └────────────────────────┘
```

---

# 📊 Dataset

The project uses the **Brazilian E-Commerce Public Dataset by Olist**.

The dataset contains multiple interconnected tables covering the complete e-commerce transaction lifecycle.

### Main Tables

| Dataset     | Description                                        |
| ----------- | -------------------------------------------------- |
| Customers   | Customer information and location                  |
| Orders      | Order lifecycle and timestamps                     |
| Order Items | Products purchased within orders                   |
| Payments    | Payment methods and transaction values             |
| Products    | Product attributes                                 |
| Reviews     | Customer review scores and comments                |
| Sellers     | Seller information                                 |
| Geolocation | Brazilian ZIP-code geographic information          |
| Translation | Portuguese-to-English product category translation |

### Dataset Scale

The project works with approximately:

* **99K customers**
* **99K orders**
* **112K order items**
* **103K payment records**
* **33K products**
* **99K reviews**
* **3K sellers**
* **1M+ geolocation records**

---

# 🔎 Data Quality & Cleaning

Before analysis and modeling, the datasets were systematically assessed and cleaned.

The data quality process included:

* Missing value analysis
* Duplicate detection
* Data type validation
* Outlier analysis
* Invalid value detection
* Text standardization
* Duplicate removal
* Timestamp conversion
* Validation of cleaned datasets

A major cleaning operation was performed on the geolocation dataset, where duplicate records were identified and removed.

The project maintains separate **raw, cleaned, processed, and final** data layers.

---

# 📈 Exploratory Data Analysis

The EDA phase focuses on understanding customer and business behavior.

Key analytical areas include:

* Monthly revenue trends
* Monthly order trends
* Order status distribution
* Customer state analysis
* Payment type analysis
* Product price analysis
* Freight cost analysis
* Delivery time analysis
* Review score analysis
* Correlation analysis

### Example Business Findings

Some of the major findings from the analysis include:

* São Paulo represents the largest revenue-generating state.
* Revenue varies significantly across months and quarters.
* Credit cards represent the dominant payment method.
* Delivery experience and review behavior provide useful signals for customer analysis.
* Freight cost varies considerably across orders.
* Customer purchasing behavior can be transformed into meaningful retention features.

---

# 🧠 Feature Engineering

Customer-level features were created to transform transactional data into machine-learning-ready information.

Important features include:

### RFM Features

**Recency**

Measures how recently a customer made a purchase.

**Frequency**

Measures how frequently a customer purchases.

**Monetary**

Measures the amount spent by the customer.

These features provide a behavioral representation of customer value and engagement.

Additional customer-level features include:

* Total orders
* Total spending
* Average order value
* Average review score
* Delivery-related features
* Customer tenure
* Purchase activity indicators
* Behavioral risk indicators

---

# 🤖 Machine Learning

The machine learning pipeline focuses on customer churn prediction.

### Workflow

```text
Customer-Level Dataset
        ↓
Feature Selection
        ↓
Train/Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Comparison
        ↓
Model Interpretation
        ↓
Production Model
```

### Models

Multiple machine learning approaches were evaluated during the modeling phase, with the selected production model saved for application use.

The Streamlit application loads the serialized churn model from:

```text
10_Streamlit_Application/models/churn_model.pkl
```

### Model Evaluation

The project evaluates model performance using appropriate classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

Model performance comparison is documented within the machine learning phase.

---

# 🔍 Explainable AI

A prediction system should not only answer:

> "Will this customer churn?"

It should also help answer:

> "Why is this customer considered at risk?"

The project therefore includes an explainability layer that identifies important customer-level risk factors.

This allows business users to interpret model predictions and connect them with possible retention actions.

---

# 🎯 Retention Recommendation Engine

Predictions become more valuable when they lead to actionable decisions.

The recommendation engine uses customer behavior and risk information to generate retention strategies.

### Example Decision Framework

```text
Low Risk
   ↓
Maintain Engagement

Medium Risk
   ↓
Targeted Engagement

High Risk
   ↓
Immediate Retention Intervention

High-Value + High Risk
   ↓
Priority Retention Campaign
```

Recommendations are designed to support practical business actions rather than simply presenting machine-learning predictions.

---

# 🧠 AI Business Intelligence

The project contains a dedicated AI Business Intelligence layer that transforms analytical outputs into business-readable information.

It includes:

* Customer explanations
* Executive summaries
* Business reports
* Risk analysis
* Retention opportunities
* Learning documentation

The final outputs are stored under:

```text
data/final/
```

Including:

```text
ai_ready_dataset.csv
ai_customer_explanations.csv
executive_summary.csv
business_report_data.csv
```

---

# 🌐 Streamlit Application

The final solution is deployed as an interactive Streamlit web application.

## 🚀 Live Demo

**https://ai-powered-customer-retention-intelligence-platform-xbk5vzn4kd.streamlit.app/**

### Application Modules

The application contains four major areas:

### 📊 Dashboard

Provides an overview of customer retention and business intelligence metrics.

### 🎯 Customer Prediction

Allows customer-level churn risk analysis using the trained machine learning model.

### 🧠 AI Insights

Provides customer explanations and AI-powered business insights.

### 📑 Executive Report

Provides high-level business summaries and retention intelligence for decision-makers.

---

# 🗂️ Project Structure

```text
AI-Powered-Customer-Retention-Intelligence-Platform/
│
├── 01_Business_Understanding/
│   ├── Business problem
│   ├── Business objectives
│   ├── KPIs
│   └── Interview preparation
│
├── 02_Dataset_Understanding/
│   ├── Dataset overview
│   ├── Data dictionary
│   ├── Table relationships
│   └── Dataset limitations
│
├── 03_Data_Quality_Assessment/
│   ├── Missing values
│   ├── Duplicate analysis
│   ├── Data type validation
│   └── Outlier analysis
│
├── 04_Data_Cleaning/
│   ├── Data type conversion
│   ├── Missing value treatment
│   ├── Duplicate handling
│   ├── Invalid value handling
│   └── Text standardization
│
├── 05_EDA/
│   ├── EDA notebooks
│   ├── Business insights
│   └── Analytical reports
│
├── 06_Feature_Engineering/
│   ├── Feature creation
│   ├── Customer features
│   ├── RFM features
│   └── Target variable
│
├── 07_Machine_Learning/
│   ├── Model setup
│   ├── Model training
│   ├── Model evaluation
│   └── Model interpretation
│
├── 08_Retention_Recommendation/
│   ├── Recommendation logic
│   ├── Recommendation evaluation
│   └── Business impact
│
├── 09_AI_Business_Intelligence/
│   ├── AI setup
│   ├── Customer explanations
│   ├── Executive summary
│   └── Business report
│
├── 10_Streamlit_Application/
│   ├── app.py
│   ├── pages/
│   ├── components/
│   ├── config/
│   ├── utils/
│   ├── models/
│   ├── data/
│   ├── tests/
│   └── documentation/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── processed/
│   └── final/
│
├── src/
│   ├── data/
│   ├── analysis/
│   └── config/
│
├── tests/
│
├── charts/
│
├── notebooks/
│
├── reports/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🛠️ Technology Stack

### Programming & Analytics

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-learn
* XGBoost
* Imbalanced-learn

### Explainable AI

* SHAP

### Application

* Streamlit

### Database & SQL

* MySQL
* SQLAlchemy
* PyMySQL

### Development & Testing

* Jupyter Notebook
* Git
* GitHub
* Pytest
* Black
* Flake8

### Model Serialization

* Joblib

---

# ▶️ Run the Project Locally

## 1. Clone the repository

```bash
git clone https://github.com/Sowmyaraju04/AI-Powered-Customer-Retention-Intelligence-Platform.git
```

```bash
cd AI-Powered-Customer-Retention-Intelligence-Platform
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

```bash
venv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Streamlit application

```bash
streamlit run 10_Streamlit_Application/app.py
```

The application should open in your browser.

---

# 🧪 Testing

The project contains automated tests covering important components of the data and application pipeline.

Testing areas include:

* Data loading
* Data validation
* Data profiling
* Data cleaning
* EDA loading
* Prediction logic
* Recommendation logic

Run the tests with:

```bash
pytest
```

---

# 📌 Key Business Value

This platform demonstrates how organizations can move from:

```text
Raw Data
    ↓
Descriptive Analytics
    ↓
Predictive Analytics
    ↓
Explainable Predictions
    ↓
Prescriptive Recommendations
    ↓
Business Action
```

Instead of treating churn prediction as an isolated machine-learning exercise, the project connects the entire workflow to business decision-making.

---

# 💼 Skills Demonstrated

This project demonstrates practical experience across multiple areas:

### Data Analytics

* Data exploration
* KPI analysis
* Business insight generation
* Customer behavior analysis

### Data Engineering

* Data ingestion
* Data cleaning
* Data validation
* Multi-table data integration

### Machine Learning

* Feature engineering
* Classification
* Model comparison
* Model evaluation
* Model interpretation

### AI & Decision Intelligence

* Explainable AI
* Customer risk analysis
* Recommendation systems
* AI-generated business insights

### Application Development

* Streamlit
* Modular Python architecture
* Model deployment
* Interactive analytics

### Software Engineering

* Project structure
* Configuration management
* Testing
* Git/GitHub
* Documentation

---

# ⚠️ Limitations

This project is based on a historical public e-commerce dataset and therefore has several limitations.

* The dataset represents historical customer behavior rather than live production data.
* The churn definition is derived from available transactional behavior and should be validated against a company's actual business definition.
* Retention recommendations are rule-based rather than automatically optimized through experimentation.
* Model performance depends on the available features and historical data.
* Business impact estimates should be validated through controlled experiments such as A/B testing before production implementation.

---

# 🔮 Future Improvements

Potential future enhancements include:

* Real-time customer scoring
* Automated model retraining
* Customer lifetime value prediction
* Advanced customer segmentation
* A/B testing framework for retention campaigns
* Campaign response prediction
* Real-time business alerts
* Cloud-based data pipelines
* Model monitoring and drift detection
* LLM-powered natural-language business querying
* Integration with CRM and marketing platforms

---

# 📚 Project Documentation

Detailed documentation is available throughout the project folders, covering:

* Business understanding
* Dataset understanding
* Data quality
* Data cleaning
* EDA
* Feature engineering
* Machine learning
* Retention recommendations
* AI business intelligence
* Streamlit architecture
* Data flow
* User journey
* Application requirements

---

# 👩‍💻 Author

**Sowmya P**

Aspiring Data Analyst | Data Science & AI Enthusiast

GitHub:
https://github.com/Sowmyaraju04

---

## ⭐ Project Highlight

> **An end-to-end customer retention intelligence platform that combines analytics, machine learning, explainable AI, and actionable retention recommendations in a deployable web application.**

If you find the project useful, consider giving the repository a ⭐ on GitHub.
