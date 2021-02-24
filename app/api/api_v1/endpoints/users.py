from fastapi import APIRouter

from app.controllers.usersController import UsersController

router = APIRouter()

@router.get('/info')
async def read_user_info():
  """
  Return the user info.
  """

  return [
    {
      "id": 1,
      "name": "Some LMI student",
      "measurements_types": ["temperature", "capacitance", "inductance"]
    }
  ]


@router.get('/')
async def get_all_users():
  """
  Return all users
  """

  db_user = UsersController.get_all_users()
  
  return db_user