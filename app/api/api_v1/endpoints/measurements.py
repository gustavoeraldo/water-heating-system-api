import typing
from app.exceptions.measureExceptions import MeasureExceptions
from sqlalchemy.sql.schema import MetaData
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from app.schemas.measurementsSchema import MeasurementsBase
from app.schemas.measuresTypes import MeasurementsTypeBase
from app.db.database import engine
from app import models
from app.db.deps import get_db
from app.controllers.measurementsController import MeasuresController

metada = MetaData()

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get('/')
async def read_measurements():
  """
  Return all measurements.
  """

  return [
    {
      "id": 1,
      "value": 15.5,
      "timestamp": "2021-12-24 23:12:00"
    }
  ]


@router.post('/')
async def add_measurement(
  measure_in: MeasurementsBase, db: Session = Depends(get_db)
  )->MeasurementsBase:

  new_measurement = MeasuresController.create_measurements(db, measure_in)

  if not new_measurement:
    raise HTTPException(
      status_code = 400,
      detail = 'Something went wrong!'
    )
  return new_measurement


# Endpoints for MEASUREMENTS TYPE
@router.post('/create-measure-type')
async def add_measure_type(
  measure_type: MeasurementsTypeBase, db: Session = Depends(get_db)):
  new_measure_type = MeasuresController.create_measure_type(measure_type.name.lower(), db)

  return new_measure_type

@router.get('/read-measure-types')
async def read_measure_types(db: Session = Depends(get_db)):
  try:
    measure_type = MeasuresController.get_measure_types(db)
  except Exception as e:
    raise HTTPException(
      status_code = 500,
      detail = f'{e}'
    )

  return measure_type