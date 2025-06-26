# src/train_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load data
df = pd.read_csv("data/salaries.csv")

# Feature and target split
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# 🔥 Split into training and testing sets (80/20 by default)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Train model on training set
model = LinearRegression()
model.fit(X_train, y_train)

#  Evaluate on test set
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📉 Test MSE: {mse:.2f}")
print(f"📈 Test R²: {r2:.2f}")

# Save both model and features
joblib.dump({"model": model, "features": X.columns.tolist()}, "model.pkl")

print("Model saved as model.pkl with feature names.")
