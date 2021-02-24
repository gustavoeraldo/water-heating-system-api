from pydantic import BaseModel
from typing import Optional

class MeasurementsBase(BaseModel):
  value: float
  created_at: Optional[str]
  type_id: int
  tag: str

  class Config:
    schema_extra = {
      "example":{
        "value": 75.6,
        "type_id": 3,
        "tag": "sensor 1"
      }
    }


class MeasurementsInDB(MeasurementsBase):
  id: int
  # owner_id: int
  deleted_at: str
  updated_at: str
