from typing import Optional, List
from sqlalchemy.orm import Session

from app.schemas.usersSchema import UserBase
from app.models.usersModel import Users
from app.exceptions.userExceptions import UserExceptions

class UsersController(Users):
  def create_user(db: Session, user_in: UserBase)->UserBase:
    try:
      db_user = Users(
        username = user_in.username,
      )
    except:
      raise UserExceptions(404, 'Insert error') 

    return db_user


  def get_all_users():
    return {'message': 'Return all users'}

  
  def get_user():
    return {'message': 'user info'}


  def delete_user():
    return {'message': 'user aws successfully deleted'}

  
  def update_user():
    return {'message': 'user was successfully updated'}
