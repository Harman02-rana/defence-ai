from pydantic import BaseModel

class ThreatInput(BaseModel):
    distance_km: float
    speed_kmph: float
    altitude_m: float
    radar_cross_section: float
    heat_signature: float
    signal_jamming: int
    object_size: float
    time_of_day: int
