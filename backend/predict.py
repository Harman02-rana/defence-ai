from fastapi import APIRouter
from schemas.request import PredictRequest
from services.model_service import predict_threat

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/")
def predict(data: PredictRequest):
    result = predict_threat(data.features)
    return {"prediction": result}
