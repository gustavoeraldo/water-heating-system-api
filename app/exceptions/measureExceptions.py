from fastapi import HTTPException

class MeasureExceptions(HTTPException):
  def __init__(self, status_code, message):
    self.status_code = status_code
    self.message = message

    super().__init(status_code=self.status_code, detail=self.message)
