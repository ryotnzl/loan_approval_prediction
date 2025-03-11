from fastapi import APIRouter
from backend.model import get_model
from backend.schemas import LoanApplicant
import numpy as np
import pandas as pd

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/")
def predict_risk(applicant: LoanApplicant):
    model = get_model()  # Load the trained model

    # Convert input into DataFrame format (assuming model expects this)
    input_data = pd.DataFrame([applicant.dict()])

    try:
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]  # Probability of risk_flag=1
        return {"risk_flag": int(prediction), "probability": float(probability)}
    except Exception as e:
        return {"error": str(e)}
