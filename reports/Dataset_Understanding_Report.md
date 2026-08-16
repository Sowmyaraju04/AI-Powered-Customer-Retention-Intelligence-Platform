---

## Enterprise Data Dictionary

An enterprise data dictionary was created to document the business purpose, keys, granularity, and analytical relevance of each dataset.

This document serves as the foundation for understanding relationships between datasets and supports future data integration, feature engineering, and customer-level analytical modeling.

---

## Table Relationships

The relationships between the Olist dataset tables were documented to establish a clear understanding of how customer, order, payment, product, seller, and review data are connected.

This relationship mapping will guide SQL joins, Python merges, customer-level aggregation, and feature engineering in subsequent phases.


---

## Entity Relationship Model

An Entity Relationship (ER) model was created to document how the Olist dataset tables are connected.

The ER model serves as the architectural blueprint for SQL joins, Python data integration, customer-level feature engineering, and downstream machine learning workflows.


---

## Table Granularity

The granularity of each table was documented to identify the level of detail represented by individual records.

Understanding table granularity is critical for designing accurate SQL joins, Python merges, customer-level aggregation, and machine learning datasets while preventing duplicate records and inflated business metrics.


---

## Business Use of Each Table

Each dataset was evaluated based on its business contribution to the customer retention problem.

This assessment identified how individual tables support customer analytics, feature engineering, machine learning, and executive reporting, ensuring that only relevant information is incorporated into the final analytical solution.


---

## Dataset Limitations

The limitations of the Olist dataset were documented to ensure that assumptions, risks, and analytical constraints are transparent throughout the project.

Recognizing these limitations helps define realistic expectations for feature engineering, churn modeling, and business recommendations while improving the credibility of the final solution.


---

# Conclusion

The Dataset Understanding phase successfully documented the business context, relational structure, analytical potential, and limitations of the Brazilian Olist E-Commerce Dataset.

This phase established a strong foundation for subsequent activities, including Data Quality Assessment, Data Cleaning, Customer-Level Data Mart creation, Feature Engineering, and Machine Learning.

By thoroughly understanding the available data before performing transformations, the project reduces analytical risk and ensures that future business insights and predictive models are built on reliable foundations.