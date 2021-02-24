from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base

class Users(Base):
  __tablename__ = 'users_t'

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String(20), index=True, nullable=False)
  # user_type = Column(Integer, ForeignKey('UserType.id'), nullable=False, index=True)
  hashed_password = Column(String)

  # measures = relationship('Measurements', back_populates='owner')
  # u_type = relationship('UserType', backref='user_type')

class UserType(Base):
  __tablename__ = 'user_type'

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
