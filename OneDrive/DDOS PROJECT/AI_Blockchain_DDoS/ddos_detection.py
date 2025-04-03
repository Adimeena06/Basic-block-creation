import pandas as pd
import joblib

def load_model():
    return joblib.load("ddos_model.pkl")

def predict_ddos(features):
    model = load_model()
    df = pd.DataFrame([features])
    return model.predict(df)[0]
