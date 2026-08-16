# Interview Preparation

## Question 1

Why did you build this project?

### Answer

I wanted to move beyond descriptive analytics by developing an end-to-end AI solution that predicts customer churn, explains model decisions, and recommends business actions. The project demonstrates data engineering, machine learning, explainable AI, business intelligence, and product thinking in a single enterprise workflow.

---

## Question 2

Why is customer retention important?

### Answer

Retaining existing customers is generally more cost-effective than acquiring new ones. Higher retention improves customer lifetime value, stabilizes revenue, and increases long-term profitability.

---

## Question 3

Why is explainable AI important?

### Answer

Business stakeholders need to understand why customers are predicted to churn before acting on the predictions. Explainable AI increases transparency, trust, and adoption by highlighting the key factors influencing each prediction.



---

# Phase 2 – Dataset Understanding

## Question 1

### Why is dataset understanding important before data cleaning?

**Answer:**

Dataset understanding helps identify the business purpose, structure, relationships, and granularity of the data before transformations are performed. It reduces the risk of incorrect joins, duplicate records, and misleading analyses.

---

## Question 2

### What is table granularity?

**Answer:**

Table granularity defines what a single row represents in a dataset. Understanding granularity is essential because different tables may represent customers, orders, products, or payments, and incorrect joins across different granularities can lead to duplicated records and inaccurate business metrics.

---

## Question 3

### Why shouldn't transactional tables be directly used for machine learning?

**Answer:**

Transactional tables contain multiple records for the same customer. Machine learning models require one observation per entity, so transactional data must first be aggregated into a customer-level analytical dataset.

---

## Question 4

### What is the purpose of an Entity Relationship Diagram?

**Answer:**

An ER diagram visually represents how tables are connected through primary and foreign keys. It serves as a blueprint for SQL joins, Python data integration, and feature engineering.

---

## Question 5

### What are the main limitations of the Olist dataset?

**Answer:**

The dataset does not contain an explicit churn label, customer demographics, marketing campaign data, or website browsing behaviour. These limitations require business assumptions and careful feature engineering to build an effective churn prediction model.