from fastapi import APIRouter

from app.schemas.measurementsSchema import MeasurementsBase # Use this for localhost
# from schemas.measurementsSchema import MeasurementsBase # Use this for deployment

router = APIRouter()

@router.get('/')
async def read_measurements():
  """
  Return all measurements.(maybe from all sensors)
  """

  return [
    {
      "id": 1,
      "value": 15.5,
      "timestamp": "2021-12-24 23:12:00"
    }
  ]


@router.post('/')
async def add_measurement(measure: MeasurementsBase):

  return {
    "measure": measure
  }