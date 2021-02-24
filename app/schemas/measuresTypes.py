from pydantic import BaseModel

class MeasurementsTypeBase(BaseModel):
  name: str

  class Config:
    schema_extra = {
      "example": {
        "name": "voltage"
      }
    }

class MeasureTypeInDB(MeasurementsTypeBase):
  id: int