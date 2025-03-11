import joblib
from pathlib import Path

# Define the path to the model
MODEL_PATH = Path("models/final_model.pkl")

def load_model():
    """Loads the trained machine learning model."""
    return joblib.load(MODEL_PATH)

# Lazy loading for efficiency
model = None

def get_model():
    """Get the loaded model, load if not already loaded."""
    global model
    if model is None:
        model = load_model()
    return model
