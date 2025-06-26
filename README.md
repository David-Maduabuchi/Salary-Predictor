# 📌 Salary Prediction using Machine Learning

> A regression-based ML web application that predicts employee salary based on years of experience. Built with scikit-learn, Streamlit, and structured following MLOps principles.

## 🧠 Abstract

This project is a lightweight yet production-ready machine learning pipeline that estimates salary based on years of experience using historical data. It demonstrates the end-to-end process of data cleaning, model training, evaluation, packaging, and deployment via an interactive Streamlit dashboard.

The goal was to transition from traditional notebooks to modular, scalable, and maintainable ML code, while integrating best practices from software engineering and data science.

## 📂 Project Structure

├── data/
│ └── salary.csv
├── notebooks/
│ └── PricePredictionModel.ipynb
├── src/
│ ├── train_model.py
│ └── predict.py
├── app.py
├── requirements.txt
├── model.pkl # Serialized model
├── README.md
└── .gitignore

## 🔍 Problem Statement

Companies and HR teams often estimate compensation subjectively, leading to inconsistencies. We aim to build a data-driven tool that can:

- Predict salary from years of experience
- Enable HR teams and professionals to make informed decisions
- Serve as a deployable proof of concept for regression models in production

## 🎯 Objective

- Collect and preprocess regression data
- Train and evaluate a Linear Regression model
- Save model alongside metadata for reuse
- Build a clean, interactive Streamlit dashboard for prediction
- Make the project GitHub-ready and deployable

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.10 |
| ML Framework | scikit-learn |
| Data Wrangling | pandas |
| Visualization | matplotlib |
| Deployment UI | Streamlit |
| Serialization | joblib |
| Virtual Env | `venv` |
| Version Control | Git + GitHub |

## 📊 Dataset Description

A small CSV dataset containing:

| Column | Description |
|--------|-------------|
| `years_of_experience` | Numeric input, e.g., `5` |
| `salary` | Target label in dollars, e.g., `3500` |