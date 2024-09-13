# Student Performance Prediction Machine Learning Model
This project aims to predict student exam scores based on various performance factors. I utilized Snowflake for data storage and initial processing, and Databricks for advanced data processing, feature engineering, and machine learning.

https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/327639136237466/3288242259835538/6002370388471942/latest.html

## Project Overview

The goal of this project is to analyze various factors affecting student performance and build a predictive model to estimate exam scores. The project is divided into the following stages:

1. **Data Loading and Storage**
2. **Initial Data Processing**
3. **Data Retrieval and Advanced Processing**
4. **Model Training and Evaluation**

## 1. Data Loading and Storage

**Snowflake** is used as the data storage and querying platform. The "Student Performance Factors" dataset is loaded into Snowflake for efficient data management. Encoded columns are added to the dataset to facilitate further analysis.
<img width="356" alt="image" src="https://github.com/user-attachments/assets/c5fc4406-41b1-4a94-b0c7-5dd8e0ccab57">

## 2. Initial Data Processing

Initial data cleaning and encoding of categorical variables are performed directly in Snowflake using SQL queries. This step ensures that the data is in a suitable format for advanced processing.

## 3. Data Retrieval and Advanced Processing

**Databricks** is used for advanced data processing and feature engineering. The processed data is retrieved from Snowflake and further processed in Databricks. This includes normalization of numerical features and the creation of new features such as total study time.

<img width="354" alt="image" src="https://github.com/user-attachments/assets/4fce13eb-4465-400c-b778-6c49ce1c700d">


## 4. Model Training and Evaluation

A Random Forest Regressor is used to predict exam scores based on the processed features. The model is trained and evaluated to assess its performance, with metrics such as Mean Squared Error used to measure accuracy.

<img width="317" alt="image" src="https://github.com/user-attachments/assets/59ce468a-2c60-420d-8bab-440264d1081b">


## Conclusion

This project showcases the integration of Snowflake and Databricks for a comprehensive data analysis and machine learning pipeline. Snowflake is used for data storage and initial processing, while Databricks is leveraged for advanced processing, feature engineering, and model training.
