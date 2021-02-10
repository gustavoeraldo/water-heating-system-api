from fastapi import APIRouter

router = APIRouter()

@router.get('/')
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