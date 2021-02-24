from sqlalchemy import Column, ForeignKey, Integer, DateTime, Float, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.database import Base

class MeasuresType(Base):
  __tablename__ = 'measures_type'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String(20), index=True, nullable=False)
  
  #              relationship('model_class_name', back_populates='tablename')
  measurements_t = relationship('Measurements', back_populates='measures_type')

class Measurements(Base):
  __tablename__ = 'measurements'

  id = Column(Integer, primary_key=True, index=True)
  # owner_id = Column(Integer, ForeignKey('Users.id'), index=True, nullable=False)
  type_id = Column(Integer, ForeignKey('measures_type.id'), nullable=False)
  value = Column(Float, index=True, nullable=False)
  tag = Column(String(20), index=True)
  created_at = Column(DateTime(timezone=True), index=True, default=func.now())
  update_at = Column(DateTime, index=True)
  deleted_at = Column(DateTime, index=True)

  # owner = relationship('Users', back_populates='measurements')
  measures_type = relationship('MeasuresType', back_populates='measurements_t')
