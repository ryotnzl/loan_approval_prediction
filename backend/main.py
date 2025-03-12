from fastapi import FastAPI
from backend.predict import router as predict_router
import catboost

app = FastAPI(title="Loan Risk Prediction API")

# Include the prediction router
app.include_router(predict_router)

@app.get("/")
def home():
    return {"message": "Loan Risk API is running"}
