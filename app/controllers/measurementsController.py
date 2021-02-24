from typing import Optional, List
from sqlalchemy.orm import Session

from app.schemas.measurementsSchema import MeasurementsBase
from app.schemas.measuresTypes import MeasurementsTypeBase, MeasureTypeInDB
from app.models.measurementsModel import Measurements, MeasuresType
from app.exceptions.measureExceptions import MeasureExceptions
from .base import ControllerBase

class MeasurementsController(ControllerBase[Measurements]):
  def create_measurements(self, db:Session, measure_in:MeasurementsBase):
    db_measurement = Measurements(
      type_id = measure_in.type_id,
      value = measure_in.value,
      tag = measure_in.tag
    )

    db.add(db_measurement)
    db.commit()
    db.refresh(db_measurement)
    
    return db_measurement


  def get_measurements(
    self, time_stamp: Optional[str], measument_type: Optional[str]
    )->List[MeasurementsBase]:
    """
    Remember to build filters:
    timestamp
    value
    measurement type
    """

    return [
      {
        "id": 1,
        "value": 45.65,
        "timestamp": "some timestamp",
        "measurement_type": "temperature"
      }
    ]


  def delete_measurements(measurement_id: int):
    return 'measurement deleted'

  
  def update_measurements(measurement_id: int):
    return 'measurement updated'


  # Methods for MEASUREMENT TYPES management
  def create_measure_type(self, measure_t: str, db: Session):
    verif_type = self.get_type(measure_t, db)

    if verif_type:
      raise MeasureExceptions(400, 'Measurement Type already exists.')

    db_measure_type = MeasuresType(
      name = measure_t
    )
    try:
      db.add(db_measure_type)
      db.commit()
      db.refresh(db_measure_type)
    except Exception as e:
      raise MeasureExceptions(400, f'Error trying to insert data in database! {e}')

    return db_measure_type


  def get_measure_types(self, db: Session)->List[MeasureTypeInDB]:
    return db.query(MeasuresType).order_by(MeasuresType.name).all()


  def get_type(self, m_type: str, db: Session)->MeasurementsTypeBase:
    return db.query(MeasuresType).filter(MeasuresType.name == m_type).first()

MeasuresController = MeasurementsController(Measurements)
