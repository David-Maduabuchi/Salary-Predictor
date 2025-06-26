# 📌 Salary Prediction using Machine Learning

> A regression-based ML web application that predicts employee salary based on years of experience. Built with scikit-learn, Streamlit, and structured following MLOps principles.

## 🧠 Abstract

This project is a lightweight yet production-ready machine learning pipeline that estimates salary based on years of experience using historical data. It demonstrates the end-to-end process of data cleaning, model training, evaluation, packaging, and deployment via an interactive Streamlit dashboard.

The goal was to transition from traditional notebooks to modular, scalable, and maintainable ML code, while integrating best practices from software engineering and data science.

## 📂 Project Structure

```bash
.
├── data/
│   └── salary.csv                  # Raw input data
├── notebooks/
│   └── PricePredictionModel.ipynb  # Initial exploration & prototyping
├── src/
│   ├── train_model.py              # Trains and saves the regression model
│   └── predict.py                  # Loads model and makes predictions
├── app.py                          # Streamlit dashboard entry point
├── requirements.txt                # Python dependencies
├── model.pkl                       # Serialized trained model
├── README.md                       # Project documentation
└── .gitignore                      # Ignored files and folders
```

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

## 🚀 How to Run the Project

Follow these steps to set up and launch the application locally:

```bash
# 1. Clone the Repository
git clone https://github.com/your-username/salary-prediction-app.git
cd salary-prediction-app

# 2. Create a Virtual Environment (Optional but Recommended)
# Windows
python -m venv venv
venv\Scripts\activate
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Train the Model
python src/train_model.py
# This will generate `model.pkl` (your serialized trained model)

# 5. Run the Streamlit App
streamlit run app.py
# Visit http://localhost:8501 in your browser to use the interactive dashboard
