from fastapi import APIRouter

router = APIRouter()

@router.post("/predict")
def predict(data: dict):
    return {"result": "ok"}
