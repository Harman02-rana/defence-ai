from pydantic import BaseModel

class SoldierData(BaseModel):
    fatigue: float
    sleep: float
    stress: float
    mission_intensity: float
