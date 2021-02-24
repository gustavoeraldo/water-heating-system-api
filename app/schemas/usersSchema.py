from pydantic import BaseModel

class UserBase(BaseModel):
  username: str


class UserInDB(UserBase):
  id: int
  user_type: int
