from fastapi import FastAPI
from predict import router as predict_router

app = FastAPI(title="Loan Risk Prediction API")

app.include_router(predict_router)

@app.get("/")
def home():
    try:
        return {"message": "Loan Risk API is running"}
    except Exception as e:
        return {"error": str(e)}
