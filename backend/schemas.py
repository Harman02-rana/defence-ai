from pydantic import BaseModel

class SoldierData(BaseModel):
    heart_rate: int
    stress_level: int
    sleep_hours: int
    fatigue_level: int
    age: int
    blood_pressure: int
    oxygen_level: int
    daily_steps: int
