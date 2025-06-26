import joblib
import pandas as pd


def predict_price(data_to_be_predicted):
    bundle = joblib.load("model.pkl")
    model = bundle["model"]
    feature_names = bundle["features"]

    # create input dataFrame based on saved feature names
    input_df  =  pd.DataFrame([data_to_be_predicted], columns=feature_names)

    prediction = model.predict(input_df)
    return prediction[0]