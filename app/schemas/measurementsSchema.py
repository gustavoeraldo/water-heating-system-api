from typing import Optional, List
from pydantic import BaseModel

class MeasurementsBase(BaseModel):
  value: float
  timestamp: str
  measurement_type: str


class MeasurementsInDB(MeasurementsBase):
  id: int
  owner_id: int