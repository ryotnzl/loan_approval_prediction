import joblib

MODEL_PATH = "models/final_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

model = None  # Initialize model as None

def get_model():
    global model
    if model is None:
        model = load_model()
    return model
