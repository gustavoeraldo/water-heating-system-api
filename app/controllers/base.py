from typing import Generic, Type, TypeVar
# from pydantic import BaseModel

from app.db.baseClass import Base

ModelType = TypeVar('ModelType', bound=Base)
# CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
# Update = TypeVar('Update', bound=BaseModel)

class ControllerBase(Generic[ModelType]):
  def __init__(self, model: Type[ModelType]):
    '''
    CRUD object with default methods to Create, Read, Update, Delete (CRUD).
    **Parameters**
    * `model`: A SQLAlchemy model class
    * `schema`: A Pydantic model (schema) class
    '''

    self.model = model
