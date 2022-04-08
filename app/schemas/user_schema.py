from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str
    nickname: str
    is_active: str

class User(UserBase):

    class Config:
        orm_mode = True