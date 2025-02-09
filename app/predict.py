from fastapi import APIRouter, Depends
from model import get_model
from schemas import LoanApplicant
import numpy as np

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/")
def predict_risk(applicant: LoanApplicant):
    model = get_model()  # Load model dynamically if not loaded
    data = np.array([[applicant.feature1, applicant.feature2, applicant.feature3]])
    
    try:
        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0][1]  # Probability of risk_flag=1
        return {"risk_flag": int(prediction), "probability": float(probability)}
    except Exception as e:
        return {"error": str(e)}
