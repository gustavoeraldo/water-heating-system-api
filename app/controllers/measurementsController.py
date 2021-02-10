from typing import Optional, List

from app.schemas.measurementsSchema import MeasurementsBase 

class MeasurementsController():
  def add_measurements(measure:MeasurementsBase):
    return 'user created!'


  def get_measurements(
    time_stamp: Optional[str], measument_type: Optional[str]
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