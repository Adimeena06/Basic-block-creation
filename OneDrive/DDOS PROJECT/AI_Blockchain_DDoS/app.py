import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the trained model
try:
    with open("ddos_model.pkl", "rb") as f:
        model = pickle.load(f)

    if not hasattr(model, "predict"):
        raise ValueError("Model does NOT have a 'predict' function!")

    print("✅ Model loaded successfully!")

except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

@app.route('/')
def home():
    return "Welcome to the DDoS Detection System\nUse the API to make predictions."

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not loaded correctly"}), 500

    try:
        data = request.get_json()
        features = np.array(data["features"])
        prediction = model.predict(features).tolist()
        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
